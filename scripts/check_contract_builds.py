#!/usr/bin/env python3
"""Rebuild German contract artifacts and detect stale committed outputs."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = (
    "bautraegervertrag",
    "bautraegervertrag-marewald",
    "bautraegervertrag-lindenhain",
)
REQUIRED_TOOLS = ("pandoc", "weasyprint", "perl", "zip", "pdftotext")
WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def fail(message: str) -> None:
    print(f"FAIL contract builds: {message}", file=sys.stderr)
    raise SystemExit(1)


def canonical_text(value: str) -> str:
    value = unicodedata.normalize("NFC", value).replace("\u00ad", "")
    value = re.sub(r"(?m)^\s*\d+\s*$", "", value)
    value = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", value)
    return re.sub(r"\s+", " ", value).strip()


def pdf_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", str(path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return canonical_text(result.stdout)


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


def compare_text(label: str, committed: str, rebuilt: str) -> None:
    if committed != rebuilt:
        fail(f"stale or divergent generated content: {label}")


def compare_contract(name: str, temporary_root: Path) -> int:
    committed_dir = ROOT / "vertragsdokumente" / name
    rebuilt_dir = temporary_root / name
    shutil.copytree(committed_dir, rebuilt_dir)

    build_script = rebuilt_dir / "build.sh"
    subprocess.run([str(build_script)], cwd=rebuilt_dir, check=True)

    committed_pdf = committed_dir / f"{name}.pdf"
    rebuilt_pdf = rebuilt_dir / f"{name}.pdf"
    compare_text(f"{name}.pdf", pdf_text(committed_pdf), pdf_text(rebuilt_pdf))

    committed_docx = committed_dir / f"{name}.docx"
    rebuilt_docx = rebuilt_dir / f"{name}.docx"
    compare_text(f"{name}.docx", docx_text(committed_docx), docx_text(rebuilt_docx))

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
    return 2 + len(committed_zip)


def main() -> None:
    missing = [tool for tool in REQUIRED_TOOLS if shutil.which(tool) is None]
    if missing:
        fail(f"missing build dependencies: {', '.join(missing)}")

    artifact_count = 0
    with tempfile.TemporaryDirectory(prefix="btv-contract-builds-") as temporary:
        temporary_root = Path(temporary)
        for name in CONTRACTS:
            artifact_count += compare_contract(name, temporary_root)

    print(
        "check_contract_builds: ok "
        f"({len(CONTRACTS)} contracts, {artifact_count} content comparisons)"
    )


if __name__ == "__main__":
    main()
