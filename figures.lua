--[[
  figures.lua — figures and tables in a BCOG 100 reading.

  Run by both the PDF pipeline (build_reading.py) and the website (Quarto), from
  the single `filters:` list in intro_to_bcs/_quarto.yml. See glossary_links.lua
  for why there is exactly one implementation of each rule.

  THE POINT OF THIS FILTER: a reading declares every figure it wants, whether or
  not the image file exists yet. A figure whose file is missing is dropped from
  the output entirely — no caption, no placeholder, no gap — and every in-text
  reference to it recovers on its own. So the prose reads correctly at every
  level of figure completeness, and nothing in the .md changes when a figure
  finally lands: drop the file into place and rebuild.

  ---------------------------------------------------------------- DECLARING

    ![The caption.](images/thing.png){#fig-thing alt="What a reader who cannot
    see the figure needs to know."}

  Caption and alt text are separate on purpose: the caption says what the figure
  shows, the alt text describes it to someone who cannot see it. Pandoc maps the
  markdown "alt" position to the figcaption and the alt= attribute to the img,
  so both come out right with no work here.

  A table is declared the same way, with the id in its caption:

    : The caption. {#tbl-thing}

  ------------------------------------------------------------- REFERENCING

  Tier 1 — the default. An EMPTY link, with a normal space before it. The
  parentheses are generated here, never typed, so nothing is left stranded when
  the figure is absent:

    ...count as the same temperature [](#fig-thing).
       present -> ...count as the same temperature (Figure 1.4).
       absent  -> ...count as the same temperature.

  Tier 2 — a reference with fallback text. The link text is what survives if the
  figure is missing:

    Compare [the reconstructionist proposal](#fig-thing) and the difference...
       present -> Compare Figure 1.4 and the difference...
       absent  -> Compare the reconstructionist proposal and the difference...

  Tier 3 — conditional prose, for the few passages where the figure IS the
  argument and no sentence survives its absence. Both versions live in the .md
  and exactly one is kept:

    ::: {.if-figure fig="thing"}
    Look at the array below. Some circles read as bumps...
    :::

    ::: {.no-figure fig="thing"}
    The visual system assumes light comes from above...
    :::

  ------------------------------------------------------------------ NUMBERS

  Figures and tables are numbered per module, from the module number in the H1
  ("# 1. Mind and Brain" -> Figure 1.1, Figure 1.2, Table 1.1). Only figures
  that actually render are numbered, so numbers shift as figures land. That is
  deliberate: references are symbolic ids, so nothing in the prose has to be
  touched. Figure numbers are not stable until a module has been taught once.
]]--

local stringify = pandoc.utils.stringify

-- ---------------------------------------------------------------- helpers

local function dirname(p)
  return p and p:match("^(.*)[/\\][^/\\]*$") or "."
end

-- Directory of the file being rendered; image paths are relative to it.
local function input_dir()
  local f = PANDOC_STATE and PANDOC_STATE.input_files
                          and PANDOC_STATE.input_files[1]
  if f then return dirname(f) end
  return "."
end

local function file_exists(path)
  local fh = io.open(path, "r")
  if fh then fh:close(); return true end
  return false
end

local function is_remote(src)
  return src:match("^https?://") ~= nil or src:match("^data:") ~= nil
end

-- ------------------------------------------------------------------ state

local base_dir = input_dir()
local module_no = nil          -- "1" from "# 1. Mind and Brain"
local figs = {}                -- id -> {id, src, exists, num, refs, declared_order}
local fig_order = {}
local tbls = {}                -- id -> {id, num}
local tbl_order = {}
local problems = {}            -- collected, reported at the end
local n_declared, n_present = 0, 0

local seen_problem = {}
local function problem(msg)
  if seen_problem[msg] then return end
  seen_problem[msg] = true
  problems[#problems + 1] = msg
end

-- A non-breaking space keeps "Figure 1.4" from splitting across a line break,
-- which otherwise happens often enough to notice in a two-column-ish measure.
local NBSP = "\u{00A0}"

local function label(kind, num)
  if module_no then return string.format("%s%s%s.%d", kind, NBSP, module_no, num) end
  return string.format("%s%s%d", kind, NBSP, num)
end

-- A trailing {#tbl-xxx} on a table caption. Pandoc does not parse an attribute
-- there (that is a Quarto crossref extension, and the PDF path is plain pandoc),
-- so it arrives as a single Str at the end of the caption.
--
-- peek_table_id reads it WITHOUT mutating: the collect pass must not disturb the
-- document, or the rewrite pass finds a caption that has already been edited.
-- strip_table_id does the removal, once, during rewrite.
local function last_content_index(inlines)
  for i = #inlines, 1, -1 do
    local t = inlines[i].t
    if t ~= "Space" and t ~= "SoftBreak" then return i end
  end
  return nil
end

local function peek_table_id(inlines)
  local i = last_content_index(inlines)
  if not i or inlines[i].t ~= "Str" then return nil end
  return inlines[i].text:match("^{#(tbl%-[%w%-_]+)}$")
end

local function strip_table_id(inlines)
  local i = last_content_index(inlines)
  if not i or inlines[i].t ~= "Str" then return end
  if not inlines[i].text:match("^{#tbl%-[%w%-_]+}$") then return end
  for j = #inlines, i, -1 do table.remove(inlines, j) end
  if inlines[#inlines] and inlines[#inlines].t == "Space" then
    table.remove(inlines, #inlines)
  end
end

local function image_in(blocks)
  local found
  pandoc.walk_block(pandoc.Div(blocks), { Image = function(im)
    if not found then found = im end
  end })
  return found
end

-- ------------------------------------------------------- pass 1: collect

local function collect(doc)
  doc:walk {
    Header = function(h)
      if h.level == 1 and not module_no then
        module_no = stringify(h):match("^%s*(%d+)%.")
      end
    end,
    Figure = function(f)
      local id = f.identifier
      if id == "" then
        problem('a figure has no id — add {#fig-something} so it can be referenced: "'
                .. stringify(f.caption.long):sub(1, 60) .. '"')
        return
      end
      if not id:match("^fig%-") then
        problem('figure id "' .. id .. '" does not start with "fig-"')
      end
      if figs[id] then
        problem('duplicate figure id "' .. id .. '"')
        return
      end
      local im = image_in(f.content)
      local src = im and im.src or ""
      local exists = src ~= "" and (is_remote(src) or file_exists(base_dir .. "/" .. src))
      if #f.caption.long == 0 then
        problem('figure "' .. id .. '" has no caption')
      elseif im then
        -- With no explicit alt=, pandoc copies the caption into the img alt
        -- attribute, so an empty alt never reaches us. The defect to catch is
        -- alt text that is merely the caption again: a caption says what the
        -- figure shows, alt text describes it to someone who cannot see it.
        local alt = stringify(im.caption)
        if alt == "" then
          problem('figure "' .. id .. '" has no alt text — add alt="..." beside the id')
        elseif alt == stringify(f.caption.long) then
          problem('figure "' .. id .. '" has alt text that is only its caption repeated'
                  .. ' — write a distinct alt="..." describing the figure')
        end
      end
      n_declared = n_declared + 1
      if exists then n_present = n_present + 1 end
      figs[id] = { id = id, src = src, exists = exists, refs = 0 }
      fig_order[#fig_order + 1] = id
    end,
    Table = function(t)
      if #t.caption.long == 0 then return end     -- uncaptioned tables are unnumbered
      local cap = t.caption.long[1]
      local id = (cap.content and peek_table_id(cap.content)) or nil
      id = id or ("tbl-anon-" .. (#tbl_order + 1))
      if tbls[id] then problem('duplicate table id "' .. id .. '"'); return end
      tbls[id] = { id = id, refs = 0 }
      tbl_order[#tbl_order + 1] = id
    end,
  }
  if module_no == nil and (#fig_order > 0 or #tbl_order > 0) then
    problem("no module number found in the H1 (expected \"# 1. Title\") — "
            .. "labels will be unqualified, e.g. \"Figure 1\" rather than \"Figure 1.1\"")
  end

  -- number what will actually render, in document order
  local n = 0
  for _, id in ipairs(fig_order) do
    if figs[id].exists then n = n + 1; figs[id].num = n end
  end
  n = 0
  for _, id in ipairs(tbl_order) do n = n + 1; tbls[id].num = n end
end

-- ------------------------------------------------------- pass 2: rewrite

-- Prefix "Figure 1.4 — " onto a caption, in place. Caption is a plain table in
-- the Lua API (long/short), with no constructor, so we mutate rather than build.
local function add_label(caption, text)
  if #caption.long == 0 then
    caption.long = pandoc.Blocks({ pandoc.Plain(pandoc.Inlines({})) })
  end
  local first = caption.long[1]
  local new = pandoc.Inlines({ pandoc.Strong({ pandoc.Str(text) }),
                               pandoc.Space(), pandoc.Str("\u{2014}"), pandoc.Space() })
  for _, el in ipairs(first.content) do new:insert(el) end
  first.content = new
end

local function resolve_link(lk)
  local target = lk.target:match("^#(.+)$")
  if not target then return nil end
  local rec, kind
  if figs[target] then rec, kind = figs[target], "Figure"
  elseif tbls[target] then rec, kind = tbls[target], "Table"
  elseif target:match("^fig%-") or target:match("^tbl%-") then
    problem('reference to "#' .. target .. '" but nothing declares that id')
    return { present = false, inlines = lk.content }
  else
    return nil                                  -- an ordinary intra-doc link
  end
  rec.refs = rec.refs + 1
  if rec.num == nil then                        -- declared but not rendering
    return { present = false, inlines = lk.content }
  end
  local text = label(kind, rec.num)
  if #lk.content == 0 then text = "(" .. text .. ")" end
  return { present = true,
           inlines = pandoc.Inlines({
             pandoc.Link({ pandoc.Str(text) }, lk.target, lk.title,
                          pandoc.Attr("", { "xref" }, {})) }) }
end

local tbl_i = 0

local function rewrite(doc)
  tbl_i = 0
  return doc:walk {
    -- Inlines, not Link, so an absent bare reference can also eat the space
    -- that preceded it and leave no double space or stranded punctuation.
    Inlines = function(inlines)
      local out, changed = pandoc.Inlines({}), false
      for _, el in ipairs(inlines) do
        local r = (el.t == "Link") and resolve_link(el) or nil
        if r == nil then
          out:insert(el)
        else
          changed = true
          if #r.inlines == 0 then
            if #out > 0 and out[#out].t == "Space" then out:remove(#out) end
          else
            for _, x in ipairs(r.inlines) do out:insert(x) end
          end
        end
      end
      if changed then return out end
    end,

    Figure = function(f)
      local rec = figs[f.identifier]
      if not rec then return nil end
      if not rec.exists then return {} end       -- drop it completely
      add_label(f.caption, label("Figure", rec.num))
      return f
    end,

    -- Captioned tables are matched to their collected record by document order,
    -- which is the order walk visits them. No id lookup, so an anonymous table
    -- and an id'd one can be mixed freely.
    Table = function(t)
      if #t.caption.long == 0 then return nil end
      tbl_i = tbl_i + 1
      local rec = tbls[tbl_order[tbl_i]]
      if not rec then return nil end
      local cap = t.caption.long[1]
      if cap.content then strip_table_id(cap.content) end
      add_label(t.caption, label("Table", rec.num))
      t.identifier = rec.id
      return t
    end,

    Div = function(d)
      local which
      if d.classes:includes("if-figure") then which = true
      elseif d.classes:includes("no-figure") then which = false
      else return nil end
      local key = d.attributes["fig"]
      if not key then
        problem("an if-figure/no-figure block has no fig= attribute")
        return nil
      end
      local id = key:match("^fig%-") and key or ("fig-" .. key)
      local rec = figs[id]
      if not rec then
        problem('conditional block refers to "' .. id .. '" but nothing declares it')
        return which and {} or d.content
      end
      local present = rec.exists
      if present == which then return d.content end
      return {}
    end,
  }
end

-- ----------------------------------------------------------------- report

local function report()
  if n_declared == 0 and #tbl_order == 0 then return end
  local w = io.stderr
  if n_declared > 0 then
    w:write(string.format("  figures : %d/%d present", n_present, n_declared))
    if n_present < n_declared then
      local missing = {}
      for _, id in ipairs(fig_order) do
        if not figs[id].exists then missing[#missing + 1] = id end
      end
      w:write("  (still to come: " .. table.concat(missing, ", ") .. ")")
    end
    w:write("\n")
  end
  if #tbl_order > 0 then
    w:write(string.format("  tables  : %d numbered\n", #tbl_order))
  end
  for _, id in ipairs(fig_order) do
    if figs[id].exists and figs[id].refs == 0 then
      w:write('            (figure "' .. id .. '" is never referenced in the text)\n')
    end
  end
  for _, m in ipairs(problems) do
    w:write("  FIGURE PROBLEM: " .. m .. "\n")
  end
end

function Pandoc(doc)
  collect(doc)
  local out = rewrite(doc)
  report()
  return out
end
