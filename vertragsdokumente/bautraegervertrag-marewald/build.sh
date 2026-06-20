#!/usr/bin/env bash
#
# Baut den Bauträgervertrag aus Markdown in die Ausgabeformate:
#   * bautraegervertrag-marewald.docx  (Word, zum Annotieren)
#   * bautraegervertrag-marewald.pdf   (PDF, zum Lesen und Versenden)
#   * bautraegervertrag-marewald-einzel-pdfs.zip  (Akte als getrennte Einzel-PDFs)
#
# Voraussetzungen:
#   * pandoc
#   * weasyprint  (als PDF-Engine; rendert über HTML/CSS, kein LaTeX nötig)
#   * perl
#   * zip
#
# Aufruf aus diesem Verzeichnis:
#   ./build.sh
#
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$DIR/bautraegervertrag-marewald.md"
OUT_DOCX="$DIR/bautraegervertrag-marewald.docx"
OUT_PDF="$DIR/bautraegervertrag-marewald.pdf"
OUT_ZIP="$DIR/bautraegervertrag-marewald-einzel-pdfs.zip"
FILTER="$DIR/build/pagebreak.lua"
CSS="$DIR/build/style.css"

command -v pandoc >/dev/null     || { echo "FEHLT: pandoc";     exit 1; }
command -v weasyprint >/dev/null || { echo "FEHLT: weasyprint"; exit 1; }
command -v perl >/dev/null       || { echo "FEHLT: perl";       exit 1; }
command -v zip >/dev/null        || { echo "FEHLT: zip";        exit 1; }
grep -q '^# Anlage: Baubeschreibung$' "$SRC" || { echo "FEHLT: # Anlage: Baubeschreibung"; exit 1; }

echo "→ bautraegervertrag-marewald"
pandoc "$SRC" --lua-filter="$FILTER" -o "$OUT_DOCX"
pandoc "$SRC" --lua-filter="$FILTER" --pdf-engine=weasyprint --css="$CSS" -o "$OUT_PDF"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

MAIN_MD="$TMP_DIR/01-wohnungsbautraegervertrag-mit-auflassung.md"
ANLAGE_MD="$TMP_DIR/02-baubeschreibung-marewald-komfort-c.md"
ZIP_DIR="$TMP_DIR/einzel-pdfs"
mkdir -p "$ZIP_DIR"

awk '/^# Anlage: Baubeschreibung$/ {exit} {print}' "$SRC" | perl -0pe 's/\s*\\newpage\s*\z/\n/' > "$MAIN_MD"
awk 'found || /^# Anlage: Baubeschreibung$/ {found=1; print}' "$SRC" > "$ANLAGE_MD"

pandoc "$MAIN_MD" --lua-filter="$FILTER" --pdf-engine=weasyprint --css="$CSS" \
  -o "$ZIP_DIR/01-wohnungsbautraegervertrag-mit-auflassung.pdf"
pandoc "$ANLAGE_MD" --lua-filter="$FILTER" --pdf-engine=weasyprint --css="$CSS" \
  -o "$ZIP_DIR/02-baubeschreibung-marewald-komfort-c.pdf"

rm -f "$OUT_ZIP"
(cd "$ZIP_DIR" && zip -X -q "$OUT_ZIP" ./*.pdf)

echo "Fertig. DOCX: $OUT_DOCX  |  PDF: $OUT_PDF  |  ZIP: $OUT_ZIP"
