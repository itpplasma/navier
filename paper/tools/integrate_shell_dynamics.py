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
assert hashlib.sha256((root/'sections/shell_dynamics.tex').read_bytes()).hexdigest() == '66f3ff185f220e8be874ea2090bc982abe42b4208ee093dc6799b5ee015e5677', 'frozen component changed; review before integration'
payload = json.loads(r'''
{
  "files": {
    "main.tex": [
      {
        "old": "\\input{sections/speed_shell}\n",
        "new": "\\input{sections/speed_shell}\n\\input{sections/shell_dynamics}\n"
      },
      {
        "old": "These additions are also review pending and supply no temporal producer.\n",
        "new": "These additions are also review pending and supply no temporal producer.\nSection~\\ref{st:section} supplies natural-variable time regularity and an\nexact evolution law for finite regularized shell residuals; its endpoint\ndriver estimate is not closed and independent review is pending.\n"
      },
      {
        "old": "No terminal or open graph node is promoted.\n",
        "new": "No terminal or open graph node is promoted.\nSection~\\ref{st:section} now justifies differentiation of a finite,\nregularized shell residual through the natural variable. This does not\njustify differentiation of the full moving projection or bound the\nnew evolution drivers uniformly at the endpoint.\n"
      }
    ],
    "README.md": [
      {
        "old": "ent-clock dependency.\nThe bound on L_c from arbitrary initial data is NOT proved; delta<=1 only\nreturns the old unknown fourth-power integral. No temporal derivative of\nthe moving speed projection is assumed. Full proofs, cutoff and\nmeasurability details, and the stopping point are in the source.\nThese are author-checked components, not an independent audit or promotion\nof any open claim. `make check-shell` is a finite algebra/source regression.\n",
        "new": "ent-clock dependency.\nThe bound on L_c from arbitrary initial data is NOT proved; delta<=1 only\nreturns the old unknown fourth-power integral. No temporal derivative of\nthe moving speed projection is assumed. Full proofs, cutoff and\nmeasurability details, and the stopping point are in the source.\nThese are author-checked components, not an independent audit or promotion\nof any open claim. `make check-shell` is a finite algebra/source regression.\n\n## Natural-variable time regularity and regularized shell dynamics (2026-09-06)\n\n`sections/shell_dynamics.tex` proves, with independent audit pending,\n\n    ||V1-V0||2^2 <= 9/8 integral (|w0|+|w1|)|f1-f0+g|^2,\n\nfor every admissible gradient g. On each compact classical interval this\ngives V in W^(1,infinity)(time;L2) and the pressure-free bound\n\n    ||V_t||2^2 <= 9/4 integral |w| |nu Delta u-(u dot grad)u|^2.\n\nFinite smooth speed features with a positive ridge penalty give an exactly\ndifferentiable residual R, retain `K=<sigma,residual>`, and decrease to the\nfull speed-projection residual at each fixed time. The source proves its\nexact evolution and quantitative derivative bound in the correct dual\nspaces. It does not differentiate the sharp moving projection.\n\nThis closes a fixed-regularization temporal-calculus obstacle, not the\narbitrary-data fourth-power bound: endpoint control of the derivative\ndriver and uniformity as the ridge penalty vanishes remain unproved.\nNo graph node or predecessor audit is promoted. `make check-dynamics`\nchecks finite algebra and source integrity, not mathematical correctness.\n"
      }
    ],
    "Makefile": [
      {
        "old": "main.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex sections/signed_defect.tex sections/speed_shell.tex\n",
        "new": "main.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex sections/signed_defect.tex sections/speed_shell.tex sections/shell_dynamics.tex\n"
      },
      {
        "old": "d\ncheck-signed:\n\tpython3 tools/check_signed_defect.py --integrated\n\n.PHONY: check-shell\ncheck-shell:\n\tpython3 tools/check_speed_shell.py --integrated\n",
        "new": "d\ncheck-signed:\n\tpython3 tools/check_signed_defect.py --integrated\n\n.PHONY: check-shell\ncheck-shell:\n\tpython3 tools/check_speed_shell.py --integrated\n\n.PHONY: check-dynamics\ncheck-dynamics:\n\tpython3 tools/check_shell_dynamics.py --integrated\n"
      }
    ],
    "proof_map.tex": [
      {
        "old": "\\raggedright\nGraph SHA-256: \\texttt{377a3190407510641039a11a88d3ceb8}\\texttt{54a6627367188a7533d7335f8ef3ec21}.\n\\Needspace{10\\baselineskip}\\section*{TAO-LOCAL: Tao local H1 theory}\\phantomsection\\label{node:TAO-LOCAL}\n",
        "new": "\\raggedright\nGraph SHA-256: \\texttt{c098f2a4d744c075a4352ecae6bf55a9}\\texttt{927dd81ebc70294ef27612fe9a6e0f7e}.\n\\Needspace{10\\baselineskip}\\section*{TAO-LOCAL: Tao local H1 theory}\\phantomsection\\label{node:TAO-LOCAL}\n"
      },
      {
        "old": "\\textbf{Manuscript labels:} \\texttt{ss:shell}, \\texttt{ss:residual}, \\texttt{ss:clock}, \\texttt{ss:gauge}, \\texttt{ss:consumer}.\n\\end{document}\n",
        "new": "\\textbf{Manuscript labels:} \\texttt{ss:shell}, \\texttt{ss:residual}, \\texttt{ss:clock}, \\texttt{ss:gauge}, \\texttt{ss:consumer}.\n\\clearpage\\section*{Review-pending component: Natural-variable time regularity and shell dynamics}\n\\textbf{Not a promoted claim or an arbitrary-data producer.}\n\nauthor-checked-independent-audit-pending. Natural-distance stability, pressure-free local time regularity and exact finite regularized shell-residual evolution; endpoint driver control and uniform refinement remain unproved, with no arbitrary-data critical estimate or node promotion.\n\n\\textbf{Evidence:} \\texttt{research/evidence/2026-09-06-shell-dynamics.md}.\n\n\\textbf{Manuscript labels:} \\texttt{st:stability}, \\texttt{st:time}, \\texttt{st:residual}, \\texttt{st:evolution}.\n\\end{document}\n"
      }
    ]
  },
  "guards": {
    "proof_map.tex": {
      "base": "c2800a7b1e52a2fa2f176e49763681bb1308cec8c722daec5b4800c9de83ca7b",
      "target": "f9dff6f235a85db74f0fab2b5d0e294bfc1835fdb3eaa6671d92484cf7cb96fa"
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
print('PASS: regularized shell dynamics source integration '+('present' if not changes else 'applied'))
print('Scope: document integrity only; independent audit and arbitrary-data temporal producer remain pending.')
