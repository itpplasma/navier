#!/usr/bin/env python3
from pathlib import Path
import json, subprocess
root=Path.cwd(); plan=root/'PLAN.md'; p=plan.read_text()
needle='source_adjoint_strain_sign: no-nonzero-solenoidal-sign-definite-nonlinear-certificate\n'
insert=needle+'source_adjoint_principal_stress_dual: high-frequency-solenoidal-force-has-order-one-over-k-symmetric-stress-potential\n'
assert p.count(needle)==1 and 'source_adjoint_principal_stress_dual:' not in p
p=p.replace(needle,insert,1)
anchor='''A terminal adjoint attack must therefore control the **magnitude** of the\nnonlinear strain budget or exploit source-specific correction structure. The\nnext exact discriminator tests the principal high-frequency source force in\nthat same strain-dual norm. Grade-changing/nonparent late regeneration remains\nthe constructive alternative. UE1 and the terminal claim remain open.\n'''
replacement='''The second complete-adjoint discriminator closes the principal-carrier\nshortcut. For a solenoidal Fourier force coefficient `f` at nonzero `k`, the\nsymmetric symbol\n\n    H=(k tensor f+f tensor k)/|k|^2\n\nsatisfies `H k=f`, `|H|_F=sqrt(2)|f|/|k|`, and\n`H:sym(k tensor z)=f.z`. Thus the principal high-frequency force is already a\nsymmetric divergence with `O(1/|k|)` stress size in exactly the strain-dual\nvariable used by the nonlinear correction term. High carrier frequency does\nnot create a favorable adjoint mismatch; any terminal obstruction must come\nfrom localization/envelope, low-frequency, or genuinely full-history effects.\nSee `research/evidence/2026-09-12-adjoint-principal-stress-dual.md`.\n\nThis is a second serious return to simple complete-adjoint mechanisms: sign\ncontrol fails structurally and the principal carrier is strain-dual cheap. Per\nthe diversification rule the next primary attack switches to the constructive\n**grade-changing/nonparent late-regeneration** route. The complete adjoint stays\navailable only through nonprincipal localized whole-history structure. UE1 and\nthe terminal claim remain open.\n'''
assert p.count(anchor)==1; plan.write_text(p.replace(anchor,replacement,1))
cp=root/'research/game/controls.json'; controls=json.loads(cp.read_text())
assert not any(c['id']=='adjoint-principal-stress-dual' for c in controls['controls'])
controls['controls'].append({'id':'adjoint-principal-stress-dual','scope':'principal nonzero Fourier mode of projected solenoidal source force','evidence':'research/evidence/2026-09-12-adjoint-principal-stress-dual.md','rigor':'exact-Fourier-symbol-author-proof','observation':{'symmetric_inverse_divergence':'Ghat=-i(k⊗f+f⊗k)/|k|^2','stress_norm':'sqrt(2)|f|/|k|','pairs_with_symmetric_strain':True,'principal_high_frequency_adjoint_obstruction':False}})
cp.write_text(json.dumps(controls,indent=2)+'\n')
base=root/'research/game/models/baseline.py'; b=base.read_text()
needle_b="    'adjoint-strain-sign-wall': {'solenoidal_strain_trace': 0, 'nonzero_strain_pointwise_indefinite': True, 'zero_strain_L2_solenoidal_adjoint': 'zero', 'sign_only_nonlinear_certificate': False},\n"
insert_b=needle_b+"    'adjoint-principal-stress-dual': {'symmetric_inverse_divergence': 'Ghat=-i(k⊗f+f⊗k)/|k|^2', 'stress_norm': 'sqrt(2)|f|/|k|', 'pairs_with_symmetric_strain': True, 'principal_high_frequency_adjoint_obstruction': False},\n"
assert b.count(needle_b)==1 and "'adjoint-principal-stress-dual'" not in b; base.write_text(b.replace(needle_b,insert_b,1))
def blob(path): return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()
sp=root/'research/game/snapshot.json'; snap=json.loads(sp.read_text()); snap['authoritative_sources']['PLAN.md']=blob(plan); ev=root/'research/evidence/2026-09-12-adjoint-principal-stress-dual.md'; snap['authoritative_sources']['research/evidence/2026-09-12-adjoint-principal-stress-dual.md']=blob(ev); snap['active_frontier']='grade-changing/nonparent late regeneration as primary constructive attack; nonprincipal localized full-history adjoint remains alternative'; sp.write_text(json.dumps(snap,indent=2)+'\n')
