#!/usr/bin/env python3
"""Build German/English two-column contract versions for the sample contracts.

The committed bilingual HTML files are generated artifacts, not separate legal
source documents. The German Markdown source remains authoritative.

Runtime dependency for translation generation:
  argostranslate with the German -> English package installed.

Rendering dependencies:
  pandoc, weasyprint, LibreOffice/soffice.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


try:
    import argostranslate.translate
except Exception:  # pragma: no cover - handled at runtime
    argostranslate = None


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ContractConfig:
    src: Path
    out_prefix: str
    short_title: str
    notary_de: str
    read_de: str
    deed_de: str


CONFIGS = [
    ContractConfig(
        src=ROOT / "vertragsdokumente/bautraegervertrag/bautraegervertrag.md",
        out_prefix="bautraegervertrag-de-en",
        short_title="Wohnungsbauträgervertrag mit Auflassung",
        notary_de="Der amtierende Notar",
        read_de="verliest",
        deed_de="beurkundet",
    ),
    ContractConfig(
        src=ROOT / "vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md",
        out_prefix="bautraegervertrag-marewald-de-en",
        short_title="Wohnungsbauträgervertrag mit Auflassung",
        notary_de="Die amtierende Notarin",
        read_de="verliest",
        deed_de="beurkundet",
    ),
    ContractConfig(
        src=ROOT / "vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md",
        out_prefix="bautraegervertrag-lindenhain-de-en",
        short_title="Wohnungsbauträgervertrag mit Auflassung",
        notary_de="Die amtierende Notarin",
        read_de="verliest",
        deed_de="beurkundet",
    ),
]


LANGUAGE_NOTICE = """## Sprachfassung, Verlesung und Verständnishilfe

**S.0** Diese Urkunde ist in einer deutsch-englischen Lesefassung erstellt. {notary_de} {deed_de} und {read_de} im Beurkundungstermin ausschließlich die deutsche Sprachfassung. Die englische Sprachfassung ist keine selbständige Vertragssprache, wird nicht verlesen und dient allein dem besseren Verständnis des Käufers; sie begründet keine von der deutschen Sprachfassung abweichenden Rechte, Pflichten, Fälligkeiten, Fristen, Beschaffenheiten oder Rechtsfolgen.
"""


LANGUAGE_NOTICE_EN = """## Language Version, Reading Aloud and Comprehension Aid

**S.0** This deed has been prepared as a German/English reading version. At the notarisation appointment, the acting notary records and reads aloud only the German language version. The English language version is not an independent contractual language, is not read aloud and serves solely to assist the Buyer in understanding the deed; it does not create any rights, obligations, due dates, time limits, qualities or legal consequences differing from the German language version.
"""


PRIORITY_CLAUSE_DE = """# Sprachvorrang

**SV.1** Bei Konflikten, Auslegungszweifeln, Abweichungen, Übersetzungsungenauigkeiten oder sonstigen Widersprüchen zwischen der deutschen und der englischen Sprachfassung ist ausschließlich die deutsche Sprachfassung maßgeblich. Die englische Sprachfassung tritt in jedem Fall hinter die deutsche Sprachfassung zurück und dient allein als Verständnishilfe.
"""


PRIORITY_CLAUSE_EN = """# Language Precedence

