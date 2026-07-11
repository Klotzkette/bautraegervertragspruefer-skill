# Bauträgervertrag — Akte Hohenwartshofen

**Navigation:** [Haupt-README](../../README.md) · [Alle Vertragsakten](../README.md) · [Downloads](#downloads-auf-einen-blick) · [Verwendung](#verwendung-mit-dem-skill) · [Neu erzeugen](#neu-erzeugen) · [Marewald](../bautraegervertrag-marewald/README.md) · [Lindenhain](../bautraegervertrag-lindenhain/README.md) · [Downloadseite](https://klotzkette.github.io/bautraegervertragspruefer-skill/#akten) · [neueste Veröffentlichung](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest)

> **Charakter dieser Akte:** bewusst fehlerhaft. Der Vertrag ist überladen mit unwirksamen und teils nichtigen Klauseln; an ihm lässt sich zeigen, wie viele rote Ampeln der Skill findet. Das wirksame Gegenstück ist die Akte Marewald (`../bautraegervertrag-marewald/`). Übersicht: [`../README.md`](../README.md).

## Downloads auf einen Blick

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den deutschen Gesamtfassungen, als Akten-ZIP mit getrennten Einzel-PDFs und als zweispaltige Deutsch/English-Lesefassung.

| Datei | Lokal im Repository | Öffentlich über Pages | Sofortdownload über Release |
| --- | --- | --- | --- |
| Deutsch Markdown | [öffnen](bautraegervertrag.md) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.md) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag.md) |
| Deutsch Word | [herunterladen](bautraegervertrag.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag.docx) |
| Deutsch PDF | [herunterladen](bautraegervertrag.pdf) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag.pdf) |
| Akten-ZIP Einzel-PDFs | [herunterladen](bautraegervertrag-einzel-pdfs.zip) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-einzel-pdfs.zip) |
| Deutsch/English HTML | [ansehen](bautraegervertrag-de-en.html) | [ansehen](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.html) |
| Deutsch/English Word | [herunterladen](bautraegervertrag-de-en.docx) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.docx) |
| Deutsch/English PDF | [herunterladen](bautraegervertrag-de-en.pdf) | [laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.pdf) | [laden](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/bautraegervertrag-de-en.pdf) |

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs. Die deutsch-englische Lesefassung ist keine eigenständige Vertragssprache: links steht die deutsche Fassung, rechts nur eine englische Verständnishilfe; die Urkunde selbst stellt klar, dass bei Beurkundung und Auslegung die deutsche Fassung maßgeblich bleibt. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade [SKILL.md](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/SKILL.md) oder kompakt [MINI_SKILL.md](https://github.com/Klotzkette/bautraegervertragspruefer-skill/releases/latest/download/MINI_SKILL.md).
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Für den vollständigen Test `Vollpaket` anfordern: Übersendungsschreiben, Mandantengutachten und phasengerechtes Schreiben an den Bauträger.

## Neu erzeugen

Nach Änderungen an [`bautraegervertrag.md`](bautraegervertrag.md) werden Word-Fassung, Gesamt-PDF und Akten-ZIP mit [`build.sh`](build.sh) so erzeugt:

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
