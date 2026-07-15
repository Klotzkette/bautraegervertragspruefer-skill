#!/usr/bin/env python3
"""Guard the user-facing routing and legal decision gates of both skills."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FULL = ROOT / "skill" / "SKILL.md"
MINI = ROOT / "skill" / "MINI_SKILL.md"


@dataclass(frozen=True)
class Scenario:
    name: str
    full_markers: tuple[str, ...]
    mini_markers: tuple[str, ...] = ()


SCENARIOS = (
    Scenario(
        "skill_without_contract",
        ("nur Skill/Prompt, kein Vertrag", "nur den Upload anfordern"),
    ),
    Scenario(
        "contract_without_role",
        ("Vertrag liegt vor, Rolle unklar", "Rolle A vorläufig"),
        ("mit Vertrag A starten",),
    ),
    Scenario(
        "guided_review",
        ("Geführter Workflow", "höchstens sieben priorisierte Befunde"),
        ("Geführt = Kurzbild", "Nächste Weiche"),
    ),
    Scenario(
        "one_shot_package",
        ("Nutzer will `one-shot`, `final`, `alle Schreiben`", "Drei-Dokumente-Paket sofort"),
        ("Vollpaket bei `vollständig/one-shot/Schreiben/final`", "Vollpaket:"),
    ),
    Scenario(
        "payment_request",
        ("konkrete Rechnung, Ratenabruf oder Zahlungsfrist", "Zahlungsfreigabekarte"),
        ("Rechnung/Ratenabruf: sofort Zahlungsfreigabekarte",),
    ),
    Scenario(
        "stop",
        ("`stop`, `abbrechen`, `beenden`, `halt`, `cancel`", "sofort mit der festgelegten Beendigungszeile"),
        ("Bei `stop/abbrechen/beenden/halt/cancel`",),
    ),
    Scenario(
        "resume",
        ("Fortsetzungsprotokoll", "nächste feste Überschrift"),
        ("Fortsetzungsmarke",),
    ),
)

FULL_OUTPUT_MARKERS = (
    "Status: Rolle A/B/C",
    "Phasenentscheidung:",
    "Sperrende IDs:",
    "Frist/Termin:",
    "Nächster Beleg/Fortsetzen bei:",
    "Dokument 1 — Übersendungsschreiben",
    "Dokument 2 — Mandantengutachten",
    "Dokument 3 — Aufforderungsschreiben",
    "heutige Auswirkung",
    "Bis wann/benötigter Beleg",
)

MINI_OUTPUT_MARKERS = (
    "Käufer-/Mandantenschreiben",
    "Mandantengutachten",
    "Aufforderungsschreiben an Bauträger",
    "Entscheidung, Sperr-IDs, Frist, nächster Beleg/Fortsetzung",
)

TEMPORAL_MARKERS = (
    "Art. 229 § 5 EGBGB",
    "Art. 229 § 6 EGBGB",
    "Art. 229 § 39 EGBGB",
    "1. Dezember 2020",
    "§ 47 und § 48 WEG",
    "29. Dezember 2025",
    "§ 13a BeurkG a. F.",
    "§ 13c BeurkG",
    "Entscheidungs-Fit-Test",
    "Normstand:",
    "Vertragstyp und Rolle:",
    "Klausel und Anspruch:",
    "Verfahrenslage:",
)


def require(markers: tuple[str, ...], text: str, label: str, errors: list[str]) -> int:
    checks = 0
    for marker in markers:
        checks += 1
        if marker not in text:
            errors.append(f"{label}: missing {marker!r}")
    return checks


def main() -> None:
    full = FULL.read_text(encoding="utf-8")
    mini = MINI.read_text(encoding="utf-8")
    errors: list[str] = []
    checks = 0

    for scenario in SCENARIOS:
        checks += require(scenario.full_markers, full, f"full/{scenario.name}", errors)
        checks += require(scenario.mini_markers, mini, f"mini/{scenario.name}", errors)

    checks += require(FULL_OUTPUT_MARKERS, full, "full/output", errors)
    checks += require(MINI_OUTPUT_MARKERS, mini, "mini/output", errors)
    checks += require(TEMPORAL_MARKERS, full, "full/temporal", errors)

    mini_temporal = (
        "Vor 1.1.2002 Art.229 §§5/6 EGBGB",
        "vor 1.1.2018 Art.229 §39 EGBGB",
        "WEG ab 1.12.2020 §§47/48 WEG",
        "bis 28.12.2025 §13a a.F., danach §13c",
        "Fit = gesichert, Teilfit = Argument, sonst Prüfbedarf",
    )
    checks += require(mini_temporal, mini, "mini/temporal", errors)

    forbidden_absolutes = (
        "§13c statt §13a BeurkG",
        "Bezugsurkunden: §13c BeurkG; §13a betrifft E-Signatur",
    )
    for marker in forbidden_absolutes:
        checks += 1
        if marker in full or marker in mini:
            errors.append(f"obsolete time-blind rule remains: {marker!r}")

    if errors:
        print("FAIL workflow contract:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)

    print(f"check_workflow_contract: ok ({checks} scenario/output/legal checks)")


if __name__ == "__main__":
    main()
