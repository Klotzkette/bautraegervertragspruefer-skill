---
name: bautraeger-zahlungsrate-pruefen
description: Prüft konkrete Bauträger-Zahlungsanforderungen gegen Vertrag, MaBV, Fälligkeitsunterlagen, Sicherheiten und Bautenstand. Berechnet das tragfähige Zahlungsergebnis, fordert fehlende Belege gezielt an und setzt die Prüfung nach deren Eingang bis zum beauftragten Schreiben fort.
---

# Bauträgerzahlungsrate prüfen

## Vorhandene Angaben auswerten

Lies zuerst Vertrag, Abruf und vorhandene Belege sowie den Gesprächsstand. Ermittle Rate, Betrag, Objekt, Vertragsstatus und Zahlungsfrist daraus; frage nicht erneut nach bekannten Angaben. Verknüpfe notarielle Mitteilung, Vormerkung, Freistellung, Bautenstandsbericht, Anlagen/Fotos, Rechnung, bisherige Zahlungen und Sicherheiten zeitlich. Ein Vertragsentwurf beweist keinen wirksamen Vertrag; bei ausdrücklich vorgegebenem späterem Testszenario führe Annahme und Urkundenbeleg getrennt.

Fehlen entscheidende Unterlagen, frage pro Antwort höchstens drei konkret bezeichnete Informationen oder Belege ab. Sage, welche Entscheidung daran hängt, und bearbeite unabhängig davon die vorhandenen Angaben. Ein auf eine Rate begrenzter Auftrag löst keine ungefragte Gesamtprüfung aus.

## Voraussetzungen und Beträge prüfen

Prüfe nach [§ 3 MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/__3.html) getrennt die allgemeinen Voraussetzungen, den vertraglichen Ratenmeilenstein und den tatsächlich belegten Leistungsstand. Die schriftliche Notarmitteilung ersetzt keine Feststellung des Bautenstands. Fehlende Unterlage bedeutet Nachweislücke; ein nachgewiesen offenes, für die verlangte Rate notwendiges Gewerk begründet dagegen einen konkreten Einwand gegen die Fälligkeit. Eine Rechnungsfrist allein begründet keine Fälligkeit.

Bei Grundstückseigentum: erste Stufe 30 % der Gesamtsumme, weitere Stufen aus den verbleibenden 70 %. Bei Erbbaurecht: 20 % und Restbasis 80 %. Restquoten sind 40/8/3/3/3/10/6/3/4/12/3/5 % für Rohbau/Dach/Heizung/Sanitär/Elektro/Fenster/Innenputz/Estrich/Sanitärfliesen/Bezugsfertigkeit/Fassade/vollständige Fertigstellung. Höchstens sieben tatsächlich verlangbare Teilbeträge; die zwölf Restgewerke sind keine zwölf zusätzlichen Abrufe. Bilde den vertraglichen Zusammenfassungsplan ab. Entfällt ein Gewerk tatsächlich, prüfe die anteilige Umverteilung; fehlende Ausführung ist kein Entfallen.

Das lokale Werkzeug [mabv_rechner.py](scripts/mabv_rechner.py) berechnet Dezimalbeträge und Gruppen. Beispiel: `python3 scripts/mabv_rechner.py --preis 674000 --gruppen '30;28;18.9;9.1;8.4;2.1;3.5'`. Löse den Pfad relativ zu diesem Skill auf. Der Rechner kontrolliert Rechenbasis und Summe; seine Ausgabe ist keine Zahlungsfreigabe und kein rechtliches Urteil über die Gruppierung.

