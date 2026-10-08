# Technische und redaktionelle Prüfung 4.8.0

Stand: 8. Oktober 2026. Dateikontrollen, visuelle Prüfung und tatsächliche Dialogantworten sind unterschiedliche Nachweise.

## Technische Kontrollen

Die vollständige Repository-Prüfung `BTV_PYTHON=<gebündeltes Python> bash scripts/validate_repo.sh` wurde nach Abschluss der Berichte erfolgreich ausgeführt, einschließlich Navigation, Quellenstruktur und Vertragsartefakten. Der vorherige Zwischenlauf meldete nur die damals noch nicht angelegten Abschlussberichte als fehlende Verweisziele; diese sind im erfolgreichen Schlusslauf enthalten.

99 Unit-/Regressionstests bestanden: 15 Plugin-Werkzeuge, 10 Vertragsartefakte, 6 Verjährung, 35 Dialog-/Ablaufregeln, 8 portable Abläufe und 25 Promptlayout/Quellenstruktur. Die acht neuen Tests betreffen die getrennte WS01-Eingabe, Zugriffsgrenzen, selbständige Fragen, ausdrückliche Verjährungsprüfung und positive Fortsetzungszweige. Vier weitere Tests sichern Markdown-Quellenlinks und die Trennung zwischen Hauptentscheidung und bloßem Verfahrenskontext. Diese Tests führen keine KI-Rechtsprüfung aus.

Plugin-Manifest und alle drei Skill-Einstiege haben die externen Strukturvalidatoren bestanden. Das Plugin-ZIP ist deterministisch neu gebaut und gegen seine Quellen geprüft; keine Installation oder Änderung eines lokalen Plugin-Caches.

Die bestehenden Testakten sind technisch konsistent: 12 Szenarien, 32 Befunde, 16 Quellenanker einschließlich Raten- und Variationsrechnungen. Sechs Word-Vertragsdateien einschließlich aller XML-Bestandteile und sechs PDFs wurden erneut auf den Entwurfsstatus kontrolliert: eigene Urkundennummer frei, keine vorgetäuschte abgeschlossene Beurkundung, kein KI-Herkunftshinweis in den Vorlagen. 33 öffentliche Spiegeldateien, drei Einzel-PDF-Archive, drei zweisprachige Vertragsfassungen, neun Provenienznachweise und das Manifest mit 51 geschützten Artefakten stimmen überein. Die Vertragsdateien wurden nicht geändert oder neu gerendert; die Kontrolle ist durch ihre unveränderten Prüfsummen gebunden.

## Vollständige Word-Prompts

Werkstatt: **76 Seiten** statt zuvor 47. Mini: **7 Seiten**. Letter, Arial 11 pt, Ränder 2,54 cm. Die Langfassung umfasst 244.797 Zeichen, der eigenständige Mini 21.924 Zeichen. Der Export übernimmt den vollständigen lesbaren Prompt ohne YAML-Metadaten und prüft die identische geordnete Folge der Hauptdokument-Textknoten vor und nach Formatierung. Keine juristische Kürzung zur Einhaltung des 100-Seiten-Rahmens.

Alle finalen PNG-Seiten wurden einzeln in Originalauflösung visuell geprüft: Werkstatt 1–26 und Mini 1–7 durch den Hauptagenten, Werkstatt 27–76 durch einen beauftragten Prüfagenten. Keine abgeschnittenen Texte, Überlappungen oder unleserlichen Quellen. Tabellenköpfe wiederholen sich; Fußzeilen bleiben frei. Drei kleine, nicht inhaltsverändernde Seitenumbrüche trennen eine Maßzahl von ihrer Einheit, Teile eines Aktenzeichens beziehungsweise einen Fundstellenhinweis von der URL. Diese Hinweise sind in der [Layoutakte mit Quell- und Dateiprüfsummen](prompt-layout-4.8.0.json) dokumentiert. Andere Word-Versionen und unmittelbare Markdown-Importe können anders umbrechen.

## Rechtsprechung und Grenzen

Alle 55 vorhandenen Themen wurden erneut recherchiert und ausführlich neu besprochen. 64 Hauptaktenzeichen, 65 Entscheidungslinks und sieben Gesetzgebungslinks sind strukturell erfasst. Die Beleglage umfasst 54 vollständig gelesene amtliche Originale; gerichtliche Reproduktionen, gekürzte Texte und offene Zugriffsgrenzen sind im [Quellenprotokoll](legal-sources-4.8.0.md) einzeln ausgewiesen. Der verbleibende Bestand darf nicht als lückenlos amtlich im Volltext verifiziert bezeichnet werden. Eine vollständige Erfassung aller denkbaren Bauträgerentscheidungen wird nicht behauptet.

Wesentliche Korrekturen betreffen die Aufhebung von KG 21 U 44/22, die begrenzte Reichweite von VII ZR 167/11, die besondere Altrechts-Verjährungslinie zur Fremdabnahme, die aktuelle Anspruchsrichtung gegen Verwalter und GdWE sowie die aufgegebene Unternehmerqualifikation anhand der Umsatzsteueroption. Eine neue Münchener Entscheidung vom August 2026 wurde anhand des Originals eingeordnet. Gesetzgebung und zeitlich gestaffeltes Inkrafttreten sind gesondert geprüft.

## Tatsächliche Dialogproben

Die [gespeicherten Antworten und ihre getrennte Auswertung](runs/2026-10-08/README.md) dokumentieren gezielte Zweirunden-Proben. WS01 ist ausdrücklich eine Textsimulation begrenzter Word-Auswahl, keine Ausführung einer Word-Erweiterung. Ein erneuter vollständiger Gesamtvertragslauf, ein unabhängiges anwaltliches Audit und ein Vergleich verschiedener KI-Anbieter wurden nicht durchgeführt. Die früheren Fehler aus [DP01](runs/2026-09-25/README.md) bleiben als historische Ergebnisse sichtbar und gelten durch diese engeren Proben nicht automatisch als behoben.
