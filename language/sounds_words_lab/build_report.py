"""
Build sounds_words_lab_report.docx from sounds_words_lab.md, on the Lab 2 report's template.

    python3 language/sounds_words_lab/build_report.py

Every "- **Qn.** ..." bullet in the handout becomes a question in the report,
in order. A Markdown table that follows a question, before the next one,
becomes a table in the report, read from the handout itself so that the two
cannot drift; the rest get "WRITE YOUR ANSWER HERE". The close-out in the app
repo checks that the two documents ask the same questions, so rerun this after
any edit to the handout that touches a question.
"""
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'comparative_approaches/evolution_lab/evolution_lab_report.docx'
DST = Path(__file__).with_name('sounds_words_lab_report.docx')
HANDOUT = Path(__file__).with_name('sounds_words_lab.md').read_text(encoding='utf-8')
TITLE = 'Lab 13 Report'
PARTS = {'Q1': 'Part 1 — Sounds', 'Q8': 'Part 2 — Stream', 'Q17': 'Part 3 — Words', 'Q22': 'Part 4 — Predictors'}
TOTAL_WIDTH = 9360


def strip_md(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    t = re.sub(r'`(.+?)`', r'\1', t)
    return t


def parse_tables(block):
    """Every Markdown table in a stretch of the handout: (header, rows), cells stripped of markup."""
    tables = []
    lines = block.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1]):
            header = [strip_md(c.strip()) for c in lines[i].strip().strip('|').split('|')]
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([strip_md(c.strip()) for c in lines[i].strip().strip('|').split('|')])
                i += 1
            tables.append((header, rows))
        else:
            i += 1
    return tables


def widths(header, rows):
    """Column widths in twentieths of a point, in proportion to the longest text in each column, the first column never under a fifth."""
    n = len(header)
    longest = [max([len(header[k])] + [len(r[k]) if k < len(r) else 0 for r in rows]) for k in range(n)]
    longest = [max(6, x) for x in longest]
    total = sum(longest)
    w = [int(TOTAL_WIDTH * x / total) for x in longest]
    w[-1] += TOTAL_WIDTH - sum(w)
    return w


def table_xml(header, rows):
    w = widths(header, rows)
    grid = ''.join(f'<w:gridCol w:w="{x}"/>' for x in w)

    def cell(text, x, bold=False):
        rpr = '<w:rPr><w:b/></w:rPr>' if bold else ''
        run = f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>' if text else '<w:r/>'
        return f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{x}"/></w:tcPr><w:p>{run}</w:p></w:tc>'

    out = ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:type="auto" w:w="0"/>'
           '<w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/></w:tblPr>'
           f'<w:tblGrid>{grid}</w:tblGrid>')
    out += '<w:tr>' + ''.join(cell(h, x, True) for h, x in zip(header, w)) + '</w:tr>'
    for r in rows:
        r = r + [''] * (len(header) - len(r))
        out += '<w:tr>' + ''.join(cell(c, x) for c, x in zip(r, w)) + '</w:tr>'
    return out + '</w:tbl>'


def para(text, style=None, bold=False):
    ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ''
    rpr = '<w:rPr><w:b/></w:rPr>' if bold else ''
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


EMPTY = '<w:p/>'

# The questions in order, each with the handout text that follows it up to the next question or heading.
matches = list(re.finditer(r'^- \*\*(Q\d+)\.\*\* (.+)$', HANDOUT, re.M))
questions = []
for k, m in enumerate(matches):
    end = matches[k + 1].start() if k + 1 < len(matches) else len(HANDOUT)
    after = HANDOUT[m.end():end]
    after = after.split('\n#')[0]
    questions.append((m.group(1), m.group(2), parse_tables(after)))
assert [int(q[0][1:]) for q in questions] == list(range(1, len(questions) + 1)), 'the questions are not numbered in order'

body = para('Names', bold=True)
body += para('Please list all names in your group. Remember, you will not be penalized for cheating or plagiarism if you have any answers that are the same as other members of your group. No more than four members per group.')
for i in range(1, 5):
    body += para(f'Name {i}', style='ListNumber')
body += EMPTY
for q, text, tables in questions:
    if q in PARTS:
        body += para(PARTS[q], bold=True)
    body += para(f'{q}. {strip_md(text)}', style='ListBullet')
    body += EMPTY
    for header, rows in tables:
        body += table_xml(header, rows) + EMPTY
    body += para('WRITE YOUR ANSWER HERE')
    body += EMPTY

with zipfile.ZipFile(SRC) as zin:
    doc = zin.read('word/document.xml').decode('utf-8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    tail = doc[doc.rindex('<w:sectPr'):] if '<w:sectPr' in doc else '</w:body></w:document>'
    core = zin.read('docProps/core.xml').decode('utf-8')
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', f'<dc:title>{TITLE}</dc:title>', core)
    with zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == 'word/document.xml':
                zout.writestr(item, (head + body + tail).encode('utf-8'))
            elif item.filename == 'docProps/core.xml':
                zout.writestr(item, core.encode('utf-8'))
            elif item.filename == 'docProps/thumbnail.jpeg':
                continue
            else:
                zout.writestr(item, zin.read(item.filename))
print(f'wrote {DST.name}: {len(questions)} questions, {sum(len(t) for _, _, t in questions)} tables')