Bei einer zusammengefassten Rate müssen alle enthaltenen Voraussetzungen erreicht sein, soweit keine tragfähige andere Vereinbarung vorliegt. Benenne das noch fehlende Gewerk; erfinde keine einseitige Teilratenfreigabe. Berechne die Fünfprozent-Sicherheit nach [§ 650m Abs. 2 und 3 BGB](https://www.gesetze-im-internet.de/bgb/__650m.html) gesondert. Unterscheide Gesamtsicherheit, schon einbehaltene Beträge, wirksame anderweitige Sicherheit und noch offenen Sicherungsbedarf. Ziehe nicht von jeder Rate nochmals volle 5 % der Vertragssumme ab.

Gleiche die Einzelangaben gegen das Fazit des Berichts ab. „Rate freigegeben“ überstimmt weder fehlende Verglasung noch offenen Estrich oder fehlende Dachrinnen. Entscheidend sind die konkrete Einheit und die erforderlichen gemeinschaftlichen Leistungen; ein Prozentsatz für das Gesamtprojekt genügt nicht automatisch.

## Zahlungsentscheidung treffen

Beginne mit **Ergebnis**: Ist der konkrete Abruf jetzt fällig, teilweise zahlbar, wegen eines feststehenden Hindernisses nicht fällig oder mangels bestimmter Belege noch nicht abschließend beurteilbar? Beziffere verlangten, rechtlich fälligen, bereits gezahlten und noch zu zahlenden Betrag, soweit sie feststehen. Bei einem feststehenden Hindernis für die gesamte angeforderte Rate können aus diesem Abruf derzeit 0 Euro fällig sein; eine bloße Nachweislücke darf nicht als erwiesene Nichtfälligkeit ausgegeben werden.

Rechne den gesamten Ratenplan intern nach. Im Bericht zum Einzelabruf genügen dessen Rechnung und der Zahlungsstand; zeige den Gesamtplan nur bei einem dafür relevanten Fehler oder auf ausdrücklichen Wunsch. Unter **Begründung** stehen die entscheidenden Vertragsstellen und Belege. Trenne fehlende Fälligkeit, Mängeleinbehalt nach § 641 Abs. 3 BGB und Sicherheit nach § 650m BGB; addiere sie nicht unkommentiert. Erläutere nur tatsächlich entscheidende Bedingungen und ihren rechnerischen Einfluss. Fehlen Betragsgrundlagen, benenne diese statt einen Betrag zu erfinden. Keine zusätzlichen Nullbetragstabellen oder Wiederholungen derselben Rechnung und Entscheidung unter mehreren Überschriften.

Für umstrittene Klauseln, Sicherungsaustausch nach § 7 MaBV, Insolvenz oder unwirksame Zahlungspläne lies die einschlägigen Abschnitte im [Werkstatt-Prompt](../bautraegervertrag-pruefen/references/werkstatt.md). Prüfe den maßgeblichen Rechtsstand. Aus einem unwirksamen Zahlungsplan folgen weder automatisch Vertragsnichtigkeit noch eine selbst erfundene Ersatzrate.

## Belege nachfordern, fortsetzen, Schreiben fertigen

Unter **Noch benötigt** stehen nur die konkreten offenen Belege oder Entscheidungen. Erkläre unter **Weiteres Vorgehen**, welche Handlung bis zur Klärung tragfähig ist und welcher Termin berücksichtigt werden muss. Leere Abschnitte entfallen. Ist ein Einwendungsschreiben oder eine Antwort auf den Abruf beauftragt, fertige den Entwurf mit beziffertem Ergebnis und konkreter Begründung unmittelbar an; biete nicht bloß an, ihn später zu schreiben. Nimm die tragende Begründung und Rechnung in das Schreiben auf. Davor genügen gegebenenfalls der Entscheidungswechsel und eine verbleibende Grenze; wiederhole kein vollständiges Gutachten, wenn keines zusätzlich beauftragt ist. Ist der notwendige Adressat oder das Begehren unklar, frage gezielt nach. Entwerfen ist keine Erlaubnis zum Versenden.

Nach Eingang weiterer Angaben prüfe die betroffenen Einwände erneut und rechne die Zahlung neu. Übernimm fortgeltende Ergebnisse, berichtige gegebenenfalls den Schreibenentwurf und erläutere die Änderung. „Weiter“ setzt den offenen Schritt fort, ohne Neuaufnahme. Der Auftrag endet mit der Zahlungsentscheidung und den beauftragten Ergebnissen oder mit einer genau bezeichneten noch erforderlichen Mitwirkung, nicht mit „Soll ich weiter?“.
