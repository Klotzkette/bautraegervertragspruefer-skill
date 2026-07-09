#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

require_file() {
  [[ -f "$1" ]] || fail "missing file: $1"
}

repo_rg() {
  if command -v rg >/dev/null 2>&1; then
    rg "$@"
  else
    grep -R "$@"
  fi
}

zip_list() {
  if command -v zipinfo >/dev/null 2>&1; then
    zipinfo -1 "$1"
  else
    unzip -Z1 "$1"
  fi
}

for path in \
  README.md \
  skill/SKILL.md \
  skill/MINI_SKILL.md \
  docs/SKILL.md \
  docs/MINI_SKILL.md \
  docs/index.html \
  scripts/build_bilingual_contracts.py \
  vertragsdokumente/bautraegervertrag/bautraegervertrag.md \
  vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf \
  vertragsdokumente/bautraegervertrag/bautraegervertrag.docx \
  vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html \
  vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.pdf \
  vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx \
  vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.pdf \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.pdf \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag.md \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag.docx \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.pdf \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.docx \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.pdf \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.pdf \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip; do
  require_file "$path"
done

skill_version="$(awk -F'"' '/^[[:space:]]+version:/{print $2; exit}' skill/SKILL.md)"
mini_version="$(awk -F'"' '/^[[:space:]]+version:/{print $2; exit}' skill/MINI_SKILL.md)"

[[ -n "$skill_version" ]] || fail "skill version not found"
[[ "$mini_version" == "${skill_version}-mini" ]] || fail "mini version mismatch: $mini_version"

grep -Fq "# Bauträgervertrag-Prüfer ${skill_version}" skill/SKILL.md || fail "SKILL.md header/version mismatch"
grep -Fq "# Mini-Bauträgervertrag-Prüfer ${skill_version}" skill/MINI_SKILL.md || fail "MINI_SKILL.md header/version mismatch"

cmp -s skill/SKILL.md docs/SKILL.md || fail "skill/SKILL.md and docs/SKILL.md differ"
cmp -s skill/MINI_SKILL.md docs/MINI_SKILL.md || fail "skill/MINI_SKILL.md and docs/MINI_SKILL.md differ"

contract_dirs=(
  bautraegervertrag
  bautraegervertrag-marewald
  bautraegervertrag-lindenhain
)

for contract_dir in "${contract_dirs[@]}"; do
  stem="$contract_dir"
  for suffix in .md .pdf .docx -de-en.html -de-en.pdf -de-en.docx -einzel-pdfs.zip; do
    source="vertragsdokumente/${contract_dir}/${stem}${suffix}"
    public="docs/vertragsdokumente/${contract_dir}/${stem}${suffix}"
    cmp -s "$source" "$public" || fail "published contract copy differs: ${public}"
  done
done

mini_chars="$(wc -m < skill/MINI_SKILL.md | tr -d ' ')"
[[ "$mini_chars" -le 7500 ]] || fail "MINI_SKILL.md exceeds 7500 chars: $mini_chars"

for mini_required in \
  "60s-Start" \
  "Kurzbild" \
  "Befundtabelle" \
  "Nächste Weiche" \
  "Käufer-/Mandantenschreiben" \
  "Mandantengutachten" \
  "Aufforderungsschreiben an Bauträger"; do
  grep -Fq "$mini_required" skill/MINI_SKILL.md || fail "MINI_SKILL.md missing required workflow/output phrase: $mini_required"
done

for full_required in \
  "Startsignal: Ich beginne jetzt" \
  "Vollpaket-Abschlussgate" \
  "Dokument 1 — Übersendungsschreiben" \
  "Dokument 2 — Mandantengutachten" \
  "Dokument 3 — Aufforderungsschreiben" \
  "VII ZR 231/22"; do
  grep -Fq "$full_required" skill/SKILL.md || fail "SKILL.md missing required workflow/legal phrase: $full_required"
done

grep -Fq "Version ${skill_version}" README.md || fail "README does not mention current version"
grep -Fq "releases/latest/download/SKILL.md" README.md || fail "README SKILL.md latest release link is missing"
grep -Fq "releases/latest/download/MINI_SKILL.md" README.md || fail "README MINI_SKILL.md latest release link is missing"
grep -Fq "Bauträgervertrag-Prüfer Skill ${skill_version}" docs/index.html || fail "docs/index.html title/header version stale"
grep -Fq "Stand ${skill_version}" docs/index.html || fail "docs/index.html stand/version stale"

