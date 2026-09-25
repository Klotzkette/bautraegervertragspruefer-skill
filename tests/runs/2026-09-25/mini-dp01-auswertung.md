# Unabhängige Auswertung DP01 – Mini 4.6.0

Bewertet wurden die tatsächlich gespeicherten Antworten, nicht ein erwartetes oder nachträglich verbessertes Ergebnis. Diese DP01-Antworten wurden nicht von diesem Auswerter erstellt. Der vorherige eigene NR-Probelauf ist weder Bewertungsgegenstand noch Beleg für DP01.

Vollständig gelesen: beide Rohantworten, `erwartungen.json`, beide DP01-Eingaben und die Vertragslesefassung einschließlich Baubeschreibung. Durch Ausgabekürzung zunächst ausgelassene Passagen wurden nachgelesen. Keine Antwort und kein Prompt wurde verändert; keine weiteren Agenten wurden eingesetzt.

## Belegschlüssel und Maßstab

- **T1** = `tests/runs/2026-09-25/mini-dp01-turn1-raw.md`, Zeilen 1–405. Mandantenschreiben **M**: 5–53; Gutachten **G**: 55–304; Notariat **N**: 308–356; Bauträger **B**: 358–405.
- **T2** = `tests/runs/2026-09-25/mini-dp01-turn2-raw.md`, Zeilen 1–252. M: 5–41; Gutachtennachtrag G: 43–135; N: 139–195; B: 197–252.
- **V** = `vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md`.
- **E** = `tests/workflow/default-package/erwartungen.json`.
- Zahlen hinter einem Kürzel sind tatsächliche Dateizeilen, keine behaupteten Druckseiten. „M fehlt“ bedeutet: im vollständig gelesenen Mandantenschreiben keine adressatengerechte Mitteilung des konkreten Befundes und keine konkrete Weglassungsbegründung gefunden.

`pass` = sachlich und im erforderlichen Dokumentenweg erfüllt; `partial` = erkennbar behandelt, aber mit bestimmbarer Inhalts-, Erläuterungs- oder Weitergabelücke; `fail` = eine wesentliche Teilanforderung beziehungsweise ein eigener erheblicher Korrekturbefund fehlt im erforderlichen Produkt. Die getrennten Außenschreiben werden gemeinsam bewertet: Nicht jede Rechtsänderung muss zusätzlich im Bauträgerbrief wiederholt werden, wenn das Notariat sie ausdrücklich erhält. Die funktionale Aufteilung ist in T1:3 und 377 erkennbar. Positive Kontrollen brauchen keine künstliche Änderungsforderung.

Maßgeblich ist besonders E:8–11: Jeder erhebliche eigene Befund muss auch die Beratung erreichen. Ein ausführliches Gutachten und vollständige Außenschreiben ersetzen diesen Weg nicht. T1:298–304 und T2:49/131 enthalten keine konkreten Gründe dafür, einzelne erhebliche Befunde im Mandantenschreiben wegzulassen.

## Pflichtbefunde F1–F8

