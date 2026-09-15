#!/usr/bin/env python3
"""Read-only DOCX inventory. XML locators are not rendered page numbers."""

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import BadZipFile, ZipFile

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
W_STRICT = "{http://purl.oclc.org/ooxml/wordprocessingml/main}"
R = "{http://schemas.openxmlformats.org/package/2006/relationships}"
PART = re.compile(r"word/(?:document|header\d+|footer\d+|footnotes|endnotes|comments)\.xml$")
MAX_TOTAL = 80 * 1024 * 1024


def text_of(element, deleted=False, inserted=True):
    out = []
    def walk(node):
        if node.tag in (W + "del", W + "moveFrom") and not deleted:
            return
        if node.tag in (W + "ins", W + "moveTo") and not inserted:
            return
        if node.tag in (W + "t", W + "delText"):
            out.append(node.text or "")
        elif node.tag == W + "tab":
            out.append("\t")
        elif node.tag in (W + "br", W + "cr"):
            out.append("\n")
        else:
            for child in node:
                walk(child)
    walk(element)
    return "".join(out)


def normalize_word_namespace(root, name):
    """Normalize a parsed Strict part in memory; never change the source archive."""
    namespace = root.tag.split("}", 1)[0] + "}" if root.tag.startswith("{") else ""
    if namespace not in (W, W_STRICT):
        raise ValueError(f"Nicht lesbarer Word-Namensraum in {name}: {namespace or '(ohne Namensraum)'}")
    if name == "word/document.xml" and root.tag != namespace + "document":
        raise ValueError("Keine lesbare DOCX: word/document.xml enthält kein Word-Dokument")
    for node in root.iter():
        if node.tag.startswith(W_STRICT):
            node.tag = W + node.tag[len(W_STRICT):]
        for key in list(node.attrib):
            if key.startswith(W_STRICT):
                node.set(W + key[len(W_STRICT):], node.attrib.pop(key))
    return namespace[1:-1]


def ancestor(node, tag, parents):
    current = parents.get(node)
    while current is not None:
        if current.tag == tag:
            return current
        current = parents.get(current)
    return None


