"""
Build thinking_ahead_lab_report.docx from thinking_ahead_lab.md, on the Lab 2 report's template.

    python3 planning_and_decisionmaking/thinking_ahead_lab/build_report.py

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
DST = Path(__file__).with_name('thinking_ahead_lab_report.docx')
HANDOUT = Path(__file__).with_name('thinking_ahead_lab.md').read_text(encoding='utf-8')

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


def even(n, total=9360):
    return [total // n] * n


PAIRS = ['1: sure $3,000 against 80% of $4,000', '2: sure $240 against 25% of $1,000', '3: 90% of $3,000 against 45% of $6,000', '4: 0.2% of $3,000 against 0.1% of $6,000']
PROCEDURES = ['Search everything', 'Goal recursion', 'Largest disk out of place', 'Move pattern', 'Memorized moves']
HOMININS = ['Adapted', 'Learned value', 'Copier', 'Shallow planner', 'Planner']

TABLES = {
    'Q1': [table(['Pair', 'Your choice, gains', 'Published share choosing that way', 'Your choice, losses', 'Published share choosing that way', 'Same as the majority?'], blank_rows(PAIRS, 5), [2400, 1300, 1500, 1300, 1500, 1360])],
    'Q7': [table(['', '1 week', '1 month', '6 months', '1 year', '5 years'], blank_rows(['Your indifference point, $ today'], 5), [2860, 1300, 1300, 1300, 1300, 1300]),
           table(['Curve', 'Its parameter', 'Summed squared error', 'Your choice, $50 today or $55 in 1 week', 'What the curve says', 'Your choice, $50 in 52 weeks or $55 in 53', 'What the curve says'], blank_rows(['A constant factor per day', 'A hyperbola'], 6), [1800, 1100, 1200, 1500, 1200, 1500, 1060])],
    'Q9': [table(['Block', 'Which came first?', 'Share of trials on which you waited for the delivery', 'Your points a minute', 'The best policy’s points a minute'], blank_rows(['The blue dispenser', 'The orange dispenser'], 4), [1900, 1500, 2600, 1600, 1760])],
    'Q11': [table(['Puzzle', 'Your moves', 'The shortest solution', 'Moves off the shortest path', 'Long pauses, and where on the graph they were'], blank_rows(['Three disks', 'Four disks'], 4), [1400, 1200, 1500, 1400, 3860])],
    'Q13': [table(['Procedure', 'Moves', 'Examined', 'Stored at most', 'Solved a scrambled start?', 'Solved with five disks?', 'Your prediction, and was it right?'], blank_rows(PROCEDURES, 6), [2100, 900, 1000, 1100, 1300, 1300, 1660])],
    'Q16': [table(['', 'Net points over the 16 tests', 'Clicks per tree', 'On the large-loss trees: times the −40 was uncovered', 'Times a look went below it', 'Points not earned on those trees'], [['You', '', '', '', '', ''], ['Look at nothing', '', '', '—', '—', '—'], ['Look at everything', '', '', '', '', ''], ['One more look when it is worth it', '', '', '', '', '']], [2400, 1400, 1200, 1700, 1300, 1360])],
    'Q19': [table(['Day', 'The cue', 'Your acts, in order, from the log', 'Did your hominin eat?', 'What the elder did'], blank_rows(['1', '2'], 4), [700, 1800, 3300, 1500, 2060])],
    'Q20': [table(['', 'A', 'B', 'C', 'D', 'E'], blank_rows(['T1 The usual day: share of days on which it ate'], 5), [3360, 1200, 1200, 1200, 1200, 1200])],
    'Q21': [table(['', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6'], blank_rows(list('ABCDE'), 6), [1200, 1360, 1360, 1360, 1360, 1360, 1360])],
    'Q23': [table(['', 'T2', 'T4', 'T5', 'T6'], blank_rows(HOMININS, 4), [2560, 1700, 1700, 1700, 1700])],
    'Q26': [table(['Heritability within the tray', 'Even soil', 'Patchy soil'], blank_rows(['Varied stock', 'One uniform line'], 2), [3360, 3000, 3000])],
    'Q27': [table(['', 'Heritability within the first tray', 'Heritability within the second tray', 'Difference between the trays’ mean heights, cm'], blank_rows(['Two uniform lines, the same even soil', 'One varied stock, complete solution against half the nitrates and no zinc', 'After the nitrates are restored', 'After the zinc is restored'], 3), [3600, 1900, 1900, 1960])],
    'Q28': [table(['', 'Correlation within identical pairs', 'Correlation within fraternal pairs', 'The twin estimate', 'The true share from genes'], blank_rows(['The reading’s figures', 'Identical twins treated more alike, about 0.20'], 4), [3000, 1600, 1600, 1500, 1660])],
    'Q29': [table(['', 'Heritability within the tray', 'Mean height, cm'], blank_rows(['Poor soil', 'Rich soil', 'Season 1', 'Season 6'], 2), [3360, 3000, 3000])],
}
PARTS = {
    'Q1': 'Part 1 — Choices',
    'Q11': 'Part 2 — Puzzles',
    'Q19': 'Part 3 — What They Carried',
    'Q26': 'Part 4 — Two Trays',
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
        for t in TABLES[q]:
            body += t + EMPTY
        body += para('WRITE YOUR ANSWER HERE')
    else:
        body += para('WRITE YOUR ANSWER HERE')
    body += EMPTY

with zipfile.ZipFile(SRC) as zin:
    doc = zin.read('word/document.xml').decode('utf-8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    tail = doc[doc.rindex('<w:sectPr'):] if '<w:sectPr' in doc else '</w:body></w:document>'
    core = zin.read('docProps/core.xml').decode('utf-8')
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 12 Report</dc:title>', core)
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
