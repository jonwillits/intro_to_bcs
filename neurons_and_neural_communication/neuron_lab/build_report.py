"""
Build neuron_lab_report.docx from neuron_lab.md, on the Lab 2 report's template.

    python3 neurons_and_neural_communication/neuron_lab/build_report.py

Every "- **Qn.** ..." bullet and "**Qn — title.** ..." paragraph in the handout
becomes a question in the report, in order; the questions that ask for numbers
get a table; the rest get "WRITE YOUR ANSWER HERE". The close-out in the app
repo checks that the two documents ask the same questions, so rerun this after
any edit to the handout that touches a question.
"""
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'comparative_approaches/evolution_lab/evolution_lab_report.docx'
DST = Path(__file__).with_name('neuron_lab_report.docx')
HANDOUT = Path(__file__).with_name('neuron_lab.md').read_text(encoding='utf-8')

questions = []
for m in re.finditer(r'^- \*\*(Q\d+)\.\*\* (.+)$', HANDOUT, re.M):
    questions.append((m.group(1), m.group(2)))
for m in re.finditer(r'^\*\*(Q\d+) — ([^*]+)\.\*\* (.+)$', HANDOUT, re.M):
    questions.append((m.group(1), f'{m.group(2)}. {m.group(3)}'))
questions.sort(key=lambda q: int(q[0][1:]))


def strip_md(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    t = re.sub(r'`(.+?)`', r'\1', t)
    return t


# Part 4's questions carry further paragraphs in the handout; folded in by hand.
EXTRAS = {
    'Q25': ["One caution, and it matters. §3.2.9 of the reading describes a much larger claim about what the simple model leaves out: that a neuron's branching input surface computes enough on its own that a single cortical cell may be better understood as a small network several layers deep. The simulation in front of you cannot show that claim at all, because the cell it models has no branching input surface. Say what the two curves do establish, and what they do not."],
    'Q26': ['(a) What will this cell do if a third input arrives at 20 spikes per second?', '(b) How long after the voltage crosses threshold does it reach its peak?', '(c) What happens to the vehicle if this connection changes sign?', '(d) Why can this cell not fire a thousand times a second?', 'Then one more, which is the point of the four questions above. Those four make the three levels look like three separate compartments, each minding its own business. §3.3.9 of the reading says something stronger: the levels are separable but not independent, and the implementational level sets terms the levels above it have to respect. You produced an example of exactly that in Q21 and Q22 — an energy budget, which is an implementational fact, deciding how many neurons can be firing at once, which is a fact about the algorithm. Explain that example in your own words, and say what it costs the picture of three tidy compartments.'],
}


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


TABLES = {
    'Q1': table(['Run', 'Signal type', 'Distance', 'World speed', 'Reaction time', 'Travel time', 'Lights collected'],
                [['1', 'Diffusing chemical', 'shortest', 'slow', '', '', ''],
                 ['2', 'Diffusing chemical', 'shortest', 'fast', '', '', ''],
                 ['3', 'Spikes', 'shortest', 'fast', '', '', ''],
                 ['4', 'Graded electrical', 'longest', 'fast', '', '', ''],
                 ['5a', 'Diffusing chemical', 'smallest', '', '', '', ''],
                 ['5b', 'Diffusing chemical', 'middle', '', '', '', ''],
                 ['5c', 'Diffusing chemical', 'largest', '', '', '', ''],
                 ['5d', 'Spikes', 'smallest', '', '', '', ''],
                 ['5e', 'Spikes', 'middle', '', '', '', ''],
                 ['5f', 'Spikes', 'largest', '', '', '', '']],
                [700, 1900, 1300, 1200, 1500, 1500, 1260]),
    'Q6': table(['Second input', 'The arithmetic the panel prints', 'What the arithmetic gives', 'Measured output rate'],
                [['0', '', '', ''], ['5', '', '', ''], ['15', '', '', '']],
                [1400, 3400, 2280, 2280]),
    'Q14': table(['A problem in the…', '…looks like this on the World tab', '…on the Unit tab', '…on the Membrane tab'],
                 [['World (the task itself)', '', '', ''], ['Unit (what the cell computes)', '', '', ''], ['Membrane (how the cell works)', '', '', '']],
                 [2340, 2340, 2340, 2340]),
    'Q16': table(['Cell', 'Tab you opened first, and why', 'Your diagnosis', 'Your reason'],
                 [['N1', '', '', ''], ['N2', '', '', ''], ['N3', '', '', ''], ['N4', '', '', '']],
                 [800, 3200, 2400, 2960]),
    'Q18': table(['Cell', 'What was actually wrong', 'Which level', 'Did your Q16 guess match? What misled you?'],
                 [['N1', '', '', ''], ['N2', '', '', ''], ['N3', '', '', ''], ['N4', '', '', '']],
                 [800, 3200, 1800, 3560]),
    'Q20': table(None,
                 [['Power at 10 spikes per second (watts)', ''], ['Firing rate at which the power is about 20 watts (spikes per second)', '']],
                 [5760, 3600]),
}
PARTS = {
    'Q1': 'Part 1 — Why a Neuron at All',
    'Q6': 'Part 2 — Taking the Cell Apart',
    'Q14': 'Part 3 — Four Sick Neurons',
    'Q20': 'Part 4 — What It Costs, and What Three Descriptions Are For',
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
    for extra in EXTRAS.get(q, []):
        body += para(strip_md(extra), style='ListBullet')
    body += EMPTY
    if q in TABLES:
        body += TABLES[q]
        if q in ('Q6', 'Q14', 'Q16', 'Q18'):
            body += EMPTY + para('WRITE YOUR ANSWER HERE')
    else:
        body += para('WRITE YOUR ANSWER HERE')
    body += EMPTY

with zipfile.ZipFile(SRC) as zin:
    doc = zin.read('word/document.xml').decode('utf-8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    tail = doc[doc.rindex('<w:sectPr'):] if '<w:sectPr' in doc else '</w:body></w:document>'
    core = zin.read('docProps/core.xml').decode('utf-8')
    core = re.sub(r'<dc:title>.*?</dc:title>|<dc:title/>', '<dc:title>Lab 3 Report</dc:title>', core)
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
