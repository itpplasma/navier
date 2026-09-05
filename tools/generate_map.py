#!/usr/bin/env python3
"""Generate the standalone clickable supplement from the authoritative graph."""
from pathlib import Path
import hashlib
import yaml

root = Path(__file__).resolve().parents[1]
source = root / 'docs/proof-graph.yaml'
graph = yaml.safe_load(source.read_text())
digest = hashlib.sha256(source.read_bytes()).hexdigest()
target = root.parent / 'navier-paper/proof_map.tex'

def esc(s):
    table = {'&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#',
             '{': r'\{', '}': r'\}', '$': r'\$', '^': r'\textasciicircum{}'}
    return ''.join(table.get(c, c) for c in s)

pos = {'LOCAL': (0,0), 'PRESSURE': (6,0),
       'ENERGY': (0,-3), 'LOW-PRESSURE': (6,-3), 'HIGH-PRESSURE': (12,-3),
       'SCALE': (0,-6), 'ABSORPTION': (6,-6),
       'ENSTROPHY': (0,-9), 'CRITICAL': (6,-9), 'ESS': (12,-9),
       'CONDITIONAL': (6,-12), 'NS-R3': (6,-15), 'ODE': (12,-15)}
tags = {'imported': 'IMPORTED', 'paper': 'PAPER', 'gap': 'GAP',
        'conditional': 'PAPER / CONDITIONAL'}
edge_labels = {
 ('LOCAL','ENERGY'): 'energy balance', ('LOCAL','PRESSURE'): 'cubic test',
 ('ENERGY','SCALE'): 'interpolate', ('LOCAL','ENSTROPHY'): 'curl equation',
 ('PRESSURE','CRITICAL'): 'integrated balance',
 ('ABSORPTION','CRITICAL'): 'unproved estimate',
 ('LOCAL','CONDITIONAL'): 'maximal lifespan',
 ('ENERGY','CONDITIONAL'): 'finite energy',
 ('CRITICAL','CONDITIONAL'): 'critical bound',
 ('ESS','CONDITIONAL'): 'continuation',
 ('CONDITIONAL','NS-R3'): 'conditional conclusion',
 ('CRITICAL','NS-R3'): 'gap must close',
 ('ENERGY','LOW-PRESSURE'): 'kernel and energy',
 ('LOW-PRESSURE','ABSORPTION'): 'bounded remainder',
 ('HIGH-PRESSURE','ABSORPTION'): 'unproved high tail'}
out = [r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=10mm]{geometry}
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

\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth,
box/.style={draw,rounded corners=2pt,text width=3.9cm,minimum height=1.1cm,align=center,font=\small},
imported/.style={box,fill=blue!8},paper/.style={box,fill=black!3},
conditional/.style={box,fill=black!3,double},gap/.style={box,dashed,thick,fill=orange!10},
edge/.style={->,thin},lab/.style={font=\scriptsize,fill=white,inner sep=2pt}]
''']
for n in graph['nodes']:
    x,y = pos[n['id']]
    out.append(r'\node[' + n['kind'] + '] ('+n['id']+') at ('+str(x)+','+str(y)+') {'
               +r'\hyperref[node:'+n['id']+']{'+esc(n['title'])+r'}\\{\scriptsize '
               + tags[n['kind']] + '}};\n')
for n in graph['nodes']:
    for dep in n['depends_on']:
        key = (dep,n['id'])
        label = edge_labels[key]
        if key == ('LOCAL','ENSTROPHY'):
            out.append(r'\draw[edge] (LOCAL.west) -- ++(-1,0) |- node[lab,pos=.72,rotate=90]{curl equation} (ENSTROPHY.west);'+'\n')
        elif key == ('PRESSURE','CRITICAL'):
            out.append(r'\draw[edge] (PRESSURE.east) -- (9.5,0) -- (9.5,-8) -- (CRITICAL.north east);\node[lab,left,text width=1.3cm] at (9.5,-1.3) {cubic balance};'+'\n')
        elif key == ('ENERGY','CONDITIONAL'):
            out.append(r'\draw[edge] (ENERGY.south east) -- (3,-4) -- node[lab,sloped,above]{finite energy} (3,-11) -- (CONDITIONAL.west);'+'\n')
        elif key == ('CRITICAL','NS-R3'):
            out.append(r'\draw[edge,dashed] (CRITICAL.east) -- ++(1.2,0) |- (NS-R3.east);\node[lab,text width=1.2cm,align=left] at (8.6,-13.7) {gap must close};'+'\n')
        elif pos[dep][0] == pos[n['id']][0]:
            out.append(r'\draw[edge] ('+dep+') -- node[lab,right,text width=1.4cm,align=left]{'+label+'} ('+n['id']+');\n')
        else:
            out.append(r'\draw[edge] ('+dep+') -- node[lab,sloped,above]{'+label+'} ('+n['id']+');\n')
out += [r'''\end{tikzpicture}

Phase I: not started; awaiting the user. Phase II: not started.
No terminal proof or counterexample is claimed.
\end{center}
\clearpage
\raggedright
''', 'Graph SHA-256: '+r'\texttt{'+digest[:32]+'}'+r'\texttt{'+digest[32:]+'}.\n']
for n in graph['nodes']:
    out += [r'\Needspace{10\baselineskip}\section*{'+esc(n['id']+': '+n['title'])+'}'+r'\phantomsection\label{node:'+n['id']+'}\n',
            r'\textbf{Class:} '+tags[n['kind']]+r'. \textbf{Phase I/II:} not started.'+'\n\n',
            esc(n['statement'])+'\n\n',
            r'\textbf{Mechanism:} '+esc(n['mechanism'])+'.\n\n',
            r'\textbf{Review:} '+esc(n['review'])+'\n\n',
            r'\textbf{Evidence:} \texttt{'+esc(n['evidence'])+'}. '
            +r'Manuscript label: \texttt{'+esc(n['paper_label'])+'}.\n\n',
            r'\textbf{Dependencies:} '+(', '.join(r'\hyperref[node:'+d+']{'+esc(d)+'}' for d in n['depends_on']) or 'none')+'. '
            +r'\hyperref[map]{Back to map}.'+'\n\n']
out.append(r'\end{document}'+'\n')
target.write_text(''.join(out))
print(target)
