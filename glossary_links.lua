--[[
  glossary_links.lua — cross-link glossary terms in a BCOG 100 reading.

  For each glossary headword (the bold term that starts an entry under the
  "## Glossary" heading), this finds the FIRST bold use of that same term in the
  prose and turns it into a link to the glossary entry; the glossary entry's
  headword becomes a link back to that first use. Matching is exact (normalized
  for case, surrounding punctuation, and simple singular/plural); anything that
  doesn't cleanly match is REPORTED to stderr, never guessed at.

  Used by both the PDF pipeline (build_reading.py, via --lua-filter) and the
  website (Quarto, via `filters:` in _quarto.yml), so links appear in both.

  Sections named "Further Reading" (and the "Glossary" itself) are excluded from
  the prose search, so bold book citations there are never linked.
]]--

local stringify = pandoc.utils.stringify
local lower = pandoc.text and pandoc.text.lower or string.lower

local function normalize(s)
  s = lower(s)
  s = s:gsub("\226\128\153", "'"):gsub("\226\128\152", "'")   -- curly quotes
  s = s:gsub("\226\128\148", "-"):gsub("\226\128\147", "-")   -- em / en dash
  s = s:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", "")
  s = s:gsub("[%.,;:!%?]+$", "")                               -- trailing punct
  if #s > 4 then                                              -- crude singularize
    if s:sub(-3) == "ies" then s = s:sub(1, #s - 3) .. "y"
    elseif s:sub(-2) == "es" and s:sub(-3) ~= "ses" then s = s:sub(1, #s - 2)
    elseif s:sub(-1) == "s" and s:sub(-2) ~= "ss" then s = s:sub(1, #s - 1) end
  end
  return s
end

local used_slugs = {}
local function slugify(s)
  s = lower(s)
  s = s:gsub("\226%z?%z?", ""):gsub("[^%w]+", "-"):gsub("^%-+", ""):gsub("%-+$", "")
  if s == "" then s = "term" end
  local base, n = s, 1
  while used_slugs[s] do n = n + 1; s = base .. "-" .. n end
  used_slugs[s] = true
  return s
end

-- collected state
local section = "prose"                 -- prose | frontmatter | glossary
local prose_strongs = {}                -- {list, idx, norm} in document order
local prose_bold = {}                   -- {norm, text} for the report
local terms, term_by_norm = {}, {}      -- glossary headwords

local function set_section(htext)
  local h = normalize(htext)
  if h == "glossary" then section = "glossary"
  elseif h == "further reading" or h == "further readings" then section = "frontmatter"
  end
  -- Further Reading / Glossary are the trailing sections, so once we leave prose
  -- we stay out of it; ordinary headers don't flip us back.
end

local function scan_inlines(list)
  for i, el in ipairs(list) do
    if el.t == "Strong" then
      local nrm = normalize(stringify(el))
      prose_bold[#prose_bold + 1] = { norm = nrm, text = stringify(el) }
      prose_strongs[#prose_strongs + 1] = { list = list, idx = i, norm = nrm }
    elseif el.content and type(el.content) == "table" then
      scan_inlines(el.content)
    end
  end
end

local function walk(blocks)
  for _, b in ipairs(blocks) do
    local t = b.t
    if t == "Header" then
      set_section(stringify(b))
    elseif t == "Para" or t == "Plain" then
      if section == "glossary" and b.content[1] and b.content[1].t == "Strong" then
        local disp = stringify(b.content[1])
        local nrm = normalize(disp)
        if not term_by_norm[nrm] then
          local term = { display = disp, norm = nrm, matched = false,
                         head_list = b.content, head_idx = 1 }
          terms[#terms + 1] = term
          term_by_norm[nrm] = term
        end
      elseif section == "prose" then
        scan_inlines(b.content)
      end
    elseif t == "BlockQuote" or t == "Div" then
      walk(b.content)
    elseif t == "BulletList" or t == "OrderedList" then
      for _, item in ipairs(b.content) do walk(item) end
    elseif t == "DefinitionList" then
      for _, it in ipairs(b.content) do
        for _, d in ipairs(it[2]) do walk(d) end
      end
    end
  end
end

function Pandoc(doc)
  walk(doc.blocks)

  -- assign slugs now (document order of glossary)
  for _, term in ipairs(terms) do term.slug = slugify(term.display) end

  -- forward links: first prose bold use of each term
  for _, ps in ipairs(prose_strongs) do
    local term = term_by_norm[ps.norm]
    if term and not term.matched then
      term.matched = true
      local inner = ps.list[ps.idx].content
      ps.list[ps.idx] = pandoc.Link({ pandoc.Strong(inner) }, "#gloss-" .. term.slug, "",
                          pandoc.Attr("term-" .. term.slug, { "glossary-ref" }, {}))
    end
  end

  -- back links: glossary headword -> first use (only for matched terms)
  for _, term in ipairs(terms) do
    if term.matched then
      local head = term.head_list[term.head_idx]
      term.head_list[term.head_idx] = pandoc.Link({ pandoc.Strong(head.content) },
                          "#term-" .. term.slug, "",
                          pandoc.Attr("gloss-" .. term.slug, { "glossary-entry" }, {}))
    end
  end

  -- report the cases we did NOT link
  local no_bold, embedded = {}, {}
  for _, term in ipairs(terms) do
    if not term.matched then
      local emb
      for _, pb in ipairs(prose_bold) do
        if pb.norm ~= term.norm and pb.norm:find(term.norm, 1, true) then emb = pb.text; break end
      end
      if emb then embedded[#embedded + 1] = string.format("%q only inside bold %q", term.display, emb)
      else no_bold[#no_bold + 1] = string.format("%q", term.display) end
    end
  end
  if #no_bold > 0 or #embedded > 0 then
    io.stderr:write("\n[glossary-links] " .. #terms .. " terms; " ..
      (#terms - #no_bold - #embedded) .. " linked.\n")
    if #no_bold > 0 then
      io.stderr:write("  not bolded anywhere in the prose (no link made):\n")
      for _, m in ipairs(no_bold) do io.stderr:write("    - " .. m .. "\n") end
    end
    if #embedded > 0 then
      io.stderr:write("  only found inside a larger bold phrase (no link made):\n")
      for _, m in ipairs(embedded) do io.stderr:write("    - " .. m .. "\n") end
    end
    io.stderr:write("\n")
  end

  return doc
end
