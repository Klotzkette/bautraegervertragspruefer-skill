#!/usr/bin/env python3
"""Validate the structured case-law anchor table, optionally including URLs."""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from threading import BoundedSemaphore
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
    "www.rechtsinformationen.bund.de",
    "gesetze.berlin.de",
    "nrwe.justiz.nrw.de",
    "www.gesetze-bayern.de",
    "www.landesrecht-bw.de",
    "rechtsprechung.hessen.de",
    "rechtsprechung.niedersachsen.de",
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

HOST_SEMAPHORES = {
    host: BoundedSemaphore(
        1 if host in {"dejure.org", "openjur.de", "www.openjur.de"} else 4
    )
    for host in ALLOWED_HOSTS
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
    "V ZR 132/23",  # Gesamt-GdWE bündelt Ansprüche auch bei Untergemeinschaften
    "V ZR 75/18",  # Warnpflichten des bauträgernahen Verwalters
    "VII ZR 388/00",  # Vollstreckungsunterwerfung mit Nachweisverzicht
}


class SourceCheckError(RuntimeError):
    pass


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


@lru_cache(maxsize=1)
def skill_version() -> str:
    match = re.search(
        r'^\s+version:\s+"([^"]+)"',
        SKILL.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    return match.group(1) if match else "dev"


def worker_count() -> int:
    raw_value = os.environ.get("BTV_URL_WORKERS", "8")
    try:
        value = int(raw_value)
    except ValueError:
        fail(f"BTV_URL_WORKERS must be an integer, got: {raw_value}")
    return max(1, min(12, value))


def verify_url(url: str) -> None:
    headers = {
        "User-Agent": (
            f"bautraegervertragspruefer-source-check/{skill_version()} "
            "(+https://github.com/Klotzkette/bautraegervertragspruefer-skill)"
        ),
        "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.5",
    }
    parsed_url = urlparse(url)
    is_pdf = parsed_url.path.lower().endswith(".pdf")
    semaphore = HOST_SEMAPHORES[parsed_url.hostname or ""]
    last_error: Exception | None = None
    with semaphore:
        request_headers = dict(headers)
        request_headers["Range"] = "bytes=0-4095"
        for attempt in range(3):
            try:
                request = Request(url, headers=request_headers, method="GET")
                with urlopen(request, timeout=15) as response:
                    if response.status >= 400:
                        raise HTTPError(
                            url,
                            response.status,
                            "HTTP error",
                            response.headers,
                            None,
                        )
                    final_host = (urlparse(response.geturl()).hostname or "").lower()
                    if final_host not in ALLOWED_HOSTS:
                        raise SourceCheckError(
                            f"source URL redirects to disallowed host {final_host}: {url}"
                        )
                    payload = response.read(4096)
                    if not payload:
                        raise SourceCheckError(
                            f"source URL returns an empty document: {url}"
                        )
                    if is_pdf and not payload.startswith(b"%PDF-"):
                        raise SourceCheckError(
                            f"source URL does not return a PDF document: {url}"
                        )
                    return
            except HTTPError as exc:
                last_error = exc
                if (
                    exc.code in {408, 420, 425, 429, 500, 502, 503, 504}
                    and attempt < 2
                ):
                    base_delay = 1.0 if exc.code in {420, 429} else 0.4
                    time.sleep(base_delay * (2**attempt))
                    continue
                break
            except (URLError, TimeoutError) as exc:
                last_error = exc
                if attempt < 2:
                    time.sleep(0.4 * (2**attempt))
                    continue
                break
    raise SourceCheckError(f"source URL is not reachable: {url} ({last_error})")


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

    if len(rows) < 43:
        fail(f"expected at least 43 case-law rows, found {len(rows)}")

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
        try:
            with ThreadPoolExecutor(max_workers=worker_count()) as executor:
                # map preserves source-table order, so a failure remains reproducible.
                list(executor.map(verify_url, seen_urls))
        except SourceCheckError as exc:
            fail(str(exc))

    print(
        "check_legal_anchors: ok "
        f"({len(rows)} rows, {total_cases} dockets, {total_urls} URLs"
        f"{', online checked' if args.online else ''})"
    )


if __name__ == "__main__":
    main()
