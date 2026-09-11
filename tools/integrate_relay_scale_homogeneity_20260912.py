#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_reference_passive_interstage_carry: exp-minus-c-Qminus-h-damped-physical-adapter-open\n'
insert=needle+'source_relay_scale_homogeneity: hard-quartic-easy-quadratic-stage-factors-one-eighth-one-half\n'
assert p.count(needle)==1 and 'source_relay_scale_homogeneity:' not in p
p=p.replace(needle,insert,1)

anchor='''The next active test must therefore construct continuous/late nonlinear\nstagewise feeding of the expanding state, prove a full physical interstage\npropagator/adjoint adapter that transfers the reference loss, address sparse\nthin-collar/nonlocal entry, or close the complete physical adjoint by another\nfull-history mechanism. No bound on the sparse collar stress or full-history\ngain has been obtained. UE1 and the terminal claim remain open.\n'''
replacement='''A further exact discriminator shows that local late regeneration itself does\nnot disappear under stage rescaling. The doubled-parent quartet is mixed order:\n`2p_1,2p_2` have identically zero quadratic self-pair coefficients and retain\nthe already proved nonzero quartic births, while `2p_3,2p_4` have strictly\nnonzero growing coordinates already at quadratic order. Uniform frequency\nrescaling by `alpha` multiplies each Leray bilinear vertex by `alpha`; hence the\nhard quartic channels scale as `alpha^3` and the easy quadratic channels as\n`alpha`. At factor-two normalization these are exact factors `1/8` and `1/2`.\nSee `research/evidence/2026-09-12-relay-scale-homogeneity.md`.\n\nThe next active test must therefore quantify a **finite-duration stage map**\nwith this hard/easy amplitude imbalance, the grade-`m` cubic pollutant and the\nexpanding inherited unstable family all retained. A constructive proof must\nshow that stage amplification restores the two hard `O(epsilon^4)` channels to\nthe four-parent input class without losing control to the easy\n`O(epsilon^2)` channels; an obstruction should prove that this is impossible or\nterminal-strength. The alternative active mechanisms remain a full physical\ninterstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or a\ncomplete full-history adjoint. No bound on the sparse collar stress or\nfull-history gain has been obtained. UE1 and the terminal claim remain open.\n'''
assert p.count(anchor)==1
p=p.replace(anchor,replacement,1)
plan.write_text(p)

controls=root/'research/game/controls.json'
c=controls.read_text()
end='''    {\n      "id": "energy-controlled-exterior-pressure",\n      "scope": "direct pressure of finite-energy quadratic exterior stress on R3",\n      "evidence": "research/evidence/2026-09-11-exterior-pressure-energy.md",\n      "rigor": "analytic-author-proof-exact-controls",\n      "observation": {\n        "L1_stress_to_L2_constant": "3/sqrt(2*pi)",\n        "optimal_intermediate_radius": "2*N*R/(2*N+5)",\n        "quadratic_far_input": "bounded by initial energy",\n        "full_history_gain": false\n      }\n    }\n  ]\n}\n'''
add='''    {\n      "id": "energy-controlled-exterior-pressure",\n      "scope": "direct pressure of finite-energy quadratic exterior stress on R3",\n      "evidence": "research/evidence/2026-09-11-exterior-pressure-energy.md",\n      "rigor": "analytic-author-proof-exact-controls",\n      "observation": {\n        "L1_stress_to_L2_constant": "3/sqrt(2*pi)",\n        "optimal_intermediate_radius": "2*N*R/(2*N+5)",\n        "quadratic_far_input": "bounded by initial energy",\n        "full_history_gain": false\n      }\n    },\n    {\n      "id": "relay-scale-homogeneity",\n      "scope": "dual-tuned source-reference factor-two parent relay",\n      "evidence": "research/evidence/2026-09-12-relay-scale-homogeneity.md",\n      "rigor": "exact-algebra-author-proof",\n      "observation": {\n        "hard_targets": "2p1,2p2 quadratic-zero quartic-nonzero",\n        "easy_targets": "2p3,2p4 quadratic-nonzero",\n        "factor_two_scale": "hard=1/8 easy=1/2",\n        "finite_duration_stage_map": false\n      }\n    }\n  ]\n}\n'''
assert c.count(end)==1 and '"relay-scale-homogeneity"' not in c
controls.write_text(c.replace(end,add,1))

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
line="    'energy-controlled-exterior-pressure': {'L1_stress_to_L2_constant': '3/sqrt(2*pi)', 'optimal_intermediate_radius': '2*N*R/(2*N+5)', 'quadratic_far_input': 'bounded by initial energy', 'full_history_gain': False},\n"
newline=line+"    'relay-scale-homogeneity': {'hard_targets': '2p1,2p2 quadratic-zero quartic-nonzero', 'easy_targets': '2p3,2p4 quadratic-nonzero', 'factor_two_scale': 'hard=1/8 easy=1/2', 'finite_duration_stage_map': False},\n"
assert b.count(line)==1 and "'relay-scale-homogeneity'" not in b
baseline.write_text(b.replace(line,newline,1))

snapshot=root/'research/game/snapshot.json'
s=json.loads(snapshot.read_text())
def blob(path):
    return subprocess.check_output(['git','hash-object',path],cwd=root,text=True).strip()
s['authoritative_sources']['PLAN.md']=blob('PLAN.md')
ev='research/evidence/2026-09-12-relay-scale-homogeneity.md'
s['authoritative_sources'][ev]=blob(ev)
s['active_frontier']='finite-duration mixed hard/easy nonlinear stage map with expanding returned state, full physical interstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or complete full-history adjoint exclusion'
snapshot.write_text(json.dumps(s,indent=2)+'\n')
