#!/usr/bin/env python3
"""Idempotent guarded document integration, not a mathematical audit."""
from pathlib import Path
import argparse
import hashlib
import json
import yaml

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--check',action='store_true')
args=p.parse_args()
root=Path(__file__).resolve().parents[1]
assert (root/'research/evidence/2026-09-06-shell-dynamics.md').is_file()
append=json.loads(r'''{
  "PLAN.md": "\n\n## Natural-variable dynamics checkpoint (2026-09-06; audit pending)\n\nFrozen paper source: `a9993cccee0f9544c49f9c98524c6c4af4c0e080`,\n`sections/shell_dynamics.tex`; evidence:\n`research/evidence/2026-09-06-shell-dynamics.md`. This is an author-checked\ncomponent derivation, not an independent audit or an arbitrary-data bound.\n\nFor every gradient increment g the natural variable V=|w|^(1/2)w obeys\n`||V1-V0||2^2 <= (9/8) integral (|w0|+|w1|)|f1-f0+g|^2`.\nConsequently V is W^(1,infinity) into L2 on each compact classical interval,\nwith pressure-free bound\n`||V_t||2^2 <= (9/4) integral |w| |nu Delta u-(u dot grad)u|^2`.\nFinite smooth speed features and a positive ridge penalty then have an\nexact absolutely continuous residual evolution, in L3--L^(3/2) and L2\npairings. This justifies a regularized temporal calculation that the\nprevious checkpoint could not assume. It does not differentiate the full\nmoving projection. The source proves the fixed-regularization estimates\nand the pointwise-in-time monotone approximation separately.\n\n**Next positive producer:** control the explicit residual-evolution drivers\nuniformly below min(H,Tstar) and control the losses in feature refinement\nand vanishing ridge penalty, or find a different signed time estimate.\nThe weighted acceleration bound contains an uncontrolled nonlinear and\nsecond-derivative term; the current energy budget does not close it.\nNo input-only bound on L_c or the fourth-power defect integral is supplied.\nIndependent audits of this and the predecessor components remain required.\nAll 29 existing graph nodes and formal statuses are unchanged; HIGH-PRESSURE,\nHIGH-STRAIN, DEFECT-L4 and NS-R3 remain open. This checkpoint replaces the\nactive task, not the historical record of prior unsuccessful approaches.\n",
  "README.md": "\n\n## Regularized shell dynamics (2026-09-06; independent audit pending)\n\nThe new paper component proves natural-variable L2 time regularity, a\npressure-free weighted acceleration bound, and the exact evolution of\nfinite smooth speed-shell residuals with a positive ridge penalty.\n`research/evidence/2026-09-06-shell-dynamics.md` records the proof and its\nboundary: endpoint control of the evolution drivers and uniformity under\nrefinement remain unproved. `PLAN.md` is the sole live status. No open or\nformal claim is promoted.\n",
  "docs/proof.md": "\n\n## Natural-variable time regularity and regularized shell dynamics\n\nThe pending component `sections/shell_dynamics.tex` proves\n\n    ||V1-V0||2^2 <= (9/8) integral (|w0|+|w1|)|f1-f0+g|^2\n\nfor every admissible gradient g. Thus on compact classical intervals\nV=|w|^(1/2)w is W^(1,infinity) into L2, and choosing the time-integrated\npressure gradient gives\n\n    ||V_t||2^2 <= (9/4) integral |w| |nu Delta u-(u dot grad)u|^2.\n\nFor finite smooth features phij=gj(|w|), Gram matrix G, moment vector b,\nand eta>0, the residual\n`R=||chi||2^2-b^T(G+eta I)^(-1)b` is absolutely continuous and retains\n`|K|<=||sigma||2 sqrt(R)`. With `a=(G+eta I)^(-1)b` and\n`r=chi-sum aj phij`, its exact evolution is\n\n    R'=2<r,chi_t>-2<r,sum aj phij,t>.\n\nThe source supplies the dual-space justifications and a full bound for\nthis derivative. It unblocks a finite regularized temporal calculation,\nnot differentiation of the sharp moving projection. Refining features and\nletting eta decrease gives the exact shell residual at each fixed time,\nbut the derivative estimates are not uniform in that limit or at Tstar.\nThe missing arbitrary-data estimate on L_c or integral ||sigma||2^4 is\ntherefore unchanged. See `research/evidence/2026-09-06-shell-dynamics.md`.\nThese are author-checked derivations awaiting independent audit; no existing\ngraph node or formal claim is promoted.\n",
  "docs/proof-graph.yaml": "  - id: REGULARIZED-SHELL-DYNAMICS\n    title: Natural-variable time regularity and shell dynamics\n    status: author-checked-independent-audit-pending\n    source_repository: itpplasma/navier-paper\n    source_commit: a9993cccee0f9544c49f9c98524c6c4af4c0e080\n    source_path: sections/shell_dynamics.tex\n    source_sha256: 66f3ff185f220e8be874ea2090bc982abe42b4208ee093dc6799b5ee015e5677\n    evidence: research/evidence/2026-09-06-shell-dynamics.md\n    paper_labels: ['st:stability', 'st:time', 'st:residual', 'st:evolution']\n    scope: Natural-distance stability, pressure-free local time regularity and exact finite regularized shell-residual evolution; endpoint driver control and uniform refinement remain unproved, with no arbitrary-data critical estimate or node promotion.\n"
}''')
changes={}
for name, addition in append.items():
    path=root/name
    original=path.read_text()
    text=original
    if name=='PLAN.md':
        old='active_task: speed-shell-temporal-producer-and-independent-component-audit'
        new='active_task: regularized-shell-dynamics-endpoint-driver-and-independent-audit'
        if new not in text:
            assert text.count(old)==1, 'concurrent active task changed; reconcile explicitly'
            text=text.replace(old,new,1)
    marker=next(line for line in addition.splitlines() if line.strip())
    if addition not in text:
        assert marker not in text, f'partial or concurrent integration in {name}'
        text+=addition
    if name=='docs/proof-graph.yaml':
        before,after=yaml.safe_load(original),yaml.safe_load(text)
        assert before['nodes']==after['nodes'], 'existing claim nodes changed'
        assert next(n for n in after['nodes'] if n['id']=='NS-R3')['kind']=='gap'
    if text!=original:
        changes[path]=text
if args.check:
    assert not changes, 'pending integration: '+', '.join(str(p.relative_to(root)) for p in changes)
else:
    for path,text in changes.items():
        path.write_text(text)
print('PASS: regularized shell dynamics integration '+('applied' if changes else 'present'))
print('Scope: document integrity only; endpoint bound and independent audit remain open.')
