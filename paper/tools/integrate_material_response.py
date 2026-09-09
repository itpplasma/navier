#!/usr/bin/env python3
"""Guarded document integration; refresh Git before running, never force-push."""
from pathlib import Path
import argparse
import hashlib

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
changes = {}
assert hashlib.sha256((root/'sections/material_response.tex').read_bytes()).hexdigest() == '54eb89147a08ee4403d8278fbe844bf396fb2978962cf156a6c5e547f4b90034'

def read(path):
    return changes.get(path, (root/path).read_text())

def replace(path, old, new):
    text = read(path)
    if text.count(new) == 1:
        return
    assert text.count(old) == 1, 'missing/ambiguous or concurrent anchor: '+path
    changes[path] = text.replace(old, new, 1)

def append(path, marker, block):
    text = read(path)
    if marker in text:
        assert text.count(marker) == 1 and block in text, 'partial/concurrent integration: '+path
    else:
        changes[path] = text+block

replace('main.tex',
        'driver estimate is not closed and independent review is pending.\n',
        'driver estimate is not closed and independent review is pending.\n'+r'''Section~\ref{mr:section} proves a strong moving-metric response, including
velocity zeros, and a corotational material law with its nonlocal
commutator retained. Its diffusion--strain action still lacks an
endpoint-uniform bound; this component is also review pending.
''')
replace('main.tex',
        'new evolution drivers uniformly at the endpoint.\n',
        'new evolution drivers uniformly at the endpoint.\n'+r'''Section~\ref{mr:section} differentiates the cubic representative in its
fixed weighted space and the natural variable strongly in $L^2$, even at
zeros. Pullback by the actual flow isolates an exact diffusion--strain
action after removal of rigid rotation. This is not differentiation of
the full sharp speed projection, and it does not bound the action or
nonlocal commutator at the endpoint. Independent audit remains pending.
''')
replace('main.tex', '\\input{sections/shell_dynamics}\n',
        '\\input{sections/shell_dynamics}\n\\input{sections/material_response}\n')

make = read('Makefile')
lines = make.splitlines(keepends=True)
indices = [i for i, line in enumerate(lines) if line.startswith('main.pdf:')]
assert len(indices) == 1, 'ambiguous main build target'
i = indices[0]
if 'sections/material_response.tex' not in lines[i]:
    lines[i] = lines[i].rstrip()+' sections/material_response.tex\n'
    changes['Makefile'] = ''.join(lines)
append('Makefile', '\ncheck-material:\n', '''
.PHONY: check-material
check-material:
\tpython3 tools/check_material_response.py --integrated
''')
append('references.bib', '@article{ConstantinIyer2008,', '''
@article{ConstantinIyer2008,
  author = {Constantin, Peter and Iyer, Gautam},
  title = {A stochastic {Lagrangian} representation of the three-dimensional
           incompressible {Navier--Stokes} equations},
  journal = {Communications on Pure and Applied Mathematics},
  volume = {61},
  number = {3},
  pages = {330--345},
  year = {2008},
  doi = {10.1002/cpa.20192},
  eprint = {math/0511067},
  archivePrefix = {arXiv},
  note = {One-form transport background only; no stochastic theorem is used}
}
''')
append('README.md', '## Strong corotational material response (2026-09-06)', '''
## Strong corotational material response (2026-09-06)

`sections/material_response.tex` proves a moving-metric response for the
cubic minimizer and a strong natural-variable derivative in L2, including
velocity zeros. Pullback by the actual flow gives an exact corotational
material law. Its diffusion-strain responses are orthogonal in the fixed
weighted space, with `action <= ||U||2^2 <= 9 action/8`. The finite
shell-residual equation retains the complete nonlocal Riesz/rotation
commutator rather than discarding it as transport.

These component proofs are author-checked and await independent audit.
The weighted acceleration and strain action are locally finite, not
bounded from arbitrary data uniformly at the endpoint. The original
critical estimate remains unproved; no graph gap or predecessor audit is
promoted. `make check-material` tests source integrity, exact constants,
projection/covariance algebra and six nonlinear finite-atom response probes
including a zero atom; it is not an analytic proof or an independent audit.
''')

# Copy only the exact generated-map change. A concurrent graph/map change
# requires regeneration from the research authority, not an overwrite.
path = 'proof_map.tex'
text = read(path)
digest = hashlib.sha256(text.encode()).hexdigest()
base = 'f9dff6f235a85db74f0fab2b5d0e294bfc1835fdb3eaa6671d92484cf7cb96fa'
target = '9376cf076167cad82acf8ce79218d48101c6856e3ee8528157c3c9910fba3db7'
if digest != target:
    assert digest == base, 'concurrent map edit; regenerate from research graph'
    old = r'Graph SHA-256: \texttt{c098f2a4d744c075a4352ecae6bf55a9}\texttt{927dd81ebc70294ef27612fe9a6e0f7e}.'
    new = r'Graph SHA-256: \texttt{4f036f34b4c4a2e44e41795a414830d3}\texttt{c1764fd5556d1825b7dfe63b3deaab11}.'
    assert text.count(old) == 1
    text = text.replace(old, new, 1)
    block = r'''\clearpage\section*{Review-pending component: Strong natural response and corotational material action}
\textbf{Not a promoted claim or an arbitrary-data producer.}

author-checked-independent-audit-pending. Strong moving-metric and zero-set natural differentiation, exact orthogonal diffusion-strain action and full material residual commutator; endpoint action control and uniform refinement remain unproved, no arbitrary-data critical bound or node promotion.

\textbf{Evidence:} \texttt{research/evidence/2026-09-06-material-response.md}.

\textbf{Manuscript labels:} \texttt{mr:response}, \texttt{mr:hadamard}, \texttt{mr:material}, \texttt{mr:residual}, \texttt{mr:balance}, \texttt{mr:rigid}.
'''
    assert text.count('\\end{document}\n') == 1
    text = text.replace('\\end{document}\n', block+'\\end{document}\n', 1)
    assert hashlib.sha256(text.encode()).hexdigest() == target, 'generated map digest mismatch'
    changes[path] = text

if args.check:
    assert not changes, 'pending integration: '+', '.join(changes)
else:
    for path, text in changes.items():
        (root/path).write_text(text)
print('PASS: guarded corotational material manuscript integration; endpoint gap retained.')
print('Scope: document/source integrity, not mathematical audit or a new regularity claim.')
