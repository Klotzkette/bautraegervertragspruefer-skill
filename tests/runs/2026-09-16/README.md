# Ergänzende Dialogproben der Fassungen 4.5.0 und 4.5.1

Am 16. September 2026 wurden **fünf Dialoge mit insgesamt 15 tatsächlichen Antworten abgeschlossen**: Mini W05, Zahlungs-Plugin W04 und Werkstatt W02 mit 4.5.0 sowie Mini und Zahlungs-Plugin W04 mit 4.5.1. Die beiden neueren Läufe wurden durch ein Nutzungslimit unterbrochen und anschließend **im selben Agentenkontext** fortgesetzt. Das war keine Wiederholungsmessung. Die Unterbrechung bleibt in den Metadaten und unveränderten Zwischenständen nachvollziehbar.

## Durchführung und Rohdaten

Jeder Lauf begann in einem neuen Codex-Unteragenten ohne geerbte Gesprächshistorie (`fork_turns: none`). Übergeben wurden die jeweilige Anleitung und nur die aktuellen Eingaben aus dem [Dialogregister](../../workflow/dialoge.json), keine Erwartungen oder späteren Nachrichten. Jede folgende Nachricht kam erst nach der abgeschlossenen vorherigen Antwort. Amtliche Webquellen waren erlaubt; Versand oder andere Vertretungshandlungen nicht. Die Vertragsakten waren ausdrücklich Markdown-Texte, keine Word-Dateien.

| Lauf | Abgeschlossener Verlauf | Unverändertes Protokoll |
| --- | --- | --- |
| Mini 4.5.0, W05 | Verjährungsfrage → Stop → eng begrenzte Wiederaufnahme | [Rohantworten](mini-w05-4.5.0-raw.md) |
| Zahlungs-Plugin 4.5.0, W04 | Zahlungsprüfung → Gegenfeststellung → Käuferbrief | [Rohantworten](plugin-w04-4.5.0-raw.md) |
| Werkstatt 4.5.0, W02 | Entwurfsprüfung → Notariatsschreiben → geänderte Abnahmeklausel | [Rohantworten](werkstatt-w02-4.5.0-raw.md) |
| Mini 4.5.1, W04 | Zahlungsprüfung → Gegenfeststellung → Käuferbrief | [Rohantworten](mini-w04-4.5.1-raw.md) |
| Zahlungs-Plugin 4.5.1, W04 | Zahlungsprüfung → Gegenfeststellung → Käuferbrief | [Rohantworten](plugin-w04-4.5.1-raw.md) |

Mini-Antwort 3 und Plugin-Antwort 2 waren vor dem Abbruch bereits gespeichert. Bei Wiederaufnahme gaben dieselben Agenten diese Texte unverändert als abschließende Antwort aus. Erst danach erhielt das Plugin Nachricht 3 und lieferte seinen abschließenden Käuferbrief. Keine korrigierte Musterantwort wurde anstelle der eigenen bisherigen Antwort eingesetzt. Die Zwischenstände bleiben erhalten: [Mini vor Wiederaufnahme](mini-w04-4.5.1-partial-raw.md), [Plugin vor Wiederaufnahme](plugin-w04-4.5.1-partial-raw.md).

Alle endgültigen Rohdateien sind bytegleich mit den während der Bearbeitung gespeicherten Originalen. System-/Entwickleranweisungen der Codex-Umgebung blieben wirksam. Modellkennung und sekundengenaue Übergabezeiten wurden nicht verlässlich erfasst und bleiben in den [Metadaten](metadata.json) `null`. Ein unabhängiger Agent hat die vollständigen Texte nachträglich anhand der getrennten Erwartungen und Eingaben bewertet; kein unabhängiges anwaltliches Audit und keine Garantie juristischer Vollständigkeit.

## Bewertung der abgeschlossenen Ausgangsläufe

