#!/usr/bin/env python3
"""Check test references and source-backed payment arithmetic, not model quality."""

import json
from decimal import Decimal
from pathlib import Path
import re
import sys

from prepare_case import input_paths


ROOT = Path(__file__).resolve().parents[1]
D = Decimal


def euro(value):
    return f"{D(value):,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def verify():
    config = json.loads((ROOT / "tests/szenarien.json").read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "tests/erwartungen.json").read_text(encoding="utf-8"))
    matrix = (ROOT / "tests/erwartungsmatrix.md").read_text(encoding="utf-8")
    ids = re.findall(r"^### ([AHML]\d{2})\b", matrix, re.MULTILINE)
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    require(len(ids) == len(set(ids)), "duplicate finding identifier")
    scenarios = config["scenarios"]
    require(len({s["id"] for s in scenarios}) == len(scenarios), "duplicate scenario identifier")
    used_ids = set()
    for scenario in scenarios:
        for finding in scenario["findings"]:
            used_ids.add(finding)
            require(finding in ids, f"{scenario['id']}: unknown finding {finding}")
        for relative in input_paths(config, scenario):
            source = ROOT / relative
            require(source.is_file(), f"{scenario['id']}: missing input {relative}")
            require(source.name not in {"README.md", "erwartungen.json", "erwartungsmatrix.md"},
                    f"{scenario['id']}: solution leaked into input list")
        require(scenario["phase"] != "entwurf" or not scenario["attachments"],
                f"{scenario['id']}: later payment documents mixed into draft scenario")
    require(set(ids) == used_ids, "matrix contains unused findings")

    checked_anchors = 0
    for key, case in expected["cases"].items():
        source_config = config["cases"][key]
        directory = ROOT / source_config["directory"]
        stem = source_config["stem"]
        documents = {"contract": (directory / f"{stem}.md").read_text(encoding="utf-8")}
        for kind in ("bautenstandsbericht", "zahlungsanforderung"):
            documents[kind] = (directory / f"{stem}-{kind}.md").read_text(encoding="utf-8")
        for anchor in case["anchors"]:
            require(anchor["text"] in documents[anchor["document"]],
                    f"{key} {anchor['location']}: source anchor changed: {anchor['text']}")
            checked_anchors += 1
        # Extract the seven actual contract-table percentages, not values repeated in prose.
        source_rates = []
        for line in documents["contract"].splitlines():
            cells = [cell.strip().replace("**", "") for cell in line.strip().strip("|").split("|")]
            if len(cells) == 3 and re.fullmatch(r"[1-7](?:\. Rate)?", cells[0]):
                match = re.fullmatch(r"([0-9]+[.,][0-9]+)\s*%", cells[2])
                if match:
                    source_rates.append(D(match.group(1).replace(",", ".")))
        rates = list(map(D, case["rates_percent"]))
        require(source_rates == rates, f"{key}: contract rate table differs from expected grouping")
        require(len(rates) == 7 and sum(rates) == 100, f"{key}: invalid seven-rate total")
        price = D(case["purchase_price"])
        called = case["called_rate"] - 1
        require(price * rates[called] / 100 == D(case["called_amount"]), f"{key}: called amount")
        require(price * sum(rates[:called]) / 100 == D(case["previous_amount"]), f"{key}: previous amount")
        require(D(case["previous_amount"]) + D(case["called_amount"]) == D(case["cumulative_amount"]),
                f"{key}: cumulative amount")
        require(price * D("0.05") == D(case["security"]), f"{key}: security amount")
        require(price * rates[0] / 100 - D(case["security"]) == D(case["first_rate_less_security"]),
                f"{key}: first rate less security")
        for field in ("purchase_price", "called_amount", "previous_amount", "cumulative_amount"):
            require(euro(case[field]) in documents["zahlungsanforderung"],
                    f"{key}: payment demand amount missing/changed ({field})")
        # 18.9% combines roof, three rough-installation trades and glazing from the remaining 70%.
        require(rates[2] == D("0.70") * (8 + 3 + 3 + 3 + 10), f"{key}: third-rate conversion")
        fourth_components = (6 + 3 + 3) if key == "L" else (6 + 3 + 4)
        require(rates[3] == D("0.70") * fourth_components, f"{key}: fourth-rate conversion")

    variation = expected["variations"]["L-S"]
    base, increase = D(variation["base_price"]), D(variation["increase"])
    require(increase > base * D(variation["threshold_percent"]) / 100, "L-S: threshold not crossed")
    require(base + increase == D(variation["new_price"]), "L-S: new price")
    require(increase * D("0.05") == D(variation["additional_security"]), "L-S: added security")
    require((base + increase) * D("0.05") == D(variation["total_security"]), "L-S: total security")
    reservation = expected["variations"]["H-Z"]
    require(D(expected["cases"]["H"]["previous_amount"]) + D(reservation["reservation_fee"]) ==
            D(reservation["cash_paid_including_reservation"]), "H-Z: reservation cash reconciliation")
    if errors:
        print("FAILED\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"PASS: {len(scenarios)} scenarios, {len(ids)} findings, {checked_anchors} source anchors; "
          "three rate tables, payment demands and variation arithmetic consistent.")
    print("Static fixture checks only. No AI test run and no legal certification.")
    return 0


if __name__ == "__main__":
    sys.exit(verify())
