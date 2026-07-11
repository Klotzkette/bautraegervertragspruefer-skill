#!/usr/bin/env python3
"""Validate local Markdown links, heading anchors and the Pages navigation."""

from __future__ import annotations

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\n]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data"}


def github_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"\s", "-", value)


def visible_markdown(text: str) -> str:
    """Blank fenced code while preserving line numbers for diagnostics."""
    visible: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
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


def heading_anchors(text: str) -> set[str]:
    counts: Counter[str] = Counter()
    anchors: set[str] = set()
    for match in HEADING_RE.finditer(text):
        base = github_slug(match.group(1))
        if not base:
            continue
        index = counts[base]
        counts[base] += 1
        anchors.add(base if index == 0 else f"{base}-{index}")
    return anchors


def link_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1 : raw.index(">")]
    return raw.split(maxsplit=1)[0]


def inside_repo(path: Path) -> bool:
    try:
        path.resolve().relative_to(ROOT)
    except ValueError:
        return False
    return True


def resolve_local(source: Path, target: str) -> tuple[Path, str]:
    parsed = urlparse(target)
    fragment = unquote(parsed.fragment)
    path_text = unquote(parsed.path)
    destination = source if not path_text else source.parent / path_text
    return destination.resolve(), fragment


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[tuple[str, int]] = []
        self.links: list[tuple[str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        line, _ = self.getpos()
        if values.get("id"):
            self.ids.append((values["id"] or "", line))
        if tag == "a" and values.get("href") is not None:
            self.links.append((values["href"] or "", line))


def main() -> None:
    errors: list[str] = []
    markdown_links = 0
    html_links = 0

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    anchor_cache: dict[Path, set[str]] = {}

    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        visible = visible_markdown(text)
        anchor_cache[source.resolve()] = heading_anchors(visible)
        for match in LINK_RE.finditer(visible):
            markdown_links += 1
            target = link_target(match.group(1))
            line = visible.count("\n", 0, match.start()) + 1
            label = f"{source.relative_to(ROOT)}:{line} -> {target}"
            if not target:
                errors.append(f"empty Markdown link: {label}")
                continue
            parsed = urlparse(target)
            if parsed.scheme.lower() in EXTERNAL_SCHEMES:
                continue
            destination, fragment = resolve_local(source, target)
            if not inside_repo(destination):
                errors.append(f"path escapes repository: {label}")
                continue
            if not destination.exists():
                errors.append(f"missing local target: {label}")
                continue
            if fragment and destination.suffix.lower() == ".md":
                anchors = anchor_cache.get(destination)
                if anchors is None:
                    target_text = destination.read_text(encoding="utf-8")
                    anchors = heading_anchors(visible_markdown(target_text))
                    anchor_cache[destination] = anchors
                if fragment not in anchors:
                    errors.append(f"missing Markdown anchor #{fragment}: {label}")

    page = ROOT / "docs" / "index.html"
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    id_counts = Counter(value for value, _ in parser.ids)
    for value, count in id_counts.items():
        if count > 1:
            errors.append(f"duplicate HTML id in docs/index.html: {value} ({count}x)")

    page_ids = set(id_counts)
    for target, line in parser.links:
        html_links += 1
        parsed = urlparse(target)
        if parsed.scheme.lower() in EXTERNAL_SCHEMES:
            continue
        label = f"docs/index.html:{line} -> {target}"
        if not target:
            errors.append(f"empty HTML link: {label}")
            continue
        destination, fragment = resolve_local(page, target)
        if not inside_repo(destination):
            errors.append(f"path escapes repository: {label}")
            continue
        if not destination.exists():
            errors.append(f"missing local target: {label}")
            continue
        if destination == page.resolve() and fragment and fragment not in page_ids:
            errors.append(f"missing HTML anchor #{fragment}: {label}")

    if errors:
        print("FAIL navigation:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)

    print(
        "check_navigation: ok "
        f"({len(markdown_files)} Markdown files, {markdown_links} Markdown links, "
        f"{html_links} Pages links)"
    )


if __name__ == "__main__":
    main()
