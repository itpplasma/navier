#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
status_anchor='source_half_grade_six_mode_bridge: rank-four-quadratic-next-parent-map-local-reference-author\n'
status_line='source_half_grade_finite_time_bridge: full-infinite-lattice-fixed-horizon-rank-four-retuning-author\n'
assert p.count(status_anchor)==1 and 'source_half_grade_finite_time_bridge:' not in p
p=p.replace(status_anchor,status_anchor+status_line,1)

anchor='''The first unresolved object is now **finite-duration and causal realization of
this six-mode bridge**. One must show that the rank-four map survives the full
short-time infinite-lattice evolution and then supply the six half-grade
ancestors late from one physical history; freely prescribing them is not a
global solution. The next discriminator is finite-duration persistence of the
rank-four target map. The nonprincipal localized full-history adjoint remains
the alternative. UE1 and the terminal claim remain open.
'''
addition='''

The finite-duration part is favorable in the complete frozen reference lattice.
For every fixed `T>0`, each next parent has exactly one nonzero positive
half-grade cross pair; its only other positive decomposition is a self pair and
vanishes identically by incompressibility. The four exact growth mismatches
`D_K=lambda_a+lambda_b-lambda_K` are strictly positive, so every causal factor
`(exp(D_K T)-1)/D_K` is nonzero. Hence the quadratic target map keeps rank four
for every fixed positive horizon. Real-analytic dependence of the full
semilinear parabolic flow on the six initial amplitudes then lets the ordinary
real implicit-function theorem retune four complex ancestor amplitudes so that
the **exact nonlinear infinite-lattice endpoint** realizes a prescribed nearby
`epsilon^2` four-parent target quartet, with every generated sideband retained.
See `research/evidence/2026-09-12-half-grade-finite-time-bridge.md`.

This is the second serious checkpoint on the same local six-mode mechanism, so
local bridge refinement stops here. The first unresolved dependency has moved
backward to **causal late supply of the six half-grade ancestors from one
physical history**. Passive reuse of the old four is already excluded by
super-amplification. The next primary mechanism must therefore deplete/cancel
old parents and regenerate the six-mode state late, or use a genuinely
different parametric interaction with the actual source background. The
nonprincipal localized full-history adjoint remains the alternative. UE1 and
the terminal claim remain open.
'''
assert p.count(anchor)==1
p=p.replace(anchor,anchor+addition,1)
plan.write_text(p)

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert all(c['id']!='half-grade-finite-time-bridge' for c in controls['controls'])
obs={
    'quadratic_competitors':'only self pairs, identically zero',
    'four_growth_mismatches':'strictly positive',
    'finite_time_target_rank':4,
    'full_infinite_lattice_retuning':True,
    'late_causal_six_mode_supply':False,
    'physical_finite_L_lift':False,
}
controls['controls'].append({
    'id':'half-grade-finite-time-bridge',
    'scope':'complete frozen source-reference infinite lattice on every fixed positive horizon near zero data',
    'evidence':'research/evidence/2026-09-12-half-grade-finite-time-bridge.md',
    'rigor':'analytic-exact-author-proof',
    'observation':obs,
})
controls_path.write_text(json.dumps(controls,indent=2)+"\n")

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
marker="    'half-grade-six-mode-bridge': {'half_grade_ancestors': '14,-13,5,-4,2,-1 all positive-branch growing', 'cubic_extremes': 'both +14 and -13 nonzero unique monomials', 'next_parent_quadratic_edges': 'all four nonzero', 'leading_target_rank': 4, 'finite_duration_bridge': 'open', 'late_causal_six_mode_supply': False},\n"
line="    'half-grade-finite-time-bridge': {'quadratic_competitors': 'only self pairs, identically zero', 'four_growth_mismatches': 'strictly positive', 'finite_time_target_rank': 4, 'full_infinite_lattice_retuning': True, 'late_causal_six_mode_supply': False, 'physical_finite_L_lift': False},\n"
assert b.count(marker)==1 and "'half-grade-finite-time-bridge'" not in b
b=b.replace(marker,marker+line,1)
baseline.write_text(b)

snapshot_path=root/'research/game/snapshot.json'
snap=json.loads(snapshot_path.read_text())
ev='research/evidence/2026-09-12-half-grade-finite-time-bridge.md'
assert ev not in snap['authoritative_sources']
def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],cwd=root,text=True).strip()
snap['authoritative_sources']['PLAN.md']=blob('PLAN.md')
snap['authoritative_sources'][ev]=blob(ev)
snap['active_frontier']='causal late supply of six half-grade ancestors from one physical history via depletion/regeneration or a distinct source-background parametric mechanism; nonprincipal localized full-history adjoint remains alternative'
snapshot_path.write_text(json.dumps(snap,indent=2)+"\n")
print('integrated finite-time six-mode bridge')
