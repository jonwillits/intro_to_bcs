"""
Build among_others_lab_report.docx from among_others_lab.md, on the Lab 2 report's template.

    python3 social_cognition/among_others_lab/build_report.py

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
DST = Path(__file__).with_name('among_others_lab_report.docx')
HANDOUT = Path(__file__).with_name('among_others_lab.md').read_text(encoding='utf-8')

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


def blank_rows(labels, cols):
    return [[label] + [''] * cols for label in labels]


PARTNERS = ['Always cooperate', 'Always defect', 'Tit-for-tat', 'Defect forever after one defection', 'Win-stay, lose-shift', 'Suspicious tit-for-tat']
ENTRIES = PARTNERS + ['My rule', 'Predictor']
ANIMALS = ['Barriers', 'Gaze', 'Line of sight now', 'Line of sight before', 'Learner, the usual room', 'Learner, many rooms']

TABLES = {
    'Q1': table(['Partner', 'Its rule', 'Your diagnosis right?', 'Rounds', 'Your points', 'Its points', 'Predictions right (share)', 'Best possible', 'Share of best'], blank_rows(list('ABCDEF'), 8), [800, 1500, 1100, 800, 900, 900, 1300, 1000, 1060]),
    'Q6': table(['R', 'Run 2, the match: Always defect : Tit-for-tat', 'Run 3, the round-robin: Tit-for-tat : Always defect', 'Run 4, the threshold x'], blank_rows(['1', '2', '3', '10', '200'], 3), [800, 3100, 3300, 2160]),
    'Q9': table(['Rank', 'Entry', 'Total (average points per round)'], blank_rows([str(i) for i in range(1, 8)], 2), [1200, 4600, 3560]),
    'Q11': table(['Partner', 'Points (mean ±)', 'Best possible', 'Share of best', 'Predicted right (share)', 'Probes', 'Lost to probing'], blank_rows(PARTNERS, 6), [2600, 1300, 1100, 1000, 1300, 900, 1160]),
    'Q13': table(['Partner', 'Rounds', 'You: predictions right (share)', 'You: share of best', 'Predictor: predictions right (share)', 'Predictor: share of best'], blank_rows(PARTNERS, 5), [2500, 900, 1600, 1300, 1700, 1360]),
    'Q14': table(['Rank', 'Entry', 'Total at 5% noise', 'Change from no mistakes'], blank_rows([str(i) for i in range(1, 9)], 3), [1000, 4000, 2200, 2160]),
    'Q15': table(['Entry', 'Share at 300, no mistakes', 'Share at 300, with mistakes'], blank_rows(ENTRIES, 2), [3600, 2800, 2960]),
    'Q18': table(['Start world', 'Your prediction', 'Which rule took over', 'At about what generation'], [['All tit-for-tat', '', '', ''], ['All always-cooperate', '', '', ''], ['All always-defect, single mutants only', '', '', ''], ['All always-defect, after a dropped block', '—', '', '']], [3200, 2000, 2200, 1960]),
    'Q21': table(['Film', 'What it was', 'Your rating, 1 to 7', 'What you ticked'], [['Film 1', 'the control', '', ''], ['Film 2', 'the scenario', '', ''], ['Film 3', 'the scenario reversed', '', '']], [1200, 2200, 1800, 4160]),
    'Q23': table(['', 'Correlation with inverse planning', 'Correlation with the “last moved toward” rule'], blank_rows(['all pauses', 'the pauses where the two disagree'], 2), [3200, 2900, 3260]),
    'Q25': table(['', 'A', 'B', 'C', 'D', 'E'], blank_rows(['T1 Standard: share on the scored piece'], 5), [3360, 1200, 1200, 1200, 1200, 1200]),
    'Q26': table(['', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'], blank_rows(list('ABCDE'), 7), [1000, 1194, 1194, 1194, 1194, 1194, 1194, 1196]),
    'Q28': table([''] + ANIMALS, [['T8, your runs', '', '', '', '', '', ''], ['T8, the full matrix', '', '', '', '', '', '—'], ['T2, the full matrix', '', '', '', '', '', '—']], [1800, 1200, 1100, 1300, 1300, 1400, 1260]),
    'Q30': table(['', 'Round 1', 'Round 2', 'Change'], blank_rows(['hit rate (shown members called Seen before)', 'false alarms to a changed detail', 'false alarms to a new member of a group', 'd′ for individuals', 'sorting accuracy'], 3), [4200, 1700, 1700, 1760]),
}
PARTS = {
    'Q1': 'Part 1 — Six Partners',
    'Q6': 'Part 2 — The Tournament',
    'Q21': 'Part 3 — Shapes and Paths',
    'Q25': 'Part 4 — What the Dominant Saw',
    'Q30': 'Part 5 — Two Rounds',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 11 Report</dc:title>', core)
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
