#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_relay_scale_homogeneity: hard-quartic-easy-quadratic-stage-factors-one-eighth-one-half\n'
insert=needle+'source_birth_linear_stage_balance: refuted-by-easy-product-and-rate-ordering\n'
assert p.count(needle)==1 and 'source_birth_linear_stage_balance:' not in p
p=p.replace(needle,insert,1)

anchor='''The next active test must therefore quantify a **finite-duration stage map**\nwith this hard/easy amplitude imbalance, the grade-`m` cubic pollutant and the\nexpanding inherited unstable family all retained. A constructive proof must\nshow that stage amplification restores the two hard `O(epsilon^4)` channels to\nthe four-parent input class without losing control to the easy\n`O(epsilon^2)` channels; an obstruction should prove that this is impossible or\nterminal-strength. The alternative active mechanisms remain a full physical\ninterstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or a\ncomplete full-history adjoint. No bound on the sparse collar stress or\nfull-history gain has been obtained. UE1 and the terminal claim remain open.\n'''
replacement='''The obvious birth-then-linear-amplification repair is now excluded exactly.\nUnder the load-bearing dual pair-product constraints, the two easy quadratic\nchildren obey an invariant nonzero product, so they cannot both be tuned below\ntheir natural `epsilon^2` scale while the two hard children begin only at\n`epsilon^4`. Moreover the source-reference positive-branch rates satisfy\n\n    r_4 > r_3 > r_2 > r_1,\n\nwith `p_3,p_4` the easy channels and `p_1,p_2` the hard channels. Hence every\ncommon positive linear amplification interval makes the easy/hard imbalance\nworse, not better. See `research/evidence/2026-09-12-stage-balance-wall.md`.\n\nAfter two serious passes at the same hard/easy stage mismatch, the active\nconstructive route must change mechanism. The next test is **nonlinear /\nhigher-dimensional balancing**: add stable grade-`2m` counterterms or other\nextra modes and determine whether the easy quadratic births can be canceled\nwithout producing lower-order hard-sector errors, then ask whether those\ncounterterms are themselves recursively supplied by the returned expanding\nstate rather than reset. The alternative active routes remain the full physical\ninterstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or a\ncomplete full-history adjoint. UE1 and the terminal claim remain open.\n'''
assert p.count(anchor)==1
p=p.replace(anchor,replacement,1)
plan.write_text(p)

controls=root/'research/game/controls.json'
c=controls.read_text()
end='''    {\n      "id": "relay-scale-homogeneity",\n      "scope": "dual-tuned source-reference factor-two parent relay",\n      "evidence": "research/evidence/2026-09-12-relay-scale-homogeneity.md",\n      "rigor": "exact-algebra-author-proof",\n      "observation": {\n        "hard_targets": "2p1,2p2 quadratic-zero quartic-nonzero",\n        "easy_targets": "2p3,2p4 quadratic-nonzero",\n        "factor_two_scale": "hard=1/8 easy=1/2",\n        "finite_duration_stage_map": false\n      }\n    }\n  ]\n}\n'''
add='''    {\n      "id": "relay-scale-homogeneity",\n      "scope": "dual-tuned source-reference factor-two parent relay",\n      "evidence": "research/evidence/2026-09-12-relay-scale-homogeneity.md",\n      "rigor": "exact-algebra-author-proof",\n      "observation": {\n        "hard_targets": "2p1,2p2 quadratic-zero quartic-nonzero",\n        "easy_targets": "2p3,2p4 quadratic-nonzero",\n        "factor_two_scale": "hard=1/8 easy=1/2",\n        "finite_duration_stage_map": false\n      }\n    },\n    {\n      "id": "stage-balance-wall",\n      "scope": "dual-tuned four-parent birth followed by common linear amplification",\n      "evidence": "research/evidence/2026-09-12-stage-balance-wall.md",\n      "rigor": "exact-algebra-spectral-author-proof",\n      "observation": {\n        "easy_product": "nonzero fixed multiple of epsilon^4",\n        "balanced_parent_easy_lower_bound": "at least one Omega(epsilon^2)",\n        "hard_birth_order": "O(epsilon^4)",\n        "linear_rate_order": "every easy rate exceeds every hard rate",\n        "birth_then_linear_balance": false\n      }\n    }\n  ]\n}\n'''
assert c.count(end)==1 and '"stage-balance-wall"' not in c
controls.write_text(c.replace(end,add,1))

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
line="    'relay-scale-homogeneity': {'hard_targets': '2p1,2p2 quadratic-zero quartic-nonzero', 'easy_targets': '2p3,2p4 quadratic-nonzero', 'factor_two_scale': 'hard=1/8 easy=1/2', 'finite_duration_stage_map': False},\n"
newline=line+"    'stage-balance-wall': {'easy_product': 'nonzero fixed multiple of epsilon^4', 'balanced_parent_easy_lower_bound': 'at least one Omega(epsilon^2)', 'hard_birth_order': 'O(epsilon^4)', 'linear_rate_order': 'every easy rate exceeds every hard rate', 'birth_then_linear_balance': False},\n"
assert b.count(line)==1 and "'stage-balance-wall'" not in b
baseline.write_text(b.replace(line,newline,1))

snapshot=root/'research/game/snapshot.json'
s=json.loads(snapshot.read_text())
def blob(path):
    return subprocess.check_output(['git','hash-object',path],cwd=root,text=True).strip()
s['authoritative_sources']['PLAN.md']=blob('PLAN.md')
ev='research/evidence/2026-09-12-stage-balance-wall.md'
s['authoritative_sources'][ev]=blob(ev)
s['active_frontier']='nonlinear or higher-dimensional balancing via stable grade-2m counterterms/extra modes and recursive supply, full physical interstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or complete full-history adjoint exclusion'
snapshot.write_text(json.dumps(s,indent=2)+'\n')
