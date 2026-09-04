---
name: bautraeger-zahlungsrate-pruefen
description: Prüft eine konkrete Bauträger-Zahlungsanforderung gegen Vertrag, MaBV, notarielle Mitteilung, Freistellung, Sicherheiten und Bautenstandsbelege. Verwenden für Rate, Zahlungsfrist, offenen Teilbaufortschritt oder widersprüchlichen Bautenstandsbericht.
---

# Bauträgerzahlungsrate prüfen

Ermittle zuerst die konkrete Frage: Welche Rate, welcher Betrag, welches Objekt, welche Zahlungsfrist? Verknüpfe Vertrag und Fassung, notarielle Mitteilung, Vormerkung, Freistellung, Bautenstandsbericht, Anlagen/Fotos, Rechnung, bisherige Zahlungen und Sicherheiten chronologisch. Ein Vertragsentwurf beweist keinen wirksamen Vertrag; bei ausdrücklich vorgegebenem späterem Testszenario führe Annahme und Urkundenbeleg getrennt.

## Voraussetzungen und Belegkette

Prüfe nach [§ 3 MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/__3.html) unabhängig voneinander die allgemeinen Voraussetzungen, den vertraglich vereinbarten Ratenmeilenstein und den tatsächlich belegten Leistungsstand. Die schriftliche Notarmitteilung gehört zur Belegkette, ersetzt aber keine Feststellung des Bautenstands. Fehlende Unterlage bedeutet Nachweislücke; ein nachgewiesen offenes, für die verlangte Rate notwendiges Gewerk bedeutet einen konkreten Fälligkeitsbefund. Eine Rechnungsfrist allein begründet keine Fälligkeit.

## Raten rechnen

Bei Grundstückseigentum: erste Stufe 30 % der Gesamtsumme, weitere Stufen aus den verbleibenden 70 %. Bei Erbbaurecht: 20 % und Restbasis 80 %. Restquoten sind 40/8/3/3/3/10/6/3/4/12/3/5 % für Rohbau/Dach/Heizung/Sanitär/Elektro/Fenster/Innenputz/Estrich/Sanitärfliesen/Bezugsfertigkeit/Fassade/vollständige Fertigstellung. Höchstens sieben tatsächlich verlangbare Teilbeträge; die zwölf Restgewerke sind keine zwölf zusätzlichen Abrufe. Baue den vertraglichen Zusammenfassungsplan nach. Entfällt ein Gewerk tatsächlich, prüfe die anteilige Umverteilung; fehlende Ausführung ist kein Entfallen.

Das lokale Werkzeug [mabv_rechner.py](scripts/mabv_rechner.py) berechnet Dezimalbeträge und Gruppen. Beispiel: `python3 scripts/mabv_rechner.py --preis 674000 --gruppen '30;28;18.9;9.1;8.4;2.1;3.5'`. Pfad relativ zu diesem Skill auflösen. Der Rechner kontrolliert Rechenbasis und Summe; seine Ausgabe ist ausdrücklich keine Zahlungsfreigabe und kein rechtliches Urteil über die Gruppierung.

Bei einer zusammengefassten Rate muss das letzte enthaltene Gewerk vollständig erreicht sein, soweit keine tragfähige andere Vereinbarung vorliegt. Weise das vertragliche Ratenhindernis aus; erfinde keine einseitige Teilratenfreigabe. Berechne die Fünfprozent-Sicherheit nach [§ 650m Abs. 2 und 3 BGB](https://www.gesetze-im-internet.de/bgb/__650m.html) gesondert. Unterscheide Gesamtsicherheit, bereits einbehaltene Beträge, wirksame anderweitige Sicherheit und den noch offenen Sicherungsbedarf. Keine wiederholte Kürzung um volle 5 % bei jeder Rate.

## Widersprüche und Ergebnis

Gleiche jede relevante Einzelangabe gegen das Fazit des Berichts ab. „Rate freigegeben“ überstimmt weder fehlende Verglasung noch offenen Estrich oder fehlende Dachrinnen. Bewerte die konkrete Einheit und erforderliche gemeinschaftliche Leistungen; Prozente des Gesamtprojekts reichen nicht automatisch.

Gib ein Ratenrechenblatt und eine Zahlungsentscheidung aus: verlangter Betrag, Rechenabweichung, belegter/unbelegter Meilenstein, allgemeine Voraussetzungen, Sicherheiten, Zahlungsverlauf, Ergebnis mit sperrenden Befund-IDs und erforderlicher Abhilfe. Mängeleinbehalt nach § 641 Abs. 3 BGB, fehlende Fälligkeit und Sicherheit nach § 650m BGB sind verschiedene Gründe; keine unkommentierte Addition. Beziffere einen zahlbaren Betrag nur, wenn er sich aus vollständigen Angaben ableiten lässt.

Für rechtlich umstrittene Klauseln, Sicherungsaustausch nach § 7 MaBV, Insolvenz oder unwirksame Zahlungspläne lies die einschlägigen Vertiefungen im [Werkstatt-Prompt](../bautraegervertrag-pruefen/references/werkstatt.md). Prüfe den maßgeblichen Rechtsstand. Aus einer unwirksamen Ratenregelung folgen weder automatisch Vertragsnichtigkeit noch eine selbst erfundene Ersatzrate.
