#!/usr/bin/env python3
"""Unit tests for lossless Markdown layout and record parsing; no DOCX or LLM run."""

from contextlib import redirect_stderr
import hashlib
import io
import json
from pathlib import Path
import re
import unittest

import check_legal_anchors as anchors
import export_prompt_docx as exporter


ROOT = Path(__file__).resolve().parents[1]
HEADERS = ("Thema", "Harte Fundstelle", "Kernaussage für Verbraucher", "Einsatz im Vertrag")
SAMPLE_RECORDS = [
    [
        "Ausführlicher synthetischer Prüfdatensatz",
        "Fundstelle: https://example.invalid/urteil.pdf?__blob=publicationFile&v=1",
        ("Einordnung mit **Hervorhebung**, § 634a und klarer Einschränkung. " * 9).strip(),
        "Konkreten Vertragswortlaut abgleichen; keinen abstrakten Leitsatz als Einzelfallentscheidung ausgeben.",
    ],
    [
        "Zweiter synthetischer Prüfdatensatz",
        "Fundstelle: https://example.invalid/zweite-entscheidung?detail=1&format=pdf",
        "Auch kurze Datensätze in derselben Tabelle müssen vollständig erhalten bleiben.",
        "Alle vier Spalten in derselben Reihenfolge übernehmen; Verknüpfungen und Sonderzeichen erhalten.",
    ],
]


def legacy_table(records):
    lines = ["| " + " | ".join(HEADERS) + " |", "| --- | --- | --- | --- |"]
    lines.extend("| " + " | ".join(record) + " |" for record in records)
    return "\n".join(lines) + "\n"


def record_values(text):
    return [columns for _, columns in anchors.extract_case_records(text)]


class FrontmatterTests(unittest.TestCase):
    def test_only_leading_metadata_is_removed(self):
        body = "# Prüfprompt\n\nAbschnitt eins.\n\n---\n\nAbschnitt zwei.\n"
        source = '---\nname: probe\nmetadata:\n  version: "1.0"\n---\n\n' + body
        self.assertEqual(exporter.frontmatter_body(source), body)

    def test_prompt_without_frontmatter_is_unchanged(self):
        source = "# Prüfprompt\n\n---\n\nEin Trenner im Inhalt.\n"
        self.assertEqual(exporter.frontmatter_body(source), source)

    def test_unterminated_metadata_is_not_silently_discarded(self):
        source = "---\nname: probe\n# Noch kein schließender Trenner\n"
        self.assertEqual(exporter.frontmatter_body(source), source)

    def test_repeated_application_keeps_the_body(self):
        source = "---\nname: probe\n---\n\n# Prüfprompt\n\nText.\n"
        body = exporter.frontmatter_body(source)
        self.assertEqual(exporter.frontmatter_body(body), body)


class NarrativeTableTests(unittest.TestCase):
    def test_all_fields_and_urls_survive_conversion(self):
        table = legacy_table(SAMPLE_RECORDS)
        converted = exporter.narrative_tables(table)
        self.assertEqual(record_values(converted), SAMPLE_RECORDS)
        self.assertEqual(anchors.extract_urls(converted), anchors.extract_urls(table))
        for record in SAMPLE_RECORDS:
            for value in record:
                self.assertIn(value, converted)
        self.assertNotIn("| --- |", converted)

    def test_conversion_is_idempotent_and_keeps_surrounding_text(self):
        source = "## Einleitung\n\nVorbemerkung.\n\n" + legacy_table(SAMPLE_RECORDS) + "\n## Danach\n\nSchluss.\n"
        once = exporter.narrative_tables(source)
        self.assertEqual(exporter.narrative_tables(once), once)
        self.assertTrue(once.startswith("## Einleitung\n\nVorbemerkung.\n"))
        self.assertTrue(once.endswith("\n## Danach\n\nSchluss.\n"))

    def test_small_numeric_table_is_retained(self):
        table = "| Baustein | Anteil R | Anteil G |\n| --- | ---: | ---: |\n| Rohbau | 40 % | 28 % |\n"
        self.assertEqual(exporter.narrative_tables(table), table)

    def test_two_column_table_is_retained_even_with_long_text(self):
        table = "| Norm | Erläuterung |\n| --- | --- |\n| § 634a | " + "Inhalt " * 80 + "|\n"
        self.assertEqual(exporter.narrative_tables(table), table)

    def test_malformed_table_is_not_partially_rewritten(self):
        table = legacy_table(SAMPLE_RECORDS) + "| Nur | zwei Zellen |\n"
        self.assertEqual(exporter.narrative_tables(table), table)

    def test_escaped_pipe_in_a_cell_survives_conversion(self):
        records = [list(row) for row in SAMPLE_RECORDS]
        records[0][3] += r" Wortlaut A\|B bleibt zusammen."
        converted = exporter.narrative_tables(legacy_table(records))
        self.assertEqual(record_values(converted), records)

    def test_backtick_and_tilde_fences_are_literal(self):
        for marker in ("`", "~"):
            with self.subTest(marker=marker):
                source = marker * 3 + "markdown\n" + legacy_table(SAMPLE_RECORDS) + marker * 3 + "\n"
                self.assertEqual(exporter.narrative_tables(source), source)

    def test_closing_fence_needs_same_marker_and_sufficient_length(self):
        table = legacy_table(SAMPLE_RECORDS)
        for marker, other in (("`", "~"), ("~", "`")):
            with self.subTest(marker=marker):
                fenced = ("  " + marker * 4 + "markdown\n"
                          + marker * 3 + "\n"             # too short
                          + other * 5 + "\n"              # wrong type
                          + marker * 4 + "suffix\n"      # trailing text
                          + "    " + marker * 4 + "\n"   # too far indented
                          + table
                          + "   " + marker * 5 + " \t\n")
                source = fenced + "\n" + table
                converted = exporter.narrative_tables(source)
                self.assertTrue(converted.startswith(fenced))
                remainder = converted[len(fenced):]
                self.assertEqual(record_values(remainder), SAMPLE_RECORDS)
                self.assertNotIn("| --- |", remainder)

    def test_unclosed_fence_keeps_the_rest_literal(self):
        source = "```markdown\n" + legacy_table(SAMPLE_RECORDS)
        self.assertEqual(exporter.narrative_tables(source), source)


