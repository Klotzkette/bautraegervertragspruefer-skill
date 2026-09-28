# Sofort beginnen und im Dialog fortsetzen

ID01 ist eine synthetische Zweirunden-Probe mit Fallstichtag 28.09.2026. Sie prüft den unmittelbaren Einstieg trotz unvollständiger Akte, begründete Rückfragen, drei bereits nutzbare Produkte und deren Fortsetzung nach einer Klarstellung. Sie ist ein Texttest und kein Nachweis einer Word-Prüfung. Die Fixturedateien allein belegen keinen Modelllauf.

## Blindlauf

Für jeden Lauf mit Werkstatt, Mini oder dem Plugin-Einstieg `bautraegervertrag-pruefen` einen frischen Chat beziehungsweise Blindagenten verwenden. Nur die jeweils zu prüfende Anweisung und die aktuell freigegebene Eingabedatei übermitteln. Der Blindagent erhält weder diese README noch [dialoge.json](dialoge.json), [erwartungen.json](erwartungen.json), frühere Auswertungen oder weitere Testdateien.

1. Zunächst ausschließlich [id01-01.md](inputs/id01-01.md) als Nutzernachricht übergeben. Die vollständige tatsächliche Antwort unverändert sichern.
2. Erst danach [id01-02.md](inputs/id01-02.md) in denselben Gesprächsverlauf geben. Die zweite Nachricht weder vorab offenlegen noch mit der ersten zusammenfassen. Auch diese Antwort unverändert sichern; keine Antwort zwischenzeitlich durch eine Musterlösung ersetzen.
3. Beide Antworten anschließend außerhalb des Blindlaufs anhand der getrennten Erwartungen bewerten. Jede Feststellung braucht einen Beleg im tatsächlichen Antworttext. Begrenzte oder fehlende Recherchewerkzeuge mitprotokollieren; eine unerfüllte Quellenprüfung nicht als bestanden werten.

Die erste Nachricht nennt ausschließlich Anliegen und Fallmaterial. Die Vertragsphase, der Erwerbszweck und der konkrete Zweck des Termins werden erst mit Nachricht zwei geklärt. Die zweite Nachricht enthält einen nicht angenommenen Änderungsvorschlag, keine neue vereinbarte Vertragsfassung. Das Register und die Erwartungen bleiben beim ausführenden Prüfer; sie gehören nicht in den Kontext des Blindagenten.

## Auswertung und technische Prüfung

Bereits Antwort eins muss aus dem vorhandenen Wortlaut arbeiten, gezielt nach Status und Terminzweck fragen und Gutachten, Mandantenschreiben sowie externen Entwurf mit ihren Grenzen tatsächlich liefern. Die Fragebegründung, die einschlägige aktuelle Rechtsprechung und deren Anwendung sind am Inhalt zu bewerten. Eine Wort-, Überschriften- oder Quellenanzahl ersetzt diese Prüfung nicht.

Für Antwort zwei die Übernahme der neuen Tatsachen, den Fortbestand des unveränderten § 9 und die Behandlung von § 8 als noch nicht vereinbarte Änderung gesondert prüfen. Aktualisierte Produkte müssen zum selben Tatsachenstand passen; bloße Angebote oder eine erneute Aufnahme genügen nicht.

Tatsächliche Läufe mit Modell, Prompt-/Pluginfassung, Werkzeugen, Eingabeprüfsummen, Rohantworten und Bewertung unter einem eigenen Verzeichnis in `tests/runs/` dokumentieren. `actual_runs` ist bei Anlage der Probe leer. Ergebnisse und unbekannte Laufmetadaten dürfen nicht vorweggenommen werden.

```sh
python3 scripts/test_workflow_dialogue.py ImmediateDialogueFixtureTests
```

Die statischen Tests kontrollieren Schema, Pfade, getrennte Eingaben, Reihenfolge und den Ausschluss von Evaluatorunterlagen. Mutationen prüfen insbesondere eine vorgezogene zweite Nachricht und geleakte Erwartungen. Sie führen keinen Blindlauf aus und bewerten keine rechtliche Richtigkeit.
