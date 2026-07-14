#!/usr/bin/env python3
"""Validate the structured case-law anchor table, optionally including URLs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


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
    "dejure.org/dienste/vernetzung/rechtsprechung?",
    "[wordlim",
    "turn0search",
    "turn1search",
    "nicht quellenhart verifiziert",
)

REQUIRED_DOCKETS = {
    "VII ZR 84/09",  # Mängel-Einbehalt auch aus einer laufenden Bautenstandsrate
    "VII ZR 310/99",  # MaBV-Zahlungsplan: Grundsatzentscheidung
    "VII ZR 167/11",  # Bereicherungsausgleich
    "V ZR 182/12",  # DIN-Vermutung nur im WEG-Binnenrecht
    "V ZR 39/24",  # Wiederholung der WEG-DIN-Linie in den Gründen
    "V ZR 34/25",  # Technikraum kann trotz gemeinschaftsdienender Anlagen SE sein
    "V ZR 50/25",  # Kostenverteilung: Angemessenheit statt bloßer Willkürkontrolle
    "VII ZR 119/24",  # Koordination bei getrennter Planer-/Unternehmervergabe
    "V ZR 243/23",  # Erstherstellungsanspruch: Grundlinie
    "V ZR 219/24",  # Erstherstellungsanspruch: Umfang
    "V ZR 102/24",  # Erhaltungslast und GdWE-Kompetenz
    "V ZR 18/25",  # GdWE-Schadensersatz ohne Garantiehaftung
}


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


def verify_url(url: str) -> None:
    headers = {
        "User-Agent": "bautraegervertragspruefer-source-check/3.7 (+https://github.com/Klotzkette/bautraegervertragspruefer-skill)",
        "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.5",
    }
    last_error: Exception | None = None
    for method in ("HEAD", "GET"):
        request_headers = dict(headers)
        if method == "GET":
            request_headers["Range"] = "bytes=0-2047"
        try:
            request = Request(url, headers=request_headers, method=method)
            with urlopen(request, timeout=20) as response:
                if response.status >= 400:
                    fail(f"source URL returned HTTP {response.status}: {url}")
                if method == "GET":
                    payload = response.read(2048)
                    if urlparse(url).path.lower().endswith(".pdf") and not payload.startswith(
                        b"%PDF-"
                    ):
                        fail(f"source URL does not return a PDF document: {url}")
                return
        except HTTPError as exc:
            last_error = exc
            # Several official court portals reject or redirect HEAD even when
            # the same resource is available by GET. HEAD is only a fast path.
            if method == "HEAD":
                continue
            break
        except (URLError, TimeoutError) as exc:
            last_error = exc
            if method == "HEAD":
                continue
            break
    fail(f"source URL is not reachable: {url} ({last_error})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--online",
        action="store_true",
        help="Also request every cited source URL (not used in CI).",
    )
    args = parser.parse_args()

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

    if len(rows) < 40:
        fail(f"expected at least 40 case-law rows, found {len(rows)}")

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

    missing_required = sorted(REQUIRED_DOCKETS - set(seen_cases))
    if missing_required:
        fail(f"missing required case-law anchors: {', '.join(missing_required)}")

    unanchored = sorted(set(CASE_RE.findall(text)) - set(seen_cases))
    if unanchored:
        fail(f"case-law references outside the anchor table: {', '.join(unanchored)}")

    if args.online:
        for url in seen_urls:
            verify_url(url)

    print(
        "check_legal_anchors: ok "
        f"({len(rows)} rows, {total_cases} dockets, {total_urls} URLs"
        f"{', online checked' if args.online else ''})"
    )


if __name__ == "__main__":
    main()
