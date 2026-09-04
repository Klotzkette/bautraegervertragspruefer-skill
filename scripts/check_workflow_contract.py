#!/usr/bin/env python3
"""Validate discoverable skill entrypoints and executable helper packaging."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/bautraegervertragspruefer"
EXPECTED = {
    "bautraegervertrag-pruefen": "references/werkstatt.md",
    "bautraeger-zahlungsrate-pruefen": "scripts/mabv_rechner.py",
    "bautraeger-word-entwurf-pruefen": "scripts/docx_pruefen.py",
}


def main():
    manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
    claude = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
    version = re.search(r'^  version: "([^"]+)"$', (ROOT / "skill/SKILL.md").read_text(), re.M)[1]
    errors = []
    if manifest["name"] != PLUGIN.name or manifest["version"] != version or claude["version"] != version:
        errors.append("Plugin identity/version differs from prompt")
    found = {p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")}
    if found != set(EXPECTED):
        errors.append(f"Skill entrypoints differ: {found}")
    for name, resource in EXPECTED.items():
        directory = PLUGIN / "skills" / name
        text = (directory / "SKILL.md").read_text()
        if f"name: {name}\n" not in text:
            errors.append(f"Skill name differs from folder: {name}")
        description = re.search(r"^description: (.+)$", text, re.M)
        if not description or len(description[1]) > 1024:
            errors.append(f"Missing or excessive discovery description: {name}")
        metadata = (directory / "agents/openai.yaml").read_text()
        if f"${name}" not in metadata:
            errors.append(f"Default prompt does not invoke its skill: {name}")
        if not (directory / resource).is_file():
            errors.append(f"Missing runnable/reference resource: {name}/{resource}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("https://", "#")):
                continue
            resolved = (directory / target).resolve()
            if not resolved.is_relative_to(PLUGIN) or not resolved.is_file():
                errors.append(f"Broken/non-contained skill reference: {name}: {target}")
    prompts = manifest["interface"]["defaultPrompt"]
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3 or any(len(p) > 128 for p in prompts):
        errors.append("Invalid plugin starter prompts")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Plugin routing/package: OK (3 separate entrypoints, local references and helpers). Behavioral evaluation is separate.")


if __name__ == "__main__":
    main()
