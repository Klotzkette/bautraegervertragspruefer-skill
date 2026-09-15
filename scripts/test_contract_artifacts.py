#!/usr/bin/env python3
"""Mutation regressions for draft-only Word templates and exact translations."""
import contextlib
import io
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from zipfile import ZipFile

import build_bilingual_contracts as bilingual
import check_contract_builds as checks


class DraftArtifactTests(unittest.TestCase):
    def test_bilingual_heading_stays_in_same_row_as_following_text(self):
        with patch.object(bilingual, "markdown_to_html", side_effect=lambda text: text):
            result = bilingual.bilingual_rows(["# Titel", "Absatz"], ["Title", "Paragraph"])
        parsed = checks.EnglishCells()
        parsed.feed(result)
        self.assertEqual(parsed.cells, ["Title\nParagraph"])
        self.assertIn('# Titel\nAbsatz</td>', result)

    def test_separate_ordered_lists_preserve_start_counter(self):
        fragment = '<ol start="3" type="a"><li>Clause</li></ol>'
        with patch.object(bilingual, "markdown_to_html", side_effect=lambda text: text):
            result = bilingual.bilingual_rows([fragment], [fragment])
        self.assertEqual(result.count('counter-reset: list-item 2'), 2)
        self.assertEqual(result.count('start="3"'), 2)

    def test_nested_rate_table_replaces_conflicting_column_widths(self):
        fragment = '<table><colgroup><col style="width:33%"></colgroup><tr><td>1</td><td>Works</td><td>30%</td></tr></table>'
        with patch.object(bilingual, "markdown_to_html", side_effect=lambda text: text):
            result = bilingual.bilingual_rows([fragment], [fragment])
        self.assertNotIn('width:33%', result)
        self.assertEqual(result.count('width:72%'), 2)
        self.assertEqual(result.count('<td>Works</td>'), 2)

    def test_changed_english_memory_rejects_stale_artifacts(self):
        original_loads = json.loads

        def changed_memory(value):
            data = original_loads(value)
            data["# ENTWURF"] = "<h1>CHANGED DRAFT TEXT</h1>"
            return data

        with patch.object(checks.json, "loads", side_effect=changed_memory):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                checks.verify_english_content()

    def test_all_reviewed_source_blocks_have_exact_translation(self):
        for config in bilingual.CONFIGS:
            memory = json.loads((config.src.parent / "build/translations.en.json").read_text())
            blocks = bilingual.inject_language_notice(bilingual.split_blocks(config.src.read_text()), config)
            for block in blocks:
                self.assertTrue(bilingual.reviewed_translation(block, memory))

    def test_changed_paragraph_ending_fails_closed(self):
        config = bilingual.CONFIGS[0]
        memory = json.loads((config.src.parent / "build/translations.en.json").read_text())
        block = next(key for key in memory if key.startswith("Für den Beurkundungstermin ist folgende Erklärung"))
        with self.assertRaisesRegex(RuntimeError, "exact source block"):
            bilingual.reviewed_translation(block + " Zusätzliche abweichende Regelung.", memory)

    def test_prefix_only_cannot_reuse_full_translation(self):
        with self.assertRaises(RuntimeError):
            bilingual.reviewed_translation("Entwurf mit neuem Inhalt", {"Entwurf": "Draft"})

    def test_visible_draft_regressions(self):
        good = "ENTWURF UR-Nr. ____________________ Vorgesehener Beurkundungstermin"
        checks.assert_draft_text(good, "fixture")
        for bad in (good.replace("ENTWURF", "AUSFERTIGUNG"),
                    good.replace("____________________", "117/2026"),
                    good + " Diese Niederschrift wurde vorgelesen und unterschrieben.",
                    good + " KI-generiert", good + " AI generated"):
            with self.subTest(bad=bad), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                checks.assert_draft_text(bad, "fixture")

    def test_hidden_xml_parts_and_split_runs_are_checked(self):
        ns = checks.WORD_NS
        body = f'<w:document xmlns:w="{ns}"><w:body><w:p><w:r><w:t>ENTWURF UR-Nr. ____________________ Vorgesehener Beurkundungstermin</w:t></w:r></w:p></w:body></w:document>'
        for part in ("word/header1.xml", "word/footer1.xml", "word/comments.xml",
                     "word/footnotes.xml", "word/endnotes.xml", "word/glossary/document.xml"):
            for tag in ("t", "delText", "instrText"):
                with self.subTest(part=part, tag=tag), tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp) / "mutated.docx"
                    payload = f'<w:root xmlns:w="{ns}"><w:p><w:r><w:{tag}>KI-</w:{tag}></w:r><w:r><w:{tag}>generiert</w:{tag}></w:r></w:p></w:root>'
                    with ZipFile(path, "w") as archive:
                        archive.writestr("word/document.xml", body)
                        archive.writestr(part, payload)
                    with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                        checks.verify_draft_docx(path)

    def test_signature_and_metadata_are_checked(self):
        ns = checks.WORD_NS
        body = f'<w:document xmlns:w="{ns}"><w:body><w:p><w:r><w:t>ENTWURF UR-Nr. ____________________ Vorgesehener Beurkundungstermin</w:t></w:r></w:p></w:body></w:document>'
        for part, payload in (("docProps/custom.xml", "<properties><value>KI-generiert</value></properties>"),
                              ("_xmlsignatures/sig1.xml", "<signature/>")):
            with self.subTest(part=part), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "mutated.docx"
                with ZipFile(path, "w") as archive:
                    archive.writestr("word/document.xml", body)
                    archive.writestr(part, payload)
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    checks.verify_draft_docx(path)


if __name__ == "__main__":
    unittest.main()
