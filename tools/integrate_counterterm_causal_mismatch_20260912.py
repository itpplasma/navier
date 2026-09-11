#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_stable_preload_balance: proved-local-reference-counterterm-repair-recursive-supply-open\n'
insert=needle+'source_four_parent_counterterm_supply: refuted-by-opposite-causal-stable-coordinate\n'
assert p.count(needle)==1 and 'source_four_parent_counterterm_supply:' not in p
p=p.replace(needle,insert,1)

anchor='''The cascade blocker therefore moves backward again: these stable counterterms\nare left-edge data and cannot be reset independently. The next exact test is\n**recursive causal supply**. Compare the required easy-target counterterms with\nthe uniquely determined quadratic stable coordinates on the four-parent\nbackward-eternal unstable manifold. If incompatible, the stage requires\ngenuinely additional inherited modes/state. The alternative active routes\nremain the full physical interstage propagator/adjoint adapter, sparse\nthin-collar/nonlocal entry, or the complete full-history adjoint. UE1 and the\nterminal claim remain open.\n'''
replacement='''The free stable-counterterm repair is **not** supplied by the same four-parent\nbackward-eternal unstable manifold. At either easy target, write the nonzero\nquadratic forcing as `F`, the stable target rate as `sigma`, and the parent-rate\nsum as `lambda_p`; the exact mismatch `D=lambda_p-sigma` is positive. The\nunique backward-eternal stable coordinate is `F/D`. In contrast, the unique\nleft-edge value which cancels that easy mode after any positive future stage\n`T` is\n\n    -F (exp(D T)-1)/D.\n\nTheir ratio is `1-exp(D T)<0` for every `T>0`. Thus the local balanced stage is\noff the four-coordinate causal unstable graph at quadratic order; no parent\nphase/factorization can repair this because both values carry the same `F`. See\n`research/evidence/2026-09-12-counterterm-causal-mismatch.md`.\n\nThis is the second serious pass at stable-counterterm supply, so the frozen\nautonomous stage graph is no longer the active mechanism. A constructive route\nnow requires genuinely additional inherited modes/state or the source's\nnonautonomous scale-changing physical history. The next active attack is the\n**full physical interstage adapter**: quantify the duration and accumulated\ncoefficient variation across one factor-two normalized scale change, rather\nthan extrapolating the fixed-fast-window finite-`L` theorem. Alternative active\nroutes remain sparse thin-collar/nonlocal entry and the complete full-history\nadjoint. UE1 and the terminal claim remain open.\n'''
assert p.count(anchor)==1
p=p.replace(anchor,replacement,1)
plan.write_text(p)

controls=root/'research/game/controls.json'
c=controls.read_text()
end='''    {\n      "id": "stable-preload-balance",\n      "scope": "short frozen full-lattice relay with two freely supplied stable easy-target counterterms",\n      "evidence": "research/evidence/2026-09-12-stable-preload-balance.md",\n      "rigor": "analytic-exact-author-proof",\n      "observation": {\n        "easy_leading_births_cancelled": true,\n        "lower_order_hard_contamination": false,\n        "corrected_hard_coefficients_nonzero": true,\n        "exact_short_stage_easy_retuning": true,\n        "recursive_counterterm_supply": false\n      }\n    }\n  ]\n}\n'''
add='''    {\n      "id": "stable-preload-balance",\n      "scope": "short frozen full-lattice relay with two freely supplied stable easy-target counterterms",\n      "evidence": "research/evidence/2026-09-12-stable-preload-balance.md",\n      "rigor": "analytic-exact-author-proof",\n      "observation": {\n        "easy_leading_births_cancelled": true,\n        "lower_order_hard_contamination": false,\n        "corrected_hard_coefficients_nonzero": true,\n        "exact_short_stage_easy_retuning": true,\n        "recursive_counterterm_supply": false\n      }\n    },\n    {\n      "id": "counterterm-causal-mismatch",\n      "scope": "easy stable coordinates on the four-parent backward-eternal source-reference unstable manifold",\n      "evidence": "research/evidence/2026-09-12-counterterm-causal-mismatch.md",\n      "rigor": "exact-analytic-author-proof",\n      "observation": {\n        "unstable_manifold_quadratic_coordinate": "F/D",\n        "future_canceling_coordinate": "-F*(exp(D*T)-1)/D",\n        "ratio_for_T_positive": "1-exp(D*T)<0",\n        "four_parent_causal_counterterm_supply": false\n      }\n    }\n  ]\n}\n'''
assert c.count(end)==1 and '"counterterm-causal-mismatch"' not in c
controls.write_text(c.replace(end,add,1))

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
line="    'stable-preload-balance': {'easy_leading_births_cancelled': True, 'lower_order_hard_contamination': False, 'corrected_hard_coefficients_nonzero': True, 'exact_short_stage_easy_retuning': True, 'recursive_counterterm_supply': False},\n"
newline=line+"    'counterterm-causal-mismatch': {'unstable_manifold_quadratic_coordinate': 'F/D', 'future_canceling_coordinate': '-F*(exp(D*T)-1)/D', 'ratio_for_T_positive': '1-exp(D*T)<0', 'four_parent_causal_counterterm_supply': False},\n"
assert b.count(line)==1 and "'counterterm-causal-mismatch'" not in b
baseline.write_text(b.replace(line,newline,1))

snapshot=root/'research/game/snapshot.json'
s=json.loads(snapshot.read_text())
def blob(path): return subprocess.check_output(['git','hash-object',path],cwd=root,text=True).strip()
s['authoritative_sources']['PLAN.md']=blob('PLAN.md')
ev='research/evidence/2026-09-12-counterterm-causal-mismatch.md'
s['authoritative_sources'][ev]=blob(ev)
s['active_frontier']='full physical interstage adapter across one factor-two scale change with inherited expanding state, sparse thin-collar/nonlocal entry, or complete full-history adjoint exclusion'
snapshot.write_text(json.dumps(s,indent=2)+'\n')
