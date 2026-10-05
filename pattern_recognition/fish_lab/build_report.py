"""
Build fish_lab_report.docx from fish_lab.md, on the Lab 2 report's template.

    python3 pattern_recognition/fish_lab/build_report.py

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
DST = Path(__file__).with_name('fish_lab_report.docx')
HANDOUT = Path(__file__).with_name('fish_lab.md').read_text(encoding='utf-8')

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


W4 = [2340, 2340, 2340, 2340]
FISH = ['Healthy', 'F1', 'F2', 'F3', 'F4']
CRITERIA = ['−1.50', '−1.00', '−0.75', '−0.50', '0', '+0.50', '+0.75', '+1.00']

TABLES = {
    'Q4': table(['After', 'Weight from A', 'Weight from B', 'Baseline', 'Test set, percent wrong'],
                [[f'{n} encounters', '', '', '', ''] for n in (100, 200, 300)], [2000, 1800, 1800, 1700, 2060]),
    'Q6': table(['How much smells vary', 'Test set, percent wrong after 1,000 encounters'],
                [['0.06 (from Step 3)', ''], ['0.15', ''], ['0.20', '']], [3600, 5760]),
    'Q7': table(['Criterion', 'Hits', 'Misses', 'False alarms', 'Correct rejections', 'Hit rate', 'False-alarm rate', 'Percent correct', 'd′'],
                [[c, '', '', '', '', '', '', '', ''] for c in ('0', '−0.50', '+0.50')],
                [1100, 900, 950, 1050, 1250, 950, 1150, 1100, 910]),
    'Q9': table(['Criterion', 'Energy per 100, the fish’s stakes', 'Energy per 100, the reading’s example'],
                [[c, '', ''] for c in CRITERIA], [2000, 3680, 3680]),
    'Q10': table(['How often an eel is upstream', 'Criterion that earns the most, the fish’s stakes'],
                 [['20%', ''], ['50% (from Q9)', ''], ['80%', '']], [3600, 5760]),
    'Q11': table(['Fish', 'Hits', 'Misses', 'False alarms', 'Correct rejections', 'Percent correct', 'd′', 'Criterion', 'Your diagnosis, before Reveal', 'The one change, after Reveal'],
                 [[f, '', '', '', '', '', '', '', '—' if f == 'Healthy' else '', '—' if f == 'Healthy' else ''] for f in FISH],
                 [850, 700, 800, 800, 1000, 900, 650, 900, 1400, 1360]),
    'Q14': table(['In a stream where an eel is upstream 80% of the time', 'Energy per 100 encounters'],
                 [['F4, with This fish’s stream on', ''], ['Healthy, with the base rate set to 80% by hand', '']], [5600, 3760]),
    'Q15': table(['Person', 'Hits', 'Misses', 'False alarms', 'Correct rejections', 'd′', 'Criterion', 'Percent correct'],
                 [['First', '42', '8', '8', '42', '', '', ''], ['Second', '49', '1', '25', '25', '', '', '']],
                 [1100, 900, 950, 1150, 1500, 1100, 1300, 1360]),
    'Q17': table(['Smell (A, B)', 'What it is', 'Hidden unit 1', 'Hidden unit 2', 'Output unit', 'Eat?'],
                 [['(0.15, 0.15)', 'twig or leaf', '', '', '', ''], ['(0.85, 0.15)', 'ripe fruit, first kind', '', '', '', ''],
                  ['(0.15, 0.85)', 'ripe fruit, second kind', '', '', '', ''], ['(0.85, 0.85)', 'rotting fruit', '', '', '', '']],
                 [1500, 2400, 1400, 1400, 1400, 1260]),
    'Q20': table(None, [['The four lines under Hidden unit 1, with their numbers', '']], [4000, 5360]),
    'Q21': table(['Hidden units', 'Seed 1: test set, percent wrong', 'Seed 2', 'Seed 3'],
                 [[n, '', '', ''] for n in ('1', '2', '4', '6')], W4),
    'Q24': table(['Setting, no hidden units', 'Result'],
                 [['No built-in receptor, 1,000 encounters', 'percent wrong:'],
                  ['Distance from the ideal strength', 'encounters to reach 5% wrong:'],
                  ['Both together, 1,000 encounters', 'percent wrong:']], [4600, 4760]),
    'Q25': table(['Hidden units, fixed at random', 'Percent wrong, not sparse', 'Percent wrong, sparse'],
                 [[n, '', ''] for n in ('2', '10', '50', '200')], [3000, 3180, 3180]),
    'Q27': table(['Hidden units', 'Encounters to reach 5% wrong (or percent wrong after 5,000)', 'Shape of the boundary'],
                 [[n, '', ''] for n in ('3', '4', '6')], [1800, 4200, 3360]),
    'Q28': table(['Route', 'Hidden units used', 'Encounters needed', 'What had to be in place before learning began'],
                 [['Built in: Distance from the ideal strength', '', '', ''], ['Wired at random: 50 sparse units', '', '', ''],
                  ['Learned: Pass the error back', '', '', '']], [2800, 1600, 1700, 3260]),
    'Q29': table(['After', 'Training, percent wrong', 'Test set, percent wrong', 'Encounters per individual, on average'],
                 [[f'{n} encounters', '', '', ''] for n in ('1,000', '3,000', '5,000')], W4),
    'Q30': table(['Setting', 'Training, percent wrong', 'Test set, percent wrong', 'Gap'],
                 [['6 individuals, 8 hidden units (from Q29)', '', '', ''], ['6 individuals, 2 hidden units', '', '', ''],
                  ['24 individuals, 8 hidden units', '', '', ''], ['60 individuals, 8 hidden units', '', '', ''],
                  ['a stream, 8 hidden units', '', '', '']], [3600, 2000, 2000, 1760]),
    'Q31': table(['After', 'Near test set, percent wrong', 'Far test set, percent wrong'],
                 [['300 encounters', '', ''], ['2,300 encounters', '', '']], [3000, 3180, 3180]),
    'Q33': table(['Repair', 'Near test set, percent wrong', 'Far test set, percent wrong'],
                 [['None (from Q31)', '', ''], ['Learn from every distance', '', ''],
                  ['Proportion of A, beside A and B, near only', '', ''], ['Proportion only, near only', '', '']],
                 [4000, 2680, 2680]),
    'Q35': table(['', 'Eel and sucker test set, percent wrong', 'Pike and chub test set, percent wrong'],
                 [['After phase 1 (1,000 encounters)', '', ''], ['Phase 2, after 100 encounters', '', ''],
                  ['Phase 2, after 1,000 encounters', '', '']], [3400, 2980, 2980]),
    'Q37': table(['', 'Eel and sucker test set, percent wrong', 'Pike and chub test set, percent wrong'],
                 [['Phase 2 with Eels and suckers stay around, after 1,000 encounters', '', '']], [3400, 2980, 2980]),
    'Q39': table(['Change', 'Sensitivity or criterion?', 'The instrument that shows it'],
                 [['(a) raising arousal and vigilance in Part 2', '', ''], ['(b) F3’s weights', '', ''],
                  ['(c) adding two hidden units in Part 3', '', ''], ['(d) switching on Distance from the ideal strength in Part 4', '', ''],
                  ['(e) going downstream in Part 5', '', '']], [4000, 2400, 2960]),
}
PARTS = {
    'Q1': 'Part 1 — One Line Will Do',
    'Q7': 'Part 2 — Jumpy or Blind?',
    'Q16': 'Part 3 — Ripe or Rotting',
    'Q24': 'Part 4 — Built In, Wired at Random, or Learned',
    'Q29': 'Part 5 — The Eels It Has Smelled',
    'Q35': 'The Closer — A New Predator',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 7 Report</dc:title>', core)
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
