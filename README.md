# Bauträgervertrag-Prüfer Skill

> Experimenteller Agent-Skill für die verbraucherseitige und anwaltlich geprägte Prüfung deutscher Bauträgerverträge — als Anregung für Kanzlei-, Verbraucher- und Due-Diligence-Arbeitsabläufe. Orientiert sich an deutschem Bauträgerrecht, MaBV, AGB-Recht, amtlichen Gesetzestexten, frei überprüfbarer Rechtsprechung und technischer Projektprüfung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.
>
> Transparenz: Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Bauträgervertrags als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> Ein-Datei-Prinzip, modellunabhängig einsetzbar. Die Vollfassung steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne externe Laufzeit, ohne Datenbank, ohne Konto und ohne zusätzliches Werkzeug. Für kleine Kontextfenster gibt es zusätzlich [`skill/MINI_SKILL.md`](skill/MINI_SKILL.md). Beide Dateien funktionieren in leistungsfähigen KI-Chatbots bzw. Sprachmodellen: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Es ist keine Installation erforderlich — siehe [Anwendung](#anwendung-so-einfach-gehts).

Konsolidierter Skill (Version 3.0.2) für die Prüfung deutscher Bauträgerverträge nach dem Ampelsystem — Befunde werden als Ampelsymbole 🔴/🟠/🟢 ausgegeben, nicht als Farbwörter. Der Skill arbeitet nicht mit austauschbaren Textbausteinen, sondern zwingt vor jeder Bewertung einen Fall-Fingerabdruck: Urkunde, Parteien, Einheit, Projektgrundstück, Kaufpreis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Baugrund, Technik, WEG-Organisation und Streitstand. Er deckt den vollständigen Bogen ab: Mandanten-Intake, Verbraucherstatus, Beurkundungsphase, MaBV-Ratenplan, Sicherungsmechanik, AGB-Klauselkontrolle, Baubeschreibung, Bausoll, Fertigstellung, Abnahme, Schlussrate, Mängelrechte, Teilungserklärung, Gemeinschaftsordnung, Sondereigentum, Gemeinschaftseigentum, Eigentumssicherung, Insolvenzrisiken, Notar- und Vollzugsrisiken, Finanzierung, Baugrund, Baugrube, HOAI-Leistungsphasen, Objektüberwachung, private Bauüberwachung, technische Plausibilität, Beweislast, Durchsetzung und Verhandlungsstrategie.

Schnellwahl: Für eine vollständige Vertragsprüfung mit Mandantenschreiben, Gutachten und Aufforderungsschreiben an Bauträger/Notar ist [`SKILL.md`](skill/SKILL.md) die Hauptfassung. Wenn ein kleineres Modell den langen Prompt nicht vollständig lädt oder die Antwort vor dem Drei-Dokumente-Paket abbricht, ist [`MINI_SKILL.md`](skill/MINI_SKILL.md) die kompakte Ausweichfassung.

## Sofort loslegen

Wer nur prüfen will, braucht keine Installation und keine GitHub-Kenntnisse:

1. Datei wählen: Normalfall [`SKILL.md`](https://klotzkette.github.io/bautraegervertragspruefer-skill/SKILL.md), kleines Kontextfenster [`MINI_SKILL.md`](https://klotzkette.github.io/bautraegervertragspruefer-skill/MINI_SKILL.md).
2. In den Chat legen: Datei in Claude, ChatGPT, Perplexity, Gemini, Mistral oder ein lokales Modell hochladen oder den Inhalt hineinkopieren.
3. Startsatz senden: Den kopierfertigen Startsatz aus [Anwendung](#anwendung-so-einfach-gehts) einfügen.
4. Vertrag nachreichen: PDF, DOCX, Text, Foto oder Akten-ZIP hochladen. Der Skill prüft ohne Bedienungsrückfragen und liefert am Ende die drei Pflichtdokumente.

Dateiwahl ohne Nachdenken: Große Modelle und Kanzlei-/Projektarbeit: `SKILL.md`. Kleine Assistenten, mobile Apps, knappe Upload-Limits oder erste Vorführung: `MINI_SKILL.md`. Testlauf mit getrennten Unterlagen: erst die Skill-Datei, dann das passende Akten-ZIP.

Reihenfolge: Am stabilsten ist erst Skill-Datei, dann Startsatz, dann Vertrag. Wenn Skill und Vertrag schon gemeinsam in derselben Unterhaltung liegen, genügt der Startsatz; nicht neu hochladen, nicht von vorn beginnen.

## Was am Ende herauskommt

Der Skill soll nicht bei einer losen Analyse stehen bleiben. Die Ausgabe hat immer dieselbe Reihenfolge und einen Statuskopf, der zeigt, welche Teile schon erledigt sind:

1. Kurzbild für die schnelle Orientierung: Vertragsstatus, rote/orange/grüne Treffer, wichtigste Sofortmaßnahme.
2. Übersendungsschreiben an den Mandanten: kurze, verständliche Einordnung mit Handlungsempfehlung.
3. Mandantengutachten: belastbare Prüfung mit Klauselmatrix, Normen, Quellenstand, Beweislandkarte, Technik- und Organisationsrisiken.
4. Aufforderungsschreiben an Bauträger/Notar: konkrete Streichungen, Änderungsfassungen und kurze Begründungen.

Wenn ein Chatbot wegen Länge abbricht, nicht neu starten: _"Bitte fahre mit dem nächsten noch fehlenden Dokument fort."_ Der Skill soll dann an der nächsten Dokumentüberschrift weiterschreiben und den Statuskopf aktualisieren.

## Download

[📥 SKILL.md jetzt herunterladen](https://klotzkette.github.io/bautraegervertragspruefer-skill/SKILL.md)

Ein Klick genügt — die Datei lädt sofort als Markdown-Datei in den Downloads-Ordner, egal ob am Computer, iPhone, Android-Gerät oder in der GitHub-App. Kein Rechtsklick, kein "Speichern unter...", kein Umweg über Menüs.

Wenn der Download-Knopf in einer App nicht direkt funktioniert, wird die Datei statt heruntergeladen angezeigt. Dann den Link gedrückt halten und "Link herunterladen" bzw. "Verknüpfte Datei laden" wählen. Alternativ die [komfortable Download-Seite](https://klotzkette.github.io/bautraegervertragspruefer-skill/) im normalen Browser öffnen — dort funktioniert der Download-Knopf zuverlässig.

Wer den Inhalt lieber direkt sehen und kopieren will, öffnet [`skill/SKILL.md`](skill/SKILL.md) — das ist die formatierte Ansicht hier im Repository. Der gesamte Text lässt sich dort mit `Strg+A` / `Cmd+A` markieren und kopieren.

## Bauträgerverträge zum Ausprobieren

Zum Ausprobieren des Skills liegen zwei freistehende Bauträgervertragsakten bereit. Beide dienen nur zum Durchspielen der Prüfung; sie sind keine Musterverträge und dürfen nicht in der Praxis eingesetzt werden.

Vertrag Hohenwartshofen — Wohnungsbauträgervertrag mit Auflassung

Fehlerakte mit bewusst groben MaBV-, AGB-, Abnahme-, Sicherungs-, Bauüberwachungs- und Baubeschreibungsproblemen; hier soll der Skill viele rote Pflichtbefunde finden.

- [📦 Akten-ZIP mit Einzel-PDFs](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip) · [📄 PDF](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf) · [📄 Word](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.docx) · [📄 Markdown](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.md)

Vertrag Marewald — Wohnungsbauträgervertrag mit Auflassung

Kontrollakte mit rechtmäßigem, aber deutlich verkäuferfreundlichem Grenzvertrag; hier soll der Skill harte gelbe Verhandlungsbefunde liefern, aber keine Nichtigkeit oder rote Pflichtverstöße behaupten.

- [📦 Akten-ZIP mit Einzel-PDFs](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip) · [📄 PDF](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf) · [📄 Word](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx) · [📄 Markdown](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md)

Beide Dokumente sind keine Musterverträge: nicht unterschreiben, nicht als Vorlage verwenden, nicht in der Praxis einsetzen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden verwenden. Eine fachliche Bewertung setzt immer eine eigenständige rechtliche und technische Prüfung voraus.

Neue Aktenregel: Jede Vertragsakte hat ab jetzt ein Akten-ZIP. Dieses ZIP enthält die Unterlagen der jeweiligen Akte nicht als ein weiteres Gesamt-PDF und nicht als bloße Formatvariante, sondern als getrennte, neutral benannte Einzel-PDFs, damit kleinere und größere KI-Systeme die Akte dokumentweise aufnehmen können.

## Kurzversion für kleinere Modelle

[📥 MINI_SKILL.md herunterladen](https://klotzkette.github.io/bautraegervertragspruefer-skill/MINI_SKILL.md)

Wenn Claude, ChatGPT, Perplexity, Gemini, Mistral oder ein lokal betriebenes Modell die große `SKILL.md` nicht zuverlässig annimmt, zu früh abbricht oder nur ein kleiner Skill-Kontext zur Verfügung steht, ist [`skill/MINI_SKILL.md`](skill/MINI_SKILL.md) die Sparversion. Sie hat weniger als 7.500 Zeichen inklusive Leerzeichen und enthält trotzdem den Kern: verbraucherseitige Prüfung, harte Quellenregeln, MaBV-/AGB-/WEG-/Technik-Pflichtblock, No-Meta-Regel, Anti-Generik-Regel und die immer verpflichtende Drei-Dokumente-Ausgabe.

Die Kurzversion ist nicht so tief wie die Vollfassung. Sie ist dafür schnell kopierbar, robust in kleineren Assistenten und gut genug abgehangen, um auch dort Zahlungsplan, Sicherheiten, Abnahme, Bausoll, Bauüberwachung, Preisanpassung, Verzug und die wichtigsten AGB-Risiken strukturiert zu prüfen.

## Anwendung: So einfach geht's

Kopierfertiger Startsatz für jeden Chatbot, jedes Projekt und jede Assistant-Konfiguration:

```text
Bitte nutze die gerade hochgeladene SKILL.md oder MINI_SKILL.md als Arbeitsanweisung.
Wenn ich gleich einen Bauträgervertrag hochlade oder einfüge, prüfe ihn ohne Rückfragen-Kaskade.
Bitte liefere zuerst ein Kurzbild und danach immer drei Dokumente: 1. Übersendungsschreiben an den Mandanten, 2. Mandantengutachten, 3. Aufforderungsschreiben an Bauträger/Notar mit konkreten Änderungsfassungen.
```

Einfachster Weg — Datei hochladen:

1. [`SKILL.md`](https://klotzkette.github.io/bautraegervertragspruefer-skill/SKILL.md) oder bei engem Kontext [`MINI_SKILL.md`](https://klotzkette.github.io/bautraegervertragspruefer-skill/MINI_SKILL.md) herunterladen.
2. Datei in das Chatfenster, Projektwissen oder die Assistant-/Skill-Konfiguration ziehen.
3. Startsatz senden.
4. Vertrag oder Akten-ZIP hochladen.

Wenn Datei-Upload nicht klappt — Text kopieren:

1. [`skill/SKILL.md`](skill/SKILL.md) öffnen, den gesamten Text mit `Strg+A` / `Cmd+A` markieren und in den Chat einfügen. Wenn das Modell die Vollfassung nicht annimmt, stattdessen [`skill/MINI_SKILL.md`](skill/MINI_SKILL.md) verwenden.
2. Dazuschreiben: _"Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Bauträgervertrag — bearbeite ihn danach."_ Enter drücken.
3. Den Vertrag einfügen oder hochladen (Text, PDF, DOCX oder Foto). Die Analyse startet von selbst.

Sofortstart in beiden Wegen: Der Skill analysiert ohne Rückfragen-Kaskade, kennzeichnet fehlende Angaben als Annahmen, prüft mit Ampelsymbolen, priorisiert verbraucherschützende Einwände und liefert harte Gegenargumente für Bauträger, Notariat, Vertrieb und finanzierende Bank. Eine gebündelte Rückfrage gibt es höchstens dann, wenn die Analyse sonst objektiv falsch oder irreführend würde. Am Ende steht immer ein Drei-Dokumente-Paket: Übersendungsschreiben an den Mandanten, Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notar mit konkreten Änderungsfassungen.

Projekt, Co-Work oder Assistant-Konfiguration: Die Datei als Projektwissen, Skill-Datei, Systemanweisung oder dauerhafte Arbeitsanweisung hinterlegen. Wenn die Oberfläche nach einem Zweck fragt: _"Prüft deutsche Bauträgerverträge verbraucherseitig und erzeugt immer Übersendungsschreiben, Mandantengutachten und Aufforderungsschreiben."_ Wenn die Oberfläche nach einem Startprompt fragt, den kopierfertigen Startsatz oben verwenden.

Wenn der Chatbot stehenbleibt: Nicht neu anfangen. Schreibe einfach: _"Bitte fahre mit dem nächsten noch fehlenden Dokument fort und liefere das Drei-Dokumente-Paket vollständig."_ Wenn die Vollfassung mehrfach abbricht, lade stattdessen `MINI_SKILL.md` und den Akten-ZIP mit Einzel-PDFs hoch; kleinere Modelle kommen mit getrennten PDFs oft schneller zu belastbaren ersten Befunden.

Wenn gar nichts passiert: Einmal klar nachschieben: _"Du hast jetzt die Arbeitsanweisung. Bitte beginne mit dem Pflicht-Prüfblock und arbeite danach das Drei-Dokumente-Paket aus."_ Danach nicht weiter erklären, sondern den Vertrag oder das Akten-ZIP hochladen.

Wenn Skill und Vertrag schon zusammen hochgeladen wurden: Einfach den Startsatz senden. Das Modell soll dann sofort mit dem Pflicht-Prüfblock beginnen und keine neue Upload-Reihenfolge verlangen.

## Inhalt

```text
skill/
├── SKILL.md       Vollfassung: Workflow, Quellenregeln, Klauselmatrix,
│                  Rechtsanker, Technikmodule, Mandantenbericht, Verhandlungspaket
└── MINI_SKILL.md  Kurzfassung unter 7.500 Zeichen für kleinere KI-Kontexte

docs/
├── SKILL.md       Veröffentlichte Vollfassung
├── MINI_SKILL.md  Veröffentlichte Kurzfassung
├── index.html     Download-Seite für Browser und Mobilgeräte
└── vertragsdokumente/  Veröffentlichte Spiegel der Vertragsakten

vertragsdokumente/
├── bautraegervertrag/
│   ├── bautraegervertrag.md / .docx / .pdf
│   ├── bautraegervertrag-einzel-pdfs.zip
│   └── build.sh, build/
└── bautraegervertrag-marewald/
    ├── bautraegervertrag-marewald.md / .docx / .pdf
    ├── bautraegervertrag-marewald-einzel-pdfs.zip
    └── build.sh, build/
```

Die Skill-Datei ist in folgende Hauptteile gegliedert:

- Sofortstart und Quellenregeln — Rollenklärung, Annahmendisziplin, Verbot nicht überprüfbarer Zitate.
- Rechtsprechungsanker — quellenharte Anker aus Bundesgerichten, Oberlandesgerichten, Kammergericht, Landgerichten sowie OpenJur und dejure.
- Normenkarte — Bauträgervertrag, Verbraucherbauvertrag, MaBV, AGB-Recht, WEG, HOAI, Abnahme, Mängelrechte, Eigentumssicherung.
- Prüfschleifen — mehrstufige Analyse vom Pflicht-Prüfblock bis zum finalen Bug-Hunt.
- Klauselmatrix — Befund, Risiko, Norm, Rechtsprechungsanker, Beweislast, Verhandlungsziel, erwartbarer Gegeneinwand und Antwort.
- MaBV- und Zahlungsprüfung — Ratenplan, Bezugsfertigkeit, Besitzübergang, Schlussrate, Sicherheiten, Finanzierungskollisionsrisiken.
- AGB-Klauselkontrolle — unangemessene Benachteiligung, Intransparenz, Beweislastverschiebung, Leistungsänderungen, Haftungs- und Fristenregime.
- Baubeschreibung und Bausoll — Vollständigkeit, Standards, Wahlrechte, Bemusterung, Nebenleistungen, Außenanlagen, Stellplätze, Sonderwünsche.
- Technik und Bauüberwachung — Baugrund, Baugrube, Abdichtung, Schallschutz, Brandschutz, Energie, Statik, Nachweise, Objektüberwachung, private Sachverständige.
- Fachmodule Bauträgerrecht 2026 — Vorinsolvenz, unwirksame Notarklauseln, anerkannte Regeln der Technik, DIN-Verweise, Preisanpassung, Bauzeitverzug, Baugruppen-GbR, Nachzügler, Sonderwünsche, Sicherheitenschichten und Haftungsketten.
- Teilungserklärung und WEG — Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, GdWE, Kostenverteilung, Abnahmeregime.
- Mandatsmodule — Mandantenbericht, Notar-/Bauträgeranschreiben, Verhandlungsfassung, Eskalations- und Klagestrategie.
- Vertragsdokumente (separate Dateien) — zusätzlich zur Skill-Datei liegen unter `vertragsdokumente/` zwei freistehende Bauträgerverträge mit Baubeschreibung als Anlage bereit; jede Akte enthält außerdem ein ZIP mit getrennten Einzel-PDFs.

Zusätzlich enthält der Skill durchgängig:

- Verbraucherschützende Priorisierung — der Skill sucht nicht nur formale Fehler, sondern wirtschaftliche, technische und organisatorische Schieflagen.
- Überzeugungsdisziplin — jedes harte Argument soll so formuliert werden, dass es gegenüber Notariat, Bauträger und deren Prozessvertretung belastbar ist.
- Kein Blindzitat — tragende Rechtsprechung wird nicht aus Modellwissen erfunden; Quellen werden als zu verifizieren markiert oder mit frei überprüfbarem Fundort benannt.
- No-Meta-Regel für jedes Vertragsdokument — der Skill spricht nie über Herkunft, Repository, Beispiel, Demonstration oder Dateirolle, sondern prüft ausschließlich den vorgelegten Vertragsstoff.
- Anti-Generik-Regel — kein Befund darf ohne Fallanker ausgegeben werden; jede rote oder orange Ampel braucht Klausel, Betrag/Rate/Frist oder Projekt-/Einheitsbezug und eine konkrete Änderungsfassung.
- Subsumtions-Gate — jede rote oder orange Ampel braucht Textstelle, konkrete Klauselwirkung, Rechtsfolge, Beweis-/Darlegungslast und Antwort auf das stärkste Gegenargument.
- Technischer Realitätscheck — ein juristisch eleganter Vertrag genügt nicht, wenn Baugrund, Baugrube, Abdichtung, Bauüberwachung oder Nachweislage nicht tragen.
- Drei-Dokumente-Ausgabe — immer: Übersendungsschreiben an den Mandanten, Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notar mit Problem, Begründung und richtiger Fassung.
- Statuskopf — Kurzbild und Dokumente 1 bis 3 werden als offen/erledigt markiert, damit auch kleine Modelle nach Abbruch sauber fortsetzen.
- Mini-Fallback — für kleine Kontextfenster gibt es `MINI_SKILL.md`; sie ersetzt die Vollfassung nicht, hält aber den Kernworkflow und die drei Pflichtdokumente fest.

## Workflow in zwölf Stufen

1. Intake, Rollenklärung und Bearbeitungsstand sichern.
2. Vertragsart, Verbraucherstatus, Beurkundungs- und Vollzugsstatus bestimmen.
3. Pflicht-Prüfblock: MaBV, Sicherung, Abnahme, Schlussrate, Verjährung, Eigentumsübergang.
4. Zahlungsplan, Bautenstand, Ratenfälligkeit und Finanzierungsrisiken prüfen.
5. AGB-Klauseln satzweise mit Ampelsymbolen und Gegenargumenten bewerten.
6. Baubeschreibung, Bausoll, Leistungsänderungen und Sonderwünsche absichern.
7. Abnahme, Besitzübergang, Mängelrechte, Vertragsstrafe und Fertigstellungstermine prüfen.
8. Teilungserklärung, Gemeinschaftsordnung, Sondereigentum und Gemeinschaftseigentum auswerten.
9. HOAI-Leistungsphasen, Objektüberwachung, private Baukontrolle und Nachweiskette prüfen.
10. Baugrund, Baugrube, Abdichtung, Schall, Brand, Energie und technische Mindestnachweise plausibilisieren.
11. Mandantenbericht, Verhandlungsziele und Gegenseitenschreiben erstellen.
12. Bug-Hunt, Dublettencheck, Quellencheck, Sanity-Check und finale Priorisierung.

## Rechtlicher Anker

- Bauträgervertrag — §§ 650u, 650v BGB; gemischte kauf- und werkvertragliche Struktur mit verbraucherschützender Sonderlogik.
- Verbraucherbau- und Bauvertragsrecht — §§ 650a ff., 650i ff. BGB, insbesondere Baubeschreibung, Abschlagszahlungen, Widerrufs- und Sicherungsfragen nach konkreter Vertragslage.
- AGB-Recht — §§ 305 bis 310 BGB; Transparenzgebot, unangemessene Benachteiligung, Klauselverbote, Beweislast, Leistungsänderungen, Haftungsbegrenzungen.
- Makler- und Bauträgerverordnung — insbesondere §§ 3, 7, 12 MaBV; Ratenplan, Sicherheiten, Entgegennahme von Vermögenswerten, Fälligkeitsvoraussetzungen.
- Abnahme und Mängelrechte — §§ 633 ff., 640, 641, 634a BGB; Trennung von Sonder- und Gemeinschaftseigentum, Verjährungsbeginn, Beweis- und Druckmittel.
- Teilungserklärung und WEG — WEG-Struktur, Gemeinschaftseigentum, Sondernutzungsrechte, Kostenverteilung, GdWE-Rolle, Beschluss- und Durchsetzungsrisiken.
- HOAI und Objektüberwachung — HOAI-Leistungsbilder, insbesondere Leistungsphase 8 als Prüfanker für Bauüberwachung, Rechnungsprüfung, Kostenfeststellung und Mängelverfolgung.
- Form und Eigentumssicherung — § 311b BGB, Auflassungsvormerkung, Lastenfreistellung, Vollzug, Notaranderkonto nur bei tragfähiger rechtlicher Grundlage.

Die `SKILL.md` enthält einen eigenen Rechtsprechungsanker mit überprüfbaren Leitentscheidungen und frei zugänglichen Fundstellen. Grundregel: Keine Zitate aus BeckRS, juris, Fachzeitschriften oder nicht frei überprüfbaren Datenbanken. Tragende Aussagen werden über offizielle Webseiten der Bundesgerichte, Oberlandesgerichte, des Kammergerichts, der Landgerichte oder über OpenJur und dejure verankert; andernfalls werden sie als Prüfhinweis statt als belegte Rechtsprechung ausgegeben.

## Einsatzlagen

- Käuferin oder Käufer will einen Vertragsentwurf vor dem Notartermin verstehen.
- Kanzlei prüft Verhandlungs-, Rücktritts-, Mängel- oder Klagestrategie.
- Verbraucherschutz, Baubegleitung oder Sachverständige wollen juristische und technische Risiken bündeln.
- Finanzierung, Zahlungsplan und Bautenstand passen nicht sauber zusammen.
- Abnahme, Besitzübergang oder Schlussrate stehen bevor.
- Teilungserklärung, Gemeinschaftsordnung oder Sondernutzungsrechte sind unklar.
- Baugrund, Baugrube, Abdichtung, Schallschutz, Brandschutz oder Energieangaben wirken lückenhaft.
- Notariat oder Bauträger lehnen Änderungen ab und brauchen harte, zitierfähige Gegenargumente.

## Offene Ein-Datei-Logik

Dieses Repository folgt einer offenen Ein-Datei-Logik: Der eigentliche Skill ist eine lesbare Markdown-Datei, nicht ein verborgenes System. Die README beschreibt nicht einzelne Bastelstände, sondern Zweck, Einsatz, Inhalt, Grenzen und Bedienung des Skills.

## Keine Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

Lesen, bevor irgendetwas davon eingesetzt wird. Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft keinerlei Aussage darüber, ob der Einsatz dieses Skills in einer konkreten Praxisumgebung berufs-, datenschutz-, urheber-, haftungs-, notar- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss der Nutzer in eigener Verantwortung vor der ersten Nutzung prüfen — das Repository, sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- Strafrechtliches Mandatsgeheimnis — §§ 203, 204 StGB. Der Skill sagt nichts darüber, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB und § 204 StGB vereinbar ist, auch nicht in Konstellationen mit mitwirkenden Personen, Cloud-Diensten, externen Sachverständigen oder technischen Dienstleistern.
- Berufsrecht — § 43e BRAO, § 2 BORA, § 53 StPO. Es wird nicht geprüft, ob der Einsatz mit anwaltlichen, notariellen, steuerberatenden, wirtschaftsprüfenden, ärztlichen, patentanwaltlichen oder sonstigen berufsrechtlichen Pflichten vereinbar ist. Gleiches gilt für Zeugnisverweigerungsrechte, Beschlagnahmeschutz und die Einschaltung Dritter.
- Datenschutz — DSGVO, BDSG. Es wird nicht beurteilt, ob eine ausreichende Rechtsgrundlage vorliegt, ob ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO geschlossen werden muss, ob eine Datenschutz-Folgenabschätzung erforderlich ist oder ob Informationspflichten, Löschkonzepte, TOMs, Drittlandtransfers und Betroffenenrechte eingehalten werden.
- KI-Verordnung — KI-VO / EU AI Act, VO (EU) 2024/1689. Es wird nicht entschieden, ob der Einsatz unter Hochrisiko-, Transparenz-, Betreiber- oder General-Purpose-AI-Pflichten fällt und welche Dokumentations-, Kontroll- oder Informationspflichten in einer konkreten Nutzung bestehen.
- Beschlagnahmeverbote und auslandsrechtliche Zugriffe. Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme, Herausgabe, Cloud Act, FISA 702, CLOUD Act warrants, PATRIOT Act oder sonstige ausländische Zugriffsrechte hinreichend geschützt sind.
- Zugang, Auftragsverarbeitung, Hosting. Wie der API-Zugang zum Modell beschafft wird, ob mit dem Anbieter ein berufsrechtskonformer Vertrag besteht, wo Daten verarbeitet werden, welche Subunternehmer beteiligt sind und ob Datenresidenz, Verschwiegenheit, Audit-Rechte und Löschung gesichert sind, bleibt vollständig in der Eigenverantwortung der Nutzerin / des Nutzers.
- Notar-, Anwalts- und Sachverständigenrolle. Der Skill ersetzt keine notarielle Belehrung, keine anwaltliche Beratung, keine technische Bauzustandsprüfung, kein Bodengutachten, keine Objektüberwachung und keine baubegleitende Qualitätskontrolle.

Anwälte, Notare, Sachverständige und andere Berufsgeheimnisträger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting-, Mandats-, Daten- und Sachverständigenkonstellation mit Berufsrecht, Datenschutz, Mandatsgeheimnis, Beschlagnahmeschutz, KI-Recht und Haftungsrecht vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz, technischer Bauprüfung oder vertraglicher Verschwiegenheit.

## Lizenz

Dieses Repository steht wahlweise unter der [MIT-Lizenz](LICENSE-MIT) oder der [Apache-2.0-Lizenz](LICENSE-APACHE) (Dual-Lizenz „MIT OR Apache-2.0"). Nutzer dürfen frei zwischen beiden Lizenzen wählen.
