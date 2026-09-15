#!/usr/bin/env python3
"""Check dialogue fixtures/instructions, not model behaviour or legal correctness."""

from copy import deepcopy
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "tests/workflow"
ENTRYPOINTS = (
    "bautraegervertrag-pruefen",
    "bautraeger-zahlungsrate-pruefen",
    "bautraeger-word-entwurf-pruefen",
)
PROMPTS = (ROOT / "skill/SKILL.md", ROOT / "skill/MINI_SKILL.md")
SKILLS = tuple(ROOT / "plugins/bautraegervertragspruefer/skills" / name / "SKILL.md"
               for name in ENTRYPOINTS)


def normalize(text):
    return re.sub(r"\s+", " ", text.replace("**", "")).strip()


def old_analysis_only_rule(text):
    """Detect the three former stopping instructions, not any mention of analysis."""
    patterns = (
        r"Vollständige\s+Prüfung\s*=\s*Analyse",
        r"Alles\s+vollständig\s+prüfen[\"“]?\s+verlangt\s+eine\s+vollständige\s+Analyse",
        r"Bei\s+[\"„]?vollständig\s+prüfen[\"“]?\s+liefere\s+die\s+vollständige\s+Analyse",
    )
    return any(re.search(pattern, normalize(text), re.I) for pattern in patterns)


# Explicit instruction-presence checks only. These patterns neither count the
# number of headings nor evaluate an answer; prohibitions may name old jargon.
COMMON_INSTRUCTIONS = {
    "bounded_questions": r"(?:höchstens|maximal)\s+(?:drei|3)\s+(?:konkrete(?:n)?|konkret\s+bezeichnete)\s+(?:Rückfragen|Fragen|Informationen|Belege)",
    "perform_commissioned_work": r"(?:fertige|fertigen|erstelle|ausarbeiten).{0,160}(?:an|Schreiben|Entwurf|Ergebnis)",
    "process_reply": r"(?:nach|bei).{0,60}(?:Antwort|Rückmeldung|neuen?\s+Unterlagen|weiterer\s+Angaben|neuen?\s+Fassung)",
    "resume_existing_work": r"weiter.{0,90}(?:offenen|gewählten|Arbeitsschritt|setzt\s+dort)",
    "completion_condition": r"(?:abschlie|schließe|Abschluss|Auftrag\s+endet).{0,180}(?:beauftragt|Ergebnis|Information|Mitwirkung)",
}
STANDALONE_INSTRUCTIONS = {
    "plain_legal_language": r"(?:verständlichem\s+juristischem\s+Deutsch|vollständigen.{0,30}verständlichen\s+Sätzen)",
    "stop": r"stop.{0,65}(?:beende|beendet)",
    "without_questions": r"ohne\s+Rückfragen.{0,180}(?:Grenzen|Annahmen|bedingt)",
    "bounded_scope": r"(?:ausdrücklich\s+begrenzter?|begrenzte\s+Frage).{0,140}(?:enden|endet|Zusatz|künstlich)",
}


def missing_instructions(text, requirements):
    normalized = normalize(text)
    return [label for label, pattern in requirements.items()
            if not re.search(pattern, normalized, re.I)]


