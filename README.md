# Bauträgervertrag-Prüfer Skill

> **Experimenteller Agent-Skill** für die verbraucherseitige und anwaltlich geprägte Prüfung deutscher Bauträgerverträge — als Anregung für Kanzlei-, Verbraucher- und Due-Diligence-Arbeitsabläufe. Der Skill orientiert sich an deutschem Bauträgerrecht, MaBV, AGB-Recht, frei überprüfbarer Rechtsprechung und technischen Projektprüfungen. Er ist kein Rechtsrat, kein Fachgutachten und keine notarielle Belehrung; alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.

> **Transparenz:** Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Bauträgervertrags als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> **Eine einzige Datei, modellunabhängig einsetzbar.** Der vollständige Skill steckt in einer Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md). Er funktioniert in jedem leistungsfähigen KI-Chatbot bzw. Sprachmodell: Claude, ChatGPT, Gemini, Mistral, Perplexity oder lokal betriebene Modelle. Es ist keine Installation, kein Konto und kein zusätzliches Werkzeug erforderlich.

**Version 2.2.0** liefert eine strukturierte, verhandlungsfähige Arbeitsfassung für Entwurf, Beurkundung, Bauphase, Abnahme, Technik, WEG-Organisation, Wirtschaft und Streit.

Der Skill steckt vollständig in einer Datei: [`skill/SKILL.md`](skill/SKILL.md). Er kann in leistungsfähige KI-Chatbots eingefügt oder als Datei hochgeladen werden. Die veröffentlichte Downloadfassung liegt unter [`docs/SKILL.md`](docs/SKILL.md) und wird über GitHub Pages bereitgestellt.

## Download

