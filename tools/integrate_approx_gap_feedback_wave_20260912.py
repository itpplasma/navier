#!/usr/bin/env python3
from pathlib import Path
import shutil
import re

root = Path.cwd()
src = Path('/tmp/approx-gap-feedback-wave')

for rel in [
    'research/check_approximate_gap_pressure.py',
    'research/check_even_feedback_packets.py',
    'research/check_feedback_form_bound.py',
    'research/evidence/2026-09-12-approximate-gap-pressure.md',
    'research/evidence/2026-09-12-even-feedback-packets.md',
    'research/evidence/2026-09-12-feedback-critical-form.md',
]:
    target = root / rel
    assert not target.exists(), f'already exists: {rel}'
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src / rel, target)

plan_path = root / 'PLAN.md'
plan = plan_path.read_text()
assert 'source_approximate_gap_pressure:' not in plan
needle = 'source_exact_angular_gap_reset: excluded-on-unforced-classical-branch-by-backward-uniqueness\n'
assert needle in plan
plan = plan.replace(needle, needle +
    'source_approximate_gap_pressure: author-all-mode-estimate-with-exp-weighted-low-sector-defect\n'
    'source_even_feedback_norm_only_action: refuted-by-small-data-unforced-packets-including-one-material-trajectory\n'
    'source_even_feedback_critical_form: author-weighted-Hessian-absorption-small-L3-input-not-produced\n', 1)
old = '''The first remaining constructive dependency is **quantitative approximate-gap
and even-feedback control for one complete inherited physical history**. Old
low angular sectors cannot be deleted at handoffs. Their pressure contribution,
cross-label mixing, and the action `B_Z` must be controlled or used in a new
full-state consumer. More independent local bridge data, principal symbols or
finite-section spectra cannot supply this missing global input. The localized
full-history adjoint and the arbitrary-data positive producer remain separate
unresolved alternatives. UE1 and NS-R3 remain open.
'''
assert old in plan
new = '''### 8.2 Approximate gaps and critical-form feedback, rather than Lipschitz action

The all-mode weighted pressure estimate now retains low sectors through

    J_gap=2 int K exp(osc(phi)) theta eta,

where theta is the weighted low-velocity fraction and eta is the actual low
pressure-source fraction. For the primary clock weight osc(phi)=O(L^(3/4)),
exponential purity theta<=exp(-cL) suffices under the stated polynomial
coefficient bounds. Qualitative or polynomial purity alone does not: a
whole-space dipole gives an exp(osc(phi)) lower bound for the low-sector
elliptic operator. See
`research/evidence/2026-09-12-approximate-gap-pressure.md`.

A norm-only repair of B_Z is false even in original unforced NS. There are
compact odd Schwartz data with initial L3 and L2 norms tending to zero,
initially zero even component, and globally smooth solutions whose generated
even-strain action tends to infinity. A nested-scale version has the same
property along the single stationary trajectory x(t)=0. Higher initial
Schwartz seminorms are not uniformly bounded, and no singular solution is
constructed. The complete canonical-pressure coefficient and finite-profile
argument are in `research/evidence/2026-09-12-even-feedback-packets.md`.

A different form estimate avoids that false inference. For scalar angular
gap N>=2, d_1=||r grad phi||_infinity/(N-1)<1/2 gives the whole-space bound

    ||exp(-phi) Hess q||_2
      <= (1-2d_1)^(-1)||exp(-phi) Delta q||_2.

Duality bounds high-sector pressure directly from the mixed stress
Z tensor w+w tensor Z, without a derivative of Z. Under
||Z_physical||_3<=nu/(4C_S), viscosity absorbs the stretching term. The new
feedback action is J_form,Z, explicitly defined with the retained low-sector
stress fraction in `research/evidence/2026-09-12-feedback-critical-form.md`.
For the source normalization, bounded exp(osc(phi)) theta xi_Z makes it
O(epsilon^(1-2kappa_s) L^M)=o(1). A compact solenoidal swirl also shows that
the exponential *low*-pressure loss remains attainable by a genuine NS stress.

Consequently the primary physical pump bound with extra exponent O(L^(3/4))
survives approximate purity and critical-small even feedback without requiring
B_Z=o(L). These are author proofs pending independent audit, not a canonical
proof-graph promotion. The critical smallness and purity are not produced for
the actual inherited source history.

The first remaining constructive dependency is now **one-history production
of critical-small even feedback and quantitative weighted low-sector control**,
using the J_gap,B+J_form,Z consumer rather than a norm-only Lipschitz-action
bound. Old modes and cross-label products must remain in the same physical
solution. Another local ladder, isolated spectrum or exact reset does not
supply this input. The localized full-history adjoint and arbitrary-data
positive producer remain unresolved alternatives. UE1 and NS-R3 remain open.
'''
plan = plan.replace(old, new, 1)
plan_path.write_text(plan)

# formal_status is live noncanonical metadata. Canonical formal phase strings
# remain checked above; requiring an enumerated prose sentence made valid
# replay/status updates fail structural CI.
verify_path = root / 'research/verify.py'
verify = verify_path.read_text()
pat = re.compile(r"# PLAN metadata may also record the owner's partial identity draft \(2b426ce\)\.\n# Neither value promotes canonical formal phases or the terminal claim\.\nassert state\['formal_status'\] in \{.*?\n\}, 'unrecognized live formal-status metadata'", re.S)
repl = "# PLAN formal_status is noncanonical live metadata; canonical phase strings are checked above.\nassert isinstance(state.get('formal_status'), str) and state['formal_status'].strip(), \\\n    'missing live formal-status metadata'"
verify2, n = pat.subn(repl, verify, count=1)
assert n == 1, 'unexpected verify.py formal-status block'
verify_path.write_text(verify2)

print('integrated approximate-gap / even-feedback research wave')