| Abgeschlossener Lauf / Antwort | Beobachtung anhand der getrennten Erwartungen |
| --- | --- |
| W05 Mini, 1 | Zweijahres-AGB als unwirksam beurteilt, fünfjährige Bauwerksfrist zugeordnet. Kein Abnahmedatum oder Fristende erfunden; fehlender Abnahmenachweis benannt. Keine unerwünschte Frage oder Briefausarbeitung. |
| W05 Mini, 2 | Ausschließlich kurze Stop-Bestätigung, keine Weiterarbeit. |
| W05 Mini, 3 | Ein Satz zum fehlenden datierten Abnahmenachweis; keine Wiederaufnahme der Gesamtprüfung. |
| W04 Plugin 4.5.0, 1 | 62.328 EUR aus 8,4 % von 742.000 EUR richtig berechnet. Positiver Bericht von noch nicht vorgelegten allgemeinen Nachweisen getrennt; den späteren Fassadenbefund nicht vorweggenommen. |
| W04 Plugin 4.5.0, 2 | Konkrete Gegenfeststellung zur offenen Fassade berücksichtigt. Nicht erreichten gebündelten Bautenstand von bloß offenen Nachweisen unterschieden und die gesamte Rate als nicht fällig beurteilt. Keine freie Teilzahlung oder unbelegte Kostenschätzung; tatsächliche Antwort formuliert. |
| W04 Plugin 4.5.0, 3 | Käuferbrief zur konkreten Rate und Teilzahlungsforderung geliefert; kein Rücktritt, kein neuer Ratenplan, kein behaupteter Versand. |
| W02 Werkstatt, 1 | Wesentlichkeitserfordernis der Abnahmefiktion beanstandet und von der Abnahmepflicht getrennt. Teilungserklärung und weitere entscheidende Anlagen ausdrücklich ungeprüft; auf den bekannten Termin bezogene Unterlagenanforderung und konkrete Frage zum Folgeprodukt. |
| W02 Werkstatt, 2 | Das beauftragte Notariatsschreiben trotz ausstehender Anlagen ausgearbeitet. Änderungen und externe Unterlagenanforderungen getrennt; weder Beurkundung noch Anlagenprüfung erfunden. |
| W02 Werkstatt, 3 | Korrigierte Fiktionsregel im begrenzten Umfang anerkannt, übrige Änderungen und Anlagen offen gehalten. Kurze Rückmeldung tatsächlich formuliert; keine neue Gesamtprüfung oder Gesamtfreigabe. |

In diesen neun abgeschlossenen Antworten wurde keiner der ausdrücklich benannten kritischen Szenariofehler beobachtet. Dies ist keine Bestätigung der Fehlerfreiheit sämtlicher juristischer Nebenbemerkungen. Zusammen mit dem [Vortag](../2026-09-15/README.md) sind nun alle fünf Szenarien wenigstens einmal vertreten, aber nicht alle Kombinationen aus Szenario und Prompt/Plugin und nicht sämtliche Szenarien mit der Fassung 4.5.1.

## Bewertung der beiden 4.5.1-Zahlungsdialoge

| Antwort | Beobachtung nach vollständiger Lektüre |
| --- | --- |
| Mini W04, 1 | Rechnet 62.328 EUR und den Zahlungsstand korrekt. Trennt den positiven Bautenstandsbericht von fehlenden weiteren Nachweisen, ohne den späteren Gegenbefund vorwegzunehmen. |
| Mini W04, 2 | Ändert die Bewertung nach dem konkreten 45-m²-Fassadenbefund auf Nichtfälligkeit der gebündelten Rate. Keine selbständig zahlbare 46.746-EUR-Teilrate; konkretes Schreiben tatsächlich geliefert. |
| Mini W04, 3 | Verfasst den verlangten Käuferbrief mit Rate, Betrag, offenen Fassadenleistungen und Zurückweisung des Teilzahlungsverlangens. Kein Rücktritt, keine neuen Zahlungsbedingungen, kein Versand. |
| Plugin W04, 1 | Richtige Rechnung und Zahlungsstand; bloß nicht vorgelegte Unterlagen werden nicht mit nachgewiesen fehlender Fälligkeit gleichgesetzt. |
| Plugin W04, 2 | Würdigt die neu vorgegebene Gegenfeststellung und erläutert den Entscheidungswechsel. Die tragende Berechnung und Begründung stehen unmittelbar im tatsächlich ausgearbeiteten Brief. |
| Plugin W04, 3 | Liefert den kurzen Käuferbrief im verlangten Umfang; keine Rücktrittserklärung, neue Ratenvereinbarung oder unbeauftragte Vertretung. |

Alle geforderten Fallkriterien wurden im engen Umfang der [Bewertungsrubrik](../../workflow/erwartungen.json) mit 2 (konkret und brauchbar) beurteilt; keine dort benannte verbotene oder kritische Kategorie wurde in den 15 Antworten beobachtet. Die [kriterienscharfe Bewertung](evaluation.json) ist von den Eingaben getrennt. Diese Bewertung umfasst nicht automatisch sämtliche juristischen Nebenbemerkungen und belegt keine vollständige Überführung aller Erstbefunde in jedes Folgeschreiben.

