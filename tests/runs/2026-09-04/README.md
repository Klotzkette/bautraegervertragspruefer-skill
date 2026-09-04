# Praxisprüfung der Fassung 4.4.0

Am 4. September 2026 wurden neutrale Eingabepakete in frischen Codex-Unteragenten geprüft. Die konkrete Modellkennung wurde nicht separat protokolliert; dies ist **kein Vergleich verschiedener KI-Anbieter**. Die Unteragenten erhielten den Prüfauftrag, den jeweils angegebenen Prompt bzw. Plugin-Einstieg und ausschließlich die vorgesehenen Eingaben. Erwartungsmatrix, Fall-README und Lösungsschlüssel waren nicht Teil ihres Auftrags. Die Auswertung erfolgte anschließend durch den bearbeitenden Hauptagenten, nicht durch einen unabhängigen juristischen Gutachter.

## Gesicherte Antworten und Auswertung

| Lauf | Anleitung | Ergebnis im begrenzten Szenario | Status |
| --- | --- | --- | --- |
| [H-Z: unveränderte Antwort](h-z-mini.md) | Mini-Prompt 4.4.0-mini | 156.492 EUR rechnerisch richtig, wegen konkret unvollständiger Leistungsgruppe nicht fällig; 22.000 EUR Reservierung nicht automatisch angerechnet; 41.400 EUR Sicherheit nicht doppelt abgezogen | Antwort abgeschlossen und ausgewertet |
| [M-E: unveränderte Antwort](m-e-plugin.md) | Vertrags-Skill → Werkstatt und Word-Skill | Gesamte DOCX samt Baubeschreibung ausgewertet; falsches Wesentlichkeitserfordernis in § 6.2 erkannt, konkrete Ersatzregel; tragfähige Schutzklauseln und begrenzter Preisänderungsmechanismus differenziert gewürdigt | Antwort abgeschlossen und ausgewertet |
| [M-Z+: gesicherte vorläufige Antwort](m-zplus-vorlaeufig.md) | Werkstatt-Prompt 4.4.0 | 127.386 EUR auf ausdrücklich ergänzter Tatsachengrundlage zahlbar; keine zusätzliche 5-%-Kürzung; fremde Belegprüfung nicht als eigene Einsicht ausgegeben | Explorativ: Antwortdatei vorhanden, nachfolgender Agentenabschluss durch Nutzungsgrenze unterbrochen; kein abgeschlossener Vergleichslauf |

Auswertung anhand der [Erwartungsmatrix](../../erwartungsmatrix.md), jeweils 0–2 Punkte pro Befund:

- **H-Z:** A02, A03, A04, H02, H03, H09, H10, H11 jeweils 2 Punkte (16/16 innerhalb dieses Erwartungskorridors). Konkrete Gegenbelege aus dem Bericht werden mit der dritten Rate verbunden; die zeitnahe Einwendung wird von einer eigenmächtigen Vertragsbeendigung getrennt. Kein beobachteter kritischer Fehler in diesen Sollbefunden.
- **M-E:** A01, A02, A03, A04, M01, M02, M03, M04 jeweils 2 Punkte (16/16 innerhalb dieses Erwartungskorridors). Enthalten sind die konkrete 3-%-Schwelle von 20.220 EUR, technische Anlagenwerte, die 17 Tage der vorgegebenen Vorbereitung und phasengerechte Entwurfsänderungen. Kein beobachteter kritischer Fehler in diesen Sollbefunden. Zusätzliche offene Punkte werden als aufklärungsbedürftig, nicht als bewiesene Baufehler behandelt.
- **M-Z+:** Die gespeicherte Antwort erfüllt inhaltlich die positive Gegenprobe: A02/A03/A04 sowie M05/M07 sind erkennbar umgesetzt. Wegen des unterbrochenen Agentenabschlusses wird kein regulärer Punktwert oder abgeschlossener Live-Erfolg gezählt.

Diese Bewertung bescheinigt nicht die Fehlerfreiheit aller zusätzlichen Ausführungen oder die rechtliche Eignung für eine echte Transaktion. Die beiden abgeschlossenen Einzelantworten sind qualitative Stichproben, keine statistische Leistungsbewertung.

## Datei- und Rechercheumfang

H-Z nutzte die DOCX-Textstruktur unmittelbar; keine gerenderte Word-Seitenansicht. M-E nutzte den Plugin-Extraktor und sah zusätzlich alle 25 gerenderten deutschen Word-Seiten an. Beide Antworten nennen ihre Lesegrenzen und verwendeten amtliche Rechtsquellen. Originale bloß erwähnter Garantien, Notarmitteilungen, Fotos und Protokolle wurden ihnen nicht nachträglich zugespielt. Die Modellantworten enthalten direkte Links zu den recherchierten Normen; aktuelle Abrufbarkeit beweist keinen zukünftigen Rechtsstand der fiktiven Szenarien 2027/2028.

Die neutralen Text-Eingaben sind unter `tests/inputs/` und in den Szenarioverweisen versioniert. Die temporären Word-Eingaben stammen aus derselben inhaltlichen Vertragsfassung vor dem abschließenden Layout-Nachbau. Ihre Dateihashes können wegen neu erzeugter Dokumentmetadaten vom endgültigen Download abweichen. Es wurde kein Erfolg mit einer ungelesenen finalen Word-Datei nachträglich behauptet; deren Text-/Layoutkontrolle ist im [Artefaktprüfbericht](../../QA-4.4.0.md) separat dokumentiert. Die [Lauf-Metadaten](metadata.json) halten die tatsächlichen Eingabedateihashes fest.

Noch offen sind systematische Wiederholungen aller zwölf Szenarien, direkte Werkstatt-/Mini-Vergleiche mit identischen Eingaben, DOCX-/Markdown-Paarvergleiche, echte Fremdmodelltests und unabhängige juristische Nachprüfung. Die Testpakete sind dafür vorbereitet; nicht ausgeführte Tests zählen nicht als bestanden.
