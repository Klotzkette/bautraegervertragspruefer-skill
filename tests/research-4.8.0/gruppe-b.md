# Recherchegruppe B – Rechtsprechungsanker 19–37

Prüftag: 08.10.2026. Auftrag: vertiefte Erwerberprüfung, keine Behauptung vollständiger Erfassung aller publizierten oder unveröffentlichten Rechtsprechung bis zu diesem Tag.

## Ergebnis und Integrationsformat

- `gruppe-b.json` ist ein JSON-Array mit 19 Einträgen, Indizes 19 bis 37. Jede `expanded_markdown` enthält genau einmal die drei Katalogpflichtlabels und bewahrt den bisherigen Titel.
- Alle 22 Bestandsaktenzeichen bleiben enthalten. Ergänzt sind VII ZR 54/07 in Eintrag 20, V ZR 128/23 in Eintrag 26 und V ZR 34/24 in Eintrag 35, jeweils mit Datum, Urteilsform, amtlichem Link und konkret gelesenen Randnummern.
- Vollständig gelesen: 24 unterschiedliche amtliche BGH-Original-PDFs (21 aus dem Bestandsauftrag, drei ergänzende Originale). Bei V ZR 182/12 enthält das gelesene Dokument auch die Behandlung des verbundenen Verfahrens V ZR 74/12. Dieses ist nicht als neuer eigenständiger Kataloganker angelegt.
- OLG Karlsruhe 19 U 128/24 bleibt ausdrücklich ein amtlich belegter Kurztext-/Leitsatzanker. Kein amtlicher Langtextzugang und keine Volltextlektüre behauptet.
- Einträge umfassen überwiegend rund 275–340 Wörter. Keine redaktionellen Sekundärzusammenfassungen als tragende Belege übernommen.
- Die JSON-Felder `source_urls`, `read_scope`, `pinpoints`, `procedural_status` und `newer_search` sind der genaue Quellen-/Statusnachweis. `full_read: true` steht nur bei vollständig gelesenem amtlichem Urteil einschließlich der relevanten Gründe.

## Abrufmethode und echte Lesegrenzen

BGH-PDFs wurden unmittelbar von bundesgerichtshof.de mit curl abgerufen und durch pdftotext -layout ausgegeben. Die Weböffnung einzelner BGH-Links (insbesondere VII ZR 45/06 und VII ZR 65/14) scheiterte zunächst mit HTTP 403. Der direkte amtliche PDF-Abruf funktionierte. Ausgaben, die bei gebündelten Aufrufen gekürzt waren, wurden anschließend abschnittsweise bis zum Schluss nachgelesen; bloßes Herunterladen wurde nicht als Lesen gewertet.

V ZR 162/25: Zunächst Version v=1 vollständig gelesen. Die im Bestandskatalog verlinkte Version v=4 anschließend direkt abgerufen; ihr vollständig extrahierter Text ist Zeichen für Zeichen mit der gelesenen Version v=1 identisch. Es besteht insoweit keine offene Versionsdifferenz.

OLG Karlsruhe: Der amtliche indexierte Kurztext führte Gericht, Datum, Aktenzeichen, Vorinstanz, Leitsätze/Randnummernverweise und ausdrücklich das Metadatum **Rechtskraft: ja**. Der kanonische Permalink, /part/L und format/xsl lieferten bei erneuten Öffnungen nur die JavaScript-Hinweisseite; auch direkter HTTP-Abruf brachte keinen Langtext. Browser-Fallback wurde versucht: IAB nicht verfügbar, Browserinventar leer. Exaktaktenzeichensuche mit Volltext, filetype:pdf und site:dnoti.de erbrachte keine zugängliche DNotI-Originalreproduktion. Eine nichtamtliche nu:legal-Wiedergabe wurde gefunden und ausschnittsweise gesehen, aber weder als amtlicher Volltext noch als Grundlage zusätzlicher nicht im amtlichen Kurztext belegter Tatsachen verwendet. Darum enthält der Eintrag keine erfundenen weiteren Tatbestandsdetails oder frei zugeschriebenen Randnummern.

## Materiell wichtige Änderungen gegenüber der Kurzfassung