## Sprache und konkrete Grenzen

| Grobe Wortzahl je Antwort, einschließlich Markdown-/Tabellentokens | Nachricht 1 | Nachricht 2 | Nachricht 3 |
| --- | ---: | ---: | ---: |
| Mini W05, 4.5.0 | 304 | 11 | 22 |
| Werkstatt W02, 4.5.0 | 3.773 | 531 | 212 |
| Zahlungs-Plugin W04, 4.5.0 | 1.042 | 842 | 256 |
| Zahlungs-Plugin W04, 4.5.1 | 798 | 496 | 239 |
| Mini W04, 4.5.1 | 1.236 | 787 | 272 |

Gezählt wurden durch Leerraum getrennte Tokens (`\S+`) nach Entfernung der `# TurnN`-Archivüberschrift. Diese einfache Umfangszahl ist kein Qualitätsmaß.

Beim Zahlungs-Plugin entfällt in der zweiten 4.5.1-Antwort die lange zusätzliche Begründung vor dem Brief; ein kurzer Ergebnisabsatz leitet unmittelbar in das Schreiben über. Die notwendige Rechnung bleibt enthalten. Der Mini wiederholt in seiner zweiten Antwort dagegen weiterhin wesentliche Argumente vor und im Brief. Seine Erstprüfung enthält zusätzliche Ausführungen zu Verzug und Verjährung. **Eine durchgehend knappe Mini-Ausgabe ist damit nicht belegt.** Die abschließenden Käuferbriefe bleiben bei beiden Fassungen auf den Auftrag begrenzt.

Die Werkstatt-Erstprüfung der Ausgangsfassung ist lang und wiederholt teilweise den Unterlagenbedarf. Das Folgeschreiben übernimmt vier Änderungen; weitere Empfehlungen aus der Erstprüfung, etwa zur Quartiersduldung, zu Baubeschreibung V.2/V.3 und zur Nacherfüllungsfrist, fehlen ohne ausdrückliche Begründung der Auswahl. Der Ablauf erfüllt die engen W02-Kriterien, beweist aber **keine vollständige Übernahme sämtlicher Erstbefunde** in einen konsolidierten Änderungsauftrag.

Die vollständige interne Ratenprüfung bleibt erforderlich. Der Ausgabeumfang wurde deshalb in 4.5.1 ausdrücklich davon getrennt. Nach Beginn der 4.5.1-Läufe wurde außerdem in der Werkstatt-Referenz „Für jede vertragliche Rate ausgeben“ durch „Für jede vertragliche Rate intern prüfen“ ersetzt. Die in diesen Läufen geladene Referenz ist dadurch nicht byteidentisch mit der endgültigen Releasefassung; Mini und Zahlungs-Einstieg blieben unverändert. Es wird kein neuer vollständiger Modelllauf mit der nachträglich geänderten Referenz behauptet. Prüfsummen und Grenze sind dokumentiert.

## Technische Abschlussprüfung und Reichweite

Die vollständige lokale Repository-Validierung einschließlich 66 Unit-/Regressionstests, Akten-, Quellenstruktur-, Navigations- und Spiegelprüfungen ist bestanden. Plugin-Manifest und alle drei Skill-Einstiege bestehen ihre Strukturvalidatoren. Die [Word-Layoutprüfung](../../prompt-layout-4.5.1.json) bindet die tatsächlich geprüften 38 beziehungsweise vier Seiten an die endgültigen Datei- und Quellprüfsummen. Die sechs Word-Vertragsvorlagen sind unverändert und ihre Entwurfskennzeichnung, offene eigene Urkundennummer und XML-Inhalte erneut technisch kontrolliert.

Diese technischen Nachweise ersetzen keine Modellgespräche. Zusammen mit dem [Vortag](../2026-09-15/README.md) liegen acht abgeschlossene Dialoge mit 24 Antworten über zwei Versionen vor. Alle fünf Szenarien sind mindestens einmal vertreten, nicht aber sämtliche Szenario-/Prompt-Kombinationen oder alle Fälle mit 4.5.1. Keine Vergleichsläufe bei anderen KI-Anbietern, Wiederholungsmessungen oder tatsächlichen Word-Bearbeitungsdialoge durchgeführt. Die Ergebnisse sind begrenzte qualitative Beobachtungen, keine Garantie fehlerfreier Prüfung.
