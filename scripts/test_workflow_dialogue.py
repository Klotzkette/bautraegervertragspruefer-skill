#!/usr/bin/env python3
"""Check dialogue fixtures/instructions, not model behaviour or legal correctness."""

from copy import deepcopy
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "tests/workflow"
DEFAULT_PACKAGE = WORKFLOW / "default-package"
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


def extra_commission_rule(text):
    """Catch known default-package regressions, while allowing explicit limits.

    This deliberately checks instruction text, not purported model behaviour.
    A scoped exception must be stated in the same sentence as the restriction;
    an unrelated nearby exception must not hide a contradictory blanket rule.
    """
    scoped_exception = re.compile(
        r"^(?:Bei|Für|Wenn|Ein|Eine|Nach).{0,100}(?:ausdrücklich\s+begrenz|"
        r"nur\s+(?:diese\s+Klausel|Analyse|technische[rn]?\s+Prüfung|das\s+Antwortschreiben))", re.I)
    regressions = (
        r"keine?\s+ungefragt.{0,50}(?:drei\s+(?:Schreiben|Dokumente)|(?:Standard|Voll)paket)",
        r"(?:vollständig\s+prüfen|(?:normale|vollständige)\s+(?:Vertrags)?prüfung|Gesamtprüfung)"
        r".{0,180}nicht\s+automatisch.{0,60}(?:drei|Schreiben|Dokumente|Paket)",
        r"(?:Standardpaket|Vollpaket|drei\s+(?:Schreiben|Dokumente)|Gutachten|Mandantenschreiben)"
        r".{0,60}(?:nur|erst|braucht|benötigt|setzt).{0,60}\b"
        r"(?:einen|(?:ausdrücklich|gesondert|zusätzlich|separat)e[nrm])\s+(?:Auftrag|Wunsch|Beauftragung)",
    )
    for sentence in re.split(r"(?<=[.!?])\s+", normalize(text)):
        if not scoped_exception.search(sentence):
            if any(re.search(pattern, sentence, re.I) for pattern in regressions):
                return True
    return False


