"""
Build way_home_lab_report.docx from way_home_lab.md, on the Lab 2 report's template.

    python3 spatial_cognition/way_home_lab/build_report.py

Every "- **Qn.** ..." bullet in the handout becomes a question in the report,
in order; the questions that ask for a table get the table; the rest get
"WRITE YOUR ANSWER HERE". The close-out in the app repo checks that the two
documents ask the same questions, so rerun this after any edit to the
handout that touches a question.
"""
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'comparative_approaches/evolution_lab/evolution_lab_report.docx'
DST = Path(__file__).with_name('way_home_lab_report.docx')
HANDOUT = Path(__file__).with_name('way_home_lab.md').read_text(encoding='utf-8')

questions = []
for m in re.finditer(r'^- \*\*(Q\d+)\.\*\* (.+)$', HANDOUT, re.M):
    questions.append((m.group(1), m.group(2)))
questions.sort(key=lambda q: int(q[0][1:]))


def strip_md(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    t = re.sub(r'`(.+?)`', r'\1', t)
    return t


def table(header, rows, widths):
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)

    def cell(text, w, bold=False):
        rpr = '<w:rPr><w:b/></w:rPr>' if bold else ''
        run = f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>' if text else '<w:r/>'
        return f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w}"/></w:tcPr><w:p>{run}</w:p></w:tc>'

    out = ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:type="auto" w:w="0"/>'
           '<w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/></w:tblPr>'
           f'<w:tblGrid>{grid}</w:tblGrid>')
    if header:
        out += '<w:tr>' + ''.join(cell(h, w, True) for h, w in zip(header, widths)) + '</w:tr>'
    for r in rows:
        out += '<w:tr>' + ''.join(cell(c, w) for c, w in zip(r, widths)) + '</w:tr>'
    return out + '</w:tbl>'


RATS = ['H', '(label)', '(label)', '(label)', '(label)', '(label)']

TABLES = {
    'Q2': table(['Trial', 'Beetles', 'Outward path, m', 'Your error, m', 'Running sum only, its error, m'], [[str(i), '', '', '', ''] for i in range(1, 9)], [1200, 1400, 2200, 2200, 2360]),
    'Q4': table(['Trial', 'Your error, m', 'Nearest program to you (smallest from you)', 'That program’s error, m'], [[str(i), '', '', ''] for i in range(1, 5)], [1200, 2200, 3600, 2360]),
    'Q7': table(['Trial', 'Landmarks moved', 'Your score', 'Running sum only', 'Landmarks only', 'Averaging', 'Following one'], [[str(i), '', '', '', '', '', ''] for i in range(1, 5)], [900, 1500, 1300, 1500, 1500, 1300, 1360]),
    'Q9': table(['Test', 'Ended at the east arm (the place)', 'Ended at the west arm (the same turn)'], [['rich room, 4 training trials', '', ''], ['rich room, 64 training trials', '', ''], ['plain enclosure, 4 training trials', '', '']], [3400, 2980, 2980]),
    'Q11': table(['Rat', 'Hidden platform: learns it?', 'Cues removed just before the choice: finds it?'], [[r, '', ''] for r in RATS], [1800, 3500, 4060]),
    'Q12': table(['Rat', 'Lamp in place', 'Lamp switched off', 'Lamp moved across the room'], [[r, '', '', ''] for r in RATS], [1800, 2400, 2400, 2760]),
    'Q24': table(['Habitat', 'Average rate, one every … s', 'Best setting, s', 'Beetles per minute at the best setting'], [['rich', '', '', ''], ['poor', '', '', '']], [1400, 2800, 2200, 2960]),
}
PARTS = {
    'Q1': 'Part 1 — The Way Home',
    'Q9': 'Part 2 — Places or Responses?',
    'Q15': 'Part 3 — Inside the Map',
    'Q24': 'The Closer — Stay or Go',
}


def para(text, style=None, bold=False):
    ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ''
    rpr = '<w:rPr><w:b/></w:rPr>' if bold else ''
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


EMPTY = '<w:p/>'
body = para('Names', bold=True)
body += para('Please list all names in your group. Remember, you will not be penalized for cheating or plagiarism if you have any answers that are the same as other members of your group. No more than four members per group.')
for i in range(1, 5):
    body += para(f'Name {i}', style='ListNumber')
body += EMPTY
for q, text in questions:
    if q in PARTS:
        body += para(PARTS[q], bold=True)
    body += para(f'{q}. {strip_md(text)}', style='ListBullet')
    body += EMPTY
    if q in TABLES:
        body += TABLES[q]
        body += EMPTY + para('WRITE YOUR ANSWER HERE')
    else:
        body += para('WRITE YOUR ANSWER HERE')
    body += EMPTY

with zipfile.ZipFile(SRC) as zin:
    doc = zin.read('word/document.xml').decode('utf-8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    tail = doc[doc.rindex('<w:sectPr'):] if '<w:sectPr' in doc else '</w:body></w:document>'
    core = zin.read('docProps/core.xml').decode('utf-8')
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 9 Report</dc:title>', core)
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
print(f'wrote {DST.name}: {len(questions)} questions')