| Befund | T1 | T2 | Konkrete Bewertung und Dokumentenbelege |
|---|---|---|---|
| **F1 Abnahmefiktion** | pass | pass | T1 G:234–240 trennt § 640 Abs. 1/2, beanstandet Wesentlichkeit und Bezugsfertigkeit; M:23 erklärt die Folge; N:334 enthält verwendbaren Ersatz. T2 G:53–63, M:17, N:157 und B:216 erkennen ausschließlich diese Änderung als erledigt an. Kein Weiterangriff auf den alten Wortlaut. |
| **F2 fehlende Anlagen/WEG/Nachweise** | partial | partial | G T1:61, 83–101, 149, 211–218, 226–230, 280–284 differenziert vorgelegt/behauptet/nicht geprüft und fordert gezielt. N:328/330/350 und B:383/387/395/397 erhalten die wesentlichen externen Anforderungen. M:25–28 nennt Eigentums-/WEG- und ausgewählte Technikfragen, verliert aber insbesondere Baugrund/Abdichtung/Altlasten als eigene entscheidungsrelevante Nachweislücke. T2 G:119–129 hält diese ausdrücklich offen; N:167–189 und B:230–244 führen sie fort; M:30–33 bleibt hinsichtlich dieser Lücke ebenso unvollständig. Keine falsche Erledigung durch § 6.2. |
| **F3 technische Zusagen/Normbezug** | partial | partial | Fensterwert Uw ≤ 1,0 wird in G T1:214 korrekt anerkannt; Schallschutz in G:201–207 mit Komfort, Gegenargument, fehlendem Nachweis und Ersatz geprüft, über M:28 und B:385 weitergeführt; T2 G:125, M:33, B:232 erhalten ihn. **RC 2 aus V:367 wird in keiner Rohantwort positiv kontrolliert**; eine Tür im Schallschutznachweis ersetzt dies nicht. **Elektrozuordnung ungelöst:** G T1:216 fordert nur eine „normativ zutreffende“ Liste; weder RAL-RG 678 noch Abgrenzung zur DIN-Mindestausstattung oder Ausgabe/Leistungsstufe werden erläutert. N:350 ist allgemein, B:387 fordert nur Stückliste. T2 G:125/B:234 reproduziert den unvollständigen Arbeitsauftrag. Elektro fehlt auch in M T1:28 und T2:33. Keine Stückzahlen erfunden, aber Pflichtteilprüfung nicht erledigt. |
| **F4 Preis/Raten/Sicherheiten/positiver Schutz** | pass | pass | G T1:107 erklärt 674.000 EUR, Restbasis 471.800 EUR, sämtliche sieben Prozentanteile und 100 %; G:111/121 und M:33–43 nennen 23.590/33.700 EUR richtig. Tatsächlicher Bautenstand/eigene Prüfung G:109, Protokoll-Schlussrate G:111, sichere Vormerkungslöschung G:264; M:19 und N:330/B:377 erhalten den Schutz. T2 M:35, G:121/128, N:171/173/179, B:238 führen ihn weiter. T1:115 bezeichnet die Aussage unglücklich als „Aktuelle Zahlungsentscheidung“, begründet 0 EUR aber ausschließlich mit fehlendem Vertrag/Abruf; keine erfundene Rechnung und kein unbegründeter Zahlungsstopp. |
| **F5 Mehrkosten/Termine** | pass | pass | G T1:163–171 würdigt konkreten engen Mechanismus, Viermonatsfrage, Saldierung und 20.220 EUR zutreffend; M:27 nennt keine Preisobergrenze. G:175–187/M:24 unterscheiden Bezug 31.03.2028 vom Endtermin; 30.06.2028 ausdrücklich Vorschlag, keine erworbene Forderung. N:346 und B:379/381 übernehmen Maßnahmen. T2 G:123–124 bewahrt die Erstprüfung, M:29/32, N:185, B:226/228 führen offene Fragen fort. Freier Festpreis und Strafenerweiterung bleiben Verhandlungsziele. |
| **F6 eigene Abnahme/fünf Jahre/Selbstvornahme/Wartung** | pass | pass | G T1:242 und 252–258 bestätigt eigene Abnahme, fünf Jahre, richtigen Beginn, organisatorische Anzeige und fehlende Wartungsverkürzung. Keine erfundene Zweijahresfrist/Ausschlusswirkung. M:19/51, N:334/348, B:377 tragen die positive Linie. T2 M:19–23/35, G:73–115, N:159–163/187 und B:218–222 ändern ausdrücklich nur die Bewertung der neuen Anzeigevorschrift; § 9.2/9.4 und eigene Abnahme bleiben erhalten. Zusätzlicher Verbesserungsbefund zur Fristsetzung siehe A27. |
| **F7 Phase/Stichtag/17 Tage/Lesegrenzen** | pass | pass | T1 M:17/47, G:59–75, N:326 und B:377: privat, Entwurf, 09.06.2026, Termin 12.06., 17 Tage aus berichteter Übersendung. G:61 verneint DOCX/PDF-/Seitenkontrolle ausdrücklich. T2:3/25/37/47/133 bewahrt Status und Grenzen; keine tatsächlich ausgeführte Beurkundung, Verschiebung oder Versendung behauptet. Wörtliche Vorvergangenheit in Briefentwürfen ist dennoch eine redaktionelle Schwäche, siehe W5. |
| **F8 neue 14-Tage-Ausschlussfolge** | pass | pass | T1: nicht eingeführt, korrekt nicht erfunden (G:254). T2 G:69–103 analysiert eigenständig ee/ff, § 307, § 306, erkennbare und verdeckte Mängel, keine geltungserhaltende Reduktion, fünfjährige Verjährung als andere Frage. M:19–23, N:159–163 und B:218–222 enthalten konsistente Beanstandung und vollständig nutzbaren Ersatz ohne Rechtsverlust allein wegen Anzeigeversäumnis. |

