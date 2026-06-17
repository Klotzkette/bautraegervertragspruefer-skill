# Bauträgervertrag-Prüfer Skill

> **Experimenteller Agent-Skill** für die verbraucherseitige und anwaltlich geprägte Prüfung deutscher Bauträgerverträge — als Anregung für Kanzlei-, Verbraucher- und Due-Diligence-Arbeitsabläufe. Orientiert sich an deutschem Bauträgerrecht, MaBV, AGB-Recht, amtlichen Gesetzestexten, frei überprüfbarer Rechtsprechung und technischer Projektprüfung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.
>
> **Transparenz:** Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Bauträgervertrags als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> **Eine einzige Datei, modellunabhängig einsetzbar.** Der vollständige Skill steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne externe Laufzeit, ohne Datenbank, ohne Konto und ohne zusätzliches Werkzeug. Er funktioniert in jedem leistungsfähigen KI-Chatbot bzw. Sprachmodell: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Es ist keine Installation erforderlich — siehe [Anwendung](#anwendung-so-einfach-gehts).

Konsolidierter Skill (Version 2.5.3) für die Prüfung deutscher Bauträgerverträge nach dem Ampelsystem — Befunde werden als Ampelsymbole 🔴/🟠/🟢 ausgegeben, nicht als Farbwörter. Der Skill arbeitet nicht mit austauschbaren Textbausteinen, sondern zwingt vor jeder Bewertung einen Fall-Fingerabdruck: Urkunde, Parteien, Einheit, Projektgrundstück, Kaufpreis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Baugrund, Technik, WEG-Organisation und Streitstand. Er deckt den vollständigen Bogen ab: Mandanten-Intake, Verbraucherstatus, Beurkundungsphase, MaBV-Ratenplan, Sicherungsmechanik, AGB-Klauselkontrolle, Baubeschreibung, Bausoll, Fertigstellung, Abnahme, Schlussrate, Mängelrechte, Teilungserklärung, Gemeinschaftsordnung, Sondereigentum, Gemeinschaftseigentum, Eigentumssicherung, Insolvenzrisiken, Notar- und Vollzugsrisiken, Finanzierung, Baugrund, Baugrube, HOAI-Leistungsphasen, Objektüberwachung, private Bauüberwachung, technische Plausibilität und Verhandlungsstrategie.

## Download

**[📥 SKILL.md jetzt herunterladen](https://klotzkette.github.io/bautraegervertragspruefer-skill/SKILL.md)**

Ein Klick genügt — die Datei lädt sofort als Markdown-Datei in den Downloads-Ordner, egal ob am Computer, iPhone, Android-Gerät oder in der GitHub-App. Kein Rechtsklick, kein "Speichern unter...", kein Umweg über Menüs.

Wenn der Download-Knopf in einer App nicht direkt funktioniert, wird die Datei statt heruntergeladen angezeigt. Dann den Link gedrückt halten und "Link herunterladen" bzw. "Verknüpfte Datei laden" wählen. Alternativ die [komfortable Download-Seite](https://klotzkette.github.io/bautraegervertragspruefer-skill/) im normalen Browser öffnen — dort funktioniert der Download-Knopf zuverlässig.

Wer den Inhalt lieber direkt sehen und kopieren will, öffnet [`skill/SKILL.md`](skill/SKILL.md) — das ist die formatierte Ansicht hier im Repository. Der gesamte Text lässt sich dort mit `Strg+A` / `Cmd+A` markieren und kopieren.

## Anwendung: So einfach geht's

**Weg A — Text kopieren:**

1. [`skill/SKILL.md`](skill/SKILL.md) öffnen, den gesamten Text mit `Strg+A` / `Cmd+A` markieren und in den Chat einfügen.
2. Dazuschreiben: _"Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Bauträgervertrag — bearbeite ihn danach."_ Enter drücken.
3. Den Vertrag einfügen oder hochladen (Text, PDF, DOCX oder Foto). Die Analyse startet von selbst.

**Weg B — Datei hineinziehen (Drag & Drop):**

1. `SKILL.md` über den [Direktdownload oben](#download) auf das Gerät laden.
2. Die Datei per Drag & Drop in das Chatfenster ziehen und dazuschreiben: _"Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Bauträgervertrag — bearbeite ihn danach."_ Enter drücken.
3. Den Vertrag nachreichen — fertig.

**Sofortstart in beiden Wegen:** Der Skill analysiert ohne Rückfragen-Kaskade, kennzeichnet fehlende Angaben als Annahmen, prüft mit Ampelsymbolen, priorisiert verbraucherschützende Einwände und liefert harte Gegenargumente für Bauträger, Notariat, Vertrieb und finanzierende Bank. Eine gebündelte Rückfrage gibt es höchstens dann, wenn die Analyse sonst objektiv falsch oder irreführend würde.

## Inhalt

```text
skill/
└── SKILL.md   Alles in einer Datei: Workflow, Quellenregeln, Klauselmatrix,
               Rechtsanker, Technikmodule, Mandantenbericht, Verhandlungspaket

docs/
├── SKILL.md   Veröffentlichte Downloadfassung
└── index.html Download-Seite für Browser und Mobilgeräte

vertragsdokumente/
└── bautraegervertrag/
    ├── bautraegervertrag.md
    ├── bautraegervertrag.docx
    └── bautraegervertrag.pdf
```

Die Skill-Datei ist in folgende Hauptteile gegliedert:

- **Sofortstart und Quellenregeln** — Rollenklärung, Annahmendisziplin, Verbot nicht überprüfbarer Zitate.
- **Rechtsprechungsanker** — quellenharte Anker aus Bundesgerichten, Oberlandesgerichten, Kammergericht, Landgerichten sowie OpenJur und dejure.
- **Normenkarte** — Bauträgervertrag, Verbraucherbauvertrag, MaBV, AGB-Recht, WEG, HOAI, Abnahme, Mängelrechte, Eigentumssicherung.
- **Prüfschleifen** — mehrstufige Analyse vom Pflicht-Prüfblock bis zum finalen Bug-Hunt.
- **Klauselmatrix** — Befund, Risiko, Norm, Rechtsprechungsanker, Verhandlungsziel, erwartbarer Gegeneinwand und Antwort.
- **MaBV- und Zahlungsprüfung** — Ratenplan, Bezugsfertigkeit, Besitzübergang, Schlussrate, Sicherheiten, Finanzierungskollisionsrisiken.
- **AGB-Klauselkontrolle** — unangemessene Benachteiligung, Intransparenz, Beweislastverschiebung, Leistungsänderungen, Haftungs- und Fristenregime.
- **Baubeschreibung und Bausoll** — Vollständigkeit, Standards, Wahlrechte, Bemusterung, Nebenleistungen, Außenanlagen, Stellplätze, Sonderwünsche.
- **Technik und Bauüberwachung** — Baugrund, Baugrube, Abdichtung, Schallschutz, Brandschutz, Energie, Statik, Nachweise, Objektüberwachung, private Sachverständige.
- **Fachmodule Bauträgerrecht 2026** — Vorinsolvenz, unwirksame Notarklauseln, anerkannte Regeln der Technik, DIN-Verweise, Preisanpassung, Bauzeitverzug, Baugruppen-GbR, Nachzügler, Sonderwünsche, Sicherheitenschichten und Haftungsketten.
- **Teilungserklärung und WEG** — Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, GdWE, Kostenverteilung, Abnahmeregime.
- **Mandatsmodule** — Mandantenbericht, Notar-/Bauträgeranschreiben, Verhandlungsfassung, Eskalations- und Klagestrategie.
- **Vertragsdokument** — ein freistehender Bauträgervertrag mit Baubeschreibung als Anlage.

Zusätzlich enthält der Skill durchgängig:

- **Verbraucherschützende Priorisierung** — der Skill sucht nicht nur formale Fehler, sondern wirtschaftliche, technische und organisatorische Schieflagen.
- **Überzeugungsdisziplin** — jedes harte Argument soll so formuliert werden, dass es gegenüber Notariat, Bauträger und deren Prozessvertretung belastbar ist.
- **Kein Blindzitat** — tragende Rechtsprechung wird nicht aus Modellwissen erfunden; Quellen werden als zu verifizieren markiert oder mit frei überprüfbarem Fundort benannt.
- **No-Meta-Regel für jedes Vertragsdokument** — der Skill spricht nie über Herkunft, Repository, Beispiel, Demonstration oder Dateirolle, sondern prüft ausschließlich den vorgelegten Vertragsstoff.
- **Anti-Generik-Regel** — kein Befund darf ohne Fallanker ausgegeben werden; jede rote oder orange Ampel braucht Klausel, Betrag/Rate/Frist oder Projekt-/Einheitsbezug und eine konkrete Änderungsfassung.
- **Technischer Realitätscheck** — ein juristisch eleganter Vertrag genügt nicht, wenn Baugrund, Baugrube, Abdichtung, Bauüberwachung oder Nachweislage nicht tragen.
- **Drei-Dokumente-Ausgabe** — Mandantenbericht, Gegenseitenschreiben und Änderungs-/Streichungsliste können in einem Durchgang erzeugt werden.

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

- **Bauträgervertrag** — §§ 650u, 650v BGB; gemischte kauf- und werkvertragliche Struktur mit verbraucherschützender Sonderlogik.
- **Verbraucherbau- und Bauvertragsrecht** — §§ 650a ff., 650i ff. BGB, insbesondere Baubeschreibung, Abschlagszahlungen, Widerrufs- und Sicherungsfragen nach konkreter Vertragslage.
- **AGB-Recht** — §§ 305 bis 310 BGB; Transparenzgebot, unangemessene Benachteiligung, Klauselverbote, Beweislast, Leistungsänderungen, Haftungsbegrenzungen.
- **Makler- und Bauträgerverordnung** — insbesondere §§ 3, 7, 12 MaBV; Ratenplan, Sicherheiten, Entgegennahme von Vermögenswerten, Fälligkeitsvoraussetzungen.
- **Abnahme und Mängelrechte** — §§ 633 ff., 640, 641, 634a BGB; Trennung von Sonder- und Gemeinschaftseigentum, Verjährungsbeginn, Beweis- und Druckmittel.
- **Teilungserklärung und WEG** — WEG-Struktur, Gemeinschaftseigentum, Sondernutzungsrechte, Kostenverteilung, GdWE-Rolle, Beschluss- und Durchsetzungsrisiken.
- **HOAI und Objektüberwachung** — HOAI-Leistungsbilder, insbesondere Leistungsphase 8 als Prüfanker für Bauüberwachung, Rechnungsprüfung, Kostenfeststellung und Mängelverfolgung.
- **Form und Eigentumssicherung** — § 311b BGB, Auflassungsvormerkung, Lastenfreistellung, Vollzug, Notaranderkonto nur bei tragfähiger rechtlicher Grundlage.

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

## Verwandte Projekte

Dieses Repository folgt derselben offenen Ein-Datei-Logik wie der [Arbeitszeugnis-Prüfer Skill](https://github.com/Klotzkette/arbeitszeugnispruefer-skill): Der eigentliche Skill ist eine lesbare Markdown-Datei, nicht ein verborgenes System. Die README beschreibt nicht einzelne Bastelstände, sondern Zweck, Einsatz, Inhalt, Grenzen und Bedienung des Skills.

## Bauträgervertragsdokument

Im Ordner [`vertragsdokumente/bautraegervertrag/`](vertragsdokumente/bautraegervertrag/) liegt ein freistehender Bauträgervertrag als [Markdown](vertragsdokumente/bautraegervertrag/bautraegervertrag.md), [Word-Dokument](vertragsdokumente/bautraegervertrag/bautraegervertrag.docx) und [PDF](vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf). Dieses Dokument ist kein Mustervertrag und darf nicht in der Praxis eingesetzt oder gegenüber echten Käuferinnen, Käufern, Bauträgern, Notariaten oder Behörden verwendet werden. Eine fachliche Bewertung setzt immer eine eigenständige rechtliche und technische Prüfung voraus.

## Keine Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

**Lesen, bevor irgendetwas davon eingesetzt wird.** Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft keinerlei Aussage darüber, ob der Einsatz dieses Skills in einer konkreten Praxisumgebung berufs-, datenschutz-, urheber-, haftungs-, notar- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss die Nutzerin oder der Nutzer in eigener Verantwortung vor der ersten Nutzung prüfen — das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- **Strafrechtliches Mandatsgeheimnis — §§ 203, 204 StGB.** Der Skill sagt nichts darüber, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB und § 204 StGB vereinbar ist, auch nicht in Konstellationen mit mitwirkenden Personen, Cloud-Diensten, externen Sachverständigen oder technischen Dienstleistern.
- **Berufsrecht — § 43e BRAO, § 2 BORA, § 53 StPO.** Es wird nicht geprüft, ob der Einsatz mit anwaltlichen, notariellen, steuerberatenden, wirtschaftsprüfenden, ärztlichen, patentanwaltlichen oder sonstigen berufsrechtlichen Pflichten vereinbar ist. Gleiches gilt für Zeugnisverweigerungsrechte, Beschlagnahmeschutz und die Einschaltung Dritter.
- **Datenschutz — DSGVO, BDSG.** Es wird nicht beurteilt, ob eine ausreichende Rechtsgrundlage vorliegt, ob ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO geschlossen werden muss, ob eine Datenschutz-Folgenabschätzung erforderlich ist oder ob Informationspflichten, Löschkonzepte, TOMs, Drittlandtransfers und Betroffenenrechte eingehalten werden.
- **KI-Verordnung — KI-VO / EU AI Act, VO (EU) 2024/1689.** Es wird nicht entschieden, ob der Einsatz unter Hochrisiko-, Transparenz-, Betreiber- oder General-Purpose-AI-Pflichten fällt und welche Dokumentations-, Kontroll- oder Informationspflichten in einer konkreten Nutzung bestehen.
- **Beschlagnahmeverbote und auslandsrechtliche Zugriffe.** Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme, Herausgabe, Cloud Act, FISA 702, CLOUD Act warrants, PATRIOT Act oder sonstige ausländische Zugriffsrechte hinreichend geschützt sind.
- **Zugang, Auftragsverarbeitung, Hosting.** Wie der API-Zugang zum Modell beschafft wird, ob mit dem Anbieter ein berufsrechtskonformer Vertrag besteht, wo Daten verarbeitet werden, welche Subunternehmer beteiligt sind und ob Datenresidenz, Verschwiegenheit, Audit-Rechte und Löschung gesichert sind, bleibt vollständig in der Eigenverantwortung der Nutzerin / des Nutzers.
- **Notar-, Anwalts- und Sachverständigenrolle.** Der Skill ersetzt keine notarielle Belehrung, keine anwaltliche Beratung, keine technische Bauzustandsprüfung, kein Bodengutachten, keine Objektüberwachung und keine baubegleitende Qualitätskontrolle.

Anwältinnen, Anwälte, Notarinnen, Notare, Sachverständige und andere Berufsgeheimnisträgerinnen/-träger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting-, Mandats-, Daten- und Sachverständigenkonstellation mit Berufsrecht, Datenschutz, Mandatsgeheimnis, Beschlagnahmeschutz, KI-Recht und Haftungsrecht vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz, technischer Bauprüfung oder vertraglicher Verschwiegenheit.

## Lizenz

Dieses Repository steht wahlweise unter der [MIT-Lizenz](LICENSE-MIT) oder der [Apache-2.0-Lizenz](LICENSE-APACHE) (Dual-Lizenz „MIT OR Apache-2.0"). Nutzerinnen und Nutzer dürfen frei zwischen beiden Lizenzen wählen.
