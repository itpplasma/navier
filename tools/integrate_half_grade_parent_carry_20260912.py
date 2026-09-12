#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
status_anchor='source_adjoint_principal_stress_dual: high-frequency-solenoidal-force-has-order-one-over-k-symmetric-stress-potential\n'
status_line='source_half_grade_parent_carry: reference-super-amplified-passive-small-data-reuse-fails\n'
assert p.count(status_anchor)==1
assert 'source_half_grade_parent_carry:' not in p
p=p.replace(status_anchor,status_anchor+status_line,1)

anchor='''This is a second serious return to simple complete-adjoint mechanisms: sign
control fails structurally and the principal carrier is strain-dual cheap. Per
the diversification rule the next primary attack switches to the constructive
**grade-changing/nonparent late-regeneration** route. The complete adjoint stays
available only through nonprincipal localized whole-history structure. UE1 and
the terminal claim remain open.
'''
addition='''

The first grade-changing discriminator closes passive reuse of the old parents.
During the same factor-two scale contraction, an old physical parent moves from
normalized `z=1` to `z=1/2`. In the continuously self-similar reference its
integrated positive-branch exponent is

    Q^(-h)/h [3a-2b log 2],
    a=(1+s^2)^(-1/2),    b=(3/5)(1+s^2).

For all four caged parent tilts `|s|<=1/2`, the bracket is strictly larger than
`9/10`. Thus passive carry amplifies every old parent by `exp(+c Q^(-h))`, while
`Q^(-h)/L -> infinity` for `L~ell^2`. Any quasi-Gaussian small parent trace used
at one stage therefore cannot simply be reused as a small half-grade ancestor at
the next stage. See
`research/evidence/2026-09-12-half-grade-parent-carry-wall.md`.

This does not exclude the grade-changing route; it sharpens it to genuinely
**late** regeneration. A surviving construction must cancel/deplete the old
parents after use and regenerate the required half-grade/nonparent state near
the next pulse, or use a nonlinear stage in which the huge positive linear
action is balanced by transfer. The next active discriminator is therefore a
local late-generation calculation with nonparent half-grade ancestry, not
another passive interstage propagator. The nonprincipal localized full-history
adjoint remains the alternative. UE1 and the terminal claim remain open.
'''
assert p.count(anchor)==1
p=p.replace(anchor,anchor+addition,1)
plan.write_text(p)

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert all(c['id']!='half-grade-parent-carry-wall' for c in controls['controls'])
obs={
    'parent_reference_exponent_bracket': '>9/10',
    'parent_carry_gain': 'exp(+c Q^(-h))',
    'Qminus_h_over_L': 'diverges for L~ell^2',
    'passive_small_data_parent_reuse': False,
    'late_nonlinear_regeneration': 'open',
}
controls['controls'].append({
    'id':'half-grade-parent-carry-wall',
    'scope':'continuously self-similar carry of the four old z=1 parents to inherited z=1/2 modes',
    'evidence':'research/evidence/2026-09-12-half-grade-parent-carry-wall.md',
    'rigor':'exact-reference-exponent-author-proof',
    'observation':obs,
})
controls_path.write_text(json.dumps(controls,indent=2)+"\n")

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
marker="    'adjoint-principal-stress-dual': {'symmetric_inverse_divergence': 'Ghat=-i(k⊗f+f⊗k)/|k|^2', 'stress_norm': 'sqrt(2)|f|/|k|', 'pairs_with_symmetric_strain': True, 'principal_high_frequency_adjoint_obstruction': False},\n"
line="    'half-grade-parent-carry-wall': {'parent_reference_exponent_bracket': '>9/10', 'parent_carry_gain': 'exp(+c Q^(-h))', 'Qminus_h_over_L': 'diverges for L~ell^2', 'passive_small_data_parent_reuse': False, 'late_nonlinear_regeneration': 'open'},\n"
assert b.count(marker)==1 and "'half-grade-parent-carry-wall'" not in b
b=b.replace(marker,marker+line,1)
baseline.write_text(b)

snapshot_path=root/'research/game/snapshot.json'
snap=json.loads(snapshot_path.read_text())
ev='research/evidence/2026-09-12-half-grade-parent-carry-wall.md'
assert ev not in snap['authoritative_sources']
def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],cwd=root,text=True).strip()
snap['authoritative_sources']['PLAN.md']=blob('PLAN.md')
snap['authoritative_sources'][ev]=blob(ev)
snap['active_frontier']='genuinely late grade-changing/nonparent regeneration after passive half-grade parent reuse fails; nonprincipal localized full-history adjoint remains alternative'
snapshot_path.write_text(json.dumps(snap,indent=2)+"\n")

print('integrated half-grade parent carry wall')
