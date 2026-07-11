#!/usr/bin/env python3
"""Validate the structured case-law anchor table without network access."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "SKILL.md"

START = "## Aktuelle Rechtsprechungsanker"
END = "## Normenkarte"

ALLOWED_HOSTS = {
    "www.bundesgerichtshof.de",
    "juris.bundesgerichtshof.de",
    "www.rechtsprechung-im-internet.de",
    "gesetze.berlin.de",
    "www.landesrecht-bw.de",
    "voris.wolterskluwer-online.de",
    "dejure.org",
    "openjur.de",
    "www.openjur.de",
}

OFFICIAL_BGH_HOSTS = {
    "www.bundesgerichtshof.de",
    "juris.bundesgerichtshof.de",
    "www.rechtsprechung-im-internet.de",
}

CASE_RE = re.compile(r"(?<!\w)(?:[IVX]{1,4}|[0-9]{1,2})\s+(?:ZR|ZB|U)\s+\d+/\d{2}(?!\d)")
DATE_RE = re.compile(r"\b\d{2}\.\d{2}\.\d{4}\b")
URL_RE = re.compile(r"https://[^\s|]+")

FORBIDDEN = (
    "BeckRS",
    "beck-online",
    "[wordlim",
    "turn0search",
    "turn1search",
    "nicht quellenhart verifiziert",
)


def fail(message: str) -> None:
    print(f"FAIL legal anchors: {message}", file=sys.stderr)
    raise SystemExit(1)


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unquote(value).lower())


def extract_section(text: str) -> str:
    try:
        start = text.index(START)
        end = text.index(END, start)
    except ValueError as exc:
        fail(f"missing section marker: {exc}")
    return text[start:end]


def extract_urls(citation: str) -> list[str]:
    return [match.rstrip(".,;") for match in URL_RE.findall(citation)]


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    section = extract_section(text)

    for token in FORBIDDEN:
        if token in section:
            fail(f"forbidden token in anchor section: {token}")

    rows: list[tuple[int, list[str]]] = []
    for number, line in enumerate(section.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        columns = [part.strip() for part in line.strip().strip("|").split("|")]
        if columns[0] == "Thema" or all(set(column) <= {"-", ":"} for column in columns):
            continue
        if len(columns) != 4:
            fail(f"table line {number} has {len(columns)} columns instead of 4")
        rows.append((number, columns))

    if len(rows) < 30:
        fail(f"expected at least 30 case-law rows, found {len(rows)}")

    seen_cases: dict[str, int] = {}
    seen_urls: dict[str, int] = {}
    total_cases = 0
    total_urls = 0

    for line_number, columns in rows:
        topic, citation, holding, use = columns
        cases = CASE_RE.findall(citation)
        dates = DATE_RE.findall(citation)
        urls = extract_urls(citation)

        if not topic or len(topic) < 8:
            fail(f"line {line_number} has no meaningful topic")
        if not cases:
            fail(f"line {line_number} has no docket number: {topic}")
        if not dates:
            fail(f"line {line_number} has no decision date: {topic}")
        if "Urteil" not in citation and "Beschluss" not in citation:
            fail(f"line {line_number} has no decision form: {topic}")
        if not urls:
            fail(f"line {line_number} has no source URL: {topic}")
        if len(holding) < 60 or len(use) < 40:
            fail(f"line {line_number} has an underspecified holding/use: {topic}")

        hosts: set[str] = set()
        for url in urls:
            parsed = urlparse(url)
            if parsed.scheme != "https":
                fail(f"line {line_number} uses non-HTTPS URL: {url}")
            host = (parsed.hostname or "").lower()
            if host not in ALLOWED_HOSTS:
                fail(f"line {line_number} uses disallowed host {host}: {url}")
            hosts.add(host)
            if url in seen_urls:
                fail(f"duplicate URL on lines {seen_urls[url]} and {line_number}: {url}")
            seen_urls[url] = line_number
            total_urls += 1

            if "/SharedDocs/Entscheidungen/" in url:
                if not any(normalized(case) in normalized(url) for case in cases):
                    fail(f"BGH PDF filename does not match docket on line {line_number}: {url}")

        if "BGH" in citation and not (hosts & OFFICIAL_BGH_HOSTS):
            fail(f"BGH row lacks an official BGH/Bund source: {topic}")

        for case in cases:
            if case in seen_cases:
                fail(f"duplicate docket {case} on lines {seen_cases[case]} and {line_number}")
            seen_cases[case] = line_number
            total_cases += 1

    print(
        "check_legal_anchors: ok "
        f"({len(rows)} rows, {total_cases} dockets, {total_urls} URLs)"
    )


if __name__ == "__main__":
    main()