**SV.1** In the event of conflicts, doubts of interpretation, deviations, translation inaccuracies or any other inconsistencies between the German and English language versions, only the German language version shall be authoritative. The English language version shall in all cases be subordinate to the German language version and serves solely as a comprehension aid.
"""


EXACT_TRANSLATIONS = {
    "Verhandelt": "Recorded",
    "zu Berlin, am 14. März 2026": "in Berlin, on 14 March 2026",
    "zu Hamburg, am 12. Juni 2026": "in Hamburg, on 12 June 2026",
    "zu Köln, am 18. September 2026": "in Cologne, on 18 September 2026",
    "Vor mir, dem unterzeichnenden Notar im Bezirk des Kammergerichts": "Before me, the undersigned Notary in the district of the Kammergericht",
    "Vor mir, der unterzeichnenden Notarin im Bezirk des Hanseatischen Oberlandesgerichts": "Before me, the undersigned Notary in the district of the Hanseatic Higher Regional Court",
    "Vor mir, der unterzeichnenden Notarin im Bezirk des Oberlandesgerichts Köln": "Before me, the undersigned Notary in the district of the Higher Regional Court of Cologne",
    "erschienen heute:": "appeared today:",
    "dem Notar von Person bekannt,": "personally known to the Notary,",
    "der Notarin von Person bekannt,": "personally known to the Notary,",
    "ausgewiesen durch gültigen Personalausweis,": "identified by a valid identity card,",
    "Die Erschienenen baten sodann um die Beurkundung des nachstehenden": "The persons appearing then requested the notarisation of the following",
}


MANUAL_TRANSLATIONS = {
    LANGUAGE_NOTICE.format(
        notary_de="Der amtierende Notar", deed_de="beurkundet", read_de="verliest"
    )
    .strip()
    .split("\n\n", 1)[1]: LANGUAGE_NOTICE_EN.strip().split("\n\n", 1)[1],
    LANGUAGE_NOTICE.format(
        notary_de="Die amtierende Notarin", deed_de="beurkundet", read_de="verliest"
    )
    .strip()
    .split("\n\n", 1)[1]: LANGUAGE_NOTICE_EN.strip().split("\n\n", 1)[1],
    PRIORITY_CLAUSE_DE.strip().split("\n\n", 1)[1]: PRIORITY_CLAUSE_EN.strip().split("\n\n", 1)[1],
}


def translate(text: str) -> str:
    if not text.strip():
        return text
    if argostranslate is None:
        raise RuntimeError(
            "argostranslate is not available. Install argostranslate and the de->en package."
        )
    result = argostranslate.translate.translate(text, "de", "en")
    return polish_translation(result)


def polish_translation(text: str) -> str:
    text = re.sub(r"\*\*([^*\n]*?)\s+\*\*", r"**\1**", text)
    replacements = {
        "seller": "Seller",
        "buyer": "Buyer",
        "notary": "Notary",
        "purchase price": "Purchase Price",
        "purchase item": "Purchased Property",
        "object of purchase": "Purchased Property",
        "contract object": "Purchased Property",
        "building description": "Building Specification",
        "division declaration": "Declaration of Division",
        "land register": "Land Register",
        "special property": "Sondereigentum",
        "common property": "Common Property",
        "provision for disposition": "priority notice of conveyance",
        "disposition reservation": "priority notice of conveyance",
        "property reserve": "priority notice of conveyance",
        "property reservation": "priority notice of conveyance",
        "reservation train by train": "priority notice of conveyance concurrently",
        "Global Grundschuld": "global land charge",
        "basic debt": "land charge",
        "basic financing liens": "financing land charges",
        "object monitoring": "site supervision",
        "ready-to-cover production": "readiness for occupancy",
        "subscription readiness": "readiness for occupancy",
        "subscription skill": "readiness for occupancy",
        "ready to move": "ready for occupancy",
        "ground exploitation and connection costs": "development and connection costs",
        "recognized rules of the technique": "recognised rules of technology",
        "recognized rules of technology": "recognised rules of technology",
        "rules of technology": "rules of technology",
        "MK-Bound": "MK-Boden",
        "Flash or special fittings": "Flush or special fittings",
        "multiplelocking": "multiple locking",
        "Makler- und Bauträgerverordnung": "German Makler- und Bauträgerverordnung (MaBV)",
        "Published today:": "appeared today:",
        "Business resident:": "business address:",
        "resident:": "resident at:",
        "issued by a valid identity card": "identified by a valid identity card",
        "known to the Notary by person": "personally known to the Notary",
    }
    for old, new in replacements.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    phrase_replacements = {
        "** at the time": " at the time",
        "**and* payments": "and payments",
        "The Seller authorizes and authorizes": "The Seller authorizes",
        "The Seller hereby authorizes and authorizes": "The Seller hereby authorizes",
        "the registration of a priority notice of conveyance train by train": "the deletion of a priority notice of conveyance concurrently",
        "the deletion of the priority notice of conveyance train by train": "the deletion of the priority notice of conveyance concurrently",
        "the property reservation train by train": "the priority notice of conveyance concurrently",
        "statement of insolvency in accordance with § 883 BGB": "priority notice of conveyance pursuant to § 883 BGB",
        "dismissal only after receipt": "registration only after receipt",
        "the Purchased Property in the position": "the Purchased Property in its position",
        "if the Seller asks": "when the Seller asks",
    }
    for old, new in phrase_replacements.items():
        text = text.replace(old, new)
    text = text.replace("**", "")
    text = text.replace("§ §", "§§")
    text = text.replace("EUR", "EUR")
    return text


def split_blocks(markdown: str) -> list[str]:
    lines = markdown.splitlines()
    blocks: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() == r"\newpage":
            blocks.append(r"\newpage")
            i += 1
            continue
        if line.lstrip().startswith("#"):
            blocks.append(line)
            i += 1
            continue
        if line.startswith("|"):
            table = [line]
            i += 1
            while i < len(lines) and lines[i].startswith("|"):
                table.append(lines[i])
                i += 1
            blocks.append("\n".join(table))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = [line]
            i += 1
            while i < len(lines) and (not lines[i].strip() or re.match(r"^\s*[-*]\s+", lines[i])):
                if lines[i].strip():
                    items.append(lines[i])
                i += 1
            blocks.append("\n".join(items))
            continue

        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip():
                break
            if nxt.strip() == r"\newpage" or nxt.lstrip().startswith("#") or nxt.startswith("|") or re.match(r"^\s*[-*]\s+", nxt):
                break
            para.append(nxt)
            i += 1
        blocks.append("\n".join(para))
    return blocks


def inject_language_notice(blocks: list[str], cfg: ContractConfig) -> list[str]:
    notice_de = LANGUAGE_NOTICE.format(
        notary_de=cfg.notary_de, deed_de=cfg.deed_de, read_de=cfg.read_de
    ).strip()
    result: list[str] = []
    inserted = False
    for index, block in enumerate(blocks):
        result.append(block)
        if not inserted and index == 0 and block.startswith("# "):
            result.extend(split_blocks(notice_de))
            inserted = True
    if not inserted:
        result[0:0] = split_blocks(notice_de)
    result.extend([r"\newpage", *split_blocks(PRIORITY_CLAUSE_DE.strip())])
    return result


def translate_block(block: str) -> str:
    if block == r"\newpage":
        return block
    if block in MANUAL_TRANSLATIONS:
        return MANUAL_TRANSLATIONS[block]
    if block.startswith("#"):
        prefix, title = re.match(r"^(#+)\s+(.*)$", block).groups()  # type: ignore[union-attr]
        manual = {
            "Bauträgervertrag": "Property Development Contract",
            "Wohnungsbauträgervertrag mit Auflassung": "Residential Property Development Contract with Conveyance",
            "Sprachfassung, Verlesung und Verständnishilfe": "Language Version, Reading Aloud and Comprehension Aid",
            "Sprachvorrang": "Language Precedence",
            "Anlage: Baubeschreibung": "Annex: Building Specification",
            "Schlussbestimmungen der Baubeschreibung": "Final Provisions of the Building Specification",
        }
        return f"{prefix} {manual.get(title, translate(title))}"
    if block.startswith("|"):
        return translate_markdown_table(block)
    if re.match(r"^\s*[-*]\s+", block):
        out = []
        for line in block.splitlines():
            marker, rest = re.match(r"^(\s*[-*]\s+)(.*)$", line).groups()  # type: ignore[union-attr]
            out.append(marker + translate_clause_text(rest))
        return "\n".join(out)
    return translate_clause_text(block)


def translate_clause_text(text: str) -> str:
    if text in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[text]
    if re.fullmatch(r"\*\*[^*\n]+\*\*", text.strip()):
        return text
    for prefix_de, prefix_en in [
        ("geschäftsansässig:", "business address:"),
        ("Geschäftsanschrift:", "business address:"),
        ("wohnhaft:", "resident at:"),
    ]:
        if text.startswith(prefix_de):
            return prefix_en + text[len(prefix_de) :]
    leading = re.match(r"^(\*\*[A-Za-z0-9.]+\*\*\s*)(.*)$", text, flags=re.S)
    if leading:
        return leading.group(1) + translate(leading.group(2))
    if text.strip() in {"\\", "——————————————————————————"}:
        return text
    if re.fullmatch(r"[\s\\—–-]+", text.strip()):
        return text
    return translate(text)


def split_table_row(row: str) -> list[str]:
    inner = row.strip().strip("|")
    return [cell.strip() for cell in inner.split("|")]


def translate_markdown_table(block: str) -> str:
    rows = block.splitlines()
    translated = []
    for idx, row in enumerate(rows):
        cells = split_table_row(row)
        if idx == 1 and all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            translated.append(row)
            continue
        translated_cells = []
        for cell in cells:
            if re.fullmatch(r"[:\-\s]+", cell) or re.fullmatch(r"[0-9., %EUR§/()A-Za-z-]+", cell) and not re.search(r"[ÄÖÜäöüß]", cell):
                translated_cells.append(cell)
            else:
                translated_cells.append(translate(cell))
        translated.append("| " + " | ".join(translated_cells) + " |")
    return "\n".join(translated)


def markdown_to_html(block: str) -> str:
    if block == r"\newpage":
        return ""
    if not block.strip():
        return ""
    proc = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html"],
        input=block,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout.strip()


def bilingual_rows(blocks: list[str], english_blocks: list[str]) -> str:
    rows = [
        '<table class="bilingual-table">',
        "<colgroup><col><col></colgroup>",
        "<thead><tr><th>Deutsche Fassung</th><th>English convenience translation</th></tr></thead>",
        "<tbody>",
    ]
    for de, en in zip(blocks, english_blocks):
        if de == r"\newpage":
            rows.append('<tr class="pagebreak"><td colspan="2"></td></tr>')
            continue
        de_html = markdown_to_html(de)
        en_html = markdown_to_html(en)
        rows.append(
            "<tr>"
            f'<td class="de">{de_html}</td>'
            f'<td class="en">{en_html}</td>'
            "</tr>"
        )
    rows.append("</tbody></table>")
    return "\n".join(rows)


def html_document(title: str, body: str) -> str:
    escaped_title = html.escape(title)
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>{escaped_title}</title>
<style>
@page {{
  size: A4 landscape;
  margin: 1.35cm 1.15cm 1.25cm 1.15cm;
  @bottom-center {{
    content: counter(page);
    font-family: "DejaVu Serif", Georgia, serif;
    font-size: 8pt;
    color: #666;
  }}
}}
body {{
  font-family: "DejaVu Serif", Georgia, serif;
  color: #111;
  font-size: 8.4pt;
  line-height: 1.34;
}}
.doc-title {{
  font-size: 16pt;
  margin: 0 0 0.8em;
  letter-spacing: 0;
}}
.doc-note {{
  margin: 0 0 1em;
  color: #333;
  font-size: 8.6pt;
}}
table.bilingual-table {{
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}}
.bilingual-table > colgroup > col {{ width: 50%; }}
.bilingual-table > thead th {{
  border: 0.8px solid #555;
  background: #eeeeee;
  padding: 5px 7px;
  text-align: left;
  font-weight: bold;
  font-size: 8.8pt;
}}
.bilingual-table > tbody > tr > td {{
  border: 0.45px solid #b5b5b5;
  vertical-align: top;
  padding: 5px 7px;
}}
.bilingual-table tr.pagebreak td {{
  border: none;
  padding: 0;
  height: 0;
  page-break-after: always;
}}
h1 {{
  font-size: 11.4pt;
  margin: 0.3em 0 0.35em;
  padding-bottom: 1px;
  border-bottom: 0.8px solid #333;
  page-break-after: avoid;
}}
h2 {{
  font-size: 9.8pt;
  margin: 0.45em 0 0.25em;
  page-break-after: avoid;
}}
h3 {{
  font-size: 9pt;
  margin: 0.4em 0 0.2em;
  page-break-after: avoid;
}}
p {{ margin: 0.35em 0; }}
blockquote {{
  margin: 0.35em 0 0.35em 0.25em;
  padding: 0.05em 0 0.05em 0.55em;
  border-left: 1.5px solid #aaa;
}}
td table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 7.6pt;
  margin: 0.35em 0;
}}
td table th, td table td {{
  border: 0.35px solid #999;
  padding: 2px 3px;
  vertical-align: top;
  text-align: left;
}}
td table th {{ background: #f0f0f0; }}
ul, ol {{ margin: 0.3em 0 0.3em 1.15em; padding: 0; }}
li {{ margin: 0.2em 0; }}
strong {{ font-weight: bold; }}
</style>
</head>
<body>
<h1 class="doc-title">{escaped_title}</h1>
<p class="doc-note">Deutsch-englische Lesefassung. Bei Abweichungen ist die deutsche Sprachfassung maßgeblich.</p>
{body}
</body>
</html>
"""


WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def repair_bilingual_docx_tables(path: Path) -> None:
    """Flatten nested rate tables that LibreOffice misplaces during HTML import.

    LibreOffice keeps the surrounding German/English table intact for prose, but
    imports the two nested Markdown tables into swapped cells at excessive width.
    Converting each rate row to a compact paragraph preserves the two-column
    reading order and prevents clipping in Word and LibreOffice.
    """

    qn = lambda name: f"{{{WORD_NS}}}{name}"
    ET.register_namespace("w", WORD_NS)

    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))

    parents = {child: parent for parent in root.iter() for child in parent}

    def ancestor(element: ET.Element, tag: str) -> ET.Element | None:
        parent = parents.get(element)
        while parent is not None and parent.tag != qn(tag):
            parent = parents.get(parent)
        return parent

    def element_text(element: ET.Element) -> str:
        return "".join(node.text or "" for node in element.iter(qn("t")))

    english_rate_replacements = {
        "Stichmonat": "Construction milestone",
        "Bautenstand": "Construction status",
        "Anteil": "Percentage",
        "Betrag": "Percentage",
        "nach Beginn der Erdarbeiten": "after commencement of earthworks",
        "Beginn der Erdarbeiten, nach Vorliegen der Voraussetzungen aus § 3.1": (
            "after commencement of earthworks and satisfaction of the conditions in § 3.1"
        ),
        "nach Fassadenarbeiten": "after completion of facade works",
        "Innenputz, Estrich und Fassadenarbeiten": (
            "interior plaster, screed and facade works"
        ),
        "Readiness to reference Train to train against transfer of ownership": (
            "readiness for occupancy concurrently with transfer of possession"
        ),
        "Readiness to reference train to train against transfer of ownership": (
            "readiness for occupancy concurrently with transfer of possession"
        ),
        "Skill of reference and train by train against transfer of ownership": (
            "readiness for occupancy concurrently with transfer of possession"
        ),
    }

    def table_lines(table: ET.Element, *, english: bool) -> list[ET.Element]:
        paragraphs: list[ET.Element] = []
        for index, row in enumerate(table.findall(qn("tr"))):
            values = [element_text(cell).strip() for cell in row.findall(qn("tc"))]
            if english:
                values = [english_rate_replacements.get(value, value) for value in values]
            paragraph = ET.Element(qn("p"))
            properties = ET.SubElement(paragraph, qn("pPr"))
            ET.SubElement(
                properties,
                qn("pStyle"),
                {qn("val"): "TableHeading" if index == 0 else "TableContents"},
            )
            ET.SubElement(properties, qn("spacing"), {qn("before"): "0", qn("after"): "80"})
            run = ET.SubElement(paragraph, qn("r"))
            if index == 0:
                run_properties = ET.SubElement(run, qn("rPr"))
                ET.SubElement(run_properties, qn("b"))
            text = ET.SubElement(run, qn("t"))
            text.text = " · ".join(values)
            paragraphs.append(paragraph)
        return paragraphs

    tables = list(root.iter(qn("tbl")))
    if not any(list(table.iter(qn("tbl")))[1:] for table in tables):
        return
    innermost_tables = [
        table for table in tables if not list(table.iter(qn("tbl")))[1:]
    ]
    if not innermost_tables:
        return
    if len(innermost_tables) % 2:
        raise RuntimeError(f"Unexpected nested table count in {path}: {len(innermost_tables)}")

    for german_table, english_table in zip(innermost_tables[::2], innermost_tables[1::2]):
        german_cell = ancestor(german_table, "tc")
        english_cell = ancestor(english_table, "tc")
        german_row = ancestor(german_cell, "tr") if german_cell is not None else None
        english_row = ancestor(english_cell, "tr") if english_cell is not None else None
        outer_table = ancestor(german_row, "tbl") if german_row is not None else None
        if any(
            element is None
            for element in (german_cell, english_cell, german_row, english_row, outer_table)
        ):
            raise RuntimeError(f"Could not locate bilingual table structure in {path}")
        if outer_table is not ancestor(english_row, "tbl"):
            raise RuntimeError(f"Nested tables do not share an outer table in {path}")

        target_cells = german_row.findall(qn("tc"))
        english_cells = english_row.findall(qn("tc"))
        if len(target_cells) != 2 or not english_cells:
            raise RuntimeError(f"Unexpected bilingual row geometry in {path}")
        if german_cell is not target_cells[1] or english_cell is not english_cells[0]:
            raise RuntimeError(f"LibreOffice table import shape changed in {path}")

        german_lines = table_lines(german_table, english=False)
        english_lines = table_lines(english_table, english=True)
        german_cell.remove(german_table)
        english_cell.remove(english_table)
        for paragraph in german_lines:
            target_cells[0].append(paragraph)
        for paragraph in english_lines:
            target_cells[1].append(paragraph)
        outer_table.remove(english_row)

    document_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    temporary = path.with_suffix(".tmp.docx")
    with ZipFile(path) as source, ZipFile(temporary, "w", ZIP_DEFLATED) as target:
        for item in source.infolist():
            data = document_xml if item.filename == "word/document.xml" else source.read(item.filename)
            target.writestr(item, data)
    temporary.replace(path)


