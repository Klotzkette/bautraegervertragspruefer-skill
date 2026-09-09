#!/usr/bin/env python3
"""Static regression for explicit limitation instructions and blind fixtures, not LLM quality."""

import json
from pathlib import Path
import re
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/limitation"
PLUGIN_REFERENCE = "skills/bautraegervertrag-pruefen/references/werkstatt.md"

# This is an instruction-presence contract, deliberately not an answer grader.
# Keep spelling/spacing variants possible; an occurrence cannot prove correct legal reasoning.
REQUIRED_CONTROLS = {
    "building_default": r"§\s*634a\s*Abs\.?\s*1\s*Nr\.?\s*2",
    "five_years": r"(?:fünf|5)\s*Jahre?\b",
    "acceptance_start": r"(?:ab|mit|Beginn.{0,40})\s+(?:(?:wirksamer?|maßgeblicher?)\s+)?Abnahme",
    "consumer_terms": r"Verbraucher.{0,20}AGB|AGB.{0,20}Verbraucher",
    "absolute_clause_ban": r"§\s*309\s*Nr\.?\s*8\s*(?:Buchst\.?\s*)?b\s*(?:Doppelbuchst\.?\s*)?ff\b",
    "two_year_clause": r"(?:zwei|2)\s*Jahre?\b|Zweijahres",
    "early_start": r"(?:früher\w*|vorgezogen\w*|vorverlegt\w*)\s+(?:Verjährungs|Frist)?Beginn|Beginn.{0,30}(?:vorziehen|vorverlegen)",
    "hidden_cutoff": r"Ausschlussfrist|Mängelanzeigefrist",
    "notice_clause_ban": r"\bee\b",
    "genuine_negotiation": r"(?:echt\w*\s+)?Aushandeln|Individualvereinbarung|Individualabrede",
    "non_building_control": r"nicht\s+bauwerksbezogen\w*|Nichtbauwerk|sonstige\w*\s+Werk",
    "no_650o_overclaim": r"§\s*650o",
}


def missing_controls(text):
    normalized = re.sub(r"\s+", " ", text.replace("**", ""))
    return [name for name, pattern in REQUIRED_CONTROLS.items()
            if not re.search(pattern, normalized, re.IGNORECASE)]


class PromptLimitationTests(unittest.TestCase):
    def test_both_standalone_prompts_have_explicit_controls(self):
        for name in ("SKILL.md", "MINI_SKILL.md"):
            with self.subTest(prompt=name):
                self.assertEqual(missing_controls((ROOT / "skill" / name).read_text(encoding="utf-8")), [])

    def test_generic_limitation_reminder_is_insufficient(self):
        old_style = (
            "Mängelverjährung regelmäßig § 634a Abs. 1 Nr. 2 und wirksame Abnahme. "
            "Haftung und Verjährung nach § 309 Nr. 7/8 prüfen. "
            "Keine pauschale 30-Jahres-Frist."
        )
        missing = missing_controls(old_style)
        self.assertIn("absolute_clause_ban", missing)
        self.assertIn("two_year_clause", missing)
        self.assertIn("five_years", missing)

    def test_downloads_and_plugin_contain_current_instructions(self):
        for name in ("SKILL.md", "MINI_SKILL.md"):
            with self.subTest(download=name):
                self.assertEqual((ROOT / "skill" / name).read_bytes(), (ROOT / "docs" / name).read_bytes())
        source = (ROOT / "skill/SKILL.md").read_bytes()
        self.assertEqual((ROOT / "plugins/bautraegervertragspruefer" / PLUGIN_REFERENCE).read_bytes(), source)
        with ZipFile(ROOT / "docs/downloads/bautraegervertragspruefer-plugin.zip") as archive:
            self.assertEqual(archive.read("bautraegervertragspruefer/" + PLUGIN_REFERENCE), source)


class LimitationFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((FIXTURES / "erwartungen.json").read_text(encoding="utf-8"))

    def test_fixture_coverage_and_evaluation_separation(self):
        self.assertTrue(self.config["evaluation_only"])
        cases = self.config["cases"]
        self.assertEqual([case["id"] for case in cases], [f"V{i:02}" for i in range(1, 8)])
        self.assertEqual({case["category"] for case in cases}, {
            "short_building_period", "component_and_four_year_periods", "early_start",
            "hidden_notice_cutoff", "valid_building_control", "non_building_control",
            "genuine_negotiation_control",
        })
        expected_paths = {ROOT / case["input"] for case in cases}
        self.assertEqual(expected_paths, set((FIXTURES / "inputs").glob("*.md")))
        for case in cases:
            with self.subTest(case=case["id"]):
                path = (ROOT / case["input"]).resolve()
                self.assertEqual(path.parent, (FIXTURES / "inputs").resolve())
                self.assertRegex(path.name, r"^v\d{2}\.md$")
                self.assertTrue(case["required"])
                self.assertTrue(case["forbidden"])
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("erwartungen.json", text)
                self.assertNotIn("REQUIRED_CONTROLS", text)

    def test_fixture_source_anchors(self):
        for case in self.config["cases"]:
            with self.subTest(case=case["id"]):
                text = (ROOT / case["input"]).read_text(encoding="utf-8")
                for anchor in case["anchors"]:
                    self.assertIn(anchor, text)

    def test_draft_fixture_status_and_blank_deed_number(self):
        for number in range(1, 6):
            with self.subTest(case=f"V{number:02}"):
                text = (FIXTURES / "inputs" / f"v{number:02}.md").read_text(encoding="utf-8")
                self.assertIn("ENTWURF — UR-Nr. __________", text)
                self.assertNotRegex(text, r"UR-Nr\.\s*\d")
                self.assertNotRegex(text, r"(?i)KI[ -]generiert|AI[ -]generated")


if __name__ == "__main__":
    print("Static prompt/fixture regression only; no model execution or legal certification.", flush=True)
    unittest.main(verbosity=2)
