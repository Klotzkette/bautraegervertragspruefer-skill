# Technische und redaktionelle Prüfung 4.7.0

Stand: 28. September 2026. Dateikontrollen, visuelle Prüfung und tatsächliche Dialogantworten sind unterschiedliche Nachweise.

## Ausgeführte technische Kontrollen

- `bash scripts/validate_repo.sh` mit gebündeltem Python: bestanden. 87 Unit-/Regressionstests (15 Plugin-Werkzeuge, 10 Vertragsartefakte, 6 Verjährung, 35 Dialog-/Ablaufregeln, 21 Promptlayout/Quellenstruktur).
- Plugin-Manifest und alle drei Skill-Einstiege: externe Strukturvalidatoren bestanden.
- Neue ID01-Fixture: zwei getrennte Eingaben, verborgene Erwartungen, feste Reihenfolge. Sieben neue Tests prüfen unter anderem vorgezogene Folgeeingaben und unzulässige Evaluatorbeigaben. Zwei bestehende Textmuster wurden grammatikalisch um Singular „Antwort“ beziehungsweise „bezeichneten“ erweitert; die geprüften Verhaltensanforderungen bleiben erhalten.
- Testakten: 12 Szenarien, 32 Befunde, 16 Quellenanker; Raten, Zahlungsanforderungen und Variationsrechnungen konsistent.
- Sechs Word-Vertragsdateien einschließlich aller XML-Bestandteile sowie sechs PDFs auf Entwurfsstatus kontrolliert: eigene Urkundennummer frei, keine vorgetäuschten abgeschlossenen Beurkundungsakte, kein KI-Herkunftshinweis in den Vorlagen.
- 33 öffentliche Spiegeldateien, drei Einzel-PDF-Archive, zweisprachige Fassungen und 51 geschützte Artefakte konsistent. Vertragsdateien wurden in dieser Fassung nicht geändert und nicht neu gerendert; ihr Inhalt ist durch die unveränderten Artefaktprüfsummen gebunden.
- Plugin-ZIP deterministisch neu gebaut und gegen sämtliche Paketquellen geprüft. Keine Installation oder Änderung eines lokalen Plugin-Caches.

## Vollständige Word-Prompts

Werkstatt: 47 Seiten. Mini: 7 Seiten. Letter, Arial 11 pt, Ränder 2,54 cm. Das Exportskript übernimmt den vollständigen lesbaren Prompt ohne YAML-Metadaten und prüft die identische geordnete Textfolge vor und nach Formatierung. Beide Dokumente unterschreiten die Grenze von 100 tatsächlich gerenderten Seiten.

Alle finalen PNG-Seiten wurden einzeln in Originalauflösung visuell geprüft: Werkstatt 1–24 durch einen Prüfagenten, Werkstatt 25–47 und Mini 1–7 durch den Hauptagenten. Keine abgeschnittenen Texte, Überlappungen oder isolierten Überschriften festgestellt; Tabellen, wiederholte Tabellenköpfe und Quellen sind lesbar. [Layoutakte mit Quell- und Dateiprüfsummen](prompt-layout-4.7.0.json). Ein anderer Word-Renderer oder der unmittelbare Import einer Markdown-Datei kann anders umbrechen.

## Rechtsprechung und Grenzen

55 Katalogeinträge mit 59 Aktenzeichen und 59 Entscheidungslinks. Die drei neuen Anker, die Berichtigung der Stuttgarter Entscheidung und die aktive Vertiefung der BGH-Entscheidungen zur Fremdabnahme und Schlussrate sind im [Quellenprotokoll](legal-sources-4.7.0.md) dokumentiert. Der übrige historische Quellen- und Gesetzgebungsbestand wurde nicht insgesamt neu geprüft. Der Strukturchecker bestätigt weder die heutige Erreichbarkeit aller Links noch die rechtliche Richtigkeit sämtlicher Inhalte.

Die neue Fassung verlangt sofortige Arbeit am verfügbaren Material, begründete Rückfragen in kurzen Runden, Weiterarbeit an unabhängigen Teilen und aktualisierte Schreiben nach neuen Antworten. Die rechtliche Perspektive bleibt diejenige der Erwerberin. Fehlende Aktenbestandteile werden nicht als nichtexistent behandelt; ein Notartermin ist kein Beweis einer erstmaligen Beurkundung und ein Änderungsvorschlag keine vereinbarte Fassung.

## Tatsächliche Dialogproben

Die [drei gezielten ID01-Läufe](runs/2026-09-28/README.md) enthalten jeweils zwei tatsächlich erzeugte Antworten in einem frischen Kontext. Alle sechs Antworten und frühen Mitteilungen sind unverändert archiviert; Folgeeingaben wurden erst nach Abschluss der jeweiligen ersten Antwort freigegeben. Alle drei Einstiege erstellten unmittelbar die drei Produkte und führten Vertragsphase, Klauselbeanstandungen und Unterlagen in der nächsten Runde fort. Die aktuelle BGH-Rechtsprechung zur Fremdabnahme wurde angewandt.

Die separate Auswertung dokumentiert auch mehrteilige Rückfragegruppen, die fehlende ausdrückliche Nennung von § 309 Nr. 8 b ff im Mini trotz erkannter Verjährungsproblematik sowie unvollständige Nachweise der Aktualitätsrecherche. Werkstatt und Mini wurden zusätzlich von einem anderen Prüfagenten bewertet. Die Läufe ersetzen weder einen erneuten vollständigen Gesamtvertragslauf noch ein unabhängiges anwaltliches Audit oder modellübergreifende Vergleichstests. Die früheren Fehler aus [DP01](runs/2026-09-25/README.md) bleiben als historische Ergebnisse sichtbar.