➡️ **[SKILL.md direkt herunterladen](https://klotzkette.github.io/bautraegervertragspruefer-skill/SKILL.md)** ⬅️

Alternativ die [Download-Seite](https://klotzkette.github.io/bautraegervertragspruefer-skill/) öffnen.

## Was Version 2.2.0 macht

- Prüft zuerst einen festen Pflichtblock: § 650m Abs. 2 BGB, § 309 Nr. 12 BGB, § 309 Nr. 15 BGB, MaBV-Fälligkeit, Abnahme Gemeinschaftseigentum, Schlussrate, Teilungserklärung und Bausoll.
- Trennt sauber zwischen Bauträgervertrag (§ 650u BGB), Verbraucherbauvertragsnormen, Kaufrecht, MaBV und AGB-Kontrolle.
- Korrigiert die MaBV-Logik: § 3 Abs. 2 MaBV arbeitet mit bis zu sieben Teilbeträgen, zusammengesetzt aus gesetzlichen Prozentbausteinen.
- Prüft jetzt zusätzlich die Projektrealität: HOAI-Leistungsphasen, LPH 8/Objektüberwachung, private Bauüberwachung, Baugrund/Baugrube, Grundwasser, Altlasten, Haustechnik, Wartungsverträge, Betriebskosten und WEG-Organisation.
- Härtet die Testakte „Bauträgervertrag aus der Hölle" mit einem professioneller wirkenden, aber verdeckt riskanten Raten-, Technik- und Bauüberwachungsregime.
- Verlangt harte Quellen: offizielle Gerichtsseiten, Landesrechtsprechungsportale, `gesetze-im-internet.de`, DeJure oder OpenJur. Keine BeckRS-, beck-online-, juris- oder Kanzleiblog-Zitate als Beleg.
- Liefert zu roten Klauseln erwartbare Bauträger-/Notarargumente und eine juristisch belastbare Antwort.
- Enthält eine 30-Punkte-Prüfschleife und einen Bug-Hunt gegen typische Rechtsfehler.

## Aktuelle Rechtsprechungsanker

Eingebaut sind insbesondere:

- **BGH, 26.03.2026 - VII ZR 68/24**: Abnahme des Gemeinschaftseigentums durch Erwerbervertreter ohne eigenes Prüf-/Abnahmerecht ist unwirksam.
- **BGH, 26.03.2026 - VII ZR 108/24**: Sachverständigenabnahme ohne eigenes Erwerberrecht ist unwirksam.
- **BGH, 22.04.2026 - VII ZR 88/25**: Schlussrate kann bei offenen protokollierten Mängeln trotz Abnahme nicht fällig sein.
- **BGH, 23.01.2026 - V ZR 91/25**: Pauschale Zustimmungspflichten zu späteren Änderungen der Teilungserklärung sind ohne benannte triftige Gründe unwirksam.
- **BGH, 09.11.2023 - VII ZR 241/22**: Abnahme durch bauträgernahe Gesellschaft/Person und Folgen unwirksamer Abnahmeklauseln.
- **BGH, 02.08.2023 - VII ZB 28/20**: Notaranderkonto, Verwahrungsanweisung und MaBV-Fragen getrennt prüfen.

## Anwendung

**Weg A — Text kopieren**

1. [`skill/SKILL.md`](skill/SKILL.md) öffnen.
2. Kompletten Text in den Chat einfügen.
3. Dazu schreiben: `Bitte halte dich an diesen Skill. Gleich kommt ein Bauträgervertrag.`
4. Vertrag, Auszug, PDF oder Foto nachreichen.

**Weg B — Datei hochladen**

1. `SKILL.md` herunterladen.
2. Datei in den Chat ziehen.
3. Vertrag nachreichen.

Der Skill startet ohne Rückfragenkaskade und liefert Pflicht-Prüfblock, Klauselmatrix, MaBV-Prüfung, Rechtsprechungsanker, Verhandlungspaket und Restfragen.

## Aufbau

```text
skill/
└── SKILL.md   Arbeitsfassung des Skills
docs/
├── SKILL.md   veröffentlichte Downloadfassung
└── index.html Downloadseite
```

Die Skill-Datei enthält:

- Harte Quellenregeln.
- Aktuelle Rechtsprechungsanker 2023-2026.
- Normenkarte zu § 650u, § 650v, § 650j, § 650k, § 650m, § 650n BGB, §§ 305 ff. BGB und MaBV.
- 30 Prüfschleifen für die Vollanalyse.
- Pflicht-Prüfblock.
- Workflow und Antwortformate.
- MaBV-Zahlungsprüfung.
- AGB-Klauselkatalog mit Gegenargument und Antwort.
- Baubeschreibung/Bausoll, Abnahme, Schlussrate, Teilungserklärung, Eigentumsschutz, Insolvenz, Verhandlung und Streit.
- HOAI-/Objektüberwachungs-, Baugrund-, Technik-, Wartungs-, Betriebskosten- und WEG-Organisationsprüfung.
- Bug-Hunt vor Ausgabe.

## Rechtlicher Hinweis

Die anwaltliche Prüfung eines Bauträgervertrags ist Rechtsdienstleistung. Dieser Skill ist eine offene Arbeitsanweisung für KI-Systeme und eine strukturierte Vorbereitung. Er ersetzt keine anwaltliche Beratung, keine notarielle Belehrung und keine Einzelfallprüfung.

Keine konkreten Mandatsunterlagen öffentlich in Issues oder Pull Requests posten.

## Keine Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

Dieses Repository ist ein technisches und fachliches Experiment. Es trifft **keine Aussage** darüber, ob der Einsatz dieses Skills in einer konkreten Kanzlei-, Unternehmens-, Verbraucher- oder Behördenumgebung berufs-, datenschutz-, geheimnisschutz- oder KI-rechtlich zulässig ist.

Vor produktiver Nutzung muss jede Nutzerin und jeder Nutzer eigenverantwortlich prüfen:

- **Mandatsgeheimnis und Berufsrecht:** Vereinbarkeit mit §§ 203, 204 StGB, § 43e BRAO, § 2 BORA sowie den jeweils einschlägigen Berufsordnungen anderer Berufsgeheimnisträger.
- **Beschlagnahme- und Zeugnisverweigerungsschutz:** Umgang mit § 53 StPO, § 97 StPO, § 160a StPO und vergleichbaren Schutzmechanismen, insbesondere wenn Entwürfe, Kaufpreise, Finanzierungsdaten, Grundbuchdaten, Gutachten oder Mandantenkommunikation verarbeitet werden.
- **Datenschutz:** Rechtsgrundlage, Art. 28 DSGVO, TOMs, Löschkonzept, Subunternehmer, Datenresidenz, Drittlandtransfer, Informationspflichten und besondere Risiken bei personenbezogenen Vertrags-, Finanzierungs- und Familiendaten.
- **KI-VO / EU AI Act:** Ob der konkrete Einsatz unter Pflichten für Betreiber, Transparenzpflichten oder besondere Risikokategorien fällt, hängt von Anwendung, Anbieter, Deployment und Nutzerkreis ab.
- **Hosting und Anbieterwahl:** Ob ein Modell direkt, über Cloud-Anbieter, über Kanzlei-IT oder lokal betrieben wird, ist für Geheimnisschutz, Datenschutz und Zugriffsbefugnisse zentral. Dieses Repository bestätigt keinen Anbieter.
- **Auslandsrechtliche Zugriffe:** Risiken aus extraterritorialen Zugriffsrechten wie US Cloud Act, FISA § 702 oder vergleichbaren Regelungen sind nicht bewertet.

Der Skill darf nicht so verstanden werden, als sei die Eingabe echter Mandats-, Vertrags-, Grundbuch-, Finanzierungs-, Bau- oder Gutachtendaten in irgendein Modell automatisch zulässig. Diese Prüfung bleibt vollständig bei der jeweiligen Nutzerin oder dem jeweiligen Nutzer.

## Lizenz

Doppellizenziert: **Apache-2.0 OR MIT**. Siehe [`LICENSE-APACHE`](LICENSE-APACHE) und [`LICENSE-MIT`](LICENSE-MIT).
