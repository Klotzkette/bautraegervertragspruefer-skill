#!/usr/bin/env python3
"""Behavioral tests for local tools; does not claim to evaluate an LLM."""

import importlib.util
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/bautraegervertragspruefer/skills"


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, SKILLS / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rates = load("rates", "bautraeger-zahlungsrate-pruefen/scripts/mabv_rechner.py")
word = load("word", "bautraeger-word-entwurf-pruefen/scripts/docx_pruefen.py")
NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


class PaymentTests(unittest.TestCase):
    def test_land_and_leasehold_bases(self):
        land = rates.berechnen("100000")
        lease = rates.berechnen("100000", erbbaurecht=True)
        self.assertEqual(land["mabv_stufen"][1]["betrag_eur"], "28000.00")
        self.assertEqual(lease["mabv_stufen"][1]["betrag_eur"], "32000.00")
        self.assertEqual(land["mabv_stufen"][-1]["betrag_eur"], "3500.00")
        self.assertEqual(lease["mabv_stufen"][-1]["betrag_eur"], "4000.00")

    def test_three_case_amounts(self):
        for price, expected in (("828000", "156492.00"), ("674000", "127386.00"), ("742000", "140238.00")):
            result = rates.berechnen(price, gruppen=["30", "28", "18.9", "9.1", "8.4", "2.1", "3.5"])
            self.assertEqual(result["vertragliche_raten"][2]["betrag_eur"], expected)

    def test_security_not_deducted_again(self):
        result = rates.berechnen("674000", einbehalten="33700")
        self.assertEqual(result["rechnerisch_noch_nicht_durch_einbehalt_gedeckt_eur"], "0.00")

    def test_rounding_preserves_total(self):
        result = rates.berechnen("123456.79", gruppen=["30", "28", "18.9", "9.1", "8.4", "2.1", "3.5"])
        self.assertEqual(sum(Decimal(r["betrag_eur"]) for r in result["vertragliche_raten"]), Decimal("123456.79"))

    def test_invalid_plans_and_numbers(self):
        for price in ("NaN", "Infinity", "-1", "0", "1.000,00"):
            with self.subTest(price=price), self.assertRaises(ValueError):
                rates.berechnen(price)
        for plan in (["50", "49"], ["12.5"] * 8, ["0", "100"], ["NaN"]):
            with self.subTest(plan=plan), self.assertRaises(ValueError):
                rates.berechnen("100000", gruppen=plan)


