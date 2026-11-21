# Vertragsmodell im Dialog prüfen

Die elf fiktiven Fälle beginnen mit derselben Zahlungsanfrage zu einem „Bauträgerprojekt“. Für die erste Antwort ist nur [offener-einstieg.md](inputs/offener-einstieg.md) sichtbar. Im zweiten Schritt erhält der Prüfer den Vertragsinhalt des jeweiligen Falls. Die vorherige eigene Antwort bleibt im Gespräch. Das [Fallregister](dialoge.json) legt für jeden Dialog den Einstieg und die Eingabereihenfolge fest. Die [Bewertungskriterien](erwartungen.json) bleiben während des Laufs außerhalb des Modellkontexts.

| Fall | Erst nach der Rückfrage verfügbarer Beleg |
| --- | --- |
| VT01 | Errichtung, Erbbaurechtsbestellung und 90.000 Euro erste Rate |
| VT02 | Grundstückserwerb und Neubau mit ausdrücklicher Endzahlung |
| VT03 | Ganzes Haus auf eigenem Grund durch einen Generalunternehmer |
| VT04 | Eigenes Grundstück mit einzeln vergebenem Dachgewerk |
| VT05 | Baugruppe mit eigener Kostenverantwortung und separatem Steuerungsvertrag |
| VT06 | Verkauf und Umbau durch verschiedene Schuldner, verbundenes Angebot |
| VT07 | Langjährig genutzte Wohnung ohne Baupflicht |
| VT08 | Umbaupflicht für den Dachstuhl, beschränkte Leistung an der Bestandstreppe |
| VT09 | Nachzügler, geschuldeter Schallschutz und frühere Erstverwalterabnahme |
| VT10 | Unterschiedliche Wohnungsnummer und Urkundenrolle in der Rechnung |
| VT11 | Vertrag über Vorauszahlung gegen Rückgewährsicherheit, bloßes Angebot einer unterdeckten Fertigstellungsbürgschaft |

Die zusätzliche Probe [MW01](marewald-einstieg.md) verwendet den vollständigen [Marewald-Mustervertrag](../../../vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md). Sie prüft, ob sich der Vertrag anhand der Urkunde unmittelbar einordnen lässt.

Die Eingangsantwort muss eine haftungs- oder zahlungsrelevante Tatsache erfragen. Die zweite Antwort soll die nun belegten Vertragsverpflichtungen zuordnen und das passende Programm anwenden. Bei VT06 und VT10 bleibt auch nach der zweiten Nachricht ein wesentlicher Widerspruch offen. Hier muss der Prüfer die verbleibende Unsicherheit erläutern.

`python3 scripts/test_workflow_dialogue.py ContractModelFixtureTests` prüft Eingangswege, Eingabereihenfolge und die Trennung der Testdaten. Die tatsächlichen Modellantworten und ihre Auswertung sind im [Laufprotokoll vom 21. November 2026](../../runs/2026-11-21/vertragsmodelle.json) festgehalten.
