# Gezielte Dialogproben der Fassung 4.8.0

Ausgeführt am 8. Oktober 2026. Drei frische, voneinander getrennte Agentenkontexte; jeweils zwei tatsächliche Nutzereingaben nacheinander. Die Folgeeingabe wurde durch den steuernden Hauptagenten erst nach der ersten finalen Antwort freigegeben. Die Prüfer erhielten weder Erwartungsmatrix noch andere Fallantworten. Archiviert sind die sechs unveränderten finalen Antworten, nicht sämtliche Zwischenmeldungen oder Toolausgaben.

Die Läufe prüfen gezieltes Textverhalten, nicht einen vollständigen Bauträgervertrag oder die Integration in Microsoft Word. Eine konkrete technische Modellkennung war nicht verlässlich verfügbar und steht deshalb in den Metadaten auf „unbekannt“. Es werden keine Anbieter-Vergleichsquoten behauptet.

## Eingaben und tatsächliche Antworten

| Einstieg und Fall | Erste Antwort | Fortsetzung | Metadaten | Getrennte Auswertung |
| --- | --- | --- | --- | --- |
| Vollständiger Werkstatt-Prompt, ID01: Erstverwalterabnahme; anschließend Klärung des bereits unterschriebenen Hauptvertrags und noch unangenommener Änderungsvorschlag | [Turn 1](full-id01-turn1.md) | [Turn 2](full-id01-turn2.md) | [Lektüre und Abrufe](metadata-full-id01.json) | [Bewertung](evaluation-full-id01.md) |
| Eigenständiger Mini-Prompt, WS01: Zweijahresklausel; anschließend fünf Jahre mit weiter vorgezogenem Beginn | [Turn 1](mini-ws01-turn1.md) | [Turn 2](mini-ws01-turn2.md) | [Lektüre und Abrufe](metadata-mini-ws01.json) | [Bewertung](evaluation-mini-ws01.md) |
| Word-Skill-Einstieg mit erlaubten lokalen Verweisen, derselbe WS01-Fall | [Turn 1](word-ws01-turn1.md) | [Turn 2](word-ws01-turn2.md) | [Lektüre und Abrufe](metadata-word-ws01.json) | [Bewertung](evaluation-word-ws01.md) |

Getrennte Eingaben und Sollkriterien: [ID01](../../workflow/immediate-dialogue/README.md), [WS01](../../workflow/word-selection/README.md). Der ID01-Fall behält seinen Stichtag 28. September 2026; das Ausführungsdatum wurde nicht als neues Ereignisdatum in die Akte übertragen.

## Beobachtetes Verhalten

- Alle drei ersten Antworten enthalten einen konkreten Klauselbefund, ein Schreiben an die Erwerberin, ein ausgearbeitetes Gutachten im tatsächlich lesbaren Umfang und geeignete externe Entwürfe. Kein Zusatzauftrag und kein Dateiexport werden vorausgesetzt.
- Alle drei zweiten Antworten aktualisieren diese Produkte anhand der neuen Angaben. Im Werkstattlauf entfällt die Variante eines erstmaligen Hauptvertragsabschlusses; die bisher nicht angenommene Streichung von § 8 wird von der weiterhin problematischen Regelung des § 9 getrennt.
- Mini und Word-Einstieg beanstanden die ursprüngliche Zweijahresfrist und ausdrücklich auch den unveränderten Beginn bei Übergabe im Fünfjahresvorschlag. § 309 Nr. 8 Buchst. b Doppelbuchst. ff BGB wird jeweils ausdrücklich auf die Verbraucher-AGB angewandt. Aushandlungsbestätigung und gesetzliche Ersatzregel werden gesondert behandelt.
- Die Antworten stellen zuerst drei, danach zwei selbständige direkte Rückfragen. Der Word-Lauf erinnert zusätzlich an den später benötigten Vertragsauszug und bleibt auch bei dessen Mitzählung bei höchstens drei Anliegen. Bekannte Eigennutzung und geklärte Vertragsphase werden nicht nochmals abgefragt. Anforderungen an die Schreibenempfänger sind von Rückfragen an die Nutzerin zu unterscheiden.
- Die Word-Auswahl bleibt als Teilprüfung bezeichnet; keine Gesamturkunde, Kommentare, Anlagen oder visuelle Word-Prüfung werden vorgetäuscht. Die Originaldatei wird nicht geändert. Die Schreibentwürfe wurden nicht versandt.