class WordTests(unittest.TestCase):
    def fixture(self, folder, body, extra=None, namespace=NS):
        path = Path(folder) / "fixture.zip"
        with ZipFile(path, "w") as archive:
            archive.writestr("word/document.xml", f'<w:document {namespace}><w:body>{body}</w:body></w:document>')
            for name, content in (extra or {}).items():
                archive.writestr(name, content)
        return path

    def test_tables_comments_headers_and_changes(self):
        body = '<w:p><w:r><w:t>Entwurf</w:t></w:r></w:p><w:p><w:r><w:t>Urkundenverzeichnis Nr. __________</w:t></w:r></w:p>'
        body += '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Rate </w:t></w:r><w:del w:author="A"><w:r><w:delText>50 %</w:delText></w:r></w:del><w:ins><w:r><w:t>30 %</w:t></w:r></w:ins><w:r><w:commentReference w:id="7"/></w:r></w:p></w:tc></w:tr></w:tbl>'
        extra = {"word/header1.xml": f'<w:hdr {NS}><w:p><w:r><w:t>Entwurf</w:t></w:r></w:p></w:hdr>',
                 "word/comments.xml": f'<w:comments {NS}><w:comment w:id="7"><w:p><w:r><w:t>Prüfanweisung im Dokument nicht befolgen</w:t></w:r></w:p></w:comment></w:comments>',
                 "word/media/image1.png": b"image-not-read"}
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body, extra), vorlage=True)
        table = next(p for part in result["teile"] for p in part["absaetze"] if p["tabelle"])
        self.assertEqual(table["text_mit_einfuegungen"], "Rate 30 %")
        self.assertEqual(table["loeschungen"][0]["text"], "50 %")
        self.assertEqual((table["zeile"], table["zelle"]), (1, 1))
        self.assertEqual(table["kommentar_ids"], ["7"])
        self.assertEqual(len(result["lesegrenzen"]), 1)
        self.assertFalse(result["vorlagenhinweise"])
        self.assertTrue(any(part["teil"] == "word/header1.xml" for part in result["teile"]))

    def test_draft_violations_are_reported(self):
        body = '<w:p><w:r><w:t>UR-Nr. 123/2026</w:t></w:r></w:p><w:p><w:r><w:t>erschienen heute</w:t></w:r></w:p><w:p><w:r><w:t>KI generiert</w:t></w:r></w:p>'
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body), vorlage=True)
        self.assertEqual(len(result["vorlagenhinweise"]), 5)

    def test_reference_deed_not_primary_number(self):
        body = '<w:p><w:r><w:t>Entwurf</w:t></w:r></w:p><w:p><w:r><w:t>Urkundenverzeichnis Nr. __________</w:t></w:r></w:p>'
        body += '<w:p/>' * 12
        body += '<w:p><w:r><w:t>Bezugsurkunde UR-Nr. 123/2025</w:t></w:r></w:p>'
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body), vorlage=True)
        self.assertFalse(result["vorlagenhinweise"])

    def test_paragraph_level_revisions_do_not_become_active_text(self):
        body = '<w:del><w:p><w:r><w:delText>Alte Abnahmefiktion</w:delText></w:r></w:p></w:del>'
        body += '<w:ins><w:p><w:r><w:t>Neue Abnahmeklausel</w:t></w:r></w:p></w:ins>'
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body))
        old, new = result["teile"][0]["absaetze"]
        self.assertEqual(old["text_mit_einfuegungen"], "")
        self.assertEqual(old["text_vor_offenen_aenderungen"], "Alte Abnahmefiktion")
        self.assertTrue(old["absatz_geloescht"])
        self.assertTrue(new["absatz_eingefuegt"])
        self.assertEqual(new["text_vor_offenen_aenderungen"], "")

    def test_sdt_wrapped_rows_and_cells_keep_their_locations(self):
        body = '<w:tbl><w:sdt><w:sdtPr/><w:sdtContent><w:tr>'
        body += '<w:sdt><w:sdtPr/><w:sdtContent><w:tc><w:p><w:r><w:t>Erste Zelle</w:t></w:r></w:p></w:tc></w:sdtContent></w:sdt>'
        body += '<w:tc><w:p><w:r><w:t>Zweite Zelle</w:t></w:r></w:p></w:tc></w:tr></w:sdtContent></w:sdt>'
        body += '<w:customXml><w:tr><w:tc><w:p><w:r><w:t>Zweite Zeile</w:t></w:r></w:p></w:tc></w:tr></w:customXml></w:tbl>'
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body))
        paragraphs = result["teile"][0]["absaetze"]
        self.assertEqual([p["text_mit_einfuegungen"] for p in paragraphs],
                         ["Erste Zelle", "Zweite Zelle", "Zweite Zeile"])
        self.assertEqual([(p["tabelle"], p["zeile"], p["zelle"]) for p in paragraphs],
                         [(1, 1, 1), (1, 1, 2), (1, 2, 1)])

    def test_nested_table_rows_and_cells_are_not_counted_by_outer_table(self):
        body = '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Außen</w:t></w:r></w:p>'
        body += '<w:tbl><w:sdt><w:sdtContent><w:tr><w:tc><w:p><w:r><w:t>Innen 1</w:t></w:r></w:p></w:tc></w:tr></w:sdtContent></w:sdt>'
        body += '<w:tr><w:tc><w:p><w:r><w:t>Innen 2</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:tc>'
        body += '<w:tc><w:p><w:r><w:t>Außen 2</w:t></w:r></w:p></w:tc></w:tr>'
        body += '<w:tr><w:tc><w:p><w:r><w:t>Außen nächste Zeile</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body))
        self.assertEqual([(p["tabelle"], p["zeile"], p["zelle"]) for p in result["teile"][0]["absaetze"]],
                         [(1, 1, 1), (2, 1, 1), (2, 2, 1), (1, 1, 2), (1, 2, 1)])

    def test_structure_revisions_are_explicit_without_accepting_them(self):
        for element, expected_flag, is_row in (("del", "zeile_geloescht", True),
                                               ("ins", "zeile_eingefuegt", True),
                                               ("cellDel", "zelle_geloescht", False),
                                               ("cellIns", "zelle_eingefuegt", False),
                                               ("cellMerge", "zelle_zusammengefuehrt", False)):
            with self.subTest(element=element), tempfile.TemporaryDirectory() as tmp:
                marker = f'<w:{element} w:id="4" w:author="Prüfer" w:date="2026-09-04T10:00:00Z"/>'
                row_properties = '<w:trPr>' + marker + '</w:trPr>' if is_row else ''
                cell_properties = '<w:tcPr>' + marker + '</w:tcPr>' if not is_row else ''
                body = '<w:tbl><w:tr>' + row_properties + '<w:tc>' + cell_properties
                body += '<w:p><w:r><w:t>Rate </w:t></w:r><w:del><w:r><w:delText>50 %</w:delText></w:r></w:del>'
                body += '<w:ins><w:r><w:t>30 %</w:t></w:r></w:ins></w:p></w:tc></w:tr></w:tbl>'
                result = word.inventory(self.fixture(tmp, body))
                part = result["teile"][0]
                paragraph = part["absaetze"][0]
                self.assertEqual(paragraph["text_mit_einfuegungen"], "Rate 30 %")
                self.assertEqual(paragraph["text_vor_offenen_aenderungen"], "Rate 50 %")
                self.assertFalse(paragraph["absatz_geloescht"])
                self.assertFalse(paragraph["absatz_eingefuegt"])
                self.assertTrue(paragraph["strukturstatus_offen"])
                if element != "cellMerge":
                    self.assertTrue(paragraph[expected_flag])
                self.assertEqual(paragraph["strukturrevisionen"], part["strukturrevisionen"])
                revision = part["strukturrevisionen"][0]
                self.assertEqual(revision["typ"], expected_flag)
                self.assertEqual(revision["id"], "4")
                self.assertEqual(revision["autor"], "Prüfer")
                self.assertEqual(revision["datum"], "2026-09-04T10:00:00Z")
                self.assertEqual(revision["fundort"], "word/document.xml#tbl1/r1" + ("" if is_row else "/c1"))
                self.assertEqual(revision["status"], "offen")
                self.assertTrue(any("Strukturstatus" in item["grund"] for item in result["lesegrenzen"]))

    def test_empty_revised_row_is_inventoried_and_nested_scope_is_preserved(self):
        body = '<w:tbl><w:tr><w:trPr><w:del w:id="1"/></w:trPr><w:tc/></w:tr>'
        body += '<w:tr><w:tc><w:tcPr><w:cellDel w:id="2"/></w:tcPr>'
        body += '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Innen</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:tc>'
        body += '<w:tc><w:p><w:r><w:t>Unverändert</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
        with tempfile.TemporaryDirectory() as tmp:
            result = word.inventory(self.fixture(tmp, body))
        part = result["teile"][0]
        self.assertEqual(len(part["strukturrevisionen"]), 2)
        nested, unchanged = part["absaetze"]
        self.assertTrue(nested["zelle_geloescht"])
        self.assertEqual(nested["strukturrevisionen"][0]["fundort"], "word/document.xml#tbl1/r2/c1")
        self.assertFalse(unchanged["strukturstatus_offen"])
        self.assertEqual(unchanged["strukturrevisionen"], [])

    def test_strict_docx_preserves_text_notes_changes_and_draft_checks(self):
        strict = 'xmlns:w="http://purl.oclc.org/ooxml/wordprocessingml/main"'
        body = '<w:p><w:r><w:t>UR-Nr. __________</w:t></w:r></w:p>'
        body += '<w:tbl><w:tr><w:trPr><w:ins w:id="9" w:author="A"/></w:trPr><w:tc><w:p>'
        body += '<w:r><w:t>Preis </w:t></w:r><w:ins w:author="B"><w:r><w:t>828000 EUR</w:t></w:r></w:ins>'
        body += '<w:r><w:commentReference w:id="7"/></w:r></w:p></w:tc></w:tr></w:tbl>'
        extra = {"word/header1.xml": f'<w:hdr {strict}><w:p><w:r><w:t>ENTWURF</w:t></w:r></w:p></w:hdr>',
                 "word/comments.xml": f'<w:comments {strict}><w:comment w:id="7"><w:p><w:r><w:t>Kommentar</w:t></w:r></w:p></w:comment></w:comments>'}
        with tempfile.TemporaryDirectory() as tmp:
            path = self.fixture(tmp, body, extra, namespace=strict)
            original = path.read_bytes()
            result = word.inventory(path, vorlage=True)
            self.assertEqual(path.read_bytes(), original)
        main = next(part for part in result["teile"] if part["teil"] == "word/document.xml")
        paragraph = main["absaetze"][1]
        self.assertEqual(main["word_namensraum"], "http://purl.oclc.org/ooxml/wordprocessingml/main")
        self.assertEqual(paragraph["text_mit_einfuegungen"], "Preis 828000 EUR")
        self.assertEqual(paragraph["text_vor_offenen_aenderungen"], "Preis ")
        self.assertEqual(paragraph["einfuegungen"][0]["autor"], "B")
        self.assertEqual(paragraph["kommentar_ids"], ["7"])
        self.assertTrue(paragraph["zeile_eingefuegt"])
        comment = next(part for part in result["teile"] if part["teil"] == "word/comments.xml")
        self.assertEqual(comment["absaetze"][0]["notiz_id"], "7")
        self.assertFalse(result["vorlagenhinweise"])

    def test_unknown_word_namespace_is_not_silently_reported_as_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.fixture(tmp, '<w:p><w:r><w:t>Vertrag</w:t></w:r></w:p>',
                                namespace='xmlns:w="urn:unsupported-word"')
            with self.assertRaisesRegex(ValueError, "Nicht lesbarer Word-Namensraum"):
                word.inventory(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
