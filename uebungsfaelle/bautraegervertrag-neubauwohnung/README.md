# Schulungsfall Bauträgervertrag Neubauwohnung

Diese Akte ist **vollständig fingiert** und dient ausschließlich Schulungszwecken für den Bauträgervertrag-Prüfer-Skill. Alle Namen, Daten, Adressen, Aktenzeichen, UR-Nummern, Banken, Notariate und das Projekt sind frei erfunden. Reale Personen, Unternehmen oder Notariate sind nicht gemeint.

## Worum es geht

Ein fiktiver Wohnungsbauträgervertrag mit Auflassung für eine Eigentumswohnung in einem fiktiven Großprojekt zwischen Stahnsdorf und Kleinmachnow. Die zugehörige Baubeschreibung wird, wie in der Urkunde vorgesehen, nur lose übergeben und ist als eigenes Dokument beigefügt.

Der Schulungsfall erlaubt es,

- den Skill an einem realistischen, komplexen Beispielvertrag zu erproben,
- eine autonome Analyse an unvermerktem Vertragsmaterial durchzuführen,
- Vertrag und Baubeschreibung gemeinsam als Prüfmaterial zu verwenden.

## Inhalt

Die Akte besteht aus zwei Dokumenten, jeweils in drei Formaten verfügbar:

1. **Wohnungsbauträgervertrag mit Auflassung** (`01-bautraegervertrag.md`)
   — Die fingierte notarielle Urkunde mit Vorbemerkungen, §§ 1–14, Bezugsurkunden- und Anlagenverzeichnis, Geschäftswert-/Kostenvermerk und Unterschriften.

2. **Baubeschreibung — Fassung Februar 2026, Version 7.2 (Auszug)** (`02-baubeschreibung-auszug.md`)
   — Die in der Urkunde referenzierte Baubeschreibung.

## Formate

Jedes Dokument liegt vor als:

- **Markdown-Quelle** in `quellen/` — die maßgebliche Fassung, die du editieren würdest, wenn du die Akte erweitern willst.
- **PDF** in `gesamt-pdf/` — zum Lesen und Versenden.
- **Word-Dokument (.docx)** in `gesamt-docx/` — zum Annotieren und Weiterbearbeiten.

PDF und DOCX werden aus den Markdown-Quellen erzeugt. Nach einer Änderung in `quellen/` regenerierst du beide Formate mit dem mitgelieferten Build-Skript:

```bash
cd uebungsfaelle/bautraegervertrag-neubauwohnung
./build.sh            # alle Dokumente
./build.sh 02         # nur die Baubeschreibung
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.

## Verwendung mit dem Skill

1. Öffne den Skill (Download über die Pages-URL des Repos).
2. Übergib dem Skill den Bauträgervertrag aus `quellen/01-bautraegervertrag.md` oder das entsprechende PDF.
3. Übergib zusätzlich die Baubeschreibung aus `quellen/02-baubeschreibung-auszug.md`, damit auch das Bausoll geprüft werden kann.

## Hinweis

Der Vertragstext ist fiktiv und äußerlich professionell gehalten. Eine inhaltliche Auswertung wird nicht mitgeliefert; genau diese autonome Prüfung soll der Skill leisten.