def validate_dialogues(config, expectations):
    errors = []
    if config.get("schema_version") != 1 or expectations.get("schema_version") != 1:
        errors.append("unsupported schema")
    if config.get("delivery") != "one_user_turn_after_previous_response":
        errors.append("delivery must wait for the preceding actual response")
    if config.get("fresh_conversation_per_case") is not True:
        errors.append("cases require fresh conversations")
    if config.get("future_turns_visible") is not False:
        errors.append("future turns must be hidden")
    if config.get("contract_format") != "markdown":
        errors.append("these dialogue fixtures are text tests, not Word tests")
    if expectations.get("evaluation_only") is not True or expectations.get("not_model_input") is not True:
        errors.append("expectations must remain evaluator-only")

    cases = config.get("cases", [])
    if [case.get("id") for case in cases] != [f"W{i:02}" for i in range(1, 6)]:
        errors.append("expected five uniquely ordered dialogue cases")
    expected_cases = expectations.get("cases", [])
    if [case.get("id") for case in expected_cases] != [case.get("id") for case in cases]:
        errors.append("expectation cases differ from input cases")
    by_id = {case.get("id"): case for case in expected_cases}
    for case in cases:
        case_id = case.get("id")
        if case.get("plugin_entrypoint") not in ENTRYPOINTS:
            errors.append(f"{case_id}: unknown plugin entrypoint")
        turns = case.get("turns", [])
        if [turn.get("turn") for turn in turns] != [1, 2, 3]:
            errors.append(f"{case_id}: expected three ordered user turns")
        evaluations = by_id.get(case_id, {}).get("turns", [])
        if [turn.get("turn") for turn in evaluations] != [1, 2, 3]:
            errors.append(f"{case_id}: every turn needs separate expectations")
        for turn in turns:
            number = turn.get("turn")
            expected_previous = None if number == 1 else number - 1
            if turn.get("after_response_to") != expected_previous:
                errors.append(f"{case_id}/{number}: incorrect conversational ordering")
            inputs = turn.get("inputs", [])
            if not inputs or len(inputs) != len(set(inputs)):
                errors.append(f"{case_id}/{number}: missing or duplicate inputs")
            for relative in inputs:
                path = (ROOT / relative).resolve()
                if not path.is_relative_to(ROOT) or not path.is_file():
                    errors.append(f"{case_id}/{number}: invalid input path {relative}")
                    continue
                if path.suffix != ".md" or path.name.lower() == "readme.md" or "runs" in path.parts:
                    errors.append(f"{case_id}/{number}: evaluator/non-text input {relative}")
                text = path.read_text(encoding="utf-8")
                if any(marker in text for marker in ("erwartungen.json", "REQUIRED_CONTROLS", "evaluation_only")):
                    errors.append(f"{case_id}/{number}: expectation leakage in {relative}")
        for evaluation in evaluations:
            for kind in ("required", "forbidden", "critical"):
                values = evaluation.get(kind)
                if not isinstance(values, list) or not values or any(not isinstance(value, str) or not value.strip() for value in values):
                    errors.append(f"{case_id}/{evaluation.get('turn')}: missing {kind} outcomes")
    return errors


class DialogueFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dialogues = json.loads((WORKFLOW / "dialoge.json").read_text(encoding="utf-8"))
        cls.expectations = json.loads((WORKFLOW / "erwartungen.json").read_text(encoding="utf-8"))

    def test_schema_paths_order_and_evaluator_separation(self):
        self.assertEqual(validate_dialogues(self.dialogues, self.expectations), [])

    def test_future_turns_cannot_be_exposed(self):
        mutated = deepcopy(self.dialogues)
        mutated["future_turns_visible"] = True
        self.assertIn("future turns must be hidden", validate_dialogues(mutated, self.expectations))

    def test_turn_cannot_skip_previous_response(self):
        mutated = deepcopy(self.dialogues)
        mutated["cases"][0]["turns"][2]["after_response_to"] = 1
        self.assertIn("W01/3: incorrect conversational ordering", validate_dialogues(mutated, self.expectations))

    def test_evaluator_files_cannot_be_model_inputs(self):
        mutated = deepcopy(self.dialogues)
        mutated["cases"][0]["turns"][0]["inputs"].append("tests/workflow/erwartungen.json")
        self.assertTrue(any("evaluator/non-text input" in error for error in validate_dialogues(mutated, self.expectations)))

    def test_every_new_input_is_referenced(self):
        paths = {ROOT / item for case in self.dialogues["cases"] for turn in case["turns"] for item in turn["inputs"]}
        self.assertEqual(set((WORKFLOW / "inputs").glob("*.md")), {path for path in paths if path.parent == WORKFLOW / "inputs"})

    def test_payment_supplements_arrive_only_in_second_turn(self):
        by_id = {case["id"]: case for case in self.dialogues["cases"]}
        for case_id, supplement in (("W03", "tests/inputs/m-zahlung-ergänzt.md"),
                                    ("W04", "tests/inputs/l-gegenfeststellung.md")):
            with self.subTest(case=case_id):
                turns = by_id[case_id]["turns"]
                self.assertNotIn(supplement, turns[0]["inputs"])
                self.assertEqual(turns[1]["inputs"], [supplement])
                self.assertNotIn(supplement, turns[2]["inputs"])

    def test_revision_input_replaces_old_clauses(self):
        text = (WORKFLOW / "inputs/w01-03.md").read_text(encoding="utf-8")
        for anchor in ("ersetzt deren bisherigen Wortlaut", "fünf Jahren", "Ansprüche wegen dieser Mängel ausgeschlossen", "ENTWURF — UR-Nr. __________"):
            self.assertIn(anchor, text)
        self.assertNotRegex(text, r"UR-Nr\.\s*\d")

    def test_stop_and_limited_resume_are_distinct_user_turns(self):
        first = (WORKFLOW / "inputs/w05-01.md").read_text(encoding="utf-8")
        second = (WORKFLOW / "inputs/w05-02.md").read_text(encoding="utf-8")
        third = (WORKFLOW / "inputs/w05-03.md").read_text(encoding="utf-8")
        self.assertIn("ohne Rückfragen", first)
        self.assertTrue(second.startswith("Stop."))
        self.assertTrue(third.startswith("Weiter,"))
        self.assertIn("nur mit einem knappen Satz", third)

    def test_metadata_template_does_not_claim_execution(self):
        template = json.loads((WORKFLOW / "laufvorlage.json").read_text(encoding="utf-8"))
        self.assertTrue(template["template_only"])
        self.assertEqual(template["status"], "not_run")
        self.assertIsNone(template["model_id"])
        self.assertIsNone(template["fresh_conversation"])
        self.assertIsNone(template["turns_delivered_sequentially"])
        self.assertEqual(template["evaluation"]["turn_results"], [])
        self.assertEqual(self.expectations["actual_runs"], [])
        self.assertEqual([turn["turn"] for turn in template["turns"]], [1, 2, 3])
        for turn in template["turns"]:
            self.assertEqual(turn["input_sha256"], {})
            self.assertIsNone(turn["raw_response_file"])


class WorkflowInstructionTests(unittest.TestCase):
    def test_old_analysis_only_defaults_are_removed(self):
        for path in PROMPTS + SKILLS:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertFalse(old_analysis_only_rule(path.read_text(encoding="utf-8")))

    def test_regression_guard_detects_old_stopping_rules(self):
        for old_rule in (
            "Vollständige Prüfung = Analyse; ausdrückliches Vollpaket = Schreiben.",
            "„Alles vollständig prüfen“ verlangt eine vollständige Analyse.",
            "Bei „vollständig prüfen“ liefere die vollständige Analyse.",
        ):
            with self.subTest(rule=old_rule):
                self.assertTrue(old_analysis_only_rule(old_rule))
        self.assertFalse(old_analysis_only_rule("Die Analyse ist die Grundlage der beauftragten Änderungen."))

    def test_standalone_prompts_keep_dialogue_scope_and_language_rules(self):
        for path in PROMPTS:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                self.assertEqual(missing_instructions(text, COMMON_INSTRUCTIONS | STANDALONE_INSTRUCTIONS), [])

    def test_each_plugin_entrypoint_has_its_own_follow_through(self):
        # Inspect entrypoints themselves, not their large reference: a tool-only
        # endpoint must also ask, resume and produce its commissioned result.
        for path in SKILLS:
            with self.subTest(skill=path.parent.name):
                self.assertEqual(missing_instructions(path.read_text(encoding="utf-8"), COMMON_INSTRUCTIONS), [])

    def test_generic_workflow_slogan_is_insufficient(self):
        text = "Prüfe den Vertrag. Nutze einen Workflow. Gib eine Analyse aus."
        self.assertEqual(set(missing_instructions(text, COMMON_INSTRUCTIONS)), set(COMMON_INSTRUCTIONS))


if __name__ == "__main__":
    print("Static dialogue fixture/instruction checks only; no model run or legal certification.", flush=True)
    unittest.main(verbosity=2)
