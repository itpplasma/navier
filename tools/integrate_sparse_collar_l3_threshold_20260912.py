#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_recentered_z1_parent_adapter: refuted-by-multiset-and-hyperbolicity-wall\n'
insert=needle+'source_sparse_collar_l3_threshold: pressure-energy-support-bound-nonobstructive-below-exponential-sparsity-threshold\n'
assert p.count(needle)==1 and 'source_sparse_collar_l3_threshold:' not in p
p=p.replace(needle,insert,1)

anchor='''Together with the single-label wall, this is a second serious return to the\nsame physical-adapter obstruction. The active run must therefore leave simple\n`z=1` recentering. A surviving constructive source route must use a genuinely\ngrade-changing/nonparent transition, additional inherited state with a new\nhyperbolic structure, or late nonlinear regeneration near the next pulse. Per\nthe diversification rule the next primary attack is the distinct sparse\nthin-collar/nonlocal-entry mechanism; the complete full-history adjoint remains\nthe alternative negative route. UE1 and the terminal claim remain open.\n'''
replacement='''Together with the single-label wall, this is a second serious return to the\nsame physical-adapter obstruction. The active run must therefore leave simple\n`z=1` recentering. A surviving constructive source route must use a genuinely\ngrade-changing/nonparent transition, additional inherited state with a new\nhyperbolic structure, or late nonlinear regeneration near the next pulse.\n\nThe first diversified sparse-collar test gives an exact wall to the obvious\ncritical-norm exclusion. Write the required direct pressure-input scale as\n`A_L=exp(-C L+o(L))` and choose collar thickness\n`delta/r=kappa L/N`. The midpoint form of the existing pressure estimate has\noperator exponent `-kappa L/2+o(L)`, so for `kappa<2C` it only forces kinetic\nenergy `exp(-(C-kappa/2)L+o(L))`. If the stress-bearing velocity occupies an\n`exp(-beta L)` fraction of the collar, Holder forces `L3` exponent\n\n    -(C-kappa/2)/2 + beta/6.\n\nThus pressure+energy+support size implies critical growth only for\n`beta>3(C-kappa/2)`; a wide exponentially sparse window remains\nnon-obstructive. See\n`research/evidence/2026-09-12-sparse-collar-l3-threshold.md`.\n\nThe next exact collar discriminator is therefore **attainability**, not another\nsupport-size estimate: determine whether divergence-free quadratic stresses in\nthe pressure-allowed collar can actually realize an entry-scale high-angular\npressure/velocity trace, or prove an operator lower-bound/non-attainability\ntheorem. If that second collar mechanism also returns to the uncontrolled full\nhistory, switch to the complete physical adjoint. UE1 and the terminal claim\nremain open.\n'''
assert p.count(anchor)==1
plan.write_text(p.replace(anchor,replacement,1))

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert not any(c['id']=='sparse-collar-l3-threshold' for c in controls['controls'])
controls['controls'].append({
  'id':'sparse-collar-l3-threshold',
  'scope':'thin-collar direct pressure signal combined with energy, support volume and L3 continuation',
  'evidence':'research/evidence/2026-09-12-sparse-collar-l3-threshold.md',
  'rigor':'analytic-scaling-author-proof-exact-exponent-check',
  'observation':{
    'required_energy_exponent':'-(C-kappa/2) for kappa<2C',
    'forced_L3_exponent':'-(C-kappa/2)/2+beta/6',
    'L3_growth_threshold':'beta>3(C-kappa/2)',
    'sparse_support_alone_excludes_collar':False,
    'quadratic_stress_attainability':'open'
  }
})
controls_path.write_text(json.dumps(controls,indent=2)+'\n')

base=root/'research/game/models/baseline.py'
b=base.read_text()
needle_b="    'recenter-cage-wall': {'same_rational_cage_after_forward_shift': False, 'same_cage_multiset_condition': 'a=1', 'outer_parent_stable_by_multiplier': 'a>=13/9', 'general_grade_changing_adapter': 'open'},\n"
insert_b=needle_b+"    'sparse-collar-l3-threshold': {'required_energy_exponent': '-(C-kappa/2) for kappa<2C', 'forced_L3_exponent': '-(C-kappa/2)/2+beta/6', 'L3_growth_threshold': 'beta>3(C-kappa/2)', 'sparse_support_alone_excludes_collar': False, 'quadratic_stress_attainability': 'open'},\n"
assert b.count(needle_b)==1 and "'sparse-collar-l3-threshold'" not in b
base.write_text(b.replace(needle_b,insert_b,1))

def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
snap_path=root/'research/game/snapshot.json'
snap=json.loads(snap_path.read_text())
snap['authoritative_sources']['PLAN.md']=blob(plan)
ev=root/'research/evidence/2026-09-12-sparse-collar-l3-threshold.md'
snap['authoritative_sources']['research/evidence/2026-09-12-sparse-collar-l3-threshold.md']=blob(ev)
snap['active_frontier']='explicit divergence-free quadratic-stress attainability/non-attainability in the pressure-allowed sparse collar, grade-changing/nonparent late regeneration, or complete full-history adjoint exclusion'
snap_path.write_text(json.dumps(snap,indent=2)+'\n')
