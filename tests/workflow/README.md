# Dialogprüfung der Prompts und Plugin-Einstiege

Diese fünf Verläufe prüfen die Bearbeitung über mehrere Nachrichten: gezielte Rückfrage, vereinbarte Ausarbeitung, neue Fassung, geänderter Nachweisstand sowie Begrenzung und Abbruch. Sie ergänzen die juristischen Einzeltests und die gesonderten Word-Artefakttests. Ein vorhandenes Testszenario ist noch kein durchgeführter Modelllauf.

## Eingaben nacheinander übergeben

1. Für **jede Kombination aus Fall und Prompt/Plugin** einen frischen Chat beginnen. Werkstatt und Mini werden jeweils allein verwendet. Beim Plugin den im Fall bezeichneten Einstieg starten; nur dessen mitgelieferte Ressourcen dürfen hinzukommen.
2. Die Abfolge aus [dialoge.json](dialoge.json) außerhalb des Modellkontexts lesen. Der Prüfer erhält weder dieses Register noch diese README, [erwartungen.json](erwartungen.json), Laufvorlagen oder frühere Auswertungen.
3. Genau die Dateien des ersten Schritts übergeben, in der angegebenen Reihenfolge. Den gesamten Antworttext unverändert sichern. Erst danach die Dateien des zweiten Schritts übergeben, wiederum auf die Antwort warten und anschließend Schritt drei übergeben. **Keine zukünftige Nutzernachricht vorab offenlegen.** Der nächste Schritt baut auf dem tatsächlichen Gespräch auf; Antworten nicht korrigieren oder durch Musterantworten ersetzen.
4. Alle Antworten erst nach Abschluss anhand der getrennten Erwartungen bewerten. Die Begründung muss aus dem tatsächlichen Antworttext folgen. Ein passendes Stichwort allein genügt nicht; zum Beispiel ist eine erneute Problemliste kein angefertigtes Schreiben.
5. Für den nächsten Fall wieder einen frischen Chat verwenden. Gleiche Fälle mit Mini, Werkstatt und passendem Plugin können verglichen werden, sofern Modell, Werkzeuge und Eingaben tatsächlich gleich sind.

Die Zahlungsfälle verwenden unveränderte vorhandene Vertrags-, Berichts- und Rechnungstexte. Die Ergänzung wird hier erst in Nachricht zwei bekannt. Vorgegebene fremde Belegprüfung darf nicht als eigene Originaleinsicht dargestellt werden. Die Fälle benutzen ausdrücklich Markdown, nicht DOCX. Sie sind daher **kein Nachweis einer Word-Prüfung** und enthalten keine erfundenen Änderungsmarkierungen.

## Abdeckung

| Fall | Gesprächsfolge |
| --- | --- |
| W01 | Klauselprüfung → beauftragtes Notariatsschreiben → neue Fassung mit neuer Ausschlussfrist |
| W02 | Entwurfsprüfung → fehlende Anlage, aber konkreter Schreibauftrag → korrigierte Abnahmeformulierung |
| W03 | offene Zahlungsvoraussetzungen → ergänzte positive Tatsachengrundlage → Mandantennachricht |
| W04 | zunächst günstiger Bautenstandsbericht → konkrete Gegenfeststellung → Antwort auf Teilzahlungsverlangen |
| W05 | begrenzte Frage ohne Rückfragen → Stop → begrenzte Fortsetzung |

Alle Schritte sind userseitige Testnachrichten, keine erwarteten Modellantworten. Die Materialien wiederholen keine zusätzliche Verjährungswarnung vor W01. Beträge und gesetzliche Erwartungsgrundlagen knüpfen an die bestehenden Akten an; bei einem echten Einsatz ist der maßgebliche Rechtsstand erneut zu prüfen.

## Bewertung und Laufnachweis

Je gefordertem Ergebnis: 0 = fehlt/falsch; 1 = nur teilweise umgesetzt; 2 = konkret und brauchbar. Für jeden Wert eine kurze Begründung mit Antwortfundstelle sichern. Verbotene Ergebnisse als eigene Fehler notieren. Ein rechtlicher oder tatsächlicher kritischer Fehler wird nicht durch eine gute Sprachbewertung ausgeglichen. Prüfen, ob das Modell wirklich fragt, antwortet, schreibt oder seine Bewertung ändert, nicht nur ob es diese Schritte ankündigt.

[laufvorlage.json](laufvorlage.json) enthält die zu erfassenden Metadaten: Datum, tatsächliche Modellkennung, Prompt-/Plugin-Version und Prüfsumme, tatsächliche System-/Entwicklerzusätze soweit bekannt, Werkzeuge, pro Nachricht Eingabeprüfsummen und Rohantwortdatei, Reihenfolge sowie Ausführungsgrenzen. Unbekanntes bleibt `null`. Für die Auswertung gibt es getrennte Ergebnisfelder; alle sind in der Vorlage leer. Die Vorlage bescheinigt keinen Lauf. Rohantworten und ausgefüllte Auswertung gehören unter `tests/runs/`.

```sh
python3 scripts/test_workflow_dialogue.py
```

Dieses Programm kontrolliert Reihenfolge, vorhandene Eingaben, Trennung von Erwartungen und einige ausdrückliche Arbeitsanweisungen. Es führt **keine Modellgespräche** aus, bewertet **keine juristische Richtigkeit** und belegt **keine allgemeine KI-Leistung**. Die Kontrollen auf Arbeitsanweisungen sind bewusst nur statische Rückfallsicherungen.
