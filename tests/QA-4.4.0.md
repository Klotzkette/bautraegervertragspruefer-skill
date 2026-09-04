# Prüfbericht 4.4.0

Prüfdatum: 4. September 2026. Geprüft wurde die überarbeitete Repository-Fassung, keine reale Erwerbsakte. Die Vertragsklauseln bleiben bewusst differenziertes Prüfmaterial; Layoutfreigabe bedeutet keine juristische Freigabe zur Unterzeichnung.

## Automatisierte Kontrollen

- **25 Regressionstests:** 15 für Ratenrechner und DOCX-Inventur, 10 für Entwurfsartefakte, Übersetzungsbindung und zweisprachige Ausgabe. Dazu gehören Cent-Rundung, Grundstück/Erbbaurecht, Doppelabzug von Sicherheiten, ungültige Zahlen, Strict-OOXML, verschachtelte/umhüllte Tabellen, strukturelle Änderungsmarkierungen, verborgene XML-Teile, fremde Bezugs-UR gegenüber eigener UR, Metadaten und veraltete Übersetzungen.
- **12 Szenarien / 32 Sollbefunde:** Dateiverweise, 16 Quellenanker, konkrete Raten und Rechenwerte konsistent. H/M dritte Rate 18,9 %, Lindenhain vierte Rate 8,4 %; Sonderwunsch-Sicherheit auf den gesamten Zusatzbetrag nach Überschreiten der 10-%-Schwelle.
- **Plugin:** offizieller lokaler Manifestprüfer und alle drei Skill-Strukturprüfer bestanden. Paketprüfung mit bytegleichen Promptreferenzen und deterministischem ZIP. Keine Installation in Benutzerkonten vorgenommen.
- **Quellenstruktur:** 49 historische Entscheidungszeilen, 53 Aktenzeichen/amtliche Entscheidungslinks und fünf Gesetzgebungslinks strukturell erhalten. Dies ist keine neue Volltextprüfung aller historischen Entscheidungen. Für die überarbeitete Falllogik wurden die einschlägigen amtlichen BGB-/MaBV-/BeurkG-Normen nachgeschlagen.
- **Vertragsartefakte:** sechs DOCX einschließlich sämtlicher XML-Teile und sechs Hauptvertrags-PDFs auf Entwurfsstatus; drei Berichte, drei Zahlungsanforderungen und drei ZIP-Pakete auf Struktur/Inhalt geprüft. 33 öffentliche Spiegeldateien müssen bytegleich sein. Das Manifest schützt 51 Quellen-, Bau- und Ausgabedateien.
- **Isolierter Nachbau:** drei deutsche Vertragsakten in temporären Verzeichnissen nachgebaut, 24 Inhaltsvergleiche mit den gelieferten DOCX/PDF/ZIP-Inhalten bestanden. Englische Übersetzungen sind an vollständige Quellblöcke gebunden; deren gesamte Textreihenfolge wird gegen HTML und Word geprüft. Keine automatische Neuübersetzung bei verändertem Quelltext.

## Visuelle Word-Prüfung

Alle sechs finalen Word-Dateien wurden gerendert und jede Seite visuell kontrolliert:

| Akte | Deutsch | Deutsch–Englisch |
| --- | ---: | ---: |
| Hohenwartshofen | 30 Seiten | 41 Seiten |
| Marewald | 25 Seiten | 26 Seiten |
| Lindenhain | 14 Seiten | 26 Seiten |
| Gesamt | 69 Seiten | 93 Seiten |

Geprüft wurden Kopf-/Spaltenköpfe, Haupt-UR, Rahmen der künftigen Beurkundung, Ratentabellen, Anlagen, Seitenumbrüche und Unterschriftsbereiche. Tabellenimportfehler sowie getrennte Überschriften und Unterschriftslinien/Namen wurden korrigiert und erneut gerendert. Die getrennten Sprachspalten behalten ihren vollständigen Text. Nach der finalen Word-Prüfung erfolgten nur noch separate HTML-/PDF-Layoutkorrekturen; keine nachträgliche Word-Inhaltsänderung.

Alle eigenen UR-Felder bleiben leer; „ENTWURF“ steht oben. Keine Bestätigung bereits erfolgter Verlesung/Genehmigung/Unterschrift und kein KI-Herkunftsvermerk im Word-Text. Die bezeichneten Bezugsurkunden behalten ihre Referenznummern. Die englischen Fassungen bleiben eine Verständnishilfe, nicht eine beglaubigte Übersetzung.

## Separate PDF-Prüfung

Die deutschen Hauptverträge (30/25/14 Seiten) und sechs einseitigen Begleitunterlagen wurden vollständig visuell geprüft: zusammen 75 Seiten. Die sieben Raten sind jeweils vollständig lesbar auf H-Seite 6, M-Seite 5 und L-Seite 4. Die zweisprachigen PDFs werden separat erzeugt; Tabellenbreiten, fortlaufende Buchstabenlisten sowie Überschrift-/Text-Zusammenhalt wurden auch dort nach Sichtprüfung korrigiert.

Finale zweisprachige PDF-Sichtprüfung abgeschlossen: Hohenwartshofen 27, Marewald 17, Lindenhain 18 Seiten. Jede Seite wurde kontrolliert und visuell freigegeben: keine sichtbaren Abschneidungen oder Überlagerungen, Ratenpläne innerhalb der Spalten, fortlaufende a/b/c-Aufzählungen und Überschriften zusammen mit Folgeabsätzen. Zusammen mit den deutschen Dateien wurden 137 PDF-Seiten geprüft.

Word- und PDF-Seitenzahlen unterscheiden sich wegen verschiedener Satzsysteme. Geprüft wurde mit LibreOffice/Poppler/WeasyPrint auf dem Arbeitsrechner. Ein abweichender Umbruch auf anderer Word-Version oder mit ersetzten Schriften bleibt möglich. Kein Rendering auf allen Office-/Betriebssystemkombinationen.

## Praxisantworten und Grenzen

Der [Laufbericht mit Rohantworten und Eingabedateihashes](runs/2026-09-04/README.md) enthält zwei abgeschlossene Codex-Einzeltests (Mini H-Z und Plugin M-E). Eine zusätzliche gespeicherte positive Werkstatt-Antwort M-Z+ ist wegen unterbrochenem Agentenabschluss ausdrücklich vorläufig. Die endgültigen Word-Dateien wurden zusätzlich wie oben beschrieben kontrolliert; die Modelltests werden nicht als Läufe auf nachträglich neu erzeugten Binärdateien ausgegeben.

Nicht durchgeführt: vollständiger Zwölf-Szenarien-Modellvergleich, statistische Wiederholungen, Anbieterwechsel, unabhängiges anwaltliches Audit, beglaubigte Übersetzungsprüfung oder echte Kaufpreisfreigabe. Die Prompts sind eigenständig nutzbar und nicht an lokale Werkzeuge gebunden; gleich gute Ergebnisse in allen KIs werden nicht zugesichert.

## Reproduzieren

```sh
bash scripts/validate_repo.sh
# Zusätzlich mit installierten Dokumentwerkzeugen und python-docx:
BTV_VERIFY_BUILDS=1 bash scripts/validate_repo.sh
```

Für echte Modelltests nur mit `tests/prepare_case.py` erzeugte Eingabepakete und die ausgewählte Anleitung übergeben, niemals die Erwartungsmatrix. Antworten unverändert sichern und erst anschließend auswerten. Änderungen an Word/Übersetzungen erfordern erneute Inhalts- und Sichtprüfung, nicht nur ein aktualisiertes Hashmanifest.
