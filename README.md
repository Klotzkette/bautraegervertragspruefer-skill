# Bauträgervertrag-Prüfer Skill

**Direktdownload:** [📥 SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) · [📥 MINI_SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md)

Diese beiden Links zeigen die Markdown-Dateien nicht erst im Browser an, sondern verweisen über `releases/latest` immer auf die jeweils neueste Release-Datei mit Download-Header. Ein Klick lädt die aktuelle `.md`-Datei unmittelbar herunter; die Links bleiben über alle Versionen hinweg gültig.

> Experimenteller Agent-Skill für die verbraucherseitige und anwaltlich geprägte Prüfung deutscher Bauträgerverträge — als Anregung für Kanzlei-, Verbraucher- und Due-Diligence-Arbeitsabläufe. Orientiert sich an deutschem Bauträgerrecht, MaBV, AGB-Recht, amtlichen Gesetzestexten, frei überprüfbarer Rechtsprechung und technischer Projektprüfung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.
>
> Transparenz: Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Bauträgervertrags als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> Ein-Datei-Prinzip, modellunabhängig einsetzbar. Die Vollfassung steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne externe Laufzeit, ohne Datenbank, ohne Konto und ohne zusätzliches Werkzeug. Für kleine Kontextfenster gibt es zusätzlich [`skill/MINI_SKILL.md`](skill/MINI_SKILL.md). Beide Dateien funktionieren in leistungsfähigen KI-Chatbots bzw. Sprachmodellen: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Es ist keine Installation erforderlich — siehe [Anwendung](#anwendung-so-einfach-gehts).

Konsolidierter Skill (Version 3.2.7) für die Prüfung deutscher Bauträgerverträge nach dem Ampelsystem — Befunde werden als Ampelsymbole 🔴/🟠/🟢 ausgegeben, nicht als Farbwörter. Der Skill arbeitet nicht mit austauschbaren Textbausteinen, sondern zwingt vor jeder Bewertung einen Fall-Fingerabdruck: Urkunde, Parteien, Einheit, Projektgrundstück, Kaufpreis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Baugrund, Technik, WEG-Organisation und Streitstand. Er deckt den vollständigen Bogen ab: Mandanten-Intake, Verbraucherstatus, Beurkundungsphase, MaBV-Ratenplan, Sicherungsmechanik, AGB-Klauselkontrolle, Baubeschreibung, Bausoll, Fertigstellung, Abnahme, Schlussrate, Mängelrechte, Teilungserklärung, Gemeinschaftsordnung, Sondereigentum, Gemeinschaftseigentum, Eigentumssicherung, Insolvenzrisiken, Notar- und Vollzugsrisiken, Finanzierung, Baugrund, Baugrube, HOAI-Leistungsphasen, Objektüberwachung, private Bauüberwachung, technische Plausibilität, Beweislast, Durchsetzung und Verhandlungsstrategie.

Qualitätssicherung: Voll- und Mini-Fassung werden auf Versionsgleichlauf, Start- und Fortsetzungslogik sowie die drei Ausgabedokumente geprüft. Der Repository-Validator kontrolliert außerdem sämtliche Pages-Kopien der Vertragsakten, das 7.500-Zeichen-Limit der Mini-Fassung, neutrale Akten-ZIPs, die No-Meta-Regel und zentrale juristische Fehlzitate. Die Rechtsprechungskarte trennt Käufer-Mängelrechte von der zehnjährigen Verjährung des einheitlichen Bauträgervergütungsanspruchs und ordnet die zwingende Abschlagslogik korrekt `§ 650v BGB` in Verbindung mit `§§ 3, 12 MaBV` zu.

Schnellwahl: Für eine geführte Vertragsprüfung mit Rollenmodus, dichter Befundtabelle, textueller Einordnung und optionalem Vollpaket ist [`SKILL.md`](skill/SKILL.md) die Hauptfassung. Wenn ein kleineres Modell den langen Prompt nicht vollständig lädt oder die Antwort abbricht, ist [`MINI_SKILL.md`](skill/MINI_SKILL.md) die kompakte Ausweichfassung.

## Schnellzugriff

| Zweck | Link | Wann nehmen? |
| --- | --- | --- |
| Vollständiger Skill | [SKILL.md direkt herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) | Normalfall, gründliche Vertragsprüfung, Kanzlei-/Projektarbeit |
| Kompakte Fassung | [MINI_SKILL.md direkt herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md) | kleine Chatbots, mobile Apps, knappe Kontextfenster |
| Browser-Downloadseite | [klotzkette.github.io/bautraegervertragspruefer-skill](https://klotzkette.github.io/bautraegervertragspruefer-skill/) | wenn GitHub unübersichtlich ist oder Downloads in Apps klemmen |
| Aktenübersicht | [vertragsdokumente/README.md](vertragsdokumente/README.md) | wenn du die drei Vertragsakten vergleichen willst |

## Vertragsakten auf einen Blick

| Akte | Prüfprofil | Akten-ZIP | Deutsch: PDF / Word / Markdown | Deutsch/English-Lesefassung |
| --- | --- | --- | --- | --- |
| Hohenwartshofen | Fehlerakte mit vielen roten Pflichtbefunden | [ZIP](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip) | [PDF](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf) · [Word](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.docx) · [Markdown](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.md) | [HTML ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html) · [HTML laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.html) · [PDF laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.pdf) · [Word laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.docx) |
| Marewald | rechtmäßig, aber verkäuferfreundlich ausgereizt | [ZIP](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip) | [PDF](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf) · [Word](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx) · [Markdown](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md) | [HTML ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html) · [HTML laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-de-en.html) · [PDF laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-de-en.pdf) · [Word laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-de-en.docx) |
| Lindenhain | faire positive Kontrollakte | [ZIP](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip) | [PDF](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf) · [Word](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx) · [Markdown](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md) | [HTML ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html) · [HTML laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-de-en.html) · [PDF laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-de-en.pdf) · [Word laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-de-en.docx) |

## Sofort loslegen

Wer nur prüfen will, braucht keine Installation und keine GitHub-Kenntnisse:

1. Datei wählen: Normalfall [`SKILL.md`](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md), kleines Kontextfenster [`MINI_SKILL.md`](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md).
2. In den Chat legen: Datei in Claude, ChatGPT, Perplexity, Gemini, Mistral oder ein lokales Modell hochladen oder den Inhalt hineinkopieren.
3. Startsatz senden: Den kopierfertigen Startsatz aus [Anwendung](#anwendung-so-einfach-gehts) einfügen und Rollenmodus wählen.
4. Vertrag nachreichen: PDF, DOCX, Text, Foto oder Akten-ZIP hochladen. Der Skill prüft ohne Bedienungsrückfragen, gibt eine dichte erste Einordnung aus und bietet dann konkrete nächste Weichen an.

Robuster Start: Der Skill soll nie still hängen. Nach Upload oder Startsatz muss zuerst ein kurzes Startsignal kommen, danach erst die längere Prüfung. Bei großen PDF-/ZIP-Akten arbeitet er stufenweise: Pflichtblock, Zahlungsplan, Abnahme/Mängel, Technik, Dokumente. Jede längere Antwort trägt eine Fortsetzungsmarke. Wenn du `beenden`, `abbrechen` oder `stop` schreibst, muss der Skill sofort aufhören und erst bei ausdrücklichem `weiter` wieder ansetzen.

Dateiwahl ohne Nachdenken: Große Modelle und Kanzlei-/Projektarbeit: `SKILL.md`. Kleine Assistenten, mobile Apps, knappe Upload-Limits oder erste Vorführung: `MINI_SKILL.md`. Testlauf mit getrennten Unterlagen: erst die Skill-Datei, dann das passende Akten-ZIP.

Reihenfolge: Am stabilsten ist erst Skill-Datei, dann Startsatz, dann Vertrag. Wenn Skill und Vertrag schon gemeinsam in derselben Unterhaltung liegen, genügt der Startsatz; nicht neu hochladen, nicht von vorn beginnen.

### 60-Sekunden-Start

| Lage | Tu genau das |
| --- | --- |
| großes Modell, Kanzlei, gründliche Prüfung | `SKILL.md` herunterladen, in den Chat oder das Projekt legen, Startsatz senden, Vertrag oder Akten-ZIP hochladen |
| kleiner Chatbot, mobile App, knappes Kontextfenster | `MINI_SKILL.md` nehmen, Akten-ZIP mit Einzel-PDFs hochladen, `prüfe das` schreiben |
| Skill und Vertrag liegen schon im Chat | nichts neu hochladen; nur den Startsatz senden |
| Antwort hängt oder bricht ab | `Bitte fahre exakt an der letzten Überschrift fort und zeige danach die Nächste Weiche.` |
| sofort alles erstellen | `Vollpaket: Käufer-/Mandantenschreiben, Gutachten und Bauträgerschreiben jetzt erstellen.` |

## Was herauskommt

Der Skill arbeitet in zwei Modi. Im geführten Workflow beginnt er mit Rollenmodus, Kurzbild, Befundtabelle und Fließtext. Danach fragt er nicht einfach „weiter?", sondern bietet konkrete Weichen an: Befunde vertiefen, Mandanten-/Käuferschreiben erstellen, Gutachten ausarbeiten, Bauträgerschreiben erstellen, Technik vertiefen, Quellen prüfen oder das Vollpaket erzeugen. Im Vollpaket-Modus liefert er die drei Dokumente in fester Reihenfolge:

Workflow-Kompass:

| Situation | Passender Weg |
| --- | --- |
| erster Blick, Status, „was fällt auf?" | geführter Workflow mit Empfehlung für die nächste Weiche |
| finaler One-Shot oder „alle Schreiben" | Vollpaket ohne Nachfrage |
| Vertrag und Skill liegen schon zusammen im Chat | Startsatz senden; der Skill beginnt vorläufig in Rolle A |
| Antwort bricht wegen Länge ab | an der Fortsetzungsmarke weiterschreiben lassen |
| Prüfung soll wirklich enden | `beenden`, `abbrechen` oder `stop`; der Skill bestätigt Ende und arbeitet nicht weiter |
| nur Bedienfrage oder Uploadproblem | vier einfache Schritte, danach Vertrag/Akten-ZIP hochladen |

1. Kurzbild für die schnelle Orientierung: Vertragsstatus, rote/orange/grüne Treffer, wichtigste Sofortmaßnahme.
2. Übersendungsschreiben an den Mandanten: kurze, verständliche Einordnung mit Handlungsempfehlung.
3. Mandantengutachten: ausführliche Prüfung mit Klauselmatrix, Subsumtion, Normen, Quellenstand, Beweislandkarte, Technik- und Organisationsrisiken.
4. Aufforderungsschreiben an den Bauträger: konkrete Streichungen, Änderungsfassungen und kurze Begründungen; das Notariat nur bei Beurkundungs- oder Vollzugsthemen in Kopie oder Zusatzabsatz.

Der Schreibstil soll dicht sein: Tabellen ordnen die Befunde, die eigentliche Begründung steht in Fließtext. Wenn ein Chatbot wegen Länge abbricht, nicht neu starten: _"Bitte fahre mit dem nächsten noch fehlenden Abschnitt fort."_ Der Skill trägt selbst eine Fortsetzungsmarke und soll an der letzten Überschrift weiterschreiben, den Statuskopf aktualisieren und die empfohlene nächste Weiche anzeigen.

## Download

[📥 SKILL.md jetzt herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md)

Ein Klick genügt — dieser Link zeigt nicht die Browseransicht der Markdown-Datei, sondern lädt `SKILL.md` als Release-Datei mit Download-Header in den Downloads-Ordner. Kein Rechtsklick, kein "Speichern unter...", kein Umweg über Menüs.

Wenn eine App den Download trotz Release-Link abfängt, den Link gedrückt halten und "Link herunterladen" bzw. "Verknüpfte Datei laden" wählen. Alternativ die [komfortable Download-Seite](https://klotzkette.github.io/bautraegervertragspruefer-skill/) im normalen Browser öffnen.

Wer den Inhalt lieber direkt sehen und kopieren will, öffnet [`skill/SKILL.md`](skill/SKILL.md) — das ist die formatierte Ansicht hier im Repository. Der gesamte Text lässt sich dort mit `Strg+A` / `Cmd+A` markieren und kopieren.

## Bauträgerverträge zum Ausprobieren

Zum Ausprobieren des Skills liegen drei freistehende Bauträgervertragsakten bereit. Die komplette Download-Matrix steht oben unter [Vertragsakten auf einen Blick](#vertragsakten-auf-einen-blick); die ausführliche Aktenübersicht liegt unter [`vertragsdokumente/README.md`](vertragsdokumente/README.md).

| Akte | Was sie testet | Erwartung an den Skill |
| --- | --- | --- |
| Hohenwartshofen | grobe MaBV-, AGB-, Abnahme-, Sicherungs-, Bauüberwachungs- und Baubeschreibungsprobleme | viele rote Pflichtbefunde, konkrete Streichungs- und Korrekturvorschläge |
| Marewald | rechtmäßiger, aber deutlich verkäuferfreundlich ausgereizter Grenzvertrag | harte gelbe Verhandlungsbefunde, aber keine künstliche Nichtigkeit |
| Lindenhain | fairer, ausgewogener und leicht käuferfreundlicher Vertragsstand | überwiegend grüne Bestätigung, nur echte Präzisierungs- oder Verhandlungspunkte |

Alle drei Dokumente sind keine Musterverträge: nicht unterschreiben, nicht als Vorlage verwenden, nicht in der Praxis einsetzen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden verwenden. Eine fachliche Bewertung setzt immer eine eigenständige rechtliche und technische Prüfung voraus.

Akten-ZIPs: Jede Vertragsakte hat ein ZIP mit getrennten, neutral benannten Einzel-PDFs. Das ist die beste Übergabeform für KI-Systeme, die große Gesamt-PDFs schlechter auswerten oder bei langen Dokumenten abbrechen.

Deutsch-englische Lesefassungen: Die zweispaltigen Fassungen sind Verständnishilfen für Käuferinnen und Käufer, die den deutschen Vertrag lesen können, aber eine parallele englische Orientierung benötigen. Sie sind nicht als amtliche Übersetzung und nicht als zweite Vertragssprache gedacht; die Lesefassung selbst enthält die notarielle Vorlese- und Sprachvorrangklausel. Vorschau-Links öffnen die HTML-Fassung im Browser; Sofortdownload-Links gehen über `releases/latest` und laden die Dateien mit Download-Header.

## Kurzversion für kleinere Modelle

[📥 MINI_SKILL.md herunterladen](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md)

Wenn Claude, ChatGPT, Perplexity, Gemini, Mistral oder ein lokal betriebenes Modell die große `SKILL.md` nicht zuverlässig annimmt, zu früh abbricht oder nur ein kleiner Skill-Kontext zur Verfügung steht, ist [`skill/MINI_SKILL.md`](skill/MINI_SKILL.md) die Sparversion. Sie hat maximal 7.500 Zeichen inklusive Leerzeichen und enthält trotzdem den Kern: Rollenmodus, geführter Workflow, harte Quellenregeln, MaBV-/AGB-/WEG-/Technik-Pflichtblock, No-Meta-Regel, Anti-Generik-Regel und Vollpaket-Option.

Die Kurzversion ist nicht so tief wie die Vollfassung. Sie ist dafür schnell kopierbar, robust in kleineren Assistenten und gut genug abgehangen, um auch dort Zahlungsplan, Sicherheiten, Abnahme, Bausoll, Bauüberwachung, Preisanpassung, Verzug und die wichtigsten AGB-Risiken strukturiert zu prüfen.

Mini-Output-Garantie: Auch die Kurzfassung endet nicht bei einer bloßen Einschätzung. Sie führt kleine Modelle auf Kurzbild, Befundtabelle, textuelle Einordnung und Nächste Weiche; im Vollpaket zwingt sie zu Käufer-/Mandantenschreiben, Mandantengutachten und Aufforderungsschreiben an den Bauträger.

## Anwendung: So einfach geht's

Kopierfertiger Startsatz für jeden Chatbot, jedes Projekt und jede Assistant-Konfiguration:

```text
Bitte nutze die gerade hochgeladene SKILL.md oder MINI_SKILL.md als Arbeitsanweisung.
Bitte frage mich zuerst nach dem Rollenmodus: A Käufer/in selbst, B anwaltlich für Käufer/in, C neutraler Schnellcheck.
Wenn ich gleich einen Bauträgervertrag hochlade oder einfüge, prüfe ihn ohne Rückfragen-Kaskade mit Kurzbild, dichter Befundtabelle, Fließtext-Einordnung und einer Nächsten Weiche.
Wenn ich „Vollpaket" schreibe, liefere bitte drei Dokumente: 1. Käufer-/Mandantenschreiben, 2. ausführliches Mandantengutachten, 3. Aufforderungsschreiben an den Bauträger mit konkreten Änderungsfassungen.
```

Einfachster Weg — Datei hochladen:

1. [`SKILL.md`](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) oder bei engem Kontext [`MINI_SKILL.md`](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md) herunterladen.
2. Datei in das Chatfenster, Projektwissen oder die Assistant-/Skill-Konfiguration ziehen.
3. Startsatz senden.
4. Vertrag oder Akten-ZIP hochladen.

Wenn Datei-Upload nicht klappt — Text kopieren:

1. [`skill/SKILL.md`](skill/SKILL.md) öffnen, den gesamten Text mit `Strg+A` / `Cmd+A` markieren und in den Chat einfügen. Wenn das Modell die Vollfassung nicht annimmt, stattdessen [`skill/MINI_SKILL.md`](skill/MINI_SKILL.md) verwenden.
2. Dazuschreiben: _"Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Bauträgervertrag — bearbeite ihn danach."_ Enter drücken.
3. Den Vertrag einfügen oder hochladen (Text, PDF, DOCX oder Foto). Die Analyse startet von selbst.

Sofortstart in beiden Wegen: Der Skill analysiert ohne Rückfragen-Kaskade, kennzeichnet fehlende Angaben als Annahmen, prüft mit Ampelsymbolen, priorisiert verbraucherschützende Einwände und liefert harte Gegenargumente für Bauträger, Notariat, Vertrieb und finanzierende Bank. Wenn der Vertrag schon vorliegt, nimmt er Rolle A vorläufig an und bietet den Wechsel zu B oder C in der nächsten Weiche an. Eine gebündelte Rückfrage gibt es höchstens dann, wenn die Analyse sonst objektiv falsch oder irreführend würde. Wenn Live-Recherche nicht verfügbar ist, beginnt der Skill trotzdem und kennzeichnet nur tragende Rechtsprechungslinien später als nicht live verifiziert.

Projekt, Co-Work oder Assistant-Konfiguration: Die Datei als Projektwissen, Skill-Datei, Systemanweisung oder dauerhafte Arbeitsanweisung hinterlegen. Wenn die Oberfläche nach einem Zweck fragt: _"Prüft deutsche Bauträgerverträge verbraucherseitig im geführten Workflow oder als Vollpaket mit Käufer-/Mandantenschreiben, Gutachten und Bauträgerschreiben."_ Wenn die Oberfläche nach einem Startprompt fragt, den kopierfertigen Startsatz oben verwenden.

Wenn der Chatbot stehenbleibt: Nicht neu anfangen. Schreibe einfach: _"Bitte fahre an der letzten Überschrift fort und zeige mir danach die Nächste Weiche."_ Wenn du das Vollpaket wolltest: _"Bitte fahre mit dem nächsten noch fehlenden Dokument fort."_ Wenn die Vollfassung mehrfach abbricht, lade stattdessen `MINI_SKILL.md` und den Akten-ZIP mit Einzel-PDFs hoch; kleinere Modelle kommen mit getrennten PDFs oft schneller zu belastbaren ersten Befunden.

Wenn gar nichts passiert: Einmal klar nachschieben: _"Du hast jetzt die Arbeitsanweisung. Bitte beginne mit Rollenmodus, Pflicht-Prüfblock, Befundtabelle und Nächster Weiche."_ Danach nicht weiter erklären, sondern den Vertrag oder das Akten-ZIP hochladen.

Wenn Skill und Vertrag schon zusammen hochgeladen wurden: Einfach den Startsatz senden. Das Modell soll dann sofort mit dem Pflicht-Prüfblock beginnen und keine neue Upload-Reihenfolge verlangen.

Wenn du die Prüfung beenden willst: Schreibe `beenden`, `abbrechen` oder `stop`. Der Skill soll dann nur noch bestätigen, dass er keine weiteren Prüfschritte ausführt. Eine spätere Fortsetzung beginnt erst nach einer neuen ausdrücklichen Weisung wie `weiter ab Dokument 2` oder `prüfe erneut`.

## Inhalt

```text
skill/
├── SKILL.md       Vollfassung: Workflow, Quellenregeln, Klauselmatrix,
│                  Rechtsanker, Technikmodule, Mandantenbericht, Verhandlungspaket
└── MINI_SKILL.md  Kurzfassung mit maximal 7.500 Zeichen für kleinere KI-Kontexte

docs/
├── SKILL.md       Veröffentlichte Vollfassung
├── MINI_SKILL.md  Veröffentlichte Kurzfassung
├── index.html     Download-Seite für Browser und Mobilgeräte
└── vertragsdokumente/  Veröffentlichte Spiegel der Vertragsakten

scripts/
├── build_bilingual_contracts.py  Erzeugt die deutsch-englischen Lesefassungen
└── validate_repo.sh              Lokaler Sanity-Check für Versionen, Downloads,
                                  Mini-Limit, Docs-Sync, Testakten und No-Meta-Regel

vertragsdokumente/
├── bautraegervertrag/
│   ├── bautraegervertrag.md / .docx / .pdf
│   ├── bautraegervertrag-de-en.html / .docx / .pdf
│   ├── bautraegervertrag-einzel-pdfs.zip
│   └── build.sh, build/
├── bautraegervertrag-marewald/
│   ├── bautraegervertrag-marewald.md / .docx / .pdf
│   ├── bautraegervertrag-marewald-de-en.html / .docx / .pdf
│   ├── bautraegervertrag-marewald-einzel-pdfs.zip
│   └── build.sh, build/
└── bautraegervertrag-lindenhain/
    ├── bautraegervertrag-lindenhain.md / .docx / .pdf
    ├── bautraegervertrag-lindenhain-de-en.html / .docx / .pdf
    ├── bautraegervertrag-lindenhain-einzel-pdfs.zip
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
- Mandatsmodule — Käufer-/Mandantenbericht, Bauträgeranschreiben, Notariatszusatz nur bei Beurkundungs-/Vollzugspunkten, Verhandlungsfassung, Eskalations- und Klagestrategie.
- Vertragsdokumente (separate Dateien) — zusätzlich zur Skill-Datei liegen unter `vertragsdokumente/` drei freistehende Bauträgerverträge mit Baubeschreibung als Anlage bereit: Fehlerakte, Verkäufer-Grenzvertrag und faire Käufer-Kontrollakte. Jede Akte enthält außerdem ein ZIP mit getrennten Einzel-PDFs und eine zweispaltige deutsch-englische Lesefassung.

Zusätzlich enthält der Skill durchgängig:

- Verbraucherschützende Priorisierung — der Skill sucht nicht nur formale Fehler, sondern wirtschaftliche, technische und organisatorische Schieflagen.
- Überzeugungsdisziplin — jedes harte Argument soll so formuliert werden, dass es gegenüber Notariat, Bauträger und deren Prozessvertretung belastbar ist.
- Kein Blindzitat — tragende Rechtsprechung wird nicht aus Modellwissen erfunden; Quellen werden als zu verifizieren markiert oder mit frei überprüfbarem Fundort benannt.
- No-Meta-Regel für jedes Vertragsdokument — der Skill spricht nie über Herkunft, Repository, Beispiel, Demonstration oder Dateirolle, sondern prüft ausschließlich den vorgelegten Vertragsstoff.
- Anti-Generik-Regel — kein Befund darf ohne Fallanker ausgegeben werden; jede rote oder orange Ampel braucht Klausel, Betrag/Rate/Frist oder Projekt-/Einheitsbezug und eine konkrete Änderungsfassung.
- Subsumtions-Gate — jede rote oder orange Ampel braucht Textstelle, konkrete Klauselwirkung, Rechtsfolge, Beweis-/Darlegungslast und Antwort auf das stärkste Gegenargument.
- Technischer Realitätscheck — ein juristisch eleganter Vertrag genügt nicht, wenn Baugrund, Baugrube, Abdichtung, Bauüberwachung oder Nachweislage nicht tragen.
- Geführter Workflow und Vollpaket — zunächst Kurzbild, Befundtabelle, Fließtext und Nächste Weiche; auf Wunsch das Vollpaket mit Käufer-/Mandantenschreiben, ausführlichem Gutachten und Bauträgerschreiben.
- Statuskopf und Fortsetzungsmarke — Rolle, Kurzbild, Modus, Dokumente 1 bis 3, Empfehlung und Fortsetzungspunkt werden markiert, damit auch kleine Modelle nach Abbruch sauber fortsetzen.
- Release-Validierung — `scripts/validate_repo.sh` prüft vor Veröffentlichung die harten Repo-Invarianten; `.github/workflows/validate.yml` führt denselben Check in GitHub Actions aus.
- Aktualisierte Rechtsprechungsanker — BGH 2026 zu Schlussrate, Abnahme, 30-Jahres-Obergrenze und Teilungserklärungsänderung; KG/OLG als gewichtete Instanzanker zu Bezugsfertigkeit, flexiblem Ratenplan, § 650m-Sicherheit, Übergabeprotokollen und GdWE-Mängelrechten.
- Mini-Fallback — für kleine Kontextfenster gibt es `MINI_SKILL.md`; sie ersetzt die Vollfassung nicht, hält aber Rollenmodus, Kernworkflow, Weiche und Vollpaket-Option fest.

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