1. **Eintrag 20:** VII ZR 54/07 führt die Schallschutzlinie unmittelbar für Eigentumswohnungen fort. Eine DIN-4109-Verweisung erklärt eine Absenkung erwartbarer Wohnqualität nicht hinreichend. Kein allgemeiner heutiger Dezibelwert aus den historischen Fällen.
2. **Eintrag 21:** Technische Aktualisierung vor Abnahme verlangt Aufklärung und informierte Entscheidung. VOB/B-Mehrvergütung, Sowieso-Kosten und vorabnahmerechtliche Kündigungs-/Vorschussfragen sind keine ungeprüften Bauträgerregeln.
3. **Eintrag 22:** Einzelgewerk und zeitlich sukzessive selbständige Vergabe sind kein Verbraucherbauvertrag allein wegen privaten Bauzwecks. Die eigenständige Bauträgerausnahme in § 650f Abs. 6 Satz 1 Nr. 2 BGB bleibt erhalten; kein Freibrief für Umgehung.
4. **Eintrag 23:** Planbereitstellung, Koordination und Überwachung sind verschiedene Obliegenheiten. Die unterschiedlichen Haftungsquoten erklären sich daraus; nicht auf den passiven Bauträgererwerber übertragen.
5. **Eintrag 24:** V ZR 39/24 handelt von eigenen öffentlich-rechtlichen Prüfpflichten eines Teilerbbauberechtigten, nicht vom vertraglichen Qualitätsstandard einer neuen Wohnung. Die DIN-Vermutung wird nur wiederholt.
6. **Eintrag 25:** Ausdrückliche Aufgabe der älteren zwingenden Raumzuordnung. Gemeinsame Anlage, Raum, Zutritt und richtiger Anspruchsgegner getrennt prüfen.
7. **Eintrag 26:** Keine bloße Willkürkontrolle und keine feste prozentuale Toleranzschwelle. Der konkrete Ausgangsschlüssel war Wohnfläche; der BGH verwies zur Flächenaufklärung zurück. V ZR 128/23 erklärt ergänzend Rücklagenkompetenz und Korrektur unbegründeter Altprivilegien.
8. **Eintrag 27:** Konkrete triftige Änderungsgründe und Zumutbarkeit erforderlich; allgemeine interne Nachteilsgrenzen genügen nicht. Private Gewerbeinvestition kann Verbraucherhandeln bleiben.
9. **Eintrag 28:** Fehlerhafte Stimmrechtsregel und Rechtsfolge des konkreten Beschlusses unterscheiden. Keine automatische Nichtigkeit aller Beschlüsse.
10. **Eintrag 29:** Feststellung bestehender Rechte gegen die GdWE nicht mit gestaltender Änderung der Gemeinschaftsordnung gleichsetzen.
11. **Eintrag 30:** Jede Stufe einer Beschlusskette prüfen. Ein unwirksamer Absenkungsbeschluss bewirkt nicht von selbst Nichtigkeit des späteren Sachbeschlusses; dessen eigene Nichtigkeitsgründe bleiben unberührt.
12. **Eintrag 31:** Keine eigenmächtige Installation und keine Privilegierung analog § 20 Abs. 2 WEG. Gestattung und spätere Betriebsstörung getrennt; TA Lärm keine pauschale Freizeichnung.
13. **Eintrag 32:** Bereits verwirkte Vertragsstrafe bleibt grundsätzlich trotz Rücktritt. Keine Aussage über Strafweiterlauf nach Rücktritt oder allgemeine AGB-Gültigkeit jeder 5-%-Klausel.
14. **Eintrag 33:** Abnahmeverlangen kann das Ende der Errichtungsphase markieren; nicht schlicht „vor der letzten Abnahme“. Vertragliche Erwerberrechte waren nicht Streitgegenstand.
15. **Eintrag 34:** Nur Gesamt-GdWE bündelt diese Herstellungsrechte. Persönlicher Rücktritt/großer Schadensersatz nicht pauschal erfasst; Beschlusskompetenz beweist keinen Baumangel.
16. **Eintrag 35 – besonders wichtig:** V ZR 34/24 verneint nach WEMoG die drittschützende Wirkung des Verwaltervertrags. Heutige vertraglich fundierte Ansprüche des Eigentümers grundsätzlich gegen GdWE, deren Regress gegen Verwalter gesondert; deliktische Eigenansprüche nicht ausgeschlossen.
17. **Eintrag 36 – besonders wichtig:** V ZR 219/24 erweitert die praktische Erstherstellungsaufgabe auf bestimmte SE-Bauteile. Rn. 35 belässt deren Kosten dennoch beim jeweiligen Eigentümer. Kein pauschales Vergemeinschaften von Kosten, kein starrer 50-%-Ausschluss der Erstherstellung.
18. **Eintrag 37:** Interne Kostenlast für Anfangsmängel, nicht Verlust vertraglicher Bauträgerrechte. Die 2025 offen gelassene Kompetenzfrage ist mit dem gesonderten Folgeanker 38 zu verbinden, nicht als weiterhin unentschieden darzustellen.

