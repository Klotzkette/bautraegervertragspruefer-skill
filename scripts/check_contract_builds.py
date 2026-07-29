#!/usr/bin/env python3
"""Verify artifact provenance and optionally rebuild German contract outputs."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "vertragsdokumente" / "artifact-manifest.sha256"
CONTRACTS = (
    "bautraegervertrag",
    "bautraegervertrag-marewald",
    "bautraegervertrag-lindenhain",
)
CASE_PROFILES = {
    "bautraegervertrag": {
        "project_token": "Am Birkenpfuhl",
        "unit_token": "4.27",
        "rate_number": 3,
        "security_amount": None,
        "required_contract_phrase": None,
        "required_request_phrase": None,
    },
    "bautraegervertrag-marewald": {
        "project_token": "Marewald Höfe",
        "unit_token": "C-2.14",
        "rate_number": 3,
        "security_amount": Decimal("33700.00"),
        "required_contract_phrase": "Keine Vorleistungen.",
        "required_request_phrase": (
            "Vor Eintritt der allgemeinen Fälligkeitsvoraussetzungen hat die "
            "Verkäuferin keine Zahlungen auf den Kaufpreis entgegengenommen."
        ),
    },
    "bautraegervertrag-lindenhain": {
        "project_token": "Lindenhain 12",
        "unit_token": "B-05",
        "rate_number": 4,
        "security_amount": Decimal("37100.00"),
        "required_contract_phrase": None,
        "required_request_phrase": None,
    },
}
ZIP_MEMBERS = {
    "bautraegervertrag": (
        "01-wohnungsbautraegervertrag-mit-auflassung.pdf",
        "02-baubeschreibung-birkenpfuhl-komfort-b4.pdf",
        "03-bautenstandsbericht-birkenpfuhl-haus-4.pdf",
        "04-zahlungsanforderung-birkenpfuhl-wohnung-4-27.pdf",
    ),
    "bautraegervertrag-marewald": (
        "01-wohnungsbautraegervertrag-mit-auflassung.pdf",
        "02-baubeschreibung-marewald-komfort-c.pdf",
        "03-bautenstandsbericht-marewald-haus-c.pdf",
        "04-zahlungsanforderung-marewald-wohnung-c-2-14.pdf",
    ),
    "bautraegervertrag-lindenhain": (
        "01-wohnungsbautraegervertrag-mit-auflassung.pdf",
        "02-baubeschreibung-lindenhain-komfort.pdf",
        "03-bautenstandsbericht-lindenhain-12.pdf",
        "04-zahlungsanforderung-lindenhain-wohnung-b-05.pdf",
    ),
}
CASE_DOCUMENT_SUFFIXES = ("-bautenstandsbericht", "-zahlungsanforderung")
REQUIRED_TOOLS = ("pandoc", "weasyprint", "perl", "zip", "pdftotext", "pdfinfo")
WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
CORE_NS = {
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
}
PROVENANCE_PREFIX = "btv-source-sha256:"
CASE_META_RE = re.compile(
    r"(?i)\b(?:testakte|testfall|übungsakte|übungsfall|schulungsakte|"
    r"schulungsfall|schulungszwecke?|trainingsakte|trainingsfall|"
    r"lösungsschlüssel|musterlösung|kontrollakte|horrorvertrag)\b"
)
PRE_NOTARIZATION_PAYMENT_RE = re.compile(
    r"(?i)\bvor (?:der )?beurkundung "
    r"(?:gezahlte[rsnm]?|geleistete[rsnm]?|entrichtete[rsnm]?)\b"
)
GERMAN_MONTHS = {
    "Januar": 1,
    "Februar": 2,
    "März": 3,
    "April": 4,
    "Mai": 5,
    "Juni": 6,
    "Juli": 7,
    "August": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Dezember": 12,
}


def fail(message: str) -> None:
    print(f"FAIL contract builds: {message}", file=sys.stderr)
    raise SystemExit(1)


def protected_paths() -> list[Path]:
    paths = [
        Path("scripts/build_bilingual_contracts.py"),
        Path("vertragsdokumente/case-style.css"),
    ]
    for name in CONTRACTS:
        base = Path("vertragsdokumente") / name
        paths.extend(
            [
                base / "build.sh",
                base / "build/pdf-template.html",
                base / "build/pagebreak.lua",
                base / "build/style.css",
                base / f"{name}.md",
                base / f"{name}.pdf",
                base / f"{name}.docx",
                *(
                    item
                    for suffix in CASE_DOCUMENT_SUFFIXES
                    for item in (
                        base / f"{name}{suffix}.md",
                        base / f"{name}{suffix}.pdf",
                    )
                ),
                base / f"{name}-einzel-pdfs.zip",
                base / f"{name}-de-en.html",
                base / f"{name}-de-en.pdf",
                base / f"{name}-de-en.docx",
            ]
        )
    return sorted(paths, key=lambda path: path.as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expected_hashes() -> dict[str, str]:
    result: dict[str, str] = {}
    for relative in protected_paths():
        absolute = ROOT / relative
        if not absolute.is_file():
            fail(f"protected file is missing: {relative}")
        result[relative.as_posix()] = sha256(absolute)
    return result


def read_manifest() -> dict[str, str]:
    if not MANIFEST.is_file():
        fail(f"artifact manifest is missing: {MANIFEST.relative_to(ROOT)}")
    result: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        MANIFEST.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line or raw_line.startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", raw_line)
        if match is None:
            fail(f"malformed manifest line {line_number}")
        digest, relative = match.groups()
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts:
            fail(f"unsafe manifest path on line {line_number}: {relative}")
        if relative in result:
            fail(f"duplicate manifest path on line {line_number}: {relative}")
        result[relative] = digest
    return result


def verify_manifest(*, check_artifacts: bool = True) -> None:
    if check_artifacts:
        verify_case_documents()
        verify_zip_structures()
        verify_bilingual_provenance()
    expected = expected_hashes()
    recorded = read_manifest()
    missing = sorted(expected.keys() - recorded.keys())
    extra = sorted(recorded.keys() - expected.keys())
    changed = sorted(
        path for path in expected.keys() & recorded.keys() if expected[path] != recorded[path]
    )
    if missing:
        fail(f"manifest lacks protected files: {', '.join(missing)}")
    if extra:
        fail(f"manifest contains unexpected files: {', '.join(extra)}")
    if changed:
        fail(
            "source, build rule or artifact changed without a verified rebuild: "
            + ", ".join(changed)
        )
    print(f"check_contract_builds: manifest ok ({len(expected)} protected files)")


def write_manifest() -> None:
    rebuild_contracts()
    verify_case_documents()
    verify_zip_structures()
    verify_bilingual_provenance()
    hashes = expected_hashes()
    lines = [
        "# Generated by: python3 scripts/check_contract_builds.py --write",
        "# Update only after German and bilingual artifacts have been rebuilt and checked.",
    ]
    lines.extend(f"{digest}  {path}" for path, digest in hashes.items())
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"check_contract_builds: wrote {MANIFEST.relative_to(ROOT)}")


def canonical_text(value: str) -> str:
    value = unicodedata.normalize("NFC", value).replace("\u00ad", "")
    value = re.sub(r"(?m)^\s*\d+\s*$", "", value)
    value = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", value)
    return re.sub(r"\s+", " ", value).strip()


def required_match(pattern: str, text: str, label: str) -> re.Match[str]:
    match = re.search(pattern, text, re.MULTILINE)
    if match is None:
        fail(f"case document lacks {label}")
    return match


def markdown_field(value: str) -> str:
    return re.sub(r"\s*<br\s*/?>\s*$", "", value, flags=re.IGNORECASE)


def parse_german_date(value: str, label: str) -> date:
    value = markdown_field(value)
    match = re.fullmatch(r"(\d{1,2})\.\s+([A-ZÄÖÜ][a-zäöüß]+)\s+(\d{4})", value)
    if match is None or match.group(2) not in GERMAN_MONTHS:
        fail(f"invalid German date in {label}: {value}")
    return date(int(match.group(3)), GERMAN_MONTHS[match.group(2)], int(match.group(1)))


def parse_german_decimal(value: str, label: str) -> Decimal:
    normalized = value.replace(".", "").replace(",", ".").replace(" ", "")
    try:
        return Decimal(normalized)
    except InvalidOperation as exc:
        fail(f"invalid decimal in {label}: {value} ({exc})")


def payment_rows(text: str, label: str) -> list[tuple[str, Decimal, Decimal]]:
    rows: list[tuple[str, Decimal, Decimal]] = []
    for raw_line in text.splitlines():
        if not raw_line.startswith("|"):
            continue
        cells = [cell.strip().replace("**", "") for cell in raw_line.strip("|").split("|")]
        if len(cells) != 3 or "%" not in cells[1] or "EUR" not in cells[2]:
            continue
        percent = parse_german_decimal(cells[1].split("%", 1)[0], f"{label} percent")
        amount = parse_german_decimal(cells[2].split("EUR", 1)[0], f"{label} amount")
        rows.append((cells[0], percent, amount))
    if len(rows) != 4:
        fail(f"{label} must contain exactly four payment calculation rows")
    return rows


def contract_rate_percentages(text: str, label: str) -> dict[int, Decimal]:
    rates: dict[int, Decimal] = {}
    for raw_line in text.splitlines():
        if not raw_line.startswith("|"):
            continue
        cells = [cell.strip().replace("**", "") for cell in raw_line.strip("|").split("|")]
        if len(cells) != 3 or "%" not in cells[2]:
            continue
        rate_match = re.fullmatch(r"(\d+)(?:\.\s*Rate)?", cells[0])
        if rate_match is None:
            continue
        rate_number = int(rate_match.group(1))
        if rate_number in rates:
            fail(f"{label}: duplicate contract rate {rate_number}")
        rates[rate_number] = parse_german_decimal(
            cells[2].split("%", 1)[0],
            f"{label} contract rate {rate_number}",
        )
    if set(rates) != set(range(1, 8)):
        fail(f"{label}: contract must contain one complete seven-rate table")
    return rates


def german_currency(value: Decimal) -> str:
    formatted = f"{value:,.2f}"
    return formatted.replace(",", "\0").replace(".", ",").replace("\0", ".")


def assert_no_case_meta(text: str, label: str) -> None:
    match = CASE_META_RE.search(text)
    if match is not None:
        fail(f"{label} contains a case-meta tell: {match.group(0)}")


def verify_case_documents() -> None:
    cent = Decimal("0.01")
    for name in CONTRACTS:
        directory = ROOT / "vertragsdokumente" / name
        contract = (directory / f"{name}.md").read_text(encoding="utf-8")
        report = (directory / f"{name}-bautenstandsbericht.md").read_text(encoding="utf-8")
        request = (directory / f"{name}-zahlungsanforderung.md").read_text(encoding="utf-8")
        profile = CASE_PROFILES[name]

        if not report.startswith("# Bautenstandsbericht\n"):
            fail(f"{name}: report title is not neutral and exact")
        if not request.startswith("# Zahlungsanforderung\n"):
            fail(f"{name}: payment-request title is not neutral and exact")
        for document_label, document in (
            ("contract", contract),
            ("report", report),
            ("payment request", request),
        ):
            assert_no_case_meta(document, f"{name} {document_label}")
            for key in ("project_token", "unit_token"):
                if str(profile[key]) not in document:
                    fail(
                        f"{name}: {document_label} lacks profile identity "
                        f"{profile[key]}"
                    )
        required_contract_phrase = profile["required_contract_phrase"]
        if required_contract_phrase and required_contract_phrase not in contract:
            fail(f"{name}: contract lost its no-advance-payment safeguard")
        required_request_phrase = profile["required_request_phrase"]
        if required_request_phrase and required_request_phrase not in request:
            fail(f"{name}: payment request contradicts its no-advance-payment safeguard")
        if required_contract_phrase:
            for document_label, document in (
                ("contract", contract),
                ("payment request", request),
            ):
                if PRE_NOTARIZATION_PAYMENT_RE.search(document):
                    fail(
                        f"{name}: {document_label} records a payment before notarisation"
                    )

        report_id = required_match(
            r"^\*\*Berichtsnummer:\*\*\s+(.+?)\s*$",
            report,
            f"{name} report number",
        ).group(1)
        report_id = markdown_field(report_id)
        if report_id not in request:
            fail(f"{name}: payment request does not identify its report")
        report_rate_match = re.search(r"/(\d{2})$", report_id)
        if report_rate_match is None or int(report_rate_match.group(1)) != int(
            profile["rate_number"]
        ):
            fail(f"{name}: report number does not encode its contract rate")

        report_date_text = required_match(
            r"^\*\*Berichtsdatum:\*\*\s+(.+?)\s*$",
            report,
            f"{name} report date",
        ).group(1)
        request_date_text = required_match(
            r"^[A-ZÄÖÜ][A-Za-zÄÖÜäöüß -]+, den (.+?)$",
            request,
            f"{name} payment-request date",
        ).group(1)
        report_date = parse_german_date(report_date_text, f"{name} report")
        request_date = parse_german_date(request_date_text, f"{name} payment request")
        if report_date > request_date:
            fail(f"{name}: payment request predates its report")
        due_date_text = required_match(
            r"bis zum \*\*(.+?)\*\*",
            request,
            f"{name} payment due date",
        ).group(1)
        due_date = parse_german_date(due_date_text, f"{name} payment due date")
        if due_date <= request_date:
            fail(f"{name}: payment due date is not after the request date")
        if f"{report_id} vom {markdown_field(report_date_text)}" not in request:
            fail(f"{name}: attachment line does not match report number and date")

        contract_urn = required_match(
            r"UR-Nr\.\s*([0-9]+/\d{4}\s+[A-Z]+)",
            contract,
            f"{name} contract deed number",
        ).group(1)
        for document_label, document in (("report", report), ("payment request", request)):
            if contract_urn not in document:
                fail(f"{name}: {document_label} does not match contract deed number")

        rows = payment_rows(request, name)
        total_label, total_percent, total_amount = rows[0]
        previous_label, previous_percent, previous_amount = rows[1]
        rate_label, rate_percent, rate_amount = rows[2]
        cumulative_label, cumulative_percent, cumulative_amount = rows[3]
        if "Gesamtkaufpreis" not in total_label or total_percent != Decimal("100.0"):
            fail(f"{name}: malformed total-price row")
        if "bisher" not in previous_label.lower() or "Rate" not in rate_label:
            fail(f"{name}: malformed prior-payment or current-rate row")
        if "kumuliert" not in cumulative_label.lower():
            fail(f"{name}: malformed cumulative-payment row")
        formatted_total = german_currency(total_amount)
        if (
            formatted_total not in contract
            and formatted_total.replace(".", " ") not in contract
        ):
            fail(f"{name}: payment-request total does not match the contract price")
        rate_number_match = re.search(r"(\d+)\.\s*Rate", rate_label)
        if rate_number_match is None:
            fail(f"{name}: current payment row lacks its contract rate number")
        rate_number = int(rate_number_match.group(1))
        if rate_number != int(profile["rate_number"]):
            fail(f"{name}: payment request addresses the wrong profile rate")
        contract_rates = contract_rate_percentages(contract, name)
        if sum(contract_rates.values(), Decimal("0")) != Decimal("100.0"):
            fail(f"{name}: contract rate percentages do not total 100 percent")
        if contract_rates.get(rate_number) != rate_percent:
            fail(f"{name}: requested rate percentage does not match the contract")
        expected_previous_percent = sum(
            (contract_rates[index] for index in range(1, rate_number)),
            Decimal("0"),
        )
        if previous_percent != expected_previous_percent:
            fail(f"{name}: prior-payment percentage does not match earlier contract rates")
        expected_cumulative_percent = expected_previous_percent + contract_rates[rate_number]
        if cumulative_percent != expected_cumulative_percent:
            fail(f"{name}: cumulative percentage does not match the contract rate sequence")
        if (total_amount * previous_percent / 100).quantize(cent) != previous_amount:
            fail(f"{name}: prior-payment arithmetic is inconsistent")
        if (total_amount * rate_percent / 100).quantize(cent) != rate_amount:
            fail(f"{name}: current-rate arithmetic is inconsistent")
        if previous_amount + rate_amount != cumulative_amount:
            fail(f"{name}: cumulative euro amount is inconsistent")
        if previous_percent + rate_percent != cumulative_percent:
            fail(f"{name}: cumulative percentage is inconsistent")
        if request.count(german_currency(rate_amount)) < 2:
            fail(f"{name}: requested amount is not repeated consistently in prose")
        expected_security = profile["security_amount"]
        if expected_security is not None and german_currency(expected_security) not in request:
            fail(f"{name}: stated completion security does not equal five percent")

        report_rows = [
            line
            for line in report.splitlines()
            if line.startswith("| ")
            and not line.startswith("| ---")
            and "Leistungsbereich" not in line
        ]
        if len(report_rows) < 3:
            fail(f"{name}: report has too few itemized findings")

        for suffix in CASE_DOCUMENT_SUFFIXES:
            path = directory / f"{name}{suffix}.pdf"
            assert_no_case_meta(pdf_text(path), f"{name}{suffix}.pdf")
            verify_single_page_a4(path)

    print(
        "check_contract_builds: case documents ok "
        f"({len(CONTRACTS)} reports, {len(CONTRACTS)} payment requests)"
    )


def pdf_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", str(path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return canonical_text(result.stdout)


def verify_single_page_a4(path: Path) -> None:
    result = subprocess.run(
        ["pdfinfo", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    pages = re.search(r"(?m)^Pages:\s+(\d+)\s*$", result)
    page_size = re.search(r"(?m)^Page size:\s+(.+?)\s*$", result)
    if pages is None or pages.group(1) != "1":
        fail(f"case letter must remain a single page: {path.name}")
    if page_size is None or "(A4)" not in page_size.group(1):
        fail(f"case letter is not rendered on A4: {path.name}")


def docx_text(path: Path) -> str:
    with ZipFile(path) as archive:
        try:
            document = archive.read("word/document.xml")
        except KeyError:
            fail(f"DOCX lacks word/document.xml: {path}")

    root = ET.fromstring(document)
    qn = lambda name: f"{{{WORD_NS}}}{name}"
    paragraphs: list[str] = []
    for paragraph in root.iter(qn("p")):
        parts: list[str] = []
        for node in paragraph.iter():
            if node.tag == qn("t"):
                parts.append(node.text or "")
            elif node.tag == qn("tab"):
                parts.append("\t")
            elif node.tag in {qn("br"), qn("cr")}:
                parts.append("\n")
        paragraphs.append("".join(parts))
    return canonical_text("\n".join(paragraphs))


def archive_pdf_texts(path: Path, scratch: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    scratch.mkdir(parents=True, exist_ok=True)
    with ZipFile(path) as archive:
        names = sorted(name for name in archive.namelist() if not name.endswith("/"))
        for index, name in enumerate(names):
            if not name.lower().endswith(".pdf"):
                fail(f"unexpected non-PDF ZIP member in {path.name}: {name}")
            extracted = scratch / f"{index:02d}-{Path(name).name}"
            extracted.write_bytes(archive.read(name))
            result[name] = pdf_text(extracted)
    return result


def verify_zip_structures() -> None:
    for name, expected_members in ZIP_MEMBERS.items():
        path = ROOT / "vertragsdokumente" / name / f"{name}-einzel-pdfs.zip"
        with ZipFile(path) as archive:
            members = [item.filename for item in archive.infolist()]
            if len(members) != len(set(members)):
                fail(f"ZIP contains duplicate member names: {path.name}")
            if tuple(sorted(members)) != tuple(sorted(expected_members)):
                fail(
                    f"ZIP member list is not exact for {path.name}: "
                    + ", ".join(members)
                )
            for item in archive.infolist():
                member = Path(item.filename)
                if item.is_dir() or member.name != item.filename or item.file_size == 0:
                    fail(f"unsafe, nested or empty ZIP member in {path.name}: {item.filename}")
                if not archive.read(item.filename).startswith(b"%PDF-"):
                    fail(f"ZIP member is not a PDF document: {path.name}:{item.filename}")
            exact_sources = {
                expected_members[2]: (
                    ROOT
                    / "vertragsdokumente"
                    / name
                    / f"{name}-bautenstandsbericht.pdf"
                ),
                expected_members[3]: (
                    ROOT
                    / "vertragsdokumente"
                    / name
                    / f"{name}-zahlungsanforderung.pdf"
                ),
            }
            for member_name, source_path in exact_sources.items():
                if archive.read(member_name) != source_path.read_bytes():
                    fail(
                        f"ZIP support document differs from its public PDF: "
                        f"{path.name}:{member_name}"
                    )
        with tempfile.TemporaryDirectory(prefix=f"btv-zip-{name}-") as temporary:
            texts = archive_pdf_texts(path, Path(temporary))
        if not texts[expected_members[2]].startswith("Bautenstandsbericht"):
            fail(f"ZIP report has the wrong visible title: {path.name}")
        if not texts[expected_members[3]].startswith("Zahlungsanforderung"):
            fail(f"ZIP payment request has the wrong visible title: {path.name}")
        for member_name, text in texts.items():
            assert_no_case_meta(text, f"{path.name}:{member_name}")
    print(f"check_contract_builds: ZIP structures ok ({len(ZIP_MEMBERS)} archives)")


def extract_provenance(value: str, label: str) -> str:
    matches = set(re.findall(rf"{PROVENANCE_PREFIX}([0-9a-f]{{64}})", value))
    if len(matches) != 1:
        fail(f"missing or ambiguous bilingual source provenance: {label}")
    return matches.pop()


def html_provenance(path: Path) -> str:
    return extract_provenance(path.read_text(encoding="utf-8"), path.name)


def pdf_provenance(path: Path) -> str:
    if shutil.which("pdfinfo") is None:
        fail("missing build dependency: pdfinfo")
    result = subprocess.run(
        ["pdfinfo", str(path)], check=True, capture_output=True, text=True
    )
    return extract_provenance(result.stdout, path.name)


def docx_provenance(path: Path) -> str:
    with ZipFile(path) as archive:
        try:
            core = ET.fromstring(archive.read("docProps/core.xml"))
        except KeyError:
            fail(f"DOCX lacks docProps/core.xml: {path.name}")
    metadata = " ".join(
        filter(
            None,
            [
                core.findtext("dc:description", default="", namespaces=CORE_NS),
                core.findtext("cp:keywords", default="", namespaces=CORE_NS),
            ],
        )
    )
    return extract_provenance(metadata, path.name)


def verify_bilingual_provenance() -> None:
    for name in CONTRACTS:
        directory = ROOT / "vertragsdokumente" / name
        expected = sha256(directory / f"{name}.md")
        artifacts = {
            "HTML": html_provenance(directory / f"{name}-de-en.html"),
            "PDF": pdf_provenance(directory / f"{name}-de-en.pdf"),
            "DOCX": docx_provenance(directory / f"{name}-de-en.docx"),
        }
        stale = [kind for kind, digest in artifacts.items() if digest != expected]
        if stale:
            fail(
                f"stale bilingual artifacts for {name}: {', '.join(stale)} "
                f"do not match {name}.md"
            )
    print(
        "check_contract_builds: bilingual provenance ok "
        f"({len(CONTRACTS) * 3} artifacts)"
    )


def compare_text(label: str, committed: str, rebuilt: str) -> None:
    if committed != rebuilt:
        fail(f"stale or divergent generated content: {label}")


def compare_contract(name: str, temporary_root: Path) -> tuple[int, str]:
    committed_dir = ROOT / "vertragsdokumente" / name
    rebuilt_dir = temporary_root / name
    shutil.copytree(committed_dir, rebuilt_dir)

    build_script = rebuilt_dir / "build.sh"
    build = subprocess.run(
        [str(build_script)],
        cwd=rebuilt_dir,
        check=False,
        capture_output=True,
        text=True,
    )
    if build.returncode != 0:
        details = "\n".join(
            part.strip() for part in (build.stdout, build.stderr) if part.strip()
        )
        fail(f"rebuild failed for {name}:\n{details}")

    committed_pdf = committed_dir / f"{name}.pdf"
    rebuilt_pdf = rebuilt_dir / f"{name}.pdf"
    compare_text(f"{name}.pdf", pdf_text(committed_pdf), pdf_text(rebuilt_pdf))

    committed_docx = committed_dir / f"{name}.docx"
    rebuilt_docx = rebuilt_dir / f"{name}.docx"
    compare_text(f"{name}.docx", docx_text(committed_docx), docx_text(rebuilt_docx))

    for suffix in CASE_DOCUMENT_SUFFIXES:
        filename = f"{name}{suffix}.pdf"
        compare_text(
            filename,
            pdf_text(committed_dir / filename),
            pdf_text(rebuilt_dir / filename),
        )

    archive_name = f"{name}-einzel-pdfs.zip"
    committed_zip = archive_pdf_texts(
        committed_dir / archive_name, temporary_root / f"committed-{name}"
    )
    rebuilt_zip = archive_pdf_texts(
        rebuilt_dir / archive_name, temporary_root / f"rebuilt-{name}"
    )
    if committed_zip.keys() != rebuilt_zip.keys():
        fail(f"ZIP member list differs after rebuild: {archive_name}")
    for member in committed_zip:
        compare_text(
            f"{archive_name}:{member}", committed_zip[member], rebuilt_zip[member]
        )
    build_log = "\n".join(
        part.strip() for part in (build.stdout, build.stderr) if part.strip()
    )
    return 2 + len(CASE_DOCUMENT_SUFFIXES) + len(committed_zip), build_log


def build_worker_count() -> int:
    raw_value = os.environ.get("BTV_BUILD_WORKERS", str(len(CONTRACTS)))
    try:
        value = int(raw_value)
    except ValueError:
        fail(f"BTV_BUILD_WORKERS must be an integer, got: {raw_value}")
    return max(1, min(len(CONTRACTS), value))


def rebuild_contracts() -> None:
    missing = [tool for tool in REQUIRED_TOOLS if shutil.which(tool) is None]
    if missing:
        fail(f"missing build dependencies: {', '.join(missing)}")

    artifact_count = 0
    with tempfile.TemporaryDirectory(prefix="btv-contract-builds-") as temporary:
        temporary_root = Path(temporary)
        shutil.copy2(
            ROOT / "vertragsdokumente" / "case-style.css",
            temporary_root / "case-style.css",
        )
        with ThreadPoolExecutor(max_workers=build_worker_count()) as executor:
            futures = {
                name: executor.submit(compare_contract, name, temporary_root)
                for name in CONTRACTS
            }
            for name in CONTRACTS:
                compared, build_log = futures[name].result()
                artifact_count += compared
                if build_log:
                    print(f"[{name}]\n{build_log}")

    print(
        "check_contract_builds: ok "
        f"({len(CONTRACTS)} contracts, {artifact_count} content comparisons)"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--rebuild",
        action="store_true",
        help="Also rebuild German PDF, DOCX and ZIP files in a temporary directory.",
    )
    mode.add_argument(
        "--write",
        action="store_true",
        help="After a successful local rebuild, rewrite the SHA-256 manifest.",
    )
    args = parser.parse_args()

    if args.write:
        write_manifest()
        verify_manifest(check_artifacts=False)
        return

    verify_manifest()
    if args.rebuild:
        rebuild_contracts()


if __name__ == "__main__":
    main()
