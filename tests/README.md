# Testakten: getrennte Eingaben und belegbare Erwartungen

Diese Tests prüfen die konkrete Vertrags- und Aktenarbeit: liest ein System die Word-Datei einschließlich Baubeschreibung, unterscheidet es Entwurf und späteren Sachverhalt, findet es relevante Klauseln und widersprüchliche Nachweise und rechnet es mit dem richtigen Kaufpreis? Die Fallnamen enthalten keine vorgegebene Rechtsbewertung.

## Einen Lauf durchführen

1. Einen frischen Chat öffnen. Einen der eigenständig verwendbaren Werkstatt-/Mini-Prompts oder die passende Plugin-Funktion starten. Hersteller, Modellversion, Datum, Promptversion, aktivierte Dateiauswertung und Recherchezugang notieren.
2. In [szenarien.json](szenarien.json) ein Szenario wählen. Nur die dort genannten `inputs` und Vertragsdateien übergeben; `erwartungsmatrix.md`, `erwartungen.json` und READMEs nicht hochladen. Für Entwurfsfälle zuerst tatsächlich DOCX verwenden. Der jeweilige Sachverhalt enthält den Arbeitsauftrag.
3. Antwort unverändert sichern und vom Auswerter anhand der [Erwartungsmatrix](erwartungsmatrix.md) bewerten. Nicht während der Prüfung verraten, welche Klausel oder welcher Zahlenwert erwartet wird.
4. Den gleichen Fall mit identischen Dateien und einem anderen Prompt/Modell wiederholen. Zusätzlich dieselbe Word-Prüfung mit dem inhaltlich entsprechenden Markdown durchführen. Abweichende Fundstellen wegen Seitenumbrüchen sind zulässig; verlorene Tabellen, Anlagen oder Inhalte sind es nicht.

Word-Fälle dürfen nicht stillschweigend auf eine andere Quelle wechseln: Kann ein Modell DOCX nicht vollständig lesen, muss es die Einschränkung benennen. Für einen Ersatzlauf kann ausdrücklich Markdown/PDF bereitgestellt werden; dieser gilt dann nicht als erfolgreicher Word-Lauf. Eine bearbeitete Word-Ausgabe muss den Entwurfsstatus und das freie Haupt-UR-Feld bewahren. Bezugsurkunden dürfen ihre eigenen Nummern behalten. Keine erfundenen Kommentare, Änderungsmarkierungen, Signaturen oder Prüfergebnisse.

Ein direkt hochladbares Paket mit neutraler Dokumentliste und ausschließlich den vorgesehenen Eingaben erzeugen:

```sh
python3 tests/prepare_case.py --scenario H-E --out /tmp/bautraeger-pruefung-h-e
python3 tests/prepare_case.py --scenario M-Z+ --out /tmp/bautraeger-pruefung-m-z-plus
```

Das Zielverzeichnis darf noch nicht existieren. Das Werkzeug kopiert die aktuelle Vertragsdatei und die zugehörigen Eingaben; es verändert keine Quelle und kopiert weder Fall-README noch Erwartungsschlüssel. Word-Entwurfsfälle sind ausdrücklich DOCX-only. Die Kennung der negativen Lindenhain-Fortsetzung lautet für den Aufruf `L-Z-` (ASCII-Minus).

## Umfang

| Szenarien | Prüft insbesondere |
| --- | --- |
| H-E, M-E, L-E | tatsächliche Word-Auswertung, Anlagen, Entwurfsstatus, phasengerechte Änderungen |
| H-Z, M-Z, L-Z | Rechnung, allgemeine Fälligkeit, Bautenstand, Belegstatus, Sicherheit |
| M-Z+, L-Z+ | günstige Zusatzinformationen: eine tragfähige Zahlungsentscheidung muss möglich bleiben |
| L-Z− | spätere konkrete Gegenfeststellung trotz zunächst positivem Bericht |
| M-A | Abnahmepflicht und Abnahmefiktion bei unwesentlichem Mangel auseinanderhalten |
| L-S | Sonderwunsch, Formfrage, erhöhte Vergütung und zusätzliche Sicherheit |
| L-W | deutsch-englische Word-Fassung, Anlage, konkrete Unklarheiten ohne erfundene Abweichung |