for asset in \
  bautraegervertrag-de-en.html \
  bautraegervertrag-de-en.pdf \
  bautraegervertrag-de-en.docx \
  bautraegervertrag-marewald-de-en.html \
  bautraegervertrag-marewald-de-en.pdf \
  bautraegervertrag-marewald-de-en.docx \
  bautraegervertrag-lindenhain-de-en.html \
  bautraegervertrag-lindenhain-de-en.pdf \
  bautraegervertrag-lindenhain-de-en.docx; do
  grep -Fq "releases/latest/download/${asset}" README.md || fail "README missing release download link for ${asset}"
  grep -Fq "releases/latest/download/${asset}" docs/index.html || fail "docs/index.html missing release download link for ${asset}"
done

versioned_downloads="$(grep -Eo 'releases/download/v[0-9]+\.[0-9]+\.[0-9]+' README.md | sort -u || true)"
if [[ -n "$versioned_downloads" ]]; then
  fail "README contains version-pinned release download links: ${versioned_downloads}"
fi

if repo_rg -n 'Y-300-Z-BECKRS|BeckRS-B|https?://[^ )"]*(juris|beck)' README.md skill docs vertragsdokumente >/tmp/btv_forbidden_sources.txt 2>/dev/null; then
  cat /tmp/btv_forbidden_sources.txt >&2
  fail "forbidden direct source artifact found"
fi

repo_rg -n '§ 650v Abs\. 4 BGB' README.md skill docs vertragsdokumente 2>/dev/null \
  | grep -Ev 'Keinen|kein ' >/tmp/btv_invalid_norms.txt || true
if [[ -s /tmp/btv_invalid_norms.txt ]]; then
  cat /tmp/btv_invalid_norms.txt >&2
  fail "nonexistent statutory subsection found"
fi

contract_sources=(
  vertragsdokumente/bautraegervertrag/bautraegervertrag.md
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag.md
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md
)

if repo_rg -n 'aus der Hölle|Horror|schrecklich|Schulungsfall|Lösungsschlüssel|Dossier Bauträgervertragsrecht|Teil A — Dossier|bewusst fehlerhaft|Kontrollakte|Fehlerakte' "${contract_sources[@]}" >/tmp/btv_meta_tells.txt 2>/dev/null; then
  cat /tmp/btv_meta_tells.txt >&2
  fail "contract document contains meta/test tell"
fi

for source in "${contract_sources[@]:0:3}"; do
  grep -Fq '# Wohnungsbauträgervertrag mit Auflassung' "$source" || fail "$source missing exact deed title"
done

bilingual_sources=(
  vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html
)

for html in "${bilingual_sources[@]}"; do
  grep -Fq "Deutsch-englische Lesefassung" "$html" || fail "$html missing bilingual notice"
  grep -Fq "ausschließlich die deutsche Sprachfassung" "$html" || fail "$html missing notarisation-language clause"
  grep -Fq "the German language version shall be authoritative" "$html" || fail "$html missing English precedence clause"
  if grep -Eq 'Bound|\*\*|subscription skill|ready-to-cover|statement of insolvency|Published today|Business resident|Housing housing|contract with disposition|Wohnungsbauträgervertrags' "$html"; then
    fail "$html contains visible translation artifact"
  fi
done

for docx in \
  vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx; do
  document_xml="$(unzip -p "$docx" word/document.xml)"
  grep -Fq 'Wohnungsbauträgervertrag mit Auflassung' <<<"$document_xml" || fail "$docx missing corrected German deed title"
  grep -Fq 'Residential Property Development Contract with Conveyance' <<<"$document_xml" || fail "$docx missing corrected English deed title"
  table_count="$(grep -o '<w:tbl>' <<<"$document_xml" | wc -l | tr -d ' ' || true)"
  [[ "$table_count" -eq 1 ]] || fail "$docx contains unflattened nested tables: $table_count"
done

for zip in \
  vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip \
  vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip \
  vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip \
  docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip \
  docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip \
  docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip; do
  require_file "$zip"
  pdf_count="$(zip_list "$zip" | grep -E '\.pdf$' | wc -l | tr -d ' ')"
  [[ "$pdf_count" -ge 2 ]] || fail "$zip contains fewer than two Einzel-PDFs"
done

echo "validate_repo: ok (version ${skill_version}, mini ${mini_chars} chars)"
