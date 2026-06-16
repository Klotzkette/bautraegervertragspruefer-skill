# Testakte „Bauträgervertrag aus der Hölle"

Diese Akte ist **vollständig fingiert** und dient ausschließlich Schulungs- und Testzwecken für den Bauträgervertrag-Prüfer-Skill. Alle Namen, Daten, Adressen, Aktenzeichen, UR-Nummern, Banken, Notariate und das Projekt sind frei erfunden. Reale Personen, Unternehmen oder Notariate sind nicht gemeint.

## Worum es geht

Ein fiktiver Wohnungsbauträgervertrag mit Auflassung für eine Eigentumswohnung in einem fiktiven Großprojekt zwischen Stahnsdorf und Kleinmachnow. Der Vertrag enthält rund **30 versteckte Fehler** — von schweren MaBV-Verstößen über AGB-Klauselfallen nach §§ 305 ff. BGB bis zu Druckmustern gegen die dingliche Sicherung des Erwerbers. Die Fehler sind nicht durch Hervorhebung markiert, sondern in einen handwerklich solide aussehenden Vertragstext eingewoben, wie er in der Beratungspraxis tatsächlich vorkommt.

Die Testakte erlaubt es,

- den Skill an einem realistischen, komplexen Beispielvertrag zu erproben,
- die eigene Klauselanalyse mit dem mitgelieferten Lösungs-Gutachten zu vergleichen,
- die Pflicht-Prüfblock-Logik durchzuspielen und gegen die im Vertrag platzierten Fallen zu prüfen,
- die Gutachten- und Korrespondenzstruktur als Ausgabevorlage zu studieren.

## Inhalt

Die Akte besteht aus drei Dokumenten, jeweils in drei Formaten verfügbar:

1. **Wohnungsbauträgervertrag mit Auflassung** (`01-bautraegervertrag.md`)
   — Die fingierte notarielle Urkunde mit Vorbemerkungen, §§ 1–14, Bezugsurkundenstruktur und Unterschriften. Enthält die eingebauten Fehler.

2. **Korrespondenz, Aktenvermerk und Beweis-/Fristenlogik** (`02-korrespondenz-und-vollvermerk.md`)
   — Mandantenanfrage per E-Mail, interner Aktenvermerk, anwaltliche Strategie-Antwort, Beweis-/Fristen-Tabelle, fünfstufiger Eskalationsplan, Honorarauszug.

3. **Anwaltliches Gutachten — Lösungsschlüssel zur Testakte** (`03-gutachten-loesungsschluessel.md`)
   — Das vollständige Prüfgutachten mit Pflicht-Prüfblock, 28 klauselgenauen Beanstandungen, Ampel-Bilanz, sieben Handlungsempfehlungen. **Anonymisierte Lehre**, keine konkreten Rechtsprechungsfundstellen.

## Formate

Jedes Dokument liegt vor als:

- **Markdown-Quelle** in `quellen/` — die maßgebliche Fassung, die du editieren würdest, wenn du die Akte erweitern willst.
- **PDF** in `gesamt-pdf/` — zum Lesen und Versenden.
- **Word-Dokument (.docx)** in `gesamt-docx/` — zum Annotieren und Weiterbearbeiten.

## Verwendung mit dem Skill

1. Öffne den Skill (Download über die Pages-URL des Repos).
2. Übergib dem Skill den Bauträgervertrag aus `quellen/01-bautraegervertrag.md` oder `gesamt-pdf/01-bautraegervertrag.pdf`.
3. Vergleiche die Ausgabe des Skills mit dem Lösungs-Gutachten in `quellen/03-gutachten-loesungsschluessel.md`.
4. Erwartetes Ergebnis: Der Skill sollte den Pflicht-Prüfblock (6 von 6 🔴) auslösen, mindestens 22 weitere 🔴-Befunde finden und eine strukturierte Risikomatrix liefern.

## Hinweis

Der Vertragstext ist absichtlich extrem verbraucherfeindlich. Reale Bauträgerverträge sind selten so dicht mit Fallen versehen — aber jede einzelne der eingebauten Klauseln ist in der Praxis schon vorgekommen. Die Akte verdichtet die Fehlerlogik zu einem Lehrstück.
