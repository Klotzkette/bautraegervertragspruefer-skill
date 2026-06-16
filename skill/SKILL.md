---
name: bautraegervertrag-pruefer
description: "Verbraucherseitige Prüfung deutscher Bauträgerverträge nach dem Ampelsystem (🔴/🟠/🟢). Erkennt MaBV-Verstöße im Ratenplan, unzulässige AGB-Klauseln nach §§ 305 ff. BGB, Risiken bei Auflassungsvormerkung und Freistellung nach § 3 MaBV, **fehlerhafte oder lückenhafte Leistungs- und Baubeschreibungen nach § 650k BGB** (Pflichtinhalte, Detaillierungstiefe, Pauschalverweise, Bemusterungsfallen, Bausoll-Lücken, Mitbeurkundungsstatus), untaugliche Vertragsstrafen, Abnahme- und Mängelrechtsfallen, Gefahrtragungs- und Eigentumsumschreibungs-Risiken. Liefert klauselgenaue Risikomatrix, Ampel-Bilanz, Gesamteinschätzung und Handlungsempfehlung — von Nachverhandlung über notarielle Korrektur bis Rücktritt und Klage. Stützt sich auf §§ 650u, 650v BGB, §§ 650a–650o BGB, § 3 MaBV, §§ 305 ff. BGB, § 311b BGB, §§ 433 ff. BGB."
version: "1.2.0"
---

# Bauträgervertrag-Prüfer (Ampelsystem für Verbraucher)

Diese Skill-Datei trägt den vollständigen Workflow zur verbraucherseitigen Analyse eines deutschen Bauträgervertrags — vom ersten Eingang des Entwurfs bis zum Klageentwurf. **Alles in einem einzigen Markdown-Dokument:** Workflow, MaBV-Ratenplan-Prüfung, AGB-Klauselkatalog, Baubeschreibungs-Check, Abnahme- und Mängelrechte, Mustertexte. Keine externen Referenzen nötig.

**Befunde werden als farbige Ampelsymbole 🔴 / 🟠 / 🟢 ausgegeben, nicht als Farbwörter.**

## Inhaltsverzeichnis