## Verfahren, Berichtigungen und spätere Recherche

Die genauen Suchanfragen stehen pro Eintrag im JSON. Suchtreffer wurden nach Datum der gerichtlichen Entscheidung und Gegenstand eingeordnet, nicht nach Veröffentlichungs-/Crawl-Datum einer Besprechung. Eine 2026-Besprechung eines Urteils aus 2025 ist keine neue gerichtliche Entscheidung.

- **V ZR 50/25:** Berichtigung vom 04.05.2026 im Original gelesen. Nur Datum der LG-Vorentscheidung berichtigt (20.02.2025 statt 21.02.2025), keine inhaltliche Neubewertung.
- **V ZR 189/24:** Berichtigung vom 15.04.2026 im Original gelesen. Nur Literaturnachweis in Rn. 15 geändert.
- **V ZR 128/23:** Berichtigung vom 24.02.2025 vollständig gelesen. In Rn. 16 WEG statt BGB.
- **VII ZR 54/07:** Original vollständig gelesen (11 Seiten, Rn. 1–21); unmittelbare Fortführung von VII ZR 45/06, keine endgültige Festlegung eines allen Wohnungen geschuldeten Werts.
- **V ZR 34/24:** Original vollständig gelesen (15 Seiten, Rn. 1–26). Alte Schutzwirkung aus V ZR 75/18 wird ausdrücklich referiert und für den neuen Rechtsstand verneint.
- **V ZR 128/23:** Original vollständig gelesen (14 Urteilsseiten plus Berichtigung). Sein Zitat von V ZR 132/23 betrifft nur Beschlussauslegung und erkennbare Bezugsunterlagen, nicht eine erneute Entscheidung der Bündelungsfrage.
- **V ZR 158/25:** In V ZR 98/25 Rn. 18 historisch als anhängig erwähnt. Exakte Aktenzeichensuche ergab keine veröffentlichte spätere Sachentscheidung. Kein heutiger Anhängigkeitsstatus behauptet. Nur Forschungsstatus, nicht im erweiterten Prompttext.
- **V ZR 76/26:** In V ZR 190/25 historisch als anhängig erwähnt. Exakte Aktenzeichensuche ergab nur Wiederholungen dieses Hinweises, keinen nachfolgenden Sachtext. Ebenfalls kein heutiger Status behauptet und nicht im erweiterten Prompttext.
- **VII ZR 68/24:** Im Recherchelauf zu VII ZR 65/14 als späteres Zitat entdeckt. Keine vollständige Lektüre, keine neue materielle Technikregel daraus übernommen.
- **OLG Schleswig 17.12.2025 – 12 U 35/25:** Spätere Anwendung zur Herausnahme wesentlicher Haustechnikgewerke entdeckt. Amtliches Inhaltsverzeichnis belegt Datum/Aktenzeichen/Thema. Abruf des gefundenen Einzel-PDFs scheiterte mit 404 bzw. Extraktionsfehler. Keine Volltextprüfung behauptet; nicht in Harte Fundstelle übernommen.
- **LG Frankfurt/Main 28.05.2026 – 13 S 70/25; LG Berlin II 16.06.2026 – 56 S 56/25:** Spätere Zitate von V ZR 50/25 entdeckt; nicht im Original gelesen, keine zusätzlichen tragenden Aussagen in den erweiterten Eintrag eingeführt.
- **V ZR 102/24:** Entscheidung vom 24.04.2026 als Nachfolger zur in V ZR 36/24 offen gelassenen Frage aufgefunden, bereits eigener Bestandsanker 38 und Auftrag der anderen Gruppe. Hier keine zweite Volltextprüfung behauptet.

## Offene Beleglücke

Für 19 U 128/24 ist vor einer über die amtlichen Leitsätze hinausgehenden Verwendung der vollständige gerichtliche Text erforderlich. Der bestehende Kurztextanker bleibt nutzbar, muss aber seine Beleggrenze behalten. Alle anderen in den Harten Fundstellen dieser Gruppe verwendeten Originalentscheidungen wurden vollständig gelesen. Negative spätere Suchbefunde sind ausdrücklich keine Garantie, dass keine unveröffentlichte Entscheidung, Verfahrenshandlung oder nicht indexierte Fortentwicklung existiert.