def inventory(path, vorlage=False):
    result = {"datei": str(Path(path)), "fundorte": "XML-Absätze; keine Seitenzahlen",
              "teile": [], "externe_beziehungen": [], "lesegrenzen": [], "vorlagenhinweise": []}
    with ZipFile(path) as archive:
        if "word/document.xml" not in archive.namelist():
            raise ValueError("Keine lesbare DOCX: word/document.xml fehlt")
        if sum(info.file_size for info in archive.infolist()) > MAX_TOTAL:
            raise ValueError("DOCX entpackt größer als 80 MiB; gesonderte Aufnahme erforderlich")
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError("Mehrdeutiges DOCX mit doppelten Archivpfaden")
        for name in names:
            if name.startswith("word/media/") or name.startswith("word/embeddings/"):
                result["lesegrenzen"].append({"teil": name, "grund": "Bild oder eingebetteter Inhalt nicht textuell ausgewertet"})
            if name.endswith(".rels"):
                rels = ET.fromstring(archive.read(name))
                for rel in rels:
                    if rel.get("TargetMode") == "External":
                        result["externe_beziehungen"].append({"teil": name, "ziel": rel.get("Target"),
                                                             "gelesen": False})
            if not PART.fullmatch(name):
                continue
            root = ET.fromstring(archive.read(name))
            source_namespace = normalize_word_namespace(root, name)
            parents = {child: parent for parent in root.iter() for child in parent}
            table_ids = {table: i for i, table in enumerate(root.iter(W + "tbl"), 1)}
            # Count owned descendants through SDT/custom-XML wrappers, excluding nested tables.
            row_numbers, cell_numbers, row_counts, cell_counts = {}, {}, {}, {}
            for row in root.iter(W + "tr"):
                table = ancestor(row, W + "tbl", parents)
                if table is not None:
                    row_counts[table] = row_counts.get(table, 0) + 1
                    row_numbers[row] = row_counts[table]
            for cell in root.iter(W + "tc"):
                row = ancestor(cell, W + "tr", parents)
                if row in row_numbers:
                    cell_counts[row] = cell_counts.get(row, 0) + 1
                    cell_numbers[cell] = cell_counts[row]
            structure_revisions, revisions_by_owner = [], {}
            for owner, number in list(row_numbers.items()) + list(cell_numbers.items()):
                is_row = owner.tag == W + "tr"
                row = owner if is_row else ancestor(owner, W + "tr", parents)
                table = ancestor(row, W + "tbl", parents)
                locator = f"{name}#tbl{table_ids[table]}/r{row_numbers[row]}"
                if not is_row:
                    locator += f"/c{number}"
                properties = owner.find(W + ("trPr" if is_row else "tcPr"))
                revision_tags = ({"ins": "zeile_eingefuegt", "del": "zeile_geloescht"} if is_row else
                                 {"cellIns": "zelle_eingefuegt", "cellDel": "zelle_geloescht", "cellMerge": "zelle_zusammengefuehrt"})
                for node in properties if properties is not None else ():
                    local = node.tag[len(W):] if node.tag.startswith(W) else ""
                    if local not in revision_tags:
                        continue
                    revision = {"fundort": locator, "typ": revision_tags[local],
                                "id": node.get(W + "id"), "autor": node.get(W + "author"),
                                "datum": node.get(W + "date"), "status": "offen",
                                "attribute": dict(node.attrib)}
                    structure_revisions.append(revision)
                    revisions_by_owner.setdefault(owner, []).append(revision)
            if structure_revisions:
                result["lesegrenzen"].append({"teil": name, "grund":
                    "Tabellen-/Zellrevisionen sind inventarisiert, aber nicht angenommen oder verworfen. "
                    "Textfassungen berücksichtigen nur Textrevisionen; Strukturstatus gesondert prüfen. "
                    "Eine Zeilenrevision legt den Revisionsstatus ihrer Zellinhalte nicht automatisch fest."})
            absatzliste = []
            for i, paragraph in enumerate(root.iter(W + "p"), 1):
                ancestors = []
                current = parents.get(paragraph)
                while current is not None:
                    ancestors.append(current)
                    current = parents.get(current)
                # Text boxes have their own paragraphs: don't silently double count them.
                rendered = ET.fromstring(ET.tostring(paragraph))
                for textbox in list(rendered.iter(W + "txbxContent")):
                    textbox.clear()
                table = next((a for a in ancestors if a.tag == W + "tbl"), None)
                cell = next((a for a in ancestors if a.tag == W + "tc"), None)
                row = next((a for a in ancestors if a.tag == W + "tr"), None)
                item = {"fundort": f"{name}#p{i}", "text_mit_einfuegungen": text_of(rendered),
                        "tabelle": table_ids.get(table), "textfeld": any(a.tag == W + "txbxContent" for a in ancestors)}
                deleted_ancestor = any(a.tag in (W + "del", W + "moveFrom") for a in ancestors)
                inserted_ancestor = any(a.tag in (W + "ins", W + "moveTo") for a in ancestors)
                item["text_vor_offenen_aenderungen"] = "" if inserted_ancestor else text_of(rendered, deleted=True, inserted=False)
                item["absatz_geloescht"] = deleted_ancestor
                item["absatz_eingefuegt"] = inserted_ancestor
                if deleted_ancestor:
                    item["text_mit_einfuegungen"] = ""
                item["strukturrevisionen"] = [revision for owner in ancestors
                                               for revision in revisions_by_owner.get(owner, ())]
                item["strukturstatus_offen"] = bool(item["strukturrevisionen"])
                for flag in ("zeile_eingefuegt", "zeile_geloescht", "zelle_eingefuegt", "zelle_geloescht"):
                    item[flag] = any(revision["typ"] == flag for revision in item["strukturrevisionen"])
                if table is not None and row is not None and cell is not None:
                    item.update({"zeile": row_numbers[row], "zelle": cell_numbers[cell]})
                note = next((a for a in ancestors if a.tag in (W + "comment", W + "footnote", W + "endnote")), None)
                if note is not None:
                    item["notiz_id"] = note.get(W + "id")
                for tag, label in (("ins", "einfuegungen"), ("del", "loeschungen")):
                    item[label] = [{"text": text_of(n, deleted=True), "autor": n.get(W + "author"),
                                    "datum": n.get(W + "date")} for n in paragraph.iter(W + tag)]
                item["kommentar_ids"] = [n.get(W + "id") for n in paragraph.iter(W + "commentReference")]
                item["felder"] = [n.text for n in paragraph.iter(W + "instrText")]
                item["felder"] += [n.get(W + "instr") for n in paragraph.iter(W + "fldSimple")]
                item["ausgeblendete_texte"] = [text_of(n, deleted=True) for n in paragraph.iter(W + "r")
                                                if n.find("./" + W + "rPr/" + W + "vanish") is not None]
                absatzliste.append(item)
            for node in root.iter():
                if node.tag == W + "altChunk":
                    result["lesegrenzen"].append({"teil": name, "grund": "altChunk-Inhalt nicht ausgewertet"})
            result["teile"].append({"teil": name, "word_namensraum": source_namespace,
                                    "absaetze": absatzliste, "strukturrevisionen": structure_revisions})
        if vorlage:
            paragraphs = [p for part in result["teile"] if part["teil"] != "word/comments.xml" for p in part["absaetze"]]
            main = next(part for part in result["teile"] if part["teil"] == "word/document.xml")
            top = "\n".join(p["text_mit_einfuegungen"] for p in main["absaetze"][:12])
            headers = "\n".join(p["text_mit_einfuegungen"] for part in result["teile"] if "header" in part["teil"] for p in part["absaetze"])
            if not re.search(r"\bEntwurf\b", top + "\n" + headers, re.I):
                result["vorlagenhinweise"].append({"grund": "Entwurf im Dokumentanfang/Kopf nicht gefunden"})
            if not re.search(r"(?:Urkunden(?:verzeichnis|rolle)?(?:snummer)?|UR[- .]?Nr|UVZ)[^\n]{0,45}_{3}", top, re.I):
                result["vorlagenhinweise"].append({"grund": "Freies Feld für eigene Urkundennummer am Anfang nicht gefunden"})
            patterns = (
                (r"\b(?:KI[ -]?generiert|mit KI generiert|AI[ -]?generated|generated (?:with|by) AI)\b", "KI-Hinweis in Vorlage"),
                (r"\b(?:erschienen heute|wurde[n]?[^.]{0,100}(?:vorgelesen|genehmigt|unterschrieben)|appeared today|was read aloud)\b", "Möglicher Vergangenheitsvermerk zur Beurkundung"),
            )
            for p in paragraphs:
                for pattern, reason in patterns:
                    if re.search(pattern, p["text_mit_einfuegungen"], re.I):
                        result["vorlagenhinweise"].append({"fundort": p["fundort"], "grund": reason,
                                                           "text": p["text_mit_einfuegungen"]})
            # Only the document opening is the primary deed field; referenced deeds elsewhere are legitimate.
            if re.search(r"(?:UR[- .]?Nr\.?|UVZ(?:[- .]?Nr\.?)?|Urkunden(?:verzeichnis|rolle)?(?:snummer)?\s*(?:Nr\.?)?)\s*[:.]?\s*\d", top, re.I):
                result["vorlagenhinweise"].append({"grund": "Möglicherweise ausgefüllte eigene Urkundennummer im Dokumentanfang"})
    result["hinweis"] = "Textaufnahme ist keine Layoutprüfung. Änderungsannahme und Beurkundungsstatus bedürfen gesonderter Feststellung."
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datei", type=Path)
    parser.add_argument("--vorlage", action="store_true")
    args = parser.parse_args()
    try:
        result = inventory(args.datei, args.vorlage)
    except (OSError, BadZipFile, ET.ParseError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
