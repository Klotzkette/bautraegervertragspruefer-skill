# MW02 · Zahlung nach nachgereichter Ergänzungsurkunde

Die Käuferin der Marewald-Wohnung C-2.14 lässt den dritten Zahlungsabruf beurteilen. Die erste Runde verwendet die vollständigen bestehenden Markdown-Fassungen von Mustervertrag samt Baubeschreibung, Bautenstandsbericht und Zahlungsanforderung. Eine Mandatsnotiz setzt den Prüfzeitpunkt. Eingereicht wird jeweils nur, was der Käuferin in dieser Runde vorliegt.

Der Fall wurde gewählt, weil die bestehende technische Nachlieferung den zunächst zweifelhaften Bautenstand bestätigt. Bei Wiedervorlage kommt zugleich eine wirksame Ergänzungsurkunde hinzu. Die Fachprüfung muss technische Leistung, rechtliche Fälligkeit und eine im Schriftverkehr erwähnte Nachbarwohnung gesondert behandeln. In beiden Runden sind ein Gutachten, ein Mandantinnenbrief und ein ausformulierter Brief an die Verkäuferin bestellt.

## Blindlauf wiederholen

Die [Fallkonfiguration](dialog.json) listet die Eingangspost in Zustellreihenfolge. Eine angemeldete Codex CLI mit Zugriff auf das angegebene Modell genügt. Der Ausgabeordner muss neu sein. Für den veröffentlichten Ausgangsstand lässt sich der Skilltext ausdrücklich von dessen Commit laden.

```sh
python3 tests/workflow/aktenfortschreibung/blindlauf.py --skill-revision de15974 /tmp/mw02-490-neu
python3 tests/workflow/aktenfortschreibung/blindlauf.py /tmp/mw02-aktueller-stand-neu
```

Das Skript liest den vollständigen Skilltext einmal und verwendet ihn für beide Runden. Jeder Modellaufruf läuft in einem leeren temporären Verzeichnis mit schreibgeschützter Sandbox und abgeschalteter Websuche. Der zweite Aufruf erhält die tatsächlich erzeugte erste Antwort und die erste Nutzeranfrage im Gesprächsverlauf. Erwartungsdateien, Prüfberichte und andere Fälle werden nicht übergeben. Der Lauf bricht ab, wenn die CLI einen Werkzeugaufruf oder keinen regulären Abschluss meldet. Die Rohantworten und SHA-256-Prüfsummen werden erst im gesonderten Ausgabeordner gespeichert.

Die [Bewertungskriterien](erwartungen.md) erst nach dem Lauf öffnen. Die [Ergebnisse vom 22. November 2026](../../runs/2026-11-22/mw02-auswertung.md) unterscheiden die geladenen Versionen und zeigen die Grenzen der Stichprobe.