F3-Unterkontrollen einzeln: Fenster **pass/pass**, Schallschutz **pass/pass**, RC-2-Positivkontrolle **fail/fail**, Auflösung DIN/RAL **fail/fail**, Verzicht auf erfundene Stückzahlen **pass/pass**. Diese Ergebnisse dürfen nicht zu einem pauschalen Technik-pass zusammengezogen werden.

## Workflow beider Turns

| Kontrolle | T1 | T2 | Beleg und Grenze |
|---|---|---|---|
| W1 Tatsächliche Produkte ohne Zusatzauftrag | pass | pass | Alle vier Texte existieren in den oben bezeichneten Abschnitten; keine bloße Ankündigung oder Paket-Rückfrage. T2 liefert zulässigen zugeordneten Gutachtennachtrag und vollständige neue Briefe. |
| W2 Arbeit trotz fehlender Anlagen | pass | pass | T1:61/99/211 und T2:47 unterscheiden Erkenntnisgrenze und erwiesenen Mangel; keine Unterbrechung des gesamten Auftrags. |
| W3 Adressat, Stimme, Frist, Erwerberinneninteresse | pass | pass | N/B in Erwerberinnenstimme mit echten Adressfeldern, Entwurfskennzeichnung, Einzelantwort und Vorbehalt ausreichender Prüfungszeit (T1:352/401; T2:191/248). Keine erfundene anwaltliche Vertretung, maximal zulässige Rückfragen nicht überschritten. |
| W4 Alt/offen/erledigt/neu im Gutachten | pass | pass | Erstprüfung nummeriert; T2:49 und 113–129 ordnen sämtliche Gutachtenpunkte zu, isolieren erledigten § 6.2 und neuen § 9.3. Die Fortgeltung ist auf tatsächliche nummerierte Abschnitte bezogen, kein unsichtbares Register. |
| W5 Handlungstatus innerhalb der Entwürfe | partial | partial | T1 N:346 „habe den Bauträger … gebeten“, B:377 „habe … vorgelegt“; T2 B:220 „habe das Notariat gebeten“ setzen parallel erst entworfene Kommunikation bereits voraus. T1:3/T2:3 erklären ausdrücklich, dass nichts versandt wurde: **kein belegter tatsächlicher Versand**, aber ungeeignete Vorannahme in versandfähigen Texten. |
| W6 Priorität/positiver Schutz | partial | partial | G T1:163–171/181/185/298 und T2:81/115/124/129 unterscheiden Rechtskorrektur, Klärung und Verhandlung. M T1:21 bündelt jedoch alles unter „sollten … erledigt werden“; T2:27–33 unterscheidet viele Zusatzforderungen nicht. Die klare Einordnung des Enddatums und des neuen Ausschlusses bleibt positiv. |
| W7 Lückenlose Befundweitergabe | fail | fail | Die nachfolgend belegten erheblichen Zusatzbefunde verschwinden vor allem aus M, obwohl G und Außenforderungen sie ausdrücklich verlangen. T2 ersetzt die bisherigen Briefe (T2:3); der Gutachtenverweis T2:49 ist kein Ersatz für fehlende Beratung. E:8/11/44 bzw. 52/62 sind insoweit nicht erfüllt. |

## Nachverfolgung zusätzlicher tatsächlich erhobener Befunde