# Explicit instruction-presence checks only. These patterns neither count the
# number of headings nor evaluate an answer; prohibitions may name old jargon.
COMMON_INSTRUCTIONS = {
    "bounded_questions": r"(?:höchstens|maximal)\s+(?:drei|3)\s+(?:konkrete(?:n)?|konkret\s+bezeichnete)\s+(?:Rückfragen|Fragen|Informationen|Belege)",
    "perform_commissioned_work": r"(?:fertige|fertigen|erstelle|ausarbeiten).{0,160}(?:an|Schreiben|Entwurf|Ergebnis)",
    "process_reply": r"(?:nach|bei).{0,60}(?:Antwort|Rückmeldung|neuen?\s+Unterlagen|weiterer\s+Angaben|neuen?\s+Fassung)",
    "resume_existing_work": r"weiter.{0,90}(?:offenen|gewählten|Arbeitsschritt|setzt\s+dort)",
    "completion_condition": r"(?:abschlie|schließe|Abschluss|Auftrag\s+endet).{0,180}(?:beauftragt|Ergebnis|Information|Mitwirkung|drei\s+Dokumente)",
}
STANDALONE_INSTRUCTIONS = {
    "plain_legal_language": r"(?:verständlichem\s+juristischem\s+Deutsch|vollständigen.{0,30}verständlichen\s+Sätzen)",
    "stop": r"stop.{0,65}(?:beende|beendet)",
    "without_questions": r"ohne\s+Rückfragen.{0,180}(?:Grenzen|Annahmen|bedingt)",
    "bounded_scope": r"(?:ausdrücklich\s+begrenzter?|begrenzte\s+Frage).{0,140}(?:enden|endet|Zusatz|künstlich)",
}
# A small set of semantic anchors, not a heading count or answer scorer. The
# separate blind dialogue below is needed to evaluate actual output quality.
ACQUISITION_WORKFLOW = {
    "fixed_acquisition_side": r"(?:immer|stets|ausschließlich).{0,65}(?:Erwerberin|Erwerberinnen)|rechtliche\s+Vertragsprüfung\s+aus\s+Sicht\s+der\s+Erwerberin",
    "carry_findings_into_outputs": r"\b(?:jede[rns]?|alle[nrs]?|sämtliche[nr]?)\b.{0,100}(?:Korrektur|Änderung|Befund|Punkt|Feststellung|Einwände).{0,260}(?:übernommen|übernehmen|übertrage|Schreiben)",
    "explain_omissions": r"(?:Weglassen|Nichtaufnahme|nicht\s+aufgenommen|nicht\s+übernommen|nicht\s+übernimmst).{0,100}(?:begründe|Grund|erklär)|(?:sachliche[rmn]?\s+Grund).{0,140}(?:erklär|nicht\s+aufgenommen)|begründe.{0,50}(?:Auslassung|Weglassen|Nichtaufnahme)",
    "revision_continuity": r"(?:neue[rn]?\s+(?:Vertragsfassung|Fassung)|Antworten|Rückmeldung|weiterer\s+Angaben).{0,260}(?:aktualisiere|überarbeite|erledigt|fortgelt|offen)",
}
PACKAGE_INSTRUCTIONS = {
    "ordinary_review_commissions_package": r"(?:normale[rn]?\s+(?:Prüfauftrag|Vertragsprüfung)|Gesamtprüfung).{0,420}(?:Gutachten|Mandantenschreiben)",
    "three_products": r"(?:drei\s+(?:ausgearbeitete\s+)?Dokumente|Gutachten.{0,180}Mandantenschreiben.{0,180}Schreiben\s+an\s+(?:den\s+)?Bauträger)",
    "no_second_commission": r"(?:ohne\s+(?:zweiten|gesonderten|zusätzlichen)\s+Auftrag|(?:weder|kein).{0,120}zweiter\s+Auftrag)",
    "explicit_scope_exception": r"ausdrücklich\s+begrenz.{0,240}(?:nur\s+(?:diese\s+Klausel|Analyse)|keine\s+Schreiben)",
    "missing_documents_allow_drafts": r"(?:fehlende[nr]?\s+(?:Unterlagen|Anlagen|Teilungserklärung)|fehlt\s+(?:nur\s+)?eine\s+Anlage).{0,340}(?:bedingte[nr]?\s+(?:Entwürfe|Schreiben)|fertige.{0,100}Schreiben|darauf\s+gestützten\s+Schreiben)",
}


def missing_instructions(text, requirements):
    normalized = normalize(text)
    return [label for label, pattern in requirements.items()
            if not re.search(pattern, normalized, re.I)]


def validate_dialogues(config, expectations, case_ids=None, turn_numbers=(1, 2, 3)):
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
    if case_ids is None:
        case_ids = [f"W{i:02}" for i in range(1, 6)]
    if [case.get("id") for case in cases] != list(case_ids):
        errors.append("expected uniquely ordered dialogue cases")
    expected_cases = expectations.get("cases", [])
    if [case.get("id") for case in expected_cases] != [case.get("id") for case in cases]:
        errors.append("expectation cases differ from input cases")
    by_id = {case.get("id"): case for case in expected_cases}
    for case in cases:
        case_id = case.get("id")
        if case.get("plugin_entrypoint") not in ENTRYPOINTS:
            errors.append(f"{case_id}: unknown plugin entrypoint")
        turns = case.get("turns", [])
        if [turn.get("turn") for turn in turns] != list(turn_numbers):
            errors.append(f"{case_id}: expected ordered user turns")
        evaluations = by_id.get(case_id, {}).get("turns", [])
        if [turn.get("turn") for turn in evaluations] != list(turn_numbers):
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


class DefaultPackageFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dialogues = json.loads((DEFAULT_PACKAGE / "dialoge.json").read_text(encoding="utf-8"))
        cls.expectations = json.loads((DEFAULT_PACKAGE / "erwartungen.json").read_text(encoding="utf-8"))

    def test_separate_registry_with_two_sequential_turns(self):
        self.assertEqual(validate_dialogues(self.dialogues, self.expectations,
                                           case_ids=("DP01",), turn_numbers=(1, 2)), [])

    def test_plain_full_review_uses_only_clean_request_and_existing_contract(self):
        first = self.dialogues["cases"][0]["turns"][0]
        self.assertEqual(first["inputs"], [
            "tests/workflow/default-package/inputs/dp01-01.md",
            "vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md",
        ])
        request = (ROOT / first["inputs"][0]).read_text(encoding="utf-8")
        self.assertTrue(request.startswith("Bitte prüfe den beigefügten Bauträgervertrag vollständig."))
        # The task must not tip off the model about output products or findings.
        self.assertNotRegex(request, r"(?i)Vollpaket|Gutachten|Mandantenschreiben|drei\s+(?:Schreiben|Dokumente)|§\s*6\.2|Ausschlussfrist|DP-F\d")

    def test_revision_introduces_replacement_without_supplying_assessment(self):
        turns = self.dialogues["cases"][0]["turns"]
        self.assertEqual(turns[1]["inputs"], ["tests/workflow/default-package/inputs/dp01-02.md"])
        text = (ROOT / turns[1]["inputs"][0]).read_text(encoding="utf-8")
        for anchor in ("§ 6.2 wird vollständig", "§ 9.3 wird vollständig", "mindestens eines Mangels",
                       "binnen 14 Tagen", "sämtliche Ansprüche", "übrigen Regelungen", "Weitere Unterlagen habe ich nicht erhalten"):
            self.assertIn(anchor, text)
        self.assertNotRegex(text, r"(?i)unwirksam|§\s*309|Pflichtbefund|DP-F\d|Vollpaket")

    def test_future_turn_and_evaluator_leak_mutations_are_rejected(self):
        mutated = deepcopy(self.dialogues)
        mutated["future_turns_visible"] = True
        mutated["cases"][0]["turns"][0]["inputs"].append("tests/workflow/default-package/erwartungen.json")
        errors = validate_dialogues(mutated, self.expectations, case_ids=("DP01",), turn_numbers=(1, 2))
        self.assertIn("future turns must be hidden", errors)
        self.assertTrue(any("evaluator/non-text input" in error for error in errors))

    def test_acceptance_requires_products_priorities_and_finding_continuity(self):
        acceptance = self.expectations["acceptance"]
        self.assertEqual(acceptance["products"], ["gutachten", "mandantenschreiben", "externes_schreiben"])
        for field in ("finding_coverage", "revision_coverage", "priority_separation", "passing_rule"):
            self.assertTrue(acceptance[field].strip(), field)
        findings = self.expectations["mandatory_findings"]
        self.assertEqual([item["id"] for item in findings], [f"DP-F{i:02}" for i in range(1, 9)])
        for item in findings:
            for field in ("source", "outcome", "second_turn"):
                self.assertTrue(item[field].strip(), (item["id"], field))
        self.assertEqual([item["id"] for item in findings if item.get("introduced_in_turn") == 2], ["DP-F08"])
        self.assertEqual(self.expectations["actual_runs"], [])

    def test_every_new_input_is_referenced(self):
        paths = {ROOT / item for case in self.dialogues["cases"] for turn in case["turns"] for item in turn["inputs"]}
        self.assertEqual(set((DEFAULT_PACKAGE / "inputs").glob("*.md")),
                         {path for path in paths if path.parent == DEFAULT_PACKAGE / "inputs"})


