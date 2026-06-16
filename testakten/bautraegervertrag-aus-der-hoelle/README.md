# Testakte „Bauträgervertrag aus der Hölle"

Diese Akte ist **vollständig fingiert** und dient ausschließlich Schulungs- und Testzwecken für den Bauträgervertrag-Prüfer-Skill. Alle Namen, Daten, Adressen, Aktenzeichen, UR-Nummern, Banken, Notariate und das Projekt sind frei erfunden. Reale Personen, Unternehmen oder Notariate sind nicht gemeint.

## Worum es geht

Ein fiktiver Wohnungsbauträgervertrag mit Auflassung für eine Eigentumswohnung in einem fiktiven Großprojekt zwischen Stahnsdorf und Kleinmachnow. Vertrag und die zugehörige (nur lose übergebene) Baubeschreibung enthalten zusammen rund **40 versteckte Fehler** — von schweren MaBV-Verstößen über AGB-Klauselfallen nach §§ 305 ff. BGB bis zu Druckmustern gegen die dingliche Sicherung, technische Baukontrolle, Baugrundrisiken, HOAI-/Objektüberwachungslogik, lückenhaftem Bausoll und späteren WEG-Betriebskosten. Die Fehler sind nicht durch Hervorhebung markiert, sondern in einen handwerklich solide aussehenden Vertragstext eingewoben, wie er in der Beratungspraxis tatsächlich vorkommt.

Die Testakte erlaubt es,

- den Skill an einem realistischen, komplexen Beispielvertrag zu erproben,
- die eigene Klauselanalyse mit dem mitgelieferten Lösungs-Gutachten zu vergleichen,
- die Pflicht-Prüfblock-Logik durchzuspielen und gegen die im Vertrag platzierten Fallen zu prüfen,
- die Gutachten- und Korrespondenzstruktur als Ausgabevorlage zu studieren.

## Inhalt

Die Akte besteht aus vier Dokumenten, jeweils in drei Formaten verfügbar:

1. **Wohnungsbauträgervertrag mit Auflassung** (`01-bautraegervertrag.md`)
   — Die fingierte notarielle Urkunde mit Vorbemerkungen, §§ 1–14, Bezugsurkunden- und Anlagenverzeichnis, Geschäftswert-/Kostenvermerk und Unterschriften. Enthält die eingebauten Fehler.

2. **Korrespondenz, Aktenvermerk und Beweis-/Fristenlogik** (`02-korrespondenz-und-vollvermerk.md`)
   — Mandantenanfrage per E-Mail, interner Aktenvermerk, anwaltliche Strategie-Antwort, Beweis-/Fristen-Tabelle, fünfstufiger Eskalationsplan, Honorarauszug.

3. **Anwaltliches Gutachten — Lösungsschlüssel zur Testakte** (`03-gutachten-loesungsschluessel.md`)
   — Das vollständige Prüfgutachten mit Pflicht-Prüfblock, klauselgenauen rechtlichen und technischen Beanstandungen, Ampel-Bilanz, sieben Handlungsempfehlungen. **Anonymisierte Lehre**, keine konkreten Rechtsprechungsfundstellen.

4. **Baubeschreibung — Fassung Februar 2026, Version 7.2 (Auszug)** (`04-baubeschreibung-auszug.md`)
   — Die in der Urkunde referenzierte, aber bewusst *nicht mitbeurkundete* Baubeschreibung. Demonstriert die typischen Bausoll-Lücken (durchgehend „nach Wahl des Verkäufers", „einfache Art und Güte", leerer Schallschutzwert, kein konkreter Energiestandard, verkäuferfreundliche Widerspruchsregel). Die konkrete Auflösung dazu steht im Gutachten unter Nr. 17d.

## Formate

Jedes Dokument liegt vor als:

- **Markdown-Quelle** in `quellen/` — die maßgebliche Fassung, die du editieren würdest, wenn du die Akte erweitern willst.
- **PDF** in `gesamt-pdf/` — zum Lesen und Versenden.
- **Word-Dokument (.docx)** in `gesamt-docx/` — zum Annotieren und Weiterbearbeiten.

PDF und DOCX werden aus den Markdown-Quellen erzeugt. Nach einer Änderung in `quellen/` regenerierst du beide Formate mit dem mitgelieferten Build-Skript:

```bash
cd testakten/bautraegervertrag-aus-der-hoelle
./build.sh            # alle Dokumente
./build.sh 04         # nur die Baubeschreibung
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.

## Verwendung mit dem Skill

1. Öffne den Skill (Download über die Pages-URL des Repos).
2. Übergib dem Skill den Bauträgervertrag aus `quellen/01-bautraegervertrag.md` (oder das PDF) — möglichst zusammen mit der Baubeschreibung aus `quellen/04-baubeschreibung-auszug.md`, damit auch das Bausoll geprüft werden kann.
3. Vergleiche die Ausgabe des Skills mit dem Lösungs-Gutachten in `quellen/03-gutachten-loesungsschluessel.md`.
4. Erwartetes Ergebnis: Der Skill sollte den Pflicht-Prüfblock auslösen, mindestens 27 🔴-Befunde finden und eine strukturierte Risiko- und Technikmatrix liefern.

## Hinweis

Der Vertragstext ist absichtlich extrem verbraucherfeindlich, aber äußerlich professionell gehalten. Reale Bauträgerverträge sind selten so dicht mit Fallen versehen — aber jede einzelne der eingebauten Klauseln ist in der Praxis als Risiko denkbar. Die Akte verdichtet die Fehlerlogik zu einem Lehrstück.
