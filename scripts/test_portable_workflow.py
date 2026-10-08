#!/usr/bin/env python3
"""Instruction/fixture regression tests, not an LLM or a Word integration test."""

import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/workflow/word-selection"


class PortableWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full = (ROOT / "skill/SKILL.md").read_text()
        cls.mini = (ROOT / "skill/MINI_SKILL.md").read_text()
        cls.evaluation = json.loads((FIXTURE / "evaluation.json").read_text())

    def test_fixture_is_evaluator_only(self):
        self.assertIs(self.evaluation["evaluation_only"], True)
        self.assertIs(self.evaluation["not_model_input"], True)
        self.assertIs(self.evaluation["future_turns_visible"], False)

    def test_turns_are_separate_files(self):
        self.assertEqual(self.evaluation["inputs"], ["inputs/ws01-01.md", "inputs/ws01-02.md"])
        self.assertEqual({p.name for p in (FIXTURE / "inputs").iterdir()}, {"ws01-01.md", "ws01-02.md"})
        for relative in self.evaluation["inputs"]:
            text = (FIXTURE / relative).read_text()
            self.assertNotIn("evaluation.json", text)
            self.assertNotIn("required", text)

    def test_second_turn_not_leaked_into_first(self):
        first = (FIXTURE / self.evaluation["inputs"][0]).read_text()
        self.assertNotIn("zwei Monate", first)
        self.assertNotIn("fünf Jahre", first)

    def test_no_fake_word_integration_claim(self):
        self.assertIn("kein Test einer echten Word", self.evaluation["scope"])

    def test_full_separates_environment_capabilities(self):
        section = self.full.split("### 1.4 ", 1)[1].split("### 1.5", 1)[0]
        for term in ("Webchat", "Plugin", "Word", "Auswahl", "Export"):
            self.assertIn(term, section)

    def test_independent_questions_not_just_numbered_groups(self):
        for text in (self.full, self.mini):
            self.assertRegex(text, r"(?:selbständige|unabhängige)\s+(?:Fragen|Rückfragen)")

    def test_both_prompts_require_explicit_limitation_prohibition(self):
        for text in (self.full, self.mini):
            normalized = re.sub(r"\s+", " ", text)
            self.assertRegex(normalized, r"(?:ausdrücklich.{0,100}§ 309|§ 309.{0,150}ausdrücklich)")

    def test_full_updates_positive_and_negative_branches(self):
        section = self.full.split("### 1.5 ", 1)[1].split("## 2", 1)[0]
        for term in ("entfällt dieser Einwand", "unverändert", "positiv ausfallen"):
            self.assertIn(term, section)


if __name__ == "__main__":
    unittest.main(verbosity=2)
