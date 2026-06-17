# Bauträgervertrag

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in drei Fassungen:

- [Markdown öffnen](bautraegervertrag.md)
- [Word-Dokument herunterladen](bautraegervertrag.docx)
- [PDF herunterladen](bautraegervertrag.pdf)

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käuferinnen, Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade den Bauträgervertrag-Prüfer-Skill aus dem Repository.
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag.md` werden Word- und PDF-Fassung so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.
