#!/usr/bin/env python3
from pathlib import Path
import shutil

root=Path.cwd()
src=Path('/tmp/small-bridge-purity-wave')
rel='research/evidence/2026-09-12-small-bridge-purity-wall.md'
target=root/rel
assert not target.exists()
target.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(src/rel,target)

p=root/'PLAN.md'
text=p.read_text()
assert 'source_small_bridge_purity:' not in text
needle='source_even_feedback_critical_form: author-weighted-Hessian-absorption-small-L3-input-not-produced\n'
assert needle in text
text=text.replace(needle,needle+'source_small_bridge_purity: fixed-horizon-small-data-bridge-retains-order-epsilon-old-grade-purity-fails\n',1)
old='''The first remaining constructive dependency is now **one-history production
of critical-small even feedback and quantitative weighted low-sector control**,
using the J_gap,B+J_form,Z consumer rather than a norm-only Lipschitz-action
bound. Old modes and cross-label products must remain in the same physical
solution. Another local ladder, isolated spectrum or exact reset does not
supply this input. The localized full-history adjoint and arbitrary-data
positive producer remain unresolved alternatives. UE1 and NS-R3 remain open.
'''
assert old in text
new='''The first remaining constructive dependency is now **one-history production
of critical-small even feedback and quantitative weighted low-sector control**,
using the J_gap,B+J_form,Z consumer rather than a norm-only Lipschitz-action
bound. Old modes and cross-label products must remain in the same physical
solution. Another local ladder, isolated spectrum or exact reset does not
supply this input.

The existing fixed-horizon six-mode bridge cannot itself produce that purity.
Its complete nonlinear endpoint is analytic in the common ancestor amplitude
`epsilon`; the entire first-order term remains in physical grade `m`, while the
new `2m` parent sector starts at quadratic order. Thus, with cutoff at `2|m|`,

    ||Pi_(|grade|<2|m|) u_epsilon(T)||_2 / ||u_epsilon(T)||_2 -> 1

for every fixed positive reference horizon as `epsilon->0`. The required
`exp(-cL)` low-sector purity therefore forces a genuinely nonperturbative
**depletion/turnover** (or a different consumer), not another small-data
Taylor/IFT stage. Exact gap reset and passive parent reuse are already excluded.
See `research/evidence/2026-09-12-small-bridge-purity-wall.md`.

This closes the perturbative cleanup mechanism. The live constructive object is
now an approximate nonperturbative turnover that transfers old grade `m` into
the next `2m` state while retaining the entire inherited field. The terminal
localized turnover contract still requires, at half scale, gain
`2<g<=2sqrt(2)`, original unforced NS evolution, full-state closure and one-data
iteration. No such turnover is certified. The nonprincipal full-history adjoint
and arbitrary-data positive producer remain unresolved alternatives. UE1 and
NS-R3 remain open.
'''
text=text.replace(old,new,1)
# Repair a concurrent editorial duplication without changing mathematical status.
text=text.replace('The\nThe pinned target build now replays','The pinned target build now replays',1)
p.write_text(text)
print('integrated small-bridge purity wall')
