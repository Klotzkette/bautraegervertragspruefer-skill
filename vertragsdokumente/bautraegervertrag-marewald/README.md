# Bauträgervertrag — Akte Marewald

**Navigation:** [Haupt-README](../../README.md) · [Alle Vertragsakten](../README.md) · [Hohenwartshofen](../bautraegervertrag/README.md) · [Lindenhain](../bautraegervertrag-lindenhain/README.md) · [Downloadseite](https://klotzkette.github.io/bautraegervertragspruefer-skill/)

> **Charakter dieser Akte:** rechtmäßig, aber grenzwertig verkäuferfreundlich. Der Vertrag reizt den zulässigen Spielraum aus, ohne rote Pflichtverletzung oder erkennbare Nichtigkeit — der Skill soll ihn als hart und ausgereizt, aber im Rahmen des Rechts einordnen (überwiegend 🟠). Das bewusst fehlerhafte Gegenstück ist die Akte Hohenwartshofen (`../bautraegervertrag/`). Übersicht: [`../README.md`](../README.md).

## Downloads auf einen Blick

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den deutschen Gesamtfassungen, als Akten-ZIP mit getrennten Einzel-PDFs und als zweispaltige Deutsch/English-Lesefassung.

| Datei | Lokal im Repository | Öffentlich über Pages | Sofortdownload über Release |
| --- | --- | --- | --- |
| Deutsch Markdown | [öffnen](bautraegervertrag-marewald.md) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald.md) |
| Deutsch Word | [herunterladen](bautraegervertrag-marewald.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald.docx) |
| Deutsch PDF | [herunterladen](bautraegervertrag-marewald.pdf) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald.pdf) |
| Akten-ZIP Einzel-PDFs | [herunterladen](bautraegervertrag-marewald-einzel-pdfs.zip) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-einzel-pdfs.zip) |
| Deutsch/English HTML | [ansehen](bautraegervertrag-marewald-de-en.html) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-de-en.html) |
| Deutsch/English Word | [herunterladen](bautraegervertrag-marewald-de-en.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-de-en.docx) |
| Deutsch/English PDF | [herunterladen](bautraegervertrag-marewald-de-en.pdf) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-marewald-de-en.pdf) |

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs. Die deutsch-englische Lesefassung ist keine eigenständige Vertragssprache: links steht die deutsche Fassung, rechts nur eine englische Verständnishilfe; die Urkunde selbst stellt klar, dass bei Beurkundung und Auslegung die deutsche Fassung maßgeblich bleibt.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade [SKILL.md](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) oder kompakt [MINI_SKILL.md](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md).
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Für den vollständigen Test `Vollpaket` anfordern; der Skill soll keine künstliche Unwirksamkeit behaupten.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag-marewald.md` werden Word-Fassung, Gesamt-PDF und Akten-ZIP so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.

Die deutsch-englische Lesefassung wird vom Repository-Generator erzeugt:

```bash
../../scripts/build_bilingual_contracts.py
```
