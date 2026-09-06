#!/usr/bin/env python3
"""Apply source-guarded manuscript/status edits; never promote proof claims.

All anchors are validated before writing. Unrelated, nonoverlapping document
edits are preserved; a changed authoritative graph/map requires regeneration.
This is mechanical integration, not an independent mathematical audit.
"""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true', help='verify without writing')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
frozen = root/'research/evidence/2026-09-06-signed-defect.md'
assert hashlib.sha256(frozen.read_bytes()).hexdigest() == '653b1903b7075f3a11f9d1b947b5e826a3dcefe4f9bd793b4507e4d08e9c6456', 'frozen evidence/source changed; review integration first'
payload = json.loads(r'''
{
  "files": {
    "PLAN.md": [
      {
        "old": "paper_status: active-paper-proof-work-2026-09-06\npaper_repo: writable-authorized-2026-09-06\nexternal_deps: permitted-if-no-axioms-beyond-mathlib\nactive_task: conformal-moment-audit-and-arbitrary-data-temporal-producer\npublic_release: false\n```\n\n",
        "new": "paper_status: active-paper-proof-work-2026-09-06\npaper_repo: writable-authorized-2026-09-06\nexternal_deps: permitted-if-no-axioms-beyond-mathlib\nactive_task: signed-form-clock-audit-and-arbitrary-data-temporal-producer\npublic_release: false\n```\n\n"
      },
      {
        "old": "Formal phases, the privacy boundary and all graph node kinds are unchanged.\nFull derivations, source checks and audit obligations are indexed in\n`research/evidence/2026-09-06-conformal-moment.md`.\n",
        "new": "Formal phases, the privacy boundary and all graph node kinds are unchanged.\nFull derivations, source checks and audit obligations are indexed in\n`research/evidence/2026-09-06-conformal-moment.md`.\n\n\n## Signed defect: exact cancellation and one-sided missing-bound target (2026-09-06)\n\nFrozen source: `navier-paper` `a14114b8527630a469e7afdea1d2ec53bacfe8f5`,\n`sections/signed_defect.tex`. Status: author-checked; independent audit\npending. Evidence: `research/evidence/2026-09-06-signed-defect.md`.\n\nThe cutoff identity `integral sigma |w|^3 = 0` gives\n`K = -integral V^T S(u) V = integral V^T B0 V`, where\n`B0=(R_i R_j sigma)+sigma I/3`. Trace-free algebra gives the direct bound\n`|K| <= (2/3) ||sigma||2 ||w||6^3` and improves the defect Gronwall\ncoefficient from `(81/32) C6^4 a0^3` to `a0^3/2`, `a0=9 C_S^2/8`.\nThe exponent four remains; no critical estimate follows just by shrinking\nthis coefficient. These proofs do not need the moment extension.\n\nA one-sided variational rate is the positive part of the supremum of\n`[integral psi^T B0 psi - (4 nu/9) integral |grad psi|^2]/integral |psi|^2`.\nThe source proves its measurability, finiteness and exact bounds. It gives\n`Q'+nu D/2 <= 3 b_nu Q` and hence the explicit missing-integral consumer\n\n    integral_0^t ||sigma||2^4\n    <= E0 Y0/(32 nu) exp(Astar exp(3 integral_0^t b_nu)),\n    Astar = 8 C_S^3 C9^3 Q0/(3 nu^3).\n\nThe last implication uses the separately pending direct quotient clock.\nAn integrable amplitude cutoff for the positive largest eigenvalue of B0,\nwith an L^(3/2)-small excess tail, is also sufficient. Both form and\namplitude clocks are critical. No eigenfunction or spectral theorem is\nassumed, and no theorem about the velocity strain is applied to B0.\n\n**Next positive producer:** derive an input-only bound on\n`sup_{t<min(H,Tstar)} integral_0^t b_nu(B0(s)) ds`, or an explicit integrable\namplitude certificate, from the vector equation. The existing upper bound\n`b_nu <= a0^3 ||sigma||2^4/(6 nu^3)` runs in the wrong direction to supply\nthat producer from energy. The evidence records the exact stopping point\nand a bare-budget scalar diagnostic, not a singular PDE solution.\n\nThis replaces the active task with signed-form evolution and independent\ncomponent audit; it does not declare the earlier moment audit complete.\nThe terminal claim and HIGH-PRESSURE, HIGH-STRAIN and DEFECT-L4 stay open.\nAll 29 existing graph nodes and formal statuses are preserved; the new\nresult is recorded only as a pending supplement. A classical-gradient\nbound remains a legitimate research target, not an \"unusable\" route merely\nbecause it would suffice for continuation.\n"
      }
    ],
    "README.md": [
      {
        "old": "The [literature dossier](literature/README.md) records source scope and\nverification limits. The companion `../navier-paper` contains the manuscript\nand clickable proof map. Its private GitHub repository is the manuscript\nauthority; both repositories use signed commits and local builds. The former\nNavier Overleaf project was deleted at the owner’s request on 2026-09-05.\nThe independently audited argument remains conditional on signed\nhigh-frequency pressure control. No solution or completed formalization is\n",
        "new": "The [literature dossier](literature/README.md) records source scope and\nverification limits. The companion `../navier-paper` contains the manuscript\nand clickable proof map. Its private GitHub repository is the manuscript\nauthority; the current owner-authorized task also permits unsigned commits.\nDocument builds and claim audits are recorded separately. The former\nNavier Overleaf project was deleted at the owner’s request on 2026-09-05.\nThe independently audited argument remains conditional on signed\nhigh-frequency pressure control. No solution or completed formalization is\n"
      },
      {
        "old": "critical temporal producer and NS-R3 remain unproved. Independent audit is\npending, no formal status changes, and the graph records a separate pending\ncomponent instead of promoting a claim. `PLAN.md` remains the live authority.\n",
        "new": "critical temporal producer and NS-R3 remain unproved. Independent audit is\npending, no formal status changes, and the graph records a separate pending\ncomponent instead of promoting a claim. `PLAN.md` remains the live authority.\n\n\n## Signed-defect missing-bound reduction (2026-09-06)\n\nThe frozen component `navier-paper/sections/signed_defect.tex` proves an\nexact scalar cancellation and a signed trace-free Hessian representation.\nIt removes the Leray factor from the fourth-power coefficient and supplies\na one-sided quadratic-form clock with an explicit critical amplitude-tail\ncertificate. See `research/evidence/2026-09-06-signed-defect.md`.\n\nThe original defect integral is now bounded explicitly in terms of that\nform clock. Its arbitrary-data, endpoint-uniform time bound is still\n**unproved**; no critical or terminal claim is promoted. The source is\nauthor-checked and awaits independent mathematical audit. The main\nmanuscript and generated map include this pending component; `PLAN.md`\nrecords the remaining vector-evolution target.\n"
      }
    ],
    "docs/proof.md": [
      {
        "old": "finiteness statements alone do not imply it. No open producer is promoted.\nSee `research/evidence/2026-09-06-conformal-moment.md` for the frozen source,\nconstants, primary-source attribution and independent-review obligations.\n",
        "new": "finiteness statements alone do not imply it. No open producer is promoted.\nSee `research/evidence/2026-09-06-conformal-moment.md` for the frozen source,\nconstants, primary-source attribution and independent-review obligations.\n\n\n## Signed defect and one-sided form clock (2026-09-06; review pending)\n\nThe new manuscript section `sections/signed_defect.tex` proves, without\nassuming moments or finite L2 energy of the representative,\n\n    integral sigma |w|^3 = 0,\n    K = -integral V^T S(u) V = integral V^T B0 V,\n    |K| <= (2/3) ||sigma||2 ||w||6^3,\n    Q' + (nu/2) D_Q <= a0^3 ||sigma||2^4 Q/(2 nu^3),\n    B0=(R_i R_j sigma)+sigma I/3,  a0=9 C_S^2/8.\n\nThe cutoff identity, zero-set chain rule and trace-free constants are\nwritten in full. This improves the old coefficient, not its fourth-power\ntime exponent. The old audited inequality is preserved as such.\n\nA measurable nonnegative rate b_nu is defined by the positive Rayleigh\nsupremum of B0 minus `(4 nu/9)` times the Dirichlet form. One has\n\n    Q(t)+(nu/2) integral_0^t D_Q <= Q0 exp(3 integral_0^t b_nu),\n    integral_0^t ||sigma||2^4\n      <= E0 Y0/(32 nu) exp(Astar exp(3 integral_0^t b_nu)),\n    Astar=8 C_S^3 C9^3 Q0/(3 nu^3).\n\nThe second inequality uses the separately review-pending quotient clock\nand the accepted energy identity. An explicit L^(3/2)-small amplitude-tail\ncertificate bounds b_nu from above. The clocks scale critically; their\nlocal finiteness is not a bound at a putative maximal time.\n\nThe missing arbitrary-data producer is still missing. Its sharpened target\nis an input-only finite bound on the accumulated signed form rate. The\navailable `b_nu <= a0^3 ||sigma||2^4/(6 nu^3)` cannot supply it because\nthe integral on its right is the original unknown. All graph node kinds\nremain unchanged. See `research/evidence/2026-09-06-signed-defect.md` for\nfrozen hashes, primary-source distinctions, the scalar-budget diagnostic,\nmechanical-check scope and required independent mathematical audit.\n"
      }
    ],
    "docs/proof-graph.yaml": [
      {
        "old": "    evidence: research/evidence/2026-09-06-conformal-moment.md\n    paper_labels: ['cm:covariance', 'cm:inverted-h1', 'cm:snapshot', 'cm:moment', 'cm:spacetime', 'cm:scaling-test']\n    scope: Finite-energy representative and L3/2 defect under a weighted-gradient hypothesis, proved at every classical time with input-only integrated moment budgets for Schwartz data; supercritical time control only, no arbitrary-data critical producer or node promotion.\n",
        "new": "    evidence: research/evidence/2026-09-06-conformal-moment.md\n    paper_labels: ['cm:covariance', 'cm:inverted-h1', 'cm:snapshot', 'cm:moment', 'cm:spacetime', 'cm:scaling-test']\n    scope: Finite-energy representative and L3/2 defect under a weighted-gradient hypothesis, proved at every classical time with input-only integrated moment budgets for Schwartz data; supercritical time control only, no arbitrary-data critical producer or node promotion.\n  - id: SIGNED-DEFECT-FORM-CLOCK\n    title: Signed defect and one-sided form clock\n    status: author-checked-independent-audit-pending\n    source_repository: itpplasma/navier-paper\n    source_commit: a14114b8527630a469e7afdea1d2ec53bacfe8f5\n    source_path: sections/signed_defect.tex\n    source_sha256: 2e0a101a00a9a9170b0d750a41876a8f556af747184d509dc22a6b5eda1b6a27\n    evidence: research/evidence/2026-09-06-signed-defect.md\n    paper_labels: ['sd:cancellation', 'sd:improved', 'sd:form-clock', 'sd:missing-bound-consumer', 'sd:tail']\n    scope: Exact signed cancellation, smaller fourth-power coefficient and an explicit conditional defect bound from a critical one-sided form clock; independent audit pending, no arbitrary-data clock bound or graph-node promotion.\n"
      }
    ]
  },
  "guards": {
    "docs/proof-graph.yaml": {
      "base": "04632a86e3cc0cb725d710d800b492de3dc2a5abdf73d2f6880f6ca7dbf4e8e2",
      "target": "811490092e1c8b1a058e072d8f24a24d5c24313f8589ed5834516b9e28c9347b"
    }
  }
}
''')
allowed = {'docs/proof.md', 'PLAN.md', 'docs/proof-graph.yaml', 'README.md'}
changes = {}
for relative, operations in payload['files'].items():
    assert relative in allowed, f'unexpected integration path: {relative}'
    path = root/relative
    original = path.read_text()
    text = original
    guard = payload['guards'].get(relative)
    if guard:
        current = hashlib.sha256(original.encode()).hexdigest()
        if current == guard['target']:
            continue
        assert current == guard['base'], f'concurrent graph/map edits in {relative}; regenerate from research authority'
    for item in operations:
        old, new = item['old'], item['new']
        assert old and new, 'empty source anchor'
        if text.count(new) == 1:
            continue
        assert text.count(old) == 1, f'missing/ambiguous anchor in {relative}: {old[:90]!r}'
        text = text.replace(old, new, 1)
    if guard:
        assert hashlib.sha256(text.encode()).hexdigest() == guard['target'], 'generated graph/map digest mismatch'
    if text != original:
        changes[path] = text
if args.check:
    assert not changes, 'pending integration: ' + ', '.join(str(p.relative_to(root)) for p in changes)
else:
    for path, text in changes.items():
        path.write_text(text)
print('PASS: guarded signed-defect integration ' + ('present' if not changes else 'applied'))
print('Scope: mechanical source integration only; arbitrary-data producer remains unproved.')
