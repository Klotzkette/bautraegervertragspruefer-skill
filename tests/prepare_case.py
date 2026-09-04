#!/usr/bin/env python3
"""Prepare an input-only evaluation folder; no answer keys or case labels."""

import argparse
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]


def input_paths(config, scenario, contract_format="docx"):
    case = config["cases"][scenario["case"]]
    stem = case["stem"] + ("-de-en" if scenario.get("bilingual") else "")
    paths = [f"{case['directory']}/{stem}.{contract_format}"]
    paths += [f"{case['directory']}/{case['stem']}-{name}.md"
              for name in scenario["attachments"]]
    return paths + scenario["inputs"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--out", type=Path, required=True,
                        help="new, not-yet-existing output directory")
    parser.add_argument("--format", choices=["docx", "md", "pdf"], default="docx")
    args = parser.parse_args()
    config = json.loads((ROOT / "tests/szenarien.json").read_text(encoding="utf-8"))
    scenario = next((s for s in config["scenarios"] if s["id"] == args.scenario), None)
    if scenario is None:
        parser.error("unknown scenario; see tests/szenarien.json")
    if scenario.get("word_only") and args.format != "docx":
        parser.error("this scenario measures Word reading and requires DOCX")
    if scenario.get("bilingual") and args.format == "md":
        parser.error("no bilingual Markdown artifact exists")
    paths = input_paths(config, scenario, args.format)
    sources = [(ROOT / path).resolve() for path in paths]
    for source in sources:
        if not source.is_relative_to(ROOT) or not source.is_file():
            parser.error(f"missing/invalid input: {source}")
        if source.name in {"README.md", "erwartungsmatrix.md", "erwartungen.json"}:
            parser.error("answer or README leakage into inputs")
    if len({source.name for source in sources}) != len(sources):
        parser.error("duplicate destination name")
    if args.out.exists():
        parser.error("output directory already exists; choose a new directory")
    args.out.mkdir(parents=True)
    for source in sources:
        shutil.copy2(source, args.out / source.name)
    inventory = "# Vorgelegte Dokumente\n\n"
    inventory += "Bearbeite den Auftrag aus den beigefügten Sachverhaltsdateien. "
    inventory += "Spätere Ergänzungen gelten nur für den ausdrücklich bezeichneten Fall.\n\n"
    inventory += "\n".join(f"- {source.name}" for source in sources) + "\n"
    (args.out / "00-dokumentliste.md").write_text(inventory, encoding="utf-8")
    print(f"{len(sources)} inputs and document list prepared: {args.out.resolve()}")
    print("No answer key copied. No model evaluation performed.")


if __name__ == "__main__":
    main()
