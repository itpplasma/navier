#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_single_label_interstage_adapter: refuted-by-unbounded-exact-lattice-deformation\n'
insert=needle+'source_recentered_z1_parent_adapter: refuted-by-multiset-and-hyperbolicity-wall\n'
assert p.count(needle)==1 and 'source_recentered_z1_parent_adapter:' not in p
p=p.replace(needle,insert,1)

anchor='''The physical adapter, if it exists, must therefore be **recentered /\nmulti-label or genuinely nonperturbative**. It needs a transition map between\noverlapping local source frames which carries the entire inherited expanding\nstate and stable counterterms without reset or temporal gluing defects. The\nother active mechanisms remain sparse thin-collar/nonlocal entry and the\ncomplete full-history adjoint. UE1 and the terminal claim remain open.\n'''
replacement='''The first exact recenter repair is also blocked. At fast-time ratio\n`tau=v/L`, the four `z=1` parent tilts are `c +/- a u_A,c +/- a u_B` with\n`a=1+tau`. Their second centered moment is exactly `a^2` times the frozen one,\nso equality with the proved rational cage after arbitrary parent permutation\nforces `a=1`: no nonzero forward shift returns exactly to that cage. If the\nnew frame instead inherits the enlarged separations, the outer positive parent\nreaches tilt `7/10` already at `a=13/9`, where its certified reference growth\nrate is strictly negative, and monotonicity keeps it stable thereafter. See\n`research/evidence/2026-09-12-recenter-cage-wall.md`.\n\nTogether with the single-label wall, this is a second serious return to the\nsame physical-adapter obstruction. The active run must therefore leave simple\n`z=1` recentering. A surviving constructive source route must use a genuinely\ngrade-changing/nonparent transition, additional inherited state with a new\nhyperbolic structure, or late nonlinear regeneration near the next pulse. Per\nthe diversification rule the next primary attack is the distinct sparse\nthin-collar/nonlocal-entry mechanism; the complete full-history adjoint remains\nthe alternative negative route. UE1 and the terminal claim remain open.\n'''
assert p.count(anchor)==1
p=p.replace(anchor,replacement,1)
plan.write_text(p)

controls_path=root/'research/game/controls.json'
controls=json.loads(controls_path.read_text())
assert not any(c['id']=='recenter-cage-wall' for c in controls['controls'])
controls['controls'].append({
  'id':'recenter-cage-wall',
  'scope':'recentered source-reference propagation constrained to the z=1 four-growing-parent class',
  'evidence':'research/evidence/2026-09-12-recenter-cage-wall.md',
  'rigor':'exact-source-phase-spectral-author-proof',
  'observation':{
    'same_rational_cage_after_forward_shift':False,
    'same_cage_multiset_condition':'a=1',
    'outer_parent_stable_by_multiplier':'a>=13/9',
    'general_grade_changing_adapter':'open'
  }
})
controls_path.write_text(json.dumps(controls,indent=2)+'\n')

base=root/'research/game/models/baseline.py'
b=base.read_text()
needle_b="    'single-label-interstage-wall': {'same_label_fast_displacement_over_L': 'diverges like Q^(-h)/ell^2', 'parent_relative_lattice_deformation_lower_bound': 'sqrt(9/500)*abs(Delta v/L)', 'direct_fixed_label_adapter': False, 'recentered_multilabel_adapter': 'open'},\n"
insert_b=needle_b+"    'recenter-cage-wall': {'same_rational_cage_after_forward_shift': False, 'same_cage_multiset_condition': 'a=1', 'outer_parent_stable_by_multiplier': 'a>=13/9', 'general_grade_changing_adapter': 'open'},\n"
assert b.count(needle_b)==1 and "'recenter-cage-wall'" not in b
base.write_text(b.replace(needle_b,insert_b,1))

# Update authoritative snapshot hashes only after the authoritative files exist.
def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
snap_path=root/'research/game/snapshot.json'
snap=json.loads(snap_path.read_text())
snap['authoritative_sources']['PLAN.md']=blob(plan)
ev=root/'research/evidence/2026-09-12-recenter-cage-wall.md'
snap['authoritative_sources']['research/evidence/2026-09-12-recenter-cage-wall.md']=blob(ev)
snap['active_frontier']='sparse thin-collar/nonlocal entry as primary diversified attack, grade-changing/nonparent physical parent regeneration, or complete full-history adjoint exclusion'
snap_path.write_text(json.dumps(snap,indent=2)+'\n')
