# Bauträgervertragsprüfer

Version 4.4.0 prüft deutsche Bauträgerverträge aus Erwerbersicht: Vertragsklauseln, Anlagen, Zahlungsraten, Abnahme, Bausoll und Eigentumssicherung. Jeder wesentliche Befund muss auf eine lesbare Stelle der vorgelegten Akte zurückgehen und eine begründete, zur Vertragsphase passende Handlung ergeben.

**Menü:** [Prompts](#werkstatt-und-mini-prompt) · [Plugin](#plugin-mit-drei-skills) · [Word](#word-vertragsvorlagen) · [Testakten](#testakten) · [Prüfung](#qualität-und-grenzen) · [Dateien](#repository-dateien) · [Lizenz](#lizenz)

## Werkstatt und Mini-Prompt

| Einsatz | Datei dieser Repository-Fassung | Letzte veröffentlichte Release-Fassung |
| --- | --- | --- |
| Gründliche Vertragsprüfung | [Werkstatt-Prompt](skill/SKILL.md) | [SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) |
| Kleines Kontextfenster | [Mini-Prompt](skill/MINI_SKILL.md) | [MINI_SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md) |

Eine Datei als Arbeitsanweisung in den gewünschten Chat laden oder ihren Text kopieren. Dann den Vertrag und die dazugehörigen Anlagen hinzufügen. Beide Prompts enthalten die nötigen Prüfanweisungen selbst; sie setzen weder dieses Plugin noch ein bestimmtes KI-Produkt voraus. Datei-, Bild- und Internetzugriff hängen vom verwendeten System ab. Die Prompts verlangen, konkrete Lese- und Quellenlücken offenzulegen.

Kopierfertiger Start für die Vertragsprüfung:

```text
Prüfe den beigefügten Bauträgervertrag vollständig aus Käufersicht. Verwende
den beigefügten Werkstatt- bzw. Mini-Prompt. Stelle zuerst fest, welche
Vertragsfassung und welche Anlagen tatsächlich lesbar vorliegen und ob
ein Entwurf oder eine beurkundete Fassung belegt ist. Begründe jeden
wesentlichen Befund an seiner Klausel, rechne die Zahlungsraten nach und
formuliere konkrete, zur Vertragsphase passende Änderungen. Behandle
fehlende Belege als offene Punkte und würdige auch tragfähige Regelungen.
```

Für einen Zahlungsfall:

```text
Prüfe die konkrete Zahlungsanforderung anhand von Vertrag, notariellem
Fälligkeitsnachweis, Freistellung, Sicherheit, Bautenstandsbericht und
Zahlungsverlauf. Trenne Ratenhöhe, Fälligkeit und Nachweislücken. Zeige
Widersprüche zwischen Einzelpositionen und Berichts-Fazit. Gib einen
zahlbaren Betrag nur an, soweit er sich aus den Belegen ableiten lässt.
```

„Vollständig prüfen“ verlangt die vollständige Analyse. Wer zusätzlich Schreiben möchte, ergänzt: `Vollpaket: Mandantenanschreiben, ausführliches Gutachten und phasengerechtes Schreiben an den Bauträger.` Ein Abbruch lässt sich anhand der Fortsetzungsnotiz fortführen.

Die Werkstatt enthält einen konzentrierten Arbeitsablauf sowie einen ausdrücklich historischen Rechtsprechungs- und Gesetzgebungsbestand. Der Mini-Prompt priorisiert ausführbare Prüfregeln statt langer Aktenzeichenlisten. Die Verwendung in einem anderen Modell ist möglich; eine gleiche Ergebnisqualität über verschiedene Modelle hinweg wird nicht behauptet.

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

Die Prüfungen kontrollieren Prompt- und Plugin-Konsistenz, Dateien und Verweise, Rechenverhalten, Word-Auswertung, die Quellenstruktur sowie Vertragsartefakte und deren Spiegelkopien. Die frühere Mindestlänge von 370.000 Zeichen und Tests auf vorgeschriebene Schlagwörter wurden durch prüfbare Paket- und Verhaltenskontrollen ersetzt. Ein langer Prompt oder ein bestandener Textvergleich belegt keine gute Rechtsprüfung.

Mit `BTV_VERIFY_BUILDS=1 bash scripts/validate_repo.sh` werden zusätzlich die deutschen Vertragsartefakte isoliert nachgebaut. `python3 scripts/check_legal_anchors.py --online` prüft die Erreichbarkeit hinterlegter Quellen. Ein erfolgreicher Abruf bestätigt weder die Richtigkeit einer Zusammenfassung noch die Übertragbarkeit einer Entscheidung. Die konkrete juristische Verwendung erfordert die Prüfung von Normstand, Volltext und Fallbezug.

Der Workflow für Word-Dateien umfasst Text- und Strukturkontrolle sowie Rendern und visuelle Prüfung. Der [Prüfbericht 4.4.0](tests/QA-4.4.0.md) und die [gesicherten Praxisantworten](tests/runs/2026-09-04/README.md) dokumentieren die tatsächlich ausgeführten Kontrollen; fehlende Tests werden nicht als bestanden dargestellt.

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
