# Technische und redaktionelle Prüfung 4.6.0

Stand: 25. September 2026. Diese Prüfung unterscheidet Dateikontrollen, visuelle Prüfung und tatsächliche Modellantworten.

## Ausgeführte Kontrollen

- `bash scripts/validate_repo.sh` mit gebündeltem Python: bestanden. 80 Unit-/Regressionstests (15 Plugin-Werkzeuge, 10 Vertragsartefakte, 6 Verjährung, 28 Dialog-/Ablaufregeln, 21 Promptlayout/Quellenstruktur).
- Drei Skill-Einstiege und Plugin-Manifest: externe Strukturvalidatoren bestanden.
- Testakten: 12 Szenarien, 32 Befunde und 16 Quellenanker; Raten, Zahlungsanforderungen und Variationsrechnungen konsistent.
- Vertragsbestand: sechs Word-Dateien einschließlich sämtlicher XML-Bestandteile sowie sechs PDFs auf Entwurfsstatus geprüft. Eigene Urkundennummer frei, keine behauptete abgeschlossene Beurkundung und kein KI-Herkunftshinweis in den Vorlagen.
- 33 öffentliche Spiegeldateien, drei Einzel-PDF-Archive, zweisprachige Fassungen und 51 geschützte Artefakte: konsistent.
- Plugin-ZIP reproduzierbar und mit den Quellfassungen identisch.
- Isolierter Neubau aller drei deutschen Vertragsakten: bestanden, 24 Inhaltsvergleiche. Der erste Versuch verwendete im untergeordneten Build den falschen Python-Pfad; mit dem gebündelten Python einschließlich `python-docx` vollständig wiederholt. Die veröffentlichten Vertragsdateien wurden nicht überschrieben.

## Word-Prompts

Werkstatt: 44 Seiten. Mini: 6 Seiten. Letter, Arial 11 pt, Ränder 2,54 cm. Der Export übernimmt den vollständigen lesbaren Prompt ohne YAML-Metadatenblock und prüft die geordnete Textfolge.

Der Hauptagent hat sämtliche finalen 44 beziehungsweise sechs PNG-Seiten einzeln visuell geprüft: lesbare Absätze und Tabellen, vollständige Texte, keine Überlappungen oder abgeschnittenen Quellen. Die [Layoutakte](prompt-layout-4.6.0.json) enthält genaue Quell- und Dateiprüfsummen. Andere Word-Versionen und ein unmittelbarer Markdown-Import können anders umbrechen.

## Fachliche Änderungen und Nachweisgrenze

Alle 49 bisherigen Rechtsprechungseinträge sind erhalten; drei im aktiven Fachteil verwendete Entscheidungen wurden zusätzlich im Katalog erschlossen. Insgesamt 52 Einträge mit 56 Aktenzeichen und 56 Quellenadressen. Die Quellenstrukturprüfung bestätigt keine vollständige juristische Richtigkeit oder aktuelle Erreichbarkeit sämtlicher Nachweise.

Die Ergänzungen wurden quellenbezogen kontrolliert, insbesondere die Normen zu Selbstvornahme, Verbraucher-AGB und Bauträgervertrag sowie die Originaltexte von KG 21 U 79/17, OLG München 9 W 1431/25 Bau e und BGH III ZR 136/07. Bei letzterer Entscheidung wurde eine falsche Deutung der „doppelten Belehrung“ berichtigt: gemeint sind Risiko und Sicherungsmöglichkeiten, keine generelle Wiederholung unmittelbar vor Zahlung. Einzelne weitere BGH-Aussagen wurden anhand amtlicher Entscheidungsnachweise oder späterer amtlicher Entscheidungen abgeglichen; ein neuer Volltextabruf aller 52 Einträge wird nicht behauptet.

Die frühere zusätzliche Bestellhürde für Gutachten und Schreiben wurde entfernt. Die normale Gesamtprüfung erfolgt aus Erwerberinnensicht und verlangt sofort sämtliche Produkte; ausdrücklich begrenzte Aufträge bleiben begrenzt. Fehlende Anlagen blockieren nicht die unabhängig möglichen Arbeiten. Notwendige Korrekturen müssen in den passenden Schreiben und späteren Nachträgen erhalten bleiben.

## Reichweite

Statische Kontrollen prüfen Regeln und Dateien, nicht die tatsächliche Leistung eines KI-Modells. Die neue Fallprobe DP01 verwendet eine gewöhnliche Prüfbitte ohne ausdrücklichen Schreibauftrag und erst danach einen Klauselrücklauf. Drei abgeschlossene Dialoge, drei begrenzte Klauselproben und drei begrenzte Schreibproben ergeben zwölf tatsächliche Antworttexte. [Auswertung, unveränderte Rohantworten und genaue Instruktionsstände](runs/2026-09-25/README.md) dokumentieren auch technische Fortsetzungen und fachliche Lücken. Alle DP01-Dialoge liefern die Produkte, bestehen aber wegen fachlicher Lücken beziehungsweise fehlender Befundübernahme nicht die strenge Gesamtbewertung. Die daraus abgeleiteten Normreferenz- und Anlagen-Zusätze wurden gezielt nachgeprüft; die dortigen Erwartungen sind erfüllt. Die gesamte Akte wurde nach diesen Zusätzen nicht erneut geprüft. Ein unabhängiges anwaltliches Audit, wiederholte statistische Messungen oder Vergleichsläufe bei anderen KI-Anbietern sind nicht Bestandteil dieser technischen Prüfung.