class CaseRecordTests(unittest.TestCase):
    def test_legacy_and_full_width_records_have_identical_fields(self):
        legacy = legacy_table(SAMPLE_RECORDS)
        full_width = exporter.narrative_tables(legacy)
        self.assertEqual(record_values(legacy), SAMPLE_RECORDS)
        self.assertEqual(record_values(full_width), record_values(legacy))

    def test_current_catalog_roundtrips_without_git_or_network(self):
        source = (ROOT / "skill/SKILL.md").read_text(encoding="utf-8")
        current = record_values(anchors.extract_section(source))
        self.assertGreaterEqual(len(current), 49)
        table = legacy_table(current)
        converted = exporter.narrative_tables(table)
        self.assertEqual(record_values(table), current)
        self.assertEqual(record_values(converted), current)
        self.assertEqual(exporter.narrative_tables(converted), converted)
        self.assertEqual(anchors.extract_urls(converted), anchors.extract_urls(table))

    def assert_invalid_records(self, source, diagnostic):
        error = io.StringIO()
        with redirect_stderr(error), self.assertRaises(SystemExit) as result:
            anchors.extract_case_records(source)
        self.assertEqual(result.exception.code, 1)
        self.assertIn(diagnostic, error.getvalue())

    def test_missing_required_label_fails(self):
        source = exporter.narrative_tables(legacy_table(SAMPLE_RECORDS))
        source = source.replace("**Einsatz im Vertrag:**", "**Anderes Feld:**", 1)
        self.assert_invalid_records(source, "needs exactly one Einsatz im Vertrag")

    def test_duplicate_required_label_fails(self):
        source = exporter.narrative_tables(legacy_table(SAMPLE_RECORDS))
        source += "\n**Harte Fundstelle:** Eine zweite Fundstelle im selben Datensatz.\n"
        self.assert_invalid_records(source, "needs exactly one Harte Fundstelle")

    def test_mixed_formats_fail_instead_of_ignoring_legacy_records(self):
        legacy = legacy_table(SAMPLE_RECORDS)
        full_width = exporter.narrative_tables(legacy)
        for source in (legacy + full_width, full_width + legacy):
            with self.subTest(legacy_first=source.startswith("|")):
                self.assert_invalid_records(source, "mixed case-law records and legacy table rows")

    def test_malformed_legacy_row_fails(self):
        self.assert_invalid_records("| Ein Thema | nur zwei Zellen |\n", "2 columns instead of 4")

    def test_record_line_numbers_point_to_actual_heading_or_row(self):
        for source in (legacy_table(SAMPLE_RECORDS), exporter.narrative_tables(legacy_table(SAMPLE_RECORDS))):
            for number, columns in anchors.extract_case_records(source):
                self.assertIn(columns[0], source.splitlines()[number - 1])


class PublishedPromptDocxTests(unittest.TestCase):
    def test_reviewed_exports_match_current_sources_and_page_budget(self):
        """Bind recorded manual review to exact bytes; this does not re-render Word."""
        full = (ROOT / "skill/SKILL.md").read_text(encoding="utf-8")
        version = re.search(r'^  version: "([^"]+)"$', full, re.MULTILINE)[1]
        report = json.loads((ROOT / f"tests/prompt-layout-{version}.json").read_text(encoding="utf-8"))
        self.assertEqual({item["source"] for item in report["artifacts"]},
                         {"skill/SKILL.md", "skill/MINI_SKILL.md"})
        self.assertEqual(len(report["artifacts"]), 2)
        for item in report["artifacts"]:
            with self.subTest(artifact=item["output"]):
                self.assertGreater(item["pages"], 0)
                self.assertEqual(item["max_pages"], 100)
                self.assertLessEqual(item["pages"], item["max_pages"])
                self.assertEqual(item["visual_qa"]["status"], "passed")
                self.assertEqual(item["visual_qa"]["pages_checked"], list(range(1, item["pages"] + 1)))
                for field, digest in (("source", "source_sha256"), ("output", "docx_sha256")):
                    path = (ROOT / item[field]).resolve()
                    self.assertTrue(path.is_relative_to(ROOT))
                    self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item[digest],
                                     "Prompt or DOCX changed after the recorded page review; re-export and review")


if __name__ == "__main__":
    print("Markdown/record unit tests only; no Word rendering, legal judgment or model execution.", flush=True)
    unittest.main(verbosity=2)
