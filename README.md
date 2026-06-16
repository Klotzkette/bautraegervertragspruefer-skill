# Bauträgervertrag-Prüfer Skill

> **Experimenteller Agent-Skill** für die verbraucherseitige Prüfung deutscher Bauträgerverträge — als Werkzeug zur eigenen Einordnung vor der Beurkundung beim Notar, zur Einschätzung schon beurkundeter Verträge oder zur Vorbereitung anwaltlicher Beratung. Orientiert sich an der deutschen Rechtspraxis, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. **Enthält keinerlei Fachgutachten oder Rechtsberatung**, alle Angaben ohne Gewähr — die Prüfung eines Bauträgervertrags ist im Zweifel anwaltlich zu begleiten.

> **Transparenz:** Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Bauträgervertrags als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> **Eine einzige Datei, modellunabhängig einsetzbar.** Der vollständige Skill steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne Anhänge, ohne externe Referenzen. Er funktioniert in jedem leistungsfähigen KI-Chatbot bzw. Sprachmodell: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Es ist keine Installation, kein Konto und kein zusätzliches Werkzeug erforderlich — siehe [Anwendung](#anwendung-so-einfach-gehts).

Konsolidierter Skill (Version 1.0) für die verbraucherseitige Prüfung deutscher Bauträgerverträge nach dem Ampelsystem — Befunde werden als farbige Ampelsymbole 🔴/🟠/🟢 ausgegeben, nicht als Farbwörter. Der Skill deckt den vollständigen Bogen ab — vom ersten Eingang des Notarentwurfs über die klauselweise Risikomatrix bis zur Klagestrategie auf Rückzahlung, Mängelbeseitigung oder Eigentumsumschreibung.

## Download

➡️ **[📥 SKILL.md jetzt herunterladen](https://klotzkette.github.io/bautraegervertragspruefer-skill/SKILL.md)** ⬅️

**Ein Klick genügt — die Datei lädt sofort als Markdown-Datei in den Downloads-Ordner, egal ob am Computer, iPhone, Android-Gerät oder in der GitHub-App.** Kein Rechtsklick, kein „Speichern unter…", kein Umweg über Menüs.

Wenn der Download-Knopf in einer App nicht direkt funktioniert (manche In-App-Browser ignorieren Download-Anweisungen): die Datei wird statt heruntergeladen angezeigt — dann den Link einfach gedrückt halten und „Link herunterladen" bzw. „Verknüpfte Datei laden" wählen. Oder die [komfortable Download-Seite](https://klotzkette.github.io/bautraegervertragspruefer-skill/) im normalen Browser öffnen — dort funktioniert der Download-Knopf garantiert.

Wer den Inhalt lieber direkt sehen und kopieren will, öffnet [`skill/SKILL.md`](skill/SKILL.md) — das ist die formatierte Ansicht hier im Repository. Der gesamte Text lässt sich dort mit `Strg+A` / `Cmd+A` markieren und kopieren.

## Anwendung: So einfach geht's

**Weg A — Text kopieren:**

1. [`skill/SKILL.md`](skill/SKILL.md) öffnen, den gesamten Text mit `Strg+A` / `Cmd+A` markieren und in den Chat einfügen.
2. Dazuschreiben: *„Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Bauträgervertrag — bearbeite ihn danach."* Enter drücken.
3. Den Vertrag einfügen (Text, PDF oder Foto). Die Analyse startet von selbst.

**Weg B — Datei hineinziehen (Drag & Drop):**

1. `SKILL.md` über den [Direktdownload oben](#download) auf das Gerät laden.
2. Die Datei per Drag & Drop in das Chatfenster ziehen, dazuschreiben: *„Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Bauträgervertrag — bearbeite ihn danach."* Enter drücken.
3. Den Vertrag nachreichen — fertig.

**Sofortstart in beiden Wegen:** Der Skill analysiert ohne Rückfragen-Kaskade, kennzeichnet fehlende Angaben als Annahmen und liefert klauselweise Risikomatrix, Ampel-Bilanz (🔴/🟠/🟢), Gesamteinschätzung und Handlungsempfehlung in einem Durchgang. Eine gebündelte Rückfrage gibt es höchstens dann, wenn die Analyse sonst objektiv falsch würde.

## Inhalt

```
skill/
└── SKILL.md   Alles in einer Datei: Workflow, MaBV-Ratenplan, AGB-Kontrolle, Mängelrechte, Mandatsmodule
```

Die Datei ist in folgende Teile gegliedert (interne Sprungmarken):

- **Workflow in neun Stufen** — vom Intake bis zur Klage, mit Rechtsanker, Sofortstart-Logik, Antwortformaten und Qualitätsgate.
- **Teil A — MaBV-Ratenplan und Sicherheiten** — § 3 Abs. 2 MaBV-Ratenplan (13 bzw. 7 Raten), § 7 MaBV-Bürgschaft, Voraussetzungen für die erste Rate, Insolvenzfestigkeit.
- **Teil B — AGB- und Klauselkontrolle** — Klauselkatalog typischer Bauträger-AGB nach §§ 305 ff. BGB.
- **Teil C — Baubeschreibung und Bausoll** — Pflichtangaben nach § 650k BGB, Wohnflächenberechnung, Bemusterungsklauseln, Pauschalverweise.
- **Teil D — Vertragsstrafen, Fertigstellungsfristen, Verzug** — Fristverbindlichkeit, BGH-Linie zur Strafhöhe, Verzugsschaden.
- **Teil E — Abnahme, Gefahrtragung, Mängelrechte, Gewährleistung** — Doppelabnahme bei Eigentumswohnungen, Abnahmefiktion, Verjährung, Schlussrate.
- **Teil F — Eigentumsschutz, Auflassungsvormerkung, Freistellung, Insolvenz** — dingliche Sicherung, § 3 Abs. 1 Nr. 3 MaBV, Bauträger-Insolvenzlagen.
- **Teil G — Mandatsmodule** — Nachverhandlungsbrief, Rücktrittserklärung, Klagestrategie, Vergleichsfenster.
- **Teil H — Musterklauseln und Sonderfälle** — verbraucherfreundliche Klauselmuster, einseitige Bauträger-AGB, Sanierung im Bestand, Eigentumswohnung, Reihenhaus, Insolvenzfall.
- **Teil I — Nichtigkeitsrisiken, Transparenzgebot und Notarhaftung** — § 307 Abs. 1 S. 2 BGB Transparenz, § 139 BGB Teil-/Gesamtnichtigkeit, § 19 BNotO Notarhaftung, Eskalationskette von Korrekturbrief bis Aufsichtsbeschwerde.

## 🚨 Pflicht-Prüfblock — wird bei jedem Vertrag zwingend zuerst geprüft

Der Skill enthält am Anfang einen festen Pflicht-Prüfblock, den er bei jedem Verbraucher-Bauträgervertrag **zwingend zuerst** durchläuft — vor allen anderen Klauselprüfungen:

1. **§ 650m BGB — 5 %-Sicherheitseinbehalt:** Wird der Verbraucher über sein Recht auf 5 % Sicherheit bei der ersten Abschlagszahlung belehrt? Fehlt der Hinweis, ist das ein schwerwiegender Verstoß 🔴.
2. **§ 309 Nr. 15 lit. a BGB — Beweislastklauseln:** Enthält der Vertrag eine Beweislastumkehr zulasten des Verbrauchers? Solche Klauseln sind unwirksam 🔴.
3. **§ 309 Nr. 15 lit. b BGB — Empfangsbestätigungen:** Enthält der Vertrag pauschale Bestätigungen, der Erwerber habe Unterlagen erhalten oder Risiken zur Kenntnis genommen? Unwirksam 🔴.
4. **§ 307 Abs. 1 S. 2 BGB — Transparenzgebot:** 350-Seiten-Konvolute, verschachtelte Untergemeinschaften, juristisch nicht erschließbarer Aufbau — alles Indizien für Transparenzverstoß 🔴.
5. **Druckmuster und Eingriffe in die dingliche Sicherung:** Vormerkungslöschung bei einseitiger Verzugsmitteilung, „Ohne Geld keine Schlüssel", anteilige Sachverständigenkosten für Bauträger-Gutachter — jeweils 🔴.

**Folgen bei kumulativem Verstoß:** Teil- oder Gesamtnichtigkeit nach § 139 BGB; **Notarhaftung nach § 19 BNotO** i. V. m. § 17 BeurkG bei evident verbraucherfeindlicher Beurkundung ohne ausreichende Belehrung. Eskalationskette von der Notar-Korrekturaufforderung über Beurkundungsverweigerung bis zur kollektiven Beschwerde bei der Notaraufsicht ist in [Teil I des Skills](skill/SKILL.md#teil-i--nichtigkeitsrisiken-transparenzgebot-und-notarhaftung) dokumentiert.

## Einsatzlagen

- **Vor der Beurkundung:** Der Notarentwurf liegt vor, der Termin steht. Skill prüft alle Klauseln, markiert kritische Stellen und schlägt Neufassungen für die Verhandlung mit Bauträger und Notar vor.
- **Nach der Beurkundung:** Vertrag bereits unterschrieben — Skill identifiziert unwirksame AGB-Klauseln nach § 307 BGB, die im Streitfall ohnehin nicht tragen.
- **In der Bauphase:** Bauverzögerung, MaBV-Ratenforderung trotz fehlender Voraussetzungen, Bemusterungsstreit.
- **Bei Abnahme und Übergabe:** Doppelabnahme Sondereigentum / Gemeinschaftseigentum, Abnahmefiktion, Schlussrateneinbehalt.
- **Bei Mängeln:** Nacherfüllung, Minderung, Selbstvornahme, Schadensersatz, Verjährungslage.
- **Bei Bauträger-Insolvenz:** Schutz durch Vormerkung, Forderungsanmeldung, Verwerter-Wahlrecht nach § 103 InsO.

## Rechtsanker (Auszug)

- **§ 650u BGB** — Bauträgervertrag
- **§ 650v BGB** — Abschlagszahlungen nach MaBV
- **§ 650k BGB** — Baubeschreibung
- **§ 311b BGB** — Beurkundungspflicht
- **§§ 305 ff. BGB** — AGB-Kontrolle
- **§ 3 MaBV** — Ratenplan und Voraussetzungen
- **§ 7 MaBV** — Bürgschaftsmodell
- **§§ 883 ff. BGB** — Auflassungsvormerkung
- **§§ 633–639, 634a BGB** — Mängelrechte, Verjährung
- **§§ 640, 641, 650g BGB** — Abnahme, Fälligkeit, Zustandsfeststellung

Konkrete BGH- und OLG-Rechtsprechung wird vom Skill **immer live verifiziert** — keine Fundstellen aus Modellwissen, sondern stets gegen `gesetze-im-internet.de`, `dejure.org` oder das Rechtsprechungsportal des Bundes geprüft.

## Wichtig: Bauträgervertragsprüfung ist Rechtsberatung

Die anwaltliche Prüfung eines Bauträgervertrags ist nach dem Rechtsdienstleistungsgesetz (RDG) Rechtsdienstleistung. Dieser Skill liefert eine **strukturierte Einordnung als Vorbereitung** — er ersetzt keine anwaltliche Beratung. Verbraucher sollten in jedem Fall, in dem eine Beurkundung ansteht oder Streit droht, eigene anwaltliche Beratung einholen. Die Verbraucherzentralen, die örtlichen Anwaltsvereine und spezialisierte Bauträgerrechts-Kanzleien sind die richtigen Ansprechpartner.

Wer den Skill im Rahmen einer Kanzleibearbeitung einsetzt, beachtet zusätzlich:

- **§ 203 StGB** — Verschwiegenheitspflicht
- **BORA / BRAO** — Berufsrechtspflichten
- **DSGVO** — Eingabe personenbezogener Daten in fremde KI-Systeme prüfen (DPA, Datenstandort)
- **KI-VO (EU AI Act)** — Hochrisiko-Anwendungen, Transparenzpflichten

## Lizenz

Doppellizenziert: **Apache-2.0 OR MIT**. Wählbar nach Wunsch. Siehe [`LICENSE-APACHE`](LICENSE-APACHE) und [`LICENSE-MIT`](LICENSE-MIT).

## Mitwirken

Hinweise auf weitere Klauseltypen, häufige Bauträger-Spezialitäten oder aktuelle BGH-Linien sind willkommen — bitte als Issue oder Pull Request einreichen. Keine konkreten Mandats-Sachverhalte einstellen.