G-, M- und Außenbelege werden getrennt ausgewiesen. T2-G-Verweise auf die nummerierte Erstprüfung zählen gemäß E:9 als Fortführung. Eine nur allgemeine Nennung des Themenbereichs erhält `partial`, wenn die konkrete Folge oder verlangte Änderung verloren geht. Zusätzliche Wünsche werden nicht als bewiesene Unwirksamkeit bewertet.

| ID / tatsächlicher Zusatzbefund | T1: G → M → Außenschreiben | T2: Fortführung → M → Außenschreiben | T1 / T2 |
|---|---|---|---|
| A01 § 13.1 Tatsachenbestätigung über mündliche Abreden neutralisieren | G:77 begründet Beweisnachteil und Ersatz; **M fehlt**; N:344 fordert Neutralisierung. | G:119 hält Korrektur offen; **M fehlt**; N:167 konkret. | fail / fail |
| A02 Zusätzliche MaBV-Voraussetzungen/Aushändigung/Rang und sämtliche Grundpfandrechte | G:95–101; M:26; N:330/B:391. Nachweislücke korrekt statt behaupteter Nichtexistenz. | G:121; M:31; N:171/B:238. | pass / pass |
| A03 Zusätzliche 14-Kalendertage-Zahlungsfrist | G:109 als Empfehlung; M fehlt; N:332. | G:121; M nennt nur MaBV-Nachweise, keine Prüfungs-/Zahlungsfrist; N:171. Verhandlungsverbesserung, kein gesetzlicher Fristanspruch behauptet. | partial / partial |
| A04 Herstellungssicherheit: Umfang und eigenes Einbehaltsrecht | G:121–123; M:38/43 beschreibt Bedingtheit/Doppelsicherung, erklärt aber die verlangte neue Wahlrechtsklausel und Gemeinschaftsumfang nicht; N:332/B:391. | G:121; M:31 nur „Herstellungssicherheit“; N:173/B:238 konkret. | partial / partial |
| A05 Gesetzliche Zusatzsicherheit bei Erhöhung über 10 % | G:125 berechnet 67.400-EUR-Schwelle/5 % Mehrbetrag und verlangt Ergänzung; **M fehlt**; N:332/B:391. | G:121 offen; **M:31 nennt nicht diese zusätzliche gesetzliche Sicherung**; N:173/B:238. | fail / fail |
| A06 Gesicherte Sonderwünsche: konkretes Angebot, Fälligkeit, §-7-Rückgewährschutz, lückenloser Wechsel | G:127–129; **M nennt nur Kosten von Sonderwünschen (45), keine Zahlungs-/Sicherungsanforderung**; N:332/B:391. | G:121; **M fehlt**; N:173/B:238 erhalten wesentliche Inhalte. | fail / fail |
| A07 Zusatzberatung 178,50 EUR: Freigabe, Zeitnachweis, Abrechnungstakt | G:129; **M fehlt**; B:389 fordert Umsetzung. | G:121/123; M:33 nur Bemusterung ohne Kostenfolge/Freigabe; N:173/B:236 konkret. | fail / fail |
| A08 Finanzierung: persönliche/dingliche Haftung, Nebenleistung, separate Bankurkunde, Zweckbegrenzung und Scheitern des Erwerbs | G:135–141; M:29 benennt Haftung/Nebenleistung und gesonderte Prüfung; N:338 setzt Details um. | G:122; M:31 hält Finanzierungsvollmacht offen; N:175 konkret. Einzelheiten sinnvoll beim Notariat. | pass / pass |
| A09 Einheitliche Leistungsänderungsgrenzen, V.2/V.3, keine Mangelfreiheitsfiktion für Schächte/Decken | G:149–153 erhebt eigenständigen Korrekturbefund; **M fehlt** (M:29 betrifft Vollmacht, nicht Baubeschreibungsfiktion); N:344/B:393. | G:123; **M fehlt**; N:183/B:240. | fail / fail |
| A10 Rechtzeitige Bemusterung, keine Entwertung von Wahlrechten durch Verkäuferverzögerung | G:155 konkrete Ergänzung; M:28 erwähnt nur Serien, nicht Verlust von Auswahlrechten; B:389. | G:123; M:33 nur Themenwort; N:183/B:236 konkret. | partial / partial |
| A11 Preisvorbehalt: Kostenbasis, Zuordnung, gewerkeübergreifende Einsparung, Preissenkung, Abstimmung § 5.6 | G:163–169; M:27 erklärt Mehrkostenrisiko und 3-%-Grenze; N:346/B:381 enthalten konkrete Abhilfe. | G:123; M:32; N:185/B:228. Haupt-/Hilfsforderung in G klar unterscheidbar. | pass / pass |
| A12 Aufhebungsalternative: konkrete Rückzahlung/Sicherheit, keine automatische Erwerbsaufgabe | G:171; M:27 erklärt nur fehlende Obergrenze, nicht Wahlrecht/Rückabwicklungsfolgen; N:346/B:381. | G:123; M:32 bleibt pauschal; N:185/B:228 erhalten Sicherungsforderungen. | partial / partial |
| A13 Endtermin/Schlussrate müssen gesamten Gemeinschafts-/Außenumfang erfassen | G:111/179–181; M:24/28; N:346/B:379/393. | G:124/125; M:29/33; N:171/185, B:226/240. | pass / pass |
| A14 Quartiersbau nach Bezug: Schutzplan für Zugänge, Verkehr, Staub/Lärm, keine pauschale Duldung | G:183 fordert eigenständiges Konzept; **M fehlt**; B:379 konkret. | G:124; **M fehlt**; B:226 konkret. | fail / fail |
| A15 Vertragsstrafe auf Endtermin erweitern, einheitliche Kappung | G:185 ausdrücklich verhandelbar; M:19/40–41 erläutert nur vorhandene Strafe; B:399 fordert Erweiterung. | G:124; M fehlt zur Erweiterung; B:246 erhält Verhandlungswunsch. Kein erdachtes bereits bestehendes Recht. | partial / partial |
| A16 Planfläche als Soll erhalten; Ist-Fläche keine einseitige Leistungsbestimmung | G:193–197 konkrete Auslegung/Klausel; M:28 nur „Flächen“; N:344/B:383 verlangen Sollklärung bzw. Berechnung. | G:125; M:33 nur „Flächen“; N:183/B:230/240 konkret. | partial / partial |
| A17 Baugrund/Abdichtung/Wassereinwirkung/Altlasten-Unterlagen | G:211/256 mit entscheidungsrelevanten Risiken; **M fehlt**; B:383/387. Keine festgestellten Ausführungsmängel behauptet. | G:109/125/127; **M fehlt**; B:230/234. | fail / fail |
| A18 Brand-/Rettungsweg-/GEG-Nachweis, Bauantragsdatum, Übergangsrecht | G:212; M:28 enthält KfW-Abgrenzung, aber nicht Brandschutz/Bauantragsdatum als Prüflücke; B:387. | G:125; M:33 nennt weder Brand/Rettungswege noch GEG-Nachweis; B:234. | partial / partial |
| A19 Lüftung/Gesamtfeuchteschutz/Nutzerverhalten/Wärme/Sommerwärmeschutz | G:212–214; M:27–28 nennt offene Themen und nicht zugesagte Wärmerückgewinnung/KfW; B:387/397 konkret. | G:125/129; M:32–33; B:234/244. | pass / pass |
| A20 Fensterbauart/Öffnung/Sonnenschutz; vorhandener Uw-Wert | G:214 erkennt Wert an; M:28 nennt Sommerwärmeschutz, aber keine eigenständige Fensterwert-Bestätigung; B:387 verlangt nur offene Ausführungsdetails. Positive Zahl muss keine Außenforderung werden. | G:125 erhält Prüfung; M:33/B:234 erhalten offenen Wärmeschutz. Keine Herabsetzung des zugesagten Werts. | pass / pass |
| A21 Serien/Auswahlumfang, „malerfertig“ und nicht enthaltener Anstrich | G:215; M:28/45 übernimmt Serien/Anstrich, **nicht die offene Oberflächenqualität**; B:389 konkret. | G:125; M:33 nennt nur Bemusterung; B:236 erhält Oberfläche und ausgeschlossenen Anstrich. | partial / partial |
| A22 Stellplatznutzbarkeit/Maße und nicht zugesagte Ladeinfrastruktur | G:217; M:28 nennt Stellplatzabmessungen; B:387 konkret. Ladeausstattung nur zusätzliche Abfrage/Verhandlung, kein vorhandener Anspruch. | G:125; M:33; B:234. | pass / pass |
| A23 Unterlagenliste und verbindliche Übergabezeitpunkte | G:226–228 trennt § 650n und zusätzliche Zusagen, formuliert Ergänzung; **M fehlt**; B:395/N:350. | G:125; M:33 hält Dokumentationstermine ausdrücklich offen; N:189/B:242 konkret. | fail / pass |
| A24 Zusätzliche Kontrollen vor Überdeckung kritischer Bauteile | G:230 verhandelbar; M:51 rät nur zur Nutzung schon vorgesehener Kontrollen und erläutert nicht deren zeitliche Lücke; B:395. | G:125; M:33 nur „Kontrolltermine“, ohne Risiko des Verdeckens; N:189/B:242 erhalten Forderung. | partial / partial |
| A25 § 6.1 Gegenrechte unabhängig von Mängelanerkennung | G:244 konkrete Klarstellung; **M fehlt**; N:336. | G:63/126; **M fehlt**; N:177. | fail / fail |
| A26 Gefahrtragung für offene/nicht abgenommene Herstellung, getrennte Protokolle | G:246 verlangt Korrektur; **M fehlt**; N:334/336. | G:63/126; **M fehlt**; N:177. | fail / fail |
| A27 Gesetzliche Ausnahmen vom Nacherfüllungs-Fristsetzungserfordernis | G:254/N:348 erhalten Ausnahme; M:51 thematisiert spätere Abnahme, **nicht diese Korrektur**. | G:101/103/127; M:23 nennt Ausnahmen ausdrücklich; N:163/B:222 identischer Ersatz. | partial / pass |
| A28 Grundstücksfreizeichnung darf vereinbarte Beschaffenheit/Baugrund-/Nutzungsrisiken nicht erfassen | G:256 ausdrücklich „Erforderliche Klarstellung“; **M fehlt**; N:348/B:383. | G:109/127 offen; **M fehlt**; N:187/B:230. | fail / fail |
| A29 Vormerkung: Anhörung, endgültiger Anspruchswegfall, bestimmte Ersatzsicherheit, Zwischenrechte | G:264; M:19 lobt bestehenden Schutz, erläutert erforderliche Präzisierungen nicht; N:340. | G:128; M:31 benennt ausstehende Vormerkungslöschungsergänzungen; N:179 führt alle weiter. | partial / pass |
| A30 Eigentumsumschreibung trotz Einbehalt, keine doppelte Sicherheit | G:266; M:29 erklärt Widerspruch; N:340 Ersatz. | G:128; M:31 offen; N:179 konkrete Lösung. | pass / pass |
| A31 Vollmacht: Außenwirkung, Verfahrensumfang, Ende, Rechteverzicht | G:268; M:29 erklärt Kernrisiko Außenwirkung; N:342 konkret. | G:128; M:31; N:181 konkret. | pass / pass |
| A32 Allgemeine Gebührenregel darf Erschließungskostenabrede nicht aushebeln | G:274 fordert ausdrückliche Klarstellung; M fehlt; N:350. | G:129 erhält Punkt 17; M:35 bestätigt Erschließung positiv ohne Kollisionsfrage; N:189. Die positive Ausgangsklausel wird nicht fälschlich verworfen. | partial / partial |
| A33 WEG-Einrichtungskosten: Leistungsumfang, Quote, Bruttohöchstbetrag/Verkäuferübernahme, Doppelentgelt | G:276; M:27 beziffert fehlende Kalkulierbarkeit als Problem; N:350/B:397 konkrete Alternativen. | G:129; M:32; N:189/B:244. | pass / pass |
| A34 Wärme-/Contracting-/Verwaltungs-/Betriebskosten und Kündigung | G:278–284; M:25/27; N:350/B:397 konkret zu Dauer, Preisen, Anlageneigentum, Kosten-/Stimmrechten. | G:129; M:30/32; N:189/B:244. | pass / pass |
| A35 Insolvenzschutzgrenzen/Verkäuferbonität/Projektfinanzierung | G:288–294 erklärt Sicherungsgrenzen und verlangt wirtschaftliche Prüfung; **M beschränkt sich auf vorhandene Sicherheit und Erwerbsnebenkosten, Risikobefund fehlt**; B:399 verlangt Informationen. | G:129 erhält wirtschaftliche Absicherung; **M fehlt**; B:246 konkret. Keine Insolvenz behauptet, aber erheblicher eigener Beratungsgegenstand verloren. | fail / fail |
| A36 Zusätzliche Fertigstellungssicherheit | G:292/298 verhandelbar; M fehlt; B:399 fragt Angebot an. | G:129 ausdrücklich verhandelbar; M fehlt; B:246. Nicht als gesetzlicher Vollschutz ausgegeben. | partial / partial |
| A37 Persönliche Gesamtfinanzierung/Erwerbsnebenkosten | G:294 und M:45 stimmen bei 37.070 EUR Steuer/711.070 EUR Zwischensumme überein; fehlende individuelle Finanzierung wird benannt. Keine sachfremde Forderung an Bauträger erforderlich: G:294 nennt ausdrücklich fehlende Eigenmittel/Zins/Tilgung der Erwerberin. | G:129 erhält „belastbare persönliche Gesamtkostenplanung“, M:25/35 bewahrt Kaufpreis-/Sicherungsinformationen, lässt Nebenkostenbedarf der ersetzten Beratung aber weg. | pass / partial |

