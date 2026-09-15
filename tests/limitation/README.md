# Gezielte Verjährungsfälle

Diese kurzen Fälle isolieren das gemeldete Übersehen einer Zweijahresklausel und prüfen zugleich auf Überkorrektur. Sie ersetzen weder die vollständigen DOCX-Testakten noch eine anwaltliche Prüfung. Die bewusst problematischen Vertragsklauseln bleiben unverändert als Prüfeingaben erhalten.

## Blind ausführen

Für jeden Fall und jede Promptfassung einen frischen Chat verwenden. Nur den Werkstatt- oder Mini-Prompt und **genau eine** Datei aus `inputs/` übergeben. Diese README, `erwartungen.json`, vorherige Antworten und Hinweise auf die erwartete Bewertung nicht mitgeben. Keine zusätzlichen Warnungen wie „achte auf Verjährung“ ergänzen; die Eingabedatei enthält bereits den vollständigen Arbeitsauftrag. Die Dateinamen tragen keine Risikowertung.

Modell/Version, Datum, Promptversion und SHA-256, Eingabedatei und SHA-256 sowie Recherchezugang festhalten. Antwort unverändert sichern. Erst danach anhand von `erwartungen.json` auswerten. Für jeden Punkt 0 = falsch/fehlt, 1 = nur teilweise, 2 = mit tragfähiger Begründung und geeigneter Folgerung; Fehlalarme und kritische Fehler separat notieren. Nicht bloß nach Normnummern in der Antwort suchen. Ein System muss den konkreten Regelungsmechanismus erklären; Normnennung allein genügt nicht.

## Abdeckung und Grenzen

| Fälle | Auswertungsziel |
| --- | --- |
| V01–V02 | kurze Frist für Bauwerksmängel; Etikett „individuell“, VOB/B-Verweis und technische Bauteile bieten keine automatische Ausnahme |
| V03 | nominell fünf Jahre mit vorverlegtem Beginn erkennen |
| V04 | gesonderte Ausschlussfrist für nicht offensichtliche Mängel erkennen |
| V05 | korrekte Fünfjahresregelung ohne erfundene Verkürzung bewerten |
| V06 | gesetzliche Zweijahresfrist eines nicht bauwerksbezogenen Werks nicht verbieten |
| V07 | nachgewiesenes echtes Aushandeln von einem bloßen Etikett unterscheiden; kein universelles Verbot aus § 634a oder § 650o ableiten |

V01–V05 sind Ausschnittsprüfungen von Entwürfen, keine vollständigen Vertragsprüfungen. V06 ist bewusst ein werkvertraglicher Abgrenzungsfall außerhalb eines Bauträgervertrags. V07 isoliert die Rechtsfrage einer als erwiesen vorgegebenen Individualvereinbarung. Der Prüfer darf tatsächliches Aushandeln im normalen Vertragsfall weiterhin nicht ohne Beleg annehmen. Eine richtige V07-Antwort ist keine allgemeine Empfehlung zur Fristverkürzung und keine Freigabe des gesamten Vertrags.

Rechtsgrundlagen: [§ 634a BGB](https://www.gesetze-im-internet.de/bgb/__634a.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html), [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 306 BGB](https://www.gesetze-im-internet.de/bgb/__306.html), [§ 650o BGB](https://www.gesetze-im-internet.de/bgb/__650o.html), [§ 202 BGB](https://www.gesetze-im-internet.de/bgb/__202.html), [§ 639 BGB](https://www.gesetze-im-internet.de/bgb/__639.html). Normkontrolle: 9. September 2026; für spätere Einsätze Rechtsstand erneut prüfen.

## Automatische Konsistenzkontrolle

```sh
python3 scripts/test_limitation_controls.py
```

Die automatischen Tests sichern explizite Prüfinhalte beider Prompts, ihre Download-/Plugin-Spiegel und die Trennung von Eingaben und Erwartungen. Sie prüfen **keine Modellantworten** und sind kein Nachweis besserer KI-Leistung. Tatsächliche Blindläufe gehören mit Rohantworten und getrennten Auswertungen in `tests/runs/`.
