# Bauträgervertrag — Akte Hohenwartshofen

> **Charakter dieser Akte:** bewusst fehlerhaft. Der Vertrag ist überladen mit unwirksamen und teils nichtigen Klauseln; an ihm lässt sich zeigen, wie viele rote Ampeln der Skill findet. Das wirksame Gegenstück ist die Akte Marewald (`../bautraegervertrag-marewald/`). Übersicht: [`../README.md`](../README.md).

## Downloads auf einen Blick

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den deutschen Gesamtfassungen, als Akten-ZIP mit getrennten Einzel-PDFs und als zweispaltige Deutsch/English-Lesefassung.

| Datei | Lokal im Repository | Öffentlich über Pages | Sofortdownload über Release |
| --- | --- | --- | --- |
| Deutsch Markdown | [öffnen](bautraegervertrag.md) | [öffnen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.md) | - |
| Deutsch Word | [herunterladen](bautraegervertrag.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.docx) | - |
| Deutsch PDF | [herunterladen](bautraegervertrag.pdf) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf) | - |
| Akten-ZIP Einzel-PDFs | [herunterladen](bautraegervertrag-einzel-pdfs.zip) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip) | - |
| Deutsch/English HTML | [ansehen](bautraegervertrag-de-en.html) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.html) |
| Deutsch/English Word | [herunterladen](bautraegervertrag-de-en.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.docx) |
| Deutsch/English PDF | [herunterladen](bautraegervertrag-de-en.pdf) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.pdf) |

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs. Die deutsch-englische Lesefassung ist keine eigenständige Vertragssprache: links steht die deutsche Fassung, rechts nur eine englische Verständnishilfe; die Urkunde selbst stellt klar, dass bei Beurkundung und Auslegung die deutsche Fassung maßgeblich bleibt. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade den Bauträgervertrag-Prüfer-Skill aus dem Repository, entweder vollständig als `SKILL.md` oder kompakt als `MINI_SKILL.md`.
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Die Ausgabe soll mit Übersendungsschreiben an die Käuferseite, Mandantengutachten und außergerichtlichem Aufforderungsschreiben an Bauträger/Notar enden.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag.md` werden Word-Fassung, Gesamt-PDF und Akten-ZIP so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.

Die deutsch-englische Lesefassung wird vom Repository-Generator erzeugt:

```bash
../../scripts/build_bilingual_contracts.py
```
