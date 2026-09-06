#!/usr/bin/env python3
"""Idempotent, guarded research integration; does not promote proof claims."""
from pathlib import Path
import argparse
import yaml

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
changes = {}

def read(path):
    return changes.get(path, (root/path).read_text())

def append(path, marker, block):
    text = read(path)
    if marker in text:
        assert text.count(marker) == 1 and block in text, 'partial/concurrent integration: '+path
    else:
        changes[path] = text.rstrip()+'\n\n'+block

old = 'active_task: regularized-shell-dynamics-endpoint-driver-and-independent-audit'
new = 'active_task: corotational-material-action-and-independent-audit'
plan = read('PLAN.md')
if new not in plan:
    assert plan.count(old) == 1, 'concurrent active-task change; reconcile explicitly'
    changes['PLAN.md'] = plan.replace(old, new, 1)

summary = '''The new source `sections/material_response.tex` in `navier-paper`, frozen at
`2959003806907fa4742518bff741f24c592921e6`, proves a strong moving-metric
response for the cubic gradient minimizer. A cubic little-o remainder, not
just the earlier big-O estimate, justifies the natural-variable derivative
in L2 including velocity zeros. No unweighted L3 derivative of w is assumed.

Pullback by the actual volume-preserving flow gives, with N=DJ(w),
P the fixed weighted gradient projection, L=I-P and S the velocity strain,

    U=(partial_t+u dot grad)V-Omega V
      =N[L(nu Delta u-Sw)+P(I-n tensor n/2)Sw].

The two weighted responses are orthogonal and their squared action obeys
`action <= ||U||2^2 <= 9 action/8`. Its explicit upper bound is
`(9/2)nu^2 integral rho|Delta u|^2 +(81/16) integral rho^3 ||S||op^2`.
This removes pressure, bulk transport and rigid rotation from the driver,
not strain or diffusion. The material finite-ridge residual equation keeps
the complete Riesz/rotation commutator and its correct dual-space pairing.
The accepted quotient balance is recovered exactly as a consistency check.

The endpoint bound is still unproved. Weighted acceleration, strain action,
the full commutator and uniform refinement losses are not controlled by
the available energy/moment budgets. Differentiating dissipation did not
establish the signed estimate needed to pay for this action. No heat
convexity or differentiation of a moving weighted projection is assumed.
See `research/evidence/2026-09-06-material-response.md` for the complete
source trail, attempted closure, author checks and independent-audit list.
This and predecessor supplements remain independently unaudited. No main
graph node or formal status is promoted; NS-R3, HIGH-PRESSURE, HIGH-STRAIN
and DEFECT-L4 remain open.
'''
append('PLAN.md', '## Corotational material checkpoint (2026-09-06)',
       '## Corotational material checkpoint (2026-09-06)\n\n'+summary+'''
Next positive producer: exploit the exact combined action or derive a
signed temporal estimate for the complete residual on actual trajectories.
Do not replace it by independent absolute estimates without checking the
lost cancellation. Independently audit the component before any promotion.
The new active task replaces the last driver target, not historical work.
''')
append('docs/proof.md', '## Strong material response (2026-09-06; audit pending)',
       '## Strong material response (2026-09-06; audit pending)\n\n'+summary)
append('README.md', '## Corotational material response (2026-09-06)',
       '''## Corotational material response (2026-09-06)

The paper now contains a full moving-metric response proof, including the
zero-set natural derivative, and an exact material law after removal of
rigid rotation. It isolates an orthogonal diffusion-strain action and
retains the nonlocal commutator in the finite shell-residual evolution.
These are author-checked component results, not an endpoint estimate;
independent audit remains pending. The next task is in `PLAN.md` and the
source/verification boundary is in
`research/evidence/2026-09-06-material-response.md`. All existing main claim
kinds and formal authorizations are preserved, including the open NS-R3,
HIGH-PRESSURE, HIGH-STRAIN and DEFECT-L4 nodes.
''')

candidate = '''  - id: COROTATIONAL-MATERIAL-RESPONSE
    title: Strong natural response and corotational material action
    status: author-checked-independent-audit-pending
    source_repository: itpplasma/navier-paper
    source_commit: 2959003806907fa4742518bff741f24c592921e6
    source_path: sections/material_response.tex
    source_sha256: 54eb89147a08ee4403d8278fbe844bf396fb2978962cf156a6c5e547f4b90034
    evidence: research/evidence/2026-09-06-material-response.md
    paper_labels: ['mr:response', 'mr:hadamard', 'mr:material', 'mr:residual', 'mr:balance', 'mr:rigid']
    scope: Strong moving-metric and zero-set natural differentiation, exact orthogonal diffusion-strain action and full material residual commutator; endpoint action control and uniform refinement remain unproved, no arbitrary-data critical bound or node promotion.
'''
path = 'docs/proof-graph.yaml'
original = read(path)
before = yaml.safe_load(original)
assert 'candidate_supplements' in before
if '  - id: COROTATIONAL-MATERIAL-RESPONSE\n' not in original:
    changes[path] = original.rstrip()+'\n'+candidate
else:
    assert candidate in original, 'partial/concurrent candidate integration'
after = yaml.safe_load(read(path))
assert before['nodes'] == after['nodes'], 'main graph promotion forbidden'
assert len({c['id'] for c in after['candidate_supplements']}) == len(after['candidate_supplements'])
assert next(n for n in after['nodes'] if n['id']=='NS-R3')['kind'] == 'gap'

if args.check:
    assert not changes, 'pending integration: '+', '.join(changes)
else:
    for relative, content in changes.items():
        (root/relative).write_text(content)
print('PASS: guarded corotational material research integration; no main node promotion.')
print('Scope: source/status integrity only, not mathematical audit or endpoint control.')
