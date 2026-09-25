#!/usr/bin/env python3
"""Check prompt packaging and Markdown integrity, not pretend LLM behavior."""

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def version(text):
    match = re.search(r'^  version: "([^"]+)"$', text, re.M)
    if not match:
        raise ValueError("Missing metadata.version")
    return match.group(1)


def check(text, label):
    errors = []
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"{label}: missing frontmatter")
    if not re.search(r"^name: [a-z0-9]+(?:-[a-z0-9]+)*$", text, re.M):
        errors.append(f"{label}: invalid skill name")
    if not re.search(r"^description: .+", text, re.M):
        errors.append(f"{label}: missing description")
    if "\x00" in text or "\ufeff" in text or "\r" in text:
        errors.append(f"{label}: invalid text encoding/control character")
    if not text.endswith("\n"):
        errors.append(f"{label}: missing final newline")
    fence = None
    headings = []
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            fence = None if fence == marker[1][0] else marker[1][0]
            continue
        if fence:
            continue
        heading = re.match(r"^(#{1,6}) (.+)$", line)
        if heading:
            headings.append((len(heading[1]), heading[2]))
    if fence:
        errors.append(f"{label}: unclosed fence")
    if sum(level == 1 for level, _ in headings) != 1:
        errors.append(f"{label}: expected one document title")
    for before, after in zip(headings, headings[1:]):
        if after[0] > before[0] + 1:
            errors.append(f"{label}: heading skips a level: {after[1]}")
    duplicate = [name for name, count in Counter(name for _, name in headings).items() if count > 1]
    if duplicate:
        errors.append(f"{label}: duplicate headings: {duplicate}")
    if re.search(r"turn\d+(?:search|view)\d+|\[wordlim|\[TODO:", text):
        errors.append(f"{label}: internal/scaffold residue")
    # Copied prompts must not rely on other local files.
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)\n]+)\)", text):
        if not target.startswith(("https://", "http://", "#")):
            errors.append(f"{label}: non-portable dependency: {target}")
    return errors


def main():
    full = (ROOT / "skill/SKILL.md").read_text()
    mini = (ROOT / "skill/MINI_SKILL.md").read_text()
    errors = check(full, "Werkstatt") + check(mini, "Mini")
    if version(mini) != version(full) + "-mini":
        errors.append("Full/mini versions differ")
    if len(mini) > 18000:
        errors.append(f"Mini exceeds the published 18,000-character budget: {len(mini)}")
    for name in ("SKILL.md", "MINI_SKILL.md"):
        if (ROOT / "skill" / name).read_bytes() != (ROOT / "docs" / name).read_bytes():
            errors.append(f"Prompt mirror differs: {name}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Prompt structure and portability: OK (workshop {len(full)} chars; mini {len(mini)} chars). No LLM claim.")


if __name__ == "__main__":
    main()
