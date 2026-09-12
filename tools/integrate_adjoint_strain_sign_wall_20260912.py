#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

root=Path.cwd(); plan=root/'PLAN.md'; p=plan.read_text()
needle='source_collar_angular_ancestry: target-grade-pressure-requires-half-grade-ancestor-no-symbol-cancellation\n'
insert=needle+'source_adjoint_strain_sign: no-nonzero-solenoidal-sign-definite-nonlinear-certificate\n'
assert p.count(needle)==1 and 'source_adjoint_strain_sign:' not in p
p=p.replace(needle,insert,1)
anchor='''This is the second serious sparse-collar mechanism. The first left a broad\nexponentially sparse noncritical window; the second shows direct pressure cannot\nbootstrap the target from low grades and merely relocates UE1 to a high-grade\nexterior ancestry hierarchy. Further local collar algebra would rename the same\nhard core. Per the diversification rule, the next primary attack is now the\n**complete physical adjoint / full-history minimum-control cost**, retaining\nexterior occupation and the nonlinear returned state. Grade-changing/nonparent\nlate regeneration remains the constructive alternative. UE1 and the terminal\nclaim remain open.\n'''
replacement='''This is the second serious sparse-collar mechanism. The first left a broad\nexponentially sparse noncritical window; the second shows direct pressure cannot\nbootstrap the target from low grades and merely relocates UE1 to a high-grade\nexterior ancestry hierarchy. Further local collar algebra would rename the same\nhard core.\n\nThe first diversified complete-adjoint test closes a sign shortcut. In the\nexact nonlinear adjoint identity the unknown term is `(w tensor w):S(z)`. For\nevery solenoidal adjoint `tr S(z)=0`; a nonzero symmetric trace-free matrix is\nindefinite, while the whole-space Fourier identity\n`2||S(z)||_2^2=||grad z||_2^2` shows that an `L2` solenoidal adjoint with zero\nstrain is itself zero. Hence no nonzero admissible adjoint can make the\nquadratic correction term one-signed for arbitrary `w`. See\n`research/evidence/2026-09-12-adjoint-strain-sign-wall.md`.\n\nA terminal adjoint attack must therefore control the **magnitude** of the\nnonlinear strain budget or exploit source-specific correction structure. The\nnext exact discriminator tests the principal high-frequency source force in\nthat same strain-dual norm. Grade-changing/nonparent late regeneration remains\nthe constructive alternative. UE1 and the terminal claim remain open.\n'''
assert p.count(anchor)==1; plan.write_text(p.replace(anchor,replacement,1))

cp=root/'research/game/controls.json'; controls=json.loads(cp.read_text())
assert not any(c['id']=='adjoint-strain-sign-wall' for c in controls['controls'])
controls['controls'].append({'id':'adjoint-strain-sign-wall','scope':'nonlinear full-adjoint de-forcing identity for arbitrary correction w','evidence':'research/evidence/2026-09-12-adjoint-strain-sign-wall.md','rigor':'exact-linear-algebra-Fourier-author-proof','observation':{'solenoidal_strain_trace':0,'nonzero_strain_pointwise_indefinite':True,'zero_strain_L2_solenoidal_adjoint':'zero','sign_only_nonlinear_certificate':False}})
cp.write_text(json.dumps(controls,indent=2)+'\n')
base=root/'research/game/models/baseline.py'; b=base.read_text()
needle_b="    'collar-angular-ancestry': {'low_low_target_grade': False, 'required_velocity_ancestor': 'abs(m)>=N/2', 'target_stress_bound': '2 ||u_H||_2 ||u||_2', 'universal_divergence_free_pressure_cancellation': False, 'collar_parent_supply': 'relocated-to-high-grade-ancestry'},\n"
insert_b=needle_b+"    'adjoint-strain-sign-wall': {'solenoidal_strain_trace': 0, 'nonzero_strain_pointwise_indefinite': True, 'zero_strain_L2_solenoidal_adjoint': 'zero', 'sign_only_nonlinear_certificate': False},\n"
assert b.count(needle_b)==1 and "'adjoint-strain-sign-wall'" not in b; base.write_text(b.replace(needle_b,insert_b,1))
def blob(path): return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
sp=root/'research/game/snapshot.json'; snap=json.loads(sp.read_text()); snap['authoritative_sources']['PLAN.md']=blob(plan); ev=root/'research/evidence/2026-09-12-adjoint-strain-sign-wall.md'; snap['authoritative_sources']['research/evidence/2026-09-12-adjoint-strain-sign-wall.md']=blob(ev); snap['active_frontier']='source-specific magnitude control of the full nonlinear adjoint strain budget, with principal-carrier stress duality as next discriminator; grade-changing/nonparent late regeneration remains constructive alternative'; sp.write_text(json.dumps(snap,indent=2)+'\n')
