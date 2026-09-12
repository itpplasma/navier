#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_sparse_collar_l3_threshold: pressure-energy-support-bound-nonobstructive-below-exponential-sparsity-threshold\n'
insert=needle+'source_collar_angular_ancestry: target-grade-pressure-requires-half-grade-ancestor-no-symbol-cancellation\n'
assert p.count(needle)==1 and 'source_collar_angular_ancestry:' not in p
p=p.replace(needle,insert,1)

anchor='''The next exact collar discriminator is therefore **attainability**, not another\nsupport-size estimate: determine whether divergence-free quadratic stresses in\nthe pressure-allowed collar can actually realize an entry-scale high-angular\npressure/velocity trace, or prove an operator lower-bound/non-attainability\ntheorem. If that second collar mechanism also returns to the uncontrolled full\nhistory, switch to the complete physical adjoint. UE1 and the terminal claim\nremain open.\n'''
replacement='''The second collar discriminator isolates exact angular ancestry. If `u_L`\ncontains only grades `2|m|<N` and `u_H=u-u_L`, angular convolution gives\n`Pi_N(u_L tensor u_L)=0` exactly and\n\n    ||Pi_N(chi u tensor u)||_1\n      <= 2 ||u_H||_2 ||u||_2.\n\nThus a grade-`N` direct pressure source must already contain a velocity ancestor\nof grade at least `N/2`. With finite energy and the collar pressure operator this\nonly forces an exponentially small high-half ancestor; it does not close the\nroute. Conversely an exact divergence-free two-wave example has nonzero\nquadratic pressure coefficient `-1`, so incompressibility supplies no universal\nsymbol cancellation once such ancestors exist. See\n`research/evidence/2026-09-12-collar-angular-ancestry.md`.\n\nThis is the second serious sparse-collar mechanism. The first left a broad\nexponentially sparse noncritical window; the second shows direct pressure cannot\nbootstrap the target from low grades and merely relocates UE1 to a high-grade\nexterior ancestry hierarchy. Further local collar algebra would rename the same\nhard core. Per the diversification rule, the next primary attack is now the\n**complete physical adjoint / full-history minimum-control cost**, retaining\nexterior occupation and the nonlinear returned state. Grade-changing/nonparent\nlate regeneration remains the constructive alternative. UE1 and the terminal\nclaim remain open.\n'''
assert p.count(anchor)==1
plan.write_text(p.replace(anchor,replacement,1))

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert not any(c['id']=='collar-angular-ancestry' for c in controls['controls'])
controls['controls'].append({
  'id':'collar-angular-ancestry',
  'scope':'axisymmetric-cutoff quadratic collar stress and target angular pressure grade N',
  'evidence':'research/evidence/2026-09-12-collar-angular-ancestry.md',
  'rigor':'exact-angular-algebra-plus-analytic-L1-author-proof',
  'observation':{
    'low_low_target_grade':False,
    'required_velocity_ancestor':'abs(m)>=N/2',
    'target_stress_bound':'2 ||u_H||_2 ||u||_2',
    'universal_divergence_free_pressure_cancellation':False,
    'collar_parent_supply':'relocated-to-high-grade-ancestry'
  }
})
controls_path.write_text(json.dumps(controls,indent=2)+'\n')

base=root/'research/game/models/baseline.py'
b=base.read_text()
needle_b="    'sparse-collar-l3-threshold': {'required_energy_exponent': '-(C-kappa/2) for kappa<2C', 'forced_L3_exponent': '-(C-kappa/2)/2+beta/6', 'L3_growth_threshold': 'beta>3(C-kappa/2)', 'sparse_support_alone_excludes_collar': False, 'quadratic_stress_attainability': 'open'},\n"
insert_b=needle_b+"    'collar-angular-ancestry': {'low_low_target_grade': False, 'required_velocity_ancestor': 'abs(m)>=N/2', 'target_stress_bound': '2 ||u_H||_2 ||u||_2', 'universal_divergence_free_pressure_cancellation': False, 'collar_parent_supply': 'relocated-to-high-grade-ancestry'},\n"
assert b.count(needle_b)==1 and "'collar-angular-ancestry'" not in b
base.write_text(b.replace(needle_b,insert_b,1))

def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
snap_path=root/'research/game/snapshot.json'
snap=json.loads(snap_path.read_text())
snap['authoritative_sources']['PLAN.md']=blob(plan)
ev=root/'research/evidence/2026-09-12-collar-angular-ancestry.md'
snap['authoritative_sources']['research/evidence/2026-09-12-collar-angular-ancestry.md']=blob(ev)
snap['active_frontier']='complete physical adjoint/full-history minimum-control cost as primary diversified attack, with grade-changing/nonparent late regeneration as constructive alternative'
snap_path.write_text(json.dumps(snap,indent=2)+'\n')
