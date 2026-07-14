# Änderungsprotokoll

## 3.8.0 - 14. Juli 2026

Diese Fassung schließt 100 im Gesamt-Audit festgestellte Fehler- und Risikogruppen:

1. Der Ausführungskern verlangt nur noch eine vollständige Lektüre jedes Dokuments statt wiederholter Vollanalysen je Fachmodul.
2. Dokumentenkarte und Befundregister dienen als gemeinsame Tatsachenbasis für Kurzbild, Gutachten und Schreiben.
3. Dieselbe Klausel wird nicht mehr in parallelen Notizen mit widersprüchlichen Bewertungen geführt.
4. Stabile Befund-IDs verbinden Rechtsprüfung, tatsächliche Fälligkeit und konkrete Handlung.
5. Entscheidungserhebliche Quellenfragen werden vor der Recherche gesammelt und gebündelt geprüft.
6. Der geführte Erstbefund vertieft höchstens sieben priorisierte Punkte und bleibt dadurch auch in kleinen Chats vollständig.
7. Eine belastbare Erstsicht erscheint vor einer optionalen Live-Recherche, sodass fehlender Netzzugriff den Start nicht blockiert.
8. Lange Vollpakete setzen an einer festen Dokumentüberschrift fort, statt bereits ausgegebene Teile zu wiederholen.
9. Sachverhalt, Norm und Quelle werden im Drei-Dokumente-Paket nicht in jedem Dokument vollständig dupliziert.
10. Der Schnellpfad verwendet dasselbe Register wie die spätere Vollanalyse und erzeugt deshalb keinen zweiten Bewertungsstand.
11. Der redundante Fachmodul-Block in Teil O wurde entfernt.
12. Teil O ist jetzt ein kompakter Triggerindex zu den kanonischen Hauptteilen.
13. Jeder Trigger ergänzt eine bestehende Befund-ID, statt einen zweiten Befund zu erzeugen.
14. Der Triggerindex trennt Vollstreckung, Schlussrate, WEG, Technik, Insolvenz und Formfragen nach zuständigem Hauptpfad.
15. Die Schnellnavigation verweist auf den Triggerindex und nicht mehr auf den beseitigten Doppelblock.
16. Die inhaltlich doppelte Klauselzeile zur Wohnflächentoleranz wurde aus der AGB-Matrix entfernt.
17. Wohnflächenabweichungen bleiben in der präziseren Klauselzeile ohne erfundene starre Prozentgrenze prüfbar.
18. BGH VII ZR 388/00 ist als amtlicher Anker zur Vollstreckungsunterwerfung mit Nachweisverzicht aufgenommen.
19. Der Skill verwirft nicht jede notarielle Vollstreckungsunterwerfung, sondern prüft AGB-Charakter, Reichweite und Nachweisverzicht.
20. Das Risiko einer vollstreckbaren Ausfertigung vor MaBV- und Vertragsfälligkeit ist nun eigener Pflichtpunkt.
21. Die AGB-Matrix enthält für den Fälligkeitsnachweisverzicht eine konkrete Verhandlungsantwort.
22. Das Streitmodul verlangt bei drohender Vollstreckung Titel, Klausel, Zustellung, Fälligkeit und Eilrechtsschutz.
23. Das Verhandlungsmodul begründet, warum eine nachweislose Klauselerteilung den Erwerber unzulässig in die Verteidigungsrolle drängt.
24. Ein beiläufiger, nicht selbst verankerter Verweis auf VII ZR 99/97 wurde entfernt, statt als ungeprüfter Zusatzbeleg stehenzubleiben.
25. BGH V ZR 132/23 ist mit amtlichem PDF als Anker für Mehrhausanlagen und Untergemeinschaften aufgenommen.
26. Der Skill stellt klar, dass nur die Gesamt-GdWE Erwerberrechte zur alleinigen Durchsetzung an sich ziehen kann.
27. Räumliche Betroffenheit eines Hauses wird nicht mehr automatisch mit Prozessführungsbefugnis der Untergemeinschaft gleichgesetzt.
28. Beschluss, Anspruchsinhaberschaft, § 9a Abs. 2 WEG und konkrete Beschlussreichweite werden getrennt geprüft.
29. Prozessführung, Vergleichsverhandlungen und Finanzierung werden nach V ZR 132/23 dem richtigen Beschlussorgan zugeordnet.
30. BGH V ZR 75/18 ist mit amtlichem PDF als Anker zu Pflichten bauträgernaher Verwalter aufgenommen.
31. Ein Interessenkonflikt des Erstverwalters mindert dessen Informations- und Beschlussvorbereitungspflichten nicht.
32. Warnung vor Gewährleistungs- und Verjährungsrisiken ist nun eigener WEG-Prüfpunkt.
33. Bauträgernähe allein löst weiterhin keinen automatischen Haftungsbefund aus.
34. Verwaltervertrag, Kenntnis, Warnung, hypothetischer Beschluss, Kausalität und Schaden bleiben beweisbedürftig.
35. Gesamt-GdWE, Untergemeinschaft und bauträgernahe Verwaltung sind im Triggerindex gemeinsam, aber rechtlich getrennt aktiviert.
36. § 650n BGB enthält nun ausdrücklich die Ausnahme für wesentliche Planungsvorgaben des Verbrauchers oder seines Beauftragten.
37. Der Skill behauptet weiterhin keinen pauschalen Anspruch auf sämtliche internen Projektunterlagen.
38. Planungsunterlagen vor Ausführung und Ausführungsnachweise bei Fertigstellung bleiben zeitlich getrennt.
39. Die Mini-Fassung übernimmt die §-650n-Ausnahme trotz ihres Zeichenlimits.
40. Die Rechtsprechungsankertabelle ist von 40 auf 43 strukturierte Entscheidungszeilen erweitert.
41. Die Tabelle enthält jetzt 47 eindeutige Aktenzeichen und 47 eindeutige Quellenadressen.
42. Der Ankerprüfer verlangt V ZR 132/23, V ZR 75/18 und VII ZR 388/00 ausdrücklich.
43. Nicht in der Ankertabelle belegte Aktenzeichen führen weiterhin zu einem harten Fehler.
44. Die Mindestzahl der Anker wurde auf 43 angehoben, damit die neuen Schutzlinien nicht unbemerkt entfallen.
45. Amtliche BGH-Entscheidungen müssen weiterhin mindestens eine offizielle BGH- oder Bundesquelle besitzen.
46. Quellen werden nicht mehr nach einem bloß erfolgreichen HEAD-Request als geprüft behandelt, sondern mit genau einem inhaltlichen GET-Prüfpfad geöffnet.
47. PDF-Quellen werden dabei zusätzlich auf die PDF-Signatur `%PDF-` geprüft.
48. Leere Dokumentantworten werden als Quellenfehler erkannt.
49. Weiterleitungen auf nicht zugelassene Hosts werden abgewiesen.
50. HTTPS bleibt für jede Quellenadresse zwingend.
51. Nur vorübergehende HTTP-Fehler und Netzfehler werden mit kurzem Backoff wiederholt.
52. Der Online-Quellencheck arbeitet parallel statt 47 Adressen nacheinander abzurufen.
53. `BTV_URL_WORKERS` begrenzt die Quellenparallelität auf einen sicheren Bereich von 1 bis 12.
54. Ein ungültiger Wert für `BTV_URL_WORKERS` erzeugt eine verständliche Fehlermeldung statt eines Python-Tracebacks.
55. Die Skill-Version für den User-Agent wird nur einmal gelesen und zwischengespeichert.
56. Der User-Agent enthält dynamisch die tatsächlich geprüfte Skill-Version.
57. Parallele URL-Prüfungen behalten die Reihenfolge der Ankertabelle für reproduzierbare Fehlerberichte.
58. Zusätzliche amtliche Bundes- und Landesrechtsprechungsportale sind explizit allowlisted; technische Dokumentkennungen amtlicher Portale werden nicht mit verbotenen kommerziellen Zitaten verwechselt.
59. Der neue Strukturprüfer kontrolliert Voll- und Mini-Skill mit mehr als 1.000 Einzelprüfungen.
60. YAML-Metadatenversionen von Voll- und Mini-Skill werden unabhängig vom Shell-Validator abgeglichen.
61. Beide Skill-Dateien müssen genau eine H1-Überschrift besitzen.
62. Doppelte Überschriften werden automatisch erkannt.
63. Unzulässige Sprünge in der Überschriftenhierarchie werden erkannt.
64. Nicht geschlossene Markdown-Codeblöcke führen zu einem Fehler.
65. Isolierte Tabellenzeilen werden erkannt, ohne Tabellenbeispiele in Codeblöcken falsch zu beanstanden.
66. Jede echte Markdown-Tabelle braucht eine valide Trennzeile.
67. Uneinheitliche Spaltenzahlen innerhalb einer Tabelle werden erkannt.
68. Doppelte Bezeichnungen in der ersten Spalte derselben Tabelle werden erkannt.
69. Identische lange Fließtextblöcke werden als redaktionelle Dublette erkannt.
70. Die kanonischen Hauptteile müssen genau einmal und in richtiger Reihenfolge vorkommen.
71. Die 30 Prüfschleifen müssen lückenlos von 1 bis 30 nummeriert sein.
72. Kern-Gates für Start, Evidenz, Ratenrechnung, Zahlungsfreigabe und Drei-Dokumente-Ausgabe sind als Invarianten gesichert.
73. Die neuen WEG- und Vollstreckungsanker sind als Rechtsinvarianten gesichert.
74. Jedes im Mini-Skill zitierte Aktenzeichen muss auch in der Vollfassung verankert sein.
75. Der alte doppelte Teil-O-Titel darf nicht wieder eingeführt werden.
76. Der neue Teil-O-Triggerindex muss genau einmal vorhanden sein.
77. Die Mini-Fassung wird sowohl auf die Obergrenze von 7.500 Zeichen als auch auf offensichtliche Unvollständigkeit geprüft.
78. Der Mini-Skill enthält jetzt Einmal-Lektüre und ein einziges Befundregister als Ausgabebasis.
79. Der Mini-Skill bündelt Quellenfragen und startet weiterhin ohne Livezugriff.
80. Der Mini-Skill prüft die Vollstreckungsunterwerfung anhand VII ZR 388/00.
81. Der Mini-Skill ordnet die Bündelung in Untergemeinschaftsfällen der Gesamt-GdWE zu.
82. Der Mini-Skill verlangt die Warnung des bauträgernahen Verwalters vor Verjährungsrisiken.
83. Der Mini-Skill behält Kurzbild, Abschlussentscheidung, Nächste Weiche und alle drei Ausgabedokumente unter 7.500 Zeichen.
84. Sämtliche textbasierten Repository-Dateien werden auf gültiges UTF-8 geprüft.
85. UTF-8-BOMs werden repositoryweit erkannt.
86. NUL-Zeichen in Textdateien werden repositoryweit erkannt.
87. CRLF- und einzelne CR-Zeichen werden repositoryweit erkannt.
88. Fehlende finale Zeilenumbrüche werden repositoryweit erkannt.
89. Nachgestellte Leerzeichen werden repositoryweit erkannt.
90. Der Navigationsprüfer berechnet Link-Zeilennummern über einmalige Zeilenoffsets statt durch wiederholtes Vollscannen.
91. Die zuvor quadratische Zeilenzuordnung im großen Skill ist damit linearisiert.
92. Unbekannte URL-Schemata und protokollrelative Hosts werden als Navigationsfehler gemeldet.
93. Der Tiefen-Build erzeugt die drei Vertragsakten parallel in voneinander getrennten temporären Verzeichnissen.
94. Build-Ausgaben werden je Akte gesammelt und anschließend in stabiler Reihenfolge ausgegeben.
95. Fehlgeschlagene Buildskripte liefern ihren erfassten Standard- und Fehlertext mit der betroffenen Akte.
96. `BTV_BUILD_WORKERS` begrenzt die Buildparallelität; ungültige Werte werden verständlich abgewiesen.
97. Der vollständige Rebuild sank lokal von rund 10,1 auf rund 3,7 Sekunden bei unverändert zwölf Inhaltsvergleichen.
98. Der Manifest-Schreibpfad wiederholt ZIP- und Provenienzprüfungen nach erfolgreicher Vorprüfung nicht mehr unnötig.
99. Der Hauptvalidator verwendet pro Lauf ein eindeutiges temporäres Verzeichnis mit Cleanup statt kollisionsanfälliger fester `/tmp`-Dateien.
100. README, Pages-Downloadseite und Sync-Workflow dokumentieren den neuen Schnellpfad, den Strukturprüfer, die Parallelitätsregler und die neuen Rechtsanker; die Sync-Pipeline kopiert Vertragsformate über eine wartbare Schleife und verhindert parallele Läufe.

