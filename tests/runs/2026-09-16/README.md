# Ergänzende Dialogproben und unterbrochener Arbeitsstand 4.5.1

Am 16. September wurden drei frische Dialoge der veröffentlichten Fassung **4.5.0 vollständig abgeschlossen**: Mini W05, Zahlungs-Plugin W04 und Werkstatt W02. Das sind neun abgeschlossene Antworten. Anschließend wurden zwei frische W04-Zahlungsdialoge mit dem Arbeitsstand 4.5.1 begonnen. Diese wurden durch ein Nutzungslimit unterbrochen und werden **nicht als vollständig bestandene Läufe** ausgewiesen. 4.5.1 ist noch nicht veröffentlicht.

## Durchführung und Rohdaten

Jeder Lauf begann in einem neuen Codex-Unteragenten ohne geerbte Gesprächshistorie (`fork_turns: none`). Übergeben wurden nur die jeweilige Anleitung und die aktuellen Eingaben aus dem [Dialogregister](../../workflow/dialoge.json), keine Erwartungen und keine späteren Nutzernachrichten. Die zweite Nachricht wurde erst nach der ersten abgeschlossenen Antwort übergeben, die dritte erst nach der zweiten. Amtliche Webquellen waren erlaubt; Versand oder andere Vertretungshandlungen nicht. Die Word-Verträge waren nicht Teil dieser Dialoge: Geprüft wurden ausdrücklich Markdown-Texte.

| Lauf | Tatsächlich abgeschlossener Verlauf | Unverändertes Protokoll |
| --- | --- | --- |
| Mini 4.5.0, W05 | Alle drei Antworten: begrenzte Verjährungsfrage, Stop, eng begrenzte Wiederaufnahme | [Rohantworten](mini-w05-4.5.0-raw.md) |
| Zahlungs-Plugin 4.5.0, W04 | Alle drei Antworten: Zahlungsprüfung, Gegenfeststellung, Käuferbrief | [Rohantworten](plugin-w04-4.5.0-raw.md) |
| Werkstatt 4.5.0, W02 | Alle drei Antworten: Entwurfsprüfung, Notariatsschreiben, geänderte Abnahmeklausel | [Rohantworten](werkstatt-w02-4.5.0-raw.md) |
| Mini Arbeitsstand 4.5.1, W04 | Antwort 1 und 2 abgeschlossen; Text für Antwort 3 bereits archiviert, aber der Agentenlauf endete vor einer abschließenden Ausgabe mit Nutzungslimit | [Unvollständiger Lauf](mini-w04-4.5.1-partial-raw.md) |
| Zahlungs-Plugin Arbeitsstand 4.5.1, W04 | Antwort 1 abgeschlossen; Text für Antwort 2 bereits archiviert, aber keine abgeschlossene Ausgabe; Nachricht 3 wurde nicht mehr übergeben | [Unvollständiger Lauf](plugin-w04-4.5.1-partial-raw.md) |

Alle fünf Protokolle wurden bytegenau mit den während der Bearbeitung gespeicherten Originalen verglichen. Die beiden nicht abschließend ausgegebenen Texte werden weder unterschlagen noch als erfolgreich abgeschlossene Agentenantworten gezählt. System-/Entwickleranweisungen der Codex-Umgebung blieben wirksam. Modellkennung und sekundengenaue Übergabezeiten wurden nicht verlässlich erfasst und bleiben in den [Metadaten](metadata.json) `null`.

## Beobachtungen nach Lektüre der Antworten

Die folgende qualitative Auswertung stammt vom Hauptagenten, nicht von einem unabhängigen anwaltlichen Gutachter. Ein zusätzlich begonnener unabhängiger Bewertungsdurchgang scheiterte ebenfalls am Nutzungslimit. Die Rohantworten wurden nicht nachträglich korrigiert.

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

## Warum der Arbeitsstand geändert wurde

Die erste Plugin-Zahlungsantwort der Fassung 4.5.0 gab wieder den gesamten Sieben-Raten-Plan aus; die Folgeantwort wiederholte Begründungen zusätzlich zum Brief. Die vollständige interne Prüfung ist erforderlich, die vollständige Wiedergabe bei jedem Einzelabruf nicht. Werkstatt, Mini und Zahlungs-Skill trennen dies jetzt ausdrücklich und verlagern die tragende Begründung bei einem beauftragten Schreiben in dieses Schreiben.

Die vorliegenden Antworten des Arbeitsstands belegen noch keine durchgehend knappe Sprache: Der Mini wiederholt vor dem Brief weiterhin Teile der Begründung. Sein bereits gespeicherter dritter Text ist ein deutlich konzentrierterer Käuferbrief. Im Plugin wurde der gespeicherte zweite Text unmittelbar nach einer kurzen Ergebnisänderung als Brief ausgearbeitet. Wegen des Abbruchs bleiben dies begrenzte Beobachtungen, kein bestandener vollständiger Vergleichslauf und keine statistische Wirksamkeitsmessung.

Nach Beginn der 4.5.1-Läufe wurde in der Werkstatt-Referenz zusätzlich der widersprechende Satz „Für jede vertragliche Rate ausgeben“ zu „Für jede vertragliche Rate intern prüfen“ geändert. Die getestete Referenz ist deshalb nicht byteidentisch mit dem endgültigen Arbeitsstand. Mini und Zahlungs-Einstiegsdatei blieben nach Testbeginn unverändert. Die jeweiligen Prüfsummen sind dokumentiert.

## Vor dem Release offen

Der lokale Endstand besteht die vollständige Repository-Validierung einschließlich 66 Unit-/Regressionstests, Akten-, Quellenstruktur-, Navigations- und Spiegelprüfungen. Plugin-Manifest und alle drei Skill-Einstiege bestehen ihre gesonderten Strukturvalidatoren. Die [Word-Layoutprüfung](../../prompt-layout-4.5.1.json) bindet die tatsächlich geprüften 38 beziehungsweise vier Seiten an die endgültigen Datei- und Quellprüfsummen. Dies sind technische Nachweise, keine zusätzlichen Modellläufe.

1. Die beiden Zahlungsdialoge sauber abschließen bzw. mit dem endgültigen Arbeitsstand in neuen getrennten Chats wiederholen; keine bereits bekannten zukünftigen Eingaben in einen frischen ersten Schritt übernehmen.
2. Vollständige Antworten nach dem getrennten Erwartungsschlüssel bewerten, insbesondere die Kürze und Wiederholungen vor beauftragten Schreiben.
3. Erst danach Release-Statushinweise aktualisieren, PR/CI prüfen, nach Main übernehmen und 4.5.1 veröffentlichen.

Die gesonderte Word-Layoutprüfung und die statischen Repository-Tests ersetzen diese offenen Dialogtests nicht. Keine Fremdmodell-Vergleichsläufe, Wiederholungsmessungen oder tatsächlichen Word-Bearbeitungsdialoge durchgeführt.
