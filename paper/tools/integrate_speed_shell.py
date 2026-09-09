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
assert hashlib.sha256((root/'sections/speed_shell.tex').read_bytes()).hexdigest() == '6d4ed41005c59d2734a1befc41779ec63e0bd6805c3178dc42b54c9a0efae4da', 'frozen component changed; review before integration'
payload = json.loads(r'''
{
  "files": {
    "main.tex": [
      {
        "old": "one-sided quadratic-form clock with a critical amplitude-tail certificate.\nIts endpoint-uniform time bound is still missing.\n",
        "new": "one-sided quadratic-form clock with a critical amplitude-tail certificate.\nIts endpoint-uniform time bound is still missing.\nSection~\\ref{ss:section} proves cancellation on every speed shell,\nremoves speed-only contributions from the signed pairing, and derives\na depleted defect bound and speed-dependent null corrections to the form.\nThese additions are also review pending and supply no temporal producer.\n"
      },
      {
        "old": "explicitly from that new input; it does not establish the input itself.\nThe new component and its nonendpoint quotient-clock suffix await\nindependent mathematical audit. No terminal or open graph node is promoted.\n",
        "new": "explicitly from that new input; it does not establish the input itself.\nThe new component and its nonendpoint quotient-clock suffix await\nindependent mathematical audit. Section~\\ref{ss:section} additionally\nproves that the defect has zero average on every speed shell, derives\na residual after removal of speed-only functions, and exploits scalar\ncorrections that leave the signed work unchanged. The endpoint-uniform\nbound on the resulting combined rate remains unproved.\nNo terminal or open graph node is promoted.\n"
      },
      {
        "old": "\\input{sections/conformal_moment}\n\\input{sections/signed_defect}\n",
        "new": "\\input{sections/conformal_moment}\n\\input{sections/signed_defect}\n\\input{sections/speed_shell}\n"
      }
    ],
    "README.md": [
      {
        "old": "promotion of DEFECT-L4 or NS-R3. `make check-signed` runs finite algebra and\nsource checks; it is not an independent mathematical audit.\n",
        "new": "promotion of DEFECT-L4 or NS-R3. `make check-signed` runs finite algebra and\nsource checks; it is not an independent mathematical audit.\n\n\n## Speed-shell cancellation and effective defect (2026-09-06; audit pending)\n\nThe new source `sections/speed_shell.tex` proves\n`integral_{|w|>k} sigma=0` for every k>0, with an L^(3/2) flux cutoff and\nno finite-energy assumption on w. Thus sigma annihilates every L2 function\nof speed. Projecting the scalar signed-work field chi off the closed speed\nsubspace gives a measurable factor delta in [0,1] and\n`|K| <= (2/3) delta ||sigma||2 ||w||6^3`. Finite speed-shell averages\nbound the residual, converging under nested refinement.\n\nSpeed-dependent scalar corrections `h(|w|)sigma I` leave the signed work\nunchanged. Their countable form-rate infimum beta satisfies\n`0<=beta<=b_nu(B0)`. With\n`c_nu=min(3 beta, a0^3 delta^4 ||sigma||2^4/(2 nu^3))` and `L_c=integral c_nu`,\n\n    Q(t)+nu/2 integral D <= Q0 exp(L_c(t)),\n    integral ||sigma||2^4 <= E0 Y0/(32 nu) exp(Astar exp(L_c(t))).\n\nThe last implication retains the pending quotient-clock dependency.\nThe bound on L_c from arbitrary initial data is NOT proved; delta<=1 only\nreturns the old unknown fourth-power integral. No temporal derivative of\nthe moving speed projection is assumed. Full proofs, cutoff and\nmeasurability details, and the stopping point are in the source.\nThese are author-checked components, not an independent audit or promotion\nof any open claim. `make check-shell` is a finite algebra/source regression.\n"
      }
    ],
    "Makefile": [
      {
        "old": "all: main.pdf proof_map.pdf\n\nmain.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex sections/signed_defect.tex\n",
        "new": "all: main.pdf proof_map.pdf\n\nmain.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex sections/signed_defect.tex sections/speed_shell.tex\n"
      },
      {
        "old": "check-signed:\n\tpython3 tools/check_signed_defect.py --integrated\n",
        "new": "check-signed:\n\tpython3 tools/check_signed_defect.py --integrated\n\n.PHONY: check-shell\ncheck-shell:\n\tpython3 tools/check_speed_shell.py --integrated\n"
      }
    ],
    "proof_map.tex": [
      {
        "old": "\\clearpage\n\\raggedright\nGraph SHA-256: \\texttt{811490092e1c8b1a058e072d8f24a24d}\\texttt{5c24313f8589ed5834516b9e28c9347b}.\n",
        "new": "\\clearpage\n\\raggedright\nGraph SHA-256: \\texttt{377a3190407510641039a11a88d3ceb8}\\texttt{54a6627367188a7533d7335f8ef3ec21}.\n"
      },
      {
        "old": "\n\\textbf{Manuscript labels:} \\texttt{sd:cancellation}, \\texttt{sd:improved}, \\texttt{sd:form-clock}, \\texttt{sd:missing-bound-consumer}, \\texttt{sd:tail}.\n",
        "new": "\n\\textbf{Manuscript labels:} \\texttt{sd:cancellation}, \\texttt{sd:improved}, \\texttt{sd:form-clock}, \\texttt{sd:missing-bound-consumer}, \\texttt{sd:tail}.\n\\clearpage\\section*{Review-pending component: Speed-shell cancellation and effective defect}\n\\textbf{Not a promoted claim or an arbitrary-data producer.}\n\nauthor-checked-independent-audit-pending. Exact shell cancellation, speed-only projection residual, measurable depleted defect and null-corrected form bounds; pending signed-work and quotient-clock dependencies explicit, no arbitrary-data temporal producer or node promotion.\n\n\\textbf{Evidence:} \\texttt{research/evidence/2026-09-06-speed-shell.md}.\n\n\\textbf{Manuscript labels:} \\texttt{ss:shell}, \\texttt{ss:residual}, \\texttt{ss:clock}, \\texttt{ss:gauge}, \\texttt{ss:consumer}.\n"
      }
    ]
  },
  "guards": {
    "proof_map.tex": {
      "base": "a3bbda9851ee7d82e2bfb21e9860995cdb06ad2e56f0da1076daadd315c35d35",
      "target": "c2800a7b1e52a2fa2f176e49763681bb1308cec8c722daec5b4800c9de83ca7b"
    }
  }
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
