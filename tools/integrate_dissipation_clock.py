#!/usr/bin/env python3
"""Anchor-checked status integration. Never promotes an open mathematical claim."""
from pathlib import Path
import argparse
import re

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
args = parser.parse_args()

def save(path, old, new):
    if args.check:
        assert old == new, f'integration missing in {path}'
    else:
        path.write_text(new)

def append_once(relative, heading, body):
    path = root/relative
    old = path.read_text()
    new = old if heading in old else old+'\n\n'+heading+'\n\n'+body.rstrip()+'\n'
    save(path, old, new)

path = root/'PLAN.md'
old = path.read_text()
match = re.search(r'```yaml\s*\n(.*?)\n```', old, re.S)
assert match, 'missing live YAML'
block = match.group(1)
for key, value in {
    'paper_status': 'active-paper-proof-work-2026-09-06',
    'paper_repo': 'writable-authorized-2026-09-06',
    'active_task': 'arbitrary-data-producer-and-dissipation-clock-audit',
}.items():
    block, count = re.subn(r'^'+key+r': .*$', key+': '+value, block, flags=re.M)
    assert count == 1, f'changed live key: {key}'
new = old[:match.start(1)]+block+old[match.end(1):]
save(path, old, new)
append_once('PLAN.md', '## Current paper task: dissipation-clock suffix (2026-09-06)', '''
This dated entry and the live YAML supersede older read-only/signed-only
workflow paragraphs for this task. The user explicitly requested paper proof
work, main-document updates and commits/pushes in both private repositories,
including unsigned commits. Ongoing formalization stays authorized and its
phase fields are unchanged; this task does not claim Phase I or II completion.

The paper component `sections/dissipation_clock.tex` derives
`Y'+nu Z <= (4 S^3/(3 nu^2)) D3 Y`, hence a uniform cubic-dissipation budget
continues the original branch directly through the nonendpoint pair `(3,9)`.
Strict pressure absorption then gives exponent
`4 S^3 (X0+3A)/(9 (1-theta) nu^3)`. A single finite first-crossing barrier
also suffices; in particular a logarithmic deficit can replace a constant
fractional margin. The previous `(4,6)` suffix is not the shortest route.

These are full written derivations, author-checked and independently unaudited.
The graph records them as a separate pending supplement, NOT a promoted node.
The accepted graph and all open/terminal kinds stay unchanged. The bare
critical-norm continuation theorem still retains ESS; the strict-pressure
suffix does not. The old claim that ESS is unavoidable for every route to a
conditional theorem must not guide implementation of this alternative.

The actual mathematical target remains an arbitrary-data producer, uniform
to a putative endpoint. The absolute-pressure attempt only gives growth of
order `B^(3/2)` and does not establish the needed signed deficit. The finite
barrier's existential formulation is again equivalent to continuation, not
a new proof of it. Full details and audit questions are in
`research/evidence/2026-09-06-dissipation-clock.md`.

Next substantive gate: independently reconstruct the dissipation-clock
component, then derive a signed pressure estimate from the vector equation
rather than assuming a critical budget. Do not report main-document builds,
regression checks, or this new sufficient condition as closure of NS-R3.
''')
append_once('AGENTS.md', '## Current task authorization (2026-09-06)', '''
The owner explicitly requested paper-proof work, updates to main documents,
and commits/pushes in `navier` and `navier-paper`, including unsigned commits.
This supersedes read-only and signed-only instructions above for the present
task. Existing formalization remains separately authorized; no formal claim
is promoted here. Keep the repositories private, preserve concurrent edits,
refresh before non-force pushes, and distinguish complete derivations,
author checks, independent audits, and unproved estimates. Repository-specific
build automation is mechanical work, not a delegated mathematical reviewer.
''')
append_once('README.md', '## Current paper continuation (2026-09-06)', '''
`PLAN.md` now records the explicitly authorized writable paper workflow.
The manuscript includes a review-pending dissipation-clock component; see
`research/evidence/2026-09-06-dissipation-clock.md` for its exact scope.
It removes ESS from the strict-pressure suffix and admits finite/logarithmic
dissipation barriers, but supplies no arbitrary-data pressure producer.
Run `python3 research/verify.py` with the paper and formal repositories
present. `--research-only` is an explicitly narrower structural check.
''')
append_once('docs/proof.md', '## Dissipation-clock continuation component (2026-09-06; review pending)', '''
The main manuscript now includes `sections/dissipation_clock.tex`, with full
derivations of the direct estimates

```text
||u||_9^3 <= (9 S^2/8) D3,
Y'+nu Z <= (4 S^3/(3 nu^2)) D3 Y,
Y(t)+nu integral_0^t Z <= Y0 exp(4 S^3 B(t)/(3 nu^2)),
B(t)=integral_0^t D3.
```

Thus a finite B budget gives continuation without an endpoint theorem. Under
the existing strict signed pressure absorption, the bound is
`B <= (X0+3A)/(3(1-theta)nu)`. The resulting direct exponent is
`4 S^3 (X0+3A)/(9(1-theta)nu^3)`. This alternative suffix does not require
ESS or quotient-minimizer regularity. The separately stated bare-L3 endpoint
theorem retains its original dependency.

A single first-crossing pressure barrier also suffices. More generally,
`integral Q_J <= nu B-Phi(B)+A_high` prevents crossing any finite b with
`Phi(b)>X0/3+A_high+L_J(H)`. A logarithmic Phi is enough despite a vanishing
fractional absorption margin. The source proves the endpoint-uniform
first-crossing argument and a scalar boundary example, with their exact
scope. These sharpenings are author-checked and await independent audit;
the graph lists a separate pending supplement, not a promoted theorem.

The missing arbitrary-data pressure estimate is still missing. Absolute
pressure estimates produce only a B-to-the-three-halves upper bound. No
choice of Phi, existence of a certificate in the already-regular case, or
successful build provides a noncircular producer. See the dated evidence
note for the derivations, failed inference, and review questions.
''')
path = root/'docs/proof-graph.yaml'
old = path.read_text()
metadata = '''\ncandidate_supplements:
  - id: DISSIPATION-CLOCK
    title: Direct nonendpoint dissipation-clock continuation
    status: author-checked-independent-audit-pending
    source_repository: itpplasma/navier-paper
    source_commit: 7748a9816d0fd9003205684761c219a0b57d9c14
    source_path: sections/dissipation_clock.tex
    evidence: research/evidence/2026-09-06-dissipation-clock.md
    paper_labels: ['dc:l9', 'dc:clock', 'dc:strict', 'dc:barrier', 'dc:nonlinear', 'dc:scalar']
    scope: Full component derivations only; no arbitrary-data producer and no graph-node promotion.
'''
if 'candidate_supplements:' not in old:
    new = old.rstrip()+'\n'+metadata