Die Rohantworten wurden zusätzlich von anderen Agenten anhand der getrennten Kriterien ausgewertet. Deren konkrete Befunde und Grenzen stehen in den verlinkten Berichten. Eine Prozentnote wäre für drei enge Proben nicht aussagekräftig.

Ein kleiner sprachlicher Mangel bleibt im Word-Lauf sichtbar: Der Einstieg von Turn 2 könnte isoliert wie eine wirksame verkürzte Frist gelesen werden. Das folgende Gutachten erklärt die Unwirksamkeit und gesetzliche Ersatzregel richtig. Die Auswertung benennt die präzisere Formulierung; die tatsächliche Antwort wurde nicht nachträglich geglättet.

## Quellen- und Kontextgrenzen

Der Werkstattprüfer las die gesamte Langfassung; gekürzte Toolausgaben wurden abschnittsweise nachgelesen. Er las die tragenden amtlichen Originale VII ZR 308/12, VII ZR 49/15 und VII ZR 68/24 nach zunächst gescheiterten Webabrufen über reguläre PDF-Streams. Die aktuelle Fremdabnahmerechtsprechung wird mit ihrer Altrechtsgrenze angewandt. Im zweiten Turn kamen die Normen zu Abnahme und Grundstücksform hinzu; bereits geprüfte Quellen wurden weiterverwendet.

Der Mini wurde vollständig gelesen. Im Word-Skill-Lauf wurden beide Einstiegsskills vollständig gelesen; die lange Werkstattreferenz wurde nicht vollständig angezeigt. Deren einschlägige Abschnitte wurden gezielt nachgelesen. Das ist ausdrücklich kein Nachweis, dass der Word-Einstieg jede Rechtsprechungsbesprechung der Langfassung verarbeitet hätte. Beide WS01-Läufe verwendeten den tatsächlich gelesenen DNotI-Entscheidungsabdruck VII ZR 248/13 nach gescheiterten amtlichen Abrufen; in Turn 2 wurden diese Quellen wiederverwendet. Die dokumentierten Aktualitätssuchen sind begrenzt, keine lückenlose Erfassung aller neueren Urteile.

Die [Hashliste](artifacts.sha256) bindet die sechs gespeicherten Antworten und drei Metadatendateien an den hier ausgewerteten Stand. Die Metadaten enthalten zusätzlich Prompt-/Eingabeprüfsummen und tatsächliche Lesegrenzen. Hashes beweisen nicht für sich die damalige Kontextzuführung oder jeden Quellenabruf. Die separaten Auswerter können das ursprüngliche Toolgeschehen aus diesen Artefakten allein nicht forensisch rekonstruieren; die Ausführungsbeschreibung beruht zusätzlich auf der Steuerung dieses Arbeitslaufs.

## Was damit nicht nachgewiesen ist

Keine echte Word-Erweiterung, keine neue vollständige DOCX-Vertragsprüfung, kein Zahlungsfall, keine Vollständigkeit aller juristischen Befunde und keine identische Leistung anderer KI-Modelle. Die DOCX-Exportprüfung des Promptdokuments ist ein eigener Nachweis in der [QA 4.8.0](../../QA-4.8.0.md). Die Fehler der früheren [DP01-Gesamtvertragsproben](../2026-09-25/README.md) werden durch diese engeren Fälle nicht für erledigt erklärt. Die erzeugten anwaltlichen Texte bleiben fallbezogen fachlich zu prüfen.
