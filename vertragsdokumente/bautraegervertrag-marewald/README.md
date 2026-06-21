# Bauträgervertrag — Akte Marewald

> **Charakter dieser Akte:** rechtmäßig, aber grenzwertig verkäuferfreundlich. Der Vertrag reizt den zulässigen Spielraum aus, ohne rote Pflichtverletzung oder erkennbare Nichtigkeit — der Skill soll ihn als hart und ausgereizt, aber im Rahmen des Rechts einordnen (überwiegend 🟠). Das bewusst fehlerhafte Gegenstück ist die Akte Hohenwartshofen (`../bautraegervertrag/`). Übersicht: [`../README.md`](../README.md).

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den Gesamtfassungen und als Akten-ZIP mit getrennten Einzel-PDFs:

- [Markdown öffnen](bautraegervertrag-marewald.md)
- [Word-Dokument herunterladen](bautraegervertrag-marewald.docx)
- [PDF herunterladen](bautraegervertrag-marewald.pdf)
- [Akten-ZIP mit Einzel-PDFs herunterladen](bautraegervertrag-marewald-einzel-pdfs.zip)

Öffentliche Download-Links über GitHub Pages:

- [Markdown direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md)
- [Word-Dokument direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx)
- [PDF direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf)
- [Akten-ZIP direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip)

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade den Bauträgervertrag-Prüfer-Skill aus dem Repository, entweder vollständig als `SKILL.md` oder kompakt als `MINI_SKILL.md`.
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Die Ausgabe soll mit Übersendungsschreiben an die Käuferseite, Mandantengutachten und außergerichtlichem Aufforderungsschreiben an Bauträger/Notar enden.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag-marewald.md` werden Word-Fassung, Gesamt-PDF und Akten-ZIP so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.
