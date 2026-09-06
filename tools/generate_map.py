#!/usr/bin/env python3
"""Generate the standalone clickable supplement from the authoritative graph.

Usage: generate_map.py [graph.yaml] [target.tex]. Layout is layered by the
longest dependency chain, so new nodes need no hand-placed coordinates.
"""
from pathlib import Path
import hashlib
import sys
import yaml

root = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'docs/proof-graph.yaml'
# Keep the research output local by default. The current task authorizes
# synchronizing the manuscript map by an explicit target path.
target = Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'docs/proof_map.tex'
graph = yaml.safe_load(source.read_text())
digest = hashlib.sha256(source.read_bytes()).hexdigest()
nodes = graph['nodes']
by_id = {n['id']: n for n in nodes}


def esc(s):
    table = {'&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#',
             '{': r'\{', '}': r'\}', '$': r'\$', '^': r'\textasciicircum{}', '–': r'\textendash{}\allowbreak{}'}
    return ''.join(table.get(c, c) for c in str(s))


# Layered layout: layer = longest path from a source node.
layer = {}


def depth(key):
    if key in layer:
        return layer[key]
    deps = by_id[key]['depends_on']
    layer[key] = 0 if not deps else 1 + max(depth(d) for d in deps)
    return layer[key]


for k in by_id:
    depth(k)
rows = {}
for k, d in layer.items():
    rows.setdefault(d, []).append(k)
xstep, ystep = 4.4, -2.6
pos = {}
for d, keys in rows.items():
    keys.sort()
    width = (len(keys) - 1) * xstep
    for i, k in enumerate(keys):
        pos[k] = (i * xstep - width / 2, d * ystep)

tags = {'imported': 'IMPORTED', 'paper': 'PAPER', 'gap': 'GAP',
        'conditional': 'PAPER / CONDITIONAL'}
out = [r'''\documentclass[10pt]{article}
\usepackage[a4paper,landscape,margin=8mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\usepackage{parskip}
\usepackage{needspace}
\pagestyle{plain}
\begin{document}
\begin{center}
\phantomsection\label{map}{\Large Navier--Stokes: dependency map}

Arrows run from premise to consumer. Dashed GAP nodes remain unproved.
PAPER denotes a written argument; review scope appears on the following pages.

\resizebox{\textwidth}{!}{%
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth,
box/.style={draw,rounded corners=2pt,text width=3.6cm,minimum height=1.0cm,align=center,font=\small},
imported/.style={box,fill=blue!8},paper/.style={box,fill=black!3},
conditional/.style={box,fill=black!3,double},gap/.style={box,dashed,thick,fill=orange!10},
edge/.style={->,thin}]
''']
for n in nodes:
    x, y = pos[n['id']]
    out.append(r'\node[' + n['kind'] + '] (' + n['id'] + ') at (' + f'{x:.2f},{y:.2f}' + ') {'
               + r'\hyperref[node:' + n['id'] + ']{' + esc(n['title']) + r'}\\{\scriptsize '
               + tags[n['kind']] + '}};\n')
for n in nodes:
    for dep in n['depends_on']:
        style = 'edge,dashed' if by_id[dep]['kind'] == 'gap' else 'edge'
        out.append(r'\draw[' + style + '] (' + dep + ') -- (' + n['id'] + ');\n')
out += [r'''\end{tikzpicture}}

Phase I: ''' + esc(graph['phase_i_status']) + r'''. Phase II: ''' + esc(graph['phase_ii_status']) + r'''.
No terminal proof or counterexample is claimed.
\end{center}
\clearpage
\raggedright
''', 'Graph SHA-256: ' + r'\texttt{' + digest[:32] + '}' + r'\texttt{' + digest[32:] + '}.\n']
for n in nodes:
    out += [r'\Needspace{10\baselineskip}\section*{' + esc(n['id'] + ': ' + n['title']) + '}' + r'\phantomsection\label{node:' + n['id'] + '}\n',
            r'\textbf{Class:} ' + tags[n['kind']] + r'. \textbf{Formal:} ' + esc(n.get('formal', 'not started')) + '.' + '\n\n',
            esc(n['statement']) + '\n\n',
            r'\textbf{Mechanism:} ' + esc(n['mechanism']) + '.\n\n',
            r'\textbf{Review:} ' + esc(n['review']) + '\n\n',
            r'\textbf{Evidence:} \texttt{' + esc(n['evidence']) + '}. '
            + r'Manuscript label: \texttt{' + esc(n['paper_label']) + '}.\n\n',
            r'\textbf{Dependencies:} ' + (', '.join(r'\hyperref[node:' + d + ']{' + esc(d) + '}' for d in n['depends_on']) or 'none') + '. '
            + r'\hyperref[map]{Back to map}.' + '\n\n']
# Review-pending supplements are not claim nodes.
for candidate in graph.get('candidate_supplements', []):
    out += [r'\clearpage\section*{Review-pending component: ' + esc(candidate['title']) + '}\n',
            r'\textbf{Not a promoted claim or an arbitrary-data producer.}' + '\n\n',
            esc(candidate['status']) + '. ' + esc(candidate['scope']) + '\n\n',
            r'\textbf{Evidence:} \texttt{' + esc(candidate['evidence']) + '}.\n\n',
            r'\textbf{Manuscript labels:} ' + ', '.join(r'\texttt{' + esc(x) + '}' for x in candidate['paper_labels']) + '.\n']
out.append(r'\end{document}' + '\n')
target.write_text(''.join(out))
print(target)
