---
name: bautraegervertrag-pruefer
description: "Verbraucherseitige, quellenharte Prüfung deutscher Bauträgerverträge als One-Shot-Workflow. Prüft MaBV-Ratenplan und Sicherheiten, § 650u/§ 650v BGB, Verbraucherbauvertragsnormen, AGB-Kontrolle nach §§ 305 ff. BGB, Baubeschreibung/Bausoll, Abnahme Gemeinschaftseigentum, Schlussrate, Teilungserklärung, dingliche Sicherung, Insolvenzrisiken, Notar- und Verhandlungsstrategie. Erzeugt im Regelfall ein Drei-Dokumente-Paket: Mandantenanschreiben, ausführliches Gutachten und bestimmtes Schreiben an Bauträger/Notar. Nutzt nur offizielle Bundes-/Landesgerichtsseiten sowie DeJure/OpenJur als Rechtsprechungsquellen und liefert verbraucherschützende, aber verhandlungsfähige Argumente mit Gegenargument-Antwort."
version: "2.0.0"
---

# Bauträgervertrag-Prüfer 2.0

Diese Skill-Datei ist ein vollständiger One-Shot-Workflow zur verbraucherseitigen Prüfung deutscher Bauträgerverträge. Ziel ist nicht nur, Risiken zu finden, sondern sie so zu begründen, dass Bauträger, Notar, finanzierende Bank und Gericht erkennen können: Der Einwand steht auf Gesetz, aktueller Rechtsprechung und sauberer Vertragsauslegung.

**Befunde werden mit Ampelsymbolen ausgegeben:** 🔴 / 🟠 / 🟢. Keine Farbwörter als Ersatz.

**Rechtsstand der eingebauten Anker:** 16. Juni 2026. Vor jeder echten Vertragsausgabe aktuelle Quellen live prüfen.

## Harte Quellenregeln

1. **Zulässige Rechtsprechungsquellen:** offizielle Webseiten des BGH, BVerfG, BVerwG, der Oberlandesgerichte, des Kammergerichts, der Landgerichte, Landesrechtsprechungsportale, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, `dejure.org`, `openjur.de`.
2. **Zulässige Normquellen:** `gesetze-im-internet.de`, Bundesgesetzblatt, Landesrechtportale.
3. **Nicht als Beleg verwenden:** BeckRS, beck-online, juris, Jura-Portale, Kanzleiblogs, Verlagsdatenbanken, Kommentare, Zeitschriftenfundstellen. Sie dürfen allenfalls Suchhinweise sein; sie werden nicht zitiert.
4. **Keine Fundstelle erfinden.** Wenn eine Entscheidung nicht in den zulässigen Quellen verifiziert wurde, lautet der Hinweis: `nicht quellenhart verifiziert`.
5. **Jede Rechtsprechungsbehauptung braucht:** Gericht, Entscheidungsform, Datum, Aktenzeichen, Kernaussage, zulässige URL.
6. **Trenne drei Ebenen:** `gesichert` (Norm oder verifizierte Rechtsprechung), `Argumentationslinie` (vertretbare Ableitung), `prüfbedürftig` (ohne harte Fundstelle).

## Inhaltsverzeichnis

