"""
Build object_lab_report.docx from object_lab.md, on the Lab 2 report's template.

    python3 perception_and_action/object_lab/build_report.py

Every "- **Qn.** ..." bullet in the handout becomes a question in the report,
in order; the questions that ask for numbers or a table get a table; the
rest get "WRITE YOUR ANSWER HERE". The close-out in the app repo checks that
the two documents ask the same questions, so rerun this after any edit to
the handout that touches a question.
"""
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'comparative_approaches/evolution_lab/evolution_lab_report.docx'
DST = Path(__file__).with_name('object_lab_report.docx')
HANDOUT = Path(__file__).with_name('object_lab.md').read_text(encoding='utf-8')

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


LAYERS = ['input', 'pooled 1', 'pooled 2', 'pooled 3', 'pooled 4']
NETS = ['Standard', 'Trained on noise A', 'Trained on blurred and sharp']

TABLES = {
    'Q3': table(['Shift'] + LAYERS, [['2 pixels', '', '', '', '', ''], ['8 pixels', '', '', '', '', '']], [1560, 1560, 1560, 1560, 1560, 1560]),
    'Q7': table(['', 'Mid-line, percent right', 'At the joints, percent right'], [['you', '', ''], ['the network', '', '']], [2400, 3480, 3480]),
    'Q8': table(['Ink removed', 'Mid-line', 'At the joints', 'Gap'], [['35%', '', '', ''], ['50%', '', '', ''], ['65%', '', '', '']], [2340, 2340, 2340, 2340]),
    'Q12': table(['Set', 'Between, d′', 'Beyond, d′', 'At right angles, d′'], [['One shoe among shoes', '', '', ''], ['One shoe among other things', '', '', '']], [3400, 1986, 1986, 1988]),
    'Q15': table(['Set', 'Between, d′', 'Beyond, d′', 'At right angles, d′'], [['One shoe among shoes, the readout', '', '', ''], ['One shoe among other things, the readout', '', '', '']], [3400, 1986, 1986, 1988]),
    'Q17': table(['', 'clean', 'noise A', 'noise B'], [[n, '', '', ''] for n in NETS] + [['you', '', '', ''], ['your settled level', '—', '', '']], [3400, 1986, 1986, 1988]),
    'Q18': table(['', 'noise A at 0.20', 'noise B at 0.35'], [['Standard', '', ''], ['Trained on noise A', '', '']], [3400, 2980, 2980]),
    'Q21': table(['Network', 'Percent right on 800 held-out drawings'], [[n, ''] for n in NETS] + [['the drawing network', ''], ['chance', '']], [4600, 4760]),
}
PARTS = {
    'Q1': 'Part 1 — Inside the Stack',
    'Q7': 'Part 2 — Parts',
    'Q12': 'Part 3 — Views',
    'Q17': 'Part 4 — Noise',
    'Q20': 'The Closer — A Drawing Is Not a Photograph',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 8 Report</dc:title>', core)
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