Weitere positive beziehungsweise phasenbedingt nicht extern zu verfolgende Feststellungen: T1 G:71/89 zu Identität/Registervertretung wird in N:328, T2 G:120/N:169 fortgeführt (**pass/pass**, kein materiell festgestellter Vertretungsfehler). G T1:278/N:350 sowie T2 N:189/B:244 wahren jederzeitige Verwalterabberufung (**pass/pass**). T1 G:187/258/M:51 zu späteren Vorbehalten/Verjährungsüberwachung bleibt in T2 G:65/107 erhalten; kein aktueller Abnahmevorgang, Zahlungsabruf oder festgestellter Baumangel erfordert jetzt zusätzliche Außenmaßnahmen. Dafür existieren konkrete Nichtaufnahmegründe in T1:304 und T2:65/97/133 (**pass/pass**). T1 G:218 unterstellt keine Barrierefreiheit; aus dieser bloßen Begrenzung wird folgerichtig keine unbestellte Zusatzleistung verlangt (**pass/pass**).

## Fachliche Kontrollen und Quellenbegrenzung

| Gegenstand | Bewertung | Befund |
|---|---|---|
| Elektro-Normsystem | fail | Die Lücke in F3 ist materiell: [DIN 18015-2:2021-10](https://www.dinmedia.de/en/standard/din-18015-2/342893816) betrifft Mindestausstattung; die Werte 1/2/3 werden von [RAL-RG 678/HEA](https://www.hea.de/themen/elektroinstallation/ral-rg-678) beschrieben. Eine „normativ zutreffende“ Liste zu verlangen löst die falsch bezeichnete Zusage nicht selbst auf. |
| § 9.3 neu/§ 650o | pass | T2:81–95 nennt das einschlägige Klauselverbot [§ 309 Nr. 8 b ee/ff BGB](https://www.gesetze-im-internet.de/bgb/__309.html), trennt § 307/§ 306 und stellt in T2:91 richtig klar, dass [§ 650o](https://www.gesetze-im-internet.de/bgb/__650o.html) § 634a nicht pauschal unabdingbar macht. Keine rechtliche Freigabe der Ausschlussfolge. |
| Sicherheit/Fertigstellung | pass | Zahlen und Maßstäbe T1:121–125/179 sind mit [§ 650m Abs. 2](https://www.gesetze-im-internet.de/bgb/__650m.html) und [§ 650k Abs. 3](https://www.gesetze-im-internet.de/bgb/__650k.html) vereinbar. Eigenes Einbehaltswahlrecht wird als Verbesserung behandelt. Kein Rechtsanspruch auf das frei vorgeschlagene Datum 30.06.2028. |
| BeurkG-Verweis | pass | § 13c in T1:73 ist kein veralteter oder erfundener Verweis: [amtlicher Text](https://www.gesetze-im-internet.de/beurkg/__13c.html); der amtliche Gesamttext weist die Änderung vom 10.12.2025 aus. |
| Rechtsprechungsnachweise/Volltextanspruch | partial | T1:205 stellt Aussage, Altfallgrenze und Gegenargument zum Schallschutz dar. T1:113 zitiert VII ZR 84/09 mit Anpassung des alten Druckzuschlags. T1:302 legt aber selbst nur Abschnitts-/Auszugsprüfung und Abrufgrenzen offen. Aus den Antwortdateien allein lässt sich keine vollständige damalige Quellenprüfung belegen; dieser Bericht wertet sie weder als erwiesen noch als erfunden. Der DeJure-Direktabruf ließ sich auch bei dieser Auswertung nicht zuverlässig lesen. Kein darauf gestützter neuer materieller Rechtsfehler festgestellt. |

## Erfüllte und nicht erfüllte Akzeptanzschranken

| Schranke aus E | Ergebnis | Konkreter Grund |
|---|---|---|
| Alle tatsächlichen Produkte vorhanden | pass | Beide Turns enthalten Beratung, Gutachten/Nachtrag und phasengerechte Außenentwürfe. |
| Richtige Reaktion auf beide Klauseländerungen | pass | F1 wird abgegrenzt erledigt, F8 vollständig neu bearbeitet; F6 wird differenziert aktualisiert. |
| Jeder Pflichtbefund vollständig geprüft | fail | F3 bleibt bei Elektro-Normzuordnung und RC-2-Kontrolle unvollständig; zusätzliche Teilgrenze F2. |
| Kein erheblicher Befund still aus einem erforderlichen Produkt verloren | fail | Besonders belastbare Gegenbelege sind A01, A05, A06, A14, A17, A25, A26, A28 und A35. Sie sind in G und Außenforderungen konkret, in M beider Turns nicht vermittelt und ohne konkreten Weglassungsgrund. A23 wird erst in T2 aufgegriffen. |
| Unveränderte Befunde im Rücklauf vollständig als Beratungs-/Änderungspaket erhalten | fail | G und Außenschreiben erhalten sie weitgehend, die ersetzte Beratung bleibt selektiv. Der referenzierte Gutachtennachtrag heilt die dokumentierten M-Lücken nicht. |

Damit ist ein Bestehen nach E:11 ausgeschlossen, ohne daraus ein pauschales Urteil über sämtliche fachlichen Ergebnisse abzuleiten. Die maßgeblichen Fehler sind konkret die unvollständige technische Pflichtprüfung und die dokumentierten Verluste auf dem Weg zur Erwerberinnenberatung; die Abnahme- und Ausschlussfristenprüfung selbst besteht.

## Unveränderte Auswertungsgrundlage (SHA-256)

| Datei | SHA-256 |
|---|---|
| T1 | `ddba83e96f4d397cbb5f2b4cf949c58538abded47fadfa621a1fc891d7781466` |
| T2 | `98c7c67ddb448c72a73c21f156d707f550880061d39a6070173e543b56fe6963` |
| Erwartungen | `122b9eff67bb636c98ca33a9af931682ec05be3c627b83bf0e4d7f380642068f` |
| Eingabe DP01-01 | `d97ece4acfd156a905734745ff86e8c5da19477851087e6718c4aefe03056290` |
| Eingabe DP01-02 | `c01ebe9849deda482713fa19fb6a7db7065bc3ee6f9cc4607e3703e42db42a3a` |
| Vertrag einschließlich Baubeschreibung | `51418ae0399cdaf5583a0d8b814a166ae107ef266512acab04636d667cbd1820` |
