#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_birth_linear_stage_balance: refuted-by-easy-product-and-rate-ordering\n'
insert=needle+'source_stable_preload_balance: proved-local-reference-counterterm-repair-recursive-supply-open\n'
assert p.count(needle)==1 and 'source_stable_preload_balance:' not in p
p=p.replace(needle,insert,1)

anchor='''After two serious passes at the same hard/easy stage mismatch, the active\nconstructive route must change mechanism. The next test is **nonlinear /\nhigher-dimensional balancing**: add stable grade-`2m` counterterms or other\nextra modes and determine whether the easy quadratic births can be canceled\nwithout producing lower-order hard-sector errors, then ask whether those\ncounterterms are themselves recursively supplied by the returned expanding\nstate rather than reset. The alternative active routes remain the full physical\ninterstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or a\ncomplete full-history adjoint. UE1 and the terminal claim remain open.\n'''
replacement='''The first higher-dimensional repair succeeds locally. Add the two stable\ngrade-`2m` easy-target coordinates at the left edge with leading size\n`-epsilon^2 T Q_j`. They cancel the `O(epsilon^2 T)` easy endpoint births.\nPhase grading prevents any `O(epsilon^3)` hard-sector contamination; the first\npreload correction to the hard grade-`2m` targets enters at\n`O(epsilon^4 T^3)`. After retaining every such leading tree, both corrected\nhard coefficients remain strictly nonzero by exact rational radical\nenclosures. Analytic endpoint dependence and the identity derivative in the\ntwo preload coordinates then give an implicit-function family which sets the\ntwo easy endpoint growing coordinates to zero, or to prescribed\n`O(epsilon^4)` values, on sufficiently short frozen-reference stages. See\n`research/evidence/2026-09-12-stable-preload-balance.md`.\n\nThe cascade blocker therefore moves backward again: these stable counterterms\nare left-edge data and cannot be reset independently. The next exact test is\n**recursive causal supply**. Compare the required easy-target counterterms with\nthe uniquely determined quadratic stable coordinates on the four-parent\nbackward-eternal unstable manifold. If incompatible, the stage requires\ngenuinely additional inherited modes/state. The alternative active routes\nremain the full physical interstage propagator/adjoint adapter, sparse\nthin-collar/nonlocal entry, or the complete full-history adjoint. UE1 and the\nterminal claim remain open.\n'''
assert p.count(anchor)==1
p=p.replace(anchor,replacement,1)
plan.write_text(p)

controls=root/'research/game/controls.json'
c=controls.read_text()
end='''    {\n      "id": "stage-balance-wall",\n      "scope": "dual-tuned four-parent birth followed by common linear amplification",\n      "evidence": "research/evidence/2026-09-12-stage-balance-wall.md",\n      "rigor": "exact-algebra-spectral-author-proof",\n      "observation": {\n        "easy_product": "nonzero fixed multiple of epsilon^4",\n        "balanced_parent_easy_lower_bound": "at least one Omega(epsilon^2)",\n        "hard_birth_order": "O(epsilon^4)",\n        "linear_rate_order": "every easy rate exceeds every hard rate",\n        "birth_then_linear_balance": false\n      }\n    }\n  ]\n}\n'''
add='''    {\n      "id": "stage-balance-wall",\n      "scope": "dual-tuned four-parent birth followed by common linear amplification",\n      "evidence": "research/evidence/2026-09-12-stage-balance-wall.md",\n      "rigor": "exact-algebra-spectral-author-proof",\n      "observation": {\n        "easy_product": "nonzero fixed multiple of epsilon^4",\n        "balanced_parent_easy_lower_bound": "at least one Omega(epsilon^2)",\n        "hard_birth_order": "O(epsilon^4)",\n        "linear_rate_order": "every easy rate exceeds every hard rate",\n        "birth_then_linear_balance": false\n      }\n    },\n    {\n      "id": "stable-preload-balance",\n      "scope": "short frozen full-lattice relay with two freely supplied stable easy-target counterterms",\n      "evidence": "research/evidence/2026-09-12-stable-preload-balance.md",\n      "rigor": "analytic-exact-author-proof",\n      "observation": {\n        "easy_leading_births_cancelled": true,\n        "lower_order_hard_contamination": false,\n        "corrected_hard_coefficients_nonzero": true,\n        "exact_short_stage_easy_retuning": true,\n        "recursive_counterterm_supply": false\n      }\n    }\n  ]\n}\n'''
assert c.count(end)==1 and '"stable-preload-balance"' not in c
controls.write_text(c.replace(end,add,1))

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
line="    'stage-balance-wall': {'easy_product': 'nonzero fixed multiple of epsilon^4', 'balanced_parent_easy_lower_bound': 'at least one Omega(epsilon^2)', 'hard_birth_order': 'O(epsilon^4)', 'linear_rate_order': 'every easy rate exceeds every hard rate', 'birth_then_linear_balance': False},\n"
newline=line+"    'stable-preload-balance': {'easy_leading_births_cancelled': True, 'lower_order_hard_contamination': False, 'corrected_hard_coefficients_nonzero': True, 'exact_short_stage_easy_retuning': True, 'recursive_counterterm_supply': False},\n"
assert b.count(line)==1 and "'stable-preload-balance'" not in b
baseline.write_text(b.replace(line,newline,1))

snapshot=root/'research/game/snapshot.json'
s=json.loads(snapshot.read_text())
def blob(path):
    return subprocess.check_output(['git','hash-object',path],cwd=root,text=True).strip()
s['authoritative_sources']['PLAN.md']=blob('PLAN.md')
ev='research/evidence/2026-09-12-stable-preload-balance.md'
s['authoritative_sources'][ev]=blob(ev)
s['active_frontier']='recursive causal supply of stable grade-2m counterterms by the returned expanding state, full physical interstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, or complete full-history adjoint exclusion'
snapshot.write_text(json.dumps(s,indent=2)+'\n')
