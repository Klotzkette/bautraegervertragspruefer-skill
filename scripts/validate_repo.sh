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

skill_version="$(awk -F'"' '/^version:/{print $2; exit}' skill/SKILL.md)"
mini_version="$(awk -F'"' '/^version:/{print $2; exit}' skill/MINI_SKILL.md)"

[[ -n "$skill_version" ]] || fail "skill version not found"
[[ "$mini_version" == "${skill_version}-mini" ]] || fail "mini version mismatch: $mini_version"

grep -Fq "# Bauträgervertrag-Prüfer ${skill_version}" skill/SKILL.md || fail "SKILL.md header/version mismatch"
grep -Fq "# Mini-Bauträgervertrag-Prüfer ${skill_version}" skill/MINI_SKILL.md || fail "MINI_SKILL.md header/version mismatch"

cmp -s skill/SKILL.md docs/SKILL.md || fail "skill/SKILL.md and docs/SKILL.md differ"
cmp -s skill/MINI_SKILL.md docs/MINI_SKILL.md || fail "skill/MINI_SKILL.md and docs/MINI_SKILL.md differ"
cmp -s vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.html || fail "Hohenwartshofen bilingual HTML docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.pdf docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.pdf || fail "Hohenwartshofen bilingual PDF docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx docs/vertragsdokumente/bautraegervertrag/bautraegervertrag-de-en.docx || fail "Hohenwartshofen bilingual DOCX docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.html || fail "Marewald bilingual HTML docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.pdf docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.pdf || fail "Marewald bilingual PDF docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx docs/vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald-de-en.docx || fail "Marewald bilingual DOCX docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md || fail "Lindenhain Markdown docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.pdf || fail "Lindenhain PDF docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.docx || fail "Lindenhain DOCX docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-einzel-pdfs.zip || fail "Lindenhain ZIP docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.html || fail "Lindenhain bilingual HTML docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.pdf docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.pdf || fail "Lindenhain bilingual PDF docs copy differs"
cmp -s vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx docs/vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain-de-en.docx || fail "Lindenhain bilingual DOCX docs copy differs"

mini_chars="$(wc -m < skill/MINI_SKILL.md | tr -d ' ')"
[[ "$mini_chars" -le 8000 ]] || fail "MINI_SKILL.md exceeds 8000 chars: $mini_chars"

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
  if grep -Eq 'Bound|\*\*|subscription skill|ready-to-cover|statement of insolvency|Published today|Business resident' "$html"; then
    fail "$html contains visible translation artifact"
  fi
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