class WorkflowInstructionTests(unittest.TestCase):
    def test_finding_continuity_has_an_actual_shared_deliverable(self):
        for relative in ("skill/SKILL.md", "skill/MINI_SKILL.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            for anchor in ("Änderungen und benötigte Unterlagen", "Beide Briefe", "vollständig aktualisiert"):
                self.assertIn(anchor, text)
            self.assertRegex(text, r"(?i)vertraulichen internen Erwägungen")

    def test_technical_reference_rule_is_concrete_in_both_prompts(self):
        for path in PROMPTS:
            with self.subTest(path=path.relative_to(ROOT)):
                paragraphs = path.read_text(encoding="utf-8").split("\n\n")
                rule = next((p for p in paragraphs if "DIN 18015-2" in p), "")
                for anchor in ("RAL-RG 678", "Ausgabe", "raumweise", "Normvolltext", "Tür"):
                    self.assertIn(anchor, rule)
                self.assertRegex(rule, r"Mindestausstattung")

    def test_technical_probe_keeps_expectations_separate(self):
        probe = ROOT / "tests" / "technical-references"
        request = (probe / "input.md").read_text(encoding="utf-8")
        expected = json.loads((probe / "erwartungen.json").read_text(encoding="utf-8"))
        self.assertTrue(expected["evaluation_only"])
        self.assertTrue(expected["not_model_input"])
        self.assertEqual(len(expected["required"]), 5)
        self.assertNotRegex(request, r"NR0[1-5]|erwartungen\.json|§ 309")
        self.assertIn("Keine Gesamtprüfung", request)
        self.assertIn("24 Monate", request)

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
        for requirements in (COMMON_INSTRUCTIONS, ACQUISITION_WORKFLOW, PACKAGE_INSTRUCTIONS):
            self.assertEqual(set(missing_instructions(text, requirements)), set(requirements))

    def test_acquisition_role_and_continuity_at_every_entrypoint(self):
        for path in PROMPTS + SKILLS:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(missing_instructions(path.read_text(encoding="utf-8"), ACQUISITION_WORKFLOW), [])

    def test_full_review_has_implicit_package_and_scoped_exceptions(self):
        # Payment and purely technical Word work have their own narrower scope.
        for path in PROMPTS + (SKILLS[0],):
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(missing_instructions(path.read_text(encoding="utf-8"), PACKAGE_INSTRUCTIONS), [])

    def test_no_blanket_extra_commission_requirement(self):
        for path in PROMPTS + SKILLS:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertFalse(extra_commission_rule(path.read_text(encoding="utf-8")))

    def test_mutated_defaults_are_rejected_even_next_to_a_scoped_exception(self):
        allowed = "Bei ausdrücklich begrenztem Auftrag werden nur die verlangten Ergebnisse erstellt. "
        for regression in (
            "Keine ungefragt angehängten drei Schreiben.",
            "„Alles vollständig prüfen“ durchläuft den Ablauf, bestellt aber nicht automatisch drei getrennte Dokumente.",
            "Das Standardpaket braucht einen zusätzlichen Auftrag.",
            "Das Vollpaket gibt es nur nach gesondertem Auftrag.",
            "Das Mandantenschreiben entsteht nur auf ausdrücklichen Wunsch.",
            "Ein zusätzliches Gutachten braucht einen Auftrag.",
        ):
            with self.subTest(regression=regression):
                self.assertTrue(extra_commission_rule(allowed + regression))

    def test_explicit_limited_requests_do_not_trigger_default_regression(self):
        for rule in (
            "Bei ausdrücklich begrenztem Auftrag keine ungefragt angehängten drei Schreiben.",
            "Bei nur technischer Prüfung entsteht das Vollpaket erst auf ausdrücklichen Wunsch.",
            "Für nur das Antwortschreiben braucht ein zusätzliches Gutachten einen Auftrag.",
            "Der normale Prüfauftrag umfasst alle drei Dokumente ohne zweiten Auftrag.",
        ):
            with self.subTest(rule=rule):
                self.assertFalse(extra_commission_rule(rule))


if __name__ == "__main__":
    print("Static dialogue fixture/instruction checks only; no model run or legal certification.", flush=True)
    unittest.main(verbosity=2)