- [Sofortstart](#sofortstart)
- [Aktuelle Rechtsprechungsanker](#aktuelle-rechtsprechungsanker)
- [Normenkarte](#normenkarte)
- [20-Prüfschleifen](#20-prüfschleifen)
- [Pflicht-Prüfblock](#pflicht-prüfblock)
- [Workflow](#workflow)
- [Antwortformate](#antwortformate)
- [Teil A — MaBV und Zahlungen](#teil-a--mabv-und-zahlungen)
- [Teil B — AGB-Klauselkontrolle](#teil-b--agb-klauselkontrolle)
- [Teil C — Baubeschreibung und Bausoll](#teil-c--baubeschreibung-und-bausoll)
- [Teil D — Abnahme und Mängelrechte](#teil-d--abnahme-und-mängelrechte)
- [Teil E — Teilungserklärung, WEG, Gemeinschaftsordnung](#teil-e--teilungserklärung-weg-gemeinschaftsordnung)
- [Teil F — Eigentumsschutz und Insolvenz](#teil-f--eigentumsschutz-und-insolvenz)
- [Teil G — Verhandlungspaket](#teil-g--verhandlungspaket)
- [Teil H — Streit, Rücktritt, Klage](#teil-h--streit-rücktritt-klage)
- [Teil I — Nichtigkeit, § 306 BGB, Notar](#teil-i--nichtigkeit--306-bgb-notar)
- [Teil J — Realfall-Pattern und Testakte](#teil-j--realfall-pattern-und-testakte)
- [Teil K — Vertiefte Dogmatik](#teil-k--vertiefte-dogmatik)
- [Teil L — Drei-Dokumente-Paket](#teil-l--drei-dokumente-paket)
- [Bug-Hunt vor Ausgabe](#bug-hunt-vor-ausgabe)

## Sofortstart

Sobald ein Bauträgervertrag, Notarentwurf, Auszug, PDF, OCR-Text oder Foto kommt, beginnt die Analyse ohne Rückfragenkaskade.

Rückfragen sind nur zulässig, wenn eine Antwort ohne die Information objektiv falsch wäre. Dann höchstens eine gebündelte Rückfrage am Ende.

Pflichtreihenfolge:

1. Vertragsstatus und Rolle feststellen: Entwurf, beurkundet, Bauphase, Abnahme, Streit.
2. Verbraucherstatus prüfen: natürliche Person, private Vermögensverwaltung, Eigennutzung, private Kapitalanlage. Bei Gewerbeeinheit nicht vorschnell Unternehmerstatus annehmen.
3. Pflicht-Prüfblock zuerst ausgeben.
4. Klauselmatrix erstellen: Originalwortlaut, Risiko, Rechtsanker, Gegenargument, Antwort, Ampel, gewünschte Änderung.
5. MaBV-Zahlungsmodell gesondert rechnen.
6. Rechtsprechung nur mit zulässiger Fundstelle nennen.
7. Verhandlungspaket mit konkreten Änderungsformulierungen liefern.
8. Wenn ein vollständiger oder im Wesentlichen vollständiger Vertrag vorliegt: Drei-Dokumente-Paket nach Teil L erzeugen, sofern der Nutzer nicht ausdrücklich nur einen Schnellscan will.

## Aktuelle Rechtsprechungsanker

Diese Anker sind besonders stark, weil sie direkt Bauträgerrecht, AGB-Kontrolle oder Notarabwicklung betreffen. Vor Ausgabe die Links live prüfen.

| Thema | Harte Fundstelle | Kernaussage für Verbraucher | Einsatz im Vertrag |
| --- | --- | --- | --- |
| Abnahme Gemeinschaftseigentum durch Erwerbervertreter | BGH, Urteil vom 26.03.2026 - VII ZR 68/24, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR__68-24.pdf?__blob=publicationFile&v=1 | Eine Bauträgerklausel, nach der drei aus der Erwerbermitte zu wählende Vertreter das Gemeinschaftseigentum abnehmen, ist unwirksam, wenn dem einzelnen Erwerber nicht das Recht bleibt, die Abnahmefähigkeit selbst zu prüfen und selbst abzunehmen. Kostenvorschussansprüche können in diesem Fall bis zur 30-Jahres-Obergrenze durchsetzbar bleiben. | Jede Vertreter-, Erstverwaltungs- oder Mehrheitsabnahme streng prüfen. Erwerberrecht auf eigene Prüfung ausdrücklich sichern. |
| Abnahme Gemeinschaftseigentum durch Sachverständigen | BGH, Urteil vom 26.03.2026 - VII ZR 108/24, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR_108-24.pdf?__blob=publicationFile&v=1 | Eine AGB-Klausel, die die Abnahme des Gemeinschaftseigentums einem vereidigten Sachverständigen überträgt, ohne dem Erwerber eigene Prüf- und Abnahmerechte zu lassen, benachteiligt Erwerber unangemessen. Ohne wirksame Abnahme bleibt der Bauträger beweisbelastet; 30-Jahres-Obergrenze. | Gegen Klauseln `Sachverständiger nimmt bindend ab`, auch wenn WEG ihn wählt. |
| Schlussrate und vollständige Fertigstellung | BGH, Urteil vom 22.04.2026 - VII ZR 88/25, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2025/VII_ZR__88-25.pdf?__blob=publicationFile&v=1 | Die Formulierung `nach vollständiger Fertigstellung` ist im Bauträgervertrag auszulegen. Wenn der Vertrag den Bauträger verpflichtet, im Abnahmeprotokoll aufgeführte Mängel/Restarbeiten zu beseitigen, kann die Schlussrate bis dahin nicht fällig sein. Nicht bloß Zug-um-Zug-Verurteilung. | Schlussrate nicht freigeben, wenn protokollierte Mängel/Restarbeiten offen sind. |
| Änderung der Teilungserklärung/Gemeinschaftsordnung | BGH, Urteil vom 23.01.2026 - V ZR 91/25, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2025/V_ZR__91-25.pdf?__blob=publicationFile&v=1 | AGB-Pflichten des Verbrauchers, späteren Änderungen der Teilungserklärung durch den Bauträger zuzustimmen, sind nach § 308 Nr. 4 BGB unwirksam, wenn die Klausel keine im Einzelnen benannten triftigen Gründe erkennen lässt. Aus § 242 BGB folgt dann regelmäßig keine Ersatz-Zustimmungspflicht. Private Vermögensverwaltung kann Verbraucherstatus bleiben, auch bei Gewerbeeinheit. | Weite Vollmachten und Zustimmungspflichten zu Teilungserklärung, Gemeinschaftsordnung, Untergemeinschaften, Nutzungsänderungen rot markieren. |
| Abnahme durch bauträgernahe Tochtergesellschaft | BGH, Urteil vom 09.11.2023 - VII ZR 241/22, DeJure: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=VII+ZR+241%2F22&Datum=09.11.2023&Gericht=BGH | Abnahmeklauseln, die eine im Lager des Bauträgers stehende Person/Gesellschaft für die Abnahme des Gemeinschaftseigentums einsetzen, sind AGB-rechtlich hoch angreifbar. Die GdWE kann Mängelrechte gebündelt geltend machen; der Verwender kann sich nicht auf die Folgen seiner unwirksamen Klausel berufen. | Gegen Tochtergesellschaft, Erstverwalter, Projektsteuerer, `neutralen` Bauträgerdienstleister. |
| Notaranderkonto bei Bauträgerabwicklung | BGH, Beschluss vom 02.08.2023 - VII ZB 28/20, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2020/VII_ZB__28-20.pdf?__blob=publicationFile&v=1 | Notaranderkonto ist kein einfacher Ersatz für MaBV-Schutz. § 57 Abs. 2 BeurkG richtet sich an den Notar; ein fehlendes Sicherungsinteresse macht die zivilrechtliche Verwahrungsabrede nicht automatisch unwirksam. Bei Abtretung/Pfändung kann der Auszahlungsanspruch gegen den Notar miterfasst sein. | Nicht pauschal `Notaranderkonto löst alles`; Verwahrungsanweisung, MaBV, Fälligkeit und Empfangsberechtigung getrennt prüfen. |

## Normenkarte

| Norm | Harte Aussage |
| --- | --- |
| § 650u BGB | Bauträgervertrag kombiniert Errichtung/Umbau mit Eigentums- oder Erbbaurechtsübertragung. Für den Bau gelten Bauvertragsnormen, soweit § 650u Abs. 2 nichts ausschließt; für die Eigentumsübertragung Kaufrecht. |
| § 650u Abs. 2 BGB | Nicht anwendbar: §§ 648, 648a, 650b bis 650e, § 650k Abs. 1, §§ 650l und 650m Abs. 1. Nicht ausgeschlossen sind § 650j, § 650k Abs. 2/3, § 650m Abs. 2, § 650n. |
| § 650v BGB | Abschlagszahlungen kann der Bauträger nur verlangen, soweit sie nach einer Verordnung aufgrund Art. 244 EGBGB vereinbart sind. Praktisch: MaBV. |
| § 650m Abs. 2 BGB | Verbraucher erhält bei erster Abschlagszahlung 5 % Sicherheit für rechtzeitige Herstellung ohne wesentliche Mängel. Bei Bauträgern nicht durch § 650u Abs. 2 ausgeschlossen. |
| § 650m Abs. 1 BGB | 90 %-Deckel für Abschläge nach § 632a; bei Bauträgervertrag durch § 650u Abs. 2 ausgeschlossen. Nicht fälschlich als Bauträger-Hauptregel nutzen. |
| § 650j BGB | Baubeschreibungspflicht nach Art. 249 EGBGB. Bei Bauträgervertrag nicht durch § 650u Abs. 2 ausgeschlossen. |
| § 650k Abs. 2/3 BGB | Unklare oder unvollständige Baubeschreibung wird unter allen Umständen ausgelegt; Zweifel gehen zulasten des Unternehmers. Fertigstellungsdatum oder Bauzeit muss verbindlich sein. |
| § 650k Abs. 1 BGB | Wird durch § 650u Abs. 2 ausgeschlossen. Nicht behaupten, die vorvertragliche Baubeschreibung werde bei Bauträgern automatisch über Abs. 1 Vertragsinhalt. Vertragsinhalt muss über Beurkundung/Einbeziehung gesichert werden. |
| § 650n BGB | Planungs- und Nachweisunterlagen vor Ausführung und spätestens mit Fertigstellung; auch bei Finanzierung/KfW/GEG-Nachweisen relevant. |
| § 309 Nr. 12 BGB | Beweislaständerungen zulasten des Kunden, insbesondere Verantwortungsbereich des Verwenders oder pauschale Tatsachenbestätigungen, sind unwirksam. Ausnahme für gesondert unterschriebene Empfangsbekenntnisse. |
| § 309 Nr. 15 BGB | Werkvertrags-AGB sind unwirksam, wenn sie wesentlich überhöhte Abschlagszahlungen erlauben oder die 5 %-Sicherheit nach § 650m Abs. 2 nicht/zu niedrig leisten lassen. |
| § 3 MaBV | Vor jeder Geldannahme: wirksamer Vertrag ohne vertragliche Rücktrittsrechte des Bauträgers, Vormerkung, Freistellung, Baugenehmigung/Bestätigung. Danach nur bis zu sieben Teilbeträge nach Bauablauf. |
| § 7 MaBV | Alternative Sicherung für alle Ansprüche auf Rückgewähr/Auszahlung; bei Eigentums-/Erbbaurechtsübertragung aufrechtzuerhalten bis § 3 Abs. 1 erfüllt ist und das Objekt vollständig fertiggestellt ist. Keine gesetzliche Formel `Vertragssumme plus 5 %`. |
| § 12 MaBV | Abweichungen zulasten des Auftraggebers von §§ 2 bis 8 MaBV sind unzulässig. |
| § 306 BGB | Regelfolge unwirksamer AGB: Klausel fällt weg, Vertrag bleibt bestehen, Gesetz tritt an die Stelle. Nicht vorschnell Gesamtnichtigkeit behaupten. |
| § 311b BGB | Grundstücks-/Bauträgervertrag braucht notarielle Beurkundung. Nicht mitbeurkundete Kernbestandteile können Formrisiken auslösen. |

## 20-Prüfschleifen

Bei jeder Vollanalyse durchlaufe diese Schleifen intern. Im Ergebnis nur die relevanten Befunde ausgeben.

1. Vertragsart: echter Bauträgervertrag oder reiner Kauf-/Werkvertrag?
2. Verbraucherstatus: Eigennutzung, private Kapitalanlage, Vermögensverwaltung, Unternehmereigenschaft?
3. Beurkundung: alle wesentlichen Anlagen mitbeurkundet?
4. Zwei-Wochen-Verbraucherschutz im Beurkundungsverfahren plausibel eingehalten?
5. § 3 Abs. 1 MaBV vor erster Zahlung vollständig erfüllt?
6. Ratenplan: sieben Teilbeträge und Prozentsätze korrekt?
7. § 7 MaBV: falls Bürgschaft, alle Rückgewähr-/Auszahlungsansprüche abgesichert?
8. 5 %-Sicherheit nach § 650m Abs. 2 BGB vorhanden, nicht abbedungen?
9. § 309 Nr. 12: keine Beweislastumkehr, keine pauschalen Tatsachenbestätigungen?
10. § 309 Nr. 15: keine überhöhten Abschläge, keine reduzierte Sicherheit?
11. Baubeschreibung: § 650j, § 650k Abs. 2/3, Art. 249 EGBGB, Bausoll konkret?
12. Fertigstellungstermin: verbindlich, nicht beliebig verschiebbar?
13. Bauänderungen: nur triftige, konkret benannte Gründe, kein freies Leistungsänderungsrecht?
14. Teilungserklärung/Gemeinschaftsordnung: keine pauschalen Änderungsvollmachten?
15. Abnahme Sondereigentum: persönlich, Protokoll, Vorbehalte, keine Fiktion durch Schlüssel?
16. Abnahme Gemeinschaftseigentum: keine bauträgernahe Person, keine bindende Fremdabnahme ohne Eigenrecht?
17. Schlussrate: vollständige Fertigstellung, protokollierte Mängel, Zurückbehaltung?
18. Vormerkung/Lastenfreistellung: keine Löschungsdruckmittel, Rang sauber?
19. Verjährung/Mängelrechte: fünf Jahre Bauwerk, keine Ausschlussfristen?
20. Verhandlungsfähigkeit: jedes 🔴 mit gesetzlicher Grundlage, Fallanker, Gegenargument und gewünschter Neufassung?

## Pflicht-Prüfblock

Dieser Block steht in jeder Vollanalyse ganz oben.

| Pflichtpunkt | Prüfung | Harte Folge |
| --- | --- | --- |
| 5 %-Sicherheit | Enthält der Vertrag eine echte Sicherheit nach § 650m Abs. 2 BGB bei der ersten Abschlagszahlung? Wird sie nicht durch Kosten, Vorleistung oder Verzicht entwertet? | Fehlt oder reduziert: 🔴, zusätzlich § 309 Nr. 15 lit. b BGB prüfen. |
| Beweislast | Verlagert eine Klausel Verantwortungsbereich des Bauträgers auf den Erwerber? | 🔴 nach § 309 Nr. 12 lit. a BGB. |
| Tatsachenbestätigung | Bestätigt der Erwerber pauschal Erhalt, Kenntnis, Prüfung, Belehrung, Vollständigkeit oder Risikoaufklärung? | 🔴 nach § 309 Nr. 12 lit. b BGB, außer gesondertes Empfangsbekenntnis. |
| MaBV-Fälligkeit | Verlangt der Bauträger Geld vor § 3 Abs. 1 MaBV oder außerhalb § 3 Abs. 2/§ 7 MaBV? | 🔴; Zahlung verweigern, Notar/Bauträger korrigieren lassen. |
| Abnahme Gemeinschaftseigentum | Wird das Recht zur eigenen Prüfung/Abnahme entzogen oder bauträgernah gebündelt? | 🔴 nach aktueller BGH-Linie 2023/2026. |
| Schlussrate | Wird Schlussrate trotz offener protokollierter Mängel oder Restarbeiten fällig gestellt? | 🔴/🟠; BGH VII ZR 88/25 nutzen. |
| Teilungserklärung | Darf Bauträger nachträglich beliebig ändern oder Zustimmung verlangen? | 🔴, § 308 Nr. 4 BGB und BGH V ZR 91/25. |
| Bausoll | Baubeschreibung konkret, vollständig, datiert und mitbeurkundet? | Lücken: 🔴/🟠; Zweifel zulasten Unternehmer (§ 650k Abs. 2 BGB). |

## Workflow

### 1 — Intake

Erfasse knapp:

| Punkt | Inhalt |
| --- | --- |
| Rolle | Erwerber, Anwalt, Verbraucherzentrale, WEG/GdWE, Notar-/Bauträger-Gegenprüfung |
| Status | Entwurf, Beurkundung terminiert, beurkundet, Bauphase, Abnahme, Mängelstreit, Insolvenz |
| Objekt | Wohnung, Teileigentum, Reihenhaus, Sanierung, Erbbaurecht |
| Preis | Gesamtpreis, Sonderwünsche, Finanzierungs-/KfW-Bezug |
| Unterlagen | Vertrag, Anlagen, Teilungserklärung, Gemeinschaftsordnung, Baubeschreibung, Freistellung, Ratenplan |
| Eilbedarf | Beurkundungstermin, Zahlungsfrist, Abnahmefrist, Klagefrist |

### 2 — Quellenrefresh

Vor einer finalen Ausgabe:

- Normen auf `gesetze-im-internet.de` prüfen, wenn Normzitat tragend ist.
- Rechtsprechung aus der Ankerliste öffnen oder über DeJure/OpenJur/offizielle Gerichtsseite verifizieren.
- Keine `Rn.` nennen, wenn sie nicht im geöffneten Volltext geprüft wurde.

### 3 — Vertragsart und Anwendbarkeit

Ein Bauträgervertrag liegt vor, wenn der Unternehmer Bauerrichtung/Umbau schuldet und zugleich Eigentum/Erbbaurecht übertragen muss (§ 650u Abs. 1 BGB).

Wenn kein Bauträgervertrag:

- Reiner Grundstückskauf: Kaufrecht/§ 311b BGB, nicht MaBV-Ratenplan.
- Reiner Bauvertrag auf eigenem Grundstück: Verbraucherbauvertrag/Bauvertrag, nicht Eigentumsübertragung.
- Sanierungsobjekt mit Aufteilung: Bauträgerrecht, wenn Erwerb und Herstellung/Sanierung verbunden sind.

### 4 — Pflichtbausteine

| Baustein | Soll | Ampel bei Fehlen |
| --- | --- | --- |
| Notarielle Beurkundung | Urkunde mit allen wesentlichen Leistungspflichten | 🔴 |
| Exakte Objektbezeichnung | Grundbuch, Flurstück, Wohnung/Teileigentum, Sondernutzungsrechte | 🔴 |
| Teilungserklärung/Gemeinschaftsordnung | beurkundet oder eindeutig einbezogen | 🔴/🟠 |
| Baubeschreibung | konkret, datiert, mitbeurkundet/eindeutig einbezogen | 🔴 |
| Fertigstellung | Datum oder bestimmbarer Zeitraum | 🔴 |
| Vormerkung | vor Zahlung an vereinbarter Rangstelle | 🔴 |
| Freistellung | auch für Nichtvollendung gesichert | 🔴 |
| Ratenplan/Sicherheit | § 3 oder § 7 MaBV | 🔴 |
| Abnahme | persönliche Rechte, Protokoll, Vorbehalte | 🔴/🟠 |
| Mängelrechte | gesetzlich, fünf Jahre Bauwerk | 🔴 bei Verkürzung |

### 5 — Klauselmatrix

Nutze diese Spalten:

| Originalwortlaut | Decodierung | Risiko | Rechtsanker | Bauträger-/Notarargument | Antwort | Änderung | Ampel |
| --- | --- | --- | --- | --- | --- | --- | --- |

Die Antwort muss streitfest sein: Gesetz zuerst, dann aktueller BGH-Anker, dann konkrete Klauselwirkung.

### 6 — Verhandlungsfassung

Für jedes 🔴:

1. Streichung oder Neufassung formulieren.
2. Kurzbegründung in zwei bis vier Sätzen.
3. Dringlichkeit: `Muss vor Beurkundung`, `Kann nachverhandelt werden`, `Streitfallposition`.

### 7 — Ergebnisbewertung

Gesamteinschätzung:

- `beurkundungsfähig nach Korrektur einzelner Punkte`
- `nur nach wesentlicher Überarbeitung beurkundungsfähig`
- `nicht beurkunden`
- `bei bereits beurkundetem Vertrag: AGB-Unwirksamkeit/Einbehalt/Klage prüfen`

## Antwortformate

### Schnellscan

```text
Kurzbild
- Vertragsart:
- Verbraucherstatus:
- Pflicht-Prüfblock: 🔴 x / 🟠 y / 🟢 z
- MaBV-Fälligkeit:
- Haupthebel:
- Sofortmaßnahme:
```

### Vollanalyse

```text
1. Pflicht-Prüfblock
2. Quellenstand
3. Vertragsart und Verbraucherstatus
4. MaBV-Zahlungsprüfung
5. AGB-Klauselmatrix
6. Baubeschreibung/Bausoll
7. Abnahme, Schlussrate, Mängelrechte
8. Eigentumsschutz/Insolvenz
9. Verhandlungspaket
10. Restfragen
```

### Streitstellen-Tabelle

```text
| Klausel | Risiko | Harte Grundlage | Erwartetes Gegenargument | Antwort | Gewünschte Fassung | Ampel |
```

### Regelausgabe

Bei vollständigem oder fast vollständigem Vertrag ist die Regelausgabe das **Drei-Dokumente-Paket**:

1. Mandantenanschreiben in einfacher Sprache.
2. Ausführliches Gutachten.
3. Schreiben an Bauträger/Notar.

Alle drei Dokumente beruhen auf denselben Befunden. Was im Gutachten 🔴 ist, muss im Schreiben an Bauträger/Notar auftauchen; was im Mandantenanschreiben als Hauptrisiko steht, muss im Gutachten belegt sein.

## Teil A — MaBV und Zahlungen

### A.1 — § 3 Abs. 1 MaBV vor erster Zahlung

Der Bauträger darf Vermögenswerte erst entgegennehmen oder sich zu deren Verwendung ermächtigen lassen, wenn die Voraussetzungen kumulativ erfüllt sind.

| Voraussetzung | Verbrauchercheck | Befund |
| --- | --- | --- |
| Wirksamer Vertrag und Genehmigungen | Notarmitteilung vorhanden; keine vertraglichen Rücktrittsrechte des Bauträgers | Fehlt: 🔴 |
| Vormerkung | Anspruch auf Eigentum/Erbbaurecht an vereinbarter Rangstelle eingetragen; bei WEG auch Begründung des Wohnungs-/Teileigentums vollzogen | Fehlt/Nachrang: 🔴 |
| Freistellung | Nicht zu übernehmende Grundpfandrechte müssen auch bei Nichtvollendung freigestellt oder Zahlungen zurückgeführt werden | Lücke: 🔴 |
| Baugenehmigung/Bestätigung | Genehmigung oder gesetzliche/behördliche Bestätigung; bei Eigenbestätigung Monatsfrist beachten | Unklar: 🟠/🔴 |

### A.2 — § 3 Abs. 2 MaBV: bis zu sieben Teilbeträge

Nicht schreiben: `dreizehn gesetzliche Raten`. Richtig ist: Der Bauträger darf in **bis zu sieben Teilbeträgen** abrechnen. Diese Teilbeträge können aus den gesetzlichen Vomhundertsätzen zusammengesetzt werden.

| Baustein | Gesetzlicher Anteil | Kontrollwert bei Grundstückserwerb (30 % + 70 %) |
| --- | --- | --- |
| Beginn Erdarbeiten | 30 % der Vertragssumme; bei Erbbaurecht 20 % | 30,0 % |
| Rohbau einschließlich Zimmerer | 40 % der restlichen Vertragssumme | 28,0 % |
| Dachflächen/Dachrinnen | 8 % der restlichen Vertragssumme | 5,6 % |
| Rohinstallation Heizung | 3 % der restlichen Vertragssumme | 2,1 % |
| Rohinstallation Sanitär | 3 % der restlichen Vertragssumme | 2,1 % |
| Rohinstallation Elektro | 3 % der restlichen Vertragssumme | 2,1 % |
| Fenster einschließlich Verglasung | 10 % der restlichen Vertragssumme | 7,0 % |
| Innenputz ohne Beiputz | 6 % der restlichen Vertragssumme | 4,2 % |
| Estrich | 3 % der restlichen Vertragssumme | 2,1 % |
| Fliesen Sanitär | 4 % der restlichen Vertragssumme | 2,8 % |
| Bezugsfertigkeit Zug um Zug gegen Besitz | 12 % der restlichen Vertragssumme | 8,4 % |
| Fassade | 3 % der restlichen Vertragssumme | 2,1 % |
| Vollständige Fertigstellung | 5 % der restlichen Vertragssumme | 3,5 % |

Bei Erbbaurecht sind die Kontrollwerte anders, weil die erste Rate 20 % beträgt und die restliche Vertragssumme 80 % ausmacht.

### A.3 — Typische MaBV-Verstöße

| Klausel/Verhalten | Problem | Antwort |
| --- | --- | --- |
| Erste Rate bei Beurkundung | § 3 Abs. 1 MaBV noch nicht erfüllt | Zahlung verweigern, Notarbestätigung/Vormerkung/Freistellung verlangen. |
| Mehr als sieben Teilbeträge | § 3 Abs. 2 MaBV sagt bis zu sieben | Zusammenfassung verlangen. |
| Pauschal `nach Baufortschritt` | Fälligkeit nicht objektiv prüfbar | Konkrete MaBV-Baustufe verlangen. |
| Schlussrate trotz offener Protokollmängel | `vollständige Fertigstellung` fraglich | BGH VII ZR 88/25 einsetzen. |
| Sonderwünsche sofort fällig | Umgehungsrisiko, wenn bauwerksbezogen und vor Leistung | Sonderwünsche nach Leistung/Abnahme oder Sicherung regeln. |
| Raten über gesetzlichem Kontrollwert | § 650v BGB i. V. m. MaBV | Korrektur auf gesetzliche Prozentsätze. |

### A.4 — § 7 MaBV-Sicherheit

§ 7 MaBV ist keine beliebige Bankbürgschaft und kein Marketingersatz. Gesichert werden müssen alle etwaigen Ansprüche des Auftraggebers auf Rückgewähr oder Auszahlung seiner Vermögenswerte. Bei Eigentums-/Erbbaurechtsübertragung ist die Sicherheit aufrechtzuerhalten, bis § 3 Abs. 1 MaBV erfüllt ist und das Vertragsobjekt vollständig fertiggestellt ist.

| Prüfpunkt | Soll | Befund |
| --- | --- | --- |
| Sicherungszweck | alle Rückgewähr-/Auszahlungsansprüche | 🔴 wenn nur Teilbetrag |
| Dauer | bis § 3 Abs. 1 erfüllt und vollständige Fertigstellung | 🔴 wenn befristet/kündbar |
| Bürge | im Geltungsbereich befugtes Kreditinstitut/Kreditversicherer | 🟠 bei Auslands-/Konzernbürge |
| Original | vor Zahlung beim Erwerber oder sicherer Zugriff | 🟠/🔴 |
| Austausch § 3/§ 7 | klar geregelt | 🟠 wenn doppeldeutig |

### A.5 — Notaranderkonto

Ein Notaranderkonto ist kein Verbraucherschutz-Automatismus.

Nutze BGH VII ZB 28/20:

- Prüfe öffentlich-rechtliche Verwahrungsanweisung an den Notar und zivilrechtliche Verwahrungsvereinbarung getrennt.
- Fehlendes Sicherungsinteresse kann notarielle Amtspflichten betreffen, macht die zivilrechtliche Abrede aber nicht automatisch unwirksam.
- Bei Pfändung/Abtretung der Kaufpreisforderung kann auch der Auszahlungsanspruch gegen den Notar erfasst sein.
- Deshalb: Fälligkeit, MaBV, Einbehalte, Abtretungen, Pfändungen und Auszahlungsanweisung sauber auseinanderhalten.

## Teil B — AGB-Klauselkontrolle

### B.1 — Grundsätze

Notarielle Beurkundung schützt nicht vor AGB-Kontrolle. Wenn der Bauträger vorformuliert und für mehrere Erwerber verwendet, sind §§ 305 ff. BGB zentral.

Regelfolgen:

- § 305c Abs. 2 BGB: Zweifel bei Auslegung gehen zulasten des Verwenders.
- § 307 BGB: unangemessene Benachteiligung/Intransparenz.
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit, wichtig bei Änderungsvorbehalten.
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit, wichtig Nr. 2, 3, 12, 15.
- § 306 BGB: unwirksame Klausel entfällt; Gesetz tritt ein.

### B.2 — Klauselkatalog mit Gegenargumenten

| Klauseltyp | Angriff | Erwartetes Gegenargument | Harte Antwort | Ampel |
| --- | --- | --- | --- | --- |
| Abnahme GE durch Vertreter aus Erwerberkreis | § 307 BGB; BGH VII ZR 68/24 | `Die Erwerber wählen doch selbst.` | Wahl genügt nicht, wenn der einzelne Erwerber sein eigenes Prüf- und Abnahmerecht verliert. | 🔴 |
| Abnahme GE durch Sachverständigen | § 307 BGB; BGH VII ZR 108/24 | `Neutraler Sachverständiger ist besser.` | Neutralität ersetzt nicht das Bestellerrecht auf eigene Prüfung und Erklärung. | 🔴 |
| Abnahme durch Tochter/Erstverwalter/Projektpartner | § 307 BGB; BGH VII ZR 241/22 | `Organisatorisch nötig.` | Bauträgernahes Lager und Entzug eigener Abnahmerechte sind nicht organisatorisch heilbar. | 🔴 |
| Nachzüglerklausel `Abnahme ist erfolgt` | § 307/§ 305c BGB; BGH VII ZR 68/24 | `Das Objekt war schon abgenommen.` | Erwerber kann nicht formularmäßig an eine frühere, fremde und ggf. unwirksame Abnahme gebunden werden. | 🔴 |
| Schlussrate ohne Mängeleinbehalt | § 641 Abs. 3 BGB; BGH VII ZR 88/25 | `Mängel werden Zug um Zug beseitigt.` | Bei Vertragswortlaut `vollständige Fertigstellung` und protokollierten Restmängeln kann schon Fälligkeit fehlen. | 🔴 |
| Schlüssel nur gegen vollständige Zahlung | § 307, § 641 Abs. 3 BGB | `Ohne Zahlung kein Besitz.` | Zahlungspflicht kann nicht das gesetzliche Zurückbehaltungsrecht bei Mängeln entwerten. | 🔴 |
| Vormerkungslöschung bei einseitiger Verzugsmitteilung | § 307 BGB, Eigentumssicherung | `Nur für Zahlungsverzug.` | Die Vormerkung ist Kernschutz gegen Insolvenz; einseitiger Druckmechanismus ist unverhältnismäßig. | 🔴 |
| Pauschale Änderung Teilungserklärung | § 308 Nr. 4 BGB; BGH V ZR 91/25 | `Bauprojekt braucht Flexibilität.` | Flexibilität nur mit im Einzelnen benannten triftigen Gründen; § 242 ersetzt unwirksame AGB regelmäßig nicht. | 🔴 |
| Pauschale Bauänderungen `gleichwertig` | § 308 Nr. 4, § 307 BGB | `Technische Anpassungen sind üblich.` | Nur konkret benannte technische Gründe, keine Qualitäts-/Flächen-/Nutzungsverschlechterung, Informationspflicht. | 🟠/🔴 |
| Beweislast für Mängel/Verzug beim Erwerber vor Abnahme | § 309 Nr. 12 lit. a BGB | `Der Erwerber behauptet den Mangel.` | Umstände im Verantwortungsbereich des Bauträgers dürfen nicht auf den Erwerber verlagert werden. | 🔴 |
| Bestätigung `alles erhalten/geprüft/verstanden` | § 309 Nr. 12 lit. b BGB | `Nur Dokumentation.` | Pauschale Tatsachenbestätigung ist unwirksam; nur gesondertes Empfangsbekenntnis ist privilegiert. | 🔴 |
| 5 %-Sicherheit fehlt oder ist reduziert | § 650m Abs. 2, § 309 Nr. 15 lit. b BGB | `MaBV schützt ausreichend.` | § 650u Abs. 2 schließt § 650m Abs. 2 nicht aus; § 309 Nr. 15 schützt die Sicherheit zusätzlich. | 🔴 |
| Verjährung unter fünf Jahre | § 634a Abs. 1 Nr. 2 BGB, § 307 BGB | `Üblich am Markt.` | Marktüblichkeit ersetzt nicht gesetzliche Bauwerksverjährung. | 🔴 |
| Mängelanzeigefrist als Ausschlussfrist | § 307 BGB | `Schnelle Klärung nötig.` | Obliegenheit zur Anzeige darf Mängelrechte nicht ausschließen. | 🔴 |
| Aufrechnung nur mit anerkannten/rechtskräftigen Forderungen | § 309 Nr. 3 BGB | `Standardklausel.` | Nur zulässig, wenn unbestrittene und rechtskräftige Forderungen ausgenommen sind; sonst 🔴. | 🟠/🔴 |
| Gerichtsstand am Sitz Bauträger | §§ 38, 29c ZPO, § 307 BGB | `Projektstandort ist sachnah.` | Verbrauchergerichtsstände dürfen nicht formularmäßig entzogen werden. | 🔴 |
| Abtretungsverbot für Mängelrechte | § 307 BGB, WEG/GdWE-Kontext | `Bündelung verhindern.` | Mängelrechte am Gemeinschaftseigentum müssen praktisch durchsetzbar bleiben. | 🟠/🔴 |
| Bemusterungsmehrkosten pauschal | § 307 Abs. 1 S. 2 BGB | `Verwaltungsaufwand.` | Kosten müssen kalkulierbar, transparent und sachlich begründet sein. | 🟠/🔴 |

### B.3 — Ausgaberegel bei AGB

Schreibe nicht nur `unwirksam`. Schreibe:

```text
Die Klausel ist als AGB angreifbar, weil sie [konkretes Recht] entzieht. Gesetzlicher Ausgangspunkt ist [Norm]. Die aktuelle BGH-Linie zu [Fallgruppe] stützt das, weil [Kernaussage]. Das erwartbare Gegenargument [x] trägt nicht, weil [juristische Antwort]. Gewünschte Fassung: [...]
```

## Teil C — Baubeschreibung und Bausoll

### C.1 — Leitgedanke

Die Baubeschreibung ist der wirtschaftliche Kern. Wer nur `hochwertig`, `marktüblich`, `anerkannten Regeln der Technik entsprechend` oder `nach Bemusterung` bekommt, hat kein belastbares Bausoll.

Bei Bauträgern:

- § 650j BGB nicht ausgeschlossen.
- § 650k Abs. 2/3 BGB nicht ausgeschlossen.
- § 650k Abs. 1 BGB ausgeschlossen; daher vorvertragliche Unterlagen nicht unkritisch als automatisch einbezogen darstellen.
- Wegen § 311b BGB müssen wesentliche Leistungsinhalte beurkundet oder eindeutig einbezogen sein.

### C.2 — Pflichtmatrix

| Punkt | Soll | Risiko |
| --- | --- | --- |
| Version | datiert, Seitenzahl, Anlagenbezeichnung | 🔴 bei `aktuelle Fassung` |
| Mitbeurkundung | Urkunde/Anlage eindeutig Bestandteil | 🔴 bei loser Übergabe |
| Wohnfläche | Grundlage WoFlV/DIN 277, Toleranz, Raumliste | 🔴 wenn fehlt |
| Energiestandard | GEG/KfW/Effizienzhaus konkret | 🔴 bei `gesetzlicher Standard` |
| Bauweise | Tragwerk, Fassade, Dach, Dämmung, Schallschutz | 🟠/🔴 |
| Haustechnik | Heizung, Warmwasser, Lüftung, Elektro, PV, Smart-Home | 🟠 |
| Innenausbau | Böden, Türen, Fliesen, Sanitär, Malerarbeiten | 🟠/🔴 |
| Außenanlagen | Terrasse, Wege, Garten, Einfriedung, Stellplätze | 🟠/🔴 |
| Sondernutzungsrechte | Lageplan, Größe, Nutzungsinhalt | 🔴 |
| Fertigstellung | Datum oder bestimmbarer Zeitraum | 🔴 |
| Unterlagen | Statik, Energieausweis, Revisionsunterlagen, GEG/KfW-Nachweise | 🟠/🔴 |

### C.3 — Auslegung

Wenn Baubeschreibung unklar oder unvollständig ist:

1. Alle vertragsbegleitenden Umstände sammeln: Prospekt, Exposé, Verkaufsgespräch, Pläne, Visualisierungen, Bemusterung, Preisklasse.
2. Komfort- und Qualitätsstandard aus dem Gesamtvertrag bestimmen.
3. Zweifel zulasten des Bauträgers (§ 650k Abs. 2 BGB, § 305c Abs. 2 BGB).
4. Für Verhandlung konkrete Mindestqualität formulieren.

### C.4 — Typische Formulierungen

| Klausel | Befund |
| --- | --- |
| `Ausstattung mittlerer Art und Güte` | Zu unkonkret, wenn Kerngewerke nicht spezifiziert. |
| `Markenfabrikat oder gleichwertig` | Nur tragfähig mit Mindestparametern. |
| `Änderungen aus technischen Gründen vorbehalten` | Nur mit triftigen Gründen, Informationspflicht, keiner Wertminderung. |
| `Bemusterung im Standard des Bauträgers` | Budget und Auswahlumfang verlangen. |
| `Wohnfläche ca.` ohne Berechnungsgrundlage | 🔴/🟠; Minderungs-/Anpassungsmechanik verlangen. |

## Teil D — Abnahme und Mängelrechte

### D.1 — Warum Abnahme zentral ist

Abnahme betrifft:

- Fälligkeit.
- Gefahrübergang.
- Beweislast.
- Beginn der fünfjährigen Verjährung bei Bauwerken.
- Wechsel vom Erfüllungs- in das Gewährleistungsregime.

### D.2 — Sondereigentum

| Soll | Befund |
| --- | --- |
| Persönlicher Termin mit Protokoll | 🟢 |
| Mängel/Restarbeiten konkret vorbehalten | 🟢 |
| Abnahme durch Schlüsselübergabe fingiert | 🔴 |
| Abnahme trotz nicht prüfbarer Gewerke | 🟠/🔴 |
| Verzicht auf Vorbehalte | 🔴 |

### D.3 — Gemeinschaftseigentum

Leitsatz für die Analyse: Der einzelne Erwerber darf durch AGB nicht sein Recht verlieren, das Gemeinschaftseigentum selbst oder durch eine Person seines Vertrauens auf Abnahmefähigkeit zu prüfen und die Abnahme selbst zu erklären.

Kritische Klauseln:

- Erstverwalter nimmt ab.
- Bauträger benennt Sachverständigen.
- WEG-Mehrheit bindet alle Erwerber ohne individuelles Recht.
- Tochtergesellschaft/Projektpartner nimmt ab.
- Nachzügler bestätigt vergangene Abnahme.
- Kosten des bauträgernahen Abnehmers werden Erwerbern auferlegt.

### D.4 — Schlussrate

Nutze BGH VII ZR 88/25 offensiv und präzise.

Prüfung:

1. Was sagt die Ratenklausel: `vollständige Fertigstellung`, `bezugsfertig`, `abnahmereif`, `ohne wesentliche Mängel`?
2. Enthält das Abnahmeprotokoll Mängel oder Restarbeiten?
3. Verpflichtet sich der Bauträger zur Beseitigung/Ausführung?
4. Sind diese Punkte erledigt?
5. Falls nein: Schlussrate nicht fällig oder jedenfalls Einbehalt.

Nicht vorschnell nur § 641 Abs. 3 BGB anwenden. Zuerst Fälligkeit prüfen.

### D.5 — Mängelrechte

| Punkt | Verbraucherposition |
| --- | --- |
| Vor wirksamer Abnahme | Bauträger bleibt für mangelfreie Herstellung beweisbelastet. |
| Nach Abnahme mit Vorbehalt | Mängelrechte bleiben; Beweisfragen prüfen. |
| Verjährung | Bauwerk grundsätzlich fünf Jahre ab Abnahme. |
| Unwirksame Abnahmeklausel | Verwender kann sich nicht zu seinen Gunsten auf die eigene unwirksame Klausel berufen. |
| Kostenvorschuss | Bei Gemeinschaftseigentum kann GdWE/WEG-Bündelung relevant sein; aktuelle BGH-Linie prüfen. |

## Teil E — Teilungserklärung, WEG, Gemeinschaftsordnung

### E.1 — Kernrisiko

Bauträger behalten sich häufig vor, Teilungserklärung, Gemeinschaftsordnung, Untergemeinschaften, Nutzungsarten oder Flächenzuschnitte nachträglich zu ändern. Das ist für Verbraucher gefährlich, weil der wirtschaftliche Wert nicht nur an der Wohnung hängt, sondern an Stimmrechten, Kostenverteilung, Sondernutzungsrechten, Gewerbenutzung und Gemeinschaftsflächen.

### E.2 — Prüfmatrix

| Klausel | Risiko | Fundstelle |
| --- | --- | --- |
| `beliebig abändern` | 🔴 | BGH V ZR 91/25 |
| Zustimmungspflicht ohne triftige Gründe | 🔴 | § 308 Nr. 4 BGB |
| Vollmacht im Außenverhältnis unbeschränkt, Innenverhältnis weich | 🔴/🟠 | § 308 Nr. 4, § 307 |
| Änderung Nutzungszweck Gewerbe/Beherbergung | 🔴 | BGH V ZR 91/25 als Anker |
| Änderung Kostenverteilung | 🔴 | Wert-/Belastungsänderung |
| Verlegung/Verkleinerung Gemeinschaftsflächen | 🔴 | Kernleistung/WEG-Struktur |
| Technische Korrektur ohne Wertänderung | 🟢/🟠 | nur mit enger Begründung |

### E.3 — Gewünschte Fassung

```text
Änderungen der Teilungserklärung oder Gemeinschaftsordnung nach Vertragsschluss bedürfen der Zustimmung des Erwerbers. Eine Zustimmung kann nur verlangt werden, wenn ein im Vertrag einzeln benannter triftiger Grund vorliegt, die Änderung Inhalt, Umfang, Wert, Nutzbarkeit, Kostenlast, Stimmrechte, Sondernutzungsrechte und Gemeinschaftsflächen des Erwerbers nicht nachteilig berührt und dem Erwerber die Änderung in Textform mit Begründung nachgewiesen wird.
```

## Teil F — Eigentumsschutz und Insolvenz

### F.1 — Vormerkung

Die Auflassungsvormerkung ist der wichtigste dingliche Schutz. Ohne sie darf im § 3-Modell nicht gezahlt werden.

| Punkt | Soll |
| --- | --- |
| Anspruch | exakt das Vertragsobjekt, Sondernutzungen, Miteigentumsanteil |
| Rang | vereinbarte Rangstelle; keine vorrangigen, nicht übernommenen Belastungen ohne Freistellung |
| Löschung | nicht durch einseitige Erklärung des Bauträgers |
| Bedingung | keine automatische Freigabe bei streitigem Zahlungsverzug |

### F.2 — Freistellung

Die Freistellung muss auch den Fall der Nichtvollendung adressieren. Der Erwerber braucht Gewissheit, dass er nicht zahlt und trotzdem in der Bauträgerfinanzierung hängen bleibt.

### F.3 — Insolvenzcheck

| Zeitpunkt | Hauptfrage |
| --- | --- |
| Vor Zahlung | Keine Zahlung ohne § 3 Abs. 1 MaBV. |
| Nach Teilzahlung | Entspricht Zahlung tatsächlich dem Baufortschritt? |
| Nach Übergabe vor Eigentumsumschreibung | Vormerkung und Freistellung prüfen. |
| Bei § 7 MaBV | Sicherheit ziehen, Umfang/Dauer prüfen. |
| Bei Notaranderkonto | Auszahlungsberechtigung, Abtretung/Pfändung, Verwahrungsanweisung prüfen. |

## Teil G — Verhandlungspaket

### G.1 — Ton

Der Stil ist bestimmt, nicht schrill. Ziel: Der Notar soll rechtlich prüfen müssen; der Bauträger soll erkennen, dass die Klausel vor Gericht schlecht steht.

### G.2 — Struktur des Schreibens

```text
Sehr geehrte Damen und Herren,

wir nehmen Bezug auf den Entwurf vom [Datum] zum Bauträgervertrag [Projekt/Wohnung]. Der Entwurf ist in mehreren Punkten vor einer Beurkundung anzupassen. Die nachfolgenden Punkte sind keine Geschmacksfragen, sondern betreffen zwingende MaBV-Vorgaben, AGB-Kontrolle und aktuelle BGH-Rechtsprechung.

1. [Klausel] - [Problem]
Original: "[...]"
Bewertung: [...]
Fundstelle: [...]
Erwartetes Gegenargument: [...]
Antwort: [...]
Gewünschte Fassung: [...]

Wir bitten um einen überarbeiteten Entwurf bis [Datum]. Ohne diese Klärung ist eine Beurkundung aus Erwerbersicht nicht verantwortbar.

Mit freundlichen Grüßen
```

### G.3 — Musterargumente

| Thema | Kurzer harter Satz |
| --- | --- |
| 5 %-Sicherheit | `§ 650u Abs. 2 BGB schließt § 650m Abs. 2 BGB nicht aus; eine AGB-Klausel, die die Sicherheit nicht oder niedriger vorsieht, ist zudem an § 309 Nr. 15 lit. b BGB zu messen.` |
| Beweislast | `Die Klausel verschiebt einen Umstand aus dem Verantwortungsbereich des Bauträgers auf den Erwerber und ist nach § 309 Nr. 12 lit. a BGB unwirksam.` |
| Empfangsbestätigung | `Eine pauschale Bestätigung von Erhalt, Kenntnis oder Prüfung ist keine neutrale Dokumentation, sondern eine Tatsachenbestätigung im Sinne von § 309 Nr. 12 lit. b BGB.` |
| Abnahme GE | `Nach der aktuellen BGH-Linie darf dem einzelnen Erwerber sein eigenes Prüf- und Abnahmerecht nicht formularmäßig entzogen werden.` |
| Schlussrate | `Offene protokollierte Mängel können bei einer Klausel 'nach vollständiger Fertigstellung' bereits die Fälligkeit der Schlussrate hindern.` |
| Teilungserklärung | `Ein pauschales Änderungsrecht ohne einzeln benannte triftige Gründe ist nach § 308 Nr. 4 BGB und BGH V ZR 91/25 nicht tragfähig.` |

## Teil H — Streit, Rücktritt, Klage

### H.1 — Nach Beurkundung

Auch nach Beurkundung gilt AGB-Kontrolle. Strategie:

1. Unwirksame Klausel schriftlich beanstanden.
2. Gesetzliche Rechtslage benennen.
3. Frist zur Korrektur/Bestätigung setzen.
4. Bei Zahlung: Einbehalt begründen.
5. Bei Abnahme: Vorbehalte und eigene Sachverständige sichern.
6. Bei WEG: Beschlusslage zur gemeinschaftlichen Geltendmachung prüfen.

### H.2 — Rücktritt

Rücktritt kommt nur mit sauberem Tatbestand in Betracht:

| Grund | Prüfung |
| --- | --- |
| Bauverzug | Fälligkeit, Verzug, Fristsetzung, Entbehrlichkeit |
| Nichtleistung | erhebliche Pflichtverletzung |
| Mangel vor Abnahme | Nacherfüllungsverlangen/Frist, Zumutbarkeit |
| Unmöglichkeit | konkret darlegen |
| Insolvenz | § 103 InsO, Vormerkung, Sicherheiten |

### H.3 — Klageziele

| Ziel | Typischer Antrag |
| --- | --- |
| Mängelbeseitigung | Leistung/Nacherfüllung |
| Vorschuss | Zahlung Kostenvorschuss |
| Schlussrate abwehren | negative Feststellung oder Verteidigung im Zahlungsprozess |
| Rückzahlung | Leistungsklage nach Rücktritt/Überzahlung |
| Auflassung | Leistung auf Eigentumsumschreibung |
| Klausel | Feststellung im konkreten Streitverhältnis |
| Notarhaftung | Schadensersatz, subsidiär prüfen |

## Teil I — Nichtigkeit, § 306 BGB, Notar

### I.1 — Keine falsche Gesamtnichtigkeitsrhetorik

Bei AGB-Verstößen ist die Regelfolge § 306 BGB:

- Unwirksame Klausel entfällt.
- Vertrag bleibt im Übrigen wirksam.
- Gesetzliche Regel tritt an die Stelle.
- Keine geltungserhaltende Reduktion zugunsten des Bauträgers.

§ 139 BGB oder Gesamtnichtigkeit nur vorsichtig nennen:

| Fall | Bewertung |
| --- | --- |
| Nicht beurkundete wesentliche Leistungspflicht | Form-/Gesamtnichtigkeitsrisiko prüfen. |
| Sittenwidriges Gesamtgefüge | § 138 BGB prüfen. |
| MaBV-Zahlungsklausel falsch | regelmäßig Zahlungsklausel/ Fälligkeit, nicht automatisch Gesamtvertrag. |
| Mehrere AGB-Verstöße | starkes Verhandlungsargument, aber nicht automatisch Gesamtvertrag nichtig. |

### I.2 — Notar

Der Notar ist unparteiischer Amtsträger, nicht Interessenvertreter des Bauträgers oder Erwerbers. Bei Verbraucherverträgen sind rechtzeitige Entwurfsübersendung und Belehrung wichtig.

Prüfe:

- Wann erhielt der Verbraucher den Entwurf?
- Wurden Anlagen vollständig übersandt?
- Hat der Notar über MaBV, Vormerkung, Freistellung, Fälligkeit, Abnahme und Risiken belehrt?
- Werden pauschale Bestätigungen statt echter Belehrung verwendet?
- Ist der Notar Seriennotar des Bauträgers?

Notarhaftung nach § 19 BNotO nur als anwaltlich zu prüfende Eskalation formulieren, nicht als Automatismus.

### I.3 — Notaranderkonto und Notarhaftung trennen

Nicht pauschal behaupten, ein Notaranderkonto mache die gesamte Abwicklung unwirksam. Richtig:

1. Gibt es berechtigtes Sicherungsinteresse und wirksame Verwahrungsanweisung?
2. Wurde MaBV/Fälligkeit dadurch umgangen?
3. Wer ist empfangsberechtigt?
4. Gibt es Abtretung, Pfändung, Insolvenzfreigabe?
5. Welche Amtspflichtfragen stellt § 57 BeurkG?
6. Welche zivilrechtlichen Ansprüche bestehen unabhängig davon?

## Teil J — Realfall-Pattern und Testakte

Dieser Teil ist ein Wiedererkennungsraster für Großprojektverträge. Er ersetzt keine Prüfung, sondern sagt: Wenn dieses Muster auftaucht, springe in den genannten Prüfteil.

Wenn im Repository die Testakte `testakten/bautraegervertrag-aus-der-hoelle/` verfügbar ist, kann sie als Schulungsfall genutzt werden. Die eigentliche Vertragsanalyse darf aber nie aus der Testakte heraus behaupten, sondern muss am vorgelegten Vertrag arbeiten.

| Pattern | Typischer Fundort | Sofortprüfung |
| --- | --- | --- |
| Wohnungsbauträgervertrag mit Auflassung in einer Urkunde | Überschrift, Kaufgegenstand, Bauverpflichtung, Auflassung | Vertragsart nach § 650u BGB; Beurkundungsumfang |
| Mehrere Bezugsurkunden | Teilungserklärung, Nachträge, Baubeschreibung, Planlisten | Mitbeurkundung/eindeutige Einbeziehung; Bausoll |
| Pauschaler Verweis auf Anlagenkonvolut | `dem Käufer bekannt`, `lag zur Einsicht vor` | § 309 Nr. 12 lit. b, § 311b, Transparenz |
| `Bezugsfertigkeit` und `vollständige Fertigstellung` vermischt | Ratenplan, Übergabe, Abnahme | MaBV, Schlussrate, BGH VII ZR 88/25 |
| Erfüllungsbürgschaft oder 5 %-Einbehalt | Zahlungsabschnitt | § 650m Abs. 2, § 309 Nr. 15, tatsächliche Übergabe der Sicherheit |
| Sonderwünsche sofort fällig | Bemusterung/Sonderwunschvereinbarung | MaBV-Umgehung, Leistung erbracht?, Transparenz |
| Pauschalierter Verzugsschaden | Fertigstellung/Verzug | § 309 Nr. 5, § 286, Anrechnung auf Schadensersatz |
| Selbstvornahme ausgeschlossen | Mängelrechte | § 307, § 637, praktische Durchsetzung |
| Weite Änderungsvollmacht | Teilungserklärung/Gemeinschaftsordnung | § 308 Nr. 4, BGH V ZR 91/25 |
| Nachzüglerklausel | Abnahme Gemeinschaftseigentum | BGH VII ZR 68/24, keine Bindung an fremde unwirksame Abnahme |
| Vormerkungslöschung bei Zahlungsverzug | Vollzug/Eigentumsschutz | § 307, Druckmittel, Insolvenzrisiko |
| Notaranderkonto als Abwicklungsersatz | Zahlungs-/Verwahrungsabschnitt | BGH VII ZB 28/20, MaBV/Fälligkeit/Empfangsberechtigung trennen |

### J.1 — Ampel aus Realfall-Pattern

Ein Pattern allein ist noch kein Ergebnis. Es ist ein Suchsignal. Der Befund wird erst rot, wenn der konkrete Wortlaut ein Recht entzieht, verschiebt oder intransparent macht.

Beispiel:

```text
Pattern: "Der Käufer bestätigt, sämtliche Bezugsurkunden erhalten und geprüft zu haben."
Prüfung: Ist das eine gesondert unterschriebene Empfangsbestätigung oder eine pauschale Tatsachenbestätigung im Vertrag?
Befund: Wenn pauschal im Vertrag, § 309 Nr. 12 lit. b BGB, 🔴.
```

### J.2 — Realitätscheck Großprojekt

Bei großen Projekten ist eine individuelle Klauseländerung oft wirtschaftlich schwer durchsetzbar. Trotzdem ist die Prüfung wertvoll:

- Vor Beurkundung: Termin verschieben, kritische Klauseln protokolliert beanstanden, Änderungswünsche schriftlich stellen.
- Bei Beurkundung trotz Einwand: Belehrung und Ablehnung der Klausel dokumentieren lassen, soweit der Notar mitwirkt.
- Nach Beurkundung: Unwirksamkeit im Streitfall einwenden; gesetzliche Lage tritt ein.
- In der WEG/GdWE: Ansprüche am Gemeinschaftseigentum kollektiv bündeln.

## Teil K — Vertiefte Dogmatik

### K.1 — Vertragstyp und Mischrecht

Der Bauträgervertrag ist kein bloßer Kaufvertrag und kein bloßer Werkvertrag. § 650u BGB spaltet:

- Errichtung/Umbau: Bauvertragsrecht, soweit nicht ausgeschlossen.
- Eigentums-/Erbbaurechtsübertragung: Kaufrecht.
- Abschlagszahlungen: § 650v BGB und MaBV.
- AGB: §§ 305 ff. BGB überlagern die Vertragsgestaltung.

Prüfe deshalb nie nur eine Normschiene.

### K.2 — Beurkundungsreichweite

Wesentliche Leistungspflichten müssen notariell beurkundet oder eindeutig einbezogen sein. Kritisch:

- Baubeschreibung nur lose übergeben.
- Pläne nicht datiert.
- Teilungserklärung nur als `bekannt` bezeichnet.
- Bemusterungslisten später austauschbar.

Je zentraler der Inhalt für Preis, Nutzbarkeit oder Bausoll ist, desto eher ist fehlende Beurkundung ein Form- oder Transparenzproblem.

### K.3 — Bezugsfertigkeit, Abnahme, vollständige Fertigstellung

Nicht vermengen:

| Begriff | Bedeutung |
| --- | --- |
| Bezugsfertigkeit | Objekt kann sicher und zumutbar genutzt werden; Restarbeiten können offen sein. |
| Abnahme | Anerkennung als im Wesentlichen vertragsgerecht; Vorbehalte möglich. |
| Vollständige Fertigstellung | Alle geschuldeten Leistungen und je nach Vertrag auch protokollierte Restmängel erledigt. |

BGH VII ZR 88/25 ist hier der starke Anker: Die Schlussrate hängt am konkreten Vertragswortlaut, nicht an einer abstrakten Gleichsetzung von Abnahme und vollständiger Fertigstellung.

### K.4 — Nachzügler

Erwerber, die nach einer vermeintlichen Abnahme des Gemeinschaftseigentums kaufen, sind nicht automatisch an eine frühere Abnahme gebunden. Formularmäßige Klauseln wie `Abnahme ist erfolgt` sind hoch angreifbar, wenn eigene Prüf- und Abnahmerechte fehlen.

### K.5 — Verzug

Für Verzug braucht es:

1. fällige Leistung.
2. Nichtleistung.
3. Mahnung oder Entbehrlichkeit.
4. Vertretenmüssen, soweit erforderlich.

Pauschale Entlastungen (`Witterung`, `Materialmangel`, `Behörden`, `Generalunternehmer`) reichen nicht. Der Bauträger muss bauablaufbezogen erklären, welches Ereignis welche konkrete Verzögerung verursacht hat.

### K.6 — Vertragsstrafe und pauschalierter Schadensersatz

Trennen:

- Vertragsstrafe: Druckmittel, meist verschuldensabhängig, AGB-Höhenkontrolle.
- Pauschalierter Schadensersatz: § 309 Nr. 5 BGB, Nachweis geringeren Schadens muss offenbleiben.
- Weitergehender Schaden: darf nicht formularmäßig unangemessen ausgeschlossen werden.

### K.7 — Verjährung bei unwirksamer Abnahme

Bei unwirksamer Abnahmeklausel beginnt die typische Gewährleistungsverjährung nicht normal zu laufen. Die BGH-Entscheidungen VII ZR 68/24 und VII ZR 108/24 setzen zugleich eine 30-Jahres-Obergrenze für dortige Kostenvorschusskonstellationen. Nicht unbesehen auf jede Anspruchsart übertragen; Anspruch, Rechtstand und Vertragsschlussdatum prüfen.

### K.8 — Selbstvornahme

Ein formularmäßiger Ausschluss des Selbstvornahmerechts ist streng zu prüfen. In der Analyse nicht behaupten, jede Klausel sei sicher unwirksam, sondern:

- Welche Mängelrechte bleiben?
- Wird § 637 BGB praktisch entwertet?
- Ist der Käufer auf den Bauträger ausgeliefert?
- Gibt es Verzug mit Nacherfüllung?

Ampel meist 🟠/🔴 je nach Wortlaut.

### K.9 — Einstweiliger Besitzübergang

Wenn die Wohnung bezugsfertig ist, der Bauträger aber wegen streitiger Restmängel die Schlüssel zurückhält, kann einstweiliger Rechtsschutz zu prüfen sein. Hohe Hürden:

- klare Bezugsfertigkeit.
- erheblicher Nutzungsdruck.
- Einbehalt rechtlich plausibel.
- keine offenen Hauptleistungsvoraussetzungen.

### K.10 — § 650m-Sicherheit und Vormerkung

Vormerkung und 5 %-Sicherheit schützen unterschiedliche Risiken:

| Schutz | Deckt ab | Deckt nicht ab |
| --- | --- | --- |
| Vormerkung | Eigentumsübertragungsanspruch | Fertigstellungs-/Mängelrisiko |
| MaBV-Ratenplan | Keine Zahlung ohne Baufortschritt/Sicherung | Mängel nach Abnahme nur begrenzt |
| § 650m Abs. 2 | rechtzeitige Herstellung ohne wesentliche Mängel | alle sonstigen Schäden automatisch |
| § 7 MaBV | Rückgewähr-/Auszahlungsansprüche | Qualitätsstreit ohne Sicherungsfall |

### K.11 — Geschäftsführer, Vertrieb, Dritte

Nicht vorschnell persönliche Haftung behaupten. Prüfe sauber:

- eigene Täuschungshandlung.
- Prospekthaftung/Vertriebsunterlagen.
- Deliktischer Schaden.
- Vertreterwissen.
- Insolvenzverschleppung nur mit konkreten Tatsachen.

### K.12 — Notar in Serienprojekten

Serienbeurkundung ist nicht automatisch pflichtwidrig. Kritisch wird es, wenn:

- Entwürfe zu spät kommen.
- Bezugsurkunden fehlen.
- der Notar erkennbare AGB-/MaBV-Risiken nicht belehrt.
- der Notar pauschale Bestätigungen protokolliert, die echte Belehrung ersetzen sollen.
- Verbrauchereinwände nicht dokumentiert werden.

## Teil L — Drei-Dokumente-Paket

Jede Vollanalyse mündet im Regelfall in drei getrennte Dokumente. Keine Vermischung der Sprachregister.

### L.1 — Dokument 1: Mandantenanschreiben

Ziel: Der Verbraucher versteht in fünf Minuten, ob er unterschreiben, verschieben, nachverhandeln oder streiten soll.

Aufbau:

```text
Betreff: Prüfung Bauträgervertrag [Projekt/Wohnung]

1. Ergebnis in einem Absatz
2. Ampel-Bilanz
3. Die wichtigsten drei bis sieben Risiken
4. Was das praktisch bedeutet
5. Nächste Schritte
6. Offene Unterlagen/Fragen
```

Stil:

- einfache Sprache.
- keine langen Normketten.
- klare Handlungsempfehlung.
- keine falsche Sicherheit.

### L.2 — Dokument 2: Gutachten

Ziel: belastbare rechtliche Arbeitsfassung.

Aufbau:

```text
A. Sachverhalt und geprüfte Unterlagen
B. Quellenstand
C. Vertragsart und Verbraucherstatus
D. Pflicht-Prüfblock
E. MaBV und Zahlungsplan
F. AGB-Klauselmatrix
G. Baubeschreibung/Bausoll
H. Abnahme, Schlussrate, Mängelrechte
I. Teilungserklärung/WEG
J. Eigentumsschutz/Insolvenz
K. Gesamteinschätzung
L. Konkrete Änderungsfassung
```

Jeder rote Befund braucht Norm, Fundstelle oder klare Argumentationslinie.

### L.3 — Dokument 3: Schreiben an Bauträger und Notar

Ziel: bestimmte, verhandlungsfähige Aufforderung.

Aufbau:

```text
Betreff: Bauträgervertrag [Projekt/Wohnung] - erforderliche Anpassungen vor Beurkundung

Sehr geehrte Damen und Herren,

der Entwurf ist in folgenden Punkten vor Beurkundung anzupassen. Die notarielle Form ersetzt nicht die AGB-Inhaltskontrolle. Zwingende MaBV- und Verbraucherschutzvorgaben stehen nicht zur Disposition.

1. [Klausel] - [Problem]
Original: [...]
Rechtsgrundlage: [...]
Gegenargument: [...]
Antwort: [...]
Gewünschte Fassung: [...]

Frist / weiteres Vorgehen
```

Ton:

- bestimmt.
- keine Übertreibung.
- keine pauschalen Nichtigkeitsdrohungen.
- bei § 306 BGB klar: unwirksame AGB fallen weg; Gesetz gilt.

### L.4 — Typische Gegenargumente und Antworten

| Gegenargument | Antwort |
| --- | --- |
| `Das ist Standard.` | Standardformulare sind gerade AGB und unterliegen §§ 305 ff. BGB. |
| `Der Notar hat es beurkundet.` | Beurkundung sichert die Form, nicht automatisch die AGB-Wirksamkeit. |
| `MaBV schützt doch schon.` | MaBV, § 650m Abs. 2 und AGB-Kontrolle schützen unterschiedliche Risiken. |
| `Der Erwerber hat alles bestätigt.` | Pauschale Tatsachenbestätigungen sind nach § 309 Nr. 12 lit. b BGB unwirksam. |
| `Das Projekt braucht Flexibilität.` | Flexibilität braucht konkret benannte triftige Gründe und darf Wert/Nutzung/Kosten nicht verschlechtern. |
| `Die Schlussrate ist wegen Abnahme fällig.` | Bei `vollständiger Fertigstellung` und offenen Protokollmängeln zuerst Fälligkeit nach Vertrag und BGH VII ZR 88/25 prüfen. |

### L.5 — Qualitätsgate für das Paket

- Sind alle drei Dokumente getrennt?
- Stimmen Ampeln und Befunde überein?
- Hat Dokument 1 keine unnötigen Fachbegriffe?
- Hat Dokument 2 harte Quellen?
- Hat Dokument 3 konkrete Neufassungen?
- Sind Gegenargumente vorweggenommen?
- Sind § 306 BGB und § 139 BGB sauber getrennt?

## Bug-Hunt vor Ausgabe

Vor jeder finalen Analyse diese Fehler ausschließen:

- `§ 309 Nr. 15` nicht für Beweislast oder Empfangsbestätigung verwenden; richtig ist § 309 Nr. 12.
- `§ 650m Abs. 1` nicht auf Bauträgervertrag anwenden; er ist durch § 650u Abs. 2 ausgeschlossen.
- `§ 650m Abs. 2` nicht als bloß analog darstellen; § 650u Abs. 2 schließt ihn nicht aus.
- `§ 650k Abs. 1` nicht als Bauträger-Hauptargument verwenden; er ist ausgeschlossen.
- `§ 650k Abs. 2/3`, § 650j, § 650n nicht übersehen.
- MaBV nicht als dreizehn gesetzliche Einzelraten beschreiben; richtig: bis zu sieben Teilbeträge, zusammensetzbar aus Bausteinen.
- § 7 MaBV nicht als `Vertragssumme + 5 %` behaupten; richtig: alle Rückgewähr-/Auszahlungsansprüche bis § 3 Abs. 1 und vollständige Fertigstellung.
- AGB-Unwirksamkeit nicht automatisch zu Gesamtnichtigkeit machen; § 306 BGB ist Regelfolge.
- Keine BeckRS-/juris-/Kanzleiblog-Fundstellen zitieren.
- Keine BGH-Entscheidung ohne zulässige URL und Liveprüfung.
- Keine schrillen Drohungen ohne Tatbestand; Verhandlungsposition soll streng, aber glaubwürdig sein.
- Jede rote Ampel muss eine konkrete gewünschte Änderung haben.

> **Ende des Skills.** Bei Anwendung: Vertrag einfügen. Der Skill startet mit Pflicht-Prüfblock, arbeitet die 20 Prüfschleifen ab, zitiert nur zulässige Quellen und liefert ein verhandlungsfähiges Verbraucherpaket.
