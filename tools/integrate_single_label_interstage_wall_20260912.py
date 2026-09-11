#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd()
plan=root/'PLAN.md'
p=plan.read_text()
needle='source_four_parent_counterterm_supply: refuted-by-opposite-causal-stable-coordinate\n'
insert=needle+'source_single_label_interstage_adapter: refuted-by-unbounded-exact-lattice-deformation\n'
assert p.count(needle)==1 and 'source_single_label_interstage_adapter:' not in p
p=p.replace(needle,insert,1)

anchor='''This is the second serious pass at stable-counterterm supply, so the frozen\nautonomous stage graph is no longer the active mechanism. A constructive route\nnow requires genuinely additional inherited modes/state or the source's\nnonautonomous scale-changing physical history. The next active attack is the\n**full physical interstage adapter**: quantify the duration and accumulated\ncoefficient variation across one factor-two normalized scale change, rather\nthan extrapolating the fixed-fast-window finite-`L` theorem. Alternative active\nroutes remain sparse thin-collar/nonlocal entry and the complete full-history\nadjoint. UE1 and the terminal claim remain open.\n'''
replacement='''The direct same-label physical adapter is also excluded. A doubled physical\nfrequency requires the similarity scale to contract by\n`rho=2^(-2/h)` before it becomes a normalized parent. On the exact `eta=0` ray,\n`Delta t=(1-rho)Q`, while the fixed lifted-label identity gives\n`partial_t v=Q^(-1-h)`. Hence a single label would have to traverse\n\n    Delta v=(1-rho)Q^(-h),\n    Delta(v/L) comparable to Q^(-h)/ell^2 -> infinity.\n\nBut the exact finite-`L` lattice map has\n`T k-k=(tau d(k),-eta d(k),0)` with `tau=v/L`; on every one of the four parent\nlabels `d(k)^2/|k|^2>=9/500`. Thus the relative lattice deformation becomes\nunbounded across one factor-two scale change. The existing fixed-fast-window\n`O(L^-1)` cage theorem cannot be extrapolated on one fixed label/reference. See\n`research/evidence/2026-09-12-single-label-interstage-wall.md`.\n\nThe physical adapter, if it exists, must therefore be **recentered /\nmulti-label or genuinely nonperturbative**. It needs a transition map between\noverlapping local source frames which carries the entire inherited expanding\nstate and stable counterterms without reset or temporal gluing defects. The\nother active mechanisms remain sparse thin-collar/nonlocal entry and the\ncomplete full-history adjoint. UE1 and the terminal claim remain open.\n'''
assert p.count(anchor)==1
p=p.replace(anchor,replacement,1)
plan.write_text(p)

controls=root/'research/game/controls.json'
c=controls.read_text()
end='''    {\n      "id": "counterterm-causal-mismatch",\n      "scope": "easy stable coordinates on the four-parent backward-eternal source-reference unstable manifold",\n      "evidence": "research/evidence/2026-09-12-counterterm-causal-mismatch.md",\n      "rigor": "exact-analytic-author-proof",\n      "observation": {\n        "unstable_manifold_quadratic_coordinate": "F/D",\n        "future_canceling_coordinate": "-F*(exp(D*T)-1)/D",\n        "ratio_for_T_positive": "1-exp(D*T)<0",\n        "four_parent_causal_counterterm_supply": false\n      }\n    }\n  ]\n}\n'''
add='''    {\n      "id": "counterterm-causal-mismatch",\n      "scope": "easy stable coordinates on the four-parent backward-eternal source-reference unstable manifold",\n      "evidence": "research/evidence/2026-09-12-counterterm-causal-mismatch.md",\n      "rigor": "exact-analytic-author-proof",\n      "observation": {\n        "unstable_manifold_quadratic_coordinate": "F/D",\n        "future_canceling_coordinate": "-F*(exp(D*T)-1)/D",\n        "ratio_for_T_positive": "1-exp(D*T)<0",\n        "four_parent_causal_counterterm_supply": false\n      }\n    },\n    {\n      "id": "single-label-interstage-wall",\n      "scope": "direct extension of the finite-L fixed-label cage across one factor-two normalized scale change",\n      "evidence": "research/evidence/2026-09-12-single-label-interstage-wall.md",\n      "rigor": "exact-source-coordinate-lattice-author-proof",\n      "observation": {\n        "same_label_fast_displacement_over_L": "diverges like Q^(-h)/ell^2",\n        "parent_relative_lattice_deformation_lower_bound": "sqrt(9/500)*abs(Delta v/L)",\n        "direct_fixed_label_adapter": false,\n        "recentered_multilabel_adapter": "open"\n      }\n    }\n  ]\n}\n'''
assert c.count(end)==1 and '"single-label-interstage-wall"' not in c
controls.write_text(c.replace(end,add,1))

baseline=root/'research/game/models/baseline.py'
b=baseline.read_text()
line="    'counterterm-causal-mismatch': {'unstable_manifold_quadratic_coordinate': 'F/D', 'future_canceling_coordinate': '-F*(exp(D*T)-1)/D', 'ratio_for_T_positive': '1-exp(D*T)<0', 'four_parent_causal_counterterm_supply': False},\n"
newline=line+"    'single-label-interstage-wall': {'same_label_fast_displacement_over_L': 'diverges like Q^(-h)/ell^2', 'parent_relative_lattice_deformation_lower_bound': 'sqrt(9/500)*abs(Delta v/L)', 'direct_fixed_label_adapter': False, 'recentered_multilabel_adapter': 'open'},\n"
assert b.count(line)==1 and "'single-label-interstage-wall'" not in b
baseline.write_text(b.replace(line,newline,1))

snapshot=root/'research/game/snapshot.json'
s=json.loads(snapshot.read_text())
def blob(path): return subprocess.check_output(['git','hash-object',path],cwd=root,text=True).strip()
s['authoritative_sources']['PLAN.md']=blob('PLAN.md')
ev='research/evidence/2026-09-12-single-label-interstage-wall.md'
s['authoritative_sources'][ev]=blob(ev)
s['active_frontier']='recentered multi-label or nonperturbative physical interstage adapter with inherited expanding state, sparse thin-collar/nonlocal entry, or complete full-history adjoint exclusion'
snapshot.write_text(json.dumps(s,indent=2)+'\n')
