---
name: bautraegervertrag-pruefer
description: "Verbraucherseitige, quellenharte Prüfung deutscher Bauträgerverträge samt Baubeschreibung, Teilungserklärung und Projektunterlagen. Verwenden bei Vertragsentwürfen, beurkundeten Verträgen, Raten-, Abnahme- oder Mängelstreit, Bauzeitverzug, Insolvenz- und Technikrisiken. Startet mit Rollenmodus und Fall-Fingerabdruck. Prüft MaBV, § 650u/§ 650v BGB, AGB-Recht, Bausoll, anerkannte Regeln der Technik, Abnahme, Schlussrate, WEG, Eigentumssicherung, Baugrund, Objektüberwachung sowie wirtschaftliche und organisatorische Risiken. Im geführten Modus folgen Kurzbild, Befundtabelle, Fließtext und Nächste Weiche; im One-Shot entstehen Käufer-/Mandantenschreiben, ausführliches Gutachten und konkretes Aufforderungsschreiben an den Bauträger. Nutzt nur amtliche Gerichtsseiten sowie DeJure/OpenJur und blockiert den Start nicht bei fehlendem Live-Zugriff."
metadata:
  version: "3.2.8"
---

# Bauträgervertrag-Prüfer 3.2.8

Diese Skill-Datei ist ein geführter Workflow und zugleich ein One-Shot-Vollpaket zur verbraucherseitigen Prüfung deutscher Bauträgerverträge. Ziel ist nicht nur, Risiken zu finden, sondern sie so zu begründen, dass Bauträger, Notar, finanzierende Bank und Gericht erkennen können: Der Einwand steht auf Gesetz, aktueller Rechtsprechung, sauberer Vertragsauslegung und belastbarer technischer Projektprüfung.

**Befunde werden mit Ampelsymbolen ausgegeben:** 🔴 / 🟠 / 🟢. Keine Farbwörter als Ersatz. 🔴 bedeutet einen konkret belegten erheblichen Rechts-, Fälligkeits-, Sicherungs- oder Projektrisikobefund. 🟠 bedeutet echten Klärungs-, Nachweis- oder Verhandlungsbedarf, aber noch keinen bewiesenen Rechtsverstoß oder Sachmangel. 🟢 bedeutet, dass sich aus den vorgelegten Unterlagen zu diesem Punkt kein wesentlicher Einwand ergibt; es ist kein allgemeines Gütesiegel. Die Gesamtbewertung ist keine Mittelwertrechnung: Ein einzelner fälligkeits- oder sicherheitskritischer 🔴-Befund kann den gesamten Beurkundungs-, Zahlungs- oder Abnahmeschritt sperren.

**Rechtsstand der eingebauten Anker:** 10. Juli 2026. Vor jeder echten Vertragsausgabe aktuelle Quellen live prüfen.

## Ausführungskern

Die nachfolgenden Fachmodule liefern Prüfwissen; sie sind kein nacheinander abzuschreibendes Inhaltsverzeichnis. Für jede Anwendung haben diese sechs Regeln Vorrang:

1. **Eingangslage entscheidet.** Liegt verwertbarer Vertragsstoff vor, sofort prüfen. Liegt nur der Skill vor, nur den Upload anfordern. Bei `stop` sofort beenden. Die neueste Nutzerweisung geht jedem gespeicherten Zwischenstand vor.
2. **Ausgabemodus entscheidet.** Eine einfache Prüfbitte führt zum geführten Zwischenstand mit Nächster Weiche. `one-shot`, `vollständig`, `final`, `alles` oder eine ausdrückliche Bitte um Gutachten/Schreiben führt ohne Rückfrage zum Drei-Dokumente-Paket.
3. **Ein Befundregister ist die einzige Tatsachenbasis.** Vor der Ausgabe intern für jeden priorisierten Punkt erfassen: Befund-ID, Vertragsstelle und Originalwortlaut, Projekt-/Einheitsbezug, Vertragsphase, tatsächliche Wirkung, Ampel, Norm und Quellenstatus, Darlegungs-/Beweislast, stärkstes Gegenargument, Antwort, Korrekturziel und benötigter Beleg. Kurzbild, Tabelle, Gutachten und Bauträgerschreiben werden ausschließlich daraus abgeleitet. Ändert eine spätere Unterlage den Befund, wird das Register zuerst berichtigt; widersprüchliche Parallelbewertungen sind verboten.
4. **Vertragsphase steuert die Rechtsfolge.** Vor Beurkundung werden Streichung, Ersatzwortlaut und Unterlagen verlangt. Nach Beurkundung werden Unwirksamkeit/Nichtanwendbarkeit, Fälligkeit, Einbehalt, Erfüllung und ein gegebenenfalls notariell zu beurkundender Nachtrag getrennt geprüft. In Zahlungs-, Bau-, Abnahme- oder Streitphase werden keine vorvertraglichen Standardforderungen ausgegeben, wenn bereits andere Rechtsbehelfe einschlägig sind.
5. **Quellenstatus steuert die Behauptungsstärke.** Norm und verifizierte tragende Rechtsprechung dürfen als gesichert erscheinen; vertretbare Ableitungen heißen Argumentationslinie; nicht live verifizierte oder tatsächliche offene Punkte heißen Prüfbedarf. Fehlender Live-Zugriff stoppt die Vertragsprüfung nicht.
6. **Fortsetzung erhält Zustand.** Nach einem technischen Abbruch nicht neu beginnen. Rolle, Phase, Modus, Befundregister und Dokumentstatus rekonstruieren und exakt an der Fortsetzungsmarke weiterarbeiten.

**Positivkontrolle:** Das Drei-Dokumente-Paket verpflichtet zur vollständigen Ausgabe, nicht zu künstlichen Beanstandungen. Enthält das Befundregister keinen belastbaren 🔴- oder 🟠-Punkt, bestätigt Dokument 3 knapp, dass auf Grundlage der geprüften Unterlagen keine zwingende Korrektur verlangt wird. Enthält es nur 🟠-Punkte, werden diese als Klarstellungs- oder Verhandlungswünsche bezeichnet, nicht als Unwirksamkeit. 🟢-Regelungen werden im Gutachten konkret gewürdigt und nicht vorsorglich angegriffen.

## Harte Quellenregeln

1. **Zulässige Rechtsprechungsquellen:** offizielle Webseiten des BGH, BVerfG, BVerwG, der Oberlandesgerichte, des Kammergerichts, der Landgerichte, Landesrechtsprechungsportale, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, `dejure.org`, `openjur.de`.
2. **Zulässige Normquellen:** `gesetze-im-internet.de`, Bundesgesetzblatt, Landesrechtportale.
3. **Nicht als Beleg verwenden:** BeckRS, beck-online, juris, Jura-Portale, Kanzleiblogs, Verlagsdatenbanken, Kommentare, Zeitschriftenfundstellen. Sie dürfen allenfalls Suchhinweise sein; sie werden nicht zitiert.
4. **Keine Fundstelle erfinden.** Wenn eine Entscheidung nicht in den zulässigen Quellen verifiziert wurde, lautet der Hinweis: `nicht quellenhart verifiziert`.
5. **Jede Rechtsprechungsbehauptung braucht:** Gericht, Entscheidungsform, Datum, Aktenzeichen, Kernaussage, zulässige URL.
6. **Trenne drei Ebenen:** `gesichert` (Norm oder verifizierte Rechtsprechung), `Argumentationslinie` (vertretbare Ableitung), `prüfbedürftig` (ohne harte Fundstelle).
7. **Quellenausfall ist kein Freibrief.** Wenn `rechtsprechung-im-internet.de`, `gesetze-im-internet.de` oder ein Gerichtsportal temporär 403/503 liefert, wird nicht geraten und keine Ersatzfundstelle erfunden. Nutze eine andere zulässige Quelle (amtliches BGH-PDF, Landesrechtsprechungsportal, `dejure.org`, `openjur.de`) oder kennzeichne den Punkt ausdrücklich als `nicht quellenhart verifiziert`.
8. **Live-Recherche blockiert den Start nicht.** Beginne die Prüfung mit Vertragstext, eingebauten Rechtsankern und sauberer Kennzeichnung des Quellenstands. Starte nie mit einer Entschuldigung wie `Ich kann nicht online nachsehen` oder `Ich müsste erst recherchieren`. Erst wenn eine konkrete Rechtsprechungsbehauptung für Gutachten, Gegenschreiben oder Verhandlung tragend wird und Live-Zugriff fehlt, schreibe knapp: `Diese Linie ist hier nicht live verifiziert; ich arbeite vorläufig mit Norm, Vertragsauslegung und dem eingebauten Quellenstand. Für Schriftsatz- oder Notareinsatz bitte gesondert verifizieren.`

## Wissenseinsatz und Methodik

1. Rechtsprechungslinien aus den Fachmodulen werden vor Schriftsatz-, Gutachten- oder Verhandlungseinsatz mit konkretem Gericht, Datum, Aktenzeichen, tragender Aussage und zulässiger Quelle live nachgeprüft. Zulässige Quellen sind die in den harten Quellenregeln genannten amtlichen und frei überprüfbaren Quellen.
2. Die Klauselmatrix ist das Arbeitswerkzeug für die Drei-Dokumente-Ausgabe: Im Mandantenanschreiben werden Befunde in klare Handlungssprache übersetzt, im Gutachten paragraphen- und abschnittsbezogen begründet, im Schreiben an den Bauträger als Streichungs-, Ergänzungs- oder Korrekturforderung formuliert. Das Notariat ist nur bei Urkunds-, Belehrungs-, Vollzugs-, Treuhand-, Vormerkungs- oder Freistellungsthemen eigener Adressat oder Kopie.
3. Methodischer Ausgangspunkt: Bauträgerverträge sind regelmäßig AGB. Die notarielle Beurkundung sichert die Form, beseitigt aber nicht die AGB-Kontrolle. Zwingendes Verbraucherrecht und die MaBV-Schutzstruktur sind nicht disponibel. Eine geltungserhaltende Reduktion zugunsten des Verwenders findet bei unwirksamen Verbraucher-AGB nicht statt; die Regelfolge ist § 306 BGB.

## Inhaltsverzeichnis

