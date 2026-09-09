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
frozen = root/'sections/signed_defect.tex'
assert hashlib.sha256(frozen.read_bytes()).hexdigest() == '2e0a101a00a9a9170b0d750a41876a8f556af747184d509dc22a6b5eda1b6a27', 'frozen evidence/source changed; review integration first'
payload = json.loads(r'''
{
  "files": {
    "main.tex": [
      {
        "old": "$L^{3/2}$ integrability of its divergence defect under a spatial moment\nhypothesis. Weighted energy on the original equation supplies input-only\nspacetime budgets, but not the critical temporal estimate.\nNo arbitrary-data critical bound is proved here.  The signed\nhigh-frequency pressure hypothesis and the signed high-strain hypothesis\nremain unproved, and each is shown to be equivalent, at its own\n",
        "new": "$L^{3/2}$ integrability of its divergence defect under a spatial moment\nhypothesis. Weighted energy on the original equation supplies input-only\nspacetime budgets, but not the critical temporal estimate.\nA signed-defect extension in Section~\\ref{sd:section} removes an avoidable\nLeray-projection factor from the fourth-power inequality and derives a\none-sided quadratic-form clock with a critical amplitude-tail certificate.\nIts endpoint-uniform time bound is still missing.\nNo arbitrary-data critical bound is proved here.  The signed\nhigh-frequency pressure hypothesis and the signed high-strain hypothesis\nremain unproved, and each is shown to be equivalent, at its own\n"
      },
      {
        "old": "recorded there applies to it as well, and no novelty is claimed for the\nconstruction or for the scaling mechanism behind it.  One further\nconsequence should be recorded, independent of the construction: the\nabsolute route left open by \\eqref{eq:qdc-KY} is unusable rather than merely\ninsufficient, since a finite input-only bound on $\\int_0^\\tau Y(t)^2dt$,\nuniform in $\\tau<\\min\\{H,T_*\\}$, is the Ladyzhenskaya--Prodi--Serrin\ncondition $u\\in L^4((0,\\tau);L^6)$ ($\\norm u_6\\leq C_SY^{1/2}$ and\n$\\frac36+\\frac24=1$), and inserting\n$|\\langle(u\\cdot\\nabla)u,\\Delta u\\rangle|\\leq\\norm u_6\\norm{\\nabla u}_3\\norm{\\Delta u}_2$\nwith\n",
        "new": "recorded there applies to it as well, and no novelty is claimed for the\nconstruction or for the scaling mechanism behind it.  One further\nconsequence should be recorded, independent of the construction: the\nabsolute route left open by \\eqref{eq:qdc-KY} requires an unproved critical\nproducer, not a consequence of the energy estimate alone. A finite input-only\nbound on $\\int_0^\\tau Y(t)^2dt$, uniform in $\\tau<\\min\\{H,T_*\\}$,\nimplies the Ladyzhenskaya--Prodi--Serrin condition $u\\in L^4((0,\\tau);L^6)$ ($\\norm u_6\\leq C_SY^{1/2}$ and\n$\\frac36+\\frac24=1$), and inserting\n$|\\langle(u\\cdot\\nabla)u,\\Delta u\\rangle|\\leq\\norm u_6\\norm{\\nabla u}_3\\norm{\\Delta u}_2$\nwith\n"
      },
      {
        "old": "$\\sup_{t<\\min\\{H,T_*\\}}\\norm{u(t)}_{H^1}<\\infty$, which already yields\nHypothesis~\\ref{hyp:critical}, by interpolating $L^3$ between $L^2$ and\n$L^6$, and, by\nProposition~\\ref{prop:localtheory}(v), $T_*=\\infty$; such a bound would\ntherefore be the conclusion this route is meant to produce, not a step\ntoward it.\n\\end{remark}\n\n\\section{Proof boundary}\n",
        "new": "$\\sup_{t<\\min\\{H,T_*\\}}\\norm{u(t)}_{H^1}<\\infty$, which already yields\nHypothesis~\\ref{hyp:critical}, by interpolating $L^3$ between $L^2$ and\n$L^6$, and, by\nProposition~\\ref{prop:localtheory}(v), $T_*=\\infty$ when this bound is\navailable for every finite horizon. Deriving that bound would establish\nthe targeted continuation, so it remains a legitimate producer to pursue;\nit cannot be inserted as an already available estimate.\n\\end{remark}\n\n\\section{Proof boundary}\n"
      },
      {
        "old": "estimate is asserted anywhere in this paper, and the conditional theorems\nare not a solution of the Navier--Stokes Millennium problem.\n\n\\input{sections/dissipation_clock}\n\n\\input{sections/defect_extensions}\n\\input{sections/conformal_moment}\n\n\\bibliographystyle{plain}\n\\bibliography{references}\n",
        "new": "estimate is asserted anywhere in this paper, and the conditional theorems\nare not a solution of the Navier--Stokes Millennium problem.\n\n\\emph{Additional missing-bound reductions, review pending.}\nThe fourth-power defect condition \\eqref{eq:qe-defect-hypothesis} is also\nunproved. Section~\\ref{sd:section} sharpens its coefficient by an exact\nsigned cancellation and replaces it, as a sufficient input, by an\nendpoint-uniform integral bound for a one-sided quadratic-form rate.\nCorollary~\\ref{sd:missing-bound-consumer} gives the original defect bound\nexplicitly from that new input; it does not establish the input itself.\nThe new component and its nonendpoint quotient-clock suffix await\nindependent mathematical audit. No terminal or open graph node is promoted.\n\n\\input{sections/dissipation_clock}\n\n\\input{sections/defect_extensions}\n\\input{sections/conformal_moment}\n\\input{sections/signed_defect}\n\n\\bibliographystyle{plain}\n\\bibliography{references}\n"
      }
    ],
    "README.md": [
      {
        "old": "check is a finite algebra/source regression, not an independent audit.\nThe anchor-checked integration tool replaces the older frozen-map\nintegrators for the current workflow; their historical evidence is retained.\n",
        "new": "check is a finite algebra/source regression, not an independent audit.\nThe anchor-checked integration tool replaces the older frozen-map\nintegrators for the current workflow; their historical evidence is retained.\n\n## Signed defect and one-sided form clock (2026-09-06; audit pending)\n\nThe main manuscript now includes `sections/signed_defect.tex`. The exact\ncancellation `integral sigma |w|^3 = 0` gives the three signed identities\n`K = -integral V^T S(u) V = integral V^T B V = integral V^T B0 V`, with\n`B0 = (R_i R_j sigma) + sigma I/3`. The direct entry is\n`|K| <= (2/3) ||sigma||2 ||w||6^3`, reducing the fourth-power coefficient\nfrom `(81/32) C6^4 a0^3` to `a0^3/2`, where `a0=9 C_S^2/8`.\n\nA one-sided variational form rate `b_nu(B0)` and an explicit critical\namplitude threshold `kappa_nu` satisfy\n`0 <= b_nu <= kappa_nu <= a0^3 ||sigma||2^4/(6 nu^3)`.\nFinite accumulated form rate suffices for continuation and supplies an\nexplicit bound for the original missing integral. The arbitrary-data\nbound on this new rate is **not proved**. Both directions and all cutoff,\nmeasurability, scaling and constant calculations are explicit in the source.\n\nThis is an author-checked, independently unaudited component, not a\npromotion of DEFECT-L4 or NS-R3. `make check-signed` runs finite algebra and\nsource checks; it is not an independent mathematical audit.\n"
      }
    ],
    "Makefile": [
      {
        "old": ".PHONY: all continuation clean\nall: main.pdf proof_map.pdf\n\nmain.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex\n\tlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\nproof_map.pdf: proof_map.tex\n",
        "new": ".PHONY: all continuation clean\nall: main.pdf proof_map.pdf\n\nmain.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex sections/signed_defect.tex\n\tlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\nproof_map.pdf: proof_map.tex\n"
      },
      {
        "old": ".PHONY: check-conformal\ncheck-conformal:\n\tpython3 tools/check_conformal_moment.py --integrated\n",
        "new": ".PHONY: check-conformal\ncheck-conformal:\n\tpython3 tools/check_conformal_moment.py --integrated\n\n.PHONY: check-signed\ncheck-signed:\n\tpython3 tools/check_signed_defect.py --integrated\n"
      }
    ],
    "references.bib": [
      {
        "old": "  archivePrefix = {arXiv},\n  note = {Version 2, 3 June 2016. Conformal-invariance background; not a regularity theorem for the nonzero-curl representative}\n}\n",
        "new": "  archivePrefix = {arXiv},\n  note = {Version 2, 3 June 2016. Conformal-invariance background; not a regularity theorem for the nonzero-curl representative}\n}\n\n@article{Miller2021Sum,\n  author = {Miller, Evan},\n  title = {{Navier--Stokes} regularity criteria in sum spaces},\n  journal = {Pure and Applied Analysis},\n  volume = {3},\n  year = {2021},\n  pages = {527--566},\n  doi = {10.2140/paa.2021.3.527},\n  eprint = {2007.02023},\n  archivePrefix = {arXiv}\n}\n"
      }
    ],
    "proof_map.tex": [
      {
        "old": "\\end{center}\n\\clearpage\n\\raggedright\nGraph SHA-256: \\texttt{04632a86e3cc0cb725d710d800b492de}\\texttt{3dc2a5abdf73d2f6880f6ca7dbf4e8e2}.\n\\Needspace{10\\baselineskip}\\section*{TAO-LOCAL: Tao local H1 theory}\\phantomsection\\label{node:TAO-LOCAL}\n\\textbf{Class:} IMPORTED. \\textbf{Formal:} not started.\n\n",
        "new": "\\end{center}\n\\clearpage\n\\raggedright\nGraph SHA-256: \\texttt{811490092e1c8b1a058e072d8f24a24d}\\texttt{5c24313f8589ed5834516b9e28c9347b}.\n\\Needspace{10\\baselineskip}\\section*{TAO-LOCAL: Tao local H1 theory}\\phantomsection\\label{node:TAO-LOCAL}\n\\textbf{Class:} IMPORTED. \\textbf{Formal:} not started.\n\n"
      },
      {
        "old": "\\textbf{Evidence:} \\texttt{research/evidence/2026-09-06-conformal-moment.md}.\n\n\\textbf{Manuscript labels:} \\texttt{cm:covariance}, \\texttt{cm:inverted-h1}, \\texttt{cm:snapshot}, \\texttt{cm:moment}, \\texttt{cm:spacetime}, \\texttt{cm:scaling-test}.\n\\end{document}\n",
        "new": "\\textbf{Evidence:} \\texttt{research/evidence/2026-09-06-conformal-moment.md}.\n\n\\textbf{Manuscript labels:} \\texttt{cm:covariance}, \\texttt{cm:inverted-h1}, \\texttt{cm:snapshot}, \\texttt{cm:moment}, \\texttt{cm:spacetime}, \\texttt{cm:scaling-test}.\n\\clearpage\\section*{Review-pending component: Signed defect and one-sided form clock}\n\\textbf{Not a promoted claim or an arbitrary-data producer.}\n\nauthor-checked-independent-audit-pending. Exact signed cancellation, smaller fourth-power coefficient and an explicit conditional defect bound from a critical one-sided form clock; independent audit pending, no arbitrary-data clock bound or graph-node promotion.\n\n\\textbf{Evidence:} \\texttt{research/evidence/2026-09-06-signed-defect.md}.\n\n\\textbf{Manuscript labels:} \\texttt{sd:cancellation}, \\texttt{sd:improved}, \\texttt{sd:form-clock}, \\texttt{sd:missing-bound-consumer}, \\texttt{sd:tail}.\n\\end{document}\n"
      }
    ]
  },
  "guards": {
    "proof_map.tex": {
      "base": "5c1aafa529332543675f3aa63957d9b16ced2b0493fc523a1fa765aac9bd8288",
      "target": "a3bbda9851ee7d82e2bfb21e9860995cdb06ad2e56f0da1076daadd315c35d35"
    }
  }
}
''')
allowed = {'proof_map.tex', 'references.bib', 'README.md', 'main.tex', 'Makefile'}
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