Alle drei Hauptverträge bleiben Entwürfe. Die Zahlungs- und Abnahmeszenarien unterstellen den Vertragsschluss für eine spätere Phase ausdrücklich. Diese Übungsannahme beweist keinen realen Vollzug. Die Kalenderdaten 2027/2028 sind fiktive Prüfzeitpunkte; die Matrix basiert auf den am 4. September 2026 nachgeschlagenen Normen. Bei einem späteren Einsatz ist der dann geltende Rechtsstand zu prüfen.

## Bewertung

Jeder Sollbefund erhält 0, 1 oder 2 Punkte: 0 = fehlt/falsch; 1 = Problem erkannt, aber Quelle, Folgerung oder Abhilfe unvollständig; 2 = konkrete Fundstelle, zutreffende Unterscheidung und brauchbare Maßnahme. Kritische Fehler werden separat gezählt: erfundene Beurkundung oder Unterlagenprüfung, Zahlungsfreigabe trotz dokumentiert fehlendem Meilenstein, falscher Eurobetrag, Übernahme eines Ausschlusses gesetzlicher Rechte oder erfundene technische Messwerte/Urteile. Eine hohe Gesamtpunktzahl kompensiert solche Fehler nicht.

Für jede Antwort festhalten: erfüllte Befund-IDs, Fehlalarme, kritische Fehler, offene Recherche-/Dateigrenzen und erforderliche fachliche Nachprüfung. Die Matrix ist ein begründeter Erwartungskorridor; zusätzliche belegte Befunde sind erlaubt. Eine pauschale Farbe pro Akte, eine bloße Schlüsselwortsuche in Modellantworten oder reine Selbsteinschätzung ersetzt die Auswertung nicht.

## Lokale Konsistenzprüfung

```sh
python3 tests/verify_testakten.py
```

Der Prüfer kontrolliert Szenarioverweise, Beleganker, Raten in den Vertragsquellen, Kaufpreis-/Abrufbeträge und Eurorechnungen einschließlich der Sonderwunschvariante. Er führt **keine KI-Vertragsprüfung** aus und bescheinigt weder juristische Richtigkeit jeder Klausel noch gute Modellleistung. DOCX-Erzeugung und Artefaktkontrollen erfolgen zusätzlich über die Repository-Buildprüfungen.

Die [Praxisprüfung vom 4. September 2026](runs/2026-09-04/README.md) enthält zwei abgeschlossene Codex-Einzeltests mit unveränderten Antworten, Eingabedateihashes und nachträglicher Auswertung sowie eine separat gekennzeichnete vorläufige positive Gegenprobe. Die [Artefakt-QA](QA-4.4.0.md) dokumentiert die Werkzeug- und Dateikontrollen. Live-Erfolge mit fremden KIs werden nicht behauptet.

Die [gezielten Verjährungsfälle](limitation/README.md) ergänzen sieben isolierte Ausschnittsprüfungen: direkte Fristverkürzung, technische Bauteile/VOB-B-Verweis, vorgezogener Beginn und verdeckte Anzeigefrist sowie drei Kontrollen gegen Fehlalarme. Eingaben und Auswerterschlüssel bleiben getrennt. Die statischen Kontrollen von `scripts/test_limitation_controls.py` ersetzen keine tatsächlichen Blindläufe.

Die [Mehrturn-Szenarien](workflow/README.md) prüfen ab Fassung 4.5.0 echte Gesprächsfolgen. Folgeeingaben werden erst nach der vorherigen Antwort übergeben, anders als bei den bisherigen zusammengefassten Ergänzungsszenarien. Die [Dialogproben vom 15. September 2026](runs/2026-09-15/README.md) enthalten drei tatsächlich ausgeführte Verläufe mit neun unveränderten Antworten und einer getrennten Bewertung. Nicht ausgeführte Fälle bleiben ausdrücklich als solche benannt.
