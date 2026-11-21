# Prüfbericht 4.9.0

Stand 21. November 2026.

## Vertragsart vor Sachprüfung

Elf erfundene Fälle beginnen mit derselben knappen Zahlungsanfrage. In jeder ersten Antwort fragte der Prüfer nach den für die Einordnung fehlenden Vertragspflichten. Erst in der zweiten Runde erhielt er die entscheidenden Klauseln. Beim zwölften Fall lag der vollständige Marewald-Entwurf bereits vor. Die 23 Antworten stammen aus Codex CLI mit gpt-6.2-astra. Erwartete Befunde waren dem Modell verborgen, ein Quellenabruf und eine Ausführung in Microsoft Word waren nicht Teil dieser Textproben. [Eingaben und Bewertungsmaßstäbe](workflow/vertragsmodelle/README.md) · [Wortlaut der Antworten, Auswertung und Prüfsummen](runs/2026-11-21/vertragsmodelle.json)

| Fall | Beobachtetes Ergebnis |
| --- | --- |
| Erbbaurecht | Der Prüfer berechnete für die erste Rate bei 300.000 Euro eine Obergrenze von 60.000 Euro und behandelte Sicherheit und Fälligkeit gesondert. |
| Bau auf eigenem Grund | Die Antwort zum Auftrag über das ganze Haus prüfte den Verbraucherbauvertrag. Beim einzelnen Dachgewerk ging sie von einem Bauvertrag aus. |
| Umbau, Bestand und Nachzügler | Die Antworten unterschieden Leistungen an einzelnen Bauteilen, einen reinen Bestandskauf und den späteren Erwerb mit eigener Herstellungspflicht. |
| Widersprüchliche Rechnung | Zwei Urkunden betrafen verschiedene Einheiten. Der Prüfer verlangte eine eindeutige Zuordnung und prüfte für jede Urkunde, ob eine eigene Frist aus der Notarmitteilung laufen konnte. |
| § 7 MaBV | Bei einem Bürgschaftsangebot prüfte die Antwort Deckungszweck und Fehlbetrag. Aus dem Baufortschritt leitete sie keine Freigabe ab. |
| Vollständiger Marewald-Vertrag | Der Prüfer ordnete die Wohnung C-2.14 anhand der Kauf-, Bau- und Zahlungsklauseln als WEG-Neubauerwerb ein. Er erkannte die freie Urkundennummer als Entwurfsmerkmal. Bewertet wurde die Vertragszuordnung. |

## Word-Fassungen und Auslieferung

Die Werkstatt enthält 255.892 Zeichen und ergibt 79 Seiten, der Mini 21.525 Zeichen und sieben Seiten. Der Export prüft beim Formatieren die Reihenfolge und den Inhalt aller Textknoten im Hauptdokument. Die Sichtprüfung umfasste alle 86 gerenderten Seiten. Tabellenköpfe auf Folgeseiten, Quellenzeilen und Seitenzahlen sind lesbar. [Layoutprüfung mit SHA-256 für Quelltexte und Word-Dateien](prompt-layout-4.9.0.json)

Die vollständige Repository-Prüfung war erfolgreich. Die 104 Einzeltests umfassen 16 Werkzeugtests, zehn Prüfungen der Vertragsartefakte, sechs zur Verjährung, 39 zu Dialogen und Ablauf, acht zur Portabilität und 25 zu Promptlayout und Quellenstruktur. Hinzu kommen die Abgleiche der Markdown-Spiegel, des Plugin-ZIP und von 33 veröffentlichten Beispieldateien. Der gesonderte Online-Lauf erreichte 70 Entscheidungs- und acht Gesetzgebungslinks. Die gezielte juristische Nachrecherche dokumentiert die Entscheidungen und ihre Anwendungsgrenzen gesondert. [Prüfskript](../scripts/validate_repo.sh) · [Quellenstand November](legal-sources-4.9.0.md)
