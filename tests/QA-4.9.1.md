# Praxisprüfung 4.9.1 vom 22. November 2026

## Marewald – Nachtrag zur Zahlungsabrede

Die erste Runde verwendet den vollständigen Marewald-Mustervertrag mit Bautenstandsbericht und drittem Zahlungsabruf. In der zweiten Runde liegen der Käuferin technische Nachweise und eine notarielle Ergänzung der Zahlungsabrede vor. Bewertet wurden die Vertragszuordnung, die Rechnung und die Übereinstimmung zwischen Gutachten, Mandantinnenbrief und Antwort an den Bauträger. [Eingaben und Ablauf](workflow/aktenfortschreibung/README.md) · [Antworten und Auswertung](runs/2026-11-22/mw02-auswertung.md)

Der Nachtrag betrifft Wohnung C-2.14. In beiden getesteten Werkstattfassungen fiel der alte Abruf über 127.386 Euro weg. Der Rest von 283.080 Euro war erst nach den neu vereinbarten Voraussetzungen und der Zahlungsaufforderung fällig. Alle drei Texte gaben diese Zuordnung wieder. Die Gutachten umfassten bei erbetener kompakter Prüfung rund 1.390 bis 1.740 Wörter.

## Rückgewährbürgschaft und gesonderte Schlussvergütung

In einem weiteren fiktiven Vertrag verlangt der Bauträger 25.000 Euro zusätzlich zu 45.000 Euro bereits erhaltener Vorauszahlung. Der angebotene Bürgschaftstausch ließe nach der neuen Zahlung 45.000 Euro ungedeckt. Die spätere Restvergütung von 400.000 Euro hat eigene Fälligkeitsvoraussetzungen. Die zweite Runde prüft den Zugang einer korrigierten Bürgschaft über 70.000 Euro und die vereinbarte Frist von fünf Bankarbeitstagen. Die Antwort an den Bauträger wird in beiden Runden gesondert ausgewertet. [Modellantworten und Befunde](runs/2026-11-22/sicherungswechsel.json) · [§ 7 MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/__7.html)

Im ersten Durchlauf sagte der Entwurf die Zahlung schon für den Fall eines späteren Zugangs zu. Nach der Anpassung kündigte der Brief allein die Prüfung der noch ausstehenden Urkunde an. Nach wirksamer Übergabe nannte der zweite Brief die fälligen 25.000 Euro und das Fristende am 27. November. Erstlauf und Wiederholung sind im Protokoll dokumentiert.

## Prüfung an den Word-Dateien

Im veröffentlichten Plugin 4.9.0 schlug die Vorlagenkontrolle bei allen drei deutsch-englischen Vertragsdateien an. Das leere deutsche Urkundenfeld stand in Absatz 13, das englische in Absatz 15. Der Extraktor hatte nur zwölf XML-Absätze berücksichtigt. Jetzt zählt eine Tabellenzeile mit beiden Sprachspalten im Dokumentanfang einmal. Die sechs deutschen und zweisprachigen Originaldateien bestehen den Test. Ein gesonderter Test trägt eine Nummer in die englische Spalte ein und prüft den Warnhinweis. Er unterscheidet dabei die eigene Nummer von einer zitierten Vollmachtsurkunde. [Werkzeugtests](../scripts/test_plugin_tools.py)

Auch die zum Herunterladen bestimmten **Prompt-Dateien** wurden neu gerendert. Die Werkstatt umfasst 79 Seiten, der Mini sieben. Auf allen Seiten wurden Satzspiegel und Fußzeilen kontrolliert. Die geänderten Sicherungshinweise sind in der Werkstatt auf Seite 16 und im Mini auf Seite 4 lesbar. [Layoutprüfung und Prüfsummen](prompt-layout-4.9.1.json)
