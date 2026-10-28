"""
Build last_night_lab_report.docx from last_night_lab.md, on the Lab 2 report's template.

    python3 memory_and_generative_models/last_night_lab/build_report.py

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
DST = Path(__file__).with_name('last_night_lab_report.docx')
HANDOUT = Path(__file__).with_name('last_night_lab.md').read_text(encoding='utf-8')

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


FORAGERS = ['you', 'Usual only', 'Tendency only', 'Tonight too', 'Tonight too, nights blurred']

TABLES = {
    'Q1': table(['Lists', 'First three positions', 'Middle positions', 'Last three positions'], [['typed at once', '', '', ''], ['typed after counting', '', '', '']], [2600, 2200, 2200, 2360]),
    'Q4': table(['Kind of word', 'Called old', 'Remember', 'Know'], [[k, '', '', ''] for k in ['studied, lists of associates', 'studied, unrelated lists', 'critical, studied lists', 'critical, control lists', 'new words']], [3800, 1800, 1800, 1960]),
    'Q7': table(['Set', 'Words recalled, of 24', 'ARC'], [['scrambled', '', ''], ['organized', '', '']], [3000, 3200, 3160]),
    'Q10': table(['Items', 'Hits', 'Misses', 'False alarms', 'Correct rejections', 'Hit rate', 'False-alarm rate', 'd′', 'Criterion'], [['fit a dorm room', '', '', '', '', '', '', '', ''], ['do not fit', '', '', '', '', '', '', '', '']], [1500, 800, 900, 1100, 1300, 1000, 1200, 700, 860]),
    'Q14': table(['', 'Nights 3 and 6', 'Nights 4 and 5', 'Night 3', 'Night 4', 'Night 5', 'Night 6'], [['kind of pair each followed', '', '', '', '', '', ''], ['beetles eaten', '—', '—', '', '', '', ''], ['when-errors of when-decisions', '', '', '', '', '', ''], ['share over digs alone', '', '', '—', '—', '—', '—'], ['a forager with no memory for nights, over digs', '', '', '—', '—', '—', '—']], [2800, 1200, 1200, 1040, 1040, 1040, 1040]),
    'Q17': table(['', 'Marked right, of 7', 'Marks of one night for another'], [['the question at the end of the week', '', '']], [3600, 2600, 3160]),
    'Q19': table([''] + FORAGERS, [[r, '', '', '', '', ''] for r in ['beetles eaten', 'digs at logs emptied last night', 'digs at smooth logs', 'share of when-errors after look-alike pairs', 'share of when-errors after different pairs']], [2800, 1000, 1300, 1400, 1300, 1560]),
    'Q20': table(['Setting', 'after look-alike pairs', 'after different pairs'], [['weak', '', ''], ['medium', '', ''], ['strong', '', '']], [2400, 3400, 3560]),
    'Q24': table(['', 'digs at logs emptied last night', 'digs at smooth logs'], [['Tonight too intact (totals)', '', ''], ['Remove the fast store (total, and rises or stays low)', '', ''], ['Damage the slow learner (total, and rises or stays low)', '', '']], [4200, 2700, 2460]),
}
PARTS = {
    'Q1': 'Part 1 — Lists of Words',
    'Q7': 'Part 2 — Two Ways to Study',
    'Q10': 'Part 3 — What Was in the Room?',
    'Q14': 'Part 4 — Nights at the Logs',
    'Q19': 'Part 5 — Learners',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 10 Report</dc:title>', core)
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