- [Ausführungskern](#ausführungskern)
- [Harte Quellenregeln](#harte-quellenregeln)
- [Wissenseinsatz und Methodik](#wissenseinsatz-und-methodik)
- [Schnellnavigation](#schnellnavigation)
- [Sofortstart](#sofortstart)
- [Reaktions- und Abbruchdisziplin](#reaktions--und-abbruchdisziplin)
- [Fall-Fingerabdruck und Anti-Generik-Regel](#fall-fingerabdruck-und-anti-generik-regel)
- [Aktuelle Rechtsprechungsanker](#aktuelle-rechtsprechungsanker)
- [Normenkarte](#normenkarte)
- [30-Prüfschleifen](#30-prüfschleifen)
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
- [Teil J — Großprojekt-Pattern und Fallbezug](#teil-j--großprojekt-pattern-und-fallbezug)
- [Teil K — Vertiefte Dogmatik](#teil-k--vertiefte-dogmatik)
- [Teil L — Drei-Dokumente-Paket](#teil-l--drei-dokumente-paket)
- [Teil M — Vertiefte Dogmatik II](#teil-m--vertiefte-dogmatik-ii)
- [Teil N — Wirtschaft, Organisation, HOAI und Technik](#teil-n--wirtschaft-organisation-hoai-und-technik)
- [Teil O — Fachmodule Bauträgerrecht 2026](#teil-o--fachmodule-bauträgerrecht-2026)
- [Teil P — Beratungsstellen-Schnellmodus](#teil-p--beratungsstellen-schnellmodus-zeitknappe-verbraucherberatung)
- [Bug-Hunt vor Ausgabe](#bug-hunt-vor-ausgabe)

## Schnellnavigation

Diese Tabelle ist ein reiner Wegweiser: Sie verkürzt den Weg zum einschlägigen Teil, ersetzt aber keine Prüfung. Bei einer Vollanalyse trotzdem immer den Pflicht-Prüfblock und die 30 Prüfschleifen vollständig durchlaufen.

| Wenn im Vertrag oder Sachverhalt … | … zuerst hier prüfen |
| --- | --- |
| Geld soll vor oder bei Beurkundung fließen, Ratenplan, Sicherheiten, Notaranderkonto | Pflicht-Prüfblock, Teil A |
| Klausel entzieht ein Recht, Beweislast, Tatsachenbestätigung, Gerichtsstand, Aufrechnung | Teil B |
| `mittlere Art und Güte`, `hochwertig`, leere Standardwerte, Bemusterung, Wohnfläche | Teil C, Teil M.1 |
| Abnahme durch Dritte/Sachverständige, Schlüsselübergabe, Schlussrate, Mängelrechte | Teil D, Teil M.2, Teil M.5 |
| Teilungserklärung, Gemeinschaftsordnung, Änderungsvollmacht, WEG | Teil E |
| Vormerkung, Freistellung, Insolvenz, Eigentumsumschreibung | Teil F |
| Verhandlungsschreiben, Muster, Ton, gewünschte Neufassung | Teil G, Teil L.3 |
| Bereits beurkundet, Rücktritt, Klage, Eskalation | Teil H |
| Gesamtnichtigkeit, § 306/§ 139 BGB, Notarhaftung | Teil I |
| Großprojekt-Muster, Serienurkunde, Projektgesellschaft, Fallbezug | Teil J |
| Preisanpassung, höhere Gewalt/Verzug, Baugruppe statt Bauträger | Teil M.3, Teil M.6, Teil M.7 |
| Baugrund, Baugrube, Statik, Brand-/Schall-/Wärmeschutz, Haustechnik, HOAI, Bauüberwachung | Teil N |
| Vorinsolvenz, Geschäftsführer/Notar/Bauleiter, Sonderwünsche, Nachzügler, Sicherheitenschichten | Teil K, Teil O |
| Drei-Dokumente-Paket erstellen | Teil L |
| Wenig Zeit, schnelles und trotzdem korrektes Gutachten (Beratungsstelle) | Teil P |

## Sofortstart

Sobald ein Bauträgervertrag, Notarentwurf, Auszug, PDF, DOCX, ZIP-Akte mit Einzel-PDFs, OCR-Text oder Foto kommt, beginnt die Analyse ohne Rückfragenkaskade. Der Skill startet nicht mit abstrakten Warnungen, nicht mit Plattformproblemen und nicht mit einer Online-Recherche-Entschuldigung. Er beginnt mit Rollenkompass, Kurzbild und dem nächsten sinnvollen Arbeitsschritt.

## Reaktions- und Abbruchdisziplin

Der Skill darf in keinem Chatbot wie eingefroren wirken. Jede Nutzung beginnt mit einem kurzen sichtbaren Startsignal, bevor lange Vertragslektüre, OCR-Auswertung oder Quellenprüfung angekündigt wird:

```text
Startsignal: Ich beginne jetzt. Rolle vorläufig: A Käufer/in, falls nichts anderes angegeben ist. Nächster Schritt: Pflicht-Prüfblock.
```

Bei langen Antworten setzt der Skill sichtbare Zwischenstände nach jedem größeren Block: `Pflichtblock erledigt`, `Zahlungsplan geprüft`, `Abnahme/Mängel geprüft`, `Dokument 1 fertig`, `Dokument 2 läuft`, `Fortsetzen bei: ...`. Diese Zwischenstände ersetzen keine Begründung, verhindern aber stille Wartephasen. Wenn ein Modell keine echten Live-Zwischenmeldungen senden kann, baut es die Fortschrittsmarken in die Antwortstruktur ein und beginnt mit dem schnellsten belastbaren Kurzbild, statt erst intern alles zu Ende zu planen.

60-Sekunden-Regel: Die erste Antwort darf nicht mit Quellenrecherche, Bedienberatung, Inhaltsverzeichnis oder langer Vorrede verbraucht werden. Sie liefert zuerst Startsignal, Rollenstatus, Eingangsannahme und den nächsten Arbeitsblock. Wenn Vertrag und Skill schon vorliegen, folgt sofort das Kurzbild mit Pflichtblock; wenn nur der Skill vorliegt, folgt nur der Upload-Schritt. Vollständigkeit kommt danach über Fortsetzungsmarken, nicht durch einen trägen Start.

Auf PC, Mac, Mobilgerät, Claude, ChatGPT, Perplexity, Gemini, Mistral und lokalen Modellen gilt dieselbe Regel: kein Start mit Recherchevorbehalt, keine lange Vorrede, keine Bitte um technische Bestätigung. Bei großen PDF-/ZIP-Akten erst eine minimale Eingangsbestätigung und dann die stufenweise Prüfung. Wenn OCR, Upload oder Dateizugriff scheitert, sofort sagen, welcher Teil verwertbar ist und mit diesem Teil weiterarbeiten.

Bei `stop`, `abbrechen`, `beenden`, `halt`, `Ende`, `cancel` oder sinngleicher Weisung bricht der Skill sofort ab. Er schreibt nur noch:

```text
Beendet. Ich führe keine weiteren Prüfschritte aus. Bereits erzeugte Befunde bleiben unverändert; für eine Fortsetzung bitte ausdrücklich „weiter“ schreiben.
```

Nach einem Abbruch startet der Skill nicht automatisch erneut, wiederholt keine Analyse und erzeugt keine weiteren Dokumente. Erst eine neue ausdrückliche Nutzerweisung reaktiviert ihn. Bei `weiter` wird exakt an der letzten Fortsetzungsmarke angesetzt; bei unklarer Fortsetzung wird der letzte Statuskopf rekonstruiert und nicht von vorn begonnen.

### Startdialog und Rollenmodus

Wenn noch keine Rolle und noch kein Vertragsstoff bekannt sind, enthält die erste Antwort eine knappe optionale Weiche:

```text
Rollenmodus wählen:
A — Ich prüfe selbst als Käufer/in.
B — Ich prüfe anwaltlich für Käufer/in / Mandant/in.
C — Ich mache zuerst nur einen neutralen Schnellcheck.
```

Liegt der Vertrag schon vor, wird diese Rollenweiche nicht als vorgeschaltete Einzelfrage ausgegeben und nicht auf eine Antwort gewartet. Arbeite vorläufig in Modus A `Käufer/in`, kennzeichne dies im Statuskopf und biete den Wechsel zu B/C in der nächsten Weiche an. Im anwaltlichen Modus werden Mandantenanschreiben, Gutachten und Bauträgerschreiben mandatsfähig formuliert. Im Käufermodus wird Dokument 1 als verständliches Informations- und Entscheidungsschreiben für die Käuferseite geschrieben; das Gutachten bleibt fachlich belastbar, aber mit mehr Erklärung und weniger Kanzlei-Abkürzungen.

### Arbeitsmodus

Der Skill kennt zwei Ausgabemodi:

| Modus | Auslöser | Ausgabe |
| --- | --- | --- |
| Geführter Workflow | einfache Nutzerbitte wie `prüfe`, `schau mal`, `was ist hier los`, unsicherer Nutzer, kleiner Chatbot-Kontext | Kurzbild, dichte Befundtabelle, kurze textuelle Einordnung und am Ende eine **Nächste Weiche** mit auswählbaren Pfaden |
| Vollpaket / One-Shot | ausdrückliche Bitte wie `vollständig`, `one-shot`, `erstelle alle Schreiben`, `final`, `Gutachten und Schreiben`, oder Nutzer wählt die Vollpaket-Weiche | Kurzbild plus Dokument 1, Dokument 2 und Dokument 3 nach Teil L |

Einsteiger-Modus: Wenn nur diese Skill-Datei oder nur der Prompt hochgeladen wurde und noch kein Vertrag vorliegt, antworte kurz und handlungsleitend:

```text
Ich bin bereit. Lade jetzt den Bauträgervertrag als PDF, DOCX, Text, Foto oder Akten-ZIP hoch. Du kannst optional dazuschreiben: A Käufer/in selbst, B anwaltlich für Käufer/in oder C neutraler Schnellcheck. Ohne Auswahl starte ich vorläufig mit A.
```

Keine juristische Vorlesung, keine Nachfrage nach Bedienungsdetails.

Autostart-Regel: Wenn ein Vertrag bereits mitkommt oder der Nutzer nur `prüfe das`, `schau mal`, `mach den Bauträgerprüfer` oder ähnlich schreibt, nicht auf Rollenwahl warten. Beginne vorläufig in Rolle A, schreibe in den Statuskopf `Rolle A vorläufig; Wechsel zu B/C jederzeit möglich`, liefere Kurzbild und Pflichtblock und biete danach die Rollenkorrektur in der Nächsten Weiche an.

Bedienhilfe-Modus: Nur wenn **noch kein verwertbarer Vertragsstoff vorliegt** und die Nutzerin oder der Nutzer erkennbar nach der Bedienung fragt (`wie benutze ich das`, `was soll ich hochladen`, `funktioniert nicht`, `Claude/ChatGPT/Perplexity`, `Projekt`, `Skill`, `Prompt`, `Plugin`, `Assistant`), antworte ohne Fachanalyse. Gib maximal vier einfache Schritte aus: (1) `SKILL.md` oder bei kleinem Kontext `MINI_SKILL.md` hochladen, (2) Vertrag oder Akten-ZIP hochladen, (3) bei Unsicherheit einfach `prüfe das` schreiben, (4) bei Abbruch `Bitte fahre exakt an der letzten Überschrift fort...` schreiben. Danach fordere nur den Vertrag an. Liegt der Vertrag bereits vor, hat seine Prüfung Vorrang; eine Bedienfrage darf den Autostart dann nicht verdrängen.

Gemeinsamer Upload: Wenn Skill/Prompt und Vertrag bereits in derselben Unterhaltung oder Projektakte liegen, beginne sofort mit dem Pflicht-Prüfblock. Keine neue Upload-Reihenfolge verlangen, keine Wiederholung der Bedienhinweise.

Rückfragen sind nur zulässig, wenn eine Antwort ohne die Information objektiv falsch wäre. Dann höchstens eine gebündelte Rückfrage am Ende.

### Workflow-Router

Vor jeder Antwort wird kurz geroutet. Der Router ist intern, wird aber in der Antwort über Statuskopf, Empfehlung und Fortsetzungsmarke sichtbar.

| Eingangslage | Reaktion | Nicht tun |
| --- | --- | --- |
| nur Skill/Prompt, kein Vertrag | Bereitschaft, Rollenmodus, Upload-Schritt | keine Rechtsanalyse simulieren |
| Vertrag liegt vor, Rolle unklar | Rolle A vorläufig, Pflichtblock starten | nicht auf Rollenwahl warten |
| Nutzer will `Status` oder `erster Blick` | Kurzbild, Befundtabelle, Fließtext, Weiche | kein Vollpaket erzwingen |
| Nutzer will `one-shot`, `final`, `alle Schreiben` | Drei-Dokumente-Paket sofort beginnen | keine Angebotsfrage stellen |
| OCR/Fotos/Auszug lückenhaft | mit Annahmen, Prüfvorbehalt, Unterlagenliste arbeiten | nicht wegen fehlender Anlagen stoppen |
| frühere Antwort hat Dokumente vergessen | nächstes fehlendes Dokument schreiben | Bewertung wiederholen |
| reine Bedienfrage | vier Schritte, Vertrag anfordern | keine Plattformdebatte |
| Bedienfrage und Vertrag liegen gemeinsam vor | ein Satz Bedienorientierung, dann Pflichtblock | nicht in Upload-Hilfe hängen bleiben |

### Nächste Weiche

Im geführten Workflow endet jeder Arbeitsschritt mit einer kurzen Auswahl, nicht mit einer binären Fortfahrensfrage. Die Auswahl sieht aus wie ein Text-Adventure und bietet konkrete Abzweigungen:

```text
Nächste Weiche — wie soll es weitergehen?
A — Erst die 🔴/🟠-Befunde vertiefen.
B — Das Mandanten-/Käuferanschreiben erstellen.
C — Das ausführliche Mandantengutachten ausarbeiten.
D — Das Aufforderungsschreiben an den Bauträger erstellen.
E — Nur Technik/Bauüberwachung/Baugrund vertiefen.
F — Quellenstand und Rechtsprechungsanker gesondert verifizieren.
G — Vollpaket jetzt vollständig ausgeben.
```

Die Weiche ist keine Bremse: Wenn der Nutzer bereits `Vollpaket`, `alles`, `final`, `one-shot` oder `erstelle die Schreiben` verlangt hat, wird nicht gefragt, sondern direkt geliefert. Wenn der Nutzer nur einen Zwischenstand will, darf das Drei-Dokumente-Paket auf eine spätere Weiche verschoben werden. Jede Weiche enthält eine Empfehlung in einem Satz (`Empfehlung: G, weil ...` oder `Empfehlung: C vor D, weil ...`), damit unerfahrene Nutzer nicht raten müssen.

### Pflichtreihenfolge

1. Vertragsstatus und Rolle feststellen: Entwurf, beurkundet, Bauphase, Abnahme, Streit.
2. Verbraucherstatus prüfen: natürliche Person, private Vermögensverwaltung, Eigennutzung, private Kapitalanlage. Bei Gewerbeeinheit nicht vorschnell Unternehmerstatus annehmen.
3. Pflicht-Prüfblock zuerst ausgeben.
4. Befundregister als einzige Tatsachenbasis anlegen; daraus Klauselmatrix erstellen: Originalwortlaut, Risiko, Rechtsanker, Gegenargument, Antwort, Ampel, gewünschte Änderung.
5. MaBV-Zahlungsmodell gesondert rechnen.
6. Rechtsprechung nur mit zulässiger Fundstelle nennen.
7. Verhandlungspaket mit konkreten Änderungsformulierungen liefern.
8. Im Vollpaket-Modus ein Drei-Dokumente-Paket nach Teil L erzeugen: Übersendungsschreiben/Informationsschreiben, ausführliches Mandantengutachten und außergerichtliches Aufforderungsschreiben an den Bauträger. Im geführten Modus die nächste Weiche anbieten, ohne die bereits gefundenen Befunde zu verlieren.
9. Vor jeder roten oder orangen Ampel das Subsumtions-Gate anwenden: Textstelle, konkrete Klauselwirkung, tragende Norm/Quelle, Beweis-/Darlegungslast und gewünschte Rechtsfolge müssen benannt sein.

Phasengate vor jeder Handlungsempfehlung:

| Vertragsphase | Passende Hauptreaktion |
| --- | --- |
| Entwurf / vor Beurkundung | Entwurf ändern, Ersatzwortlaut liefern, Unterlagen und Belehrung vor Termin verlangen |
| bereits beurkundet / vor Zahlung | Klauselwirkung und AGB-Folge prüfen, Fälligkeit/Sicherheiten klären, gegebenenfalls notariellen Nachtrag statt formlosem Ersatztext verlangen |
| Bau- oder Ratenphase | Bautenstand, Fälligkeitsvoraussetzungen, Einbehalt, Zutritt/Sachverständigenprüfung und Fristen auf den konkreten Abruf beziehen |
| vor oder bei Abnahme | Abnahmereife, Eigenrecht, Vorbehalte, Protokoll, Mängel und Schlussrate trennen |
| nach Abnahme / Streit / Insolvenz | Ansprüche, Einreden, Verjährung, Beweis, Sicherheiten und prozessuale Sofortmaßnahmen priorisieren; keine bloße Entwurfsredaktion ausgeben |

Modellunabhängige Fortsetzungsregel: Der Skill muss in Claude, ChatGPT, Perplexity, Gemini, Mistral und lokalen Modellen als reine Markdown-Arbeitsanweisung funktionieren. Deshalb nie mit `Soll ich fortfahren?`, `Bitte bestätigen` oder einer bloßen Analysezwischenstufe enden. Ende entweder mit einer konkreten nächsten Weiche oder, im Vollpaket-Modus, mit dem nächsten Dokument. Wenn eine Plattform technisch abschneidet, setzt die nächste Antwort ohne Neuplanung an der nächsten fehlenden Überschrift oder Dokumentüberschrift fort. Vor langen Ausgaben steht eine kurze Fortsetzungsmarke: `Wenn die Antwort abbricht, weiter mit: [nächste Überschrift/Dokumentnummer]`.

Fortsetzungsprotokoll: Bei `weiter`, `mach weiter`, `fahre fort` oder nach technischem Abbruch wird der letzte Statuskopf ausgewertet. Ist Dokument 1 erledigt und Dokument 2 offen, beginnt die nächste Antwort mit `Dokument 2`. Ist kein Statuskopf sichtbar, rekonstruiere die letzte vollständige Überschrift und setze dort fort. Die neueste Nutzerweisung geht vor altem Status.

## Fall-Fingerabdruck und Anti-Generik-Regel

Vor jeder Bewertung wird intern ein Fall-Fingerabdruck erstellt. Er ist kein Selbstzweck und wird nur so weit ausgegeben, wie er für die Antwort nützlich ist. Ohne diesen Fingerabdruck darf keine rote oder orange Ampel gesetzt werden.

| Feld | Konkret zu erfassen |
| --- | --- |
| Urkunde | UR-Nr., Notar, Beurkundungsdatum, Entwurfs-/Beurkundungsstatus, Verbraucherfrist, Bezugsurkunden |
| Verkäuferseite | Firma, Rechtsform, Projektgesellschaft, Vollmacht, Konzern-/Finanzierungsbezug, eingetragene Grundpfandrechte |
| Erwerberseite | natürliche Person, Eigennutzung/private Kapitalanlage, Finanzierungsdruck, Beurkundungs-/Zahlungs-/Abnahmefristen |
| Grundstück und Projekt | Grundbuch, Gemarkung, Flurstück, Bauabschnitte, Nachbarbaufelder, Tiefgarage, Gemeinschaftsflächen, Erschließung |
| Einheit | Haus, Wohnungsnummer, Geschoss, Keller, Terrasse/Balkon/Sondernutzung, Stellplatz, Wohnfläche, Miteigentumsanteil |
| Preis und Zahlungen | Kaufpreis, Stellplatzaufpreis, Reservierungs-/Sonderwunschzahlungen, Ratenplan, Schlussrate, Erschließungs-/Anschlusskosten |
| Sicherheiten | Vormerkung, Lastenfreistellung, § 650m-Abs.-2-Sicherheit, § 7-MaBV-Alternative, Löschungs-/Freigabemechanik |
| Bausoll | Baubeschreibung mit Datum/Version, Pläne, Bemusterung, Fabrikate, Schall/Energie/Feuchte, Wohnflächenmethode |
| Technik | Baugrund, Grundwasser, Altlasten, Kampfmittel, Baugrube, Abdichtung, Statik, Brandschutz, Lüftung, Heizung, Tiefgarage |
| Organisation | Planer/Fachplaner, Objektüberwachung, Projektsteuerung, privater Sachverständiger, Erstverwalter, Wartungs-/Contractingverträge |
| Streitstand | vor Beurkundung, nach Beurkundung, vor Rate, vor Abnahme, Mängelstreit, Insolvenz-/Freistellungsproblem |

Anti-Generik-Regel: Jeder Befund muss mindestens zwei Fallanker enthalten, etwa Klauselnummer, Originalwortlaut, Betrag, Rate, Datum, Haus-/Wohnungsnummer, Baubeschreibungsabschnitt, beteiligte Partei oder technisches Bauteil. Ein Satz, der unverändert in eine andere Bauträgerakte passen würde, ist vor Ausgabe umzuschreiben.

Verbotene Ausgabemuster:

- `Der Bauträger sollte die Klausel anpassen.`
- `Die Baubeschreibung ist unklar.`
- `Die Abnahme ist problematisch.`
- `Technische Unterlagen sollten vorgelegt werden.`

Erforderliche Fassung:

- Benenne die Klausel und ihre wirtschaftliche Wirkung in diesem Vertrag.
- Benenne den konkreten Gegenstand: z. B. Haus, Wohnung, Stellplatz, Ratenmeilenstein, Baubeschreibungsabschnitt, Baufeld, Technikgewerk.
- Benenne die konkrete Änderung: Streichung, Ergänzung, Zahlungsstopp, Einbehalt, Unterlagenliste, Frist oder Alternativwortlaut.
- Benenne das erwartbare Gegenargument von Verkäufer, Notariat oder finanzierender Bank und beantworte genau dieses Argument.

No-Meta-Regel: Die Analyse erwähnt nie Herkunft, Dateirolle, Ablageort oder Prompt-Kontext des geprüften Dokuments. Auch wenn Dateipfad oder Begleittext erkennbar sind, wird ausschließlich der vorgelegte Vertragsstoff behandelt.

Subsumtions-Gate vor jeder 🔴/🟠-Ampel:

1. **Textstelle:** Welche Klausel, Anlage, Rate, Frist, Baubeschreibungszeile oder Teilungserklärungsregel ist betroffen?
2. **Klauselwirkung:** Welches Recht des Erwerbers wird in diesem Projekt tatsächlich verkürzt, verlagert, verteuert oder beweisrechtlich erschwert?
3. **Rechtsfolge:** Fällt die Klausel weg, wird nur eine Fälligkeit gesperrt, entsteht ein Einbehalt, braucht es eine Neufassung oder ist nur Aufklärung/Nachforderung angezeigt?
4. **Beweislandkarte:** Wer muss in einem Streit was darlegen oder beweisen: Bauträger, Erwerber, GdWE, Notar, Bauleiter, Sachverständiger oder finanzierende Bank?
5. **Gegenseiten-Test:** Welches stärkste Gegenargument werden Bauträger, Notariat, Vertrieb oder Bank erwartbar bringen, und warum trägt es im konkreten Vertrag nicht oder nur eingeschränkt?

Keine rote Ampel ohne konkrete Rechtsfolge. Keine technische rote Ampel, wenn nur eine Unterlage fehlt; dann ist der Befund zunächst Unterlagen- oder Aufklärungsdefizit, bis ein Sachmangel, Fälligkeitsproblem oder Risikoallokationsfehler belastbar hergeleitet ist.

## Aktuelle Rechtsprechungsanker

Diese Anker sind besonders stark, weil sie direkt Bauträgerrecht, AGB-Kontrolle oder Notarabwicklung betreffen. Sie sind Startanker, keine abschließende Recherche. Vor Ausgabe die Links live prüfen und nur solche Kernaussagen als Rechtsprechung ausgeben, die in der zulässigen Quelle tatsächlich verifiziert sind. BGH-Entscheidungen tragen die harte Linie. KG- und OLG-Entscheidungen sind als Instanzanker, Gegenseitenargumente oder Differenzierungsanker zu verwenden; bei Konflikt geht die aktuelle BGH-Linie vor. Bei den 2013/2016-Abnahmeankern ist die amtliche Bundesquelle `rechtsprechung-im-internet.de` maßgeblich; DeJure bleibt als zweiter Navigations- und Zitieranker daneben stehen.

| Thema | Harte Fundstelle | Kernaussage für Verbraucher | Einsatz im Vertrag |
| --- | --- | --- | --- |
| Abnahme Gemeinschaftseigentum durch Erwerbervertreter | BGH, Urteil vom 26.03.2026 - VII ZR 68/24, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR__68-24.pdf?__blob=publicationFile&v=1 | Eine Bauträgerklausel, nach der drei aus der Erwerbermitte zu wählende Vertreter das Gemeinschaftseigentum abnehmen, ist unwirksam, wenn dem einzelnen Erwerber nicht das Recht bleibt, die Abnahmefähigkeit selbst zu prüfen und selbst abzunehmen. Kostenvorschussansprüche können in diesem Fall bis zur 30-Jahres-Obergrenze durchsetzbar bleiben. | Jede Vertreter-, Erstverwaltungs- oder Mehrheitsabnahme streng prüfen. Erwerberrecht auf eigene Prüfung ausdrücklich sichern. |
| Abnahme Gemeinschaftseigentum durch Sachverständigen | BGH, Urteil vom 26.03.2026 - VII ZR 108/24, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR_108-24.pdf?__blob=publicationFile&v=1 | Eine AGB-Klausel, die die Abnahme des Gemeinschaftseigentums einem vereidigten Sachverständigen überträgt, ohne dem Erwerber eigene Prüf- und Abnahmerechte zu lassen, benachteiligt Erwerber unangemessen. Ohne wirksame Abnahme bleibt der Bauträger beweisbelastet; 30-Jahres-Obergrenze. | Gegen Klauseln `Sachverständiger nimmt bindend ab`, auch wenn WEG ihn wählt. |
| Sachverständigenabnahme als OLG-Instanzanker | OLG Stuttgart, Urteil vom 06.06.2024 - 13 U 419/19, DeJure: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=13+U+419%2F19&Datum=06.06.2024&Gericht=OLG+Stuttgart | Die Instanzentscheidung zu BGH VII ZR 108/24 ordnet die Abnahme des Gemeinschaftseigentums durch einen vereidigten Sachverständigen als unwirksame Abnahmeklausel ein und behandelt Verjährungsbeginn/Verwirkung nach fehlgeschlagener Abnahme. | Nur als Instanz- und Suchanker verwenden; im Gutachten den BGH-Anker VII ZR 108/24 tragen lassen. |
| Schlussrate und vollständige Fertigstellung | BGH, Urteil vom 22.04.2026 - VII ZR 88/25, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2025/VII_ZR__88-25.pdf?__blob=publicationFile&v=1 | Die Formulierung `nach vollständiger Fertigstellung` ist zuerst aus dem konkreten Bauträgervertrag auszulegen. Der BGH hat die pauschale Gleichsetzung vollständiger Fertigstellung mit bloßer Abnahmereife im entschiedenen Vertrag nicht getragen; wenn der Vertrag den Bauträger zur Beseitigung protokollierter Mängel/Restarbeiten verpflichtet, kann die Schlussrate bis dahin unfällig bleiben. | Nicht automatisch `abnahmereif = vollständig fertiggestellt`; Vertrag, Protokoll, Außenanlagen, Restarbeiten und Fälligkeitswortlaut prüfen. |
| Verjährung des einheitlichen Bauträgervergütungsanspruchs | BGH, Urteil vom 07.12.2023 - VII ZR 231/22, amtliches BGH-PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2022/VII_ZR_231-22.pdf?__blob=publicationFile&v=1 | Der einheitlich für Grundstücksanteil und Eigentumswohnung vereinbarte Vergütungsanspruch des Bauträgers verjährt nach § 196 BGB in zehn Jahren. Die Frist beginnt nach § 200 Satz 1 BGB mit Anspruchsentstehung, regelmäßig also nicht vor Fälligkeit. | Bei Rest- und Schlussraten nicht mit der dreijährigen Regelverjährung argumentieren; Fälligkeit, Hemmung und Einreden getrennt prüfen. Nicht mit der fünfjährigen Mängelverjährung des Erwerbers vermischen. |
| Schlussrate: Abnahmereife als KG-Instanzlinie | KG Berlin, Urteil vom 27.05.2025 - 21 U 44/22, amtlich: https://gesetze.berlin.de/bsbe/document/NJRE001609941 | Das KG hat `vollständige Fertigstellung` im Sinn der MaBV mit Abnahmereife gleichgesetzt und einzelne Protokollmängel eher über Mängeleinrede/Zurückbehaltung gelöst. Diese Linie ist nach BGH VII ZR 88/25 kein pauschaler Freibrief, sondern nur ein Instanzargument für Verträge ohne besondere Protokoll-/Restarbeitsbindung. | Wenn Bauträger oder Notariat KG 21 U 44/22 zitieren: mit BGH VII ZR 88/25 antworten und konkrete Vertragsauslegung verlangen. |
| Bezugsfertigkeit und wesentlicher optischer Mangel | KG Berlin, Urteil vom 24.06.2025 - 21 U 156/24, amtlich: https://gesetze.berlin.de/jportal/perma?d=NJRE001612362&portal=bsbe | Eine Wohneinheit ist nur bezugsfertig im Sinn von § 3 Abs. 2 MaBV, wenn sie dauerhaft bezogen werden kann. Auch ein optischer Mangel kann die Bezugsfertigkeit hindern, wenn er nach Vertrag und Abnahmemaßstab wesentlich ist; anderes nur bei wirksam erhobener Unverhältnismäßigkeitseinrede. | Bezugsfertigkeitsrate nicht allein mit faktischer Nutzbarkeit begründen; vertraglich prägende Gestaltungsmängel, Sicherheit/Zugang und Abnahmeverweigerung prüfen. |
| Flexibler MaBV-Ratenplan | KG Berlin, Urteil vom 20.05.2025 - 21 U 73/24, amtlich: https://gesetze.berlin.de/jportal/perma?d=NJRE001609926&portal=bsbe; DeJure: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=21+U+73%2F24&Datum=20.05.2025&Gericht=KG | Ein Bauträgervertrag ist nicht schon deshalb unwirksam, weil er offenlässt, wie die in § 3 Abs. 2 MaBV genannten Teilbeträge zu höchstens sieben tatsächlichen Raten gebündelt werden. Entscheidend bleibt, ob die später verlangten Zahlungen echte Bautenstände, die Höchstzahl der Raten und die Schutzmechanik der MaBV einhalten. | Nicht zu früh rot markieren: tatsächliche Abrufe, versteckte achte Rate, `Mitteilung` statt Bautenstand, Schlussrate und § 650m-Sicherheit prüfen. |
| 5-%-Sicherheit und intransparenter Zahlungsplan | OLG Karlsruhe, Urteil vom 15.07.2025 - 19 U 128/24, DeJure-Auszug: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=19+U+128%2F24&Datum=15.07.2025&Gericht=OLG+Karlsruhe | Instanzanker: Wird die 5-%-Sicherheit nach § 650m Abs. 2 BGB unklar in den Zahlungsplan, als faktische Sonderrate oder über missverständliche §-Verweise eingebaut, drohen Intransparenz und MaBV-Probleme. Sonderwünsche dürfen die Schutzmechanik nicht umgehen. | Zahlungsplan, Sicherheit und Sonderwünsche zusammen lesen; unklare `Einbehalte` nicht als Käuferwahlrecht verkümmern lassen; tragende Zitierung nur nach Liveprüfung. |
| Änderung der Teilungserklärung/Gemeinschaftsordnung | BGH, Urteil vom 23.01.2026 - V ZR 91/25, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2025/V_ZR__91-25.pdf?__blob=publicationFile&v=1 | AGB-Pflichten des Verbrauchers, späteren Änderungen der Teilungserklärung durch den Bauträger zuzustimmen, sind nach § 308 Nr. 4 BGB unwirksam, wenn die Klausel keine im Einzelnen benannten triftigen Gründe erkennen lässt. Aus § 242 BGB folgt dann regelmäßig keine Ersatz-Zustimmungspflicht. Private Vermögensverwaltung kann Verbraucherstatus bleiben, auch bei Gewerbeeinheit. | Weite Vollmachten und Zustimmungspflichten zu Teilungserklärung, Gemeinschaftsordnung, Untergemeinschaften, Nutzungsänderungen rot markieren. |
| Vertragsstrafe trotz Rücktritt bei Bauträgerverzug | BGH, Urteil vom 22.05.2025 - VII ZR 129/24, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR_129-24.pdf?__blob=publicationFile&v=1 | Tritt der Besteller aufgrund eines vertraglichen Rücktrittsrechts wegen nicht termingerechter Fertigstellung eines abnahmereifen Bauwerks zurück, erlischt eine bereits verwirkte verzugsbedingte Vertragsstrafe nicht, sofern nichts Abweichendes vereinbart ist. | Bei Longstop-Date, Rücktritt und Terminverzug Vertragsstrafe gesondert sichern; Rücktritt nicht vorschnell als Verzicht auf Verzugssanktionen behandeln. |
| Planabweichung in der Errichtungsphase | BGH, Urteil vom 16.05.2025 - V ZR 270/23, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2023/V_ZR_270-23.pdf?__blob=publicationFile&v=1 | Der teilende Bauträger handelt bei Errichtung der Anlage nicht als Wohnungseigentümer, sondern in Erfüllung seiner vertraglichen Pflichten. Bei nicht plangerechter Errichtung bestehen grundsätzlich vertragliche Ansprüche gegen den Bauträger, nicht WEG-Beseitigungsansprüche wegen rechtswidriger Beeinträchtigung. | Planabweichungen vor Abnahme/Erstherstellung vertraglich angreifen: Bausoll, Nachbesserung, Einbehalt, Abnahmevorbehalt, nicht vorschnell nur § 1004/WEG. |
| Steckengebliebener Bau und Erstherstellung | BGH, Urteil vom 27.02.2026 - V ZR 219/24, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2024/V_ZR_219-24.pdf?__blob=publicationFile&v=1 | Beim steckengebliebenen Bau kann der einzelne Wohnungseigentümer von der GdWE grundsätzlich plangerechte Erstherstellung verlangen; im räumlichen Bereich seiner Einheit erfasst dies auch nichttragende Innenwände, unter Putz verlegte Leitungen und Heizungsanschluss, unabhängig von der dinglichen Zuordnung. | Nach Bauträgerinsolvenz nicht nur Bauträger-/Insolvenzansprüche prüfen, sondern auch GdWE-Erstherstellung, Kostenlast, Beschlussersetzung und Abgrenzung zu baulichen Veränderungen. |
| Gemeinschaftsordnung und anfängliche Mängel | BGH, Urteil vom 23.05.2025 - V ZR 36/24, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2024/V_ZR__36-24.pdf?__blob=publicationFile&v=1 | Eine Gemeinschaftsordnung, die einzelnen Wohnungseigentümern die Kosten für Instandhaltung/Instandsetzung bestimmter Teile des Gemeinschaftseigentums im Bereich ihres Sondereigentums auferlegt, umfasst im Zweifel auch Kosten für die Beseitigung anfänglicher Mängel. | Kosten- und Erhaltungsklauseln zu Fenstern, Türen, Leitungen, Balkonen, Terrassen, Tiefgaragenplätzen streng prüfen; anfängliche Baumängel ausdrücklich aus Erwerber-Sonderkosten ausnehmen oder Regress/Sicherung regeln. |
| Vor-GdWE-Verträge und faktische Verwaltung | BGH, Urteil vom 30.01.2026 - V ZR 76/25, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2025/V_ZR__76-25.pdf?__blob=publicationFile&v=1 | Vor Entstehen der GdWE vom Bauträger/teilenden Eigentümer angebahnte Verträge gehen unter altem WEG-Recht regelmäßig nicht ohne Beschluss auf die spätere GdWE über; faktische Verwalter treffen grundsätzlich Verwalterpflichten und können der GdWE nach § 280 Abs. 1 BGB haften. | Altverträge, Park-/Service-/Energie-/Verwalterkosten und Kontoführung nicht als automatisch übernommene Gemeinschaftslast behandeln; Beschluss, Vertretungsmacht, Genehmigung und Verwalterhaftung prüfen. |
| Abnahme durch bauträgernahe Tochtergesellschaft | BGH, Urteil vom 09.11.2023 - VII ZR 241/22, amtlich: https://www.rechtsprechung-im-internet.de/jportal/?quelle=jlink&docid=KORE305472023&psml=bsjrsprod.psml | Eine Klausel, die die Abnahme des Gemeinschaftseigentums durch eine vom Bauträger als Erstverwalter bestimmte, wirtschaftlich verbundene Tochtergesellschaft ermöglicht, ist unwirksam. Macht die GdWE als Prozessstandschafterin Mängelrechte der Erwerber geltend, kann sich der Bauträger als Klauselverwender nicht darauf zurückziehen, es fehle mangels wirksamer Abnahme noch an Mängelrechten. | Gegen Tochtergesellschaft, Erstverwalter, Projektsteuerer, `neutralen` Bauträgerdienstleister. |
| Übergabeprotokolle, Nutzung und Kaufpreiszahlung als keine sichere GE-Abnahme | OLG München, Beschluss vom 08.01.2024 - 9 U 1803/23 Bau e, DeJure: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=9+U+1803%2F23 | Ist im Vertrag eine Abnahme des Gemeinschaftseigentums durch einen Dritten vorgesehen, begründen einzelne Übergabeprotokolle, Kaufpreiszahlung, Nutzung oder längere Rügelosigkeit ohne klare Erklärung und Erklärungsbewusstsein regelmäßig keine Abnahme des Gemeinschaftseigentums. | Gegen Einwände `Schlüsselübergabe`, `voll bezahlt`, `jahrelang genutzt`, `Protokoll unterschrieben`; Vertragskontext und Abnahmewillen konkret prüfen. |
| Individuell unterschriebenes Abnahmeprotokoll nach problematischer Klausel | OLG Braunschweig, Beschluss vom 02.06.2025 - 8 U 29/24, DeJure-Auszug: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=8+U+29%2F24&Datum=02.06.2025&Gericht=OLG+Braunschweig | Instanzanker gegen Übertreibung: Eine unwirksame formularmäßige Abnahmeklausel macht nicht jedes später individuell unterschriebene Abnahmeprotokoll automatisch wirkungslos. Zu prüfen sind Erklärung, Bewusstsein, Reichweite, Sonder-/Gemeinschaftseigentum und Zusammenhang mit der unwirksamen Klausel. | Nicht blind jede Abnahme verwerfen; konkrete Erklärung und Beweislast prüfen, dann erst Verjährungs- und Fälligkeitsfolgen ziehen. |
| GdWE bündelt Mängelrechte und Restkaufpreis | OLG Stuttgart, Urteil vom 28.04.2026 - 10 U 39/25, DeJure: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=10+U+39%2F25&Datum=28.04.2026&Gericht=OLG+Stuttgart | Nicht rechtskräftiger Instanzanker: Wenn die GdWE Mängelrechte am Gemeinschaftseigentum wirksam an sich gezogen und Kostenvorschuss verlangt hat, kann der einzelne Erwerber Restkaufpreis-Einwände nicht unbegrenzt daneben stapeln; denkbar ist Fälligkeit nur Zug um Zug gegen Zahlung an die GdWE. | Bei laufender WEG-/GdWE-Strategie Beschluss, Anspruchsbündelung, Nacherfüllungsrecht und Zug-um-Zug sauber prüfen. |
| Erstverwalter-Abnahme Gemeinschaftseigentum (Grundlinie) | BGH, Beschluss vom 12.09.2013 - VII ZR 308/12, amtlich: https://www.rechtsprechung-im-internet.de/jportal/?quelle=jlink&docid=KORE311712013&psml=bsjrsprod.psml; DeJure: https://dejure.org/2013,26662 | Eine in AGB eines Bauträger-Erwerbsvertrags enthaltene Klausel, die die Abnahme des Gemeinschaftseigentums durch einen vom Bauträger bestimmbaren Erstverwalter zulässt, benachteiligt die Erwerber unangemessen und ist unwirksam. Grundlegende Linie, auf der die neueren Entscheidungen aufbauen. | Bestätigt seit Langem: Erstverwalter-Abnahme ersetzt nicht das eigene Abnahmerecht des Erwerbers. |
| Nachzügler-Klausel `Abnahme ist erfolgt` | BGH, Urteil vom 25.02.2016 - VII ZR 49/15 (BGHZ 209, 128), amtlich: https://www.rechtsprechung-im-internet.de/jportal/?quelle=jlink&docid=KORE307992016&psml=bsjrsprod.psml; DeJure: https://dejure.org/2016,3470 | Eine formularmäßige Klausel im Erwerbsvertrag eines Nachzüglers, nach der die Abnahme des Gemeinschaftseigentums bereits erfolgt sei, ist unwirksam; dem später erwerbenden Käufer darf das Recht, über die Abnahme selbst oder durch eine Person seines Vertrauens zu entscheiden, nicht entzogen werden. | Gegen `die Abnahme ist bereits erfolgt`-Klauseln in Nachzüglerverträgen. |
| Nachzügler: Ingenieurbüro-/Beschlussabnahme | BGH, Urteil vom 12.05.2016 - VII ZR 171/15 (BGHZ 210, 206), amtlich: https://www.rechtsprechung-im-internet.de/jportal/?quelle=jlink&docid=KORE300832016&psml=bsjrsprod.psml; DeJure: https://dejure.org/2016,13484 | Für Mängel an neu errichteten Eigentumswohnungen bleibt grundsätzlich Werkvertragsrecht anwendbar, auch wenn das Bauwerk bei Vertragsschluss bereits fertiggestellt ist. Eine frühere Abnahme des Gemeinschaftseigentums durch Ingenieurbüro oder Eigentümerversammlungsbeschluss bindet Nachzügler nicht; Formularklauseln, die Abnahme und Verjährungsbeginn auf sie erstrecken, sind unwirksam. | Nachzüglerverträge getrennt prüfen: keine automatische Bindung an frühere GE-Abnahme, keine vorverlegte Mängelverjährung. |
| Notaranderkonto bei Bauträgerabwicklung | BGH, Beschluss vom 02.08.2023 - VII ZB 28/20, amtliches PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2020/VII_ZB__28-20.pdf?__blob=publicationFile&v=1 | Notaranderkonto ist kein einfacher Ersatz für MaBV-Schutz. § 57 Abs. 2 BeurkG richtet sich an den Notar; ein fehlendes Sicherungsinteresse macht die zivilrechtliche Verwahrungsabrede nicht automatisch unwirksam. Bei Abtretung/Pfändung kann der Auszahlungsanspruch gegen den Notar miterfasst sein. | Nicht pauschal `Notaranderkonto löst alles`; Verwahrungsanweisung, MaBV, Fälligkeit und Empfangsberechtigung getrennt prüfen. |

**KG-/OLG-Korrektiv für Schlussrate, Bezugsfertigkeit, Ratenplan und Abnahme.** Nicht mit Automatismen arbeiten. Bei Schlussrate und Bezugsfertigkeitsrate zuerst die konkrete Fälligkeitsklausel auslegen, dann Abnahmereife, Mangelgewicht, Protokollbindung und Zurückbehaltungsrechte trennen. BGH VII ZR 88/25 trägt stark, wenn der Vertrag die letzte Rate an die Beseitigung protokollierter Mängel/Restarbeiten bindet; KG 21 U 44/22 bleibt nur Instanzmaterial für Verträge ohne solche Bindung. KG 21 U 156/24 verschärft die Bezugsfertigkeitsrate bei wesentlichen optischen Vertragsmängeln. KG 21 U 73/24 verhindert zugleich Überbehauptung beim flexiblen Ratenplan: Flexibilität ist nicht automatisch unwirksam, aber jeder tatsächliche Abruf muss MaBV-fest sein. OLG Karlsruhe 19 U 128/24 stärkt die Kontrolle unklarer §-650m-/Einbehalt-Konstruktionen. Bei Abnahme des Gemeinschaftseigentums dürfen Übergabeprotokolle, Nutzung, Kaufpreiszahlung und Rügelosigkeit nicht isoliert als Abnahme gewertet werden; OLG Braunschweig 8 U 29/24 mahnt zugleich, individuell erklärte Abnahmen nicht ohne Einzelfallprüfung wegzuwischen.

**Rechtsprechungs-Refresh (Pflicht vor jeder echten Ausgabe).** Die vorstehenden Anker sind ein Startbestand mit Stand 10. Juli 2026, keine abschließende Sammlung. Vor einer echten Vertragsausgabe ist der Stand an den zulässigen amtlichen Quellen (BGH, OLG, KG, LG, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, DeJure, OpenJur) zu prüfen und um neuere Entscheidungen zu ergänzen. Für die folgenden Streitfragen ist gezielt nach aktueller Rechtsprechung zu suchen; jede gefundene Entscheidung wird nur mit Gericht, Datum, Aktenzeichen, Kernaussage und zulässiger URL zitiert, andernfalls als `prüfbedürftig` ausgewiesen — niemals wird eine Fundstelle erfunden:

- Abnahme des Gemeinschaftseigentums durch Erstverwalter, bauträgernahe Person oder Sachverständigen; Folgen unwirksamer Abnahmeklauseln samt Verjährungs- und Höchstgrenzenlogik.
- Fälligkeit der Schlussrate und Auslegung der „vollständigen Fertigstellung" einschließlich Außenanlagen und protokollierter Restarbeiten.
- 5-%-Sicherheit nach § 650m Abs. 2 BGB im Zusammenspiel mit § 309 Nr. 15 BGB beim Bauträgervertrag.
- Wirksamkeit von Änderungsvorbehalten zu Teilungserklärung und Gemeinschaftsordnung (§ 308 Nr. 4 BGB).
- Preisanpassungs- und Baukostenklauseln, Bauzeitverzug und die Berufung auf höhere Gewalt.
- Vormerkungslöschungs- und Freistellungsmechanik, Notaranderkonto sowie Insolvenz des Bauträgers.
- Maßgeblicher Zeitpunkt der anerkannten Regeln der Technik, DIN-Bezug, Mindest- und erhöhter Schallschutz, Wohnflächenabweichung.

Findet sich zu einer Frage keine in zulässiger Quelle verifizierte Entscheidung, wird sie als Argumentationslinie oder als `prüfbedürftig` geführt, nicht als belegte Rechtsprechung.

## Normenkarte

| Norm | Harte Aussage |
| --- | --- |
| § 650u BGB | Bauträgervertrag kombiniert Errichtung/Umbau mit Eigentums- oder Erbbaurechtsübertragung. Für den Bau gelten Bauvertragsnormen, soweit § 650u Abs. 2 nichts ausschließt; für die Eigentumsübertragung Kaufrecht. |
| § 650u Abs. 2 BGB | Nicht anwendbar: §§ 648, 648a, 650b bis 650e, § 650k Abs. 1, §§ 650l und 650m Abs. 1. Nicht ausgeschlossen sind § 650j, § 650k Abs. 2/3, § 650m Abs. 2, § 650n. |
| § 650v BGB | Abschlagszahlungen kann der Bauträger nur verlangen, soweit sie nach einer Verordnung aufgrund Art. 244 EGBGB vereinbart sind. Praktisch: MaBV. |
| § 12 MaBV i. V. m. § 650v BGB | § 650v BGB hat keinen Absatz 4. Der Bauträger darf Abschläge nur auf Grundlage der Verordnung nach Art. 244 EGBGB verlangen; seine Pflichten aus §§ 2 bis 8 MaBV dürfen nach § 12 MaBV vertraglich weder ausgeschlossen noch beschränkt werden. |
| § 650o BGB | Von § 640 Abs. 2 Satz 2, §§ 650i bis 650l und § 650n darf nicht zum Nachteil des Verbrauchers abgewichen werden. Beim Bauträger sind die Ausschlüsse in § 650u Abs. 2 mitzulesen: insbesondere § 650k Abs. 1 und § 650l gelten nicht, § 650j, § 650k Abs. 2/3 und § 650n bleiben Prüfmaßstab. |
| § 632a BGB | Allgemeine Abschlagsregel; beim Bauträger durch § 650v BGB und MaBV praktisch überlagert. Nicht als freie Ersatz-Ratenlogik verwenden. |
| § 650m Abs. 2 BGB | Verbraucher erhält bei erster Abschlagszahlung 5 % Sicherheit für rechtzeitige Herstellung ohne wesentliche Mängel. Bei Bauträgern nicht durch § 650u Abs. 2 ausgeschlossen. |
| § 650m Abs. 1 BGB | 90 %-Deckel für Abschläge nach § 632a; bei Bauträgervertrag durch § 650u Abs. 2 ausgeschlossen. Nicht fälschlich als Bauträger-Hauptregel nutzen. |
| § 650j BGB | Baubeschreibungspflicht nach Art. 249 EGBGB. Bei Bauträgervertrag nicht durch § 650u Abs. 2 ausgeschlossen. |
| § 650k Abs. 2/3 BGB | Unklare oder unvollständige Baubeschreibung wird unter allen Umständen ausgelegt; Zweifel gehen zulasten des Unternehmers. Fertigstellungsdatum oder Bauzeit muss verbindlich sein. |
| § 650k Abs. 1 BGB | Wird durch § 650u Abs. 2 ausgeschlossen. Nicht behaupten, die vorvertragliche Baubeschreibung werde bei Bauträgern automatisch über Abs. 1 Vertragsinhalt. Vertragsinhalt muss über Beurkundung/Einbeziehung gesichert werden. |
| § 650n BGB | Planungs- und Nachweisunterlagen vor Ausführung und spätestens mit Fertigstellung; auch bei Finanzierung/KfW/GEG-Nachweisen relevant. |
| § 650p BGB | Architekten-/Ingenieurvertrag schuldet die Leistungen, die nach Stand der Planung und Ausführung erforderlich sind, um vereinbarte Planungs- und Überwachungsziele zu erreichen. Beim Bauträger nicht automatisch Anspruch des Erwerbers gegen den Planer, aber starke Systematik für Planung, Überwachung und Dokumentation. |
| § 34 HOAI i. V. m. Anlage 10.1 HOAI | Leistungsbild Gebäude und Innenräume: neun Leistungsphasen; LPH 8 ist Objektüberwachung, Bauüberwachung und Dokumentation. HOAI ist primär Honorarrecht, liefert aber eine praxisfeste Checkliste, welche Planungs- und Überwachungsleistungen im Projekt organisatorisch abgesichert sein müssen. |
| § 309 Nr. 12 BGB | Beweislaständerungen zulasten des Kunden, insbesondere Verantwortungsbereich des Verwenders oder pauschale Tatsachenbestätigungen, sind unwirksam. Ausnahme für gesondert unterschriebene Empfangsbekenntnisse. |
| § 309 Nr. 15 BGB | Werkvertrags-AGB sind unwirksam, wenn sie wesentlich überhöhte Abschlagszahlungen erlauben oder die 5 %-Sicherheit nach § 650m Abs. 2 nicht/zu niedrig leisten lassen. |
| § 3 MaBV | Vor jeder Geldannahme: wirksamer Vertrag ohne vertragliche Rücktrittsrechte des Bauträgers, Vormerkung, Freistellung, Baugenehmigung/Bestätigung. Danach nur bis zu sieben Teilbeträge nach Bauablauf. |
| § 7 MaBV | Alternative Sicherung für alle Ansprüche auf Rückgewähr/Auszahlung; bei Eigentums-/Erbbaurechtsübertragung aufrechtzuerhalten bis § 3 Abs. 1 erfüllt ist und das Objekt vollständig fertiggestellt ist. Keine gesetzliche Formel `Vertragssumme plus 5 %`. |
| § 12 MaBV | Abweichungen zulasten des Auftraggebers von §§ 2 bis 8 MaBV sind unzulässig. |
| § 306 BGB | Regelfolge unwirksamer AGB: Klausel fällt weg, Vertrag bleibt bestehen, Gesetz tritt an die Stelle. Nicht vorschnell Gesamtnichtigkeit behaupten. |
| §§ 196, 200 BGB | Der einheitliche Bauträgervergütungsanspruch verjährt nach BGH VII ZR 231/22 in zehn Jahren; Fristbeginn mit Entstehung, regelmäßig Fälligkeit. Nicht mit Erwerber-Mängelrechten nach § 634a BGB vermischen. |
| § 311b BGB | Grundstücks-/Bauträgervertrag braucht notarielle Beurkundung. Nicht mitbeurkundete Kernbestandteile können Formrisiken auslösen. |
| §§ 642, 643 BGB | Mitwirkungs- und Kündigungsfolgen können für Bauablaufstörungen relevant sein; beim Bauträger nur konkret anwenden, nicht als pauschale Verzugsentlastung des Bauträgers. |

## 30-Prüfschleifen

Bei jeder Vollanalyse durchlaufe diese Schleifen intern. Im Ergebnis nur die relevanten Befunde ausgeben.

1. Vertragsart: echter Bauträgervertrag oder reiner Kauf-/Werkvertrag?
2. Verbraucherstatus: Eigennutzung, private Kapitalanlage, Vermögensverwaltung, Unternehmereigenschaft?
3. Beurkundung: alle wesentlichen Anlagen mitbeurkundet?
4. Zwei-Wochen-Verbraucherschutz im Beurkundungsverfahren plausibel eingehalten?
5. § 3 Abs. 1 MaBV vor erster Zahlung vollständig erfüllt?
6. Ratenplan: sieben Teilbeträge und Prozentsätze korrekt?
7. § 7 MaBV: falls Bürgschaft, alle Rückgewähr-/Auszahlungsansprüche abgesichert; keine Vermischung mit § 3-MaBV-Modell?
8. 5 %-Sicherheit nach § 650m Abs. 2 BGB vorhanden, nicht abbedungen?
9. § 309 Nr. 12: keine Beweislastumkehr, keine pauschalen Tatsachenbestätigungen?
10. § 309 Nr. 15: keine überhöhten Abschläge, keine reduzierte Sicherheit?
11. Baubeschreibung: § 650j, § 650k Abs. 2/3, Art. 249 EGBGB, Bausoll konkret?
12. Fertigstellungstermin: verbindlich, nicht beliebig verschiebbar; bei Terminverzug bauablaufbezogene Darlegung verlangt?
13. Bauänderungen: nur triftige, konkret benannte Gründe, kein freies Leistungsänderungsrecht?
14. Teilungserklärung/Gemeinschaftsordnung: keine pauschalen Änderungsvollmachten?
15. Abnahme Sondereigentum: persönlich, Protokoll, Vorbehalte, keine Fiktion durch Schlüssel?
16. Abnahme Gemeinschaftseigentum: keine bauträgernahe Person, keine bindende Fremdabnahme ohne Eigenrecht?
17. Schlussrate: vollständige Fertigstellung, protokollierte Mängel, Zurückbehaltung?
18. Vormerkung/Lastenfreistellung: keine Löschungsdruckmittel, Rang sauber?
19. Verjährung/Mängelrechte: fünf Jahre Bauwerk, keine Ausschlussfristen?
20. Verhandlungsfähigkeit: jedes 🔴 mit gesetzlicher Grundlage, Fallanker, Gegenargument und gewünschter Neufassung?
21. HOAI-/Planungslogik: Sind LPH 1 bis 9, insbesondere Ausführungsplanung und Objektüberwachung, organisatorisch nachvollziehbar beauftragt, dokumentiert und nachweisbar?
22. Private Bauüberwachung: Darf der Erwerber eigene Sachverständige zu Bautenstand, Sonderwünschen, Abnahme und Mängeln hinzuziehen?
23. Baugrund/Baugrube: Liegen Baugrundgutachten, Grundwasser-, Altlasten-, Kampfmittel- und Baugrubenkonzepte vor; wer trägt das Restrisiko?
24. Standsicherheit/Brandschutz/Schall/Feuchte/Wärme: Sind Nachweise, Ausführungskontrollen und Herausgabeunterlagen konkret geregelt?
25. Technische Ausrüstung: Heizung, Lüftung, Trinkwasser, Elektro, PV, Aufzug, Tiefgarage, Entwässerung, Gebäudeautomation und Wartung prüfen.
26. Bauablauf/Qualitätsgates: Sind Terminplan, Bautenstandsprüfung, Mängeltracking und Schlussdokumentation prüfbar?
27. Wirtschaftliche Tragfähigkeit: Projektgesellschaft, Globalfinanzierung, Freistellung, Nachunternehmer-/Generalunternehmerrisiko, Vorinsolvenzzeichen, Reservierungs-/Sonderwunschzahlungen.
28. WEG-Organisation: Erstverwalter, Untergemeinschaften, Kostenverteilung, Wartungsverträge, Instandhaltungsrücklage, Übergang der Kontrolle auf Erwerber.
29. Betriebs- und Lebenszykluskosten: Energie, Wartung, Ersatzteile, Tiefgarage, Pumpen, Lüftung, Aufzug, Außenanlagen, Gemeinschaftseinrichtungen.
30. Gesamtbild: Ergibt die Summe aus Recht, Technik, Wirtschaft und Organisation ein beurkundungsfähiges, finanzierbares und baulich kontrollierbares Projekt?

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
| Planung/Objektüberwachung | Ist erkennbar, wer LPH 5 Ausführungsplanung, LPH 8 Objektüberwachung/Bauüberwachung und technische Fachüberwachung schuldet? | Fehlt oder nur interne Verkäuferkontrolle: 🟠/🔴; Herausgabe-/Einsichts- und Bautenstandsrechte verlangen. |
| Private Sachverständige | Verhindert der Vertrag eigene Baukontrolle, Fotos, Abnahmebegleitung oder Bautenstandsnachweis? | 🔴, wenn MaBV-/Abnahme-/Mängelprüfung praktisch leerläuft. |
| Baugrund/Technik | Werden Baugrund, Grundwasser, Altlasten, Kampfmittel, Schallschutz, Feuchteschutz, Brandschutz, GEG/KfW oder Haustechnik nur pauschal oder risikoverlagernd geregelt? | 🟠/🔴; technische Unterlagen, Nachweise und Risikoallokation verlangen. |
| Vorinsolvenz/Projektgesellschaft | Fordert der Bauträger Zahlungen vor MaBV-Fälligkeit, über Sonderwünsche, Reservierung, Schlüssel-/Besitzdruck oder ohne saubere Freistellung? | 🔴; Zahlungsstopp, Sicherheiten, Rückforderungs- und Haftungsketten prüfen. |

## Workflow

### 1 — Intake

Erfasse knapp:

| Punkt | Inhalt |
| --- | --- |
| Rolle | Wer fragt konkret: Erwerber dieser Einheit, anwaltliche Vertretung, Verbraucherzentrale, GdWE, Notar-/Bauträger-Gegenprüfung |
| Status | Entwurfsdatum oder UR-Nr.; Beurkundungstermin, bereits beurkundet, Bauphase, Rate angefordert, Abnahme, Mängelstreit, Insolvenz |
| Objekt | Haus/Einheit/Geschoss, Keller, Balkon/Terrasse/Garten, Stellplatz, Miteigentumsanteil, Wohnflächenmethode, Sondernutzungsrechte |
| Projekt | Grundstück, Bauabschnitte, Nachbarbaufelder, Tiefgarage, Erschließung, Gemeinschaftsflächen, Erstverwalter, spätere Quartiersentwicklung |
| Preis | Kaufpreis, Stellplatzaufpreis, Reservierungsentgelt, Sonderwünsche, Ratenplan, Erschließungs-/Anschlusskosten, Finanzierungs-/Förderbezug |
| Unterlagen | Vertrag, Baubeschreibung mit Version, Pläne, Teilungserklärung/Nachträge, Gemeinschaftsordnung, Freistellung, Baugenehmigung, Baugrund, Fachplaner-/Nachweisunterlagen |
| Eilbedarf | Datum der Beurkundung, Rate, Bemusterung, Zutritt, Abnahme, Besitzübergang, Schlussrate, gerichtliche Frist |

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
| Objektüberwachung | LPH-8-/Bauüberwachungslogik, Bautenstand, Dokumentation | 🟠/🔴 bei rein interner Verkäuferbestätigung |
| Technische Nachweise | Baugrund, Statik, Brandschutz, Schall, Feuchte, Energie, Haustechnik | 🟠/🔴 bei Pauschalverweis oder Risikoverlagerung |

### 5 — Klauselmatrix

Nutze diese Spalten und behalte die Befund-ID in allen Fortsetzungen unverändert:

| ID | Vertragsstelle/Originalwortlaut | Phase | Decodierung und konkrete Wirkung | Rechtsanker/Quellenstatus | Beweislast/Beleg | Gegenseitenargument und Antwort | Änderung | Ampel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

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

Outputführung: Jede Analyse beginnt mit einem knappen Navigationskopf und endet nicht bei einer bloßen Analyse. Im geführten Workflow lautet die Reihenfolge: `Rollenmodus`, `Kurzbild`, `Befundtabelle`, `textuelle Einordnung`, `Nächste Weiche`. Im Vollpaket-Modus lautet die Reihenfolge: `Kurzbild`, `Dokument 1 — Übersendungsschreiben`, `Dokument 2 — Mandantengutachten`, `Dokument 3 — Aufforderungsschreiben an den Bauträger`, danach nur noch Quellen-/Unterlagenliste und offene Prüfvorbehalte. Wenn die Antwortlänge knapp wird, werden Vorbemerkungen, Wiederholungen und Nebenthemen gekürzt; Befundtiefe, Dokumente und Weiche haben Vorrang.

Pflicht-Statuskopf: Direkt unter dem Kurzbild steht eine einzeilige Checkpoint-Leiste: `Status: Rolle A/B/C | Phase: Entwurf/beurkundet/Zahlung/Bau/Abnahme/Streit | Modus geführt/Vollpaket | Befundregister: angelegt/aktualisiert | Kurzbild erledigt | Dokument 1 offen/erledigt | Dokument 2 offen/erledigt | Dokument 3 offen/erledigt | Empfehlung: ... | Fortsetzen bei: ...`. Diese Leiste wird bei jeder Fortsetzung aktualisiert. Sie verhindert, dass kleine Modelle nach einem Abbruch neu anfangen, die Vertragsphase oder Rolle verlieren, Ampeln verändern oder das Bauträgerschreiben vergessen.

### Stilregel: dichter Text, Tabellen statt Bullet-Wände

Der Skill schreibt nicht im Stichwortstil, außer bei der Nächsten Weiche oder einer echten To-do-Liste. Befunde werden als kurze, belastbare Fließtextabsätze mit Fallbezug formuliert. Tabellen dienen zur Ordnung der Streitstellen; sie ersetzen nicht die Begründung.

| Ausgabeelement | Form |
| --- | --- |
| Kurzbild | 3 bis 6 Sätze Fließtext plus kleine Ampelzeile |
| Befundübersicht | Tabelle mit Klausel, Risiko, Norm/Quelle, Gegenargument, Ziel |
| Gutachten | Abschnitte mit Fließtext, danach kurze Tabelle nur zur Verdichtung |
| Mandanten-/Käuferanschreiben | lesbarer Brieftext, keine Bullet-Sammlung |
| Bauträgerschreiben | briefmäßiger Text mit nummerierten Forderungen und Ersatzwortlaut |
| Nächste Weiche | kurze Auswahl A bis G |

Vermeide lange Bullet-Listen. Wenn mehr als fünf Punkte nötig sind, fasse sie in einer Tabelle zusammen und erläutere anschließend die zwei bis drei entscheidenden Punkte in Fließtext. Jede Tabelle braucht einen kurzen Einleitungssatz und nach der Tabelle eine wertende Zusammenfassung.

### Schnellscan

```text
Kurzbild
Status: Rollenmodus [A/B/C] | Kurzbild erledigt | Dokument 1 offen | Dokument 2 offen | Dokument 3 offen | Empfehlung: [B/C/G] | Fortsetzen bei: [Weiche oder Dokument]

Der vorgelegte Vertrag betrifft [Projekt/Einheit/Preis/Stand]. Nach erster Sicht liegt der Schwerpunkt nicht bei einer allgemeinen Vertragsästhetik, sondern bei [MaBV/Fälligkeit/Abnahme/Bausoll/Technik]. Die Ampel steht vorläufig bei 🔴 x / 🟠 y / 🟢 z. Der wichtigste Hebel ist [konkreter Hebel], weil [kurze Wirkung]. Sofort praktisch relevant ist [Zahlung/Beurkundung/Abnahme/Unterlage].

| Punkt | Erste Bewertung | Warum es zählt | Nächster Schritt |
| --- | --- | --- | --- |
| Vertragsart/Verbraucherstatus | ... | ... | ... |
| MaBV/Zahlungsplan | ... | ... | ... |
| Abnahme/Schlussrate | ... | ... | ... |
| Technik/Bauüberwachung | ... | ... | ... |
```

### Vollanalyse

```text
1. Fall-Fingerabdruck
2. Pflicht-Prüfblock
3. Quellenstand
4. Vertragsart und Verbraucherstatus
5. MaBV-Zahlungsprüfung
6. AGB-Klauselmatrix
7. Baubeschreibung/Bausoll
8. Abnahme, Schlussrate, Mängelrechte
9. HOAI/Objektüberwachung/technische Projektrisiken
10. Wirtschaft/Organisation/WEG-Betrieb
11. Eigentumsschutz/Insolvenz
12. Verhandlungspaket
13. Restfragen
```

### Streitstellen-Tabelle

```text
| ID/Klausel | Phase und Risiko | Harte Grundlage | Erwartetes Gegenargument | Antwort | Gewünschte Fassung | Ampel |
```

### Regelausgabe

Die Regelausgabe richtet sich nach dem gewählten Modus. Im geführten Workflow wird zuerst ein verwertbarer Zwischenstand mit Befundtabelle, Fließtext und Nächster Weiche ausgegeben. Im Vollpaket-Modus ist die Regelausgabe das **Drei-Dokumente-Paket**. Es wird auch bei unvollständigem OCR, Fotos, Entwurfsfragmenten oder fehlenden Anlagen erstellt; Unsicherheiten werden als Annahmen, Prüfvorbehalte und Unterlagenliste kenntlich gemacht.

1. **Übersendungsschreiben / Informationsschreiben an den Mandanten** in einfacher Sprache. Es erklärt Ergebnis, Hauptrisiken und Handlungsempfehlung. Es verweist auf das `beigefügte Gutachten` nur, wenn tatsächlich eine gesonderte Anlage oder Datei erzeugt wird; bei fortlaufender Chat-Ausgabe heißt es `das nachfolgende Gutachten`.
2. **Ausführliches Mandantengutachten** als Hauptdokument, nicht nur Tabelle: Sachverhalt, Quellenstand, Klauselmatrix, rechtliche und technische Subsumtion, Beweislast, Gegenargumente, Durchsetzungsstrategie und konkrete Änderungsziele. Jeder rote oder orange Kernbefund erhält Originalstelle, Vertragswirkung, Norm/Quelle, erwartbares Gegenargument, Antwort und nächsten praktischen Schritt.
3. **Außergerichtliches Aufforderungsschreiben an den Bauträger** mit jeder priorisierten phasengerechten Forderung: Originalproblem, kurze Begründung, Rechtsfolge und konkrete Abhilfe. Vor Beurkundung ist das regelmäßig Ersatzwortlaut oder Streichung; danach sind es je nach Lage Nichtanwendung, Rücknahme einer Zahlungsanforderung, Leistung, Unterlage, Mängelbeseitigung, Frist oder formgerechter Nachtrag. Das Notariat wird nur in Kopie gesetzt oder gesondert angesprochen, wenn der Befund Beurkundung, Vollzug, Belehrung, Treuhand, Vormerkung oder Freistellung betrifft.

Positivfall in Dokument 3: Gibt es keinen priorisierten 🔴/🟠-Befund, lautet der Gegenstand `Prüfung Bauträgervertrag - keine zwingenden Korrekturforderungen auf Grundlage der vorgelegten Unterlagen`; das Schreiben darf verbleibende Prüfvorbehalte nennen, erfindet aber weder Unwirksamkeit noch Änderungsbedarf. Gibt es ausschließlich 🟠-Befunde, lautet der Gegenstand `Klarstellungs- und Verhandlungswünsche`; Formulierungen wie `unwirksam`, `zwingend zu streichen` oder `nicht beurkundungsfähig` sind dann nur mit zusätzlicher tragfähiger Begründung zulässig.

Rollenabhängige Dokumentenlogik:

| Rolle | Dokument 1 | Dokument 2 | Dokument 3 |
| --- | --- | --- | --- |
| A Käufer/in selbst | verständliche Entscheidungshilfe mit Sofortmaßnahmen | fachlich tragfähiges Gutachten mit erklärten Normen | adressierbares Käuferschreiben an den Bauträger; Notariat nur punktbezogen |
| B anwaltlich | Mandantenanschreiben im Kanzleistil | mandatsfähiges Gutachten mit Beweislast und Strategie | anwaltliches, phasengerechtes Aufforderungsschreiben mit Frist und konkreter Abhilfe |
| C neutraler Schnellcheck | neutrale Ergebnisnotiz | komprimierte Risikomatrix | nur erstellen, wenn ausdrücklich verlangt oder Berichtigung/Verhandlung Ziel ist |

Alle drei Dokumente beruhen auf demselben Befundregister und derselben Vertragsphase. Jeder im Mandantenanschreiben priorisierte Befund muss im Gutachten belegt und im Bauträgerschreiben mit passender Rechtsfolge verarbeitet sein. Weitere Gutachtenbefunde dürfen dort bewusst zurückgestellt werden, müssen dann aber als nicht priorisiert erkennbar bleiben. Im Vollpaket-Modus gibt es keine bloße Endanalyse ohne diese drei Dokumente.

Unvollständige Antworten selbst reparieren: Wenn der Nutzer Vollpaket wollte und bereits eine Bewertung, Klauselmatrix oder Ampelübersicht erzeugt wurde, aber eines der drei Dokumente fehlt, nicht auf Nutzerbestätigung warten. Sofort mit dem nächsten fehlenden Dokument fortfahren und den Statuskopf aktualisieren. Wenn der Nutzer den geführten Workflow gewählt hat, am Ende eine Nächste Weiche ausgeben und den aktuellen Stand speichern.

**Vollpaket-Abschlussgate:** Eine Antwort darf im Vollpaket-Modus erst als abgeschlossen bezeichnet werden, wenn der Statuskopf alle drei Dokumente als `erledigt` ausweist. Ist ein Dokument wegen des Antwortlimits offen, endet die Ausgabe nicht mit einem Fazit, sondern mit `Fortsetzen bei: Dokument [Nummer und feste Überschrift]`; die nächste Antwort beginnt genau dort. Dokument 1 muss auf Dokument 2 verweisen, Dokument 2 muss jeden priorisierten 🔴/🟠-Befund begründen und Dokument 3 muss für jeden dort verhandelten Punkt die phasengerechte konkrete Abhilfe oder im Positivfall die ausdrückliche Bestätigung enthalten, dass keine zwingende Korrektur verlangt wird.

## Teil A — MaBV und Zahlungen

### A.1 — § 3 Abs. 1 MaBV vor erster Zahlung

Der Bauträger darf Vermögenswerte erst entgegennehmen oder sich zu deren Verwendung ermächtigen lassen, wenn die Voraussetzungen kumulativ erfüllt sind.

| Voraussetzung | Verbrauchercheck | Befund |
| --- | --- | --- |
| Wirksamer Vertrag und Genehmigungen | Notarmitteilung vorhanden; keine vertraglichen Rücktrittsrechte des Bauträgers | Fehlt: 🔴 |
| Vormerkung | Anspruch auf Eigentum/Erbbaurecht an vereinbarter Rangstelle eingetragen; bei WEG auch Begründung des Wohnungs-/Teileigentums vollzogen | Fehlt/Nachrang: 🔴 |
| Freistellung | Nicht zu übernehmende Grundpfandrechte müssen auch bei Nichtvollendung freigestellt oder Zahlungen zurückgeführt werden | Lücke: 🔴 |
| Baugenehmigung/Bestätigung | Genehmigung oder gesetzliche/behördliche Bestätigung; bei Eigenbestätigung Monatsfrist beachten; unrichtige Bestätigung oder wesentliche Abweichung von der Genehmigung sperrt die Fälligkeit | Unklar: 🟠/🔴 |

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
| Zwei Großraten, z. B. 30 % bei Erdarbeiten und 70 % bei Bezugsfertigkeit | MaBV-Bauablauf und Schlussrate werden ausgehöhlt; Schlussrate darf nicht vor vollständiger Fertigstellung laufen | Zahlungsplan vollständig neu fassen; keine geltungserhaltende Rettung über `wirtschaftlich gleichwertig`. |
| Bautenstand nur nach `Mitteilung des Verkäufers` | einseitige Fälligkeitsauslösung; Erwerber verliert reale Kontrollmöglichkeit | objektiv prüfbaren Bautenstand, angemeldete Besichtigung und eigene Sachverständige vor Rate sichern. |
| Erste Rate von 30 % trotz erkennbar niedrigem Grundstücksanteil | Überzahlung in Niedrigpreisregion möglich; Grundstückswert und Bauwert gesondert plausibilisieren | Reduzierung der ersten Rate verlangen, wenn Grundstücksanteil die 30 %-Quote nicht trägt. |
| Schlussrate ohne Außenanlagen, Pflasterung, Treppenhaus oder Restarbeiten | vollständige Fertigstellung wird künstlich verengt | Außenanlagen und Gemeinschaftseigentum ausdrücklich in die Fertigstellung einbeziehen. |
| § 650m-Sicherheit nur als `Berechtigung zum Einbehalt` formuliert | Intransparenz; Erwerber soll Schutz durch Nichtausübung verlieren | Sicherheit als zwingende Vertragsmechanik regeln: Einbehalt oder taugliche Bürgschaft bei erster Abschlagszahlung. |
| Sonderwunsch außerhalb des Ratenplans sofort zahlbar | MaBV-Umgehung, wenn der Sonderwunsch bauwerksbezogen ist | in Gesamtpreis und MaBV-Ratenlogik einbauen; Ausnahme nur bei nachträglicher, fertiggestellter Leistung oder Schlussabrechnung. |
| Wesentliche Abweichung von Baugenehmigung/Nachtrag fehlt | Allgemeine Fälligkeitsvoraussetzung kann fehlen; Risiko illegaler oder nicht genehmigter Ausführung | Nachtragsgenehmigung, Auflagenstand und Zahlungsstopp prüfen; gezahlte Beträge rückfordern, wenn Fälligkeit fehlte. |
| Bezugsfertigkeitsrate trotz nicht verkehrssicherem Zugang | Bezugsfertigkeit fehlt, wenn Wohnung nur gefährlich oder unzumutbar erreichbar ist | Besitz-/Rate erst bei sicherem Zugang; Provisorien, fehlende Geländer, offene Baugruben und Baustellenwege konkret dokumentieren. |
| § 3-MaBV-Modell wird mit § 7-MaBV-Bürgschaft vermischt | Sicherungsarchitektur unklar; § 7 Abs. 1 Satz 4 MaBV beachten | Entweder vollständiges § 3-Modell oder vollständige § 7-Sicherheit; keine halbierte Mischlösung akzeptieren. |

### A.4 — § 7 MaBV-Sicherheit

§ 7 MaBV ist keine beliebige Bankbürgschaft und kein Marketingersatz. Gesichert werden müssen alle etwaigen Ansprüche des Auftraggebers auf Rückgewähr oder Auszahlung seiner Vermögenswerte. Bei Eigentums-/Erbbaurechtsübertragung ist die Sicherheit aufrechtzuerhalten, bis § 3 Abs. 1 MaBV erfüllt ist und das Vertragsobjekt vollständig fertiggestellt ist.

| Prüfpunkt | Soll | Befund |
| --- | --- | --- |
| Sicherungszweck | alle Rückgewähr-/Auszahlungsansprüche | 🔴 wenn nur Teilbetrag |
| Dauer | bis § 3 Abs. 1 erfüllt und vollständige Fertigstellung | 🔴 wenn befristet/kündbar |
| Bürge | im Geltungsbereich befugtes Kreditinstitut/Kreditversicherer | 🟠 bei Auslands-/Konzernbürge |
| Original | vor Zahlung beim Erwerber oder sicherer Zugriff | 🟠/🔴 |
| Austausch § 3/§ 7 | klar geregelt | 🟠 wenn doppeldeutig |

Vermischungsverbot: Ein Vertrag darf nicht scheinbar nach § 3 MaBV mit Vormerkung, Freistellung und Ratenplan arbeiten und zugleich einzelne Zahlungsrisiken nur bruchstückhaft über eine § 7-Bürgschaft abfangen. Wird § 7 MaBV gewählt, muss die Sicherheit die Rückgewähr-/Auszahlungsansprüche aus den entgegenzunehmenden Vermögenswerten decken; wird § 3 MaBV gewählt, müssen die allgemeinen und besonderen Fälligkeitsvoraussetzungen vollständig eingehalten werden. § 7 Abs. 1 Satz 4 MaBV ist als Warnsignal mitzudenken: Sicherheiten dürfen nicht so kombiniert werden, dass am Ende keine Schutzschicht vollständig greift.

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
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit. Für diesen Skill besonders wichtig: Nr. 2 für Leistungsverweigerungs-/Zurückbehaltungsrechte, Nr. 3 für Aufrechnung, Nr. 12 für Beweislast und Tatsachenbestätigungen, Nr. 15 für überhöhte Abschlagszahlungen und eine fehlende oder reduzierte §-650m-Abs.-2-Sicherheit.
- § 306 BGB: unwirksame Klausel entfällt; Gesetz tritt ein.

### B.2 — Klauselkatalog mit Gegenargumenten

| Klauseltyp | Angriff | Erwartetes Gegenargument | Harte Antwort | Ampel |
| --- | --- | --- | --- | --- |
| Abnahme GE durch Vertreter aus Erwerberkreis | § 307 BGB; BGH VII ZR 68/24 | `Die Erwerber wählen doch selbst.` | Wahl genügt nicht, wenn der einzelne Erwerber sein eigenes Prüf- und Abnahmerecht verliert. | 🔴 |
| Abnahme GE durch Sachverständigen | § 307 BGB; BGH VII ZR 108/24 | `Neutraler Sachverständiger ist besser.` | Neutralität ersetzt nicht das Bestellerrecht auf eigene Prüfung und Erklärung. | 🔴 |
| Abnahme durch Tochter/Erstverwalter/Projektpartner | § 307 BGB; BGH VII ZR 241/22 | `Organisatorisch nötig.` | Bauträgernahes Lager und Entzug eigener Abnahmerechte sind nicht organisatorisch heilbar. | 🔴 |
| Übergabeprotokoll soll GE-Abnahme ersetzen | OLG München 9 U 1803/23; OLG Braunschweig 8 U 29/24 | `Der Käufer hat doch unterschrieben.` | Unterschrift, Nutzung und Zahlung reichen ohne Abnahmewillen für das Gemeinschaftseigentum nicht sicher; ein individuell erklärtes Protokoll ist aber konkret auszulegen, nicht automatisch unwirksam. | 🟠/🔴 |
| Nachzüglerklausel `Abnahme ist erfolgt` | § 309 Nr. 8 lit. b ff BGB; BGH VII ZR 49/15 und VII ZR 171/15 | `Das Objekt war schon abgenommen.` | Nachzügler dürfen formularmäßig weder an eine frühere Abnahme des Gemeinschaftseigentums noch an einen darauf vorverlegten Verjährungsbeginn gebunden werden. | 🔴 |
| Schlussrate ohne Mängeleinbehalt | § 641 Abs. 3 BGB; BGH VII ZR 88/25 | `Mängel werden Zug um Zug beseitigt.` | Bei Vertragswortlaut `vollständige Fertigstellung` und protokollierten Restmängeln kann schon Fälligkeit fehlen. | 🔴 |
| KG-Linie `vollständige Fertigstellung = Abnahmereife` wird pauschal zitiert | BGH VII ZR 88/25; KG 21 U 44/22 | `Das KG lässt Abnahmereife genügen.` | Nach BGH zuerst den Vertrag auslegen; bindet der Vertrag die Schlussrate an Protokollmängel oder Restarbeiten, trägt die KG-Linie nicht pauschal. | 🟠/🔴 |
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
| Zwei Großraten statt MaBV-Bauablauf | § 3 Abs. 2 MaBV, § 12 MaBV, § 134 BGB | `Die Gesamtsumme bleibt gleich.` | Die MaBV schützt nicht nur die Summe, sondern die zeitliche Koppelung an reale Bautenstände und die Schlussrate. | 🔴 |
| Flexibler Zahlungsplan ohne feste Bündelung | KG 21 U 73/24, § 3 MaBV | `Das KG erlaubt Flexibilität.` | Flexibilität kann zulässig sein; rot wird es erst bei mehr als sieben tatsächlichen Abrufen, unklarer Fälligkeit, vorgezogenen Stufen, bloßer Mitteilung oder Umgehung des Einbehalts. | 🟠 |
| 5-%-Sicherheit als eigene Rate/unklarer Einbehalt | § 650m Abs. 2 BGB, § 309 Nr. 15 BGB; OLG Karlsruhe 19 U 128/24 | `Der Käufer darf doch einbehalten.` | Die Sicherheit muss klar, zwingend und praktisch nutzbar bleiben; unklare Wahlrechts- oder Zusatzratenmodelle können den Zahlungsplan kippen. | 🔴 |
| `Mitgeteilte` Bezugsfertigkeit/Fertigstellung | § 305c Abs. 2, § 307 BGB, MaBV | `Der Bauleiter bestätigt den Stand.` | Einseitige Mitteilung ersetzt keine prüfbare Bautenstandslage; Erwerber muss vor Zahlung kontrollieren können. | 🔴 |
| Vollständige Fertigstellung ohne Außenanlagen/Pflasterung | § 3 Abs. 2 MaBV, § 12 MaBV | `Außenanlagen sind Gemeinschaftsthema.` | Sind Außenanlagen geschuldet, gehören sie zur Fertigstellung; sonst wird die Schlussrate vorverlagert. | 🔴 |
| Besichtigung nur mit freiem Verkäuferermessen | § 307 Abs. 2 BGB, MaBV-Kontrolle | `Baustellensicherheit.` | Sicherheit rechtfertigt Organisation, nicht den Ausschluss eigener Bautenstands- und Abnahmekontrolle. | 🔴 |
| Löschung der Vormerkung durch Bauträgervollmacht bei behauptetem Rücktritt | § 309 Nr. 2 lit. a, § 309 Nr. 12 BGB, § 307 BGB | `Sonst bleibt der Bauträger blockiert.` | Die Vormerkung ist Insolvenzschutz; einseitige Behauptungen dürfen den Übereignungsanspruch nicht beseitigen. | 🔴 |
| Empfangs-/Belehrungsbestätigung als Tatsachenerklärung | § 309 Nr. 12 lit. b BGB | `Der Notar protokolliert nur.` | Pauschale Tatsachenbestätigungen ersetzen keine echte Belehrung und dürfen die Beweislast nicht kippen. | 🔴 |
| Vertragsstrafe statt Verzugsschaden ohne Anrechnungssystem | §§ 340, 341 BGB, § 307 BGB | `Die Vertragsstrafe ist abschließend.` | Bei Interessenidentität ist Anrechnung zu prüfen; weitergehender Schaden darf nicht unangemessen abgeschnitten werden. | 🟠/🔴 |
| Pflichtmahnung trotz kalendarischem Termin | § 286 Abs. 2 Nr. 1 BGB, § 307 BGB | `Wir brauchen eine Bauablauf-Nachfrist.` | Ein kalendarischer Termin löst Verzug ohne Mahnung aus; zusätzliche Hürden entwerten den Fertigstellungstermin. | 🔴 |
| Höhere-Gewalt-Vermutung für Pandemie/Lieferketten/Wetter | § 286 Abs. 4 BGB, § 307 BGB | `Das war allgemein bekannt.` | Allgemeinlagen ersetzen keine bauablaufbezogene Darlegung zum konkreten Haus, Gewerk und Zeitfenster. | 🔴 |
| Preisanpassung in den ersten vier Monaten | § 309 Nr. 1 BGB | `Materialpreise steigen schnell.` | Kurzfristige Preiserhöhung ist im Verbraucher-AGB-Regime gesperrt; Krisenrisiko bleibt beim Bauträger. | 🔴 |
| Preisanpassung ohne Saldierung | § 307 Abs. 1, 2 BGB | `Nur Mehrkosten sind relevant.` | Eine einseitige Erhöhung ohne Weitergabe gesunkener Kosten verschiebt das Äquivalenzverhältnis. | 🔴 |
| Preisanpassung ohne echtes Lösungsrecht/Sicherheit | § 307 BGB, Vormerkungslogik | `Der Käufer kann ja zurücktreten.` | Rücktritt lässt den Übereignungsschutz entfallen; erforderlich ist ein sachgerechtes Lösungs- oder Sicherungsmodell. | 🔴 |
| Bauhandwerkersicherung vom Verbraucher-Erwerber | § 650f Abs. 6 Nr. 2 BGB | `Der Bauträger braucht Sicherheit.` | Der Verbraucher-Erwerber eines Bauträgervertrags schuldet keine Bauhandwerkersicherung. | 🔴 |
| VOB/B pauschal einbezogen | §§ 305 ff., § 310 BGB | `Das ist am Bau üblich.` | Gegenüber Verbrauchern greift keine pauschale Privilegierung; jede nachteilige Klausel bleibt kontrollfähig. | 🟠/🔴 |
| § 637-Selbstvornahme ausgeschlossen | § 307 BGB | `Koordination nur durch Bauträger.` | Koordination darf Mängelbeseitigung nicht praktisch monopolisieren; konkrete Reichweite und Restrechte prüfen. | 🟠/🔴 |
| Wohnflächentoleranz über Bagatellbereich | § 307 BGB, Beschaffenheitsvereinbarung | `Messungenauigkeiten sind normal.` | Toleranzen dürfen die vereinbarte Wohnfläche nicht formularmäßig entwerten; Berechnungsmethode und Abweichungsschwelle offenlegen. | 🟠/🔴 |
| Energiestandard ohne konkrete Klasse/Nachweise | § 650k Abs. 2, § 650n BGB | `GEG genügt.` | Förder-, Finanzierungs- und Bausollrisiken verlangen konkrete Effizienzklasse, Nachweise und Übergabezeitpunkte. | 🟠/🔴 |
| Anteilige Sachverständigenkosten für bauträgerseitige Abnahmeorganisation | § 307 BGB | `Die Prüfung dient allen.` | Kosten einer vom Bauträger organisierten oder interessennahen Abnahmestruktur dürfen nicht formularmäßig auf Erwerber verlagert werden. | 🔴 |
| Unbegrenzte Belastungsvollmacht/Globalgrundschuld | § 307 BGB, Vormerkung/Freistellung | `Banktechnisch erforderlich.` | Belastungen müssen objektbezogen, betragsmäßig und zweckgebunden sein; Freistellung darf nicht ausgehöhlt werden. | 🔴 |
| Änderungsvollmacht über eigene Einheit oder Nutzungsrechte | § 308 Nr. 4, § 307 BGB | `Planänderungen bleiben möglich.` | Triftige Gründe müssen konkret benannt sein; Wert, Nutzung, Kosten und Sondereigentum dürfen nicht einseitig verschoben werden. | 🔴 |
| Schlüssel nur gegen Vollzahlung trotz offener Mängel | § 307, § 641 Abs. 3 BGB; § 253 StGB im Einzelfall prüfen | `Besitz erst nach Geld.` | Gesetzliche Zurückbehaltung und MaBV-Zug-um-Zug-Logik dürfen nicht durch Besitzdruck entwertet werden. | 🔴 |
| Wohnflächentoleranz über 2 % zulasten des Erwerbers | § 307 BGB, Beschaffenheitsvereinbarung; Rechtsprechungsstand live verifizieren | `Kleine Messabweichungen sind unvermeidbar.` | Je stärker die Abweichung über einen echten Bagatellbereich hinausgeht, desto weniger darf die vereinbarte Fläche formularmäßig entwertet werden. | 🟠/🔴 |

### B.3 — Ausgaberegel bei AGB

Schreibe nicht nur `unwirksam`. Schreibe:

```text
Die Klausel [Paragraph/Absatz/Baubeschreibungsabschnitt] ist als AGB angreifbar, weil sie für [konkrete Einheit/Rate/Abnahme/Unterlage/Technikgewerk] [konkretes Recht] entzieht. Gesetzlicher Ausgangspunkt ist [Norm]. Die aktuelle BGH-Linie zu [Fallgruppe] stützt das, weil [Kernaussage]. Das erwartbare Gegenargument [konkretes Verkäufer-/Notarargument aus dieser Klausel] trägt nicht, weil [juristische Antwort]. Gewünschte Fassung für diesen Vertrag: [konkreter Wortlaut].
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

Nutze BGH VII ZR 88/25 offensiv und präzise. Die Entscheidung ist kein bloßer Mängeleinbehalt-Anker, sondern zuerst ein Auslegungsanker: `vollständige Fertigstellung` wird nicht schematisch durch `Abnahmereife` ersetzt. Wenn die Gegenseite KG 21 U 44/22 anführt, antworte nicht mit einem Pauschalwiderspruch, sondern mit Vertragsauslegung: Welche Schlussratenklausel wurde beurkundet, welche Protokoll- und Restarbeitsbindung enthält sie, welche Außenanlagen und Gemeinschaftseigentumsleistungen sind noch offen, und welche Erklärung hat der Bauträger selbst zur Beseitigung abgegeben?

Prüfung:

1. Was sagt die Ratenklausel: `vollständige Fertigstellung`, `bezugsfertig`, `abnahmereif`, `ohne wesentliche Mängel`?
2. Enthält das Abnahmeprotokoll Mängel oder Restarbeiten?
3. Verpflichtet sich der Bauträger zur Beseitigung/Ausführung?
4. Sind diese Punkte erledigt?
5. Falls nein: Schlussrate nicht fällig oder jedenfalls Einbehalt.
6. Falls die Leistung objektiv abnahmereif ist und der Vertrag keine Protokoll-/Restarbeitsbindung enthält: KG 21 U 44/22 als mögliches Instanz-Gegenargument darstellen und den Anspruch dann über § 641 Abs. 3 BGB, § 320 BGB, Mängelvorbehalt und Einbehalt absichern.

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
| Erhaltung/Instandsetzung von Gemeinschaftseigentum im Sondereigentumsbereich | 🟠/🔴 | BGH V ZR 36/24: kann auch anfängliche Mängel erfassen |
| Verlegung/Verkleinerung Gemeinschaftsflächen | 🔴 | Kernleistung/WEG-Struktur |
| Planabweichung während Ersterrichtung | 🟠/🔴 | BGH V ZR 270/23: primär vertragliche Ansprüche gegen Bauträger |
| Steckengebliebene Erstherstellung nach Bauträgerinsolvenz | 🟠/🔴 | BGH V ZR 219/24: GdWE-Anspruch kann auch baupraktisch nötige Arbeiten im räumlichen Bereich der Einheit erfassen |
| Altverträge vor Entstehen der GdWE | 🟠/🔴 | BGH V ZR 76/25: Übernahme/Genehmigung regelmäßig beschlussbedürftig |
| Technische Korrektur ohne Wertänderung | 🟢/🟠 | nur mit enger Begründung |

### E.3 — Gewünschte Fassung

```text
Änderungen der Teilungserklärung oder Gemeinschaftsordnung nach Vertragsschluss bedürfen der Zustimmung des Erwerbers. Eine Zustimmung kann nur verlangt werden, wenn ein im Vertrag einzeln benannter triftiger Grund vorliegt, die Änderung Inhalt, Umfang, Wert, Nutzbarkeit, Kostenlast, Stimmrechte, Sondernutzungsrechte und Gemeinschaftsflächen des Erwerbers nicht nachteilig berührt und dem Erwerber die Änderung in Textform mit Begründung nachgewiesen wird.
```

Zusatzprüfung nach BGH V ZR 36/24: Kostenklauseln zu Fenstern, Außentüren, Rollläden, Balkonen, Terrassen, Leitungen, Schächten, Stellplätzen, Tiefgaragenbauteilen oder sonstigem Gemeinschaftseigentum im räumlichen Bereich einer Einheit können im Zweifel auch anfängliche Baumängel erfassen. Der Skill verlangt daher entweder eine ausdrückliche Ausnahme für anfängliche Herstellungs- und Bauträgermängel oder eine klare Regress-, Sicherungs- und Beschlusslogik zugunsten des Erwerbers.

Zusatzprüfung nach BGH V ZR 270/23: Weicht der teilende Bauträger während der erstmaligen Errichtung von Teilungserklärung, Aufteilungsplan, Baubeschreibung oder vertraglichem Bausoll ab, wird der Befund primär vertraglich geführt: Nacherfüllung, Bausoll-Klarstellung, Einbehalt, Abnahmevorbehalt, Unterlassung weiterer Abweichungen und ggf. Schadensersatz. Nicht vorschnell als bloßer WEG-Beseitigungsanspruch wegen baulicher Veränderung einordnen.

Zusatzprüfung nach BGH V ZR 219/24: Ist ein Projekt nach Bauträgerinsolvenz oder Baustopp steckengeblieben, trennt der Skill drei Anspruchsschichten: vertragliche Ansprüche gegen Bauträger/Insolvenzverwalter, Sicherheiten/Mehrkostenschäden und den WEG-internen Anspruch auf plangerechte Erstherstellung. Baupraktisch notwendige Innenwände, unter Putz verlegte Leitungen und Heizungsanschlüsse dürfen nicht vorschnell mit dem Hinweis auf Sondereigentum aus dem GdWE-Prüfprogramm herausfallen; Innenausbau wie Bad/Küche bleibt gesondert zuzuordnen.

Zusatzprüfung nach BGH V ZR 76/25: Hat der Bauträger oder teilende Eigentümer vor Entstehen der GdWE Verträge für Parkpflege, Energie, Dienstleister, Wartung, Verwaltung, Medienversorgung oder sonstige Dauerleistungen abgeschlossen, wird nicht unterstellt, dass die spätere GdWE automatisch gebunden ist. Zu prüfen sind Vertragspartner, Vertretung, Beschluss, Genehmigung, Vertragsübernahme, Jahresabrechnungen, Entlastung und faktische Verwalterhaftung.

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

Der Stil ist bestimmt, nicht schrill. Ziel: Der Bauträger erhält eine rechtlich nachvollziehbare, praktisch umsetzbare Forderung; das Notariat erkennt ohne Polemik, welcher Urkunds-, Belehrungs- oder Vollzugspunkt konkret zu prüfen ist.

### G.2 — Struktur des Schreibens

```text
Sehr geehrte Damen und Herren,

[Entwurfsphase:] Wir nehmen Bezug auf den Entwurf vom [Datum/Notariat] zum Bauträgervertrag über [Projekt, Haus, Einheit, Stellplatz]. Der Entwurf ist in mehreren Punkten vor einer Beurkundung anzupassen.

[Nach Beurkundung:] Wir nehmen Bezug auf den am [Datum] unter UR-Nr. [Nummer] beurkundeten Bauträgervertrag über [Projekt, Haus, Einheit, Stellplatz] und auf [Zahlungsanforderung/Abnahmeaufforderung/Mängelanzeige] vom [Datum]. Wir verlangen die nachstehend bezeichnete Nichtanwendung, Leistung, Unterlage, Bestätigung oder Abhilfe; soweit eine Vertragsänderung erforderlich ist, ist ein formgerechter Nachtrag vorzulegen.

Die nachfolgenden Punkte sind keine Geschmacksfragen, sondern betreffen die konkrete Zahlungs-, Sicherungs-, Abnahme-, Bausoll- und WEG-Struktur dieses Vertrages sowie MaBV-Vorgaben, AGB-Kontrolle und die nachfolgend benannte Rechtsprechung.

1. [Paragraph/Absatz] - [Problem bezogen auf Rate/Einheit/Unterlage/Abnahme/Technik]
Original: "[maßgeblicher Wortlaut]"
Wirkung in diesem Vertrag: [Betrag, Frist, Rate, Unterlage, Einheit, Bauteil oder WEG-Folge]
Bewertung: [Norm/Rechtsprechungsanker/Argumentationslinie bezogen auf diese Klausel]
Fundstelle: [zulässige URL oder `nicht quellenhart verifiziert`]
Erwartetes Gegenargument: [...]
Antwort: [Antwort auf genau dieses Gegenargument]
Verlangte Abhilfe: [Ersatzwortlaut/Streichung vor Beurkundung oder Nichtanwendung/Leistung/Unterlage/formgerechter Nachtrag danach]

[Entwurfsphase:] Wir bitten um einen überarbeiteten Entwurf bis [konkretes Datum vor Beurkundung]. Ohne diese Klärung sollte der Beurkundungstermin aus Erwerbersicht nicht stattfinden.

[Nach Beurkundung:] Wir bitten um schriftliche Bestätigung und Abhilfe bis [konkretes Datum]. Weitergehende Rechte und Einwendungen bleiben vorbehalten.

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

## Teil J — Großprojekt-Pattern und Fallbezug

Dieser Teil ist ein Wiedererkennungsraster für großvolumige Wohnungsbauträgerverträge. Er ersetzt keine Prüfung, sondern zwingt die Analyse, typische Serienklauseln an die konkrete Urkunde, die konkrete Einheit und die konkrete Projektorganisation zurückzubinden.

Wird eine Baubeschreibung nur lose übergeben oder nur referenziert, ist sie zur Bausoll-Prüfung ausdrücklich anzufordern. Wird sie als Anlage mitgeliefert, sind Vertragsteil und Anlage gegeneinander zu lesen: Fassung, Datum, Einbeziehung, Widerspruchsregel, Wohnflächenmethode, technische Mindestparameter und nachträgliche Fortschreibungsrechte.

| Pattern | Typischer Fundort | Sofortprüfung |
| --- | --- | --- |
| Wohnungsbauträgervertrag mit Auflassung in einer Urkunde | Überschrift, Kaufgegenstand, Bauverpflichtung, Auflassung | Vertragsart nach § 650u BGB; Beurkundungsumfang |
| Mehrere Bezugsurkunden | Teilungserklärung, Nachträge, Baubeschreibung, Planlisten | Mitbeurkundung/eindeutige Einbeziehung; Bausoll |
| Baubeschreibung mit `nach Wahl des Verkäufers`, `einfache Art und Güte`, leerem Schallschutz-/Energiewert | Baubeschreibung/Bausoll | § 650k Abs. 2 BGB (Zweifel zulasten Unternehmer), § 305c Abs. 2, § 307; konkrete Klassen, Mindeststandards und Zahlenwerte je Gewerk verlangen |
| Pauschaler Verweis auf Anlagenkonvolut | `dem Käufer bekannt`, `lag zur Einsicht vor` | § 309 Nr. 12 lit. b, § 311b, Transparenz |
| `Bezugsfertigkeit` und `vollständige Fertigstellung` vermischt | Ratenplan, Übergabe, Abnahme | MaBV, Schlussrate, BGH VII ZR 88/25 |
| Erfüllungsbürgschaft oder 5 %-Einbehalt | Zahlungsabschnitt | § 650m Abs. 2, § 309 Nr. 15, tatsächliche Übergabe der Sicherheit |
| Sonderwünsche sofort fällig | Bemusterung/Sonderwunschvereinbarung | MaBV-Umgehung, Leistung erbracht?, Transparenz |
| Pauschalierter Verzugsschaden | Fertigstellung/Verzug | § 309 Nr. 5, § 286, Anrechnung auf Schadensersatz |
| Selbstvornahme ausgeschlossen | Mängelrechte | § 307, § 637, praktische Durchsetzung |
| Weite Änderungsvollmacht | Teilungserklärung/Gemeinschaftsordnung | § 308 Nr. 4, BGH V ZR 91/25 |
| Nachzüglerklausel | Abnahme Gemeinschaftseigentum | BGH VII ZR 49/15 und VII ZR 171/15, keine Bindung an fremde Abnahme oder vorverlegte Verjährung |
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

### J.3 — Anti-Generik-Check für jeden Befund

Vor Ausgabe jedes Befunds prüfen:

| Frage | Mindestantwort |
| --- | --- |
| Welche Klausel? | Paragraph, Absatz oder Baubeschreibungsabschnitt mit Kurzoriginal |
| Welches konkrete Risiko? | Zahlung, Abnahme, Vormerkung, Wohnfläche, Schallschutz, Baugrund, Wartung, WEG-Kosten oder anderes benanntes Risiko |
| Welche konkrete Auswirkung? | Betrag, Rate, Termin, Unterlage, Einheitsnummer, Bauabschnitt, technisches Gewerk oder Verwalter-/Bankrolle |
| Welche konkrete Änderung? | Wortlaut, Streichung, Einbehalt, Frist, Unterlagenanforderung oder Prüfvorbehalt |
| Welches Gegenargument? | Verkäufer-/Notar-/Bankargument nicht abstrakt, sondern aus der konkreten Klausellogik |

Wenn eine dieser Antworten fehlt, ist der Befund noch nicht ausgabereif.

## Teil K — Vertiefte Dogmatik

### K.1 — Vertragstyp und Mischrecht

Der Bauträgervertrag ist kein bloßer Kaufvertrag und kein bloßer Werkvertrag. § 650u BGB spaltet:

- Errichtung/Umbau: Bauvertragsrecht, soweit nicht ausgeschlossen.
- Eigentums-/Erbbaurechtsübertragung: Kaufrecht.
- Abschlagszahlungen: § 650v BGB und MaBV.
- AGB: §§ 305 ff. BGB überlagern die Vertragsgestaltung.

Prüfe deshalb nie nur eine Normschiene. Bei einer Wohnungseigentumseinheit wird der Vertragsgegenstand zusätzlich durch Teilungserklärung, Gemeinschaftsordnung, Aufteilungsplan, Baubeschreibung und Pläne geprägt. Bei Altbau- oder Sanierungsobjekten ist zu trennen: Sind die Sanierungsleistungen nach Umfang und Bedeutung neubaugleich, kann Werkvertragsrecht auch auf nicht unmittelbar angefasste Altbausubstanz ausstrahlen; bei bloßer Renovierung bleibt Werkvertragsrecht auf die konkret übernommenen Arbeiten begrenzt.

Abgrenzung:

| Struktur | Kein Bauträgervertrag, wenn … | Skill-Folge |
| --- | --- | --- |
| Generalunternehmer/Generalübernehmer | kein Eigentum oder Erbbaurecht verschafft wird | Werk-/Bauvertragsrecht ohne MaBV-Bauträgerlogik prüfen |
| Baubetreuer | der Erwerber/Bauherr im eigenen Namen Verträge schließt und der Betreuer nur organisiert | Vollmachten, Finanzierungsmittel und § 650f-Ausnahme gesondert prüfen |
| Projektsteuerer | nur Koordination/Controlling ohne eigene Bauherstellung und Eigentumsverschaffung übernommen wird | Leistungsbild, Haftung und Berichtspflichten prüfen |
| Baugruppen-GbR | mehrere Bauherren gemeinsam Grundstück und Bauleistung strukturieren | Teil M.7 anwenden; MaBV nicht anwenden |

### K.2 — Beurkundungsreichweite

Der Bauträgervertrag ist nach § 311b Abs. 1 BGB insgesamt notariell zu beurkunden. Nicht nur die Grundstücksübertragung, sondern auch alle werkvertraglichen Herstellungspflichten und wirtschaftlich zusammenhängenden Nebenabreden müssen in die Beurkundung oder in eine wirksame Bezugsurkundenstruktur. Maßgeblich ist nicht, was die Parteien formal beurkunden wollten, sondern was aus Sicht des Geschäfts wirtschaftlich zusammengehört.

Mitzubeurkunden oder als Bezugsurkunde sauber einzubeziehen sind insbesondere:

- Baubeschreibung mit Datum und Version.
- Planlisten, Aufteilungspläne, Ausführungs-/Grundrisspläne, soweit sie das Bausoll bestimmen.
- Teilungserklärung, Gemeinschaftsordnung, Nachträge, Sondernutzungsrechte.
- Vorverträge, Options- und entgeltliche Reservierungsvereinbarungen, wenn sie Erwerbsdruck erzeugen.
- Abreden über Vorausleistungen auf den späteren Bauträgervertrag.
- Sonderwünsche vor Beurkundung, soweit sie Preis, Leistung, Fläche, Sondereigentum oder Bauablauf prägen.

Bezugsurkunden nach § 13a BeurkG können Baubeschreibung, Pläne und Teilungserklärung praktikabel auslagern. Das ist kein Freibrief:

| Punkt | Skill-Prüfung |
| --- | --- |
| Bezeichnung | Ist die Bezugsurkunde mit Datum, Notar/UR-Nr., Planstand und Anlagenliste eindeutig identifizierbar? |
| Belehrung | Erstreckt sich die notarielle Belehrung nach § 17 BeurkG auch auf die Bezugsurkunde und ihre Risiken? |
| Wesentlichkeit | Werden echte Hauptpflichten nur versteckt ausgelagert, ohne in der Urkunde verständlich aufzuscheinen? |
| Zugriff | Hatte der Verbraucher den Text rechtzeitig und vollständig vor Beurkundung? |
| Widersprüche | Gibt es Rangregeln zwischen Urkunde, Baubeschreibung, Plänen, Prospekt und Teilungserklärung? |

Folgen fehlender Beurkundung sind streng zu prüfen: Verletzung der Form kann Nichtigkeit nach § 125 Satz 1 BGB i. V. m. § 311b Abs. 1 BGB auslösen; Heilung kommt grundsätzlich erst durch Auflassung und Eintragung in Betracht. Im laufenden Erwerbermandat bedeutet das: Nicht sofort mit Gesamtnichtigkeit drohen, sondern zuerst Vertragsstand, Vollzug, Eintragung und den konkreten fehlenden Bestandteil bestimmen.

Sonderwünsche:

| Zeitpunkt | Folge |
| --- | --- |
| vor Beurkundung vereinbart | grundsätzlich mitbeurkunden und in Gesamtpreis/Ratenplan einordnen |
| nach Beurkundung, ohne Grundstücks-/Sondereigentumsänderung | regelmäßig formfrei möglich, aber MaBV- und Gewährleistungslogik beachten |
| nach Beurkundung mit Änderung von Sondereigentum, Miteigentumsanteil oder Teilungserklärung | neue Beurkundungspflicht prüfen |
| Abrechnung außerhalb MaBV-Ratenplan | 🔴, wenn bauwerksbezogene Leistung vorab bezahlt werden soll |

VOB/B und Koppelungen: Eine formularmäßige Einbeziehung der VOB/B gegenüber Verbrauchern ist kein Schutzschild gegen AGB-Kontrolle. Koppelungen des Erwerbs an weitere Verträge, insbesondere Erstverwalter-, Wartungs-, Contracting- oder Finanzierungsbindungen aus dem Verkäuferumfeld, sind auf Druckwirkung, Transparenz und sachlichen Grund zu prüfen.

### K.3 — Bezugsfertigkeit, Abnahme, vollständige Fertigstellung

Nicht vermengen:

| Begriff | Bedeutung |
| --- | --- |
| Bezugsfertigkeit | Objekt kann sicher und zumutbar genutzt werden; Restarbeiten können offen sein. |
| Abnahme | Anerkennung als im Wesentlichen vertragsgerecht; Vorbehalte möglich. |
| Vollständige Fertigstellung | Alle geschuldeten Leistungen und je nach Vertrag auch protokollierte Restmängel erledigt. |

BGH VII ZR 88/25 ist hier der starke Anker: Die Schlussrate hängt am konkreten Vertragswortlaut, nicht an einer abstrakten Gleichsetzung von Abnahme und vollständiger Fertigstellung.

Bezugsfertigkeit setzt nicht nur vier Wände und Sanitärnutzung voraus. Der Zugang zur Einheit muss verkehrssicher und zumutbar sein. Fehlende Treppengeländer, offene Schächte, provisorische Bretterbrücken, ungesicherte Baustellenwege, fehlende Beleuchtung in zentralen Zugangsbereichen oder nicht nutzbare Rettungswege sind deshalb als harte Bezugsfertigkeits- und Besitzübergaberisiken zu prüfen.

### K.4 — Nachzügler

Erwerber, die nach einer vermeintlichen Abnahme des Gemeinschaftseigentums kaufen, sind nicht automatisch an eine frühere Abnahme gebunden. Formularmäßige Klauseln wie `Abnahme ist erfolgt` sind hoch angreifbar, wenn eigene Prüf- und Abnahmerechte fehlen.

Amtliche BGH-Anker: VII ZR 49/15 erklärt eine Nachzüglerklausel, die spätere Erwerber an eine frühere Abnahme des Gemeinschaftseigentums bindet, wegen mittelbarer Verkürzung der Verjährung nach § 309 Nr. 8 lit. b ff BGB für unwirksam. VII ZR 171/15 bestätigt zusätzlich, dass eine Ingenieurbüro- oder Beschlussabnahme aus einer Zeit, in der der Nachzügler weder Wohnungseigentümer noch werdender Wohnungseigentümer war, keine Abnahmewirkung zu seinen Lasten entfaltet; für neu errichtete Eigentumswohnungen bleibt Werkvertragsrecht grundsätzlich relevant, auch wenn das Bauwerk bei Vertragsschluss bereits fertiggestellt ist.

Prüfraster:

| Konstellation | Einordnung |
| --- | --- |
| Erwerb kurz nach Errichtung, Arbeiten vor Vertragsschluss bereits ausgeführt | werkvertragliche Mängelrechte nicht vorschnell ausschließen; förmliche Abnahme mit Nachzügler vereinbaren und durchführen |
| Erwerb nach längerer Vermietung, Richtwert drei Jahre nach Errichtung als Warnsignal | Kaufrechtsnähe prüfen; keine automatische Bauträger-Werkvertragslogik behaupten |
| Vertrag enthält `Käufer erkennt frühere Abnahme an` | 🔴, wenn als AGB ohne eigenes Prüf-/Abnahmerecht |
| Vertrag will innerhalb kurzer Zeit nach Fertigstellung Kaufrecht statt Werkvertragsrecht vereinbaren | 🟠/🔴; Verbraucherleitbild, Umgehung und Transparenz prüfen |

Ausgabe: Beim Nachzügler immer Vertragsdatum, Fertigstellungs-/Übergabedatum, vorherige Nutzung/Vermietung, Abnahmeakte der GdWE und konkrete Klausel zitieren. Keine abstrakte Aussage `Nachzügler haben immer Werkvertragsrecht`.

### K.5 — Verzug

Für Verzug braucht es:

1. fällige Leistung.
2. Nichtleistung.
3. Mahnung oder Entbehrlichkeit.
4. Vertretenmüssen, soweit erforderlich.

Pauschale Entlastungen (`Witterung`, `Materialmangel`, `Behörden`, `Generalunternehmer`) reichen nicht. Der Bauträger muss bauablaufbezogen erklären, welches Ereignis welche konkrete Verzögerung verursacht hat.

Bei kalendarisch bestimmten Fertigstellungsterminen ist die Mahnung nach § 286 Abs. 2 Nr. 1 BGB entbehrlich. Wird der Termin später einvernehmlich verschoben, ist zu prüfen, ob für den neuen Termin erneut ein kalendermäßiger Leistungszeitpunkt vereinbart wurde oder ob Mahnung/Fristsetzung nötig wird.

§ 313 BGB ist als Bauträger-Einwendung streng zu behandeln: War die behauptete Krise bei Vertragsschluss bereits eingetreten oder absehbar, trägt der Bauträger das Kalkulations- und Organisationsrisiko grundsätzlich selbst. Nach Verzugseintritt eintretende Ereignisse entlasten nicht pauschal; mindestens braucht es einen gesonderten bauablaufbezogenen Nachweis, dass gerade dieses Ereignis die weitere Fertigstellung selbständig verzögert hat.

Restvergütung/Widerklage des Bauträgers: Schluss- oder Restzahlung ist nur fällig, wenn Abnahme vorliegt oder die Abnahmefiktion nach § 640 Abs. 2 BGB greift. Beim Verbraucher muss die Aufforderung die besondere Textformbelehrung enthalten; bereits ein konkret benannter Mangel kann die Fiktion hindern. Ohne Abnahme/Fiktion keine automatische Fälligkeit nach § 641 BGB.

### K.6 — Vertragsstrafe und pauschalierter Schadensersatz

Trennen:

- Vertragsstrafe: Druckmittel, meist verschuldensabhängig, AGB-Höhenkontrolle.
- Pauschalierter Schadensersatz: § 309 Nr. 5 BGB, Nachweis geringeren Schadens muss offenbleiben.
- Weitergehender Schaden: darf nicht formularmäßig unangemessen ausgeschlossen werden.

Verzugsschäden bei verspäteter Übergabe sind konkret zu erfassen, nicht pauschal als `Nutzungsausfall`:

| Schadensposition | Prüfpunkt |
| --- | --- |
| Ersatzwohnung | ortsübliche Miete, Zeitraum, Angemessenheit, Belege |
| Umzugskosten | Hin- und Rückumzug, Einlagerung, doppelte Organisation |
| Lagerkosten | nur für nicht unterbringbares Mobiliar; Zeitraum und Rechnung |
| Bereitstellungszinsen | nur für noch nicht abgerufene Darlehensvaluta; kein Sowieso-Schaden, aber von Zinsen auf bereits ausgezahlte Valuta trennen |
| doppelte Miete | Unkündbarkeit oder Zumutbarkeit der Altwohnung prüfen |
| Hotel-/Zwischenunterkunft | Erforderlichkeit und Dauer plausibilisieren |
| Nutzungsausfallschaden | nur bei fühlbarer Gebrauchsbeeinträchtigung; Größenunterschied oder Komfortmangel allein genügt nicht sicher |

Vertragsstrafe und Schadensersatz: Bei Interessenidentität wird die Vertragsstrafe nach § 341 Abs. 2 i. V. m. § 340 Abs. 2 BGB auf den weitergehenden Schaden angerechnet. Zinsen im Prozess: § 291 BGB ab Rechtshängigkeit, § 289 BGB gegen Zinseszins und § 308 ZPO zur Antragsbindung beachten.

### K.7 — Verjährung bei unwirksamer Abnahme

Bei unwirksamer Abnahmeklausel beginnt die typische Gewährleistungsverjährung nicht normal zu laufen. Die BGH-Entscheidungen VII ZR 68/24 und VII ZR 108/24 setzen zugleich eine 30-Jahres-Obergrenze für dortige Kostenvorschusskonstellationen. Nicht unbesehen auf jede Anspruchsart übertragen; Anspruch, Rechtstand und Vertragsschlussdatum prüfen.

OLG Stuttgart 10 U 4/25 mit einer 15-Jahres-Linie ist nach den BGH-Entscheidungen vom 26.03.2026 nur noch als Instanz- und Konfliktmarker zu behandeln. Wenn dieselbe Kostenvorschuss-Konstellation einer unwirksamen Bauträger-Abnahme des Gemeinschaftseigentums vorliegt, trägt die 30-Jahres-Obergrenze des BGH. Wenn Anspruchsart, Zeitraum, tatsächliche Abnahmeerklärung oder Verjährungseinrede anders liegen, wird der Unterschied ausdrücklich offengelegt statt schematisch die längere Frist zu behaupten.

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
- keine Selbstwiderlegung durch längeres Zuwarten, wenn Dringlichkeit behauptet wird.

Anspruchsrichtung sauber formulieren: Besitzverschaffung setzt regelmäßig unstreitige oder glaubhaft gemachte Bezugsfertigkeit, Erfüllung der fälligen Zahlungen oder ein annahmeverzugsbegründendes Zahlungs-/Hinterlegungsangebot und keine durchgreifenden Gegenrechte voraus. Das Verfahren darf die Hauptsache nicht ohne tragfähige Eilgrundlage vorwegnehmen.

### K.10 — § 650m-Sicherheit und Vormerkung

Vormerkung und 5 %-Sicherheit schützen unterschiedliche Risiken:

| Schutz | Deckt ab | Deckt nicht ab |
| --- | --- | --- |
| Vormerkung | Eigentumsübertragungsanspruch | Fertigstellungs-/Mängelrisiko |
| MaBV-Ratenplan | Keine Zahlung ohne Baufortschritt/Sicherung | Mängel nach Abnahme nur begrenzt |
| § 650m Abs. 2 | rechtzeitige Herstellung ohne wesentliche Mängel | alle sonstigen Schäden automatisch |
| § 7 MaBV | Rückgewähr-/Auszahlungsansprüche | Qualitätsstreit ohne Sicherungsfall |

Auflassungsvormerkung: Sie schützt den Übereignungsanspruch, auch insolvenzfest in der Logik des § 106 InsO. Sie schützt nicht die Bauvollendung, nicht die Mangelfreiheit, nicht Mehrkosten der Fertigstellung und nicht alle Schadensersatzpositionen.

§ 650m Abs. 2 BGB: Beim Verbraucher-Bauträgervertrag zwingend mitzudenken. Verzicht, bloß fakultativer Einbehalt oder Kostenbelastung des Erwerbers für die Sicherheit sind rot zu prüfen.

§ 7 MaBV-Bürgschaft: Sie ist Alternative zur § 3-MaBV-Ratenabwicklung, nicht dekorativer Zusatz. Häufig sichert sie Rückgewähr-/Auszahlungsansprüche, aber nicht jeden Schadensersatz wegen Mängeln oder Verzugs. Bürgschaftstext, Dauer, Bürge, Kündbarkeit und Sicherungsfall wörtlich auswerten.

Insolvenzlogik: Der Grundstücksanspruch ist über die Vormerkung zu sichern; der Werkleistungsanspruch kann in die Wahlrechtslogik des Insolvenzverwalters nach § 103 InsO geraten. Mandatsschritte: Vormerkung und Rang prüfen, Freistellungserklärung beschaffen, Insolvenzverwalter zur Erklärung auffordern, § 7-Sicherheit in Anspruch nehmen, § 650m-Sicherheit festhalten, Mehrkosten der Fertigstellung und Geschäftsführerhaftung gesondert prüfen.

### K.11 — Geschäftsführer, Vertrieb, Dritte

Nicht vorschnell persönliche Haftung behaupten. Prüfe sauber:

- eigene Täuschungshandlung.
- Prospekthaftung/Vertriebsunterlagen.
- Deliktischer Schaden.
- Vertreterwissen.
- Insolvenzverschleppung nur mit konkreten Tatsachen.

Bei MaBV-Verstößen in der Vorinsolvenzphase zusätzlich prüfen:

| Anspruchsgegner | Ansatz |
| --- | --- |
| Geschäftsführer der Bauträger-GmbH | § 823 Abs. 2 BGB i. V. m. § 3 oder § 7 MaBV als Schutzgesetz; Vorsatz, mindestens bedingter Vorsatz, konkret anhand operativer Rolle, Zahlungsanforderung und Kenntnis prüfen |
| Geschäftsführer/Vertrieb | § 823 Abs. 2 BGB i. V. m. § 263 StGB, wenn vorzeitig fällige Raten mit Täuschung über Fälligkeit, Baufortschritt oder Sicherheit vereinnahmt werden |
| Architekt/Bauleiter/Projektsteuerer | Vertrag mit Schutzwirkung zugunsten Dritter prüfen, wenn Bautenstandsbestätigungen erteilt werden und der Erwerber gerade darauf zahlt |
| Vertrieb/Prospektverantwortliche | Prospekt-/Aufklärungshaftung prüfen, wenn Baugrund, Energie, Schall, Fertigstellung oder Sicherheit vertriebsseitig falsch dargestellt wurden |

Output-Regel: Persönliche Haftung nie als Drohkulisse formulieren. Immer Tatsachenanker nennen: wer hat welche Zahlungsanforderung, Bautenstandsbestätigung oder Freistellungsaussage wann gegenüber welchem Erwerber verwendet?

### K.12 — Notar in Serienprojekten

Serienbeurkundung ist nicht automatisch pflichtwidrig. Kritisch wird es, wenn:

- Entwürfe zu spät kommen.
- Bezugsurkunden fehlen.
- der Notar erkennbare AGB-/MaBV-Risiken nicht belehrt.
- der Notar pauschale Bestätigungen protokolliert, die echte Belehrung ersetzen sollen.
- Verbrauchereinwände nicht dokumentiert werden.

Notarhaftung nach § 19 BNotO ist bei Fahrlässigkeit grundsätzlich subsidiär, bei Vorsatz nicht in gleicher Weise auf anderweitigen Ersatz zu verweisen. Für den Skill gilt:

| Pflichtfeld | Konkret zu prüfen |
| --- | --- |
| § 17 BeurkG | Belehrung über rechtliche Tragweite, insbesondere MaBV-Fälligkeit, Sicherheiten, Vormerkung, Freistellung, Abnahme und Preisanpassung |
| § 14 BNotO | unparteiische Amtsführung; keine bloße Durchleitung bauträgerseitiger Druckmuster |
| AGB-/MaBV-Kontrolle | erkennbare Unwirksamkeitsrisiken nicht ignorieren; bei kritischen Klauseln dokumentiert belehren |
| Niedriger Grundstücksanteil/erste Rate | örtliches Preisniveau und Überzahlung in der ersten MaBV-Rate als Warnpunkt prüfen |
| Freistellungserklärung | Inhalt, steckengebliebener Bau, Lastenfreistellung und Aussetzung der Fälligkeit verständlich machen |
| Preisanpassung | Erhöhungsrisiko, Lösungsrecht, Saldierung und Sicherung offenlegen |

Prozessstrategie: Bei fahrlässiger Notarpflichtverletzung in einem Prozess gegen Bauträger/Geschäftsführer an Streitverkündung denken. Bei belastbaren Vorsatzindizien kann eine Klageerweiterung oder gesonderte Inanspruchnahme zu prüfen sein. Keine Notarhaftung behaupten, ohne Urkundenstand, Belehrungsprotokoll, Kenntnislage und anderweitige Ersatzmöglichkeiten konkret zu erfassen.

## Teil L — Drei-Dokumente-Paket

Wenn der Nutzer das Vollpaket verlangt oder in der Nächsten Weiche `G — Vollpaket` wählt, mündet die Analyse zwingend in drei getrennte Dokumente. Keine Vermischung der Sprachregister. Wenn der Nutzer nur geführt prüfen will, darf Teil L abschnittsweise über die Weiche aufgerufen werden. Jedes Dokument beginnt mit seiner festen Überschrift (`Dokument 1`, `Dokument 2`, `Dokument 3`), damit Fortsetzungen und Copy/Paste in Kanzlei- oder Mandantenakten nicht durcheinanderlaufen.

### L.1 — Dokument 1: Übersendungsschreiben / Informationsschreiben an den Mandanten

Ziel: Der Verbraucher versteht in fünf Minuten, ob er unterschreiben, verschieben, nachverhandeln, zahlen, einbehalten, abnehmen oder streiten soll. Das Schreiben ist als Kanzlei-/Mandantenanschreiben formuliert und verweist bei einer separaten Datei auf das beigefügte, bei einer fortlaufenden Chat-Ausgabe auf das nachfolgende Gutachten.

Aufbau:

```text
Betreff: Prüfung Bauträgervertrag [Projektname, Haus/Einheit/Stellplatz, Entwurfsdatum oder UR-Nr.] - Übersendung der ersten Einschätzung und des Gutachtens

Sehr geehrte/r [Mandant/in],

[Bei separater Anlage:] Anbei erhalten Sie die Prüfung des Bauträgervertrags [Projekt/Haus/Einheit].
[Bei Ausgabe im selben Text:] Nachfolgend erhalten Sie die Prüfung des Bauträgervertrags [Projekt/Haus/Einheit].
Kurz zusammengefasst:

1. Ergebnis in einem Absatz
2. Ampel-Bilanz
3. Die wichtigsten drei bis sieben Risiken
4. Was das praktisch für Zahlung, Beurkundung, Abnahme oder Besitzübergang bedeutet
5. Nächste Schritte mit konkreten Fristen
6. Hinweis auf das beigefügte oder nachfolgende Gutachten
7. Offene Unterlagen/Fragen
```

Pflichtinhalte, wenn einschlägig:

- Kein 14-Tage-Widerruf versprechen, wenn ein beurkundeter Bauträgervertrag vorliegt und § 650l BGB durch § 650u Abs. 2 BGB ausgeschlossen ist.
- Bei Preisanpassung die mögliche Mehrbelastung in Euro/Bandbreite und die fehlende Sicherheit verständlich ausweisen.
- Bei Terminverzug die Bauablauf-Darlegung und konkrete Schadenspositionen erklären, nicht nur `Verzug liegt vor`.
- Bei unwirksamer Abnahme die Folge für Verjährung und 30-Jahres-Obergrenze als anspruchsbezogenes Prüfthema darstellen, nicht als pauschales Versprechen.
- Bei Technik/Baugrund benennen, welche Unterlage fehlt und warum das für genau dieses Haus, diese Tiefgarage, diese Außenanlage oder diese Einheit relevant ist.

Stil:

- einfache Sprache.
- keine langen Normketten.
- klare Handlungsempfehlung.
- keine falsche Sicherheit.

### L.2 — Dokument 2: Mandantengutachten

Ziel: ausführliche, belastbare rechtliche und technische Arbeitsfassung für den Mandanten. Das Gutachten ist das Hauptdokument der Prüfung; es trägt das Mandantenanschreiben und das außergerichtliche Aufforderungsschreiben an den Bauträger. Es darf nicht auf eine Ampeltabelle oder Klauselliste schrumpfen. Die Tabelle ordnet, aber die tragende Arbeit liegt in der abschnittsweisen Begründung.

Aufbau:

```text
A. Sachverhalt und geprüfte Unterlagen
B. Quellenstand
C. Fall-Fingerabdruck
D. Vertragsart und Verbraucherstatus
E. Pflicht-Prüfblock
F. MaBV und Zahlungsplan
G. AGB-Klauselmatrix
H. Baubeschreibung/Bausoll
I. Abnahme, Schlussrate, Mängelrechte
J. HOAI/Objektüberwachung/technische Projektrisiken
K. Wirtschaft/Organisation/WEG
L. Eigentumsschutz/Insolvenz
M. Bauzeitverzug, Vertragsstrafe, Nutzungsausfall und Restvergütung
N. Notar-, Geschäftsführer-, Bauleiter- und Vertriebsrisiken
O. Gesamteinschätzung
P. Konkrete Änderungsfassung und Verhandlungsauftrag
Q. Beweis- und Durchsetzungslandkarte
R. Priorisierte Unterlagen- und To-do-Liste
```

Mindesttiefe: Jeder rote oder orange Kernbefund wird in einem eigenen Absatz durchsubsumiert. Der Absatz nennt (1) die konkrete Vertragsstelle, (2) die wirtschaftliche oder technische Wirkung für genau diese Einheit/dieses Projekt, (3) Norm, verifizierte Quelle oder klar gekennzeichneten Prüfbedarf, (4) Rechtsfolge oder Verhandlungsziel, (5) erwartbares Gegenargument des Bauträgers und (6) die Antwort darauf. Bei sehr langen Verträgen sind mindestens die zehn wichtigsten Befunde vollständig auszuarbeiten; weitere Befunde dürfen tabellarisch folgen, müssen aber mit Fortsetzungsauftrag gekennzeichnet werden.

Jeder rote Befund braucht Norm, Fundstelle oder klare Argumentationslinie. Nicht quellenhart verifizierte Rechtsprechungslinien werden als Prüfbedarf gekennzeichnet; keine Entscheidung, kein Datum und kein Aktenzeichen werden aus Modellwissen ergänzt. Das Gutachten schreibt für den Käufer, nicht für ein Lehrbuch: Es erklärt, warum genau diese Rate, diese Abnahmeklausel, diese Baubeschreibungslücke, diese Bauüberwachungsregel oder diese Vollmacht im konkreten Vertrag praktisch gefährlich ist.

Der Abschnitt `B. Quellenstand` enthält eine kurze Quellenhierarchie: BGH/amtliche Bundesquelle zuerst, dann amtliche Landesrechtsprechung von KG/OLG/LG, danach DeJure/OpenJur als frei zugängliche Navigations- und Volltextanker. Wenn eine KG-/OLG-Entscheidung nur eine Instanzlinie bildet oder mit neuerer BGH-Rechtsprechung zu gewichten ist, wird das offen gesagt; sie wird nicht als gleichrangige höchstrichterliche Regel ausgegeben.

Pflichtabschnitt im Gutachten: **Beweis- und Durchsetzungslandkarte.** Für die wichtigsten Befunde wird knapp ausgewiesen:

- Anspruch oder Einwendung: Zahlung verweigern, Einbehalt, Streichung, Neufassung, Unterlagenherausgabe, Mängelrecht, Schadensersatz, Besitz, Abnahmevorbehalt.
- Darlegungs-/Beweislast: Wer trägt im Streit die Tatsachen für Fälligkeit, Bautenstand, Abnahme, Vertretenmüssen, Mangel, Technikstandard oder Individualabrede?
- Erforderliche Belege: Urkunde, Ratenanforderung, Freistellungserklärung, Bautenstandsfotos, Abnahmeprotokoll, Baugrundgutachten, Fachplanerbestätigung, Energie-/Schall-/Brandschutznachweis, Korrespondenz.
- Taktik: sofort vor Beurkundung, vor Zahlung, vor Abnahme, nach Abnahme oder im Streitverfahren verwertbar.

Das Gutachten endet mit einem phasengerechten Verhandlungs- und Durchsetzungsauftrag: Welche Klauseln vor Beurkundung gestrichen oder ersetzt werden müssen, welche Rechtsfolgen nach Beurkundung geltend zu machen sind, welche Unterlagen vor Zahlung oder Abnahme vorzulegen sind und welche Punkte nur 🟠 zu verhandeln bleiben.

### L.3 — Dokument 3: Außergerichtliches Aufforderungsschreiben an den Bauträger

Ziel: bestimmte, verhandlungsfähige Aufforderung an den Bauträger/Verkäufer mit der zur Vertragsphase und Ampel passenden Rechtsfolge. Vor Beurkundung werden notwendige Vertragsänderungen verlangt. Nach Beurkundung werden keine bloßen Entwurfswünsche formuliert, sondern Nichtanwendung einer unwirksamen Klausel, Erfüllung, Unterlagen, Fälligkeit, Einbehalt, Mängelbeseitigung, Fristsetzung oder ein erforderlicher notarieller Nachtrag. Reine 🟠-Punkte werden als Klarstellungs- oder Verhandlungswünsche formuliert. Fehlen 🔴/🟠-Punkte, wird ausdrücklich keine zwingende Korrektur verlangt. Jede Forderung nennt kurz das Problem, die rechtliche/technische Begründung und die richtige Fassung oder Handlung. Das Notariat ist nicht Standard-Hauptadressat; es wird nur in Kopie gesetzt oder mit einem eigenen kurzen Zusatz angesprochen, soweit Urkundsgestaltung, Belehrung, Vollzug, Treuhandabwicklung, Vormerkung, Lastenfreistellung oder Beurkundungsreife betroffen sind.

Aufbau:

```text
An: [Bauträger/Verkäufer]
Kopie: [Notariat nur bei Beurkundungs-, Vollzugs- oder Belehrungspunkt]

Betreff: Bauträgervertrag [Projektname, Haus/Einheit/Stellplatz, Entwurfsdatum oder UR-Nr.] - [Anpassungen vor Beurkundung / Klärung von Fälligkeit und Sicherheiten / Mängel und Abnahme / außergerichtliche Anspruchsdurchsetzung]

Sehr geehrte Damen und Herren,

[Entwurfsphase:] Der von Ihnen vorgelegte Entwurf ist in folgenden Punkten vor Beurkundung anzupassen.
[Nach Beurkundung:] Der am [Datum] beurkundete Vertrag bedarf in folgenden Punkten der rechtlichen und tatsächlichen Klärung. Soweit eine Klausel unwirksam oder eine Forderung nicht fällig ist, wird ihre Nichtanwendung beziehungsweise die Zurücknahme der Zahlungsanforderung verlangt. Soweit eine wirksame Vertragsänderung erforderlich ist, bitten wir um einen notariell beurkundungsfähigen Nachtrag; dieses Schreiben ersetzt ihn nicht.

Die notarielle Form ersetzt nicht die AGB-Inhaltskontrolle. Zwingende MaBV- und Verbraucherschutzvorgaben stehen nicht zur Disposition.

1. [Paragraph/Absatz/Baubeschreibungsabschnitt] - [konkretes Problem]
Original: [maßgeblicher Wortlaut]
Warum das so nicht geht: [kurze Begründung mit Norm/Argumentationslinie]
Gegenargument: [...]
Antwort: [Antwort auf das konkrete Gegenargument]
Verlangte Abhilfe: [voller Ersatzwortlaut oder Streichungsanweisung vor Beurkundung / Nichtanwendungsbestätigung, Leistung, Unterlage, Frist oder notarieller Nachtrag nach Beurkundung]

Frist / weiteres Vorgehen

[Nur falls einschlägig, Entwurfsphase:]
Hinweis an das Notariat: Die nachfolgend bezeichneten Punkte betreffen auch Beurkundungsreife oder Belehrung. Wir bitten, den Entwurf bis zur Klärung nicht als beurkundungsreif zu behandeln.

[Nur falls einschlägig, nach Beurkundung:]
Hinweis an das Notariat: Die nachfolgend bezeichneten Punkte betreffen den Vollzug, die Fälligkeitsmitteilung, die Treuhandabwicklung oder einen formgerechten Nachtrag. Wir bitten, den Vollzugsschritt bis zur Klärung nicht auf die beanstandete Voraussetzung zu stützen.
```

Ton:

- bestimmt.
- keine Übertreibung.
- keine pauschalen Nichtigkeitsdrohungen.
- bei § 306 BGB klar: unwirksame AGB fallen weg; Gesetz gilt.
- immer konkrete Fassung liefern: bloß `bitte anpassen` genügt nicht.
- keine formlose Vertragsänderung als rechtssicher darstellen, wenn § 311b BGB oder die Änderung von Sondereigentum, Miteigentumsanteilen, Teilungserklärung, Leistung oder Gegenleistung eine notarielle Beurkundung erfordern kann.

Pflichtforderungen, wenn die Klausel vorkommt:

- Preisanpassung ohne Lösungsrecht/Saldierung: streichen oder mit Preisvorbehalt nach billigem Ermessen, Kalkulationsoffenlegung, Saldierung und gesicherter Lösungsmöglichkeit neu fassen.
- Abnahme durch Erstverwalter, Tochtergesellschaft, Projektsteuerer, Sachverständigen oder Erwerbervertreter: streichen oder ausdrückliches Eigenrecht jedes Erwerbers auf Prüfung und persönliche Abnahme sichern.
- Vollständige Fertigstellung ohne Außenanlagen/Restarbeiten: Definition korrigieren; Schlussrate erst nach vollständiger Fertigstellung einschließlich geschuldeter Außenanlagen und Gemeinschaftseigentumsarbeiten.
- Bautenstandsmitteilung allein durch Bauträger/Bauleiter: objektive Prüfbarkeit, angemeldete Besichtigung und Hinzuziehung eigener Sachverständiger sichern.
- Freistellung, Vormerkung oder Löschungsvollmacht unklar: Zahlungsfälligkeit aussetzen und dingliche Sicherheit unangetastet lassen, bis objektive Voraussetzungen erfüllt sind.

### L.4 — Typische Gegenargumente und Antworten

| Gegenargument | Antwort |
| --- | --- |
| `Das ist Standard.` | Standardformulare sind gerade AGB und unterliegen §§ 305 ff. BGB. |
| `Der Notar hat es beurkundet.` | Beurkundung sichert die Form, nicht automatisch die AGB-Wirksamkeit. |
| `MaBV schützt doch schon.` | MaBV, § 650m Abs. 2 und AGB-Kontrolle schützen unterschiedliche Risiken. |
| `Der Erwerber hat alles bestätigt.` | Pauschale Tatsachenbestätigungen sind nach § 309 Nr. 12 lit. b BGB unwirksam. |
| `Das Projekt braucht Flexibilität.` | Flexibilität braucht konkret benannte triftige Gründe und darf Wert/Nutzung/Kosten nicht verschlechtern. |
| `Die Schlussrate ist wegen Abnahme fällig.` | Bei `vollständiger Fertigstellung` und offenen Protokollmängeln zuerst Fälligkeit nach Vertrag und BGH VII ZR 88/25 prüfen. |
| `Der Käufer kann keinen eigenen Bauüberwacher auf die Baustelle schicken.` | Freier Baustellenzutritt ist nicht geschuldet; eine sicherheitskonforme Begleitung eigener Sachverständiger zu Bautenstand, Abnahme und Mängelprüfung darf aber nicht formularmäßig ausgehöhlt werden. |
| `Die HOAI gilt nur für den Architektenvertrag.` | Richtig, aber die HOAI-Leistungsphasen sind ein fachlich anerkanntes Organisationsraster. Der Bauträger muss ein prüfbares Bausoll, Bauüberwachung und Dokumentation sicherstellen. |
| `Baugrund und Grundwasser sind Projektumstände.` | Gerade deshalb müssen Gutachten, Auflagen, Kosten- und Verzugsfolgen offengelegt und beim Bauträger als Herstellungsverpflichtetem verortet werden, soweit nichts konkret anderes vereinbart ist. |
| `Pandemie, Lieferkette oder Wetter erklären die Verzögerung.` | Allgemeine Störungen erklären nichts. Es braucht den Bauablaufplan, das konkrete Ereignis, betroffene Gewerke, Folgevorgänge, Wiederanlaufzeit und Nachweise. |
| `Der Käufer kann bei Preiserhöhung zurücktreten.` | Rücktritt kann den Vormerkungsschutz zerstören. Ein brauchbares Lösungsrecht muss bereits geleistete Zahlungen und den Eigentumssicherungsstatus absichern. |
| `Die § 7-MaBV-Bürgschaft reicht doch.` | Nur, wenn sie den konkreten Sicherungszweck, die Dauer und alle Rückgewähr-/Auszahlungsansprüche tatsächlich abdeckt; sie ersetzt nicht beliebig § 650m Abs. 2 BGB oder die § 3-MaBV-Fälligkeit. |
| `Sonderwünsche sind Privatsache und sofort zahlbar.` | Bauwerksbezogene Sonderwünsche dürfen die MaBV-Ratenlogik nicht umgehen; Zeitpunkt, Leistung, Gewährleistung, Bausoll und Ratenplan müssen zusammenpassen. |

### L.5 — Qualitätsgate für das Paket

- Zeigt der Statuskopf Dokument 1, 2 und 3 jeweils als `erledigt`, bevor die Ausgabe als abgeschlossen bezeichnet wird?
- Sind alle drei Dokumente getrennt?
- Enthält Dokument 1 ein echtes Übersendungsschreiben mit Hinweis auf das Gutachten?
- Verwendet Dokument 1 `beigefügt/anbei` nur bei einer echten Anlage und sonst `nachfolgend`?
- Stimmen Ampeln und Befunde überein?
- Hat Dokument 1 keine unnötigen Fachbegriffe?
- Hat Dokument 2 harte Quellen?
- Hat Dokument 3 zu jeder wesentlichen Forderung Problem, Kurzbegründung und konkrete richtige Fassung?
- Sind Gegenargumente vorweggenommen?
- Sind § 306 BGB und § 139 BGB sauber getrennt?
- Ist jeder Fachbefund mit Fallanker, Norm, Gegenargument und konkreter Änderung ausgegeben?
- Decken Dokument 1 bis 3 denselben priorisierten Befundbestand ab, ohne neue, unbegründete Ampeln erst im Bauträgerschreiben einzuführen?
- Stimmen Betreff, Forderungen und Rechtsfolgen in Dokument 3 mit der festgestellten Vertragsphase überein?
- Wird bei einem bereits beurkundeten Vertrag zwischen Klausel-Nichtanwendung, gesetzlicher Ersatzregel, Erfüllungsforderung und gegebenenfalls formbedürftigem Nachtrag unterschieden?
- Bleibt Dokument 3 im Positivfall frei von künstlichen Forderungen und trennt es reine 🟠-Verhandlungswünsche sprachlich von zwingenden 🔴-Korrekturen?

## Teil M — Vertiefte Dogmatik II

Teil M ergänzt die bisherige Karte um acht Themen, die in aktuellen Bauträgerstreitigkeiten regelmäßig den Ausschlag geben. Jeder Block ist als Werkzeug für die Klauselmatrix und für das Drei-Dokumente-Paket ausgelegt.

### M.1 — Anerkannte Regeln der Technik und DIN-Normen

Grundsatz: Ohne abweichende Vereinbarung schuldet der Bauträger als Mindeststandard die Einhaltung der anerkannten Regeln der Technik. Maßgeblich ist der Stand zum Zeitpunkt der Abnahme, nicht zum Vertragsschluss. Verstöße sind auch dann ein Mangel, wenn sich noch kein Schaden gezeigt hat.

Drei-Stufen-Modell der Technikbegriffe:

| Stufe | Anforderung | Typische Auswirkung |
| --- | --- | --- |
| Anerkannte Regeln der Technik | wissenschaftlich richtig anerkannt + in der Fachpraxis bewährt | werkvertraglicher Mindeststandard |
| Stand der Technik | aktueller Erkenntnisstand, Bewährung nicht erforderlich | umweltrechtlich, sicherheitsrechtlich, vertraglich nur bei ausdrücklicher Vereinbarung |
| Stand von Wissenschaft und Technik | theoretisch machbarer Spitzenstand | praktisch nur in Hochrisikobereichen geschuldet |

DIN-Normen und vergleichbare Regelwerke (VDI-Richtlinien, VDE-Bestimmungen) sind **keine** Rechtsnormen, sondern privatrechtliche Empfehlungen. In der bauvertragsrechtlichen Rechtsprechung des für Werkvertragsrecht zuständigen Zivilsenats gilt **keine Vermutung**, dass DIN-Normen die anerkannten Regeln der Technik wiedergeben. Im Einzelfall ist sachverständig zu prüfen, ob die jeweilige Norm den anerkannten Stand abbildet — oder nur einen Branchenkompromiss.

Senatsdifferenzierung als Quellenpflicht: Die Linie des für Grundstücks- und Wohnungseigentumssachen zuständigen Senats zu DIN-Normen im wohneigentumsrechtlichen Binnenverhältnis darf nicht in den Werkvertragsstandard des Bauträgervertrags hinübergezogen werden. Wenn eine Antwort sich auf diese Differenz stützt, wird sie vor Ausgabe live mit zulässiger Fundstelle verifiziert oder als Prüfbedarf markiert.

Bauträger-Klauselmuster und Befund:

| Klausel | Befund |
| --- | --- |
| „Anerkannte Regeln der Technik zum Vertragsschluss" | 🔴 (verschiebt das Risiko auf den Erwerber). Gewünscht: „zum Zeitpunkt der Abnahme". |
| „Anerkannte Regeln der Technik zum Tag der Baugenehmigung" | 🔴 (noch früherer Stichtag). |
| „DIN-Normen in der zum Vertragsschluss geltenden Fassung" | 🔴; DIN ist nicht automatisch anerkannte Regel der Technik. |
| „Energetische Anforderungen nach geltendem Recht" ohne konkrete Klasse | 🔴 (Bausoll-Lücke; gewünscht: KfW-/Effizienzhaus-Klasse oder vergleichbarer Standard). |
| Bedenken-/Aufklärungsklausel: Abweichung von aaRdT nur bei dokumentierter Belehrung | 🟢 (verhandlungsfähig). |

Verhaltensregel bei Änderung der anerkannten Regeln zwischen Vertragsschluss und Abnahme: Der Bauträger muss den Erwerber über die Änderung und die Folgen aufklären; der Erwerber wählt zwischen (a) Einhaltung des neuen Standards mit gegebenenfalls Mehrkostenabrechnung über die jeweils einschlägige Vergütungsregel und (b) Beschaffenheitsvereinbarung nach unten unter ausdrücklicher Inkaufnahme der Folgen. Beim Globalpauschalvertrag liegt das Risiko der zwischenzeitlichen Standardentwicklung grundsätzlich beim Bauträger; eine Anpassung nach den Grundsätzen über die Störung der Geschäftsgrundlage scheidet typisch aus.

In der Gewährleistungsphase richtet sich die Mängelbeseitigung nach den anerkannten Regeln **zum Zeitpunkt der Beseitigung**, nicht zum Zeitpunkt der Abnahme. Mehrkosten infolge gestiegener Anforderungen sind keine Sowieso-Kosten; ein bleibender Mehrwert kann eine Ausgleichspflicht des Erwerbers begründen.

Bedenkenhinweis: Der Bauträger kann Mängelrisiken aus ungeeigneten Vorleistungen, Eigenleistungen oder nachträglichen Erwerberwünschen nicht still auf den Erwerber verschieben. Er muss konkret, verständlich und dokumentiert warnen: welches Bauteil, welche Vorleistung, welche technische Regel, welche Folge für Gewährleistung, Termine und Kosten. Ohne solchen Hinweis bleibt die rote Ampel bestehen.

Bestandsobjekte und Sanierungen: Beim Altbau ist nicht automatisch Neubaustandard geschuldet. Entscheidend ist, welches Bauteil der Bauträger erneuert, welches System unangetastet bleibt, welche Sanierungsqualität versprochen wurde und ob die Sanierung nach Umfang und Bedeutung neubaugleich ist. Der Skill darf weder den Bestandscharakter gegen den Erwerber überdehnen noch unmögliche Neubaustandards für nicht bearbeitete Altsubstanz versprechen.

Sonderregel im wohnungseigentumsrechtlichen Binnenrecht: Der für Sachenrecht zuständige Senat zieht DIN-Normen — insbesondere zum Mindest-Schallschutz — als Auslegungshilfe heran. Diese Linie betrifft nachbarrechtliche Rücksichtnahmepflichten zwischen Wohnungseigentümern, **nicht** den bauvertragsrechtlichen Mindeststandard zwischen Bauträger und Erwerber. Eine Übertragung dieser Wohnungseigentums-Maßstäbe auf die Bauträger-Werkleistung ist unzulässig; der bauvertragsrechtliche Standard liegt regelmäßig höher als der wohneigentumsrechtliche Minimal-Schallschutz.

Für die Klauselmatrix folgt: Jede vom Bauträger formulierte Verengung der anerkannten Regeln der Technik auf einen früheren Stichtag, auf bloßen DIN-Verweis oder auf ein „mittlere Art und Güte"-Auffangregime ohne konkrete Mindestklasse ist als 🔴 zu führen, mit Verweis auf § 633 Abs. 2 BGB und das BGB-Werkvertragsverständnis vom Werkmangel.

### M.2 — Vollständige Fertigstellung nach § 3 Abs. 2 MaBV

Die letzte Rate (3,5 %) wird nicht schon bei Bezugsfertigkeit fällig, sondern erst bei vollständiger Fertigstellung. Vollständige Fertigstellung bedeutet: sämtliche vertraglich geschuldeten Leistungen erbracht — einschließlich der **Außenanlagen**, sonstiger Restarbeiten am Gemeinschaftseigentum und aller Bestandteile des Bausolls. Eine vertragliche Verengung des Begriffs (z. B. „Außenanlagen gehören nicht zur Fertigstellung") ist mit dem Schutzzweck der MaBV unvereinbar.

Wesentliche Mängel stehen der vollständigen Fertigstellung entgegen. Bei unwesentlichen Mängeln und Protokollmängeln zuerst den Vertrag auslegen: Bindet der Vertrag die letzte Rate an die Beseitigung protokollierter Mängel/Restarbeiten, kann bereits die Fälligkeit fehlen (BGH VII ZR 88/25). Fehlt eine solche Fälligkeitsbindung und ist das Werk abnahmereif, ist KG 21 U 44/22 nur ein Instanzargument dafür, die Schlussrate nicht schon wegen einzelner Protokollmängel als unfällig zu behandeln; dann bleiben insbesondere § 641 Abs. 3 BGB, § 320 BGB und ein sauber bezifferter Einbehalt zu prüfen.

Für die Bezugsfertigkeitsrate gilt ein eigener Maßstab: Dauerhafte Bewohnbarkeit verlangt mehr als faktische Betretbarkeit oder vorübergehende Nutzung. Wesentliche Mängel können die Bezugsfertigkeit auch dann hindern, wenn sie vor allem optisch wirken, sofern das betroffene Gestaltungselement nach Vertrag, Prospekt, Baubeschreibung oder Bemusterung prägend ist (KG 21 U 156/24). Der Skill darf daher weder jede optische Abweichung bagatellisieren noch jede Restarbeit automatisch zur Fälligkeitssperre machen; entscheidend sind Vertragsprägung, Zumutbarkeit, Abnahmereife und eine etwaige Unverhältnismäßigkeitseinrede.

Zentrale Praxisaussagen:

| Konstellation | Folge |
| --- | --- |
| Schlussrate vor vollständiger Fertigstellung angefordert | 🔴; verstoßen wird gegen § 3 Abs. 2 MaBV i. V. m. § 12 MaBV, § 134 BGB; die Annahme ist verboten, gezahlte Beträge können nach § 817 Satz 1 i. V. m. § 818 Abs. 2 BGB zurückverlangt werden |
| „Außenanlagen außerhalb der Fertigstellungsrate" | 🔴; Außenanlagen gehören zur Fertigstellung, soweit vertraglich geschuldet |
| „Vollständig fertiggestellt" wenn Bezugsfertigkeit + Schlüsselübergabe vorliegt | 🔴; Fertigstellung ≠ Bezugsfertigkeit |
| Wesentliche Mängel am Gemeinschaftseigentum noch offen | Fertigstellungsrate nicht fällig, Rückforderbarkeit gegebener Zahlungen |
| Nur unwesentliche Protokollmängel | Vertrag zuerst auslegen: bei ausdrücklicher Beseitigungspflicht kann die Schlussrate noch nicht fällig sein; bei abnahmereifem Werk ohne Fälligkeitsbindung mindestens Zurückbehaltungsrecht nach § 641 Abs. 3 BGB |
| Bezugsfertigkeitsrate trotz wesentlichem optischem Vertragsmangel | 🔴/🟠; KG 21 U 156/24 prüfen: dauerhafte Bewohnbarkeit, Vertragsprägung, Abnahmeverweigerung und § 635 Abs. 3 BGB sauber trennen |
| Aufspaltung der Fertigstellungsrate in zwei Stufen (z. B. 2 % + 1,5 %) zur Sicherung definierter Restarbeiten | grundsätzlich denkbar; in einem klar abgegrenzten Sieben-Raten-Plan zulässig, wenn jede Stufe einem konkreten Bauablauf entspricht |
| Schlussrate-Klausel bindet Fälligkeit an einseitige Bauträgerbestätigung | 🔴; Empfängerhorizont, § 305c Abs. 2 BGB |

Praxisregel für das Mandat: Zahlungen auf die Fertigstellungsrate **nicht** leisten, solange Restarbeiten am Gemeinschaftseigentum offen sind, wesentliche Mängel beanstandet wurden oder der Vertrag die Schlussrate an die Erledigung protokollierter Punkte knüpft. Ein Bautenstands-Vermerk eines bauträgerunabhängigen Sachverständigen ist die saubere Grundlage. Bei bereits gezahlten Beträgen ist die Rückforderung über § 817 Satz 1 BGB i. V. m. § 818 Abs. 2 BGB zu prüfen; ein Mängelbeseitigungs-/Restarbeitsbudget begrenzt die Rückforderung nicht starr, ist aber argumentativ relevant.

### M.3 — Preisanpassungsklauseln und Krisenrisiko

Bauträgerverträge sind regelmäßig AGB im Sinn der §§ 305 ff. BGB, auch wenn ein Notar sie entworfen hat oder aus seiner Mustersammlung verwendet. Individualvereinbarungen werden in der Praxis selten erreicht; bloßes Verhandeln reicht nicht. Der Bauträger muss die Klausel ernsthaft zur Disposition stellen und Änderungen tatsächlich zulassen — typisch erkennbar an dokumentierten Vertragstextänderungen.

Preisanpassungsklauseln sind keine reinen Preisabreden und unterliegen damit der AGB-Inhaltskontrolle. Das gesetzliche Recht zur Anpassung wegen Störung der Geschäftsgrundlage scheidet typisch aus, wenn die Krisenlage bei Vertragsschluss bereits absehbar war oder das Vertragsverständnis ein gedeckeltes Budget des Erwerbers vorsieht. Die freie und außerordentliche Kündigung nach §§ 648, 648a BGB ist beim Bauträgervertrag durch § 650u Abs. 2 BGB ausgeschlossen; keine Seite kann eine Preisanpassung über diese Kündigungsrechte erzwingen oder unterlaufen.

Wirksamkeitsanforderungen an eine Preisanpassungsklausel im Verbraucher-Bauträgervertrag:

| Anforderung | Wirksamkeitsfolge |
| --- | --- |
| Keine kurzfristige Erhöhung innerhalb der ersten vier Monate (§ 309 Nr. 1 BGB) | sonst unwirksam |
| Anpassung nur bei höherer Gewalt / unvorhersehbaren Ereignissen, nicht bei Kalkulationsfehlern, Lieferantenwechsel, Personalengpässen ohne Krisenbezug | sonst unwirksam wegen unangemessener Benachteiligung |
| Nur tatsächliche Mehrbelastung weitergeben, kein zusätzlicher Gewinn, kein Inflationsausgleich, keine Bauträger-Marge | sonst unwirksam |
| Saldierungsgrundsatz: gesunkene Kostenbestandteile sind dem Erwerber als Preissenkung weiterzugeben | sonst unwirksam wegen Verschiebung des Äquivalenzverhältnisses |
| Transparenz: Anlass, Bezugsgrößen, Berechnungsweg klar und überschaubar | sonst unwirksam wegen Verstoßes gegen § 307 Abs. 1 Satz 2 BGB |
| Lösungsrecht des Erwerbers ab einer Schwelle | unentbehrlich; ohne Lösungsrecht regelmäßig unwirksam |

Zur Wahl des Lösungsrechts: Ein Rücktrittsrecht des Erwerbers reicht regelmäßig **nicht** aus, weil mit dem Rücktritt der Übereignungsanspruch entfällt und damit die Auflassungsvormerkung erlischt (Schutzlücke des Vormerkungsmodells). Sachgerecht ist ein vertraglich vereinbartes Recht zur Teilkündigung der werkvertraglichen Leistung — beim Geschosswohnungsbau praktisch nur gemeinsam mit allen Erwerbern ausübbar — oder eine vertragliche Aufhebungsregel mit ausdrücklicher Sicherheit für die bereits geleisteten Zahlungen.

Vorzugswürdige Klauselform: **Preisvorbehalt** nach billigem Ermessen (statt mathematischer Kostenelemente-Klausel). Anlass und Modus müssen so klar formuliert sein, dass der Erwerber bei Vertragsschluss erkennt, in welchen Krisenlagen und in welchem Rahmen sich der Preis ändern kann. Die konkrete Kalkulation muss der Bauträger im Anpassungsfall offenlegen.

Befundkategorien für die Klauselmatrix:

| Befund | Ampel |
| --- | --- |
| Preisanpassung ohne Lösungsrecht | 🔴 |
| Preisanpassung ohne Saldierung (nur Erhöhung, keine Senkung) | 🔴 |
| Preisanpassung in den ersten vier Monaten zulässig | 🔴 |
| Mathematische Kostenelemente-Klausel ohne offengelegte Kalkulation | 🔴 / 🟠 |
| Preisvorbehalt nach billigem Ermessen, höhere Gewalt, mit Saldierung und Lösungsrecht ab Schwelle | 🟢 |

Notarpflicht: Bei der Beurkundung muss der Notar den Erwerber ausdrücklich auf das Preisanpassungsrisiko hinweisen. Fehlt der Hinweis bei einer für den Erwerber überraschenden Klausel, ist eine Notarhaftungsfrage offen.

### M.4 — Verbraucherbauvertrag im engeren und im weiteren Sinn

Der Verbraucherschutz bei Bauverträgen ist in Deutschland zweispurig:

| Spur | Anwendungsbereich | Kernregelungen |
| --- | --- | --- |
| Verbraucherbauvertrag im engeren Sinn (§ 650i BGB) | Bau eines neuen Gebäudes oder erhebliche Umbaumaßnahmen, die mit einem Neubau vergleichbar sind | Baubeschreibungspflicht (§ 650j BGB i. V. m. Art. 249 EGBGB), Auslegungsregeln (§ 650k Abs. 2/3 BGB), 5 %-Sicherheit (§ 650m Abs. 2 BGB), Pflicht zur Übergabe von Planungs- und Nachweisunterlagen (§ 650n BGB), Widerrufsrecht außerhalb der Beurkundung (§ 650l BGB) |
| Verbraucherbauvertrag im weiteren Sinn | Verträge zwischen Verbraucher und Unternehmer über Bauleistungen, die nicht unter § 650i BGB fallen (Einzelgewerke, untergeordnete Bauwerke, größere Renovierungen) | Allgemeine Informationspflichten der §§ 312 ff. BGB, situative Widerrufsrechte bei Fernabsatz/Außergeschäftsraumverträgen |

Konsequenzen für den Skill:

- **Beim Bauträgervertrag mit Auflassung in einer Urkunde** gilt § 650l BGB nicht; die Beurkundung ersetzt das Widerrufsrecht. Das ist im Mandantenanschreiben transparent zu machen — keine falschen Hoffnungen auf 14-Tage-Widerruf.
- **Einzelgewerkvergabe** (z. B. der Verbraucher beauftragt direkt mehrere Handwerker zum Bau seines Einfamilienhauses): Die Einordnung als Verbraucherbauvertrag im engeren Sinn ist umstritten, hat aber gewichtige Argumente für sich. Vertretbar ist, die Einzelgewerkvergabe als Verbraucherbauvertrag i. e. S. zu behandeln, wenn die Beauftragung zeitlich gebündelt erfolgt und für die einzelnen Handwerker erkennbar ist, dass sie zu einem Neubau beitragen.
- **Baubeschreibungspflicht** nach § 650j BGB i. V. m. Art. 249 EGBGB greift unabhängig von der Beurkundung. Die Baubeschreibung wird über § 650k Abs. 1 BGB regelmäßig Vertragsinhalt — beim **reinen** Verbraucherbauvertrag. Beim Bauträgervertrag ist § 650k Abs. 1 BGB durch § 650u Abs. 2 BGB ausgeschlossen; die Baubeschreibung wird daher nur dann Vertragsinhalt, wenn sie konkret mitbeurkundet oder ausdrücklich einbezogen ist.
- **§ 650k Abs. 2/3 BGB** (Auslegung lückenhafter Baubeschreibungen zulasten des Unternehmers, verbindlicher Fertigstellungstermin) gilt **auch beim Bauträgervertrag** weiter — eine zentrale Verbraucherwaffe, die in Klauselmatrizen aktiv eingesetzt werden sollte.
- **§ 650n BGB** verpflichtet zur Übergabe der Planungs- und Nachweisunterlagen vor Ausführung und spätestens mit Fertigstellung. KfW-/GEG-Nachweise, Brandschutzgutachten, Schallschutznachweise gehören dazu. Klauseln, die diese Pflicht verkürzen, sind unwirksam.

Falle bei der Anwendungsbereich-Diskussion: Die Privilegierung des § 650f Abs. 6 Nr. 2 BGB (Verbraucher muss keine Bauhandwerkersicherung stellen) ist an den Verbraucherstatus geknüpft, nicht zwingend an einen Verbraucherbauvertrag i. e. S. Auch beim klassischen Bauträgervertrag mit Verbraucher als Erwerber besteht keine Pflicht des Erwerbers, dem Bauträger eine Bauhandwerkersicherung zu stellen.

### M.5 — Folgen unwirksamer Abnahme: die 30-Jahres-Linie

Eine in AGB enthaltene Abnahmeklausel ist nach aktueller Rechtsprechung des für das Werkvertragsrecht zuständigen Zivilsenats regelmäßig unwirksam, wenn sie

- die Abnahme einer im Lager des Bauträgers stehenden Person überträgt (Erstverwalter, Tochtergesellschaft, Projektsteuerer, vom Bauträger benannter Sachverständiger),
- oder den einzelnen Erwerber von der eigenen Prüfung und Abnahmeerklärung ausschließt,
- oder eine kollektive Bindung des Erwerbers an die Abnahmeerklärung Dritter erzeugt.

Auch bei jederzeit widerruflicher Bevollmächtigung Dritter zur Abnahme ist die Klausel angreifbar, wenn der Erwerber nicht ausdrücklich darauf hingewiesen wird, dass er die Abnahme persönlich erklären und die Vollmacht jederzeit widerrufen kann.

Rechtsfolgen einer unwirksamen Abnahmeklausel und einer auf ihr beruhenden faktischen „Abnahme":

| Stufe | Inhalt |
| --- | --- |
| Klausel | unwirksam nach §§ 307 ff. BGB |
| „Abnahme" auf der Grundlage dieser Klausel | regelmäßig ebenfalls unwirksam; der Bauträger kann sich als Verwender der Klausel auf die Unwirksamkeit der von ihm gestellten Regel nicht berufen (Grundsatz der personalen Teilunwirksamkeit) |
| Konkludente Abnahme durch rügelose Nutzung oder Zahlung | regelmäßig nicht ausreichend, solange der Erwerber von einer wirksamen Abnahmeerklärung Dritter ausging |
| Übergabe-/Abnahmeprotokoll zum Sondereigentum | keine sichere Abnahme des Gemeinschaftseigentums, wenn Vertrag und Ablauf auf Dritt- oder Sonderabnahme verweisen; der Bauträger darf der Erklärung nicht den für ihn günstigsten Sinn beilegen (OLG München 9 U 1803/23 Bau e) |
| Verjährungsbeginn der Mängelrechte | nicht angelaufen; der Bauträger kann sich gegenüber dem Erwerber nicht auf den Beginn der fünfjährigen Mängelverjährung berufen |
| Höchstgrenze | In den aktuellen BGH-Konstellationen zu unwirksamen Abnahmeklauseln wurde für die Durchsetzung von Kostenvorschussansprüchen eine 30-Jahres-Obergrenze herangezogen. Nicht pauschal auf jede Anspruchsart übertragen; Anspruch, Zeitpunkt, Rechtsstand und Verhalten der Parteien prüfen. |
| Verwirkung | nur in engen Ausnahmefällen; ein schutzwürdiges Vertrauen des Bauträgers liegt typisch nicht vor, weil er die Lage durch die unwirksame Klausel selbst herbeigeführt hat |

Folgerung für die Nachholung der Abnahme: Der Bauträger kann die Erwerber nachträglich zur Abnahme auffordern. Für die Frage der Abnahmereife gilt dann eine **ergänzende Vertragsauslegung**: Maßstab ist nicht mehr der ursprünglich vereinbarte Neuzustand, sondern das, was redliche Parteien bei Berücksichtigung von Zeitablauf und bestimmungsgemäßer Nutzung vereinbart hätten. Alters- und nutzungsbedingte Verschleißerscheinungen stehen der Abnahmereife dann nicht entgegen.

Strategische Konsequenzen für Mandate:

| Mandantenrolle | Hebel |
| --- | --- |
| Erwerber mit alter Anlage (Abnahme über bauträgernahe Person erfolgt) | Mängel der letzten Jahre noch prüfen; Verjährungsbeginn und 30-Jahres-Obergrenze anspruchsbezogen bewerten |
| Gemeinschaft der Wohnungseigentümer | Vergemeinschaftungsbeschluss; Mängelrügen wirken erst ab Beschluss verjährungshemmend, nicht rückwirkend |
| Bauträger mit Altprojekten | Erwerber zur Nachholung der Abnahme auffordern; selbständiges Beweisverfahren gegen Nachunternehmer einleiten, um Verjährung der eigenen Regressansprüche zu hemmen; Abgeltungsvergleich mit der Gemeinschaft prüfen |

Wichtige Differenzierungen:

- **Aktuelles Recht (Verträge ab 1.1.2002)**: Mängelrechte vor Abnahme bestehen grundsätzlich nicht; der Erwerber hat ohne Abnahme nur Erfüllungsansprüche. Allerdings ist es dem Bauträger über den Grundsatz der personalen Teilunwirksamkeit verwehrt, sich auf die fehlende Abnahme zu berufen. Mängelrechte sind daher praktisch durchsetzbar, als wäre wirksam abgenommen worden — einschließlich Kostenvorschuss, Minderung und Schadensersatz.
- **Berechtigte vorläufige Abnahmeverweigerung**: Wenn der Erwerber die Abnahme zu Recht verweigert, weil das Werk nicht abnahmereif ist, gelten die Grundsätze der personalen Teilunwirksamkeit nicht. Hier kann die regelmäßige Verjährung von Ansprüchen wegen Schlechtleistung schon vor der fünfjährigen Mängelverjährungsfrist eintreten — eine systematische Asymmetrie, die im Schrifttum offen umstritten ist. Praxis: Erwerber sollte parallel die nachträgliche Abnahme erklären, um die fünfjährige Frist mit dem Sicherheitsanker zu eröffnen.
- **„Vergessene" Abnahme**: Ist die Abnahme schlicht unterblieben (kein Klauseldefekt, keine konkludente Abnahme, keine berechtigte Verweigerung), gilt für die Abnahmereife ebenfalls die ergänzende Vertragsauslegung; Anknüpfungspunkt ist regelmäßig der Zeitpunkt der Übergabe.

Für den Klauselmatrix-Output: Jede AGB-Abnahmeklausel zugunsten einer im Lager des Bauträgers stehenden Person oder mit einer kollektiven Bindung der Erwerber ist 🔴 zu führen, mit Hinweis auf die aktuelle BGH-Linie, die mögliche personale Teilunwirksamkeit und die anspruchsbezogen zu prüfende Höchstgrenzen-Logik. Im Schreiben an den Bauträger (Teil L) ist die Klausel zur Streichung zu verlangen, hilfsweise so umzuformulieren, dass jeder Erwerber das ausdrückliche Recht behält, das Gemeinschaftseigentum selbst oder durch eine Person seines Vertrauens zu prüfen und die Abnahme persönlich zu erklären; das Notariat wird bei Beurkundungsreife oder Belehrungsbedarf in Kopie gesetzt.

### M.6 — Bauablaufbezogene Darlegung bei Verzug

Wenn der vertragliche Fertigstellungstermin überschritten wird und der Bauträger sich auf höhere Gewalt, Pandemielage, Lieferengpässe, Streik, Witterung, Personalmangel oder „sonstige unabwendbare Umstände" beruft, ist sein Vortrag substanziiert zu prüfen. Eine pauschale Berufung reicht nicht.

Anforderungen an die Darlegung des Bauträgers:

| Element | Inhalt |
| --- | --- |
| Bauablaufplan | Welcher Arbeitsablauf war geplant? Mit welchen Vorgängen? Welche Pufferzeiten? |
| Konkretes Ereignis | Welches Ereignis hat den Ablauf gestört? Genaues Datum, genaue Beschreibung, vorzugsweise mit Belegen (Lieferantenkorrespondenz, Behördenbescheide, Wettergutachten, Personalmeldungen) |
| Auswirkung | Wie und in welchem zeitlichen Umfang hat das Ereignis konkret welchen Vorgang gestört? |
| Folgen | Welche Folgevorgänge waren betroffen? Wurde versucht, durch Umdisposition gegenzusteuern? |
| Anpassungs- und Wiederanlaufzeit | Wie lange war die Wiederaufnahme nach Wegfall der Störung erforderlich? |

Reicht die Darlegung nicht, **bleibt** der Bauträger im Verzug ab dem ursprünglich vereinbarten Termin. Verzugsschäden sind dann nach § 286 BGB ersatzfähig — Miete für Ersatzwohnung, Bereitstellungszinsen auf noch nicht abgerufenes Darlehen, doppelte Mietbelastung, Lagerkosten, Umzugskosten, Hotelkosten. Bereitstellungszinsen sind dabei kein Sowieso-Schaden; sie wären bei rechtzeitiger Leistung gerade nicht angefallen.

Vertragsstrafe und pauschalierter Schadensersatz: Beide Instrumente kompensieren regelmäßig denselben Verzugsschaden; bei Interessenidentität wird der eine auf den anderen angerechnet. Eine Klausel, die den weitergehenden Schadensersatz auf Vorsatz und grobe Fahrlässigkeit beschränkt, ist auf ihre Vereinbarkeit mit § 309 Nr. 7 BGB zu prüfen.

Eine vertragliche Klausel, die für den Eintritt des Verzugs eine zusätzliche, gesetzlich nicht vorgesehene Mahnung mit langer Nachfrist und Einschreiben verlangt, weicht vom gesetzlichen Leitbild des § 286 Abs. 2 Nr. 1 BGB ab und ist nach § 307 BGB regelmäßig unwirksam.

### M.7 — Baugruppen-GbR als Alternative zum Bauträger

Wer als Verbraucher bewusst keinen Bauträgervertrag schließen will, kann sich mit anderen zu einer Baugruppe (typisch in der Form einer GbR) zusammenschließen und das Grundstück gemeinsam erwerben, gemeinsam bebauen und anschließend in eine WEG aufteilen. Der Skill prüft solche Konstellationen mit veränderten Maßstäben:

| Punkt | Bauträgervertrag | Baugruppe |
| --- | --- | --- |
| Vertragspartner | ein Bauträger | mehrere Verbraucher als Gesellschafter |
| Bauherreneigenschaft | Bauträger ist Bauherr; Erwerber kauft das fertige Werk | jeder Gesellschafter ist Bauherr |
| MaBV | gilt | gilt nicht (keine Bauträgerleistung) |
| Insolvenzrisiko | Insolvenz des Bauträgers trifft alle Erwerber im Projekt | aufgeteilt auf einzelne Handwerker; Gegenstück: persönliche Risiken der Gesellschafter |
| Beurkundungspflicht des Gesellschaftsvertrags | nicht einschlägig | grundsätzlich beurkundungspflichtig, soweit der Vertrag die Verpflichtung zur Übertragung von Sondereigentum oder zur Aufgabe von Bruchteilseigentum enthält; Heilung nach § 311b Abs. 1 Satz 2 BGB ist beim WEG-Modell typisch ausgeschlossen, weil eine wirksame Auflassung an die Gesellschafter erst nach Vollzug der Teilungserklärung erfolgt |
| Haftung | Bauträger haftet, Erwerber zahlen | Gesellschafter haften nach den Grundsätzen der GbR; nach geltendem Personengesellschaftsrecht ist eine Haftungsbeschränkung im Außenverhältnis nur eingeschränkt möglich |

Notarielle und vertragliche Prüfpunkte beim Baugruppenmodell:

| Prüfpunkt | Inhalt |
| --- | --- |
| Beurkundung des Gesellschaftsvertrags | erforderlich, soweit ein Eigentumsübertragungsbezug besteht; sicherer Weg: Vollbeurkundung des Gesellschaftsvertrags |
| Rumpfgründung als Alternative | Gesellschaft wird ohne Grundstücksbezug formfrei gegründet; alle eigentumsbezogenen Vereinbarungen werden später in beurkundeter Form ergänzt — hohes Risiko der Lückenhaftigkeit |
| Bruchteilseigentum als Alternative | Erwerb des Grundstücks in Bruchteilseigentum, Ausbau als Werkvertrag; Teilungserklärung folgt — saubere, aber komplexe Variante |
| Beitragspflichten | planmäßige Zahlungen plus Nachschusspflicht regeln; bei privaten Verbrauchern Nachschusspflicht eng begrenzen |
| Übertragung von Gesellschaftsanteilen | Bindung an Mehrheitsbeschluss; Vorkaufsrechte; Anti-Spekulationsklauseln |
| Freiwilliges und unfreiwilliges Ausscheiden | Kündigung nach § 725 BGB; Ausschluss aus wichtigem Grund; Abfindungsregelungen mit klaren Bewertungsmaßstäben |
| Aufspaltung des Grundstücks-Kaufvertrags | bei großer Mitgliederzahl praktikabel; berufsrechtlich (Notar) und insolvenzrechtlich zulässig, wenn Angebot und Annahme rechtssicher dokumentiert sind |
| Finanzierungsgrundschulden | typischerweise einzeln pro Gesellschafter; bei gemeinsamer Globalgrundschuld besondere Sicherungs- und Auseinandersetzungsregeln |
| Teilungserklärung und Übertragung der Sondereigentumseinheiten | nach Fertigstellung; Realisierung des Bauziels jedes Gesellschafters in eine eigene WE-Einheit |

Wenn die Anfrage nicht eindeutig einen Bauträgervertrag betrifft, sondern eine Baugruppen-Konstruktion erkennen lässt (mehrere Bauherren, gemeinsamer Grundstückserwerb, gemeinsame Auftragsvergabe an Handwerker), prüft der Skill den Vertrag entlang dieser Kategorie statt entlang der Bauträger-Pflicht-Prüfblock-Logik. Im Mandantenanschreiben ist die Strukturdifferenz auszuweisen.

### M.8 — Erweiterungen der Klauselmatrix und der Antwortformate

Die folgenden Punkte ergänzen die Klauselmatrix in Teil B um aktuelle Streitfelder:

| Klauseltyp | Befund | Verhandlungsantwort |
| --- | --- | --- |
| „Anerkannte Regeln der Technik zum Vertragsschluss" | 🔴 | „zum Zeitpunkt der Abnahme; bei Änderung Hinweispflicht des Bauträgers" |
| „Geltendes Recht" als Energiestandard | 🔴 | „mindestens KfW-/Effizienzhausklasse X; Abweichung nur mit ausdrücklicher Belehrung" |
| Preisanpassung ohne Lösungsrecht des Erwerbers | 🔴 | Lösungsrecht ab Schwelle (z. B. 5 %) als gesonderte Klausel |
| Preisanpassung ohne Saldierung | 🔴 | Saldierungspflicht mit Nachweis aus Bauträger-Kalkulation |
| Verkürzung der vollständigen Fertigstellung auf Bezugsfertigkeit | 🔴 | Wortlaut „vollständige Fertigstellung einschließlich Außenanlagen und sämtlicher Restarbeiten" |
| Zusätzliche Mahnpflicht im Verzug | 🔴 | streichen; gesetzlicher § 286 BGB |
| Bauträgerklausel zur Bauablauf-„Höhere Gewalt"-Vermutung | 🔴 | konkrete Darlegung erforderlich, sonst Verzug ab Termin |
| Abnahme durch Erstverwalter / Tochtergesellschaft / Bauträger-Sachverständigen | 🔴 | streichen oder Eigenrecht des Erwerbers ausdrücklich sichern |
| Baugruppen-GbR-Vertrag ohne Beurkundung der Eigentumsbezüge | 🔴 | Vollbeurkundung oder Bruchteilsmodell mit nachgelagerter Teilung |
| Interne Projektsteuerung ersetzt Bauüberwachung | 🔴 | Nachweis LPH 8/technische Fachüberwachung und eigene Kontrollrechte des Erwerbers sichern |
| Baustellenzutritt nur mit Verkäufergenehmigung, keine Fotos, keine Sachverständigen | 🔴 | Begleiteter Zutritt zu Qualitätsgates, MaBV-Bautenstandsprüfung und Abnahme muss möglich sein |
| Baugrund-/Grundwasser-/Altlastenrisiko pauschal beim Erwerber | 🔴 | Gutachten offenlegen; Restrisiken und Mehrkosten beim Bauträger, soweit nicht konkret aufgeklärt und bepreist |
| Schallschutz/Feuchteschutz/Lüftung nur als Nutzerverhalten definiert | 🟠/🔴 | konkrete Nachweise, Wartungs-/Bedienkonzept und Mindestparameter verlangen |

Für die drei Dokumente aus Teil L gelten zusätzlich:

- **Mandantenanschreiben (L.1)**: Wenn der Vertrag Preisanpassungsklauseln oder Risiken aus geänderten anerkannten Regeln der Technik enthält, ist die finanzielle Bandbreite klar zu benennen — keine vage Aussage „kann teurer werden".
- **Gutachten (L.2)**: Die Abschnitte zu Baubeschreibung, Schlussrate und Abnahme sind um die 30-Jahres-Linie und die personale Teilunwirksamkeit zu ergänzen, soweit unwirksame Abnahmeklauseln festgestellt wurden.
- **Schreiben an den Bauträger (L.3)**: Bei AGB-Preisanpassungsklauseln, Verkürzung der Fertigstellungsdefinition und Klauseln zu „anerkannten Regeln der Technik zum Vertragsschluss" ist die Streichung oder verhandlungsfähige Neufassung mit ausformuliertem Wortlaut-Vorschlag zu fordern. Das Notariat nur bei Urkunds- oder Vollzugsthemen gesondert adressieren oder in Kopie setzen.

Ergänzungen zum Bug-Hunt (vor jeder Ausgabe):

- DIN-Norm nicht als anerkannte Regel der Technik behandeln; richtig ist die Einzelfallprüfung.
- Vollständige Fertigstellung nicht mit Bezugsfertigkeit gleichsetzen.
- Preisanpassung nicht ohne Lösungsrecht akzeptieren.
- Unwirksame Abnahmeklauseln nicht als bloßes „Beratungsproblem" abhandeln; Verjährungsbeginn und 30-Jahres-Obergrenze aber anspruchsbezogen prüfen, nicht pauschal behaupten.
- Bauablauf-Argumente der Bauträgerseite nicht ungeprüft als höhere Gewalt durchgehen lassen.
- § 650l BGB nicht für beurkundete Bauträgerverträge in Anspruch nehmen; das Widerrufsrecht greift dort nicht.
- Bauhandwerkersicherung (§ 650f BGB) nicht vom Verbraucher-Erwerber fordern; § 650f Abs. 6 Nr. 2 BGB privilegiert ihn.
- Baugruppen-GbR nicht mit Bauträgervertrag-Maßstäben prüfen; die MaBV greift nicht.

## Teil N — Wirtschaft, Organisation, HOAI und Technik

Teil N verhindert den häufigsten Praxisfehler: Ein Vertrag kann juristisch bearbeitet sein und trotzdem ein schlechtes Bauprojekt absichern. Die Analyse muss deshalb neben AGB/MaBV immer prüfen, ob Planung, Bauüberwachung, Baugrund, technische Qualität, Wirtschaft und WEG-Organisation real kontrollierbar sind.

### N.1 — Rollenmodell

Erstelle bei jeder Vollanalyse ein Rollenbild:

| Rolle | Mindestprüfung |
| --- | --- |
| Bauträger/Projektgesellschaft | Eigenkapital, Konzernbindung, Globalfinanzierung, Freistellung, Bauherreneigenschaft |
| Architekt/Objektplaner | Welche Leistungsphasen beauftragt? Wer schuldet Ausführungsplanung, Objektüberwachung und Dokumentation? |
| Fachplaner | Tragwerk, Brandschutz, Schall, Wärme/Feuchte, technische Ausrüstung, Außenanlagen, Tiefgarage |
| Bauleiter/Objektüberwacher | Unabhängigkeit, Qualifikation, Berichtswesen, Mängelverfolgung, Haftpflichtdeckung |
| Prüfingenieur/Prüfsachverständige | Statik, Brandschutz, ggf. Sonderbau-/Garagenanforderungen |
| Bodengutachter | Baugrund, Grundwasser, Altlasten, Kampfmittel, Versickerung, Baugrubenverbau |
| Generalunternehmer/Nachunternehmer | Vertragliche Schnittstellen, Insolvenz-/Austauschrisiko, Gewährleistungsdurchgriff |
| Erstverwalter/WEG | Interessenkonflikt, Abnahme, Wartungsverträge, Mängelverfolgung, Dokumentationsübergabe |

Kernfrage: Wer kontrolliert wen, wer berichtet an wen und welche Unterlagen bekommt der Erwerber oder später die GdWE? Eine rein interne Verkäuferkontrolle ist kein Ersatz für prüfbare Qualitätssicherung.

### N.2 — HOAI-Leistungsphasen als Prüfraster

Die HOAI ist primär Honorarrecht. Sie begründet nicht automatisch einen Direktanspruch des Erwerbers gegen den Architekten des Bauträgers. Sie ist aber ein belastbares Organisationsraster. § 34 HOAI nennt für Gebäude und Innenräume neun Leistungsphasen; Anlage 10.1 beschreibt die Grundleistungen.

| LPH | Inhalt | Verbrauchercheck |
| --- | --- | --- |
| 1 Grundlagenermittlung | Aufgabenstellung, Bedarf, Untersuchungsbedarf | Wurde Bedarf/Qualitätsziel dokumentiert oder nur Vertriebssprache? |
| 2 Vorplanung | Varianten, Zielkonflikte, Kostenschätzung, Terminplan | Gibt es belastbare Planungsgrundlagen, Baugrund-/Genehmigungsrisiken, Terminlogik? |
| 3 Entwurfsplanung | System- und Integrationsplanung, Kostenberechnung | Passt Baubeschreibung zu Plänen, Technik, Kosten und Prospekt? |
| 4 Genehmigungsplanung | Bauantrag, öffentlich-rechtliche Nachweise | Liegt die Baugenehmigung für das konkrete Haus vor? Sind Auflagen eingepreist? |
| 5 Ausführungsplanung | ausführungsreife Details | Ohne LPH-5-Logik sind Schall, Abdichtung, Brandschutz, Haustechnik und Details nicht prüfbar. |
| 6/7 Vergabe | Leistungsverzeichnisse, Angebotsprüfung, Vergabe | Unklare GU-/Nachunternehmer-Schnittstellen sind Insolvenz- und Qualitätsrisiko. |
| 8 Objektüberwachung | Bauüberwachung und Dokumentation | Zentral: Bautenstand, Mängeltracking, Rechnungs-/Ratenfreigabe, technische Abnahmen. |
| 9 Objektbetreuung | Mängelverfolgung nach Fertigstellung | WEG braucht geordneten Übergang, Gewährleistungsmanagement und Unterlagen. |

Gewünschte Vertragsposition: Der Bauträger muss bestätigen, dass fachlich geeignete Objekt- und Fachplaner für die erforderlichen Planungs- und Überwachungsleistungen eingesetzt werden, und der Erwerber/GdWE erhält die zur Prüfung, Abnahme, Finanzierung, Förderung und Unterhaltung erforderlichen Unterlagen.

### N.3 — Private Bauüberwachung und Sachverständige

Der Erwerber darf die Baustelle nicht beliebig betreten und keine Anweisungen an Unternehmer geben. Verkehrssicherung, Arbeitsschutz, Bauablauf und Hausrecht sind real. Daraus folgt aber nicht, dass der Bauträger jede unabhängige Kontrolle ausschließen darf.

Verhandlungsfähige Mindestlösung:

- begleiteter Baustellenzutritt zu definierten Qualitätsgates: Rohbau, Fenster/Dach, Rohinstallation, Estrich, Abdichtung/Tiefgarage, Bezugsfertigkeit, Abnahme.
- Teilnahme eines eigenen Architekten, Bauingenieurs oder Sachverständigen des Erwerbers.
- Einsicht in prüfbare Bautenstands- und Mängelberichte vor MaBV-Raten.
- Fotos der eigenen Einheit und relevanter Gemeinschaftsbereiche, soweit keine Persönlichkeits-/Sicherheitsinteressen entgegenstehen.
- keine Weisungen an Handwerker; Kommunikation über Bauträger/Objektüberwachung.
- Abnahmebegleitung für Sondereigentum und Gemeinschaftseigentum.

Klauseln, die `eigene Bautenstandskontrollen`, `private Sachverständige`, `Fotodokumentation` oder `Teilnahme an Abnahmen` pauschal ausschließen, sind als 🔴 zu führen, weil sie MaBV-Fälligkeit, Abnahmeprüfung und Mängelrechte praktisch entwerten.

### N.4 — Baugrund, Baugrube und Grundstücksrealität

Baugrundrisiken zerstören die schönste Vertragsprüfung. Der Skill prüft deshalb immer:

| Thema | Zu verlangende Unterlagen/Angaben |
| --- | --- |
| Baugrund | geotechnischer Bericht, Gründungsempfehlung, Setzungsprognose, Bodenklassen, Tragfähigkeit |
| Grundwasser | Bemessungswasserstand, Dränage-/Wannen-Konzept, temporäre Wasserhaltung, Auftriebssicherheit |
| Baugrube | Verbau, Nachbarbebauung, Erschütterung, Beweissicherung, Bauzustände |
| Altlasten | orientierende/Detailuntersuchung, Entsorgungskonzept, Deponieklassen, Kostenrisiko |
| Kampfmittel | Auskunft/Sondierung, Freigabe, Bauverzugs- und Kostenfolge |
| Niederschlagswasser | Versickerung, Rückhaltung, Überflutungsschutz, Notwasserwege |
| Tiefgarage | Abdichtung, Entwässerung, Gefälle, Chloridbelastung, Lüftung, Brandschutz |

Rote Klauselmuster:

- `Der Käufer übernimmt alle Risiken aus Baugrund, Grundwasser oder Altlasten`.
- `Gutachten dienen nur internen Zwecken und begründen kein Bausoll`.
- `Wasserhaltung, Verbau oder Entsorgung können als Mehrkosten umgelegt werden`.
- `Verzögerungen wegen Baugrund/Altlasten verlängern die Frist ohne Nachweis`.

Antwort: Baugrund und Baugrube liegen im Verantwortungsbereich des Bauträgers als Bauherrn und Herstellungsverpflichteten. Eine Risikoverlagerung ist nur denkbar, wenn der konkrete Umstand offen, verständlich, bepreist und vertraglich eng geregelt ist.

### N.5 — Technische Kernmatrix

In jeder Vollanalyse mindestens diese technischen Themen scannen:

| Bereich | Typische harte Frage |
| --- | --- |
| Tragwerk | geprüfte Statik, Prüfbericht, Ausführungsplanung, Durchbrüche/Sonderwünsche |
| Brandschutz | Konzept, Auflagen, Tiefgarage, Rettungswege, Abschottungen, Dokumentation |
| Schallschutz | Mindeststandard oder erhöhter Schallschutz? Trittschall, Installationsschall, Aufzug/Tiefgarage |
| Wärmeschutz/Energie | GEG, KfW-/Effizienzhausversprechen, Wärmebrücken, Luftdichtheit, Förderbedingungen |
| Feuchte/Abdichtung | Keller/Tiefgarage, Balkone, Flachdach, Sockel, Bäder, Duschen, Anschlüsse |
| Lüftung | Lüftungskonzept, Nutzerpflichten, Schimmelrisiko, Wartung, Nachströmung |
| Trinkwasser/Heizung | Hygiene, Zirkulation, Wärmepumpe/Fernwärme, Abrechnung, Betriebsrisiko |
| Elektro/PV/Smart Home | Zählerkonzept, Ladeinfrastruktur, Reserven, Wartung, Datenschutz |
| Aufzug/Tiefgarage | Betriebskosten, Wartung, Ersatzteile, Brandschutz, Barrierefreiheit |
| Außenanlagen | Entwässerung, Beleuchtung, Spielplatz, Pflanzung, Erhaltungspflichten |

Pauschale Verkäuferklauseln wie `Funktionsfähigkeit nur bei ordnungsgemäßem Nutzerverhalten`, `Schimmel ist kein Mangel bei falschem Lüften` oder `technische Anlagen sind keine Beschaffenheitsvereinbarung` sind nie isoliert zu akzeptieren. Sie brauchen Bedienkonzept, Nachweis, Übergabeunterlagen und dürfen das Bausoll nicht verschieben.

### N.6 — Wirtschaftliche und organisatorische Prüfung

Der Erwerber kauft nicht nur Mauerwerk, sondern ein langfristiges Organisations- und Kostenpaket.

| Thema | Prüffrage |
| --- | --- |
| Projektgesellschaft | Ist sie substanzarm? Gibt es Patronat, Muttergesellschaft, Gewährleistungsreserve? |
| Finanzierung | Globalgrundschuld, Freistellung, Auszahlungsvoraussetzungen, Bankfreigaben |
| GU-/Nachunternehmerstruktur | Wer baut tatsächlich? Austauschrecht? Insolvenz eines GU? |
| Sonderwünsche | Vorauszahlung, Schnittstellen, Gewährleistung, Terminrisiko, MaBV-Einordnung |
| Betriebskosten | Fernwärme, Contracting, Aufzug, Tiefgarage, Lüftung, Wasserhaltung, Gemeinschaftseinrichtungen |
| Wartungsverträge | Laufzeit, Kündbarkeit, Preisanpassung, Erstverwalter-Interessenkonflikt |
| Instandhaltungsrücklage | realistisch für Technik/Tiefgarage/Aufzug/Pumpen? |
| Untergemeinschaften | Kostenverteilung, Stimmrechte, Sondernutzungen, spätere Bauabschnitte |

Rote Linie: Keine Klausel darf wirtschaftliche Risiken verstecken, die den Gesamtpreis faktisch erhöhen oder die WEG über lange Wartungs-, Verwaltungs- oder Betriebspflichten an bauträgernahe Unternehmen bindet.

### N.7 — Dokumentations- und Übergabepaket

Mindestens verlangen:

- Baugenehmigung mit Auflagen für das konkrete Haus.
- geprüfte Statik/Prüfberichte, Brandschutznachweise, Schallschutz-/Wärmeschutznachweise.
- Energieausweis, GEG-/KfW-/Fördernachweise, Luftdichtheits-/Inbetriebnahmeprotokolle soweit geschuldet.
- Revisionspläne, Wartungs- und Bedienungsanleitungen, Fachunternehmererklärungen.
- Protokolle zu technischen Inbetriebnahmen: Heizung, Lüftung, Trinkwasser, Aufzug, Brandmelde-/Rauchabzugstechnik, Tiefgarage.
- Mängel- und Restarbeitenliste für Sonder- und Gemeinschaftseigentum.
- Gewährleistungs-/Ansprechpartnerliste für Gewerke.

§ 650n BGB ist der gesetzliche Anker für Planungs- und Nachweisunterlagen. Bei Bauträgern ist die Norm nicht durch § 650u Abs. 2 ausgeschlossen. Für reine Komfortunterlagen kann die Anspruchsgrundlage anders liegen; für öffentlich-rechtliche Nachweise, Förder-/Finanzierungsbedingungen und berechtigt geweckte Erwartungen ist § 650n aktiv zu prüfen.

### N.8 — Ausgabe in den drei Dokumenten

**Mandantenanschreiben:** Technik/Wirtschaft in Klartext: `Das größte Risiko ist nicht nur Klausel X, sondern dass Sie vor Zahlung und Abnahme keine unabhängige Kontrolle von Baugrund, Bautenstand und technischen Nachweisen erhalten.`

**Gutachten:** Eigener Abschnitt `HOAI/Objektüberwachung/Technik/Wirtschaft`. Jede technische rote Ampel braucht: Vertragswortlaut, praktisches Risiko, fehlende Unterlage, gewünschte Änderung.

**Schreiben an den Bauträger:** Keine Fachsimpelei. Forderungen konkret:

```text
Bitte ergänzen Sie eine Regelung, wonach der Erwerber nach angemessener Voranmeldung und unter Beachtung der Sicherheitsvorgaben einen eigenen Sachverständigen zu den Bautenstands- und Abnahmeterminen hinzuziehen darf. Die Fälligkeit von MaBV-Raten darf nicht allein durch eine interne Bauleiterbestätigung des Verkäufers ausgelöst werden, sondern muss durch objektiv nachvollziehbaren Baufortschritt prüfbar sein.
```

### N.9 — Scoring

| Befund | Gewicht |
| --- | --- |
| Keine eigene/private Bautenstandskontrolle vor Raten | 🔴 |
| LPH 8/Bauüberwachung nur intern und ohne Dokumentation | 🔴 |
| Baugrund-/Grundwasser-/Altlastenrisiko beim Erwerber | 🔴 |
| Baugenehmigung oder Auflagen für das konkrete Objekt fehlen | 🔴 |
| Keine konkreten Schall-/Energie-/Feuchteschutzparameter | 🟠/🔴 |
| Erstverwalter kontrolliert Abnahme, Wartung und Mängelmanagement | 🔴 |
| Lange Wartungs-/Contractingbindung an Verkäuferumfeld | 🟠/🔴 |
| Technische Unterlagen erst `nach Ermessen` oder gar nicht | 🔴 |

## Teil O — Fachmodule Bauträgerrecht 2026

Teil O ist die verdichtete Arbeitskarte der fachlichen Erweiterung. Er wird nicht separat ausgegeben, sondern steuert, welche Prüffragen in Teil B, K, L, M und N zwingend mitzudenken sind. Alles, was auf konkrete Rechtsprechung hinausläuft und nicht bereits in den Rechtsprechungsankern mit zulässiger URL steht, wird vor Schriftsatz- oder Gutachtenverwendung live über offizielle Gerichtsseiten, `rechtsprechung-im-internet.de`, `dejure.org` oder `openjur.de` verifiziert.

### O.1 — Vorinsolvenz, MaBV-Druckmuster und Rückforderung

Wenn der Bauträger in einer angespannten Projektlage früh, großvolumig oder außerhalb sauberer MaBV-Fälligkeit Geld will, wird nicht nur der Zahlungsplan geprüft. Der Skill prüft drei Ebenen:

| Ebene | Prüfauftrag |
| --- | --- |
| Zahlungsfälligkeit | § 3 Abs. 1 MaBV vollständig? § 3 Abs. 2 MaBV-Bautenstand real erreicht? § 7 MaBV wirklich alternativ und ausreichend? |
| Druckmechanik | Schlüssel, Besitz, Sonderwunsch, Vormerkungslöschung, Mahnkosten, Verzugsdrohung oder Notartermin werden als Hebel genutzt? |
| Anspruchskette | Rückforderung verfrühter Zahlungen, Zurückbehaltung, § 650m-Sicherheit, Geschäftsführer-/Bauleiter-/Notarhaftung mit konkretem Vorsatz-/Pflichtwidrigkeitsanker |

Rote Muster: zwei Großraten, `mitgeteilte` Bautenstände, Schlussrate vor Außenanlagen, Bauleiterbestätigung ohne Erwerberkontrolle, unrichtige Genehmigungsfreiheitsbestätigung, wesentliche Abweichung von der Baugenehmigung ohne Nachtrag, Freistellungserklärung mit Lücken beim steckengebliebenen Bau, § 650m-Sicherheit als bloßes Wahlrecht, einseitige Vormerkungslöschung.

Bei steckengebliebenem Bau nach Bauträgerinsolvenz zusätzlich BGH V ZR 219/24 prüfen: GdWE-Erstherstellung, Beschlussersetzung, Kostenlast für gemeinschafts- und sondereigentumsnahe Gewerke, Abgrenzung zu baulichen Veränderungen sowie Vorrang erfolgversprechender vertraglicher Ansprüche gegen Bauträger oder Insolvenzverwalter.

Zusatzprüfung Baugenehmigung: Ist die Genehmigung nur behauptet, ist die Monatsfrist bei Eigenbestätigung noch offen oder weicht das ausgeführte Haus wesentlich von der Genehmigung ab, wird keine Rate freigegeben. Der Skill fordert Genehmigung, Nachtragsgenehmigung, Auflagenstand und Abgleich mit Plan-/Baubeschreibungsstand.

### O.2 — Bauzeitverzug, Schadenspositionen und Restvergütung

Bei verzögerter Übergabe werden Termin, Darlegung und Schaden getrennt:

1. Kalendarischer Termin oder nur `voraussichtlich`?
2. Verschiebung wirksam vereinbart oder nur einseitig angekündigt?
3. Bauablaufbezogene Entlastung: Ereignis, Gewerk, Dauer, Folgevorgang, Wiederanlaufzeit.
4. Schadenspositionen mit Belegen: Ersatzmiete, Umzug, Lager, Hotel, doppelte Miete, Bereitstellungszinsen, Nutzungsausfall.
5. Vertragsstrafe, pauschalierter Schaden und weiterer Schaden mit Anrechnung prüfen. Nach BGH VII ZR 129/24 erlischt eine bereits verwirkte verzugsbedingte Vertragsstrafe bei Rücktritt wegen nicht termingerechter Fertigstellung nicht automatisch; abweichende Vertragsregelung ausdrücklich prüfen.
6. Restvergütung des Bauträgers nur bei Abnahme, wirksamer Abnahmefiktion oder sonstiger Fälligkeitsgrundlage.

§ 313 BGB wird nur als enges Korrektiv geprüft. War die Krise bei Vertragsschluss bereits erkennbar, darf der Bauträger sie nicht als nachträgliches Überraschungsrisiko recyceln.

### O.3 — Technikrecht: DIN, anerkannte Regeln und Standardänderung

DIN-Konformität ist kein Vollbeweis für Mangelfreiheit. Der Skill trennt:

| Kategorie | Funktion |
| --- | --- |
| anerkannte Regeln der Technik | werkvertraglicher Mindeststandard; wissenschaftliche Anerkennung plus praktische Bewährung |
| Stand der Technik | höherer aktueller Erkenntnisstand; zivilrechtlich nur bei Vereinbarung oder spezieller Norm |
| Stand von Wissenschaft und Technik | Spitzenstandard für Hochrisikobereiche |

Stichtag für das Bausoll ist grundsätzlich die Abnahme. Standardänderungen zwischen Vertragsschluss und Abnahme lösen Aufklärungs- und Entscheidungsbedarf aus. Mängelbeseitigung nach Abnahme richtet sich nach dem Standard der Beseitigung; Mehrkosten werden nicht pauschal als Sowieso-Kosten abgetan, ein bleibender Mehrwert ist aber sauber zu prüfen.

### O.4 — Verbraucherbauvertrag, Bauträgervertrag und allgemeines Verbraucherrecht

Der Skill hält die Spuren auseinander:

| Spur | Bauträgerfolge |
| --- | --- |
| § 650i BGB Verbraucherbauvertrag i. e. S. | Bauträgervertrag ist eigener Typ nach § 650u BGB; nicht mechanisch gleichsetzen |
| § 650l BGB Widerruf | beim beurkundeten Bauträgervertrag durch § 650u Abs. 2 BGB ausgeschlossen |
| § 650k Abs. 2/3 BGB | bleibt beim Bauträger nutzbar; lückenhafte Baubeschreibung wird zulasten des Unternehmers ausgelegt |
| § 650n BGB | Unterlagenpflicht bleibt; GEG/KfW/Brandschutz/Schall/Statik/Nachweise aktiv verlangen |
| §§ 312 ff. BGB | nur ergänzend bei situativem Fernabsatz-/Außergeschäftsraumbezug prüfen |
| Einzelgewerkvergabe | offen und fallabhängig; nicht als entschieden ausgeben |

### O.5 — Baugruppen-GbR statt Bauträger

Wenn mehrere Verbraucher gemeinsam Grundstück und Bauleistungen organisieren, verlässt die Prüfung den Bauträgerpfad. MaBV greift mangels Bauträgerleistung nicht. Dafür entstehen Form-, Haftungs- und Gesellschaftsrisiken: Beurkundung des eigentumsbezogenen Gesellschaftsvertrags, Heilungsproblem im WEG-Modell, Nachschüsse, persönliche Gesellschafterhaftung, Ausscheiden, Insolvenz einzelner Gesellschafter, Finanzierung und spätere Aufteilung.

Der Skill muss im Mandantenanschreiben klar sagen: Die Baugruppe vermeidet Bauträgerrisiken, verliert aber zugleich MaBV-Schutzschichten. Das ist kein automatisch verbraucherfreundlicher Ersatz.

### O.6 — Beurkundung, Bezugsurkunden, Sonderwünsche

Prüfung vor Beurkundung:

- Sind Baubeschreibung, Pläne, Teilungserklärung und Sonderwünsche konkret beurkundet oder eindeutig bezogen?
- Gibt es entgeltliche Reservierungsvereinbarungen oder Vorausleistungen mit Erwerbsdruck?
- Werden wesentliche Vertragsbedingungen in Bezugsurkunden versteckt?
- Haben Sonderwünsche Auswirkungen auf Ratenplan, Bausoll, Gewährleistung, Termine oder Sondereigentum?
- Wird die VOB/B oder ein externer Standard nur pauschal einbezogen?

Bei Formrisiko nicht reflexhaft Gesamtnichtigkeit behaupten. Vertragsstand, Auflassung, Eintragung und Heilung prüfen.

### O.7 — Nachzügler, Altbau und Sanierungsobjekte

Nachzüglerfälle brauchen einen eigenen Block im Gutachten. Erfasst werden: Errichtung/Fertigstellung, vorherige Abnahmeakte, Vermietungsdauer, Zustand bei Erwerb, eigener Abnahmetermin, Klausel zur Anerkennung fremder Abnahme und Art der übernommenen Sanierungsleistung. BGH VII ZR 49/15 und VII ZR 171/15 sind die vorrangigen Nachzügler-Anker: keine formularmäßige Bindung an fremde Abnahme, keine vorverlegte Mängelverjährung und keine automatische Verdrängung des Werkvertragsrechts nur wegen Fertigstellung vor Vertragsschluss. Bei längerer Vermietung und echtem Bestandsverkauf ist Kaufrechtsnähe gesondert zu prüfen.

### O.8 — Persönliche und notarielle Anspruchsketten

Der Skill nutzt persönliche Haftung nur mit Tatsachenunterbau:

| Beteiligter | Wann prüfen |
| --- | --- |
| Geschäftsführer | vorzeitige MaBV-Ratenanforderung, Kenntnis des Bau-/Fälligkeitsstands, operative Zahlungssteuerung |
| Bauleiter/Architekt | Bautenstandsbestätigung, Abnahmeprotokoll, technische Freigabe, auf die der Erwerber zahlt |
| Notar | erkennbare MaBV-/AGB-Risiken, Freistellung, Preisanpassung, § 650m, Vormerkung, Belehrung und Dokumentation |
| Vertrieb | Prospektangaben zu Energie, Schall, Baugrund, Fertigstellung, Finanzierung oder Förderfähigkeit |

Keine pauschalen Vorwürfe. Jeder Vorwurf braucht Handlung, Zeitpunkt, Kenntnis, Adressat und Schaden.

### O.9 — Großkommentar-Check: anwendbar, ausgeschlossen, modifiziert

Bei jedem vollständigen Gutachten wird eine knappe Anwendungskarte gebaut:

| Vorschriftengruppe | Bauträger-Status |
| --- | --- |
| §§ 633 ff. BGB | für Errichtung/Umbau grundsätzlich anwendbar |
| § 640 BGB | Abnahme anwendbar; Abnahmefiktion bei Verbraucher nur mit Belehrung |
| § 650j BGB | Baubeschreibungspflicht nicht ausgeschlossen |
| § 650k Abs. 1 BGB | durch § 650u Abs. 2 ausgeschlossen; Baubeschreibung muss beurkundet/einbezogen werden |
| § 650k Abs. 2/3 BGB | weiter anwendbar |
| § 650l BGB | ausgeschlossen |
| § 650m Abs. 1 BGB | ausgeschlossen |
| § 650m Abs. 2/3 BGB | weiter zu prüfen |
| § 650n BGB | weiter zu prüfen |
| §§ 648, 648a, 650b bis 650e BGB | durch § 650u Abs. 2 ausgeschlossen |
| § 650v BGB i. V. m. §§ 3, 12 MaBV | Abschläge nur in MaBV-konformer Vereinbarung; MaBV-Pflichten dürfen vertraglich nicht zulasten des Erwerbers ausgeschlossen oder beschränkt werden |
| §§ 642, 643 BGB | bei Mitwirkungsfragen anwendbar, aber kein Pauschalventil für Bauträgerverzug |

### O.10 — Klauselmatrix: 25 harte Treffer

Die Matrix in Teil B ist bei Vollanalysen mindestens mit diesen Treffern abzugleichen:

| Treffer | Kernbefund |
| --- | --- |
| zwei Großraten oder Vorabrate ohne Bautenstand | MaBV-/AGB-rot |
| Schlussrate vor Besitzübergabe oder vollständiger Fertigstellung | MaBV-/Fälligkeitsproblem |
| `mitgeteilte` Bezugsfertigkeit/Fertigstellung | einseitige Fälligkeit, § 305c Abs. 2/§ 307 prüfen |
| Außenanlagen aus Fertigstellung ausgenommen | MaBV-rot |
| § 650m-Verzicht oder intransparenter Einbehalt | zwingender Verbraucherschutz |
| Baugenehmigung fehlt, Eigenbestätigung ungeprüft oder Schwarzbauverdacht | allgemeine Fälligkeitsvoraussetzung offen |
| Vormerkungslöschung per Bauträgervollmacht | § 309 Nr. 2 lit. a/Nr. 12/§ 307 prüfen |
| Beweislastumkehr/Empfangsbestätigung | § 309 Nr. 12 lit. a/b |
| Mängelrügefrist, Verjährungsverkürzung, Selbstvornahmeausschluss | Mängelrechte entwertet |
| Abnahme durch Erstverwalter, Tochter, Sachverständigen oder Vertreter | Eigenrecht des Erwerbers fehlt |
| Wohnflächen-/Schallschutz-/Energiestandard-Lücken | Bausoll konkretisieren |
| anerkannte Regeln zum Vertragsschluss statt Abnahme | Standardrisiko verschoben |
| Preisanpassung ohne Saldierung/Lösungsrecht | AGB-rot |
| Schlüssel nur gegen Vollzahlung trotz Mängeln | Druckmuster, § 253 StGB im Einzelfall prüfen |
| Besichtigungsausschluss/private Sachverständige ausgeschlossen | MaBV- und Abnahmeprüfung ausgehöhlt |
| zusätzliche Mahnpflicht trotz kalendarischem Termin | § 286-Leitbild unterlaufen |
| Bezugsfertigkeitsrate trotz gefährlichem Baustellenzugang | Bezugsfertigkeit fehlt; Verkehrssicherheit dokumentieren |
| Wohnflächentoleranz über 2 % | Rechtsprechungsstand live prüfen; konkrete Fläche, Methode und wirtschaftliche Auswirkung ausweisen |

### O.11 — Drei-Dokumente-Umsetzung

Mandantenanschreiben: klare Entscheidungshilfe zu Unterschrift, Zahlungsstopp, Nachverhandlung, Abnahme, Besitz oder Streit. Keine Normwand.

Gutachten: jedes Fachmodul wird dort behandelt, wo es hingehört: MaBV in F, AGB in G, Bausoll/Technik in H/J, Abnahme in I, Verzug in M, Haftung in N.

Schreiben an den Bauträger: keine akademische Vollständigkeit, sondern konkrete Streichungs- und Änderungsforderungen mit Alternativwortlaut; Notariat nur bei Beurkundungs-, Belehrungs- oder Vollzugspunkt in Kopie oder Zusatzabsatz.

## Teil P — Beratungsstellen-Schnellmodus (zeitknappe Verbraucherberatung)

Dieser Teil richtet sich an Beraterinnen und Berater in Verbraucherzentralen, Erwerberschutz- und Mietervereinen sowie kleinen Kanzleien, die solide Grundkenntnisse im Bauträgerrecht haben, aber wenig Zeit. Ziel: in kurzer Zeit ein korrektes, belastbares und versandfertiges Erstgutachten, das die eigene Kompetenz verstärkt statt sie zu ersetzen. Der Modus erfindet nichts dazu — er priorisiert und sequenziert die übrigen Teile.

### P.1 — Zeitbudget-Pfad (Richtwert 30 Minuten)

1. Fall-Fingerabdruck (ca. 5 Min): Parteien, Verbraucherstatus, Einheit, Preis, Ratenplan, Sicherheiten, Beurkundungs-/Bauphase, Fristen, Anlagen. Fehlendes als Annahme markieren, nicht zurückfragen.
2. Pflicht-Prüfblock zuerst (ca. 10 Min): die Punkte des Pflicht-Prüfblocks abarbeiten — sie tragen das Mandat (MaBV-Fälligkeit, 5-%-Sicherheit, Beweislast/Tatsachenbestätigung, Abnahme Gemeinschaftseigentum, Schlussrate, Teilungserklärung, Bausoll, Bauüberwachung).
3. Top-Risiken priorisieren (ca. 5 Min): die drei bis sieben Befunde mit der größten wirtschaftlichen oder fristbezogenen Wirkung nach vorn; Nebenschauplätze zurückstellen.
4. Nächste Weiche setzen oder Vollpaket erzeugen (ca. 10 Min): Käufer-/Mandantenschreiben, Mandantengutachten und Aufforderungsschreiben nach Teil L — direkt versandfertig, wenn Vollpaket gewählt wurde.

### P.2 — Entscheidungs-zuerst-Reihenfolge

Bei akutem Zeitdruck zuerst die fünf Fragen klären, die typischerweise über das Mandat entscheiden:

- Darf jetzt überhaupt gezahlt werden? (§ 3 Abs. 1 MaBV erfüllt, Vormerkung eingetragen, Freistellung vorhanden)
- Ist die 5-%-Sicherheit nach § 650m Abs. 2 BGB vorhanden oder unzulässig abbedungen?
- Bleibt das eigene Abnahmerecht für Sonder- und Gemeinschaftseigentum erhalten?
- Wird die Schlussrate erst bei vollständiger Fertigstellung einschließlich Außenanlagen fällig?
- Steht ein Termin (Beurkundung, Zahlung, Abnahme, Klage-/Rücktrittsfrist) an, der eine Sofortmaßnahme erzwingt?

### P.3 — Korrektheitssicherung für Nicht-Spezialisten

- Pflicht-Prüfblock und Bug-Hunt sind das Mindestgerüst; nichts davon auslassen, auch unter Zeitdruck.
- Drei Ebenen trennen: gesichert (Norm oder verifizierte Rechtsprechung), Argumentationslinie, prüfbedürftig. Im Zweifel als prüfbedürftig kennzeichnen statt zu überdehnen.
- Keine Fundstelle erfinden; Rechtsprechung nur mit zulässiger Quelle, sonst als zu verifizieren ausweisen.
- Jede rote oder orange Ampel braucht Klauselstelle, konkreten Betrag/Frist/Einheit und eine gewünschte Fassung.

### P.4 — Wann an Spezialisten oder Sachverständige abgeben

Im Gutachten klar vermerken, wenn ein Punkt vertiefte Spezial- oder Sachverständigenprüfung braucht: Baugrund-, Statik-, Brandschutz- oder Bauphysikfragen, komplexe Insolvenz- und Sicherungslagen, Notarhaftung, hohe Streitwerte, gerichtliche Eilbedürftigkeit. So bleibt das Schnellgutachten ehrlich und haftungsbewusst und überschreitet nicht die eigene Prüftiefe.

### P.5 — Versandfertigkeit (Selbstcheck vor Abgabe)

- Ergebnis in einem Satz und Ampel-Bilanz vorhanden?
- Drei bis sieben priorisierte Hauptrisiken mit konkreter Handlungsempfehlung?
- Fristen und Sofortmaßnahmen benannt?
- Nachforderungsliste für fehlende Unterlagen?
- Mandantenanschreiben in einfacher Sprache, ausführliches Gutachten mit Quellen, Bauträgerschreiben mit konkreten Neufassungen und Notariat nur bei Urkunds-/Vollzugspunkt?

## Bug-Hunt vor Ausgabe

Vor jeder finalen Analyse diese Fehler ausschließen:

- `§ 309 Nr. 15` nicht für Beweislast oder Empfangsbestätigung verwenden; richtig ist § 309 Nr. 12.
- `§ 650m Abs. 1` nicht auf Bauträgervertrag anwenden; er ist durch § 650u Abs. 2 ausgeschlossen.
- `§ 650m Abs. 2` nicht als bloß analog darstellen; § 650u Abs. 2 schließt ihn nicht aus.
- Keinen `§ 650v Abs. 4 BGB` zitieren; § 650v hat keine Absätze. Für die zwingende Ratenlogik § 650v BGB i. V. m. §§ 3, 12 MaBV, für Verbraucherbauvorschriften § 650o BGB und für Abschläge/Sicherheit in AGB § 309 Nr. 15 BGB prüfen.
- `§ 650k Abs. 1` nicht als Bauträger-Hauptargument verwenden; er ist ausgeschlossen.
- `§ 650k Abs. 2/3`, § 650j, § 650n nicht übersehen.
- MaBV nicht als dreizehn gesetzliche Einzelraten beschreiben; richtig: bis zu sieben Teilbeträge, zusammensetzbar aus Bausteinen.
- § 7 MaBV nicht als `Vertragssumme + 5 %` behaupten; richtig: alle Rückgewähr-/Auszahlungsansprüche bis § 3 Abs. 1 und vollständige Fertigstellung.
- AGB-Unwirksamkeit nicht automatisch zu Gesamtnichtigkeit machen; § 306 BGB ist Regelfolge.
- Keine BeckRS-/juris-/Kanzleiblog-Fundstellen zitieren.
- Keine BGH-Entscheidung ohne zulässige URL und Liveprüfung.
- Keine schrillen Drohungen ohne Tatbestand; Verhandlungsposition soll streng, aber glaubwürdig sein.
- 🔴 nicht für bloß fehlende Unterlagen, offene Tatsachen oder reine Verhandlungswünsche verwenden; solche Punkte bleiben 🟠, bis ein erheblicher Rechts-, Fälligkeits-, Sicherungs- oder Projektrisikobefund konkret belegt ist. 🟢 nie als pauschale Wirksamkeitsgarantie formulieren.
- Jede rote Ampel muss eine konkrete gewünschte Änderung haben.
- Statuskopf nicht vergessen: Rolle, Vertragsphase, Modus, Befundregister, Weiche und Dokumente 1 bis 3 müssen als offen/erledigt oder nächster Schritt markiert sein.
- Befundregister nicht zwischen Kurzbild, Gutachten und Bauträgerschreiben neu erfinden: Befund-IDs, Ampeln, Quellenstatus und Vertragsphase müssen konsistent bleiben.
- Jede rote oder orange Ampel muss das Subsumtions-Gate bestehen: Textstelle, Wirkung, Rechtsfolge, Beweislast und Gegenargument.
- Fehlende Unterlagen nicht vorschnell als bewiesenen Mangel verkaufen; sauber zwischen Unterlagenlücke, Aufklärungsdefizit, Fälligkeitssperre, Sachmangel und AGB-Risiko trennen.
- Technik nicht hinter Jura verstecken: Baugrund, Baugrube, Objektüberwachung, private Sachverständige, LPH 8, Unterlagen, Wartung und Betriebskosten immer mitprüfen.
- HOAI nicht als Direktanspruch des Erwerbers gegen den Bauträger-Architekten ausgeben; als Organisations- und Plausibilitätsraster verwenden.
- Keine MaBV-Rate allein aufgrund interner Bauleiterbestätigung akzeptieren, wenn dem Erwerber jede objektive Bautenstandskontrolle abgeschnitten wird.
- Private Bauüberwachung nicht mit freiem Baustellenzutritt verwechseln; sachgerechte Lösung ist angemeldeter, sicherheitskonformer Zutritt mit eigenem Sachverständigen.
- DIN-Normen nicht als automatische anerkannte Regeln der Technik ausgeben; Einzelfall und Senatsdifferenzierung live prüfen.
- Vollständige Fertigstellung nie mit Bezugsfertigkeit, Abnahme oder Schlüsselübergabe gleichsetzen.
- Schlussrate vor Außenanlagen, Restarbeiten am Gemeinschaftseigentum oder protokollierten Mängeln nicht vorschnell als fällig behandeln.
- Preisanpassung ohne Saldierung, Kalkulationsoffenlegung und gesichertes Lösungsrecht nicht als `marktüblich` akzeptieren.
- Bauablaufargumente (`Pandemie`, `Lieferketten`, `Wetter`, `GU-Insolvenz`) nie ohne Bauablaufplan, Gewerkbezug und Wiederanlaufzeit durchgehen lassen.
- § 650l BGB-Widerruf nicht beim beurkundeten Bauträgervertrag versprechen.
- Bauhandwerkersicherung nach § 650f BGB nicht vom Verbraucher-Erwerber verlangen.
- Baugruppen-GbR nicht mit Bauträgermaßstäben prüfen; keine MaBV anwenden, dafür § 311b BGB, MoPeG-Haftung und Nachschüsse prüfen.
- Die zehnjährige Verjährung des einheitlichen Bauträgervergütungsanspruchs nach §§ 196, 200 BGB und BGH VII ZR 231/22 nicht mit der fünfjährigen Verjährung von Erwerber-Mängelansprüchen nach § 634a Abs. 1 Nr. 2 BGB vermischen.
- Beweislastumkehr und Empfangsbestätigung immer § 309 Nr. 12 lit. a/b BGB zuordnen, nicht § 309 Nr. 15.
- Schlüsselverweigerung trotz Mängeln nicht als bloße Vertragsfrage abhandeln; Besitzdruck, Zurückbehaltungsrecht und § 253 StGB im Einzelfall prüfen.
- Persönliche Haftung von Geschäftsführer, Bauleiter, Vertrieb oder Notar nur mit Handlung, Kenntnis, Pflichtverletzung und Schaden ausgeben.
- Nicht belegte Rechtsprechungslinien als Prüfbedarf markieren; keine Aktenzeichen, Daten oder Zitate erfinden.
- Nach Beurkundung kein reines `Entwurf bitte ändern`-Schreiben ausgeben; Nichtanwendung, Fälligkeit, Einbehalt, Erfüllung, Abhilfe und einen gegebenenfalls formbedürftigen Nachtrag unterscheiden.
- `Anbei` oder `beigefügt` nur schreiben, wenn tatsächlich eine gesonderte Anlage oder Datei erzeugt wird; im fortlaufenden Chat auf das `nachfolgende Gutachten` verweisen.
- Auch im Vollpaket keine Beanstandung erfinden: Bei ausschließlich 🟢 Befunden in Dokument 3 keine zwingende Korrektur verlangen; reine 🟠 Punkte als Klarstellungs- oder Verhandlungswünsche kennzeichnen.

> **Ende des Skills.** Bei Anwendung: Vertrag einfügen. Der Skill startet mit Pflicht-Prüfblock, arbeitet die 30 Prüfschleifen ab, zitiert nur zulässige Quellen und liefert ein verhandlungsfähiges Verbraucherpaket.
