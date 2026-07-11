# Bauträgervertrag — Akte Lindenhain

**Navigation:** [Haupt-README](../../README.md) · [Alle Vertragsakten](../README.md) · [Downloads](#downloads-auf-einen-blick) · [Verwendung](#verwendung-mit-dem-skill) · [Neu erzeugen](#neu-erzeugen) · [Hohenwartshofen](../bautraegervertrag/README.md) · [Marewald](../bautraegervertrag-marewald/README.md) · [Downloadseite](https://klotzkette.github.io/bautraegervertragspruefer-skill/#akten) · [neueste Veröffentlichung](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest)

> **Charakter dieser Akte:** fair, ausgewogen und leicht käuferfreundlich. Der Vertrag ist als positive Kontrollakte gedacht: Der Skill soll nicht reflexhaft rote Befunde produzieren, sondern erkennen, dass Zahlungsplan, Sicherheiten, Abnahme, Unterlagen, Baukontrolle und Sprachfassung verbraucherseitig sauber geregelt sind. Übersicht: [`../README.md`](../README.md).

## Downloads auf einen Blick

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den deutschen Gesamtfassungen, als Akten-ZIP mit getrennten Einzel-PDFs und als zweispaltige Deutsch/English-Lesefassung.

| Datei | Lokal im Repository | Öffentlich über Pages | Sofortdownload über Release |
| --- | --- | --- | --- |
| Deutsch Markdown | [öffnen](bautraegervertrag-lindenhain.md) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain.md) |
| Deutsch Word | [herunterladen](bautraegervertrag-lindenhain.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain.docx) |
| Deutsch PDF | [herunterladen](bautraegervertrag-lindenhain.pdf) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain.pdf) |
| Akten-ZIP Einzel-PDFs | [herunterladen](bautraegervertrag-lindenhain-einzel-pdfs.zip) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-einzel-pdfs.zip) |
| Deutsch/English HTML | [ansehen](bautraegervertrag-lindenhain-de-en.html) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-de-en.html) |
| Deutsch/English Word | [herunterladen](bautraegervertrag-lindenhain-de-en.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-de-en.docx) |
| Deutsch/English PDF | [herunterladen](bautraegervertrag-lindenhain-de-en.pdf) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-lindenhain-de-en.pdf) |

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs. Die deutsch-englische Lesefassung ist keine eigenständige Vertragssprache: links steht die deutsche Fassung, rechts nur eine englische Verständnishilfe; die Urkunde selbst stellt klar, dass bei Beurkundung und Auslegung die deutsche Fassung maßgeblich bleibt.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade [SKILL.md](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) oder kompakt [MINI_SKILL.md](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md).
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Erwartung: überwiegend 🟢, punktuell höchstens 🟠 für Verhandlungsfragen; keine 🔴, wenn der Skill sauber zwischen fairer Gestaltung und Pflichtverstoß trennt.

## Neu erzeugen

Nach Änderungen an [`bautraegervertrag-lindenhain.md`](bautraegervertrag-lindenhain.md) werden Word-Fassung, Gesamt-PDF und Akten-ZIP mit [`build.sh`](build.sh) so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern [`build/style.css`](build/style.css) und [`build/pagebreak.lua`](build/pagebreak.lua).

Die deutsch-englische Lesefassung wird vom [`Repository-Generator`](../../scripts/build_bilingual_contracts.py) erzeugt:

```bash
../../scripts/build_bilingual_contracts.py
```

Danach prüft [`check_contract_builds.py`](../../scripts/check_contract_builds.py) die Dateien gegen das [`Artefaktmanifest`](../artifact-manifest.sha256).

**Weiter:** [Alle Vertragsakten](../README.md) · [Haupt-README](../../README.md) · [Downloadseite](https://klotzkette.github.io/bautraegervertragspruefer-skill/#akten) · [neueste Veröffentlichung](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest)
