#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
status_anchor='source_half_grade_parent_carry: reference-super-amplified-passive-small-data-reuse-fails\n'
status_line='source_half_grade_six_mode_bridge: rank-four-quadratic-next-parent-map-local-reference-author\n'
assert p.count(status_anchor)==1 and 'source_half_grade_six_mode_bridge:' not in p
p=p.replace(status_anchor,status_anchor+status_line,1)

anchor='''This does not exclude the grade-changing route; it sharpens it to genuinely
**late** regeneration. A surviving construction must cancel/deplete the old
parents after use and regenerate the required half-grade/nonparent state near
the next pulse, or use a nonlinear stage in which the huge positive linear
action is balanced by transfer. The next active discriminator is therefore a
local late-generation calculation with nonparent half-grade ancestry, not
another passive interstage propagator. The nonprincipal localized full-history
adjoint remains the alternative. UE1 and the terminal claim remain open.
'''
addition='''

That local nonparent discriminator is favorable once the inherited state is
enlarged. Besides the four old half-grade keys `5,-4,2,-1`, the complete cubic
dynamics supplies both extreme keys `14` and `-13`; each extreme has a unique
cubic monomial and a nonzero growing coordinate, and both are linearly unstable
at normalized `z=1/2`. The six half-grade modes have four exact quadratic
next-parent edges

    14+(-4)->5,   -13+5->-4,
    5+(-1)->2,    -4+2->-1,

where the arrows divide the input key sum by two when returning to `z=1`.
Every full Leray growing projection is nonzero. Moreover, fixing nonzero shared
ancestors `x_5,x_-4`, the leading four-target Jacobian in
`(x_14,x_-13,x_-1,x_2)` has nonzero determinant. Thus the old two-hard/two-easy
order mismatch is not intrinsic to a six-coordinate grade-changing state; the
four next parents can all be generated quadratically with a rank-four leading
map. See `research/evidence/2026-09-12-half-grade-six-mode-bridge.md`.

The first unresolved object is now **finite-duration and causal realization of
this six-mode bridge**. One must show that the rank-four map survives the full
short-time infinite-lattice evolution and then supply the six half-grade
ancestors late from one physical history; freely prescribing them is not a
global solution. The next discriminator is finite-duration persistence of the
rank-four target map. The nonprincipal localized full-history adjoint remains
the alternative. UE1 and the terminal claim remain open.
'''
assert p.count(anchor)==1
p=p.replace(anchor,anchor+addition,1)
plan.write_text(p)

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert all(c['id']!='half-grade-six-mode-bridge' for c in controls['controls'])
obs={
    'half_grade_ancestors':'14,-13,5,-4,2,-1 all positive-branch growing',
    'cubic_extremes':'both +14 and -13 nonzero unique monomials',
    'next_parent_quadratic_edges':'all four nonzero',
    'leading_target_rank':4,
    'finite_duration_bridge':'open',
    'late_causal_six_mode_supply':False,
}
controls['controls'].append({
    'id':'half-grade-six-mode-bridge',
    'scope':'frozen local source-reference bridge from six z=1/2 ancestors to four next z=1 parents',
    'evidence':'research/evidence/2026-09-12-half-grade-six-mode-bridge.md',
    'rigor':'exact-algebra-spectral-author-proof',
    'observation':obs,
})
controls_path.write_text(json.dumps(controls,indent=2)+"\n")

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
marker="    'half-grade-parent-carry-wall': {'parent_reference_exponent_bracket': '>9/10', 'parent_carry_gain': 'exp(+c Q^(-h))', 'Qminus_h_over_L': 'diverges for L~ell^2', 'passive_small_data_parent_reuse': False, 'late_nonlinear_regeneration': 'open'},\n"
line="    'half-grade-six-mode-bridge': {'half_grade_ancestors': '14,-13,5,-4,2,-1 all positive-branch growing', 'cubic_extremes': 'both +14 and -13 nonzero unique monomials', 'next_parent_quadratic_edges': 'all four nonzero', 'leading_target_rank': 4, 'finite_duration_bridge': 'open', 'late_causal_six_mode_supply': False},\n"
assert b.count(marker)==1 and "'half-grade-six-mode-bridge'" not in b
b=b.replace(marker,marker+line,1)
baseline.write_text(b)

snapshot_path=root/'research/game/snapshot.json'
snap=json.loads(snapshot_path.read_text())
ev='research/evidence/2026-09-12-half-grade-six-mode-bridge.md'
assert ev not in snap['authoritative_sources']
def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],cwd=root,text=True).strip()
snap['authoritative_sources']['PLAN.md']=blob('PLAN.md')
snap['authoritative_sources'][ev]=blob(ev)
snap['active_frontier']='finite-duration rank-four six-mode half-grade bridge, then late causal supply of its six ancestors from one physical history; nonprincipal localized full-history adjoint remains alternative'
snapshot_path.write_text(json.dumps(snap,indent=2)+"\n")
print('integrated six-mode half-grade bridge')
