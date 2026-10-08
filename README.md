# Bauträgervertragsprüfer

Fassung 4.8.0 verbindet einen gut lesbaren Einstieg mit einer deutlich erweiterten juristischen Langfassung. Die Prüfung beginnt unmittelbar am Vertrag und führt über begründete Rückfragen zu Gutachten, Mandantenschreiben und passenden Entwürfen an Bauträger beziehungsweise Notariat. Kein Zusatzauftrag und kein Kennwort „Vollpaket“ nötig.

Version 4.8.0 prüft deutsche Bauträgerverträge stets aus Sicht der Erwerberin. Pro Runde höchstens drei selbständige entscheidungserhebliche Fragen, keine versteckten Fragenbündel. Neue Angaben ändern sämtliche betroffenen Bewertungen und Schreiben. Ein Notartermin beweist keine erstmalige Beurkundung, ein Änderungsvorschlag keine bereits vereinbarte Änderung. Webchat, Plugin und Word verwenden denselben fachlichen Ablauf mit ausdrücklich benannten Zugriffsgrenzen.

**Menü:** [Prompts](#werkstatt-und-mini-prompt) · [Plugin](#plugin-mit-drei-skills) · [Word](#word-vertragsvorlagen) · [Testakten](#testakten) · [Prüfung](#qualität-und-grenzen) · [Dateien](#repository-dateien) · [Lizenz](#lizenz)

## Werkstatt und Mini-Prompt

| Einsatz | Datei dieser Repository-Fassung | Letzte veröffentlichte Release-Fassung |
| --- | --- | --- |
| Gründliche Vertragsprüfung | [Werkstatt-Prompt](skill/SKILL.md) | [SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) |
| Kleines Kontextfenster | [Mini-Prompt](skill/MINI_SKILL.md) | [MINI_SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md) |

Formatierte Word-Fassungen: [Werkstatt-Prompt 4.8.0 als DOCX](docs/downloads/werkstatt-prompt-4.8.0.docx) mit **76 Seiten** statt bisher 47 und [Mini-Prompt 4.8.0 als DOCX](docs/downloads/mini-prompt-4.8.0.docx) mit **7 Seiten**. Gemessen mit LibreOffice, Letter, Arial 11 pt und 2,54 cm Rändern; Word-Version und Schriftverfügbarkeit können den Umbruch verändern. Markdown selbst hat keine feste Seitenzahl. Die Langfassung wächst von 137.497 auf 244.797 Zeichen. Ihre 55 vertieften Rechtsprechungseinträge behandeln 64 Hauptaktenzeichen mit Sachverhalt, tragenden Gründen, Ergebnis, konkreter Verwendung und Grenzen. Die Word-Dateien enthalten den vollständigen lesbaren Prompt ohne technischen YAML-Metadatenblock; keine juristischen Kürzungen zur Einhaltung des 100-Seiten-Rahmens.

Eine Datei als Arbeitsanweisung in den gewünschten Chat laden oder ihren Text kopieren. Dann den Vertrag und die dazugehörigen Anlagen hinzufügen. Beide Prompts enthalten die nötigen Prüfanweisungen selbst; sie setzen weder dieses Plugin noch ein bestimmtes KI-Produkt voraus. Datei-, Bild- und Internetzugriff hängen vom verwendeten System ab. Die Prompts verlangen, konkrete Lese- und Quellenlücken offenzulegen.

Kopierfertiger Start für die Vertragsprüfung:

```text
Prüfe den beigefügten Bauträgervertrag vollständig aus Käufersicht. Verwende
den beigefügten Werkstatt- bzw. Mini-Prompt. Stelle zuerst fest, welche
Vertragsfassung und welche Anlagen tatsächlich lesbar vorliegen und ob
ein Entwurf oder eine beurkundete Fassung belegt ist. Begründe jeden
wesentlichen Befund an seiner Klausel, rechne die Zahlungsraten nach und
formuliere konkrete, zur Vertragsphase passende Änderungen. Kläre
entscheidende Lücken mit gezielten Rückfragen. Erstelle unmittelbar das
Gutachten, ein Mandantenschreiben und passende Entwürfe an Bauträger oder
Notariat. Arbeite Antworten und neue Fassungen in alle betroffenen Texte ein.
```

Für einen Zahlungsfall:

```text
Prüfe die konkrete Zahlungsanforderung anhand von Vertrag, notariellem
Fälligkeitsnachweis, Freistellung, Sicherheit, Bautenstandsbericht und
Zahlungsverlauf. Trenne Ratenhöhe, Fälligkeit und Nachweislücken. Zeige
Widersprüche zwischen Einzelpositionen und Berichts-Fazit. Gib einen
zahlbaren Betrag nur an, soweit er sich aus den Belegen ableiten lässt.
```

„Bitte prüfe den Vertrag vollständig“ umfasst schon die drei ausgearbeiteten Produkte. Erhebliche erforderliche Änderungen und Nachweise werden in die passenden Schreiben übernommen; Verhandlungswünsche bleiben als solche erkennbar. Fehlende Anlagen führen zu gezielten Fragen und bedingten Ergebnissen, nicht zum Stillstand. Nachgereichte Unterlagen ändern sämtliche betroffenen Texte; unveränderte offene Punkte bleiben erhalten. Ausdrückliche Begrenzungen wie „nur Analyse“, „keine Schreiben“ oder „nur technische Word-Prüfung“ werden respektiert. Entwerfen erlaubt weder Versand noch Zahlung oder rechtsgeschäftliche Erklärungen.

Der gesamte bisherige Rechtsprechungskatalog wurde am 08.10.2026 erneut bearbeitet. Fünf weitere Originalentscheidungen ergänzen den Bestand, darunter die neue Münchener Entscheidung zur persönlichen Sicherheitsstellungshaftung vom August 2026. [Quellenprotokoll und Übertragungsgrenzen](tests/legal-sources-4.8.0.md) trennen 54 vollständig gelesene amtliche Originale von gerichtlichen Reproduktionen, Auszügen und offenen Beleglücken. Aufgehobene oder ausdrücklich aufgegebene Aussagen bleiben nicht als heutige Gegenautorität stehen. Der Gesetzgebungsstand ist gesondert aktualisiert. Die Prompts verlangen weiterhin fallbezogene Recherche während der Bearbeitung, keinen vorgelagerten Abruf sämtlicher Links. Gleiche Ergebnisqualität in unterschiedlichen Modellen wird nicht behauptet.

Beide Fassungen verlangen eine ausdrückliche Verjährungsprüfung: Bauwerksmängel regelmäßig fünf Jahre ab maßgeblicher Abnahme (§ 634a Abs. 1 Nr. 2, Abs. 2 BGB), eine Zweijahresverkürzung in Verbraucher-AGB unwirksam nach § 309 Nr. 8 b ff BGB. Vorgezogener Beginn, technische Gebäudeanlagen und verdeckte Mängelanzeigefristen gehören dazu. Echte Individualvereinbarungen und die gesetzliche Zweijahresfrist für nicht bauwerksbezogene Werke werden gesondert beurteilt. Dazu gibt es [sieben gezielte Testfälle](tests/limitation/README.md) und [Praxisantworten der früheren Fassung](tests/runs/2026-09-09/README.md).

Der Mini umfasst 21.924 Zeichen bei einer Grenze von 22.000 und bleibt eigenständig. Die neue [Word-Auswahlprobe WS01](tests/workflow/word-selection/README.md) prüft eine Zweijahresklausel und danach einen Vorschlag mit fünf Jahren, aber unverändert vorgezogenem Fristbeginn. Sie simuliert begrenzten Word-Zugriff als Text, keine echte Word-Erweiterung. Die [ID01-Dialogprobe](tests/workflow/immediate-dialogue/README.md), der [DP01-Dialogfall](tests/workflow/default-package/dialoge.json) und [fünf weitere Mehrturn-Testfälle](tests/workflow/README.md) bleiben erhalten. Eingaben und Erwartungen sind getrennt; statische Kontrollen belegen keine Modellleistung.

Reproduzierbarer Word-Export: `python scripts/export_prompt_docx.py skill/SKILL.md neuer-werkstatt-prompt.docx --soffice /pfad/zu/soffice`. Benötigt Python mit `python-docx`, Pandoc, LibreOffice und `pdfinfo`. Das Skript erhält bestehende Zieldateien und verweigert die Ausgabe oberhalb von 100 tatsächlich gerenderten Seiten. Vor Weitergabe alle Seiten visuell prüfen; ein Seitenzähler allein ist keine Layoutkontrolle.

## Plugin mit drei Skills

[Plugin-ZIP herunterladen](docs/downloads/bautraegervertragspruefer-plugin.zip) oder [Plugin-Quellen ansehen](plugins/bautraegervertragspruefer). Das Paket enthält Manifeste für Codex und Claude Code, drei Skills, den vollständigen Werkstatt-Prompt und zwei lokale Python-Werkzeuge. Es benötigt keine Zugangsdaten. Die Installation richtet sich nach der Plugin-Funktion des jeweiligen Programms; das Repository installiert nichts im Hintergrund.

| Skill | Aufgabe |
| --- | --- |
| [`bautraegervertrag-pruefen`](plugins/bautraegervertragspruefer/skills/bautraegervertrag-pruefen/SKILL.md) | Gesamtprüfung mit Fundstellen, Subsumtion, Gegenargument und konkreter Abhilfe |
| [`bautraeger-zahlungsrate-pruefen`](plugins/bautraegervertragspruefer/skills/bautraeger-zahlungsrate-pruefen/SKILL.md) | Abruf, Ratenplan, Bautenstand, Fälligkeitsbelege und Sicherheiten abgleichen |
| [`bautraeger-word-entwurf-pruefen`](plugins/bautraegervertragspruefer/skills/bautraeger-word-entwurf-pruefen/SKILL.md) | DOCX einschließlich Tabellen, Kommentaren, Änderungen und Entwurfsstatus aufnehmen |

Die Rechenhilfe verwendet Dezimalbeträge, trennt 70-%- und 80-%-Restbasis und verhindert doppelte Berücksichtigung bereits einbehaltener Sicherheit. Sie entscheidet nicht über die rechtliche Fälligkeit. Der Word-Extraktor gibt XML-Fundorte aus, keine erfundenen Word-Seitenzahlen. Bilder, eingebettete Dateien und ungeprüfte externe Verknüpfungen bleiben als Lesegrenzen sichtbar.

## Word-Vertragsvorlagen

Die drei Vertragsvorlagen stehen jeweils auf Deutsch und als deutsch-englische Lesefassung bereit:

| Akte | Deutsch | Deutsch und Englisch |
| --- | --- | --- |
| Hohenwartshofen / Am Birkenpfuhl | [Word-Entwurf](vertragsdokumente/bautraegervertrag/bautraegervertrag.docx) | [Word-Lesefassung](vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx) |
| Marewald Höfe | [Word-Entwurf](vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx) | [Word-Lesefassung](vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx) |
| Lindenhain 12 | [Word-Entwurf](vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx) | [Word-Lesefassung](vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx) |

Oben steht **Entwurf**, die eigene Urkundennummer bleibt frei. Der Vorlagenrahmen behauptet keine bereits erfolgte Beurkundung, Verlesung, Genehmigung oder Unterschrift. Nummern tatsächlich bezeichneter Bezugsurkunden bleiben erhalten. Die Word-Vorlagen enthalten keinen Hinweis „KI generiert“.

Die Vertragsklauseln sind Prüfmaterial und enthalten auch beanstandungswürdige Regelungen. Diese werden als Testeingabe erhalten. Eine gut gestaltete Vorlage und die Bezeichnung einer Akte sind keine rechtliche Freigabe. Tatsächlich beurkundete Fremddokumente werden bei einer Prüfung nicht in Entwürfe umgeschrieben.

## Testakten

[Aktenübersicht und Formate](vertragsdokumente/README.md): [Hohenwartshofen](vertragsdokumente/bautraegervertrag/README.md), [Marewald](vertragsdokumente/bautraegervertrag-marewald/README.md), [Lindenhain](vertragsdokumente/bautraegervertrag-lindenhain/README.md).

Die Tests trennen die Word-Entwurfsprüfung vor Beurkundung von ausdrücklich beschriebenen späteren Zahlungsszenarien. Ein Vertragsentwurf allein beweist weder eine Beurkundung noch den Eintritt allgemeiner Fälligkeitsvoraussetzungen. Eine im Begleitschreiben erwähnte Bankgarantie oder Notarmitteilung gilt nicht als selbst gelesenes Dokument.

Im [Testbereich](tests/) liegen neutrale Aufträge, nachvollziehbare Rechenerwartungen, klauselscharfe Sollbefunde und Gegenproben. Erwartungsdaten werden einem prüfenden Modell nicht mitgegeben. Die Bewertung erfasst auch unberechtigte Beanstandungen, erfundene Tatsachen, Verwechslungen von Klauselkontrolle und Zahlungsentscheidung sowie ignorierte Word-Inhalte. Der Teststatus unterscheidet statische Kontrollen, ausgeführte Werkzeugtests und tatsächlich durchgeführte Modellläufe.

## Qualität und Grenzen

```bash
bash scripts/validate_repo.sh
```

Die Prüfungen kontrollieren Prompt- und Plugin-Konsistenz, Dateien und Verweise, Rechenverhalten, Word-Auswertung, die Quellenstruktur sowie Vertragsartefakte und deren Spiegelkopien. Die Mehrturn-Tests kontrollieren außerdem Eingabetrennung und gezielte Ablaufregeln; tatsächliche Antworten werden gesondert bewertet. Ein langer Prompt oder ein bestandener Textvergleich belegt keine gute Rechtsprüfung.

Mit `BTV_VERIFY_BUILDS=1 bash scripts/validate_repo.sh` werden zusätzlich die deutschen Vertragsartefakte isoliert nachgebaut. `python3 scripts/check_legal_anchors.py --online` prüft die Erreichbarkeit hinterlegter Quellen. Ein erfolgreicher Abruf bestätigt weder die Richtigkeit einer Zusammenfassung noch die Übertragbarkeit einer Entscheidung. Die konkrete juristische Verwendung erfordert die Prüfung von Normstand, Volltext und Fallbezug.

Der Workflow für Word-Dateien umfasst Text- und Strukturkontrolle sowie Rendern und visuelle Prüfung. Nur sichtbare Auswahl bedeutet nur Teilprüfung; fehlender Dateiexport verhindert keine ausgearbeiteten Chattexte. Der [Prüfbericht 4.8.0](tests/QA-4.8.0.md) und die [aktuellen Praxisantworten mit Auswertung](tests/runs/2026-10-08/README.md) dokumentieren die tatsächlich ausgeführten Kontrollen und ihre Grenzen. Ein erneuter vollständiger Gesamtvertragslauf oder anbieterübergreifender Leistungstest wird nicht behauptet. Die fachlichen Lücken früherer [Gesamtvertragsproben](tests/runs/2026-09-25/README.md) werden durch die engeren Dialogproben nicht für erledigt erklärt. [Prüfbericht 4.7.0](tests/QA-4.7.0.md) und [frühere Praxisantworten](tests/runs/2026-09-28/README.md) bleiben unverändert erhalten.

## Repository-Dateien

| Zweck | Dateien |
| --- | --- |
| Portable Prompts | [Werkstatt](skill/SKILL.md), [Mini](skill/MINI_SKILL.md) |
| Plugin | [Manifest](plugins/bautraegervertragspruefer/.codex-plugin/plugin.json), [Paketbau](scripts/package_plugin.py), [Werkzeugtests](scripts/test_plugin_tools.py) |
| Testakten | [Übersicht](vertragsdokumente/README.md), [Testbereich](tests/) |
| Word und PDF erzeugen | [Zweisprachiger Builder](scripts/build_bilingual_contracts.py), [Artefaktprüfer](scripts/check_contract_builds.py), [Quellenmanifest](vertragsdokumente/artifact-manifest.sha256), [Aktenlayout](vertragsdokumente/case-style.css) |
| Validierung | [Gesamtprüfung](scripts/validate_repo.sh), [Promptstruktur](scripts/check_skill_quality.py), [Workflow/Paket](scripts/check_workflow_contract.py), [Rechtsanker](scripts/check_legal_anchors.py), [Navigation](scripts/check_navigation.py) |
| Dokumentation | [Downloadseite](docs/index.html), [Werkstatt-Spiegel](docs/SKILL.md), [Mini-Spiegel](docs/MINI_SKILL.md), [Änderungen](CHANGELOG.md) |
| Automatisierung | [Validierung](.github/workflows/validate.yml), [Spiegelprüfung](.github/workflows/sync-docs.yml) |

Die Repository-Fassung und die zuletzt veröffentlichte Release-Fassung können sich unterscheiden. `releases/latest` zeigt immer auf die letzte Veröffentlichung; die relativen Dateilinks oben zeigen die hier vorliegende Fassung.

## Lizenz

Wahlweise [MIT](LICENSE-MIT) oder [Apache-2.0](LICENSE-APACHE). Dieses Repository enthält mit KI-Unterstützung entwickelte Texte und Testdaten. Der Hinweis zur Entstehung steht in der Projektbeschreibung, nicht im Text der Word-Vertragsvorlagen.
