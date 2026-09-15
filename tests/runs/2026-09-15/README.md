# Dialogproben der Fassung 4.5.0

Am 15. September 2026 wurden drei getrennte Codex-Verläufe mit jeweils drei Nutzernachrichten und drei abgeschlossenen Antworten durchgeführt: W01 mit Mini, W01 mit Werkstatt und W03 mit dem Zahlungs-Plugin. Das sind **neun tatsächliche Antworten in drei Dialogen**, nicht neun unabhängige Chats und nicht fünf bestandene Szenarien.

## Durchführung und unveränderte Antworten

Für jeden Lauf wurde ein neuer Unteragent ohne übernommene Gesprächshistorie gestartet (`fork_turns: none`). Er erhielt den bezeichneten Prompt beziehungsweise Plugin-Einstieg und die vorgesehenen aktuellen Eingaben. Erwartungsschlüssel, Auswertungen und spätere Nutzernachrichten blieben während der Prüfung verborgen. Nachricht zwei wurde erst nach der abgeschlossenen ersten Antwort übergeben, Nachricht drei erst nach der zweiten. Innerhalb eines Dialogs blieb der Gesprächsstand erhalten; es wurden keine Musterantworten anstelle seiner eigenen Antworten eingesetzt.

Die drei Rohdateien enthalten die tatsächlich ausgegebenen Antworttexte, jeweils unter `Turn1`, `Turn2` und `Turn3`:

| Lauf | Anleitung und Eingabeabfolge | Rohantworten |
| --- | --- | --- |
| Mini, W01 | Mini-Prompt allein; ursprüngliche Rosenhof-Klauseln → Notariatsschreiben beauftragt → geänderte Klauselfassung | [Mini W01](mini-w01-raw.md) |
| Werkstatt, W01 | Werkstatt-Prompt; dieselbe nacheinander zugespielte W01-Abfolge | [Werkstatt W01](werkstatt-w01-raw.md) |
| Plugin, W03 | Einstieg `bautraeger-zahlungsrate-pruefen` mit seinen Ressourcen; Marewald-Zahlungsakte → ergänzte Tatsachen → Mandantennachricht beauftragt | [Plugin W03](plugin-w03-raw.md) |

Die genauen Eingabedateien stehen im [Dialogregister](../../workflow/dialoge.json), Durchführungsvorgaben im [Testprotokoll](../../workflow/README.md). Die gesonderten [Laufmetadaten](metadata.json) dokumentieren tatsächliche Versionen, Prüfsummen und Ausführungsgrenzen. System- und Entwickleranweisungen der Codex-Umgebung blieben wirksam; dies war kein allein durch einen frei kopierten Prompt gesteuerter Test bei einem fremden KI-Anbieter.

Die konkrete Modellkennung und sekundengenaue Übergabezeitpunkte wurden nicht verlässlich erfasst und werden nicht nachträglich ergänzt. Protokolliert ist die tatsächliche Reihenfolge der Übergaben. Im Plugin-Lauf half ein weiterer Unteragent bei der Prüfung von Primärrecht, ohne spätere Falldaten oder Erwartungen zu erhalten.

Der Werkstatt-Lauf verwendete den protokollierten Promptstand mit SHA-256-Präfix `8fb8f029`; dieselbe Langfassung lag zu Beginn der Zahlungsprüfung als Plugin-Referenz vor. Anschließend wurde für die endgültige Fassung nur eine redundante abschließende Startanweisung entfernt. Die Prüfsummen sind deshalb nicht identisch. Für die bytegenau endgültige Langfassung wird hier kein erneuter vollständiger Modelllauf behauptet; die geänderte Schlusszeile betraf nicht den bereits getesteten Arbeitsablauf oder die fachlichen Regeln.

## Nachträgliche Auswertung der neun Antworten

Die folgende Bewertung entstand erst nach vollständiger Lektüre der Rohantworten anhand der getrennten [Erwartungen](../../workflow/erwartungen.json). Die Antworten wurden nicht nachträglich verbessert. Bewertet werden die bezeichneten Beobachtungen und das tatsächlich gelieferte Arbeitsergebnis, nicht bloße Schlüsselwörter oder eine Selbsteinschätzung des geprüften Modells.

