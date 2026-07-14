-- Setzt DOCX-Umbrüche direkt an den Anfang der folgenden Überschrift.
-- Ein eigener Absatz mit w:br kann bei knapp gefüllter Vorseite auf die
-- Folgeseite rutschen und dort eine unerwünschte Leerseite erzeugen.
local function is_page_break(block)
  return block.t == 'RawBlock'
    and block.format:match('tex')
    and (block.text:match('\\newpage') or block.text:match('\\pagebreak'))
end

function Pandoc(doc)
  local blocks = pandoc.List()
  local pending_docx_break = false
  local is_docx = FORMAT:match('docx') or FORMAT:match('openxml')

  for _, block in ipairs(doc.blocks) do
    if is_page_break(block) then
      if is_docx then
        pending_docx_break = true
      else
        blocks:insert(pandoc.RawBlock('html', '<div style="break-after: page;"></div>'))
      end
    else
      if pending_docx_break then
        if block.t == 'Header' then
          block.content:insert(1, pandoc.RawInline('openxml', '<w:br w:type="page"/>'))
        else
          blocks:insert(pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
        end
        pending_docx_break = false
      end
      blocks:insert(block)
    end
  end

  return pandoc.Pandoc(blocks, doc.meta)
end
