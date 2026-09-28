"""
Build brain_lab_report.docx from brain_lab.md, on the Lab 2 report's template.

    python3 vertebrate_neural_architecture/brain_lab/build_report.py

Every "- **Qn.** ..." bullet in the handout becomes a question in the report,
in order; the questions that ask for a table get one; the rest get "WRITE
YOUR ANSWER HERE". The close-out in the app repo checks that the two
documents ask the same questions, so rerun this after any edit to the
handout that touches a question.
"""
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'comparative_approaches/evolution_lab/evolution_lab_report.docx'
DST = Path(__file__).with_name('brain_lab_report.docx')
HANDOUT = Path(__file__).with_name('brain_lab.md').read_text(encoding='utf-8')

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


STRUCTURES = ['spinal cord', 'hindbrain', 'reticular formation', 'norepinephrine cluster', 'cerebellum', 'tectum',
              'periaqueductal gray', 'dopamine clusters', 'serotonin clusters', 'hypothalamus', 'thalamus',
              'basal ganglia', 'amygdala', 'pallium', 'hippocampus']
BENCH = ['hindbrain and reticular formation', 'norepinephrine cluster', 'cerebellum', 'tectum (superior colliculus)',
         'periaqueductal gray', 'dopamine clusters', 'hypothalamus', 'thalamus', 'basal ganglia (striatum)', 'amygdala',
         'pallium (neocortex)', 'hippocampus', 'serotonin clusters']
CARDS = ['1. A tectum that maps space and orients the animal', '2. Basal ganglia with two opposed pathways', '3. A pallium',
         '4. A cerebellum', '5. A six-layered pallium (neocortex)', '6. Basal ganglia output nucleus divided in two',
         '7. A corpus callosum', '8. An amygdala-like region', '9. A large brain for its body size']
EXPERIMENTS = [
    ('Remove the hindbrain', '—'), ('Remove the neocortex', 'Open field'), ('Remove the neocortex', 'Lever'),
    ('Remove the dopamine clusters', 'Lever'), ('Remove the dopamine clusters', 'Tone and shock'), ('Remove the dopamine clusters', 'Open field'),
    ('Silence dopamine fibers during training', 'Lever'), ('Silence dopamine fibers during training', 'Timed blink'),
    ('Silence climbing fibers during training', 'Timed blink (both readouts)'), ('Silence climbing fibers during training', 'Lever'),
    ('Silence climbing fibers during training', 'Tone and shock'),
    ('Remove the amygdala', 'Tone and shock'), ('Remove the amygdala', 'Cue and food'), ('Remove the amygdala', 'Lever'),
    ('Stimulate the periaqueductal gray', '—'), ('Stimulate one point on the tectum, at 0 and at 1', '—'),
    ('Stimulate the dopamine clusters', 'Open field'), ('Stimulate the dopamine clusters', 'Lever'),
]
TASKS = ['Orient', 'Tone and shock', 'Cue and food', 'Lever', 'Timed blink', 'Open field']

TABLES = {
    'Q2': table(['Card', 'You said', 'It was', 'Kind of error'], [['', '', '', ''] for _ in range(5)], [1500, 2500, 2500, 2860]),
    'Q4': table(['Structure', 'Which division', 'What the reading says it does (one line)'],
                [[s, '', ''] for s in STRUCTURES], [2400, 2200, 4760]),
    'Q8': table(['Card', 'Where you placed it', 'Where the key places it', 'Match?'],
                [[c, '', '', ''] for c in CARDS], [3400, 2400, 2400, 1160]),
    'Q13': table(['Structure'] + TASKS + ['What it appears to be for'],
                 [[s] + [''] * 7 for s in BENCH], [1900, 800, 900, 900, 800, 900, 900, 2260]),
    'Q16': table(['Experiment', 'Task', 'Label', 'Found in', 'Result'],
                 [[e, t, '', '', ''] for e, t in EXPERIMENTS], [2600, 1700, 1300, 1300, 2460]),
    'Q22': table(['Kind of learning', 'Which pathway, when silenced, stopped it?', 'Which task showed it', 'Which task was untouched'],
                 [[k, '', '', ''] for k in ['unsupervised', 'prediction', 'supervised', 'reinforcement']], [2000, 2800, 2300, 2260]),
    'Q24': table(['Structure', 'Jobs it took part in, on the evidence of Step 2', 'Which single job you assigned it in Step 1'],
                 [[s, '', ''] for s in ['amygdala', 'basal ganglia (striatum)', 'cerebellum', 'dopamine clusters', 'pallium (neocortex)']],
                 [2400, 4000, 2960]),
}
PARTS = {
    'Q1': 'Part 1 — One Plan, Many Brains',
    'Q13': 'Part 2 — An Address Is Not an Account',
    'Q25': 'The Closer — Design One Experiment',
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
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 6 Report</dc:title>', core)
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