- [Rechtlicher Anker](#rechtlicher-anker)
- [Wann diese Skill greift](#wann-diese-skill-greift)
- [Sofortstart-Logik](#sofortstart-logik)
- [Workflow in neun Stufen](#workflow-in-neun-stufen)
- [Antwortformate](#antwortformate)
- [Qualitätsgate vor jeder Ausgabe](#qualitätsgate-vor-jeder-ausgabe)
- [Teil A — MaBV-Ratenplan und Sicherheiten](#teil-a--mabv-ratenplan-und-sicherheiten)
- [Teil B — AGB- und Klauselkontrolle](#teil-b--agb--und-klauselkontrolle)
- [Teil C — Leistungsbeschreibung, Baubeschreibung und Bausoll](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll)
- [Teil D — Vertragsstrafen, Fertigstellungsfristen, Verzug](#teil-d--vertragsstrafen-fertigstellungsfristen-verzug)
- [Teil E — Abnahme, Gefahrtragung, Mängelrechte, Gewährleistung](#teil-e--abnahme-gefahrtragung-mängelrechte-gewährleistung)
- [Teil F — Eigentumsschutz, Auflassungsvormerkung, Freistellung, Insolvenz](#teil-f--eigentumsschutz-auflassungsvormerkung-freistellung-insolvenz)
- [Teil G — Mandatsmodule: Nachverhandlung, Rücktritt, Klage](#teil-g--mandatsmodule-nachverhandlung-rücktritt-klage)
- [Teil H — Musterklauseln und Sonderfälle](#teil-h--musterklauseln-und-sonderfälle)
- [Teil I — Nichtigkeitsrisiken, Transparenzgebot und Notarhaftung](#teil-i--nichtigkeitsrisiken-transparenzgebot-und-notarhaftung)
- [Teil J — Realfall-Pattern aus Großprojekten (Anschauungsmaterial)](#teil-j--realfall-pattern-aus-großprojekten-anschauungsmaterial)

## 🚨 Pflicht-Prüfblock vor jeder Vollanalyse

**Diese fünf Punkte werden bei jedem Bauträgervertrag mit Verbraucherbeteiligung zwingend zuerst geprüft — unabhängig davon, was im übrigen Vertrag steht. Schlägt einer dieser Punkte aus, ist das im Sofortstart-Output noch vor der Klausel-Risikomatrix sichtbar zu machen.**

1. **§ 650m BGB — 5 %-Sicherheitseinbehalt.** Hat der Verbraucher das Recht, **bei der ersten Abschlagszahlung 5 %** der Gesamtvergütung als Sicherheit einzubehalten (oder eine Sicherheit i. H. v. 5 % zu erhalten)? Fehlt der Hinweis vollständig oder wird das Recht ausgeschlossen, ist das ein **🔴 schwerwiegender Verstoß** und ein Indiz dafür, dass der Vertrag insgesamt verbraucherfeindlich konzipiert ist.
2. **§ 309 Nr. 15 lit. a BGB — Beweislastumkehr.** Enthält der Vertrag eine Klausel, die dem Verbraucher die Beweislast für Umstände aufbürdet, die im Verantwortungsbereich des Bauträgers liegen? Beispiele: „Der Erwerber trägt die Beweislast für Baumängel", „Verzögerungen gelten als nicht vom Bauträger verschuldet, sofern der Erwerber das Gegenteil nicht nachweist". → **🔴 unwirksam nach § 309 Nr. 15 lit. a BGB**.
3. **§ 309 Nr. 15 lit. b BGB — Empfangsbestätigung als Tatsachenerklärung.** Enthält der Vertrag eine Klausel, in der der Verbraucher den Erhalt einer Erklärung, eines Dokuments oder einer Leistung **vorab pauschal** bestätigt („Der Erwerber bestätigt, die Baubeschreibung erhalten und geprüft zu haben", „Der Erwerber bestätigt, über Risiken aufgeklärt worden zu sein")? → **🔴 unwirksam nach § 309 Nr. 15 lit. b BGB**.
4. **Transparenzgebot § 307 Abs. 1 S. 2 BGB.** Ist der Vertrag verständlich oder ein unüberschaubares Konvolut (250–500+ Seiten mit Anlagen, Verweisketten, juristisch nicht erschließbarem Aufbau)? Bei Verbraucherbauträgerverträgen ist Intransparenz prüfungsrelevant; im Extremfall verlieren intransparente Klauseln ihre Wirksamkeit. **🔴 wenn Umfang/Aufbau für Verbraucher nicht zumutbar erschließbar.**
5. **Druckmuster und Eingriffe in dingliche Sicherung.** Enthält der Vertrag Klauseln, die
   - die Löschung der Auflassungsvormerkung **bei einseitiger Verzugsmitteilung des Bauträgers** vorsehen,
   - die Schlüsselübergabe von „vollständiger Zahlung" abhängig machen, obwohl noch Restmängel oder Restleistungen ausstehen (Drohmuster „ohne Geld keine Schlüssel"),
   - dem Erwerber **anteilige Kosten des vom Bauträger gestellten Sachverständigen** für die technische Abnahme aufbürden?
   
   → Jeder dieser Punkte ist **🔴 schwerwiegend** und für den Mandantenbericht hervorzuheben.
6. **Leistungs- und Baubeschreibung — § 650k BGB.** Liegt der Vertrag **ohne** vollständige Leistungs-/Baubeschreibung vor oder verweist er nur pauschal auf „branchenübliche Standards", „allgemein anerkannte Regeln der Technik" oder „Ausstattung mittlerer Art und Güte", ohne konkretes Bausoll zu definieren? Fehlen Pflichtangaben (Wohnflächenberechnung mit Grundlage, Energie-/KfW-Standard, Bauweise, Innenausbau-Standards, verbindlicher Fertigstellungstermin)? Wird die Leistungsbeschreibung in einer separaten, **nicht mitbeurkundeten Anlage** geführt, sodass sie später bestritten werden kann? → **🔴 schwerwiegend** — Bausoll-Lücken sind die häufigste Streitquelle und Hebel für Mängel-, Minderungs- und Schadensersatzansprüche. Detailprüfung: [Teil C](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll).

**Folgen, wenn einer dieser Punkte aus dem Vertrag schlägt:** Klauselunwirksamkeit nach §§ 307, 309 BGB; im Extremfall **Teilnichtigkeit oder Gesamtnichtigkeit** nach § 139 BGB, wenn die Aushöhlung des Verbraucherschutzes den Kern des Vertrags erfasst. **Notarhaftung** nach § 19 BNotO i. V. m. § 17 BeurkG kommt in Betracht, wenn der Notar einen offensichtlich einseitig zulasten des Verbrauchers gestalteten Vertrag ohne ausreichende Belehrung beurkundet hat. Näheres: [Teil I](#teil-i--nichtigkeitsrisiken-transparenzgebot-und-notarhaftung).

## Rechtlicher Anker

- **§ 650u BGB** — Bauträgervertrag: Werkvertrag über die Errichtung oder den Umbau eines Hauses oder vergleichbaren Bauwerks, verbunden mit der Verpflichtung zur Eigentumsübertragung. Es gelten ergänzend die Vorschriften des Werkvertrags- und Kaufrechts (§ 650u Abs. 2 BGB).
- **§ 650v BGB** — Abschlagszahlungen nur nach Maßgabe der **Makler- und Bauträgerverordnung (MaBV)**.
- **§ 650m BGB** — **5 %-Sicherheitseinbehalt** zugunsten des Verbrauchers bei Verbraucherbauverträgen (analog/ergänzend bei Bauträgerverträgen maßgeblich, da Bauträgervertrag werkvertragliche Elemente enthält). Verbraucher kann bei erster Abschlagszahlung 5 % der Gesamtvergütung einbehalten oder Sicherheitsleistung verlangen. **Pflichtprüfung in jedem Verbraucher-Bauträgervertrag.**
- **§ 650k BGB** — Inhalt des Verbraucherbauvertrags: Pflicht zur Baubeschreibung und zu verbindlichen Angaben zum Zeitpunkt der Fertigstellung. Vorschrift gilt mittelbar auch für die Bauträgerseite.
- **§ 650l BGB** — Widerrufsrecht des Verbrauchers (sofern nicht beurkundet bzw. nach § 312 Abs. 2 Nr. 3 BGB ausgeschlossen — bei Bauträgerverträgen wegen § 311b BGB regelmäßig kein Widerrufsrecht; Hinweis muss aber vertraglich klar sein).
- **§ 311b Abs. 1 BGB** — Beurkundungspflicht: Bauträgerverträge sind notariell zu beurkunden; Verstoß führt zur Nichtigkeit.
- **§§ 305 ff. BGB** — AGB-Kontrolle. § 305c BGB (überraschende Klauseln), **§ 307 Abs. 1 S. 2 BGB Transparenzgebot**, § 307 BGB (unangemessene Benachteiligung), §§ 308, 309 BGB (Klauselverbote). Auch bei beurkundeten Bauträgerverträgen anwendbar — die notarielle Beurkundung schützt nicht vor AGB-Kontrolle.
- **§ 309 Nr. 15 lit. a BGB** — Verbot von Beweislastklauseln, die den Verbraucher entgegen der gesetzlichen Verteilung belasten. **Pflichtprüfung.**
- **§ 309 Nr. 15 lit. b BGB** — Verbot pauschaler Empfangs- oder Kenntnisnahmebestätigungen. **Pflichtprüfung.**
- **§ 139 BGB** — Teilnichtigkeit: Führt zur Gesamtnichtigkeit, wenn der Vertrag ohne die nichtigen Bestandteile nicht abgeschlossen worden wäre.
- **§ 19 BNotO i. V. m. § 17 BeurkG** — **Notarhaftung** bei Verletzung der Belehrungspflicht. Bei evident einseitig zulasten des Verbrauchers gestalteten Verträgen, ungeprüft beurkundet, kommt Schadensersatzpflicht des Notars in Betracht.
- **§ 3 MaBV** — Voraussetzungen für Vermögenswert-Annahme: Beurkundung, Auflassungsvormerkung, Lastenfreistellung, Baugenehmigung, Ratenplan nach § 3 Abs. 2 MaBV mit höchstens 13 (bzw. 7 zusammengefassten) Raten und festen Prozentsätzen.
- **§ 7 MaBV** — Alternativsicherung statt Ratenplan: unbefristete, selbstschuldnerische Bankbürgschaft über die gesamte Vertragssumme zzgl. 5 %. Praktisch selten, aber zulässig.
- **§§ 433 ff., 311b, 925 BGB** — Eigentumsübertragung: Auflassung vor dem Notar und Eintragung im Grundbuch.
- **§§ 883 ff. BGB** — Auflassungsvormerkung: dingliche Sicherung des Erwerbsanspruchs; Rang nach Eingang beim Grundbuchamt entscheidend.
- **§§ 640, 641 BGB** — Abnahme und Fälligkeit der Vergütung im Werkvertrag.
- **§ 650g BGB** — Zustandsfeststellung bei verweigerter Abnahme.
- **§§ 633–639 BGB** — Mängelrechte; **§ 634a BGB** — Verjährung (5 Jahre bei Bauwerken).
- **§ 650f BGB** — Bauhandwerkersicherung (für Bauunternehmer, NICHT zugunsten des Bauträger-Erwerbers; relevant für Insolvenzfälle).
- **§ 632a BGB** — Abschlagszahlungen im Werkvertragsrecht (wird im Bauträgerrecht durch MaBV überlagert).

> **Rechtsprechung live prüfen.** Keine Entscheidung aus Modellwissen zitieren. Vor jeder Ausgabe Stellen über `gesetze-im-internet.de`, `dejure.org` oder das Rechtsprechungsportal des Bundes mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wann diese Skill greift

- Verbraucher hat einen Bauträgervertrags-Entwurf vom Notar oder Bauträger erhalten und will ihn vor Beurkundung prüfen lassen.
- Erwerber hat schon beurkundet und will rückwirkend einzelne Klauseln, MaBV-Konformität oder Sicherheiten überprüfen.
- Bauträger ist insolvenzbedroht oder hat den Bau eingestellt; Erwerber prüft seine Position.
- Mängelrechtsstreit nach Übergabe.
- Verbraucherzentrale, Mietervereins-Hauskaufberatung, Erwerberanwalt oder Schulungsfall.

Wenn dagegen ein reiner Grundstückskaufvertrag (ohne Errichtungsverpflichtung) oder ein Werkvertrag ohne Eigentumsübertragung vorliegt: anderes Mandat, dieser Skill ist nicht zuständig — sondern Kaufrecht (§§ 433 ff. BGB) bzw. Bauvertragsrecht (§§ 650a ff. BGB) isoliert.

**Hinweise zum Pflicht-Prüfblock am Anfang dieser Datei:** Die dort genannten fünf Punkte sind keine Empfehlung, sondern Pflicht — sie werden bei jedem Vertrag mit Verbraucherbeteiligung zwingend geprüft. Nähere Begründung und Eskalationsoptionen (Nichtigkeit, Notarhaftung) in [Teil I](#teil-i--nichtigkeitsrisiken-transparenzgebot-und-notarhaftung).

## Sofortstart-Logik

Sobald ein Vertragstext, Auszug oder Foto des Bauträgervertrags eingefügt wird, **startet die Vollanalyse ohne Rückfragen-Kaskade**. Fehlende Angaben werden als Annahmen markiert (z. B. „Annahme: § 3 Abs. 2 MaBV-Ratenplan, da keine Bürgschaft erkennbar"). Maximal **eine gebündelte Rückfrage** am Ende, und nur dann, wenn die Analyse ohne die Information objektiv falsch würde.

Pflichtoutput im Sofortstart:

1. **Pflicht-Prüfblock-Ergebnis** (§ 650m, § 309 Nr. 15 lit. a/b, Transparenzgebot, Druckmuster) — als erstes, mit klarer Ampel pro Pflichtpunkt.
2. Klauselweise Risikomatrix (Originaltext · Decodierung · Risiko · Ampel).
3. Ampel-Bilanz (Anzahl 🔴 / 🟠 / 🟢).
4. **Nichtigkeitseinschätzung** (Teil- oder Gesamtnichtigkeit § 139 BGB? Hinweis auf mögliche Notarhaftung § 19 BNotO?).
5. Gesamteinschätzung (verbraucherfreundlich · ausgewogen · einseitig zugunsten Bauträger).
6. Handlungsempfehlung (Nachverhandlung mit konkreten Vorschlägen · Beurkundung verweigern · Notartermin verschieben · Rücktritt prüfen · Klage · Notar-Beschwerde / Notarhaftung).

## Workflow in neun Stufen

Arbeite in dieser Reihenfolge. Springe nur zurück, wenn ein späterer Schritt einen früheren in Frage stellt (z. B. Ratenplan-Verstoß macht spätere Klauselprüfung obsolet).

### 1 — Intake und Rollenklärung

| Punkt | Klärung |
| --- | --- |
| Rolle | Erwerber, Anwalt, Verbraucherzentrale, Bauträger/Notar (Quergegenprüfung). |
| Ziel | Verstehen, vor Beurkundung nachverhandeln, beurkundeten Vertrag prüfen, Sicherheiten klären, Rücktritt prüfen, Klage vorbereiten. |
| Vertragsstatus | Entwurf · Notarentwurf · beurkundet · in Vollzug · vollzogen mit Übergabe · Streitphase. |
| Objektart | Eigentumswohnung in Mehrfamilienhaus, Reihenhaus, Doppelhaushälfte, Einfamilienhaus auf Bauträger-Grundstück, Sanierung im Bestand. |
| Bauträger | Größe, Bonität-Hinweise, Konzernanbindung, Historie. |
| Notar | Vom Bauträger benannt? Eigenvorschlag? Region? |
| Kaufpreis | Gesamtpreis, Anteile Grund/Bau, evtl. Sonderwünsche. |
| Finanzierung | Eigenkapital, Bankdarlehen, KfW, evtl. Anschlussfinanzierungsrisiko. |
| Eilbedarf | Beurkundungstermin schon angesetzt? Wann? |

Notiere alles in einem Mandatsblatt. Wenn der Vertrag als PDF kommt: zuerst die formale Prüfung aus [Teil B](#teil-b--agb--und-klauselkontrolle) abschnittsweise durchgehen, dann den Ratenplan ([Teil A](#teil-a--mabv-ratenplan-und-sicherheiten)).

### 2 — Vertragsart und Pflichtbausteine sichern

Ein Bauträgervertrag muss diese **Pflichtbausteine** enthalten — fehlt einer, ist das ein eigener Befund:

| Pflichtbaustein | Rechtsgrundlage | Folge bei Fehlen |
| --- | --- | --- |
| Notarielle Beurkundung | § 311b Abs. 1 BGB | Nichtigkeit |
| Bezeichnung des Grundstücks (Flur, Flurstück, Adresse) | § 311b BGB | Beurkundungsmangel |
| Beschreibung des herzustellenden Werks (Baubeschreibung) | § 650k BGB analog | Risikofehler 🔴 |
| Verbindliche Fertigstellungstermine bzw. Zeitraum | § 650k Abs. 3 BGB | 🔴 |
| Kaufpreis und Aufteilung Grund/Bau | § 311b BGB | 🔴 |
| Auflassungsvormerkung zugunsten Erwerber | § 3 Abs. 1 Nr. 2 MaBV | 🔴 (Zahlungsverbot) |
| Lastenfreistellung | § 3 Abs. 1 Nr. 3 MaBV | 🔴 |
| Ratenplan nach § 3 Abs. 2 MaBV oder Bürgschaft nach § 7 MaBV | § 650v BGB | 🔴 |
| Regelung zur Abnahme | §§ 640, 650g BGB | 🟠 wenn unzulässig formularvertraglich vorweggenommen |
| Mängelrechte und Verjährung | §§ 634, 634a BGB | 🟠 bei AGB-Abweichung zulasten Erwerber |

### 3 — Klauselweise Analyse: Ampel-Risikomatrix

Bilde für jede notenrelevante Klausel vier Spalten:

1. Originalwortlaut (mit Klauselnummer/Paragraph aus dem Vertrag).
2. Decodierte Aussage (was würde sie im Streitfall bedeuten).
3. Rechtsfolge / Risiko (welcher Verbrauchernachteil entsteht konkret).
4. Ampel 🔴 / 🟠 / 🟢.

Material:

- [Teil A](#teil-a--mabv-ratenplan-und-sicherheiten) — Ratenplan-Prozentsätze, Stichmonate, Mehr- als 7-Raten-Frage.
- [Teil B](#teil-b--agb--und-klauselkontrolle) — Klauselkatalog typischer Bauträger-AGB.
- [Teil C](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll) — Leistungs- und Baubeschreibungs-Pflichtangaben, Bausoll-Definition, Bemusterungsfalle.
- [Teil D](#teil-d--vertragsstrafen-fertigstellungsfristen-verzug) — Fristen, Vertragsstrafen, Verzugsschaden.
- [Teil E](#teil-e--abnahme-gefahrtragung-mängelrechte-gewährleistung) — Abnahmeklauseln, Mängelrechte.
- [Teil F](#teil-f--eigentumsschutz-auflassungsvormerkung-freistellung-insolvenz) — dingliche Sicherung.

Wenn eine Klausel im Katalog nicht steht, leite das Risiko aus dem objektiven Empfängerhorizont her und vermerke die Unsicherheit (Beispiel: „Risiko Orange, weil X benachteiligt; ohne BGH-Stütze; Live-Recherche empfohlen").

### 4 — MaBV-Ratenplan im Detail

Der Ratenplan ist die **härteste** Schutzvorschrift für den Verbraucher. Prüfe satzweise gegen [Teil A](#teil-a--mabv-ratenplan-und-sicherheiten):

- Ist § 3 Abs. 2 MaBV vereinbart (Ratenplan) oder § 7 MaBV (Bürgschaft)?
- Wenn Ratenplan: Sind die 13 Einzelraten korrekt oder zu 7 zusammengefasst? Stimmen die Prozentsätze? Sind die Voraussetzungen (Rohbau, Dach, …) korrekt benannt?
- Sind die Voraussetzungen für die erste Rate nach § 3 Abs. 1 MaBV erfüllt (Vertrag rechtswirksam, Auflassungsvormerkung eingetragen, Freistellung, Baugenehmigung)?
- Vorauszahlungsklauseln über den Ratenplan hinaus → **immer 🔴**.

### 5 — Leistungsbeschreibung, Baubeschreibung und Bausoll

Eine schwache oder lückenhafte Leistungsbeschreibung ist die **häufigste Streitquelle** und der wichtigste Hebel für spätere Mängel- und Minderungsansprüche. „Leistungsbeschreibung" und „Baubeschreibung" werden im Bauträgervertrag oft synonym verwendet; manche Verträge führen die Leistungsbeschreibung als eigene Anlage. Beides definiert das **Bausoll** — was nicht klar beschrieben ist, kann der Bauträger später bestreiten.

Pflichtprüfpunkte:

- **Vollständigkeit** nach § 650k Abs. 2 BGB (Art und Umfang der Leistung, wesentliche Eigenschaften, Gebäudedaten, Bauphysik, Innenausbau, Technik, Energiestandard, Außenanlagen, Fertigstellungstermin).
- **Beurkundungsumfang:** Ist die Leistungsbeschreibung **mitbeurkundet** (Bestandteil der notariellen Urkunde) oder nur lose als Anlage beigefügt? Nur Mitbeurkundetes ist sicher Vertragsbestandteil (§ 311b BGB).
- **Wohnflächenangabe** und Berechnungsgrundlage (DIN 277? WoFlV?) — mit Toleranzangabe?
- **Detaillierung der Ausstattung** (Bodenbeläge, Sanitär, Heizung, Fenster, Dämmung, Elektrik, Lüftung, Smart-Home) — konkrete Produkte/Klassen oder nur Sammelbegriffe?
- **Bemusterungsklauseln:** Wer trägt Mehrkosten? Welche Auswahl ist im Preis enthalten? Bemusterungsbudget pro Gewerk?
- **Energie-Standard, KfW-Klasse, GEG-Konformität** mit konkreter Klasse, nicht nur „geltendes Recht".
- **Pauschalverweise** auf „branchenübliche", „allgemein anerkannte Regeln der Technik" oder „Ausstattung mittlerer Art und Güte" — punktuell zulässig, aber **kein** Ersatz für konkretes Bausoll → oft 🟠 / 🔴.
- **Schaufenster-Drift:** Hochwertiger Aufgabenkatalog im Prospekt, im Vertrag aber nur Pauschalverweise — Indiz für gezielte Aushöhlung des Bausolls. Werbeangaben sind nur dann geschuldet, wenn sie zum Vertragsinhalt gemacht wurden.
- **Widersprüche zwischen Plan, Baubeschreibung und Vertragstext** — was geht im Streitfall vor? (Regel: Mitbeurkundetes vor loser Anlage; konkrete Beschreibung vor Pauschalverweis.)

Material: [Teil C](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll).

### 6 — Fristen, Strafen, Verzug

- Gibt es einen **verbindlichen** Fertigstellungstermin oder nur einen unverbindlichen „voraussichtlichen" Termin?
- Vertragsstrafe wirksam vereinbart? Höhe verhältnismäßig (BGH-Linie: max. 5 % der Auftragssumme, pro Tag max. 0,2–0,3 ‰)?
- Ist der Verzugsschadensersatz ausgeschlossen oder limitiert? → 🟠 / 🔴.

Material: [Teil D](#teil-d--vertragsstrafen-fertigstellungsfristen-verzug).

### 7 — Abnahme, Gefahrtragung, Mängelrechte

- **Achtung Falle:** Trennung Sondereigentum / Gemeinschaftseigentum. Klauseln, die die Abnahme des Gemeinschaftseigentums dem Bauträger selbst oder einem von ihm bestimmten Sachverständigen übertragen, sind nach ständiger BGH-Rechtsprechung unwirksam (live verifizieren).
- Gefahrübergang regelmäßig mit Abnahme oder Übergabe (§ 644 BGB / § 446 BGB analog).
- Mängelrechte: Verjährung 5 Jahre ab Abnahme (§ 634a Abs. 1 Nr. 2 BGB) — Verkürzung in AGB regelmäßig unwirksam.
- Vorbehaltsfreie Schlussratenfreigabe-Klauseln: 🔴.

Material: [Teil E](#teil-e--abnahme-gefahrtragung-mängelrechte-gewährleistung).

### 8 — Eigentumsschutz, Auflassungsvormerkung, Freistellung, Insolvenz

- Auflassungsvormerkung **vor** der ersten Zahlung im Grundbuch eingetragen? Rang erstrangig?
- Lastenfreistellung gesichert (Freistellungserklärung der finanzierenden Bank des Bauträgers, § 3 Abs. 1 Nr. 3 MaBV)?
- Falls Bauträgerinsolvenz: Welche Stufe? Wer hält den Schlüssel? Welche Sicherheit greift?

Material: [Teil F](#teil-f--eigentumsschutz-auflassungsvormerkung-freistellung-insolvenz).

### 9 — Mandantenbericht, Verhandlung, Eskalation

Liefere dem Mandanten:

- Knappe Zusammenfassung (Ampel-Bilanz, Hauptrisiken).
- Streitstellen-Tabelle: Originalwortlaut · gewünschte Neufassung · Begründung · BGH-Stütze (live).
- Handlungsempfehlung: nachverhandeln · Beurkundung verschieben · Vertrag nicht unterzeichnen · nach Beurkundung nachverhandeln · Rücktritt prüfen · Klage.

Wenn nachverhandelt oder formal aufgefordert werden soll, baue daraus das **Korrekturschreiben** an Bauträger bzw. Notar. Material und Mustertexte: [Teil G](#teil-g--mandatsmodule-nachverhandlung-rücktritt-klage).

## Antwortformate

### Schnellscan

```
Kurzbild
- Vertragsart:
- Pflichtbausteine vollständig?:
- MaBV-Ratenplan konform?:
- Ampel-Bilanz: 🔴 X / 🟠 Y / 🟢 Z
- Hauptrisiko:
- Eilbedarf:

Nächster Schritt
- Vorschlag in einem Satz.
```

### Vollanalyse

```
1. Pflichtbausteine sichern.
2. Klauselweise Ampel-Risikomatrix.
3. MaBV-Ratenplan im Detail.
4. Leistungsbeschreibung, Baubeschreibung und Bausoll prüfen.
5. Fristen und Vertragsstrafen.
6. Abnahme und Mängelrechte.
7. Eigentumsschutz und Insolvenzfestigkeit.
8. Streitstellen-Tabelle.
9. Handlungsempfehlung.
```

Tabellen mit Spalten **Originalwortlaut · Decodierte Aussage · Risiko · Ampel**.

### Mandatsoutput

- Zusammenfassung in vier bis acht Sätzen.
- Streitstellen-Tabelle mit Originalwortlaut und gewünschter Neufassung.
- Konkrete Verhandlungspunkte sortiert nach Risiko (🔴 zuerst).
- Empfehlung: nachverhandeln · nicht beurkunden · beurkunden mit Vorbehalt · klagen · zurücktreten · Schadensersatz.

## Qualitätsgate vor jeder Ausgabe

- Sind Umlaute, Namen, Klauselnummern, Daten und Beträge sauber übernommen?
- Ist die Vertragsart richtig (Bauträger vs. reiner Werkvertrag vs. reiner Kaufvertrag)?
- Ist der MaBV-Ratenplan korrekt geprüft (13 vs. 7 Raten, Prozentsätze, Voraussetzungen)?
- Sind AGB-Verstöße konkret an einer Vorschrift festgemacht (§ 307 BGB, § 309 BGB usw.)?
- Keine erfundenen Klauseln, BGH-Fundstellen oder Prozentsätze?
- Wirkt das Ergebnis wie eine verwendbare anwaltliche Arbeitsfassung — nicht wie ein Schema?

---

# Teil A — MaBV-Ratenplan und Sicherheiten

Die Makler- und Bauträgerverordnung (MaBV) ist die **schärfste Verbraucherschutzvorschrift** im Bauträgerrecht. Sie regelt, wann der Bauträger Geld vom Erwerber annehmen darf und in welchen Raten.

## A.1 — Grundvoraussetzungen nach § 3 Abs. 1 MaBV

Bevor die **erste** Rate fällig wird, müssen folgende Voraussetzungen kumulativ vorliegen:

| Voraussetzung | § 3 Abs. 1 MaBV | Verbrauchercheck |
| --- | --- | --- |
| Vertrag rechtswirksam | Nr. 1 | Notariell beurkundet, keine schwebende Unwirksamkeit |
| Auflassungsvormerkung eingetragen | Nr. 2 | Erstrangig zugunsten Erwerber |
| Lastenfreistellung | Nr. 3 | Freistellungserklärung der finanzierenden Bank des Bauträgers liegt vor |
| Baugenehmigung erteilt oder Negativattest | Nr. 4 | Bei Bestandsobjekten ggf. nicht erforderlich |

Fehlt **eine** dieser Voraussetzungen, ist die Zahlungsanforderung des Bauträgers **rechtswidrig** — Erwerber kann und muss verweigern. **Ampel 🔴.**

## A.2 — Ratenplan nach § 3 Abs. 2 MaBV

Höchstens **13 Einzelraten**, alternativ zu **7 zusammengefassten Raten** zusammenfassbar. Prozentsätze sind verbindlich.

### Standardratenplan (13 Raten)

| Rate | Voraussetzung | Anteil (%) |
| --- | --- | --- |
| 1 | nach Beginn der Erdarbeiten | 30,0 |
| 2 | nach Rohbaufertigstellung einschließlich Zimmererarbeiten | 28,0 |
| 3 | nach Herstellung der Dachflächen und Dachrinnen | 5,6 |
| 4 | nach Rohinstallation der Heizungsanlagen | 2,1 |
| 5 | nach Rohinstallation der Sanitäranlagen | 2,1 |
| 6 | nach Rohinstallation der Elektroanlagen | 2,1 |
| 7 | nach Fenstereinbau einschließlich Verglasung | 7,0 |
| 8 | nach Innenputz, ausgenommen Beiputzarbeiten | 4,2 |
| 9 | nach Estrich | 2,1 |
| 10 | nach Fliesenarbeiten im Sanitärbereich | 2,8 |
| 11 | nach Bezugsfertigkeit und Zug-um-Zug gegen Besitzübergabe | 8,4 |
| 12 | nach Fassadenarbeiten | 2,1 |
| 13 | nach vollständiger Fertigstellung | 3,5 |
| **Summe** | | **100,0** |

### Zusammengefasster Ratenplan (max. 7 Raten)

| Rate | Voraussetzung | Anteil (%) |
| --- | --- | --- |
| 1 | nach Beginn der Erdarbeiten | 30,0 |
| 2 | nach Rohbaufertigstellung einschließlich Zimmererarbeiten | 28,0 |
| 3 | nach Herstellung der Dachflächen, Dachrinnen und Rohinstallation Heizung/Sanitär/Elektrik | 11,9 |
| 4 | nach Fenstereinbau einschließlich Verglasung | 7,0 |
| 5 | nach Innenputz und Estrich | 6,3 |
| 6 | nach Bezugsfertigkeit und Zug-um-Zug gegen Besitzübergabe | 8,4 |
| 7 | nach Fassadenarbeiten und vollständiger Fertigstellung | 8,4 |
| **Summe** | | **100,0** |

### Häufige Verstöße

| Verstoß | Befund |
| --- | --- |
| Höhere Prozentsätze als verordnet | 🔴 |
| Andere Reihenfolge (Voraussetzungen vorgezogen) | 🔴 |
| Mehr als 13 / mehr als 7 Raten | 🔴 |
| Erste Rate fällig „bei Vertragsschluss" ohne Auflassungsvormerkung | 🔴 |
| Schlussrate vor vollständiger Fertigstellung fällig | 🔴 |
| Zwischenraten mit „nach Baufortschritt" ohne konkrete Voraussetzung | 🟠 |
| Pauschalrate für „Sonderwünsche" außerhalb des Ratenplans | 🟠 (kann zulässig sein, prüfen) |

## A.3 — Alternative: Bürgschaft nach § 7 MaBV

Statt Ratenplan kann der Bauträger eine **unbefristete, selbstschuldnerische Bankbürgschaft** über die gesamte Vertragssumme zzgl. 5 % stellen. Dann darf der Erwerber vorzeitig Zahlungen leisten, weil die Bürgschaft das Insolvenzrisiko abdeckt.

Verbrauchercheck bei § 7-Bürgschaft:

| Prüfpunkt | Soll | Befund bei Verstoß |
| --- | --- | --- |
| Bürge ist deutsche Großbank oder vergleichbar | ja | 🟠 bei Auslandsbürge oder unbekanntem Bürgen |
| Bürgschaftssumme = Vertragssumme + 5 % | ja | 🔴 wenn niedriger |
| Unbefristet | ja | 🔴 wenn befristet |
| Selbstschuldnerisch | ja | 🟠 wenn nur Ausfallbürgschaft |
| Originalurkunde an Erwerber vor erster Zahlung | ja | 🔴 wenn nur Kopie oder „liegt bereit" |

## A.4 — Insolvenzfestigkeit

- **Ratenplan-Modell:** Erwerber zahlt nur, was bereits gebaut ist. Bei Bauträger-Insolvenz hat er ein „totes" Grundstück mit Halbfertigem Bau — aber kein verlorenes Geld für Nicht-Geleistetes.
- **Bürgschaftsmodell:** Erwerber zahlt vor, ist aber abgesichert.
- **Notaranderkonto:** Heute praktisch unzulässig (§ 3 MaBV verlangt Ratenplan oder Bürgschaft).

---

# Teil B — AGB- und Klauselkontrolle

Bauträgerverträge enthalten regelmäßig vorformulierte Klauseln, auch wenn sie notariell beurkundet werden. Notarielle Beurkundung **schützt nicht** vor AGB-Kontrolle nach §§ 305 ff. BGB — das ist ständige Rechtsprechung (live verifizieren).

## B.1 — Maßstäbe

| Vorschrift | Inhalt |
| --- | --- |
| § 305c BGB | Überraschende und mehrdeutige Klauseln |
| § 307 BGB | Generalklausel: unangemessene Benachteiligung |
| § 308 BGB | Klauselverbote mit Wertungsmöglichkeit |
| § 309 BGB | Klauselverbote ohne Wertungsmöglichkeit (greifen über § 307 BGB häufig auch bei B2C-Bauträgerverträgen) |

## B.2 — Klauselkatalog

| Klauseltyp | Originaltext (typisch) | Decodierung | Ampel |
| --- | --- | --- | --- |
| **Abnahmevollmacht zugunsten Bauträger** | „Der Erwerber bevollmächtigt den Bauträger zur Abnahme des Gemeinschaftseigentums" | Selbstabnahme durch den Bauträger — vom BGH ständig als unwirksam beurteilt | 🔴 |
| **Sachverständigenabnahme durch Bauträgervertrauten** | „Die Abnahme erfolgt durch einen vom Bauträger zu benennenden Sachverständigen" | Faktische Selbstabnahme | 🔴 |
| **Bemusterungs-Mehrkosten-Pauschale** | „Bei Bemusterung anfallende Mehrkosten werden mit pauschal 20 % berechnet" | Unangemessen, weil pauschal und intransparent | 🟠 / 🔴 |
| **Verjährungsverkürzung** | „Gewährleistungsansprüche verjähren in 2 Jahren" | Verstoß gegen § 634a BGB (5 Jahre bei Bauwerken), unwirksam | 🔴 |
| **Mängelrechtsausschluss** | „Geringfügige Mängel berechtigen nicht zur Zurückbehaltung" | Aushöhlung des Zurückbehaltungsrechts | 🔴 |
| **Vorbehaltsfreie Schlussratenfreigabe** | „Der Erwerber verpflichtet sich, die Schlussrate ohne Einbehalt zu zahlen" | Aushebelung des Druckmittels gegen Restmängel | 🔴 |
| **Verzicht auf Zurückbehaltungsrecht** | „Ein Zurückbehaltungsrecht wegen Mängeln ist ausgeschlossen" | § 309 Nr. 2 BGB | 🔴 |
| **Einseitige Bauänderungsklauseln** | „Der Bauträger ist berechtigt, technisch gleichwertige Änderungen vorzunehmen" | Wenn ohne Zustimmungsvorbehalt: zu weitgehend | 🟠 |
| **Notarvorschrift** | „Beurkundender Notar ist ausschließlich Notar Dr. X" | Erwerber muss freie Notarwahl haben (§ 17 BeurkG-Hinweis) | 🟠 |
| **Erfüllungsort/Gerichtsstand zugunsten Bauträger** | „Erfüllungsort und Gerichtsstand sind Sitz des Bauträgers" | Bei Verbrauchern unzulässig (§§ 29c ZPO, 38 ZPO) | 🔴 |
| **Aufrechnungsverbot** | „Eine Aufrechnung ist nur mit unbestrittenen oder rechtskräftig festgestellten Forderungen zulässig" | Zulässig (entspricht § 309 Nr. 3 BGB) | 🟢 |
| **Rücktritts-Beschränkung** | „Ein Rücktritt ist nur aus wichtigem Grund möglich" | Aushebelung gesetzlicher Rücktrittsrechte | 🔴 |
| **Übergabeerklärung als Abnahmefiktion** | „Mit Übergabe gilt das Werk als abgenommen" | § 640 Abs. 2 BGB wird umgangen, problematisch | 🟠 / 🔴 |
| **Schlüsselübergabe als Abnahme** | „Die Übergabe des Schlüssels gilt als Abnahme" | Konkludente Abnahme darf nicht formularvertraglich pauschaliert werden | 🔴 |
| **Schiedsklausel** | „Streitigkeiten entscheidet ein Schiedsgericht" | Bei Verbrauchern: § 1031 Abs. 5 ZPO Form erforderlich; meist 🔴 |
| **Beweislastumkehr — § 309 Nr. 15a BGB** | „Der Erwerber trägt die Beweislast für das Vorliegen eines Mangels bei Gefahrübergang" / „Verzögerungen gelten als nicht vom Bauträger verschuldet, sofern der Erwerber nicht das Gegenteil nachweist" | **Direkter Verstoß gegen § 309 Nr. 15 lit. a BGB** — Klausel unwirksam | 🔴 |
| **Pauschale Empfangs-/Kenntnisnahmebestätigung — § 309 Nr. 15b BGB** | „Der Erwerber bestätigt, die Baubeschreibung erhalten und geprüft zu haben" / „Der Erwerber bestätigt, über alle wesentlichen Risiken aufgeklärt worden zu sein" | **Direkter Verstoß gegen § 309 Nr. 15 lit. b BGB** — Klausel unwirksam | 🔴 |
| **Ausschluss / Verschweigen § 650m BGB (5 %-Sicherheitseinbehalt)** | Im Vertrag fehlt jeder Hinweis auf den 5 %-Sicherheitseinbehalt nach § 650m BGB; ggf. ausdrückliche Ausschlussklausel | Aushöhlung zwingenden Verbraucherrechts — Klausel unwirksam; **Pflicht-Prüfblockverstoß** | 🔴 |
| **Vormerkungslöschung bei einseitiger Verzugsmitteilung** | „Der Erwerber bewilligt schon jetzt die Löschung der Auflassungsvormerkung, sobald der Bauträger den Verzug des Erwerbers anzeigt" | Aushöhlung der dinglichen Sicherung; Druckmittel des Bauträgers — unangemessene Benachteiligung § 307 BGB | 🔴 |
| **Schlüsselübergabe nur gegen vollständige Zahlung („ohne Geld keine Schlüssel")** | „Die Schlüsselübergabe erfolgt erst nach vollständiger Zahlung aller Raten einschließlich Schlussrate" | Aushöhlung Zurückbehaltungsrecht § 641 Abs. 3 BGB; bei Restmängeln muss Schlüssel auch Zug-um-Zug gegen Schlussrate (minus Einbehalt) übergeben werden | 🔴 |
| **Anteilige Sachverständigenkosten für Bauträger-Gutachter** | „Die Kosten des vom Bauträger zu benennenden Sachverständigen für die technische Abnahme tragen die Erwerber anteilig" | Faktische Selbstabnahme + Kostenabwälzung; doppelter Verstoß | 🔴 |

## B.3 — Strategie bei AGB-Verstößen

- **Vor Beurkundung:** Klausel streichen lassen — das ist meist möglich, weil der Notar zur Verbraucherbelehrung verpflichtet ist (§ 17 BeurkG).
- **Nach Beurkundung:** Berufung auf Unwirksamkeit nach § 307 BGB; AGB-rechtlich unwirksame Klauseln entfallen ersatzlos (kein geltungserhaltende Reduktion).
- **Im Streitfall:** Klage auf Feststellung der Unwirksamkeit oder unmittelbare Anwendung der gesetzlichen Regel.

---

# Teil C — Leistungsbeschreibung, Baubeschreibung und Bausoll

Die Leistungs- bzw. Baubeschreibung definiert, **was geschuldet ist** (das „Bausoll"). Was nicht beschrieben ist, kann der Bauträger später bestreiten. Eine schwache oder lückenhafte Leistungsbeschreibung ist die **häufigste** Streitquelle in Bauträgerverträgen — vor MaBV-Verstößen, vor Abnahmestreit, vor Vertragsstrafenfragen.

**Terminologie.** „Leistungsbeschreibung" und „Baubeschreibung" werden in der Praxis oft synonym verwendet. Manche Verträge führen sie als ein Dokument, andere trennen sie (z. B. „Baubeschreibung" für das Gebäude und „Leistungsbeschreibung" für Ausstattung, Außenanlagen, technische Gewerke). Rechtlich entscheidend ist nicht der Begriff, sondern: **Was wurde wirksam zum Vertragsinhalt gemacht?** Nur was **mitbeurkundet** ist (§ 311b BGB), ist sicher Vertragsbestandteil. Lose Anlagen, Prospekte oder „Bemusterungslisten" sind im Streitfall häufig nicht durchsetzbar.

## C.0 — Pflicht-Check Leistungsbeschreibung

| Prüfpunkt | Soll | Mangel | Ampel |
| --- | --- | --- | --- |
| Mitbeurkundung | Bestandteil der Urkunde oder mitverlesener Anlage | Nur lose beigefügt, „liegt vor", „wurde übergeben" | 🔴 |
| Eindeutige Bezeichnung | Datierte Version, Seitenzahl, Versionsindex | Undatiert, „aktuelle Fassung", mehrere Stände im Umlauf | 🔴 |
| Vollständigkeit nach § 650k Abs. 2 BGB | Alle Pflichtangaben enthalten (s. C.1) | Pflichtangabe fehlt | 🔴 pro Fehlstelle |
| Konkretheit | Konkrete Produkte/Hersteller/Klassen oder konkrete Mindeststandards | Nur Sammelbegriffe („hochwertig", „marktüblich") | 🔴 / 🟠 |
| Bemusterungsbudget | Pro Gewerk in Euro/m² oder als Stückzahl beziffert | Nur „im Preis enthalten, soweit Standard" | 🟠 |
| Energie-/GEG-Standard | Konkrete KfW-/Effizienzhaus-Klasse benannt | „geltendes Recht", „GEG-konform" ohne Klasse | 🔴 |
| Toleranzen | Wohnfläche mit Toleranzangabe (z. B. ± 3 %) auf Basis WoFlV | Keine Toleranz, keine Grundlage, DIN 277 ohne Hinweis | 🟠 / 🔴 |
| Vorrangregel | Klausel zur Konfliktauflösung: Mitbeurkundetes vor Anlage, Plan vor Text usw. | Keine Regel — Streit vorprogrammiert | 🟠 |
| Schaufenster-Vergleich | Prospekt-/Exposé-Aussagen mit Leistungsbeschreibung abgleichen | Werbeaussagen nicht im Vertrag wiederzufinden | 🔴 (Werbung ist nicht geschuldet, wenn nicht beurkundet) |

**Praxisregel:** Wer ein 30-seitiges Hochglanz-Exposé erhält, aber im Vertrag nur eine 4-seitige Baubeschreibung mit Pauschalverweisen findet, hat ein klassisches Schaufenster-Pattern. Werbeangaben sind nach BGH-Linie nur dann geschuldet, wenn sie zum Vertragsinhalt gemacht wurden — sonst nicht durchsetzbar.

## C.1 — Pflichtangaben nach § 650k BGB (analog für Bauträger)

| Pflichtangabe | Inhalt | Ampel bei Fehlen |
| --- | --- | --- |
| Art und Umfang der Bauleistung | Vollausstattung Sondereigentum + Gemeinschaftsanteil | 🔴 |
| Wesentliche Eigenschaften | Wohnflächen, Raumhöhen, Energie-Standard | 🔴 |
| Gebäudedaten | Bauart, Bauweise, Baustoffe | 🟠 |
| Innenausbau-Standards | Bodenbeläge, Sanitär, Türen, Fenster, Heizung | 🟠 |
| Technik | Lüftung, Sanitärtechnik, Elektrik, Smart-Home | 🟠 |
| Energiestandard | KfW-Effizienzhaus-Klasse, GEG-Konformität | 🔴 |
| Außenanlagen | Grundstücksbefestigung, Terrasse, Garten, Carport | 🟠 |
| Verbindlicher Fertigstellungstermin | Konkretes Datum oder enger Zeitraum | 🔴 |

## C.2 — Wohnflächenberechnung

| Berechnungsgrundlage | Folge | Ampel |
| --- | --- | --- |
| WoFlV (Wohnflächenverordnung) | Verbraucherfreundlich, abgestufte Anrechnung | 🟢 |
| DIN 277 | Höhere Werte, ungünstiger für Erwerber | 🟠 |
| Keine Angabe | Streit vorprogrammiert | 🔴 |
| „Circa-Angabe ohne Toleranz" | Praktisch unwirksam | 🔴 |
| Toleranz > 3 % | BGH-kritisch | 🟠 |

## C.3 — Bemusterungsklauseln

Die Bemusterung ist die Phase, in der der Erwerber Bodenbeläge, Sanitär, Fliesen usw. auswählt. Häufige Fallen:

| Klausel | Bedeutung | Ampel |
| --- | --- | --- |
| „Bemusterung erfolgt beim vom Bauträger benannten Bemusterungshaus" | Eingeschränkte Auswahl | 🟠 |
| „Mehrkosten werden gesondert berechnet" — ohne Aufschlüsselung | Intransparenz | 🟠 |
| „Mehrkostenpauschale 20 %" | Häufig unangemessen | 🔴 |
| „Sonderwünsche sind sofort fällig" | Außerhalb des MaBV-Ratenplans → 🔴 |
| „Bemusterungsfrist 4 Wochen, danach Standardausstattung" | Erwerberdruck, oft 🟠 |
| „Aufzahlung bei Materialwechsel zum Listenpreis +50 %" | Intransparent, 🔴 |

## C.4 — Pauschalverweise

Pauschalverweise auf „branchenüblich" oder „allgemein anerkannte Regeln der Technik" sind **kein** Ersatz für konkrete Beschreibung. Sie können punktuell zulässig sein, dürfen aber nicht den Kern der Bauleistung ersetzen.

| Pauschalverweis | Ampel |
| --- | --- |
| „Sanitärausstattung mittlerer Art und Güte" | 🟠 |
| „Bodenbeläge nach Auswahl des Erwerbers im Rahmen der Bemusterung" | 🟢 (mit Budgetangabe) / 🔴 (ohne) |
| „Heizung nach den anerkannten Regeln der Technik" | 🟠 |
| „Energie-Standard nach geltendem Recht" | 🔴 (keine konkrete Klasse) |

---

# Teil D — Vertragsstrafen, Fertigstellungsfristen, Verzug

## D.1 — Fertigstellungstermin

| Termintyp | Bewertung | Ampel |
| --- | --- | --- |
| Konkretes Datum oder enger Zeitraum (Quartal) | Verbindlich, durchsetzbar | 🟢 |
| „voraussichtlich" + grober Zeitraum | Unverbindlich, schwer durchsetzbar | 🟠 |
| „nach Baufortschritt" ohne Datum | Praktisch wertlos | 🔴 |
| „bezugsfertig 18 Monate nach Baubeginn" | Brauchbar, wenn Baubeginn konkret | 🟢 |
| Vorbehaltsklausel „höhere Gewalt, Witterung, Baustoffknappheit" weit gefasst | Aushebelung der Verbindlichkeit | 🔴 |

## D.2 — Vertragsstrafen und pauschalierter Schadensersatz

**Begriffsabgrenzung.** Bauträgerverträge umgehen die strenge Vertragsstrafen-Rechtsprechung häufig, indem statt einer Vertragsstrafe ein **pauschalierter Schadensersatz** vereinbart wird (typisch: ein fester Betrag pro Tag und pro m² Wohnfläche). Unterschiede:

| Merkmal | Vertragsstrafe | Pauschalierter Schadensersatz |
| --- | --- | --- |
| Schädigungsnachweis nötig | nein | nein (gerade das ist der Sinn der Pauschale) |
| Weitergehender Schaden zusätzlich | nein (Anrechnung) | **ja**, wenn höher und nachgewiesen — Pauschale wird angerechnet |
| BGH-Obergrenze pro Tag | 0,2–0,3 ‰ | (nicht direkt übertragbar; AGB-Kontrolle nach § 309 Nr. 5 BGB) |
| Gesamtkappung | max. 5 % der Vertragssumme | wird in Bauträgerverträgen typischerweise ebenfalls auf 5 % gedeckelt |
| Mahnung nötig | nein (mit Terminüberschreitung) | **ja**, sobald der Termin durch nicht zu vertretende Umstände nach hinten verschoben wurde — sonst Verzugsschaden verloren |

**Praxisregel für Mandanten:** Bei pauschaliertem Schadensersatz immer mahnen, sobald der verschobene Termin verstrichen ist. Ohne Mahnung kein Verzug, ohne Verzug auch keine weitergehenden Schadensersatzansprüche (§ 286 BGB). Siehe auch [Teil J.6](#j6--vertragsstrafe-vs-pauschalierter-schadensersatz-realfall).

Wirksamkeit einer Vertragsstrafe (BGH-Linie, live verifizieren):

| Prüfpunkt | Maßstab |
| --- | --- |
| Verschulden vorausgesetzt | ja |
| Höhe pro Tag | max. 0,2–0,3 ‰ der Vertragssumme |
| Gesamthöhe | max. 5 % der Vertragssumme |
| Verzug, nicht bloße Terminüberschreitung | ja |

| Verstoß | Befund |
| --- | --- |
| Strafe unverschuldensabhängig | 🔴 |
| Strafe > 5 % | 🔴 |
| Tagessatz > 0,3 ‰ | 🟠 |
| Strafausschluss vollständig | 🔴 (massive Benachteiligung) |

## D.3 — Verzug und Schadensersatz

| Klausel | Befund |
| --- | --- |
| „Schadensersatz wegen Verzugs ausgeschlossen" | 🔴 |
| „Mietausfall wird nur bis Höhe der vereinbarten Vertragsstrafe ersetzt" | 🟠 (BGH-Linie prüfen) |
| „Anspruch auf Mehraufwand erfordert Schriftform und sofortige Anzeige" | 🟠 |
| Klausel verlangt anwaltliche Mahnung vor Verzug | 🔴 (gegen § 286 BGB) |

---

# Teil E — Abnahme, Gefahrtragung, Mängelrechte, Gewährleistung

Die Abnahme ist der **wichtigste Zeitpunkt** im Bauträgervertrag. Sie löst aus: Gefahrübergang, Beweislastumkehr für Mängel, Beginn der Gewährleistungsfrist, Fälligkeit der Schlussrate.

## E.1 — Doppelabnahme bei Eigentumswohnungen

Bei Eigentumswohnungen sind **zwei Abnahmen** zu unterscheiden:

| Abnahme | Gegenstand | Wer nimmt ab |
| --- | --- | --- |
| Sondereigentum | Wohnung des Erwerbers | Erwerber persönlich |
| Gemeinschaftseigentum | Treppenhaus, Dach, Fassade, Heizung, Außenanlagen | Eigentümergemeinschaft (Verwaltung mit Beschluss) bzw. jeder einzelne Erwerber selbst |

**Wichtigster Fallstrick:** Klauseln, die die Abnahme des Gemeinschaftseigentums dem Bauträger, einem von ihm benannten Sachverständigen oder dem (oft vom Bauträger eingesetzten) Erstverwalter übertragen, sind nach ständiger BGH-Rechtsprechung unwirksam (live verifizieren — BGH zur Selbstabnahme).

| Klausel | Ampel |
| --- | --- |
| „Abnahme des Gemeinschaftseigentums durch den Bauträger" | 🔴 |
| „Abnahme durch vom Bauträger benannten Sachverständigen" | 🔴 |
| „Abnahme durch den vom Bauträger bestellten Erstverwalter" | 🔴 |
| „Abnahme durch einen vom Erwerber zu wählenden Sachverständigen" | 🟢 |
| „Mit Einzug gilt das Werk als abgenommen" | 🔴 (Abnahmefiktion bei Verbraucherbauvertrag eng begrenzt, § 640 Abs. 2 BGB) |

## E.2 — Abnahmefiktion (§ 640 Abs. 2 BGB)

§ 640 Abs. 2 BGB regelt die fiktive Abnahme nach Fristsetzung. Im Verbraucherbauvertrag gilt sie nur mit Belehrung. Bauträgerverträge unterliegen § 650u BGB — die Belehrungspflicht ist umstritten. Strenge Klauseln gehören zu prüfen.

## E.3 — Gefahrtragung

| Klausel | Befund |
| --- | --- |
| Gefahrübergang mit vollständiger Abnahme | 🟢 |
| Gefahrübergang schon mit Übergabe / Schlüsselübergabe | 🟠 |
| Gefahrübergang „mit Beginn der Schlüsselübergabe für Bemusterungstermine" | 🔴 |

## E.3a — 5 %-Sicherheitseinbehalt nach § 650m BGB (Pflichtpunkt)

§ 650m BGB gibt dem Verbraucher das Recht, **bei der ersten Abschlagszahlung 5 %** der Gesamtvergütung einzubehalten oder Sicherheit zu verlangen. Dies ist **zwingendes Verbraucherrecht** — jeder Ausschluss oder jedes Verschweigen ist eine unangemessene Benachteiligung.

| Befund | Bewertung |
| --- | --- |
| Vertrag enthält klare Belehrung über 5 %-Einbehalt | 🟢 |
| Vertrag schweigt zum 5 %-Einbehalt | 🔴 (zwingendes Recht verschwiegen) |
| Vertrag schließt Einbehalt ausdrücklich aus | 🔴 (offensichtlich unwirksam) |
| Vertrag senkt Einbehalt auf < 5 % | 🔴 |
| Vertrag stellt Sicherheit nur gegen pauschale Kosten zur Verfügung | 🟠 (Detail prüfen) |

**Praxiswichtig:** In vielen Bauträgerverträgen wird § 650m BGB schlicht **nicht erwähnt**. Das alleine ist bereits ein Hauptbefund, der im Mandantenbericht vor jedem anderen Punkt erscheinen muss. Konsequenz: AGB-Verstoß § 307 BGB; bei massivem Häufungsbild Hinweis auf Notarhaftung § 19 BNotO (siehe [Teil I](#teil-i--nichtigkeitsrisiken-transparenzgebot-und-notarhaftung)).

## E.4 — Mängelrechte und Verjährung

| Punkt | Gesetz | Bewertung |
| --- | --- | --- |
| Verjährung | § 634a Abs. 1 Nr. 2 BGB: 5 Jahre ab Abnahme | 🟢 |
| Verkürzung in AGB | unwirksam | 🔴 wenn vereinbart |
| Verlängerung in Vertrag | zulässig | 🟢 |
| Nacherfüllungsvorrang | § 635 BGB | 🟢 |
| Selbstvornahme nach Fristsetzung | § 637 BGB | 🟢 |
| Minderung statt Rücktritt | § 638 BGB | 🟢 |
| Schadensersatz | §§ 634 Nr. 4, 280 ff. BGB | 🟢 |

| Klausel | Befund |
| --- | --- |
| „Mängelanzeige binnen 14 Tagen nach Entdeckung" | 🔴 (verschuldensunabhängige Ausschlussfrist) |
| „Mängelrechte erlöschen bei Veräußerung der Wohnung" | 🔴 |
| „Geringfügige Mängel werden nicht beseitigt" | 🔴 (Aushöhlung Nacherfüllungsanspruch) |
| „Mängelbeseitigung erfolgt durch vom Bauträger benannten Handwerker" | 🟠 |

## E.4a — Selbstvornahmeausschluss § 637 BGB

In vielen Bauträgerverträgen ist das Selbstvornahmerecht des Erwerbers nach § 637 BGB **formularvertraglich ausgeschlossen**. Die Wirksamkeit dieser Klausel ist höchstrichterlich nicht abschließend geklärt; der Streit ist offen — und damit für den Erwerber **angreifbar**, weil eine wirksamkeitsfreundliche Auslegung die unangemessene Benachteiligung nach § 307 BGB nähert.

| Klausel | Befund |
| --- | --- |
| „Selbstvornahmerecht nach § 637 BGB ausgeschlossen" | 🟠–🔴 (Rechtslage offen, im Streitfall angreifbar) |
| „Selbstvornahme erst nach zweimaligem Fehlschlagen der Nacherfüllung" | 🟠 |
| Selbstvornahme nur mit vorheriger schriftlicher Zustimmung des Bauträgers | 🔴 (Aushöhlung) |
| Selbstvornahme im Rahmen der gesetzlichen Voraussetzungen offen | 🟢 |

**Argumentationslinie für den Erwerber:** Bei Verzug des Bauträgers mit der Nacherfüllung darf der Besteller nach allgemeinen werkvertraglichen Grundsätzen auf Kosten des Unternehmers Mängel beseitigen lassen. Dies vor Schriftsatzverwendung mit konkreter, live verifizierter BGH-Entscheidung zu § 637 BGB und zur neueren Schadensersatzlinie unterlegen. Praktische Vertiefung: [Teil J.9](#j9--selbstvornahmeausschluss--6374-realfall).

## E.5 — Schlussrate und Zurückbehaltungsrecht

§ 641 Abs. 3 BGB: Bei Mängeln kann der Erwerber das **doppelte der voraussichtlichen Mängelbeseitigungskosten** der Schlussrate einbehalten.

| Klausel | Befund |
| --- | --- |
| Pauschaler Einbehaltsausschluss | 🔴 |
| Einbehalt nur in Höhe der einfachen Beseitigungskosten | 🔴 (§ 641 Abs. 3 BGB verlangt das Doppelte) |
| Einbehalt erfordert Sachverständigengutachten | 🟠 |
| Einbehalt nur bei wesentlichen Mängeln | 🟠 |

---

# Teil F — Eigentumsschutz, Auflassungsvormerkung, Freistellung, Insolvenz

Ohne dingliche Sicherung ist jede Zahlung ein Insolvenzrisiko. Die Auflassungsvormerkung ist das **wichtigste Schutzinstrument** des Erwerbers.

## F.1 — Auflassungsvormerkung (§§ 883 ff. BGB)

| Prüfpunkt | Soll | Befund bei Verstoß |
| --- | --- | --- |
| Bewilligt | ja, im Vertrag | 🔴 wenn fehlt |
| Eintragung im Grundbuch | vor erster Zahlung | 🔴 wenn nachher |
| Rang | erstrangig (ggf. Gleichrang nur mit Finanzierungsgrundschuld der Erwerberbank) | 🔴 wenn nachrangig zu Bauträger-Banken |
| Beschränkung auf Wohneinheit | konkret bezeichnet | 🟠 wenn pauschal |

## F.2 — Lastenfreistellung (§ 3 Abs. 1 Nr. 3 MaBV)

Der Bauträger finanziert das Bauvorhaben oft über Grundschulden zugunsten einer Bank. Diese Grundschulden müssen bei Übertragung an den Erwerber gelöscht oder dahingehend freigegeben werden, dass die Erwerberwohnung lastenfrei bleibt. Dies erfolgt durch eine **Freistellungserklärung** der finanzierenden Bank des Bauträgers.

| Inhalt der Freistellungserklärung | Befund bei Verstoß |
| --- | --- |
| Bedingungsfreie Freistellung gegen Zahlung der Schlussrate | 🟢 |
| Freistellung nur bei Bauvollendung | 🟠 (Streit über Bauvollendung möglich) |
| Freistellung erfordert vollständige Kaufpreiszahlung | 🔴 (nicht MaBV-konform) |
| Freistellungsbetrag = anteiliger Kaufpreis | 🟢 |
| Freistellungsbetrag = Gesamtkaufpreis | 🔴 |

## F.3 — Eigentumsumschreibung

Eigentum geht erst über mit **Eintragung im Grundbuch** nach Auflassung (§ 925, § 873 BGB). Bis dahin ist der Erwerber „werdender Eigentümer" — die Vormerkung sichert ihn dinglich.

## F.4 — Bauträger-Insolvenz

| Szenario | Schutzlage Erwerber |
| --- | --- |
| Insolvenz vor erster Zahlung | Keine Verluste; Vertrag wird im Insolvenzverfahren oft fortgeführt oder aufgehoben |
| Insolvenz nach Teilzahlungen, Bau steht | Vormerkung schützt; Erwerber kann Fortsetzung verlangen oder neuen Bauträger beauftragen — Reste-Bau finanziert er selbst |
| Insolvenz nach Teilzahlungen, Bau läuft weiter (Sanierung) | Sachwalter / Verwalter führt Verträge fort |
| Insolvenz nach Übergabe vor Eigentumsumschreibung | Vormerkung sichert dinglichen Übertragungsanspruch |
| Bürgschaftsmodell (§ 7 MaBV) | Bürgschaft greift; Bank zahlt zurück |

**Faustregel:** Bei Bauträger-Insolvenz ist die Vormerkung der wichtigste Schutz. Wer ohne Vormerkung gezahlt hat, ist einfacher Insolvenzgläubiger.

---

# Teil G — Mandatsmodule: Nachverhandlung, Rücktritt, Klage

## G.1 — Nachverhandlung vor Beurkundung

### Funktion

Der Notarentwurf ist der **beste Verhandlungszeitpunkt**. Nach Beurkundung sind Änderungen aufwändig (neue Beurkundung). Vor Beurkundung sind Streichungen und Einfügungen meist problemlos.

### Aufbau Korrekturbrief an Bauträger/Notar

1. Bezugnahme: Notarentwurf vom [Datum], geplanter Termin am [Datum].
2. Verbraucher mit vollem Namen, Geburtsdatum, Adresse.
3. Punktweise Beanstandung: Klausel-Nr. · Originaltext · Verstoß · Vorschlag.
4. Fristsetzung: Übersendung des überarbeiteten Entwurfs bis [Datum].
5. Hinweis: Ohne Korrektur Beurkundung nicht möglich.

### Mustertext

> Sehr geehrte Damen und Herren,
>
> wir nehmen Bezug auf den Notarentwurf vom [Datum], geplanter Beurkundungstermin [Datum, Uhrzeit] in der Kanzlei Notar [Name]. In Vertretung des Erwerbers, Herrn/Frau [Name], beanstanden wir folgende Punkte:
>
> **§ X — Ratenplan.** Originaltext: „[…]". Der Ratenplan entspricht nicht § 3 Abs. 2 MaBV; konkret ist die [n-te] Rate mit [Y] % statt der zulässigen [Z] % bemessen. Wir bitten um Anpassung auf den Standard-Ratenplan der MaBV.
>
> **§ X — Abnahme Gemeinschaftseigentum.** Originaltext: „[…]". Die Klausel überträgt die Abnahme dem Bauträger bzw. einem von ihm benannten Sachverständigen. Nach ständiger BGH-Rechtsprechung ist dies unwirksam. Wir bitten um folgende Neufassung: „[…]".
>
> **§ X — Gewährleistung.** Originaltext: „[…]". Die Verkürzung auf zwei Jahre verstößt gegen § 634a Abs. 1 Nr. 2 BGB. Wir bitten um Streichung dieser Klausel.
>
> **§ X — Vertragsstrafe.** Originaltext: „[…]". Die Vertragsstrafe ist mit [Höhe] unverhältnismäßig. Wir bitten um Anpassung auf maximal 5 % der Vertragssumme, Tagessatz maximal 0,3 ‰.
>
> [weitere Punkte analog]
>
> Wir bitten um Übersendung eines überarbeiteten Entwurfs bis zum [Datum]. Ohne entsprechende Korrektur kann die Beurkundung am [Termin] nicht stattfinden.
>
> Mit freundlichen Grüßen
> [Erwerber / Anwalt]

## G.2 — Verhandlung nach Beurkundung

Bei bereits beurkundetem Vertrag sind drei Wege denkbar:

1. **Außergerichtliche Verhandlung** mit Verweis auf AGB-Unwirksamkeit nach § 307 BGB. Bauträger akzeptiert oft, weil die Klausel ohnehin nicht trägt.
2. **Notarielle Nachbeurkundung** einer Korrekturvereinbarung — aufwändig, aber rechtssicher.
3. **Berufung auf Unwirksamkeit im Streitfall** — gesetzliche Regel greift dann automatisch, AGB-Klausel entfällt.

## G.3 — Rücktritt und Kündigung

### Rücktrittsgründe vor Bauvollendung

| Grund | Vorschrift | Wirkung |
| --- | --- | --- |
| Bauträger gerät in Verzug, Frist abgelaufen | § 323 BGB | Rücktritt möglich, Rückzahlungsanspruch |
| Bauträger leistet nicht (Bauverzögerung über Jahre) | § 323 BGB | wie oben |
| Anfänglicher Mangel der Baubeschreibung mit irreparabler Wirkung | § 326 Abs. 5 BGB | Rücktritt möglich |
| Bauträger-Insolvenz | Insolvenzverwalter entscheidet über Erfüllung (§ 103 InsO) | Wahlrecht Verwalter |
| Treuwidrige Vertragsänderung durch Bauträger | § 313 BGB | Anpassung oder Rücktritt |

### Kündigung nach Abnahme

Reine Mängelrechte (§§ 634 ff. BGB) — kein Rücktritt mehr, sondern Nachbesserung, Minderung, Schadensersatz.

### Mustertext Rücktrittserklärung

> Sehr geehrte Damen und Herren,
>
> wir nehmen Bezug auf den notariellen Bauträgervertrag vom [Datum], URNr. [Nummer]/[Jahr] des Notars [Name].
>
> In Vertretung unseres Mandanten, Herrn/Frau [Name], erklären wir hiermit den **Rücktritt** vom Vertrag, gestützt auf § 323 Abs. 1 BGB. Trotz schriftlicher Mahnung vom [Datum] und Fristsetzung zur Fertigstellung bis zum [Datum] ist die Bauleistung bis heute nicht erbracht.
>
> Die Voraussetzungen des § 323 BGB liegen vor: [genaue Aufzählung — Vertrag, Fälligkeit, Mahnung, Fristsetzung, Fristablauf, keine Erfüllung].
>
> Wir fordern Sie zur Rückzahlung der bisher geleisteten [Betrag] EUR bis zum [Datum] auf. Eine Rückübertragung der eingeräumten Auflassungsvormerkung bieten wir Zug-um-Zug an.
>
> Sollte die Rückzahlung nicht fristgerecht erfolgen, werden wir Klage zum zuständigen Landgericht erheben.
>
> Mit freundlichen Grüßen

## G.4 — Klagestrategie

### Klagearten

| Klageziel | Klageart | Streitwert |
| --- | --- | --- |
| Rückzahlung geleisteter Raten nach Rücktritt | Leistungsklage | volle gezahlte Summe |
| Feststellung der Unwirksamkeit einzelner Klauseln | Feststellungsklage | 50 % des wirtschaftlichen Interesses |
| Mängelbeseitigung (Nacherfüllung) | Leistungsklage | Kosten der Mängelbeseitigung |
| Schadensersatz wegen Mängeln | Leistungsklage | Schadenssumme |
| Auflassung / Eigentumsumschreibung | Leistungsklage | Verkehrswert |
| Schlussratenrückforderung | Leistungsklage | Schlussratenbetrag |

### Gerichtszuständigkeit

| Streitwert | Gericht |
| --- | --- |
| bis 5.000 € | Amtsgericht |
| über 5.000 € | Landgericht |
| Bei Verbrauchern | Wohnsitzgerichtsstand möglich (§ 29c ZPO) |

### Beweismittel

- Bauträgervertrag (notarielle Urkunde).
- Baubeschreibung.
- Schriftverkehr (E-Mail, Brief).
- Bautagebücher des Bauträgers.
- Sachverständigengutachten.
- Zeugen: Bauleiter, Handwerker, Architekt, Bauüberwacher.
- Fotos vom Baufortschritt.

### Beweislast

| Sachverhalt | Beweislast |
| --- | --- |
| Vor Abnahme: Werkleistung mangelfrei erbracht | Bauträger |
| Nach Abnahme: Mangel | Erwerber |
| Bauverzug | Erwerber (Fälligkeit + Verzug) |
| AGB-Charakter einer Klausel | Erwerber (Vorformulierung) |
| AGB-Unwirksamkeit nach § 307 BGB | Gericht (rechtliche Würdigung) |

### Kostenrisiko

| Punkt | Hinweis |
| --- | --- |
| Anwaltskosten | nach RVG, abhängig vom Streitwert |
| Gerichtskosten | nach GKG, abhängig vom Streitwert |
| Sachverständigenkosten | hoch (oft 3.000–10.000 €) |
| Rechtsschutzversicherung | klären, ob Bausachen mitversichert |
| Prozesskostenhilfe | bei wirtschaftlicher Bedürftigkeit |

## G.5 — Vergleichsfenster

Vor dem ersten Verhandlungstermin sind 70–80 % aller Bauträgerstreitigkeiten vergleichbar. Vorformuliertes Vergleichsangebot bereithalten:

- Nachbesserung in konkretem Umfang + Termin.
- Minderungsbetrag in EUR.
- Verlängerte Gewährleistungsfrist.
- Übernahme Sachverständigenkosten.
- Erledigungserklärung.

---

# Teil H — Musterklauseln und Sonderfälle

## H.1 — Verbraucherfreundlicher Musterabschnitt (🟢)

> **§ X Abnahme.**
> (1) Die Abnahme des Sondereigentums erfolgt durch den Erwerber persönlich nach Fertigstellung der Wohnung.
> (2) Die Abnahme des Gemeinschaftseigentums erfolgt durch einen von der Eigentümergemeinschaft bzw. — bis zur Bildung der Eigentümergemeinschaft — durch einen von jedem Erwerber selbst gewählten öffentlich bestellten und vereidigten Sachverständigen. Die Kosten trägt der Bauträger.
> (3) Eine Abnahmefiktion durch Einzug, Schlüsselübergabe oder Bezahlung der Schlussrate ist ausgeschlossen.

> **§ Y Gewährleistung.**
> (1) Es gelten die gesetzlichen Mängelrechte nach §§ 634 ff. BGB.
> (2) Die Verjährungsfrist beträgt fünf Jahre ab Abnahme (§ 634a Abs. 1 Nr. 2 BGB).
> (3) Eine Verkürzung dieser Frist ist ausgeschlossen.

> **§ Z Schlussrate.**
> Der Erwerber ist berechtigt, von der Schlussrate das Doppelte der voraussichtlichen Mängelbeseitigungskosten einzubehalten (§ 641 Abs. 3 BGB).

## H.2 — Einseitig zugunsten Bauträger (🔴)

> **§ X Abnahme.**
> Mit Schlüsselübergabe gilt das Werk als abgenommen. Eine darüber hinausgehende förmliche Abnahme findet nicht statt.

Befund: Abnahmefiktion durch Schlüsselübergabe; § 640 Abs. 2 BGB wird umgangen; Beweislastumkehr für Mängel sofort. **🔴**.

> **§ Y Gewährleistung.**
> Gewährleistungsansprüche verjähren in zwei Jahren ab Übergabe.

Befund: Verstößt gegen § 634a Abs. 1 Nr. 2 BGB (5 Jahre). AGB-rechtlich unwirksam. **🔴**.

> **§ Z Vertragsstrafe.**
> Die Vereinbarung einer Vertragsstrafe wegen Bauverzögerung ist ausgeschlossen. Schadensersatzansprüche des Erwerbers wegen Verzugs sind auf die Höhe einer ortsüblichen Vergleichsmiete für die Verzugszeit beschränkt.

Befund: Doppelte Aushebelung — Strafe ausgeschlossen, Schaden gedeckelt. **🔴**.

## H.3 — Sonderfall: Sanierung im Bestand

Bei der Bauträgerleistung im Bestand (z. B. Altbau-Sanierung mit Aufteilung in Eigentumswohnungen) gelten Besonderheiten:

| Punkt | Besonderheit | Ampel |
| --- | --- | --- |
| Baugenehmigung | oft nur Bauanzeige; Genehmigungsersatz | 🟠 |
| Bestandsschutz | Welche Mängel gelten als „Bestand" und nicht als zu sanieren? | 🟠 |
| Energiestandard | GEG-Konformität bei Sanierung weniger streng | 🟠 |
| Bemusterungsumfang | oft eingeschränkt durch Denkmalauflagen | 🟢 wenn transparent |
| Schadstoffe | Asbest, PCB, KMF: muss adressiert sein | 🔴 wenn Klausel fehlt |
| Restwertgarantie | regelmäßig fehlend | 🟠 |

## H.4 — Sonderfall: Eigentumswohnung im Geschosswohnungsbau

| Punkt | Hinweis | Ampel |
| --- | --- | --- |
| Teilungserklärung | mitbeurkunden / als Anlage | 🟢 |
| Sondernutzungsrechte (Garten, Stellplatz, Keller) | klar zugeordnet | 🟢 |
| Gemeinschaftsordnung (Hausordnung, Stimmrechte) | mitbeurkunden | 🟢 |
| Erstverwalter durch Bauträger bestellt | bis 3 Jahre OK; Kündigung möglich | 🟠 |
| Wirtschaftsplan-Vorschau | als Anlage | 🟢 wenn vorhanden |

## H.5 — Sonderfall: Reihenhaus / Doppelhaushälfte

| Punkt | Besonderheit |
| --- | --- |
| Eigenes Grundstück | Vermessung und Grenzfeststellung Pflicht |
| Nachbarbau-Risiken | Schadensersatz bei Beschädigung Reihenhausnachbar |
| Trennwand | Schallschutzklasse muss konkret benannt sein |
| Außenanlagen | Pflasterung, Einfriedung, Garten — oft Sonderpositionen |

## H.6 — Sonderfall: Bauträger-Insolvenz nach Beurkundung

Drei-Stufen-Check für Erwerber:

1. **Vormerkung im Grundbuch eingetragen?** Wenn ja, dinglich gesichert.
2. **Welche Raten bereits gezahlt?** Wenn ja, prüfen, ob Bauleistung dafür erbracht wurde.
3. **Wahl des Insolvenzverwalters nach § 103 InsO?** Erfüllt: Bau geht weiter. Verweigerung: Erwerber wird Insolvenzgläubiger für Schaden, behält aber Vormerkung.

| Stufe | Handlung |
| --- | --- |
| Sofort | Insolvenzverwalter kontaktieren, Forderung anmelden |
| Kurzfristig | Bauzustand dokumentieren (Fotos, Sachverständiger) |
| Mittelfristig | Vermarktung des Halbfertigen prüfen oder Restbau-Bauträger suchen |
| Bei Bürgschaft (§ 7 MaBV) | Bürgschaft sofort ziehen |

---

# Teil I — Nichtigkeitsrisiken, Transparenzgebot und Notarhaftung

Dieser Teil bearbeitet die schwersten Fälle: Verträge, die so weitgehend einseitig zulasten des Verbrauchers gestaltet sind, dass nicht nur einzelne Klauseln, sondern der gesamte Vertrag oder zentrale Teile davon hinfällig sein können — mit gleichzeitiger Haftungsfrage gegen den beurkundenden Notar.

## I.1 — Transparenzgebot § 307 Abs. 1 S. 2 BGB

Klauseln in AGB müssen **klar und verständlich** sein. Maßstab: Ein durchschnittlicher Verbraucher, der den Vertrag aufmerksam liest, muss seine Rechte und Pflichten erkennen können.

| Befund | Bewertung |
| --- | --- |
| Vertrag inkl. Anlagen unter 50 Seiten, klare Gliederung | 🟢 |
| 50–150 Seiten, komplexer Aufbau aber nachvollziehbar | 🟠 |
| 150–300 Seiten, mit Verweisketten und juristischer Spezialterminologie | 🔴 (Transparenzverstoß indiziert) |
| > 300 Seiten, mehrere Untergemeinschaften, juristisch nur mit Spezialwissen erschließbar | 🔴 schwerwiegend (typischer Fall der Großprojekt-Verbrauchertäuschung) |
| Wesentliche Verbraucherrechte versteckt in Anlage 7 von 12 | 🔴 |
| Wesentliche Belehrungen (§ 650m, § 309 Nr. 15) fehlen ganz | 🔴 (kumulativ mit anderen Punkten) |

**Rechtsfolge:** Intransparente Klauseln sind nach § 307 Abs. 1 S. 2 BGB **unwirksam**. Bei kumulativem Häufungsbild kann der Vertrag im Verbraucherinteresse insgesamt einer strengeren Auslegung unterliegen (§ 305c Abs. 2 BGB — Auslegung zugunsten des Verbrauchers).

## I.2 — Teil- und Gesamtnichtigkeit nach § 139 BGB

Ein Bauträgervertrag ist nicht schon dann nichtig, wenn einzelne Klauseln AGB-rechtlich unwirksam sind — die unwirksamen Klauseln entfallen ersatzlos, der übrige Vertrag bleibt grundsätzlich bestehen (§ 306 BGB). Anders aber, wenn:

| Fallgruppe | Folge |
| --- | --- |
| Verstoß gegen Beurkundungsformerfordernis (§ 311b BGB) | **Gesamtnichtigkeit** |
| Kernpflichten des Verbraucherschutzes ausgehöhlt (mehrere Pflicht-Prüfblock-Punkte zugleich verletzt) | Indiz für Gesamtnichtigkeit nach § 139 BGB — Vertrag wäre ohne die unwirksamen Klauseln vom Verbraucher nicht abgeschlossen worden |
| MaBV-Verstoß (§ 650v BGB i. V. m. § 3 MaBV) hinsichtlich der Zahlungsmodalitäten | **Teilnichtigkeit der Zahlungsklauseln**; gesetzlicher Ratenplan greift |
| Sittenwidrigkeit § 138 BGB (auffälliges Missverhältnis) | Gesamtnichtigkeit |
| Verstoß gegen Verbotsgesetz (z. B. RDG bei Anwaltsumgehung) | Gesamtnichtigkeit |

**Indikatoren für Gesamtnichtigkeitsrisiko (kumulativ prüfen):**

- Mehrere Pflicht-Prüfblock-Verstöße gleichzeitig (§ 650m **und** § 309 Nr. 15a/b **und** Transparenzdefizit **und** dingliche Druckmuster).
- Vertragsumfang 250+ Seiten ohne Gliederungsleitfaden.
- Mehrere Untergemeinschaften mit verschachtelten Stimmrechten, ohne Verbraucher-Belehrung.
- Auflassungsvormerkungslöschungsbewilligung schon im Vertrag enthalten.
- Schlüsselübergabe + Vormerkungslöschung + Sachverständigenkosten-Abwälzung kombiniert.

Bei Häufung dreier oder mehr dieser Indikatoren ist im Mandantenbericht ausdrücklich ein **Gesamtnichtigkeitsrisiko nach § 139 BGB** zu vermerken und anwaltliche Prüfung dringend zu empfehlen.

## I.3 — Notarhaftung nach § 19 BNotO i. V. m. § 17 BeurkG

Der Notar ist **Schutzherr** im Beurkundungsverfahren. Pflichten:

- **§ 17 Abs. 1 BeurkG** — Pflicht zur Belehrung über rechtliche Tragweite, Risiken, Folgen.
- **§ 17 Abs. 2a BeurkG** — bei Verbraucherverträgen verstärkte Belehrungspflicht; Verbraucher soll Zeit zur Prüfung haben (in der Praxis: Entwurfsversand mindestens 2 Wochen vor Beurkundung).
- **§ 14 BNotO** — Unparteilichkeit; der Notar darf **nicht** einseitig den Bauträger berücksichtigen.
- **§ 4 BeurkG** — Pflicht zur Prüfung des Inhalts auf rechtliche Bedenken, insbesondere AGB-Wirksamkeit.

### Haftungsanspruch des Verbrauchers

**§ 19 BNotO** — Notar haftet für **vorsätzlich oder fahrlässig** verursachten Schaden bei Verletzung von Amtspflichten.

| Voraussetzung | Prüfung |
| --- | --- |
| Amtspflichtverletzung | Belehrung über § 650m unterlassen? Belehrung über § 309 Nr. 15a/b unterlassen? Unparteilichkeit verletzt? Prüfungspflicht verletzt? |
| Schaden | Konkrete Vermögenseinbuße des Erwerbers (z. B. nicht durchsetzbarer Einbehalt, mängelbehaftetes Eigentum) |
| Kausalität | Bei pflichtgemäßer Belehrung hätte der Erwerber den Vertrag nicht oder anders abgeschlossen |
| Verschulden | bei evident verbraucherfeindlichen Klauseln regelmäßig zumindest Fahrlässigkeit |
| Subsidiarität (§ 19 Abs. 1 S. 2 BNotO) | Kein anderweitiger Ersatz vom Bauträger durchsetzbar (z. B. Insolvenz) |

### Indikatoren für Notarhaftung

- Notar wurde vom Bauträger benannt und beurkundete für Dutzende oder Hunderte Erwerber denselben verbraucherfeindlichen Vertrag.
- Entwurf wurde dem Verbraucher erst kurz vor oder während des Beurkundungstermins ausgehändigt (Verstoß § 17 Abs. 2a BeurkG).
- Pflichtbelehrungen zu § 650m BGB, MaBV, Eigentumsschutz, AGB-Klauseln fehlen im Protokoll.
- Notar protokolliert pauschale Empfangsbestätigungen, statt einzeln zu belehren.
- Notar hat offensichtlich gegen § 309 Nr. 15a/b verstoßende Klauseln beurkundet, ohne darauf hinzuweisen.

### Beschwerden und Disziplinarverfahren

- **Notarprüfung** beim zuständigen Landgericht / Oberlandesgericht (Notaraufsicht).
- **Notarkammer** als Berufsorganisation (Beschwerdemöglichkeit).
- **Disziplinarmittel** nach BNotO (Verweis, Geldbuße bis Amtsverlust).
- **Zivilklage auf Schadensersatz** beim Landgericht.

In der Praxis wird die Notaraufsicht oft erst aktiv, wenn mehrere Erwerber kollektiv Beschwerde einlegen. Bei Großprojekten (200+ Wohneinheiten) mit identischem Vertragsmuster lohnt sich die **kollektive Beschwerde**.

## I.4 — Mustertext: Hinweis auf Nichtigkeitsrisiko im Korrekturbrief

> Sehr geehrte Damen und Herren,
>
> wir nehmen Bezug auf den notariellen Entwurf vom [Datum] zum Bauträgervertrag über die Wohneinheit Nr. […] im Projekt [Name]. Unser Mandant hat den Entwurf in einer Fassung von [Seitenzahl] Seiten einschließlich Anlagen erhalten.
>
> Bei der Prüfung haben sich folgende **schwerwiegende Bedenken** ergeben, die einer Beurkundung in der vorliegenden Fassung entgegenstehen:
>
> 1. Der Vertrag enthält **keinen Hinweis** auf das Recht des Verbrauchers nach § 650m BGB, bei der ersten Abschlagszahlung 5 % der Gesamtvergütung als Sicherheit einzubehalten. Dieses zwingende Verbraucherrecht wird verschwiegen.
> 2. Die Klausel in § […] verlagert die Beweislast für […] auf den Erwerber. Dies verstößt direkt gegen **§ 309 Nr. 15 lit. a BGB** und ist unwirksam.
> 3. Die in § […] enthaltene pauschale Bestätigung, der Erwerber habe […] erhalten und geprüft, verstößt gegen **§ 309 Nr. 15 lit. b BGB** und ist unwirksam.
> 4. Die Klausel in § […] sieht die Löschung der Auflassungsvormerkung bereits bei einseitiger Verzugsanzeige des Bauträgers vor. Dies höhlt die dingliche Sicherung des Erwerbers in unangemessener Weise aus und verstößt gegen § 307 BGB.
> 5. Der Vertrag erfasst [Anzahl] Wohneinheiten und mehrere Untergemeinschaften auf [Seitenzahl] Seiten. Für einen durchschnittlichen Verbraucher ist die Tragweite nicht erschließbar; das Transparenzgebot § 307 Abs. 1 S. 2 BGB ist verletzt.
>
> In der Kumulation begründen diese Punkte ein **Risiko der Teil- bzw. Gesamtnichtigkeit nach § 139 BGB**. Unser Mandant behält sich vor, im Falle der Beurkundung in der vorliegenden Fassung **Notarhaftungsansprüche nach § 19 BNotO** geltend zu machen.
>
> Wir bitten den Notar als unparteiischen Sachwalter beider Vertragsteile (§ 14 BNotO, § 17 BeurkG) um überarbeitete Fassung des Entwurfs bis zum [Datum] mit den notwendigen Belehrungen und Klauselanpassungen.
>
> Mit freundlichen Grüßen
> [Anwalt / Verbraucher]

## I.5 — Eskalationskette

1. **Korrekturbrief an Notar und Bauträger** mit Hinweis auf konkrete Verstöße und Nichtigkeitsrisiko (siehe I.4).
2. **Beurkundungstermin verschieben** bis Klauseln überarbeitet sind.
3. **Beurkundung ablehnen**, wenn keine Korrektur erfolgt — alternativ Wahl eines anderen Notars.
4. **Nach erfolgter Beurkundung:** Schriftliche Mahnung an Bauträger zur Vertragsanpassung mit Hinweis auf AGB-Unwirksamkeit.
5. **Klage auf Feststellung der Unwirksamkeit einzelner Klauseln** bzw. **Klage auf Gesamtnichtigkeit nach § 139 BGB** mit Rückabwicklungsbegehren.
6. **Parallel:** Beschwerde bei der Notaraufsicht (Landgericht / Oberlandesgericht); ggf. kollektiv mit anderen betroffenen Erwerbern.
7. **Notarhaftungsklage § 19 BNotO** bei Insolvenz des Bauträgers oder anderweitig nicht durchsetzbarem Anspruch.

---

# Teil J — Realfall-Pattern aus Großprojekten (Anschauungsmaterial)

Dieser Teil sammelt die wiederkehrenden Klausel- und Verhandlungsmuster, die in realen, beurkundeten Bauträgerverträgen aus Berliner Großprojekten (Quartiers- und Mehrhausanlagen mit 100+ Einheiten, Untergemeinschaften, Bezugsurkunden-Technik) beobachtet wurden — zusammen mit den Punkten, die anwaltliche Gutachten an solchen Verträgen typischerweise beanstanden. Die Muster sind anonymisiert (kein realer Verkäufer-, Notar- oder Erwerbername). Sie dienen als Lernmaterial: So sieht ein handwerklich solider, aber verbraucher-ungleichgewichtiger Bauträgervertrag aus, und so liest sich die strukturierte Prüfung dazu.

Teil J ersetzt keinen Prüfungsschritt aus Teilen A–I, sondern liefert die Wiedererkennungs-Muster: Wenn dir eines dieser Patterns im Vertrag begegnet, springst du in den dort genannten Prüfteil und arbeitest die konkreten Befunde aus.

## J.0 — Strukturmerkmale eines Großprojekts-Bauträgervertrags

| Strukturmerkmal | Was du im Vertrag siehst | Wo geprüft |
| --- | --- | --- |
| Wohnungsbauträgervertrag mit Auflassung in einer Urkunde | Überschrift; §§ zu Kaufgegenstand, Bauleistung, Auflassung im selben Dokument | Pflicht-Prüfblock; [Teil F](#teil-f--eigentumsschutz-auflassungsvormerkung-freistellung-insolvenz) |
| Bezugsurkunden (Teilungserklärung mit mehreren Nachträgen, separate Baubeschreibung) per § 13a BeurkG | § 0.2/0.3 verweist auf weitere UR-Nrn., „auf Vorlesen wurde verzichtet" | [Teil C](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll); J.1 |
| Untergemeinschaften in der Gemeinschaftsordnung | Teil 3 der Teilungserklärung: pro Haus eine Untergemeinschaft, eigene Kostentragung | [Teil F](#teil-f--eigentumsschutz-auflassungsvormerkung-freistellung-insolvenz); J.2 |
| Planungs- und Änderungsvorbehalt des Verkäufers | Vorbemerkung: „Verkäufer behält sich vor, einzelne Häuser/Bauabschnitte nicht zu errichten…" | J.3 |
| Drittwirkungsbezogene Nutzungsbedingung (z. B. Lärmschutz über Nachbarbebauung) | § 0.6: Nutzung erst nach Errichtung der Blockrandbebauung auf Nachbargrundstück | J.4 |
| 7-Raten-MaBV-Plan mit konkreten Prozentsätzen | § 3.2: 30 % → 28 % → 13,3 % → 6,3 % → 10,5 % → 8,4 % → 3,5 % | [Teil A](#teil-a--mabv-ratenplan-und-sicherheiten); J.5 |
| Erfüllungsbürgschaft 5 % nach § 650m Abs. 2/3, § 632a BGB | § 3.3: Bürgschaft eines Kreditinstituts über 5 %, treuhänderisch beim Notar | [Teil E.3a](#e3a--5-sicherheitseinbehalt-nach--650m-bgb-pflichtpunkt); J.5 |
| Pauschalierter Schadensersatz pro Tag/m² mit 5 %-Deckel statt Vertragsstrafe | § 5.7.2: EUR pro Tag und m² Wohnfläche, gedeckelt auf 5 % des Kaufpreises | [Teil D.2](#d2--vertragsstrafen-und-pauschalierter-schadensersatz); J.6 |
| Doppelabnahme SE/GE mit IHK-Sachverständigem auf Bauträgerkosten | § 6.2 + § 6.3: Sondereigentum mit Erwerber, Gemeinschaftseigentum durch IHK-vereidigten Sachverständigen | [Teil E.1](#e1--doppelabnahme-bei-eigentumswohnungen); J.7 |
| Abnahmefiktion bei Nicht-Teilnahme nach Nachfrist (§ 640 Abs. 2 BGB) | § 6.2.1 letzter Absatz: 16-Tage-Nachfrist mit Belehrung | [Teil E.2](#e2--abnahmefiktion--640-abs-2-bgb); J.7 |
| § 315-BGB-Leistungsbestimmungsrecht für unbestimmte Leistungen | § 5.5: bei Lücken in der Baubeschreibung bestimmt der Verkäufer nach billigem Ermessen, „mittlere Art und Güte" | J.8 |
| Selbstvornahmeausschluss § 637 BGB | § 9.4: „Das Selbstvornahmerecht des Käufers nach § 637 BGB ist ausgeschlossen" | [Teil E.4a](#e4a--selbstvornahmeausschluss--637-bgb); J.9 |
| Wohnflächentoleranz 3 % nach WoFlV | § 5.8.2: Unterschreitung erst ab 3 % relevant | [Teil C](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll); J.10 |
| Anerkannte Regeln der Technik „zum Vertragsschluss" statt „zur Fertigstellung" | typisch in Bezugs-Baubeschreibung | J.11 |
| Disclaimer Verkaufsunterlagen (Visualisierungen, Prospekte sind nicht verbindlich) | § 5.10: Käufer bestätigt, dass keine Zusagen außerhalb der Urkunde gemacht wurden | J.12 |
| Sonderwunschvergütung pro Stunde (typisch 90 EUR/h) + Bemusterungsfrist (typisch 4 Wochen) | § 5.3: Beratungspauschale 5 h, danach Stundenhonorar | J.13 |
| Vollmacht zur Belastung und zur Teilungserklärungsänderung | § 4 + § 12: Käufer bevollmächtigt Verkäufer | J.14 |

## J.1 — Bezugsurkunden und § 13a BeurkG

Großprojekt-Verträge sind selten Einzeldokumente. Sie bestehen aus:

- Hauptvertrag (der Wohnungsbauträgervertrag mit Auflassung).
- Teilungserklärung mit Gemeinschaftsordnung als Bezugsurkunde 1, oft mit mehreren Nachträgen.
- Baubeschreibung als Bezugsurkunde 2 (eigene UR-Nummer).
- Anlagenkonvolut Pläne — typisch beim letzten Nachtrag, der die früheren Pläne ablöst.
- Anlage Ausstattungskatalog / Bemusterungs-Festlegung zum konkreten Vertrag.

Wichtig: Die Verweisung nach § 13a BeurkG macht die Bezugsurkunden zum Gegenstand der Beurkundung — die Verhandlungsbeteiligten verzichten typischerweise auf Vorlesen und Vorlage zur Durchsicht. Genau hier entstehen Risiken:

| Prüfpunkt | Befund |
| --- | --- |
| Wurden alle Bezugsurkunden dem Erwerber mindestens zwei Wochen vor dem Termin übersandt (§ 17 Abs. 2a BeurkG)? | 🔴 wenn nicht |
| Wird die zuletzt gültige Planfassung benannt (z. B. „Pläne gem. 4. Nachtrag, Anlagenkonvolut NT 4-1")? | 🟢 wenn ja, 🔴 wenn auf alte Fassung verwiesen |
| Werden die Pläne der eigenen Vorstellung mit Eintragungen im Grundriss abgeglichen (Wandverlauf, Dusche tatsächlich vorhanden, Türschlag, Steckdosenpositionen)? | 🟠 wenn nicht; spätere Änderung sehr teuer |
| Sind die Grunddienstbarkeiten der Abteilung II eingesehen worden? | 🟠 (Risiko, dass Versorgungs- oder Nachbarrechte unentdeckt bleiben) |

Mandantenhinweis: Vor Beurkundung den Grundriss endgültig prüfen. Was an Anlage 1 nicht stimmt, wird später als Sonderwunsch behandelt — mit Mehrkosten, Bemusterungsfrist und Diskussionsbedarf.

## J.2 — Untergemeinschaften nach Gemeinschaftsordnung

Großprojekte teilen das Gemeinschaftseigentum in Untergemeinschaften pro Haus (typisch in Teil 3 der Teilungserklärung, § 1 der Gemeinschaftsordnung). Die Untergemeinschaften sind hinsichtlich der Kostentragung — soweit rechtlich möglich — selbständig.

| Folge | Bewertung |
| --- | --- |
| Erwerber zahlt nur für Instandhaltung, Reparatur, Schönheitsreparaturen der eigenen Untergemeinschaft (eigenes Haus) | 🟢 |
| Keine Beteiligung an Mängelbeseitigungskosten anderer Häuser im Projekt | 🟢 |
| Prüfung nötig: Ist diese Kapselung in der Gemeinschaftsordnung tatsächlich so geregelt oder nur in der Vorbemerkung versprochen? | 🔴 wenn nur im Hauptvertrag versprochen, in der GO aber nicht abgesichert |
| Achtung bei Pflege-, Instandhaltungs-, Instandsetzungs- und Schönheitsreparaturpflichten am Gemeinschaftseigentum innerhalb des eigenen Hauses | gehört zur Untergemeinschaft — weiterhin gemeinschaftlich zu tragen |

Fehlt die Untergemeinschaft, können Erwerber an Mängelbeseitigungskosten anderer Häuser beteiligt werden, obwohl sie davon keinen Nutzen haben. Vor Beurkundung klären.

## J.3 — Planungs- und Änderungsvorbehalt des Verkäufers

In Großprojekten behält sich der Verkäufer typisch vor:

- die Anzahl der Wohn-/Teileigentumseinheiten und Stellplätze zu ändern (Zusammenlegung, Aufteilung),
- einzelne Mehrfamilienhäuser oder Bauabschnitte nicht zu errichten,
- „sonstige Änderungen der Planung" vorzunehmen, soweit erforderlich,
- die Teilungserklärung später noch zu ändern (Vollmacht durch Erwerber).

Das ist bei großen Vorhaben gängig und nachvollziehbar, hat aber Folgen für den Erwerber. Prüfraster:

| Vorbehaltsklausel | Bewertung |
| --- | --- |
| Bauträger darf einzelne Häuser nicht errichten | 🟠 (Auswirkung auf Außenanlagen, Schallschutz, Quartierscharakter) |
| Erwerber hat keinen Anspruch auf Errichtung der weiteren Häuser | 🟠 (sachgerecht, aber kommunizieren) |
| Fälligkeit der Raten hängt nur am eigenen Hausbautenstand, nicht am Gesamtprojekt | 🟢 (vorteilhaft) |
| Aber: Schallschutz oder Nutzungsvoraussetzungen hängen an Errichtung Nachbargebäude/Bauabschnitt | siehe J.4 |
| Erwerber-Duldungspflicht für Lärm/Staub durch Folgebau auch nach Übergabe | 🟠 (verhandeln: Anspruch auf Schallminderung, Sauberkeit, Wegfreiheit) |

## J.4 — Drittwirkungs-Fallen („Nutzung erst nach Nachbargebäude")

Wenn der Schallschutz im Blockinnenbereich durch eine Blockrandbebauung auf einem Nachbargrundstück sichergestellt werden muss, entstehen Risiken:

- Späte Nutzbarkeit: Die Wohnung darf erst genutzt werden, wenn die Orientierungswerte der DIN 18 005 eingehalten werden. Das kann an einem Drittprojekt hängen.
- Finanzierungsrisiko: Wenn die Fälligkeit von Ratenstufen (z. B. der 3. bis 7. Rate) an dieses Drittprojekt geknüpft ist, schwebt Bereitstellungszinsen-Risiko bei der Bank.
- Verhandlung mit der Bank: Der Erwerber muss seine finanzierende Bank über das Drittprojekt informieren und Bereitstellungszinsen-Strukturen entsprechend planen.

Prüfraster:

| Befund | Ampel |
| --- | --- |
| Vertrag verknüpft Nutzungsbeginn mit Errichtung Nachbarbau | 🟠 (sachgerecht, aber für Erwerber risikoreich) |
| Vertrag verknüpft späte Kaufpreisraten mit Drittprojekt-Voraussetzungen | 🟢 (vorteilhaft für Erwerber — keine Zahlung ohne Nutzbarkeit) |
| Aber: Bereitstellungszinsen-Risiko bei Bank | 🟠 (Mandantenhinweis nötig) |
| Keine Regelung zum Zeitpunkt der Drittbebauung | 🔴 (offenes Ende) |

## J.5 — 7-Raten-MaBV-Plan und Vertragserfüllungsbürgschaft

Der typische zusammengefasste 7-Raten-Plan nach § 3 Abs. 2 MaBV hat folgende Stichmonate (Prozentsätze sind beispielhaft, MaBV gibt nur die Stichmonate vor; die Vom-Hundert-Sätze sind vom Bauträger frei kombinierbar, soweit sie zu den Stichmonaten passen):

| Rate | Stichmonat | Beispielprozentsatz |
| --- | --- | --- |
| 1. Rate | nach Beginn der Erdarbeiten (zugleich Voraussetzung Sicherheit nach § 3.3 / § 650m) | 30,0 % |
| 2. Rate | nach Rohbaufertigstellung einschließlich Zimmererarbeiten | 28,0 % |
| 3. Rate | nach Rohinstallation Heizung, Sanitär, Elektro + Fenstereinbau (mit Verglasung) | 13,3 % |
| 4. Rate | nach Innenputz (ohne Beiputz) + Estrich | 6,3 % |
| 5. Rate | nach Dachflächen/Dachrinnen + Fassadenarbeiten + Fliesen Sanitärbereich | 10,5 % |
| 6. Rate | nach Bezugsfertigkeit, Zug um Zug gegen Besitzübergabe | 8,4 % |
| 7. Rate | nach vollständiger Fertigstellung | 3,5 % |

Prüfraster im Mandat:

- Stimmen die Stichmonate mit § 3 Abs. 2 MaBV überein? Achtung: nicht jeder Posten der Beispielzeile ist Pflicht; maßgeblich sind die MaBV-Stichmonate.
- Wird der konkrete Bautenstand vor Zahlung durch eine Bauleiterbestätigung dokumentiert? Immer fordern und vor Zahlung verifizieren (eigene Inaugenscheinnahme, ggf. Ingenieur).
- Erfüllungsbürgschaft 5 %: Wird sie mit der ersten Abschlagsrechnung tatsächlich übersandt? Wenn nicht, sind 5 % der ersten Rate als Sicherheitseinbehalt einzubehalten — zwingendes Verbraucherrecht nach § 650m BGB (siehe [Teil E.3a](#e3a--5-sicherheitseinbehalt-nach--650m-bgb-pflichtpunkt)).
- Sichert die Bürgschaft auch Schadensersatzansprüche (z. B. wegen verspäteter Übergabe), nicht nur die mangelfreie Fertigstellung? Wenn nicht: nachverhandeln.
- Wer entscheidet über Rückgabe der Bürgschaft? Wenn der Notar treuhänderisch verwahrt und der Erwerber der Rückgabe widersprechen kann (z. B. binnen 14 Tagen): 🟢.

## J.6 — Vertragsstrafe vs. pauschalierter Schadensersatz (Realfall)

In Großprojekten findet sich häufig statt einer Vertragsstrafe ein pauschalierter Tages-Schadensersatz pro m² Wohnfläche, z. B. „EUR 0,48 pro Tag und m² Wohnfläche", gedeckelt auf 5 % des Gesamtkaufpreises, mit Anrechnungsmöglichkeit weitergehender Schäden.

Mandantenhinweise:

- Der Tagessatz pro m² ist niedrig im Vergleich zum tatsächlichen Mietausfall in Großstädten (oft EUR 20–40/m² Monatsmiete). Pauschale deckt nicht den realen Schaden.
- Erwerber kann den weitergehenden Schaden (insbesondere Bereitstellungszinsen, doppelte Mietzahlung, Hotelkosten) zusätzlich geltend machen — muss ihn aber konkret darlegen und beweisen. Die Pauschale wird angerechnet.
- Bei Bauzeitverlängerung aus Gründen, die der Verkäufer nicht zu vertreten hat (höhere Gewalt, Streik, Witterung, behördliche Auflagen), verschiebt sich der Termin. Damit der Verkäufer nach Ablauf des neuen Termins in Verzug kommt, ist eine Mahnung erforderlich (§ 286 BGB). Ohne Mahnung verliert der Erwerber den Anspruch auf weitergehende Schadensersatzansprüche — ein häufiger Fehler.

Vorgehen bei Verzögerung:

1. Original-Spätesttermin im Kalender markieren.
2. Bei Verschiebung: Verzögerungsgrund schriftlich vom Verkäufer bestätigen lassen.
3. Neuen Termin festlegen (oder vom Verkäufer mitteilen lassen).
4. Nach Ablauf des neuen Termins: förmliche Mahnung mit Fristsetzung.
5. Pauschalen Schadensersatz und weitergehende Schäden parallel anmelden.

## J.7 — Doppelabnahme SE/GE mit IHK-Sachverständigem

Großprojekt-Verträge lösen die Abnahme des Gemeinschaftseigentums häufig so:

- Das Sondereigentum nimmt der Erwerber selbst ab (gemeinsame Begehung, Niederschrift).
- Das Gemeinschaftseigentum wird durch einen von der IHK benannten vereidigten Sachverständigen auf Kosten des Verkäufers begutachtet. Anschließend wird der Erwerber zur rechtsgeschäftlichen Abnahmeerklärung aufgefordert; bei Verstreichen einer Nachfrist (typisch 16 Tage) greift die Abnahmefiktion nach § 640 Abs. 2 BGB.

Prüfraster:

| Befund | Bewertung |
| --- | --- |
| IHK-vereidigter Sachverständiger durch Bauträger bestellt | 🟠 (nicht per se unwirksam, aber Indiz für Bauträger-Nähe) |
| Erwerber hat das Recht, eigenen Sachverständigen hinzuzuziehen | 🟢 (Pflicht, im Mandat empfehlen) |
| Anteilige Sachverständigenkosten beim Erwerber | 🔴 (siehe Pflicht-Prüfblock Punkt 5) |
| Abnahmefiktion bei Nicht-Reaktion nach 16-Tage-Frist | 🟠 (zulässig nur mit Belehrung nach § 640 Abs. 2 S. 2 BGB) |
| Abnahmefiktion auch ohne Anwesenheit des Erwerbers bei Begehung | 🔴 wenn Belehrung fehlt |

Mandantenhinweise:

- Eigener Ingenieur für die GE-Abnahme. Mit Abnahme beginnt die Gewährleistungsfrist, findet die Beweislastumkehr statt und wird die Schlussrate fällig. Ein IHK-Sachverständiger auf Bauträgerkosten ist nicht der Vertreter des Erwerbers.
- Rechtzeitig zur Begehung erscheinen — bei Nicht-Teilnahme greift die Fiktion.
- Mängelliste schriftlich, mit Foto, mit Zuordnung zu SE oder GE.

## J.8 — § 315-BGB-Leistungsbestimmungsrecht des Bauträgers

Typische Klausel: „Soweit die Baubeschreibung keine oder unbestimmte Angaben hinsichtlich notwendiger Leistungen enthält, ist der Verkäufer gemäß § 315 BGB zur Leistungsbestimmung nach billigem Ermessen berechtigt. Die Leistung muss mindestens von mittlerer Art und Güte sein …"

Das ist eine gefährliche Leerstelle, weil die Baubeschreibung damit gezielt Lücken lassen kann — die der Bauträger später selbst füllt.

| Prüfpunkt | Befund |
| --- | --- |
| Klausel verweist auf § 315 BGB als Lückenfüller | 🟠–🔴 (je nach Umfang der Lücken) |
| „Mittlere Art und Güte" als Mindestmaßstab | 🟠 (verbreitet, aber nicht Bausoll-konkret) |
| Klausel mit Bezugsgröße (z. B. „Fliesen mindestens EUR 35/m² Listenpreis") | 🟢 |
| Lücke betrifft Kernausstattung (Bodenbeläge, Sanitär, Türen) | 🔴 |

Verhandlungsstrategie: Statt „mittlere Art und Güte" konkrete Mindestklassen oder Mindestpreise pro Gewerk verlangen. Wer ohne konkretes Bausoll baut, baut zu Lasten des Erwerbers.

## J.9 — Selbstvornahmeausschluss § 637 (Realfall)

Typische Klausel im Mängelteil: „Das Selbstvornahmerecht des Käufers nach § 637 BGB ist ausgeschlossen."

Stand der Diskussion:

- Die formularvertragliche Ausschlussklausel ist höchstrichterlich nicht abschließend geklärt.
- Argumentationslinie für den Erwerber: Bei Verzug des Unternehmers mit der Nacherfüllung muss der Besteller die Mängel auf Kosten des Unternehmers beseitigen lassen dürfen — das ist Kernbestand des werkvertraglichen Schutzes.
- Die neuere BGH-Linie zum Schadensersatz statt der Leistung (kein abstrakter Anspruch auf Mängelbeseitigungskosten, sondern nur Minderwert) verändert die Ausgangslage zusätzlich.
- Risiko: Die Klausel kann unwirksam sein — dann gilt das Gesetz. Sie kann aber auch wirksam sein — dann hat der Erwerber den Selbstvornahmeweg verloren.

Prüfung vor Schriftsatzverwendung: Aktuelle BGH-Entscheidung zu § 637 BGB (Wirksamkeit von Ausschlussklauseln im Bauträgervertrag) live verifizieren — Gericht, Datum, Aktenzeichen, tragende Aussage. Keine Aussage aus Modellwissen verwenden.

Verhandlungsstrategie vor Beurkundung: Klausel streichen oder so umformulieren, dass Selbstvornahme nach den gesetzlichen Voraussetzungen (insbesondere bei Verzug des Bauträgers mit der Nacherfüllung) möglich bleibt.

## J.10 — Wohnflächentoleranz: 3 % ist zu viel

Typische Klausel: „Aus einer Unterschreitung der sich nach der Wohnflächenverordnung ermittelten Wohnfläche kann der Käufer nur Rechte herleiten, wenn die Abweichung 3 % unterschreitet."

Mandantenhinweise (live verifizieren, BGH-Linie):

- Die Rechtsprechung sieht Abweichungen von 1 %, eventuell auch 2 %, als geringfügig an.
- 3 % geht darüber hinaus und ist zugunsten des Erwerbers nachverhandelbar.
- Alternativ: Toleranzgrenze auf 1 % senken oder Kaufpreis um den Wert der Differenz reduzieren.

| Toleranzgrenze | Bewertung |
| --- | --- |
| 1 % | 🟢 |
| 2 % | 🟠 |
| 3 % | 🟠–🔴 (nachverhandeln) |
| > 3 % | 🔴 |
| Keine Toleranzangabe | 🔴 (Streit vorprogrammiert) |

## J.11 — „Anerkannte Regeln der Technik" — Stichtag

Typische Klausel: „Der Verkäufer hat die Leistungen nach den anerkannten Regeln der Technik zum Zeitpunkt des Vertragsschlusses zu errichten."

Problem: Zwischen Vertragsschluss und Fertigstellung können 1–3 Jahre liegen. In dieser Zeit ändern sich die anerkannten Regeln der Technik. Wer mit Stichtag Vertragsschluss baut, baut potenziell veraltet.

Verhandlungsforderung: Stichtag „zum Zeitpunkt der Fertigstellung" — das ist die verbraucherfreundlichere und sachgerechte Fassung.

| Stichtag | Bewertung |
| --- | --- |
| Zum Zeitpunkt der Fertigstellung | 🟢 |
| Zum Zeitpunkt des Vertragsschlusses | 🟠 (technisch überholbar) |
| Keine Festlegung | 🟠 (gesetzlich vermutet: Fertigstellung) |

Realistische Lage: In Großprojekten, in denen schon andere Einheiten verkauft sind, ist eine Änderung dieser Klausel zu Gunsten des einzelnen Erwerbers oft nicht durchsetzbar (Gleichbehandlung der Erwerber im selben Projekt). Dann zumindest dokumentieren, dass auf den Wunsch hingewiesen wurde.

## J.12 — Verkaufsunterlagen-Disclaimer

Typische Klausel: „Der Käufer erklärt, dass ihm von Vertriebsmitarbeitern oder anderen Beauftragten keine Zusagen zur Ausgestaltung des Kaufgegenstandes gemacht wurden, die nicht Gegenstand des vorliegenden Vertrages oder der in Bezug genommenen Urkunden sind. Visualisierungen in Verkaufsunterlagen stellen keine verbindlichen Angaben dar."

Folge:

- Was im Hochglanz-Exposé, in Visualisierungen, in Show-Wohnungen gezeigt wird, ist im Streit nicht durchsetzbar, wenn es nicht in der Baubeschreibung oder im Vertrag steht.
- Das ist ein klassisches Schaufenster-Pattern — prospektliche Highlights, vertragliche Pauschalverweise. Siehe [Teil C](#teil-c--leistungsbeschreibung-baubeschreibung-und-bausoll).

Verhandlungsstrategie:

- Vor Beurkundung abgleichen: Was im Exposé/in der Show-Wohnung versprochen wurde, muss in der Leistungsbeschreibung oder im Vertrag stehen.
- Konkrete Materialien, Hersteller, Klassen schriftlich fixieren.
- Disclaimer ist als AGB an sich nicht angreifbar — aber der materielle Schutz entsteht nur durch konkrete Bausoll-Festlegung.

## J.13 — Sonderwünsche und Bemusterung

Typische Klauseln in Großprojekten:

- Bemusterung beim vom Bauträger benannten Bemusterungspartner.
- 5 Beratungsstunden im Kaufpreis enthalten, danach EUR 90/h Beratungshonorar.
- Bemusterung innerhalb 4 Wochen nach Aufforderung; danach Standardausstattung.
- Spätere Änderungen nur, sofern der Baufortschritt es noch zulässt.
- Spätere Sonderwünsche sind separat zu zahlen und nicht im MaBV-Ratenplan enthalten.

Mandantenhinweise:

- Alle Sonderwünsche im Vertrag fixieren — als Anlage zum Vertrag, mitbeurkundet, mit Mehrpreis und Liefertermin. Spätere Wünsche kosten zusätzlich Zeit und Geld.
- Bemusterung gut vorbereiten — die 4-Wochen-Frist ist eng. Wer nicht entscheidet, bekommt Standard.
- Außerhalb der Standardausstattung mit Bezugsgröße verhandeln („Fliesen-Mehrpreis nur, wenn der Listenpreis EUR 35/m² übersteigt").
- Vorsicht bei Innentüren, Sanitär, Elektroinstallation, Bodenbelägen — hier sind Standardvarianten oft eng definiert; nachträgliche Änderungen kostspielig oder unmöglich.
- Sonderwünsche für eine Dusche, Türschlag, Steckdosen-Position frühzeitig klären — wer die Grundrissanlage nicht prüft, kann später keine Anpassung mehr durchsetzen.

## J.14 — Belastungs- und Änderungsvollmachten

Typische Vollmachten im Vertrag:

- Belastungsvollmacht (§ 4): Käufer bevollmächtigt Verkäufer, Grundpfandrechte des Käufers (Finanzierungsgrundschulden) zugunsten der finanzierenden Bank des Käufers zu bewilligen.
- Teilungserklärungs-Änderungsvollmacht (§ 12): Käufer bevollmächtigt Verkäufer, die Teilungserklärung später noch zu ändern (z. B. bei Umplanung anderer Häuser).

Prüfraster:

| Vollmachtsumfang | Bewertung |
| --- | --- |
| Belastung nur zur Finanzierung des Kaufgegenstands, betragsbegrenzt | 🟢 |
| Belastung ohne Betragsbegrenzung | 🔴 |
| Keine persönliche Haftung des Erwerbers begründbar | 🟢 |
| Teilungserklärungs-Änderung nur für andere Einheiten, nicht für die eigene | 🟢 |
| Teilungserklärungs-Änderung pauschal, auch für die eigene Einheit | 🔴 |
| Rückruf-/Widerrufsmöglichkeit | meist nicht vorgesehen; ggf. nachverhandeln |

Die Vollmachten sind bei Großvorhaben gängig und meist sachgerecht — aber im Detail prüfen, ob die eigene Einheit geschützt ist.

## J.15 — Gutachtenstruktur für den Mandantenbericht

Wenn der Skill als Vorbereitung eines anwaltlichen Gutachtens dient, folgt die Ausgabe der paragraphenweisen Gutachtenstruktur, wie sie in der Praxis tatsächlich verwendet wird:

```
Kaufvertrag
  Vorbemerkung
    Zu § 0.1: Planungsvorbehalt
    Zu § 0.6: Nutzungsvoraussetzung Nachbarbau
  § 1 Kaufgegenstand
    Zu Grundbuchauszug, Grundriss, Dienstbarkeiten
  § 2 Kaufpreis
  § 3 Kaufpreiszahlung
    Zu § 3.1: Fälligkeit
    Zu § 3.2: Ratenplan + Bautenstand-Kontrolle
    Zu § 3.3: Vertragserfüllungsbürgschaft / 5 %-Einbehalt
    Zu § 3.4: Bürgschafts-Treuhand
  § 4 Kaufpreisfinanzierung
  § 5 Baupflicht, Baubeschreibung
    Zu § 5.3: Sonderwünsche, Bemusterung
    Zu § 5.5: „Anerkannte Regeln der Technik" — Stichtag
    Zu § 5.7: Fertigstellungstermin, pauschalierter Schadensersatz
    Zu § 5.8: Wohnflächentoleranz
  § 6 Übergabe, Abnahme, Teilungserklärung
    Zu § 6.1: Leistungsverweigerungsrecht bei Mängeln
    Zu § 6.2: Abnahme Sondereigentum + Abnahmefiktion
    Zu § 6.3: Abnahme Gemeinschaftseigentum + Ingenieur
  § 7 Erschließungskosten
  § 8 Zutritt zur Baustelle
  § 9 Haftung, Mängelrechte, Verzug, Verjährung
    Zu § 9.4: Selbstvornahmeausschluss § 637 BGB
  § 10 Vormerkung
  §§ 11–16 Übrige Regelungen + Vollmachten
Baubeschreibung
  Zu Ausstattungskatalog (Anlage)
  Zu Innentüren, Elektroinstallation, Bodenbelägen, Sanitärobjekten
Teilungserklärung / Gemeinschaftsordnung
  Pflichten gegenüber anderen Eigentümern
  Untergemeinschaften
```

Stilregeln für den Mandantenbericht:

- Paragraphenweise vorgehen, jeden § explizit ansprechen — auch dann, wenn er unkritisch ist („Die Regelung in § X ist nicht zu beanstanden."). Das gibt dem Mandanten Sicherheit, dass tatsächlich alles geprüft wurde.
- Bei kritischen Punkten: Originalwortlaut zitieren, Decodierung liefern, konkreten Verhandlungsvorschlag machen.
- Realitätscheck zur Durchsetzbarkeit: Bei Großprojekten ist eine Klauseländerung zugunsten eines einzelnen Erwerbers oft nicht durchsetzbar (Gleichbehandlung). Dann mitteilen: „Hinweis: In großen Bauvorhaben gleichlautend, Änderung zu Ihren Gunsten voraussichtlich nicht möglich; zumindest dokumentieren, dass auf die Problematik hingewiesen wurde."
- Bauliche Prüfung neben rechtlicher: Bei zentralen Bausoll-Fragen (Baubeschreibung, Grundriss, Ausstattungskatalog) ausdrücklich empfehlen, einen Ingenieur hinzuzuziehen.
- Abschluss: Anbieten, die Punkte im Gespräch zu vertiefen.

## J.16 — Lehren aus realen Verträgen — die zehn häufigsten Hebel

Fasst zusammen, was aus der Praxis als „klassische Knackpunkte" bei Großprojekt-Bauträgerverträgen wiederkehrt:

1. Grundrissprüfung vor Beurkundung — Wand, Türen, Dusche, Steckdosen abgleichen; spätere Änderung wird Sonderwunsch.
2. Bezugsurkunden lesen — Teilungserklärung, Nachträge, Baubeschreibung; nicht nur das Hauptdokument.
3. Untergemeinschaften prüfen — Kostenkapselung gegen Mängel anderer Häuser?
4. Bautenstandskontrolle vor Ratenzahlung — nicht blind auf Bauleiterbestätigung verlassen.
5. 5 %-Sicherheitseinbehalt nach § 650m BGB — wenn keine Erfüllungsbürgschaft übersandt wird, einbehalten. Pflicht-Prüfblock Punkt 1.
6. Mahnung nach verschobenem Termin — sonst keine weitergehenden Verzugsansprüche.
7. Wohnflächentoleranz auf 1 % nachverhandeln — 3 % ist zu viel.
8. Selbstvornahmeausschluss § 637 BGB — angreifbar, Rechtsprechung live prüfen.
9. Doppelabnahme: eigener Ingenieur — sowohl SE als auch GE; mit Abnahme läuft Beweislastumkehr und Gewährleistungsfrist.
10. Sonderwünsche im Vertrag — was nicht beurkundet ist, kostet später Ärger; Bezugsgröße (EUR/m²) für Mehrkosten verhandeln.

---

> Ende des Skills. Bei Anwendung: Vertragstext einfügen, Sofortstart-Logik nutzt automatisch alle Teile A bis J. Pflicht-Prüfblock am Anfang — § 650m BGB, § 309 Nr. 15 lit. a BGB, § 309 Nr. 15 lit. b BGB, Transparenzgebot § 307 Abs. 1 S. 2 BGB, Druckmuster und Eingriffe in die dingliche Sicherung, Leistungs- und Baubeschreibung § 650k BGB — ist in jedem Verbraucher-Bauträgervertrag zwingend zuerst durchzulaufen. Teil J liefert die Wiedererkennungsmuster aus realen Großprojekten und die Gutachtenstruktur für den Mandantenbericht.