def build_contract(cfg: ContractConfig, render: bool) -> None:
    source = cfg.src.read_text(encoding="utf-8")
    blocks = inject_language_notice(split_blocks(source), cfg)
    english_blocks: list[str] = []
    for block in blocks:
        if block.strip() == LANGUAGE_NOTICE.format(
            notary_de=cfg.notary_de, deed_de=cfg.deed_de, read_de=cfg.read_de
        ).strip():
            english_blocks.extend(split_blocks(LANGUAGE_NOTICE_EN.strip()))
            continue
        if block.strip() == PRIORITY_CLAUSE_DE.strip():
            english_blocks.extend(split_blocks(PRIORITY_CLAUSE_EN.strip()))
            continue
        english_blocks.append(translate_block(block))

    if len(blocks) != len(english_blocks):
        raise RuntimeError(f"Block count mismatch for {cfg.src}: {len(blocks)} != {len(english_blocks)}")

    out_dir = cfg.src.parent
    out_html = out_dir / f"{cfg.out_prefix}.html"
    out_pdf = out_dir / f"{cfg.out_prefix}.pdf"
    out_docx = out_dir / f"{cfg.out_prefix}.docx"
    html_text = html_document(
        f"{cfg.short_title} — Deutsch/English",
        bilingual_rows(blocks, english_blocks),
    )
    out_html.write_text(html_text, encoding="utf-8")

    if render:
        subprocess.run(["weasyprint", str(out_html), str(out_pdf)], check=True)
        tmp_odt = out_dir / f"{cfg.out_prefix}.odt"
        for stale in [tmp_odt, out_docx]:
            stale.unlink(missing_ok=True)
        subprocess.run(["soffice", "--headless", "--convert-to", "odt", "--outdir", str(out_dir), str(out_html)], check=True)
        subprocess.run(["soffice", "--headless", "--convert-to", "docx", "--outdir", str(out_dir), str(tmp_odt)], check=True)
        repair_bilingual_docx_tables(out_docx)
        tmp_odt.unlink(missing_ok=True)
        print(f"built {out_html.relative_to(ROOT)}, {out_pdf.relative_to(ROOT)}, {out_docx.relative_to(ROOT)}")
    else:
        print(f"built {out_html.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-render", action="store_true", help="Only generate bilingual HTML.")
    parser.add_argument(
        "--repair-docx",
        type=Path,
        help="Repair an already generated bilingual DOCX without running translation.",
    )
    args = parser.parse_args()

    if args.repair_docx is not None:
        repair_bilingual_docx_tables(args.repair_docx.resolve())
        print(f"repaired {args.repair_docx}")
        return

    for tool in ["pandoc"]:
        if shutil.which(tool) is None:
            raise SystemExit(f"Missing required tool: {tool}")
    if not args.no_render and shutil.which("weasyprint") is None:
        raise SystemExit("Missing required tool: weasyprint")
    if not args.no_render and shutil.which("soffice") is None:
        raise SystemExit("Missing required tool: soffice")

    for cfg in CONFIGS:
        build_contract(cfg, render=not args.no_render)


if __name__ == "__main__":
    main()
