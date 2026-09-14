"""
Build bilaterian_lab_report.docx from bilaterian_lab.md, on the Lab 2 report's template.

    python3 neural_circuits_affect_and_valence/bilaterian_lab/build_report.py

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
DST = Path(__file__).with_name('bilaterian_lab_report.docx')
HANDOUT = Path(__file__).with_name('bilaterian_lab.md').read_text(encoding='utf-8')

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


ANIMALS = ['W1', 'W2', 'W3', 'W4']
SCORE = ['Cues reached per minute', 'Reversals per minute', 'Time in reverse', 'Energy per cue reached']

TABLES = {
    'Q4': table(['Food weight b₁', 'Copper weight b₂', 'Crossings in 2 min', 'Harm in 2 min'],
                [['+1', '−1', '', ''], ['+3', '−3', '', ''], ['+3', '−1', '', ''], ['+3', '−0.2', '', ''],
                 ['your own:', '', '', ''], ['your own:', '', '', '']],
                [2340, 2340, 2340, 2340]),
    'Q6': table(None,
                [['Weight b₁ (food odor)', ''], ['Weight b₂ (cool water)', ''], ['Baseline b₀', ''], ['Threshold θ', ''],
                 ['Arithmetic, both cues present', ''], ['Arithmetic, food odor only', '']],
                [4000, 5360]),
    'Q8': table(None, [['The one number you changed, and its new value', '']], [4000, 5360]),
    'Q11': table(None,
                 [['Weight b₁ (food odor)', ''], ['Weight b₂ (predator scent)', ''], ['Baseline b₀', ''], ['Threshold θ', '']],
                 [4000, 5360]),
    'Q13': table(['A fault in the…', '…looks like this on the Circuit panel', '…on the Chemistry panel', '…in the dish'],
                 [['Wiring (a weight, a switch, a threshold)', '', '', ''], ['Chemistry (a modulator level)', '', '', '']],
                 [2340, 2340, 2340, 2340]),
    'Q14': table(['Animal'] + SCORE + ['What it does'],
                 [[a, '', '', '', '', ''] for a in ANIMALS],
                 [700, 1500, 1500, 1300, 1500, 2860]),
    'Q15': table(['Animal', 'Wiring, chemistry, or nowhere?', 'Your reason'],
                 [[a, '', ''] for a in ANIMALS],
                 [800, 2800, 5760]),
    'Q16': table(['Animal', 'Cue concentration', 'Cues reached per minute', 'What it did'],
                 [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                 [1200, 1800, 2200, 4160]),
    'Q17': table(['Animal', 'What was actually wrong', 'Wiring, chemistry, or nowhere', 'Did your Q15 guess match? What misled you?'],
                 [[a, '', '', ''] for a in ANIMALS],
                 [800, 3200, 2000, 3360]),
    'Q20': table(['Control', 'Moves the animal toward', 'The molecule', 'Your reason'],
                 [['pursuit', '', '', ''], ['satiety and tone', '', '', ''], ['arousal and vigilance', '', '', ''], ['relief', '', '', '']],
                 [1800, 2200, 1800, 3560]),
}
PARTS = {
    'Q1': 'Part 1 — Where Good and Bad Come From',
    'Q6': 'Part 2 — Build the Animal from the Truth Table',
    'Q13': 'Part 3 — Same Diagram, Different Chemistry',
    'Q21': 'The Closer — What the Animal Cannot Do',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 4 Report</dc:title>', core)
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
