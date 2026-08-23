--[[
  glossary_links.lua — cross-link glossary terms in a BCOG 100 reading.

  For each glossary headword (the bold term that starts an entry under the
  "## Glossary" heading), this finds the FIRST bold use of that same term in the
  prose and turns it into a link to the glossary entry; the glossary entry's
  headword becomes a link back to that first use. Matching is exact (normalized
  for case, surrounding punctuation, and simple singular/plural); anything that
  doesn't cleanly match is REPORTED to stderr, never guessed at.

  This is the ONLY implementation of the glossary rule. It is run by both the
  PDF pipeline (build_reading.py) and the website (Quarto), both of which take
  their filter list from the `filters:` block of intro_to_bcs/_quarto.yml. There
  is deliberately no second copy of this file and no parallel implementation in
  Python: the two used to disagree about the HTML they emitted, which broke the
  PDF's glossary styling in a way that looked like a filter bug.

  The HTML contract (style.css and styles.css depend on it):
    first prose use   ->  <a id="ref-SLUG"   class="gloss-link" href="#gloss-SLUG">
    glossary headword ->  <a id="gloss-SLUG" class="gloss-back" href="#ref-SLUG">
  The glossary entry paragraph carries NO class. It is styled structurally, via
  `h2#glossary ~ p`, because a Pandoc Para cannot carry attributes and wrapping
  each entry in a Div would break that same sibling selector on the website.

  Sections named "Further Reading" (and the "Glossary" itself) are excluded from
  the prose search, so bold book citations there are never linked.

  Pass -M glossary-links=false to skip the linking; the report still runs.
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
local prose_strongs = {}                -- {list, idx, norm, text, linked} in document order
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
      local txt = stringify(el)
      local nrm = normalize(txt)
      prose_bold[#prose_bold + 1] = { norm = nrm, text = txt }
      prose_strongs[#prose_strongs + 1] = { list = list, idx = i, norm = nrm,
                                            text = txt, linked = false }
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

local function q(s) return '"' .. s .. '"' end

function Pandoc(doc)
  walk(doc.blocks)

  local add_links = true
  local flag = doc.meta["glossary-links"]
  if flag ~= nil then
    local v = lower(stringify(flag))
    if v == "false" or v == "no" or v == "0" then add_links = false end
  end

  -- assign slugs now (document order of glossary)
  for _, term in ipairs(terms) do term.slug = slugify(term.display) end

  -- match each term to its first, not-yet-claimed bold use in the prose
  for _, ps in ipairs(prose_strongs) do
    local term = term_by_norm[ps.norm]
    if term and not term.matched then
      term.matched = true
      ps.linked = true
      if add_links then
        local inner = ps.list[ps.idx].content
        ps.list[ps.idx] = pandoc.Link({ pandoc.Strong(inner) }, "#gloss-" .. term.slug, "",
                            pandoc.Attr("ref-" .. term.slug, { "gloss-link" }, {}))
      end
    end
  end

  -- back links: glossary headword -> first use (only for matched terms)
  if add_links then
    for _, term in ipairs(terms) do
      if term.matched then
        local head = term.head_list[term.head_idx]
        term.head_list[term.head_idx] = pandoc.Link({ pandoc.Strong(head.content) },
                            "#ref-" .. term.slug, "",
                            pandoc.Attr("gloss-" .. term.slug, { "gloss-back" }, {}))
      end
    end
  end

  -- ---------------------------------------------------------------- report
  local linked = 0
  for _, term in ipairs(terms) do if term.matched then linked = linked + 1 end end

  if #terms > 0 then
    io.stderr:write(string.format("  glossary: linked %d/%d terms to their in-text use%s\n",
      linked, #terms, add_links and "" or "  (linking disabled; report only)"))
  end

  -- terms with no usable first bold use
  for _, term in ipairs(terms) do
    if not term.matched then
      local emb
      for _, pb in ipairs(prose_bold) do
        if pb.norm ~= term.norm and pb.norm:find(term.norm, 1, true) then emb = pb.text; break end
      end
      if emb then
        io.stderr:write("            (" .. q(term.display) ..
                        " appears only inside the longer bold phrase " .. q(emb) .. ")\n")
      else
        io.stderr:write("            (no bolded in-text use found for: " .. term.display .. ")\n")
      end
    end
  end

  -- stray bold: prose bold that is NOT a first-use glossary term. The house rule
  -- is that bold means a glossary term at its first use and nothing else, so a
  -- second mention or a bolded-for-emphasis phrase is a defect worth reporting.
  local seen_stray = {}
  for _, ps in ipairs(prose_strongs) do
    if not ps.linked then
      local key = lower(ps.text)
      if not seen_stray[key] then
        seen_stray[key] = true
        io.stderr:write("  stray bold (not a first-use glossary term): " .. q(ps.text) .. "\n")
      end
    end
  end

  return doc
end