| Antwort | Konkrete Beobachtung | Bewertung im vorgegebenen Umfang |
| --- | --- | --- |
| Mini W01, 1 | Beurteilt die Zweijahresklausel ausdrücklich als unwirksam, nennt fünf Jahre ab maßgeblicher Abnahme und verwirft das bloße Individual-Etikett. Liefert Ersatz für § 9.4 und Streichung des zweiten Satzes von § 15.2. | Beide geforderten Ergebnisse umgesetzt; keine bloße Themenliste. |
| Mini W01, 2 | Liefert unmittelbar das angeforderte Notariatsschreiben mit beiden Änderungen und nutzbaren Formulierungen. | Beide geforderten Ergebnisse umgesetzt; keine erneute Erlaubnisfrage, kein zusätzliches Gutachten und kein behaupteter Versand. |
| Mini W01, 3 | Erkennt § 9.4 als bereinigt, erklärt den neuen Anspruchsausschluss in § 15.2 und liefert ein aktualisiertes Schreiben mit dessen Beseitigung. | Alle drei geforderten Ergebnisse umgesetzt; die entfallene Individual-Erklärung wird nicht als weiterhin geltender Text behandelt. |
| Werkstatt W01, 1 | Begründet die Unwirksamkeit der Zweijahresfrist, die gesetzliche Ersatzregel und die fehlende Bedeutung der Individualitätsbestätigung; formuliert beide Änderungen aus. | Beide geforderten Ergebnisse umgesetzt; kein bloßer Verhandlungswunsch anstelle des Rechtsbefunds. |
| Werkstatt W01, 2 | Verfasst das beauftragte Schreiben; der verbleibende Haftungsausnahmesatz soll beim Austausch der Verjährungsregel erhalten bleiben. | Beide geforderten Ergebnisse umgesetzt; kein Wiederbeginn der Erstprüfung. |
| Werkstatt W01, 3 | Beschränkt den verbleibenden Änderungsbedarf auf die neue Ausschlussfrist und begründet, weshalb fünf Jahre in § 9.4 diese nicht unschädlich machen. Das Schreiben wird entsprechend angepasst. | Alle drei geforderten Ergebnisse umgesetzt; keine Freigabe des gesamten Rücklaufs allein aufgrund der neuen Fünfjahresregel. |
| Plugin W03, 1 | Rechnet 18,9 % von 674.000 EUR als 127.386 EUR nach. Unterscheidet offene allgemeine Voraussetzungen und Garantie von der konkreten Heizkreisverteiler-Unklarheit. Fordert drei sachbezogene Gruppen von Belegen mit Entscheidungsbezug an. | Beide geforderten Ergebnisse umgesetzt; die spätere Ergänzung wird nicht vorweggenommen und die bloße Nachweislücke nicht als bewiesene Nichtfälligkeit ausgegeben. |
| Plugin W03, 2 | Ändert nach den neuen Angaben die Entscheidung auf 127.386 EUR zahlbar. Die fortbestehende Garantie über 33.700 EUR wird nicht nochmals abgezogen. Kennzeichnet die Angaben als vorgegebenen Sachverhalt und die Originalprüfung als fremde Tätigkeit. | Alle drei geforderten Ergebnisse umgesetzt; keine erneute Anforderung derselben bereits geklärten Angaben. Unabhängige Vertragsfragen werden getrennt behandelt. |
| Plugin W03, 3 | Liefert eine kurze Mandantennachricht zur konkret bezeichneten Rechnung, dem Betrag und der Zahlungsgrundlage. Hinweise auf Abnahme und spätere Mängelrechte bleiben knapp. | Beide geforderten Ergebnisse umgesetzt; kein bloßes Angebot, die Nachricht erst später anzufertigen. |

In diesen Antworten wurde keiner der für W01 beziehungsweise W03 ausdrücklich benannten kritischen Fehler beobachtet. Das ist eine begrenzte qualitative Bewertung und keine Bestätigung der Fehlerfreiheit sämtlicher juristischer oder technischer Nebenbemerkungen.

## Sprache, Rückfragen und verbleibende Grenzen

Die Schreiben bestehen aus verwendbaren vollständigen Sätzen. Es fehlen die zuvor störenden Ampeln, leeren Zahlungskarten, sichtbaren Verwaltungskennungen und pauschalen Schlussfragen wie „Soll ich weiter?“. Bei W01 ist die erste Anfrage ausdrücklich auf zwei Klauseln begrenzt und ihr Sachverhalt vollständig. Dass dort keine künstliche Rückfrage gestellt wird, ist sachgerecht. Der nächste beauftragte Schritt wird anschließend ohne neue Bestätigungsrunde tatsächlich ausgeführt.

Die erste Zahlungsantwort ist weiterhin vergleichsweise lang: Sie enthält den gesamten Ratenplan, Einzelberechnung, mehrere Sicherheitsalternativen und drei ausführliche Nachweisgruppen. Auch die zweite Antwort wiederholt Teile der Rechnung. Die dort zusätzlich behandelten unabhängigen Vertragsfragen waren allerdings ausdrücklich angefordert. Der abschließende Mandantenbrief ist deutlich kürzer. Die Probe belegt deshalb gelungene Fortsetzung und ein knappes Folgeschreiben, aber nicht, dass jede umfangreiche Erstprüfung bereits optimal gestrafft ist.

Nicht durchgeführt wurden W02, W04 und W05, also insbesondere die weitere Fassungsprüfung einer vollständigen Akte, der negative Zahlungsrücklauf und der Stop-/Ohne-Rückfragen-Verlauf. Diese Fälle bleiben vorbereitet. Ebenfalls nicht durchgeführt: wiederholte Läufe zur Streuung, Vergleich mehrerer KI-Anbieter, unabhängiges anwaltliches Audit oder ein Dialog mit tatsächlicher Word-Dateibearbeitung. Alle hier geprüften Vertragsunterlagen waren Markdown-Texte; die Rohantworten behaupten keine Word- oder Bildprüfung. Gesonderte Word-Artefaktprüfungen sind kein Ersatz für einen solchen Dialogtest.

Die Ergebnisse belegen das beobachtete Verhalten dieser drei Codex-Läufe. Die Prompts können fehlerfreie Prüfung, identische Sprache oder einen vollständig gelungenen Arbeitsablauf in anderen KIs nicht garantieren. Statische Repository-Tests und diese tatsächlichen Dialogproben bleiben getrennte Nachweise.
