#!/usr/bin/env python3
"""Check structural, editorial and workflow invariants of both skill files."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FULL = ROOT / "skill" / "SKILL.md"
MINI = ROOT / "skill" / "MINI_SKILL.md"
CASE_RE = re.compile(r"(?<!\w)(?:[IVX]{1,4}|[0-9]{1,2})\s+(?:ZR|ZB|U)\s+\d+/\d{2}(?!\d)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")

REQUIRED_FULL_SECTIONS = (
    "## Ausführungskern",
    "## Harte Quellenregeln",
    "## Sofortstart",
    "## Fall-Fingerabdruck und Anti-Generik-Regel",
    "## Aktuelle Rechtsprechungsanker",
    "## Normenkarte",
    "## 30-Prüfschleifen",
    "## Pflicht-Prüfblock",
    "## Workflow",
    "## Antwortformate",
    "## Teil A — MaBV und Zahlungen",
    "## Teil B — AGB-Klauselkontrolle",
    "## Teil C — Baubeschreibung und Bausoll",
    "## Teil D — Abnahme und Mängelrechte",
    "## Teil E — Teilungserklärung, WEG, Gemeinschaftsordnung",
    "## Teil F — Eigentumsschutz und Insolvenz",
    "## Teil L — Drei-Dokumente-Paket",
    "## Teil N — Wirtschaft, Organisation, HOAI und Technik",
    "## Teil O — Fachmodul-Triggerindex",
    "## Bug-Hunt vor Ausgabe",
)

REQUIRED_WORKFLOW_PHRASES = (
    "Schnellpfad ohne Qualitätsverlust",
    "Ein Befundregister ist die einzige Tatsachenbasis",
    "Dokumente nur einmal vollständig",
    "gebündelten Quellencheck",
    "Startsignal: Ich beginne jetzt",
    "Vollpaket-Abschlussgate",
    "Dokumenten- und OCR-Gate",
    "Evidenz- und Drei-Achsen-Gate",
    "Zeitstands- und Entscheidungs-Fit-Gate",
    "Fristen- und Eiltriage",
    "Erstantwort-Vertrag",
    "Ratenrechenblatt und Vorleistungsprofil",
    "Zahlungsfreigabekarte",
    "Abschlussentscheidung",
    "Dokument 1 — Übersendungsschreiben",
    "Dokument 2 — Mandantengutachten",
    "Dokument 3 — Aufforderungsschreiben",
)

REQUIRED_LEGAL_PHRASES = (
    "VII ZR 388/00",
    "V ZR 132/23",
    "V ZR 75/18",
    "Gesamt-GdWE",
    "Untergemeinschaft",
    "vollstreckbare Ausfertigung",
    "soweit der Verbraucher oder sein Beauftragter die wesentlichen Planungsvorgaben erstellt",
    "Art. 229 § 39 EGBGB",
    "§ 13a BeurkG a. F.",
    "29. Dezember 2025",
)

TEXT_SUFFIXES = {".css", ".html", ".lua", ".md", ".py", ".sh", ".sha256", ".yaml", ".yml"}
TEXT_NAMES = {"LICENSE-APACHE", "LICENSE-MIT"}


class Audit:
    def __init__(self) -> None:
        self.checks = 0
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)


def frontmatter_version(text: str, label: str, audit: Audit) -> str:
    match = FRONTMATTER_RE.match(text)
    audit.require(match is not None, f"{label}: missing YAML frontmatter")
    if match is None:
        return ""
    versions = re.findall(r'^\s+version:\s+"([^"]+)"\s*$', match.group("body"), re.MULTILINE)
    audit.require(len(versions) == 1, f"{label}: expected exactly one metadata version")
    return versions[0] if versions else ""


def check_text_hygiene(text: str, label: str, audit: Audit) -> None:
    audit.require(not text.startswith("\ufeff"), f"{label}: UTF-8 BOM is not allowed")
    audit.require(text.endswith("\n"), f"{label}: final newline is missing")
    audit.require("\r" not in text, f"{label}: CRLF/CR characters found")
    audit.require("\t" not in text, f"{label}: tab characters found")
    audit.require("\n\n\n" not in text, f"{label}: more than one blank line in sequence")
    trailing = [
        number
        for number, line in enumerate(text.splitlines(), 1)
        if line.rstrip() != line
    ]
    audit.require(not trailing, f"{label}: trailing whitespace on lines {trailing[:8]}")

    fence: tuple[str, int] | None = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker is None:
            continue
        token = marker.group(1)[0]
        if fence is None:
            fence = (token, number)
        elif fence[0] == token:
            fence = None
    audit.require(
        fence is None,
        f"{label}: unclosed code fence from line {fence[1] if fence else '?'}",
    )


def visible_markdown(text: str) -> str:
    """Blank fenced examples while keeping line numbers stable."""
    visible: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker is not None:
            token = marker.group(1)[0]
            if fence is None:
                fence = token
            elif fence == token:
                fence = None
            visible.append("\n" if line.endswith("\n") else "")
        elif fence is not None:
            visible.append("\n" if line.endswith("\n") else "")
        else:
            visible.append(line)
    return "".join(visible)


def check_headings(text: str, label: str, audit: Audit) -> None:
    headings = [(len(match.group(1)), match.group(2)) for match in HEADING_RE.finditer(text)]
    audit.require(bool(headings), f"{label}: no headings found")
    audit.require(
        sum(level == 1 for level, _ in headings) == 1,
        f"{label}: expected exactly one H1",
    )
    duplicates = sorted(
        name for name, count in Counter(name for _, name in headings).items() if count > 1
    )
    audit.require(not duplicates, f"{label}: duplicate headings: {', '.join(duplicates)}")
    for previous, current in zip(headings, headings[1:]):
        audit.require(
            current[0] <= previous[0] + 1,
            f"{label}: heading level jumps from H{previous[0]} to H{current[0]} at {current[1]}",
        )


def split_table_row(line: str) -> list[str]:
    body = line.strip()[1:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", body)]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)


def check_tables(text: str, label: str, audit: Audit) -> None:
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        if not (lines[index].startswith("|") and lines[index].endswith("|")):
            index += 1
            continue
        start = index
        block: list[list[str]] = []
        while index < len(lines) and lines[index].startswith("|") and lines[index].endswith("|"):
            block.append(split_table_row(lines[index]))
            index += 1
        audit.require(len(block) >= 2, f"{label}:{start + 1}: isolated table row")
        if len(block) < 2:
            continue
        width = len(block[0])
        audit.require(width >= 2, f"{label}:{start + 1}: table has fewer than two columns")
        audit.require(
            is_separator_row(block[1]),
            f"{label}:{start + 2}: table header lacks a valid separator row",
        )
        for offset, row in enumerate(block):
            audit.require(
                len(row) == width,
                f"{label}:{start + offset + 1}: table has {len(row)} instead of {width} columns",
            )

        keys = [row[0].casefold() for row in block[2:] if row and not is_separator_row(row)]
        duplicate_keys = sorted(key for key, count in Counter(keys).items() if key and count > 1)
        audit.require(
            not duplicate_keys,
            f"{label}:{start + 1}: duplicate first-column labels: {', '.join(duplicate_keys)}",
        )


def check_duplicate_prose(text: str, label: str, audit: Audit) -> None:
    candidates = [
        re.sub(r"\s+", " ", line.strip())
        for line in text.splitlines()
        if len(line.strip()) >= 100
        and not line.startswith("|")
        and not line.startswith("```")
        and not re.match(r"^\d+\.\s", line)
    ]
    duplicates = sorted(line for line, count in Counter(candidates).items() if count > 1)
    audit.require(not duplicates, f"{label}: duplicated long prose blocks found")


def section(text: str, start: str, end: str, label: str, audit: Audit) -> str:
    start_count = text.count(start)
    end_count = text.count(end)
    audit.require(start_count == 1, f"{label}: section marker occurs {start_count} times: {start}")
    audit.require(end_count == 1, f"{label}: section marker occurs {end_count} times: {end}")
    if start_count != 1 or end_count != 1:
        return ""
    return text[text.index(start) : text.index(end, text.index(start))]


def check_repository_texts(audit: Audit) -> None:
    paths = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and (path.suffix in TEXT_SUFFIXES or path.name in TEXT_NAMES)
    )
    audit.require(bool(paths), "no repository text files found")
    for path in paths:
        label = path.relative_to(ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            audit.require(False, f"{label}: text file is not valid UTF-8")
            continue
        audit.require(not text.startswith("\ufeff"), f"{label}: UTF-8 BOM is not allowed")
        audit.require("\x00" not in text, f"{label}: NUL byte found")
        audit.require("\r" not in text, f"{label}: CRLF/CR characters found")
        audit.require(text.endswith("\n"), f"{label}: final newline is missing")
        trailing = any(line.rstrip() != line for line in text.splitlines())
        audit.require(not trailing, f"{label}: trailing whitespace found")


def main() -> None:
    audit = Audit()
    full = FULL.read_text(encoding="utf-8")
    mini = MINI.read_text(encoding="utf-8")

    check_repository_texts(audit)

    for text, label in ((full, "skill/SKILL.md"), (mini, "skill/MINI_SKILL.md")):
        check_text_hygiene(text, label, audit)
        check_headings(text, label, audit)
        visible = visible_markdown(text)
        check_tables(visible, label, audit)
        check_duplicate_prose(visible, label, audit)

    full_version = frontmatter_version(full, "skill/SKILL.md", audit)
    mini_version = frontmatter_version(mini, "skill/MINI_SKILL.md", audit)
    audit.require(
        mini_version == f"{full_version}-mini",
        "full and mini metadata versions diverge",
    )
    audit.require(
        f"# Bauträgervertrag-Prüfer {full_version}" in full,
        "full H1 does not match metadata version",
    )
    audit.require(
        f"# Mini-Bauträgervertrag-Prüfer {full_version}" in mini,
        "mini H1 does not match full metadata version",
    )
    audit.require(len(mini) <= 7500, f"mini exceeds 7,500 characters: {len(mini)}")
    audit.require(len(mini) >= 6000, f"mini is unexpectedly incomplete: {len(mini)} characters")

    last_position = -1
    full_lines = full.splitlines()
    for heading in REQUIRED_FULL_SECTIONS:
        count = full_lines.count(heading)
        audit.require(count == 1, f"full skill section occurs {count} times: {heading}")
        if count == 1:
            position = re.search(rf"(?m)^{re.escape(heading)}$", full).start()
            audit.require(
                position > last_position,
                f"full skill section is out of order: {heading}",
            )
            last_position = position

    for phrase in REQUIRED_WORKFLOW_PHRASES:
        audit.require(phrase in full, f"full skill misses workflow invariant: {phrase}")
    for phrase in REQUIRED_LEGAL_PHRASES:
        audit.require(phrase in full, f"full skill misses legal invariant: {phrase}")

    loops = section(full, "## 30-Prüfschleifen", "## Pflicht-Prüfblock", "full skill", audit)
    loop_numbers = [int(value) for value in re.findall(r"(?m)^(\d+)\.\s", loops)]
    audit.require(
        loop_numbers == list(range(1, 31)),
        "30-Prüfschleifen are incomplete or misnumbered",
    )

    anchors = section(
        full,
        "## Aktuelle Rechtsprechungsanker",
        "## Normenkarte",
        "full skill",
        audit,
    )
    mini_cases = set(CASE_RE.findall(mini))
    anchor_cases = set(CASE_RE.findall(anchors))
    missing_mini_cases = sorted(mini_cases - anchor_cases)
    audit.require(
        not missing_mini_cases,
        "mini cites dockets absent from the full anchor table: " + ", ".join(missing_mini_cases),
    )

    audit.require(
        "## Teil O — Fachmodule Bauträgerrecht 2026" not in full,
        "obsolete duplicate Part O remains",
    )
    audit.require(
        full.count("## Teil O — Fachmodul-Triggerindex") == 1,
        "Part O trigger index is missing",
    )
    for phrase in (
        "Vollpaket:",
        "Käufer-/Mandantenschreiben",
        "Mandantengutachten",
        "Aufforderungsschreiben an Bauträger",
        "Nächste Weiche",
        "Befundregister",
        "Zahlungsfreigabekarte",
    ):
        audit.require(phrase in mini, f"mini misses workflow invariant: {phrase}")

    if audit.errors:
        print("FAIL skill quality:", file=sys.stderr)
        for error in audit.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)

    print(
        "check_skill_quality: ok "
        f"({audit.checks} structural/editorial checks, mini {len(mini)} chars)"
    )


if __name__ == "__main__":
    main()
