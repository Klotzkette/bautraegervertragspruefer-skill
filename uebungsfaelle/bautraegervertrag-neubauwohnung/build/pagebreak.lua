-- Wandelt rohe LaTeX-Seitenumbrüche (\newpage, \pagebreak) aus den
-- Markdown-Quellen in ein zielformatgerechtes Umbruchelement um:
--   * DOCX/OpenXML -> echter Word-Seitenumbruch
--   * HTML/PDF (weasyprint) -> CSS-Seitenumbruch
-- So bleiben die Quellen mit \newpage gut lesbar und beide Ausgabeformate
-- erhalten saubere Seitenumbrüche.
function RawBlock(el)
  if el.format:match('tex') and (el.text:match('\\newpage') or el.text:match('\\pagebreak')) then
    if FORMAT:match('docx') or FORMAT:match('openxml') then
      return pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    else
      return pandoc.RawBlock('html', '<div style="break-after: page;"></div>')
    end
  end
end
