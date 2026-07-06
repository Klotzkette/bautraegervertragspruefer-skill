# Bauträgervertrag — Akte Lindenhain

> **Charakter dieser Akte:** fair, ausgewogen und leicht käuferfreundlich. Der Vertrag ist als positive Kontrollakte gedacht: Der Skill soll nicht reflexhaft rote Befunde produzieren, sondern erkennen, dass Zahlungsplan, Sicherheiten, Abnahme, Unterlagen, Baukontrolle und Sprachfassung verbraucherseitig sauber geregelt sind. Übersicht: [`../README.md`](../README.md).

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den Gesamtfassungen und als Akten-ZIP mit getrennten Einzel-PDFs:

- [Markdown öffnen](bautraegervertrag-lindenhain.md)
- [Word-Dokument herunterladen](bautraegervertrag-lindenhain.docx)
- [PDF herunterladen](bautraegervertrag-lindenhain.pdf)
- [Akten-ZIP mit Einzel-PDFs herunterladen](bautraegervertrag-lindenhain-einzel-pdfs.zip)

Deutsch-englische Lesefassung:

- [Zweispaltiges HTML öffnen](bautraegervertrag-lindenhain-de-en.html)
- [Zweispaltiges Word-Dokument herunterladen](bautraegervertrag-lindenhain-de-en.docx)
- [Zweispaltiges PDF herunterladen](bautraegervertrag-lindenhain-de-en.pdf)

Öffentliche Download-Links über GitHub Pages:

- [Markdown direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md)
- [Word-Dokument direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx)
- [PDF direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf)
- [Akten-ZIP direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip)
- [Deutsch/English-HTML direkt öffnen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html)
- [Deutsch/English-Word direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx)
- [Deutsch/English-PDF direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.pdf)

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs. Die deutsch-englische Lesefassung ist keine eigenständige Vertragssprache: links steht die deutsche Fassung, rechts nur eine englische Verständnishilfe; die Urkunde selbst stellt klar, dass bei Beurkundung und Auslegung die deutsche Fassung maßgeblich bleibt.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade den Bauträgervertrag-Prüfer-Skill aus dem Repository, entweder vollständig als `SKILL.md` oder kompakt als `MINI_SKILL.md`.
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Erwartung: überwiegend 🟢, punktuell höchstens 🟠 für Verhandlungsfragen; keine 🔴, wenn der Skill sauber zwischen fairer Gestaltung und Pflichtverstoß trennt.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag-lindenhain.md` werden Word-Fassung, Gesamt-PDF und Akten-ZIP so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.

Die deutsch-englische Lesefassung wird vom Repository-Generator erzeugt:

```bash
../../scripts/build_bilingual_contracts.py
```
