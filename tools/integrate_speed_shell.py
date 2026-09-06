#!/usr/bin/env python3
"""Guarded source integration only; no mathematical claim is promoted."""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
assert hashlib.sha256((root/'research/evidence/2026-09-06-speed-shell.md').read_bytes()).hexdigest() == '86b8a0f13352fa1c55bdf60338f2c6ca49d8e0527fd716d9b319c45cbb8f1114', 'frozen component changed; review before integration'
payload = json.loads(r'''
{
  "files": {
    "PLAN.md": [
      {
        "old": "paper_repo: writable-authorized-2026-09-06\nexternal_deps: permitted-if-no-axioms-beyond-mathlib\nactive_task: signed-form-clock-audit-and-arbitrary-data-temporal-producer\n",
        "new": "paper_repo: writable-authorized-2026-09-06\nexternal_deps: permitted-if-no-axioms-beyond-mathlib\nactive_task: speed-shell-temporal-producer-and-independent-component-audit\n"
      },
      {
        "old": "bound remains a legitimate research target, not an \"unusable\" route merely\nbecause it would suffice for continuation.\n",
        "new": "bound remains a legitimate research target, not an \"unusable\" route merely\nbecause it would suffice for continuation.\n\n\n## Speed-shell checkpoint and remaining temporal producer (2026-09-06)\n\nFrozen paper source: `5643f3e53ce837896fdd69247c3972ba4180ebfa`,\n`sections/speed_shell.tex`; evidence:\n`research/evidence/2026-09-06-speed-shell.md`. Author-checked, independently\nunaudited; no graph node or formal phase is promoted.\n\nThe defect now has a proved zero average on every positive speed shell,\nnot only against the cubic speed. Removing all L2 functions of speed from\nthe scalar signed-work field yields a measurable delta in [0,1] and the\nbound `|K| <= (2/3) delta ||sigma||2 ||w||6^3`. Finite shell averages give\nexplicit residual upper bounds. Scalar corrections `h(|w|)sigma I` leave\nsigned work unchanged, giving a measurable form infimum beta<=b_nu(B0).\nThe minimum rate\n`c_nu=min(3 beta, a0^3 delta^4 ||sigma||2^4/(2 nu^3))` therefore suffices;\nits integral L_c gives the explicit original-defect consumer\n`integral ||sigma||2^4 <= E0 Y0/(32 nu) exp(Astar exp(L_c))`.\nThe final implication still uses the independently pending quotient clock.\n\nThe missing positive producer is an input-only bound on L_c uniformly below\nmin(H,Tstar), or a bound on one of the earlier sufficient rates. This has\nnot been obtained. Replacing delta by one returns the original unknown;\nthe energy/moment comparison does not upgrade its time exponent. The speed\nprojection and minimizing correction must not be differentiated without a\nnew regularity theorem. Critical scaling is unchanged. The source provides\nfull spatial proofs and a conditional suffix, not a completed Navier--Stokes\nproof or a strict separation of actual-branch finiteness conditions.\n\nNext mathematical work: independently audit this and predecessor components,\nthen derive an actual vector-evolution bound exploiting the shell cancellation.\nHIGH-PRESSURE, HIGH-STRAIN, DEFECT-L4 and NS-R3 remain open. Preserve all\nexisting formal authorizations, privacy restrictions and historical evidence.\n"
      }
    ],
    "README.md": [
      {
        "old": "manuscript and generated map include this pending component; `PLAN.md`\nrecords the remaining vector-evolution target.\n",
        "new": "manuscript and generated map include this pending component; `PLAN.md`\nrecords the remaining vector-evolution target.\n\n\n## Speed-shell cancellation (2026-09-06; independent audit pending)\n\nThe paper now derives cancellation on every positive speed shell, a\nmeasurable residual after removing speed-only functions, and scalar\ncorrections that leave signed work unchanged. The resulting effective-defect\nand optimized form rates do not exceed their earlier counterparts.\nTheir endpoint-uniform time bound is still unproved. Full evidence and the\nprecise failed closure are in `research/evidence/2026-09-06-speed-shell.md`;\n`PLAN.md` remains the sole live status. No open or formal claim is promoted.\n"
      }
    ],
    "docs/proof.md": [
      {
        "old": "frozen hashes, primary-source distinctions, the scalar-budget diagnostic,\nmechanical-check scope and required independent mathematical audit.\n",
        "new": "frozen hashes, primary-source distinctions, the scalar-budget diagnostic,\nmechanical-check scope and required independent mathematical audit.\n\n\n## Speed-shell cancellation and effective defect (2026-09-06; audit pending)\n\nThe new source `sections/speed_shell.tex` proves\n`integral_{|w|>k} sigma=0` for every k>0, with an L^(3/2) flux cutoff and\nno finite-energy assumption on w. Thus sigma annihilates every L2 function\nof speed. Projecting the scalar signed-work field chi off the closed speed\nsubspace gives a measurable factor delta in [0,1] and\n`|K| <= (2/3) delta ||sigma||2 ||w||6^3`. Finite speed-shell averages\nbound the residual, converging under nested refinement.\n\nSpeed-dependent scalar corrections `h(|w|)sigma I` leave the signed work\nunchanged. Their countable form-rate infimum beta satisfies\n`0<=beta<=b_nu(B0)`. With\n`c_nu=min(3 beta, a0^3 delta^4 ||sigma||2^4/(2 nu^3))` and `L_c=integral c_nu`,\n\n    Q(t)+nu/2 integral D <= Q0 exp(L_c(t)),\n    integral ||sigma||2^4 <= E0 Y0/(32 nu) exp(Astar exp(L_c(t))).\n\nThe last implication retains the pending quotient-clock dependency.\nThe bound on L_c from arbitrary initial data is NOT proved; delta<=1 only\nreturns the old unknown fourth-power integral. No temporal derivative of\nthe moving speed projection is assumed. Full proofs, cutoff and\nmeasurability details, and the stopping point are in the source.\nThese are author-checked components, not an independent audit or promotion\nof any open claim. The paper target `make check-shell` is a finite algebra/source regression.\n\nEvidence: `research/evidence/2026-09-06-speed-shell.md`.\n"
      }
    ],
    "docs/proof-graph.yaml": [
      {
        "old": "    paper_labels: ['sd:cancellation', 'sd:improved', 'sd:form-clock', 'sd:missing-bound-consumer', 'sd:tail']\n    scope: Exact signed cancellation, smaller fourth-power coefficient and an explicit conditional defect bound from a critical one-sided form clock; independent audit pending, no arbitrary-data clock bound or graph-node promotion.\n",
        "new": "    paper_labels: ['sd:cancellation', 'sd:improved', 'sd:form-clock', 'sd:missing-bound-consumer', 'sd:tail']\n    scope: Exact signed cancellation, smaller fourth-power coefficient and an explicit conditional defect bound from a critical one-sided form clock; independent audit pending, no arbitrary-data clock bound or graph-node promotion.\n  - id: SPEED-SHELL-EFFECTIVE-DEFECT\n    title: Speed-shell cancellation and effective defect\n    status: author-checked-independent-audit-pending\n    source_repository: itpplasma/navier-paper\n    source_commit: 5643f3e53ce837896fdd69247c3972ba4180ebfa\n    source_path: sections/speed_shell.tex\n    source_sha256: 6d4ed41005c59d2734a1befc41779ec63e0bd6805c3178dc42b54c9a0efae4da\n    evidence: research/evidence/2026-09-06-speed-shell.md\n    paper_labels: ['ss:shell', 'ss:residual', 'ss:clock', 'ss:gauge', 'ss:consumer']\n    scope: Exact shell cancellation, speed-only projection residual, measurable depleted defect and null-corrected form bounds; pending signed-work and quotient-clock dependencies explicit, no arbitrary-data temporal producer or node promotion.\n"
      }
    ]
  },
  "guards": {}
}
''')
changes = {}
for relative, operations in payload['files'].items():
    path = root/relative
    original = path.read_text()
    text = original
    guard = payload['guards'].get(relative)
    if guard:
        current = hashlib.sha256(original.encode()).hexdigest()
        if current == guard['target']:
            continue
        assert current == guard['base'], 'concurrent map edit; regenerate from authoritative research graph'
    for operation in operations:
        old, new = operation['old'], operation['new']
        if text.count(new) == 1:
            continue
        assert text.count(old) == 1, f'missing or ambiguous integration anchor in {relative}: {old[:70]!r}'
        text = text.replace(old, new, 1)
    if guard:
        assert hashlib.sha256(text.encode()).hexdigest() == guard['target'], 'map digest mismatch'
    if text != original:
        changes[path] = text
if args.check:
    assert not changes, 'pending integration: '+', '.join(str(p.relative_to(root)) for p in changes)
else:
    for path, text in changes.items():
        path.write_text(text)
print('PASS: speed-shell source integration '+('present' if not changes else 'applied'))
print('Scope: document integrity only; independent audit and arbitrary-data temporal producer remain pending.')
