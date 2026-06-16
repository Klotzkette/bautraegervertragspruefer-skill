#!/usr/bin/env bash
#
# Baut die Testakte „Bauträgervertrag aus der Hölle" aus den maßgeblichen
# Markdown-Quellen in quellen/ in die beiden Ausgabeformate:
#   * gesamt-docx/<name>.docx  (Word, zum Annotieren)
#   * gesamt-pdf/<name>.pdf     (PDF, zum Lesen und Versenden)
#
# Voraussetzungen:
#   * pandoc
#   * weasyprint  (als PDF-Engine; rendert über HTML/CSS, kein LaTeX nötig)
#
# Aufruf aus dem Akten-Verzeichnis:
#   ./build.sh            # baut alle Quellen
#   ./build.sh 01 04      # baut nur Quellen, deren Dateiname mit 01 bzw. 04 beginnt
#
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$DIR/quellen"
OUT_DOCX="$DIR/gesamt-docx"
OUT_PDF="$DIR/gesamt-pdf"
FILTER="$DIR/build/pagebreak.lua"
CSS="$DIR/build/style.css"

command -v pandoc >/dev/null     || { echo "FEHLT: pandoc";     exit 1; }
command -v weasyprint >/dev/null || { echo "FEHLT: weasyprint"; exit 1; }

mkdir -p "$OUT_DOCX" "$OUT_PDF"

shopt -s nullglob
for md in "$SRC"/*.md; do
  base="$(basename "$md" .md)"

  # Optionaler Filter über Präfix-Argumente
  if [ "$#" -gt 0 ]; then
    match=0
    for pat in "$@"; do [[ "$base" == "$pat"* ]] && match=1; done
    [ "$match" -eq 1 ] || continue
  fi

  echo "→ $base"
  pandoc "$md" --lua-filter="$FILTER" \
    -o "$OUT_DOCX/$base.docx"
  pandoc "$md" --lua-filter="$FILTER" \
    --pdf-engine=weasyprint --css="$CSS" \
    -o "$OUT_PDF/$base.pdf"
done

echo "Fertig. DOCX: $OUT_DOCX  |  PDF: $OUT_PDF"
