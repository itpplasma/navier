#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
status_anchor='source_half_grade_finite_time_bridge: full-infinite-lattice-fixed-horizon-rank-four-retuning-author\n'
status_line='source_pump_half_grade_parity: even-source-cannot-zero-seed-odd-half-grade-sector\n'
assert p.count(status_anchor)==1 and 'source_pump_half_grade_parity:' not in p
p=p.replace(status_anchor,status_anchor+status_line,1)

anchor='''This is the second serious checkpoint on the same local six-mode mechanism, so
local bridge refinement stops here. The first unresolved dependency has moved
backward to **causal late supply of the six half-grade ancestors from one
physical history**. Passive reuse of the old four is already excluded by
super-amplification. The next primary mechanism must therefore deplete/cancel
old parents and regenerate the six-mode state late, or use a genuinely
different parametric interaction with the actual source background. The
nonprincipal localized full-history adjoint remains the alternative. UE1 and
the terminal claim remain open.
'''
addition='''

The first actual-source pump test gives an exact parity obstruction. Measure
physical phase in units of the half-grade ancestor integer `m`. The local source
mean/background has grade zero and the previous pure daughter pump has grade
`2m`; all source harmonics and residuals are therefore even. The complete
correction equation preserves phase parity, so an initially zero odd sector can
never create the required grade-`m` half-grade ancestors. The previous daughter
pump does have nonzero Leray transfer in exactly three complementary pairs

    (14,-13),   (5,-4),   (2,-1),

but in each two-mode block the directional growing coefficients have opposite
signs and hence negative off-diagonal product. The pump transfers a pre-existing
odd seed; it does not manufacture the first one. See
`research/evidence/2026-09-12-source-pump-half-grade-parity.md`.

The surviving nonlinear repair is now sharper. A seed in the inner pair can
produce its complement through the pump; that pair creates a grade-zero radial
difference shear of key `3`, and shear feedback can shift half-grade keys by
three. The next discriminator is the complete **one-odd-seed shear ladder**:
determine the minimum seed degree of the four next parents after all pump and
quadratic paths are admitted, rather than assuming the prescribed-shear theorem
can simply be spliced in. The nonprincipal localized full-history adjoint
remains the alternative. UE1 and the terminal claim remain open.
'''
assert p.count(anchor)==1
p=p.replace(anchor,anchor+addition,1)
plan.write_text(p)

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert all(c['id']!='source-pump-half-grade-parity' for c in controls['controls'])
obs={
    'source_background_phase_parity':'even in half-grade m units',
    'zero_odd_sector_invariant':True,
    'pump_complement_pairs':'(14,-13),(5,-4),(2,-1)',
    'all_directional_pump_coefficients_nonzero':True,
    'pair_offdiagonal_products':'strictly negative',
    'zero_seed_parametric_half_grade_generation':False,
    'nonlinear_cross_pair_seed_spread':'open',
}
controls['controls'].append({
    'id':'source-pump-half-grade-parity',
    'scope':'actual physical phase parity plus frozen local previous-daughter pump acting on the six half-grade ancestors',
    'evidence':'research/evidence/2026-09-12-source-pump-half-grade-parity.md',
    'rigor':'exact-physical-grading-symbol-author-proof',
    'observation':obs,
})
controls_path.write_text(json.dumps(controls,indent=2)+"\n")

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
marker="    'half-grade-finite-time-bridge': {'quadratic_competitors': 'only self pairs, identically zero', 'four_growth_mismatches': 'strictly positive', 'finite_time_target_rank': 4, 'full_infinite_lattice_retuning': True, 'late_causal_six_mode_supply': False, 'physical_finite_L_lift': False},\n"
line="    'source-pump-half-grade-parity': {'source_background_phase_parity': 'even in half-grade m units', 'zero_odd_sector_invariant': True, 'pump_complement_pairs': '(14,-13),(5,-4),(2,-1)', 'all_directional_pump_coefficients_nonzero': True, 'pair_offdiagonal_products': 'strictly negative', 'zero_seed_parametric_half_grade_generation': False, 'nonlinear_cross_pair_seed_spread': 'open'},\n"
assert b.count(marker)==1 and "'source-pump-half-grade-parity'" not in b
b=b.replace(marker,marker+line,1)
baseline.write_text(b)

snapshot_path=root/'research/game/snapshot.json'
snap=json.loads(snapshot_path.read_text())
ev='research/evidence/2026-09-12-source-pump-half-grade-parity.md'
assert ev not in snap['authoritative_sources']
def blob(path): return subprocess.check_output(['git','hash-object',str(path)],cwd=root,text=True).strip()
snap['authoritative_sources']['PLAN.md']=blob('PLAN.md')
snap['authoritative_sources'][ev]=blob(ev)
snap['active_frontier']='complete one-odd-seed nonlinear shear ladder for causal late half-grade supply; nonprincipal localized full-history adjoint remains alternative'
snapshot_path.write_text(json.dumps(snap,indent=2)+"\n")
print('integrated source-pump half-grade parity')
