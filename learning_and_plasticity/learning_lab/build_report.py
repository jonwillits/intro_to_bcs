"""
Build learning_lab_report.docx from learning_lab.md, on the Lab 2 report's template.

    python3 learning_and_plasticity/learning_lab/build_report.py

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
DST = Path(__file__).with_name('learning_lab_report.docx')
HANDOUT = Path(__file__).with_name('learning_lab.md').read_text(encoding='utf-8')

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


RULES = ['Coincidence', 'Prediction', 'Teacher', 'Verdict']
W4 = [2340, 2340, 2340, 2340]

TABLES = {
    'Q1': table(['', 'b₁ at the start', 'b₁ after 4 minutes', 'Harm after 4 minutes'],
                [['Learning on', '', '', ''], ['Learning off', '', '', '']], W4),
    'Q6': table(['Learning rate η', 'By hand, with both rates at 40', 'What the salt weight did'],
                [['1', '', 'reached 3.00 after about:'], ['0.01', '', 'after 3 minutes it was:          over this many meals:']],
                [1800, 2800, 4760]),
    'Q7': table(['Run', 'What you set', 'Weights after the run'],
                [['Second cue, 3 minutes', 'almond odor at every site', 'salt:          almond odor:'],
                 ['Delay, 5 minutes', 'interval 10 s', 'salt:'],
                 ['Part 1a, 3 minutes', 'b₁ = −2', 'b₁:'],
                 ['Part 1a, 3 minutes', 'b₁ = 0.1', 'b₁:']],
                [2600, 3000, 3760]),
    'Q9': table(['Bounds', 'Salt weight at the end', 'Did the weight trace ever go down?', 'Roughly what fraction of the last minute was the verdict on?'],
                [['Both off', '', '', ''], ['Weakening on', '', '', ''], ['Competition on', '', '', ''],
                 ['Competition on, with the second cue', 'salt:      almond odor:', '', '']], W4),
    'Q11': table(['Rule', 'Salt weight when it stopped climbing', 'After phase 2: salt', 'After phase 2: almond odor', 'Phase 3: does it seek out almond odor?'],
                 [['Coincidence', '', '', '', ''], ['Prediction', '', '', '', '']],
                 [1500, 2100, 1700, 1900, 2160]),
    'Q14': table(None, [['What the panel showed at one meal (both lines)', '']], [4000, 5360]),
    'Q16': table(['Rule', 'After 3 min — salt', 'After 3 min — almond odor', '3 min after the flip — salt', '3 min after the flip — almond odor'],
                 [[r, '', '', '', ''] for r in RULES],
                 [1500, 1900, 2000, 1900, 2060]),
    'Q17': table(['Rule', 'What Φ was', 'Where that number came from'],
                 [[r, '', ''] for r in RULES], [1500, 3000, 4860]),
    'Q18': table(['Rank (1 = easiest for an animal to get)', 'Rule', 'Your reason'],
                 [['1', '', ''], ['2', '', ''], ['3', '', ''], ['4', '', '']], [2400, 1800, 5160]),
    'Q20': table(['', 'First trial on which its value passed 0.30', 'On trial 1', 'On about trial 30'],
                 [['the approach', '', '—', '—'], ['the turn', '', '—', '—'], ['the marker', '', 'value:', 'value:'],
                  ['Surprise at the food', '—', '', '']], W4),
    'Q22': table(['Trace window', 'First trial on which the marker’s value passed 0.30', 'Surprise at the food at the end'],
                 [['0 s', '', ''], ['3 s (from Step 2)', '', ''], ['10 s', '', '']], [2000, 4200, 3160]),
    'Q24': table(['Discount γ', 'An outcome 10 s away is worth', 'Last row of the grid: marker, turn, approach'],
                 [['0.5', '', ''], ['0.9 (from Step 2)', '', ''], ['0.99', '', '']], [2000, 3000, 4360]),
    'Q25': table(['', 'Salt weight', 'dish one', 'session one', 'Response to salt alone'],
                 [['Before acquisition', '0.00', '0.00', '0.00', ''], ['After acquisition', '', '', '', ''], ['After extinction', '', '', '', '']],
                 [2200, 1700, 1700, 1700, 2060]),
    'Q26': table(['Button', 'What it does', 'Response to salt alone', 'Did any weight move?'],
                 [['(after extinction)', '', '', ''], ['Move to the second dish', 'the animal is in another dish', '', ''],
                  ['Move back to the first dish', '', '', ''], ['Wait', 'time passes, with no training of any kind', '', ''],
                  ['Deliver one outcome', 'one meal at its mouth, with no cue', '', '']], [2400, 3000, 2000, 1960]),
}
PARTS = {
    'Q1': 'Part 1 — Let the Weights Change',
    'Q11': 'Part 2 — Where the Number Comes From',
    'Q19': 'Part 3 — Credit Across Time',
    'Q25': 'The Closer — Extinction Is Not Unlearning',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 5 Report</dc:title>', core)
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