elif 'id: DISSIPATION-CLOCK' in old:
    new = old
else:
    raise SystemExit('Concurrent candidate metadata exists; reconcile instead of overwriting')
save(path, old, new)
path = root/'tools/generate_map.py'
old = path.read_text()
marker = '# Review-pending supplements are not claim nodes.'
new = old
if marker not in old:
    anchor = "out.append(r'\\end{document}' + '\\n')"
    assert old.count(anchor) == 1, 'changed map-generator anchor'
    addition = "# Review-pending supplements are not claim nodes.\nfor candidate in graph.get('candidate_supplements', []):\n    out += [r'\\clearpage\\section*{Review-pending component: ' + esc(candidate['title']) + '}\\n',\n            r'\\textbf{Not a promoted claim or an arbitrary-data producer.}' + '\\n\\n',\n            esc(candidate['status']) + '. ' + esc(candidate['scope']) + '\\n\\n',\n            r'\\textbf{Evidence:} \\texttt{' + esc(candidate['evidence']) + '}.\\n\\n',\n            r'\\textbf{Manuscript labels:} ' + ', '.join(r'\\texttt{' + esc(x) + '}' for x in candidate['paper_labels']) + '.\\n']\n"
    compile(addition, 'candidate-map-addition', 'exec')
    new = old.replace(anchor, addition+anchor, 1)
new = new.replace('# The manuscript repository is read-only from 2026-09-06 (see AGENTS.md), so the\n# default output moved into this repository. Pass an explicit path to override.',
                  '# Keep the research output local by default. The current task authorizes\n# synchronizing the manuscript map by an explicit target path.')
save(path, old, new)
print('PASS: live plan, authorization, README, proof dossier, pending metadata and map generator integrated; no graph node promoted.')
