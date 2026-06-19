#!/usr/bin/env bash
#
# Baut den Bauträgervertrag aus Markdown in die beiden Ausgabeformate:
#   * bautraegervertrag-marewald.docx  (Word, zum Annotieren)
#   * bautraegervertrag-marewald.pdf   (PDF, zum Lesen und Versenden)
#
# Voraussetzungen:
#   * pandoc
#   * weasyprint  (als PDF-Engine; rendert über HTML/CSS, kein LaTeX nötig)
#
# Aufruf aus diesem Verzeichnis:
#   ./build.sh
#
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$DIR/bautraegervertrag-marewald.md"
OUT_DOCX="$DIR/bautraegervertrag-marewald.docx"
OUT_PDF="$DIR/bautraegervertrag-marewald.pdf"
FILTER="$DIR/build/pagebreak.lua"
CSS="$DIR/build/style.css"

command -v pandoc >/dev/null     || { echo "FEHLT: pandoc";     exit 1; }
command -v weasyprint >/dev/null || { echo "FEHLT: weasyprint"; exit 1; }

echo "→ bautraegervertrag-marewald"
pandoc "$SRC" --lua-filter="$FILTER" -o "$OUT_DOCX"
pandoc "$SRC" --lua-filter="$FILTER" --pdf-engine=weasyprint --css="$CSS" -o "$OUT_PDF"

echo "Fertig. DOCX: $OUT_DOCX  |  PDF: $OUT_PDF"
