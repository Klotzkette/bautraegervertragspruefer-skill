#!/usr/bin/env bash
#
# Baut den Bauträgervertrag aus Markdown in die Ausgabeformate:
#   * bautraegervertrag-lindenhain.docx
#   * bautraegervertrag-lindenhain.pdf
#   * bautraegervertrag-lindenhain-bautenstandsbericht.pdf
#   * bautraegervertrag-lindenhain-zahlungsanforderung.pdf
#   * bautraegervertrag-lindenhain-einzel-pdfs.zip  (vier getrennte Akten-PDFs)
#
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$DIR/bautraegervertrag-lindenhain.md"
REPORT_SRC="$DIR/bautraegervertrag-lindenhain-bautenstandsbericht.md"
REQUEST_SRC="$DIR/bautraegervertrag-lindenhain-zahlungsanforderung.md"
OUT_DOCX="$DIR/bautraegervertrag-lindenhain.docx"
OUT_PDF="$DIR/bautraegervertrag-lindenhain.pdf"
OUT_REPORT_PDF="$DIR/bautraegervertrag-lindenhain-bautenstandsbericht.pdf"
OUT_REQUEST_PDF="$DIR/bautraegervertrag-lindenhain-zahlungsanforderung.pdf"
OUT_ZIP="$DIR/bautraegervertrag-lindenhain-einzel-pdfs.zip"
FILTER="$DIR/build/pagebreak.lua"
CSS="$DIR/build/style.css"
CASE_CSS="$DIR/../case-style.css"
TEMPLATE="$DIR/build/pdf-template.html"

command -v pandoc >/dev/null     || { echo "FEHLT: pandoc";     exit 1; }
command -v weasyprint >/dev/null || { echo "FEHLT: weasyprint"; exit 1; }
command -v perl >/dev/null       || { echo "FEHLT: perl";       exit 1; }
command -v zip >/dev/null        || { echo "FEHLT: zip";        exit 1; }
grep -q '^# Anlage: Baubeschreibung$' "$SRC" || { echo "FEHLT: # Anlage: Baubeschreibung"; exit 1; }
grep -q '^# Bautenstandsbericht$' "$REPORT_SRC" || { echo "FEHLT: neutraler Titel im Bautenstandsbericht"; exit 1; }
grep -q '^# Zahlungsanforderung$' "$REQUEST_SRC" || { echo "FEHLT: neutraler Titel in der Zahlungsanforderung"; exit 1; }

echo "→ bautraegervertrag-lindenhain"
pandoc "$SRC" --lua-filter="$FILTER" -o "$OUT_DOCX"
pandoc "$SRC" --lua-filter="$FILTER" --template="$TEMPLATE" --pdf-engine=weasyprint --css="$CSS" -o "$OUT_PDF"
pandoc "$REPORT_SRC" --template="$TEMPLATE" --pdf-engine=weasyprint --css="$CSS" --css="$CASE_CSS" -o "$OUT_REPORT_PDF"
pandoc "$REQUEST_SRC" --template="$TEMPLATE" --pdf-engine=weasyprint --css="$CSS" --css="$CASE_CSS" -o "$OUT_REQUEST_PDF"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

MAIN_MD="$TMP_DIR/01-wohnungsbautraegervertrag-mit-auflassung.md"
ANLAGE_MD="$TMP_DIR/02-baubeschreibung-lindenhain-komfort.md"
ZIP_DIR="$TMP_DIR/einzel-pdfs"
mkdir -p "$ZIP_DIR"

awk '/^# Anlage: Baubeschreibung$/ {exit} {print}' "$SRC" | perl -0pe 's/\s*\\newpage\s*\z/\n/' > "$MAIN_MD"
awk 'found || /^# Anlage: Baubeschreibung$/ {found=1; print}' "$SRC" > "$ANLAGE_MD"

pandoc "$MAIN_MD" --lua-filter="$FILTER" --template="$TEMPLATE" --pdf-engine=weasyprint --css="$CSS" \
  -o "$ZIP_DIR/01-wohnungsbautraegervertrag-mit-auflassung.pdf"
pandoc "$ANLAGE_MD" --lua-filter="$FILTER" --template="$TEMPLATE" --pdf-engine=weasyprint --css="$CSS" \
  -o "$ZIP_DIR/02-baubeschreibung-lindenhain-komfort.pdf"
cp "$OUT_REPORT_PDF" "$ZIP_DIR/03-bautenstandsbericht-lindenhain-12.pdf"
cp "$OUT_REQUEST_PDF" "$ZIP_DIR/04-zahlungsanforderung-lindenhain-wohnung-b-05.pdf"

rm -f "$OUT_ZIP"
(cd "$ZIP_DIR" && zip -X -q "$OUT_ZIP" ./*.pdf)

echo "Fertig. Vertrag: DOCX/PDF  |  Bautenstand und Zahlungsanforderung: PDF  |  Akten-ZIP: 4 Einzel-PDFs"
