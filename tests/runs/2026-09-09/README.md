# Verjährungskontrolle 4.4.1

## Tatsächlich ausgeführter Mini Lauf

Ein neuer Codex-Agent erhielt ausschließlich den vollständigen Mini-Prompt 4.4.1 und die sieben neutralen Kurzfälle V01–V07. Er hatte weder Langfassung noch Erwartungsschlüssel oder frühere Antworten. Die [Rohantworten](mini-kurzfaelle-raw.md) enthalten Prompt- und Eingabeprüfsummen sowie Quellen- und Ausführungsgrenzen. Diese Datei ist die davon getrennte nachträgliche Auswertung anhand von `tests/limitation/erwartungen.json`.

Die sieben Sachverhalte wurden in einem gemeinsamen Agentlauf getrennt geprüft. Das ist eine gegenüber den Erwartungen blinde Sammelprobe, **nicht** sieben frische Chats nach dem strengeren Protokoll. Es gab keinen Lauf bei einem externen KI-Anbieter und keinen Modellvergleich. Das Ergebnis belegt die beobachteten Antworten, keine allgemeine Zuverlässigkeitsquote.

| Fall | Beobachteter Kernbefund | Fehlalarmkontrolle |
| --- | --- | --- |
| V01 | Zweijahresklausel für Neubau ausdrücklich nach § 309 Nr. 8 b ff als unwirksam erkannt; fünf Jahre ab Abnahme und § 306 Abs. 2 genannt; Individual-Etikett heilt nicht; Ersatztext geliefert | Haftungsausnahmen nicht als Heilung angesehen; keine Gesamtnichtigkeit |
| V02 | Vierjahresfrist und technische Zweijahresfrist jeweils beanstandet; VOB/B-Bezug gegenüber Verbraucherin nicht privilegiert; beide Klauseln korrigiert | Bauwerksbezug entsprechend Sachverhalt gewürdigt, nicht allein nach Anlagenbezeichnung entschieden |
| V03 | Nominelle fünf Jahre nicht ungeprüft freigegeben; fremde Erstabnahme als unzulässiger Frühbeginn erkannt und erwerberbezogenen Ersatz vorgeschlagen | Kein erfundenes eigenes Ablaufdatum und keine pauschalen 30 Jahre |
| V04 | Richtige Frist in § 11.1 und rechtsvernichtende Anzeigeklausel in § 11.2 getrennt; § 309 Nr. 8 b ee/ff angewandt, Ausschlussfolge gestrichen | Keine automatische Hemmung durch Mängelanzeige behauptet; nicht zusätzlich pauschal die Schriftform eines Notarvertrags verworfen |
| V05 | Gesetzliche fünf Jahre und eigene beziehungsweise wirksam vertretene Abnahme positiv bewertet | Kein künstlicher Änderungsbedarf oder vollständige Vertragsfreigabe |
| V06 | Fahrradreparatur als sachbezogenes Werk nach § 634a Abs. 1 Nr. 1 mit zwei Jahren ab Abnahme eingeordnet | Keine Übertragung der Fünfjahresfrist auf sämtliche Verbraucherwerkverträge |
| V07 | Vorgegebenes echtes Aushandeln von AGB unterschieden; kein universelles Verbot aus § 634a/§ 650o; § 202 und § 639 als Grenzen genannt | Keine uneingeschränkte Wirksamkeitsbescheinigung; fünf Jahre als Verhandlungswunsch statt zwingende Rechtsfolge bezeichnet |

In diesen Antworten wurden alle vier gezielt problematischen Regelungsmechanismen erkannt; bei den drei Gegenfällen wurde die jeweils untersuchte zulässige beziehungsweise nicht pauschal verbotene Gestaltung nicht allein wegen Verbraucherbeteiligung beanstandet. Der Auswerter hat die Rohantworten nicht nachträglich verbessert. Die Auswertung ersetzt keine unabhängige anwaltliche Fachbegutachtung.

Die Fälle enthalten keine DOCX-Dateien und keine vollständige Bauträgerakte. Die Antworten sind deshalb kein erneuter Praxistest der Word-Aufnahme oder aller MaBV-Rechenschritte. Vorhandene Word-Artefaktkontrollen und frühere Vollaktenläufe bleiben separat dokumentiert.

## Tatsächlich ausgeführter Werkstatt Lauf

Ein weiterer neuer Codex-Agent erhielt ausschließlich die Langfassung 4.4.1 und V01/V04. Er sah weder Mini noch Erwartungen oder die vorstehenden Mini-Antworten. Seine [unveränderten Rohantworten](werkstatt-kurzfaelle-raw.md) dokumentieren Eingaben, Prüfsummen und Quellenzugriff. Auch hier wurden zwei Sachverhalte getrennt im selben Agentenkontext bearbeitet, nicht zwei technisch isolierte Chats.

V01: Die Werkstattantwort erkannte die Zweijahresklausel unmittelbar als unwirksam nach § 309 Nr. 8 b ff, ordnete fünf Jahre ab maßgeblicher Abnahme zu, verwarf die Heilung durch Individual-Etikett und Notarbelehrung und lieferte Ersatztexte sowie § 306 als Rechtsfolge. V04: Sie unterschied die richtige Grundfrist von der versteckten Ausschlussfrist, wandte ausdrücklich ee in Verbindung mit ff an und beseitigte den Anspruchsausschluss durch eine konkrete Ersatzregelung. Keine pauschale Gesamtnichtigkeit, Vollvertragsfreigabe oder automatische Hemmung durch Mängelanzeige wurde behauptet.

Damit wurden auch in der Langfassung die beiden getesteten Fehlermechanismen tatsächlich erkannt. Für V02/V03/V05/V06/V07 ist hier kein zusätzlicher Werkstattlauf dokumentiert. Die gesetzesgestützten Antworten zitieren keine als geprüft ausgegebene, tatsächlich ungelesene Rechtsprechung. Das ist kein herstellerübergreifender Test.

## Automatische Kontrollen

`scripts/test_limitation_controls.py` kontrolliert explizite Prüfinhalte, Spiegel und Fixture-Trennung. `scripts/test_prompt_layout.py` kontrolliert verlustfreie Formatumwandlung, Frontmatter, Code-Fences und vollständige Rechtsprechungsdatensätze. Beides sind Struktur- beziehungsweise Programmkontrollen, keine automatischen Beurteilungen juristischer KI-Antworten.