## 3.7.0 - 14. Juli 2026

Diese Fassung beseitigt die 30 größten im Gesamt-Audit verbliebenen Fehlergruppen:

1. Der Skill berücksichtigt BGH VII ZR 84/09: Mängel können auch bei einer laufenden Bautenstandsrate ein angemessenes Leistungsverweigerungsrecht auslösen.
2. Eine Verkäufermitteilung wird nicht mehr mit dem objektiv erreichten MaBV-Bautenstand gleichgesetzt oder schon für sich als unwirksam behandelt.
3. Der Skill erfindet kein allgemeines Recht auf freien Baustellenzutritt, sondern prüft Vertragsrecht, Sicherheitsorganisation und konkrete Vereitelungswirkung getrennt.
4. Fehlende private Sachverständigenkontrolle führt nicht mehr automatisch zu einem roten Befund.
5. HOAI-Leistungsphase 8 dient nur noch als Organisationsraster und wird nicht als eigener Direktanspruch des Erwerbers ausgegeben.
6. Baugrund-, Grundwasser- und Altlastenklauseln werden nach Gutachten, Aufklärung, Festpreis, Transparenz und tatsächlicher Risikowirkung bewertet.
7. § 650n BGB wird auf bedarfs- und zeitbezogene Behörden- oder Drittnachweise begrenzt; andere Unterlagen benötigen eine eigene Anspruchsgrundlage.
8. Fehlende Baugenehmigung und spätere genehmigungsabweichende Ausführung werden rechtlich getrennt geprüft.
9. MaBV-Raten werden nach Bausteinen, zulässiger Bündelung, Abrufzahl, Eurobetrag und kumulierter Vorleistung gerechnet, nicht nur nach Etiketten verglichen.
10. Die Mechanik des § 650m Abs. 2 Satz 3 BGB ist korrigiert: Auf Unternehmerverlangen wird die Sicherheit durch Einbehalt erbracht; Garantie oder Zahlungsversprechen bleiben möglich.
11. Die Freigabe der §-650m-Sicherheit richtet sich nach dem tatsächlich erreichten Sicherungszweck, nicht nach bloßem Abnahmeangebot oder pauschal nach fünf Jahren.
12. Nach Abnahme bleibt für die Mangelbestimmung zunächst das bei Abnahme geschuldete Vertragssoll maßgeblich; aktuelle Anforderungen verändern es nicht automatisch.
13. Der als 25-Punkte-Katalog bezeichnete Kontrollblock enthält nun tatsächlich 25 unterscheidbare Treffer.
14. Der Mini-Skill enthält die korrigierten Regeln zu Raten-Einbehalt, Sicherungsaustausch, Baustellenkontrolle, § 650n und Genehmigungsabweichung innerhalb des 7.500-Zeichen-Limits.
15. Der Validator verlangt die zentralen Rechtskorrekturen jetzt in Voll- und Mini-Fassung jeweils separat statt versehentlich nur in einer von beiden.
16. Der Rechtsprechungsvalidator verlangt mindestens 40 Anker einschließlich VII ZR 84/09 und kann alle 44 Quellen-URLs optional live abrufen.
17. Der Zweispalten-Generator übersetzt nun auch rein ASCII-geschriebene deutsche Tabellenzellen, vereinheitlicht die juristische Terminologie und versieht jede deutsch-englische HTML-, PDF- und DOCX-Fassung mit einem maschinenlesbaren SHA-256-Herkunftsnachweis ihrer deutschen Vertragsquelle.
18. Ein neues Provenienzgate verhindert, dass ein Manifest mit veralteten zweisprachigen Fassungen neu geschrieben wird.
19. Die drei Akten-ZIPs dürfen nur noch die jeweils zwei erwarteten, benannten und nicht leeren Einzel-PDFs enthalten; zusätzliche oder verschachtelte Dateien führen zum Fehler. DOCX-Seitenumbrüche sitzen jetzt an der folgenden Überschrift und erzeugen bei voller Vorseite keine Leerseite mehr; eine minimale geschützte PDF-Vorlage entfernt unbenutztes Pandoc-CSS und dessen Renderwarnung.
20. Die Vertretung der Marewald-KG erfolgt nun rechtssicher über die Geschäftsführung ihrer Komplementär-GmbH statt über eine Prokura ohne ausgewiesene Grundstücksbefugnis.
21. Marewald gibt die Fertigstellungssicherheit erst nach tatsächlicher Erreichung des gesamten Sicherungszwecks frei.
22. Die Marewald-Vorleistung wird vorbehaltlos angerechnet und erzeugt keine Verfall-, Anerkenntnis- oder Verzichtswirkung.
23. Der zusätzliche Marewald-Beratungsaufwand ist als transparenter Bruttopreis einschließlich Umsatzsteuer ausgewiesen.
24. Exposé, Visualisierung und Musterwohnung bleiben bei Marewald als vertragsbegleitende Auslegungsumstände erhalten; § 650k Abs. 2 BGB wird nicht formularmäßig leergeräumt.
25. Offene Marewald-Leistungsangaben werden am konkreten Komfort- und Qualitätsstandard statt an einem abstrakten Mindeststandard ausgerichtet.
26. Die starre Marewald-Wohnflächentoleranz samt Kürzung nur für den überschießenden Anteil ist durch eine bedeutungs- und wirkungsbezogene Regel ersetzt.
27. Erstmalige Erschließung und vertragsnotwendige Anschlüsse sind bei Marewald eindeutig im Festpreis enthalten.
28. Der Marewald-Haftungsausschluss für Grund und Boden wahrt grobe Fahrlässigkeit sowie Schäden an Leben, Körper und Gesundheit; die Umschreibung respektiert berechtigte Einbehalte bei insolvenzfester Sicherung.
29. Die Vertretung der Lindenhain-KG ist über eine bezeichnete Komplementär-GmbH berichtigt; die unzutreffende Selbstvertretung der KG ist beseitigt.
30. Lindenhain trennt nun schriftliche MaBV-Fälligkeitsmitteilung, Freistellung beim steckengebliebenen Bau, §-650n-Zeitpunkte, § 9a Abs. 2 WEG, § 321 BGB, Formprüfung von Sonderwünschen und den numerisch bestimmten Energiestandard präzise voneinander.

## 3.6.2 - 14. Juli 2026

- Rechtsprechungs- und Sicherheitenpräzisierung der Version 3.6.
- Ausbau der drei Vertragsakten und ihrer deutsch-englischen Lesefassungen.
