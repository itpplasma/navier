#!/usr/bin/env python3
"""Integrate pending defect extensions; reject changed anchors and preserve other edits."""
from pathlib import Path
import argparse
root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--check', action='store_true')
args = p.parse_args()
def save(name, old, new):
    if args.check:
        assert old == new, f'integration missing: {name}'
    else:
        (root/name).write_text(new)
def replace(text, old, new):
    if new in text:
        return text
    assert text.count(old) == 1, 'Changed or ambiguous manuscript anchor: '+old[:90]
    return text.replace(old, new, 1)
old = (root/'main.tex').read_text()
text = old
text = replace(text, "Second, for $a\\ne2$ no\nbound of $\\norm\\sigma_a$ by $\\norm{\\nabla u}_a$ is available; only the case\n$a=2$ of \\eqref{eq:qdc-sigmaid} is proved, and the corresponding weighted\nCalder\\'on--Zygmund question is open.", "Second, Theorem~\\ref{de:near2} now supplies an unweighted bound of\n$\\norm\\sigma_a$ by $\\norm{\\nabla u}_a$ on a fixed open interval around\n$2$, under the stated additional integrability assumption on the gradient.\nThat extension awaits independent audit and does not settle a weighted\nCalder\\'on--Zygmund theorem at arbitrary exponents.")
text = replace(text, '\\emph{The hypothesis is implied by a classical criterion, not weaker than\nit.}  By \\eqref{eq:qdc-sigmaid}, $\\norm{\\sigma(t)}_2\\le\\frac12\\norm{\\nabla u(t)}_2$\nat every time, so\n\\[\n \\int_0^\\tau\\norm{\\sigma(t)}_2^4dt\\le\\frac1{16}\\int_0^\\tau Y(t)^2dt,\n \\qquad Y=\\norm{\\nabla u}_2^2 .\n\\]\nHypothesis \\eqref{eq:qe-defect-hypothesis} is therefore \\emph{implied} by\nthe classical Ladyzhenskaya--Prodi--Serrin and Beir\\~ao da Veiga gradient\ncriterion $\\nabla u\\in L^4_tL^2_x$, which lies on the same line\n\\eqref{eq:qe-defect-scaling} with $a=2$, $s=4$.  As a hypothesis the\ncriterion of Corollary~\\ref{cor:qe-defect-producer} is thus \\emph{not\nweaker} than those classical conditions; it is a weakening of a known\nsufficient condition in the observed quantity, and no strict improvement is\nproved.  Whether a branch with $\\int_0^{T_*}Y^2=\\infty$ but\n$\\int_0^{T_*}\\norm\\sigma_2^4<\\infty$ exists is not settled here in either\ndirection.  What is different is what is observed: only one scalar\nderivative of the minimizing representative, $\\operatorname{div}w$, rather\nthan the full velocity gradient $\\nabla u$.  That is the whole of the\ninterest of the criterion, and it is a statement about the shape of the\nobserved quantity, not about logical strength.\n\n', "\\emph{Implication direction and the actual-branch finiteness question.}\nBy \\eqref{eq:qdc-sigmaid},\n$\\norm{\\sigma(t)}_2\\le\\frac12\\norm{\\nabla u(t)}_2$ at every time, hence\n\\[\n \\int_0^\\tau\\norm{\\sigma(t)}_2^4dt\n \\le\\frac1{16}\\int_0^\\tau Y(t)^2dt,\n \\qquad Y=\\norm{\\nabla u}_2^2.\n\\]\nThus the classical gradient condition implies the defect condition, not\nconversely by this estimate alone.  Earlier wording that an implied\ncondition is ``not weaker'' reversed that logical direction.  No strict\nimprovement follows merely from observing a smaller quantity.\nCorollary~\\ref{de:no-separation}, whose component proof awaits independent\naudit, now supplies the reverse finiteness implication on actual selected\nbranches, with an explicit bound and without the endpoint theorem.\nConsequently the earlier unresolved possibility of finite fourth-power\ndefect integral but infinite squared-enstrophy integral is excluded by\nthat proof.  The distinction is the observed scalar, not a demonstrated\nstrict gain in the class of trajectories certified.\n\n")
text = replace(text, 'not imply it on an interval whose length is not controlled.', 'not imply it even on a fixed finite interval; see the scalar example\nat the end of Section~\\ref{de:section}.')
text = replace(text, '\\allowdisplaybreaks', '\\allowdisplaybreaks\n\\setlength{\\emergencystretch}{2em}')
text = replace(text, '\\[\n \\langle\\Delta u,\\nabla p\\rangle\n =\\sum_i\\int(-4\\pi^2|\\xi|^2\\hat u_i)\\,\\overline{2\\pi i\\xi_i\\hat p}\\,d\\xi\n =\\int4\\pi^2|\\xi|^2\\,\\overline{\\hat p}\\,\\Big(\\sum_i2\\pi i\\xi_i\\hat u_i\\Big)d\\xi\n =\\int4\\pi^2|\\xi|^2\\,\\overline{\\hat p}\\,(\\nabla\\cdot u)^\\wedge\\,d\\xi=0 ,\n\\]', '\\[\n\\begin{aligned}\n \\langle\\Delta u,\\nabla p\\rangle\n &=\\sum_i\\int(-4\\pi^2|\\xi|^2\\hat u_i)\n                    \\,\\overline{2\\pi i\\xi_i\\hat p}\\,d\\xi\\\\\n &=\\int4\\pi^2|\\xi|^2\\,\\overline{\\hat p}\n                   \\,\\Big(\\sum_i2\\pi i\\xi_i\\hat u_i\\Big)d\\xi\\\\\n &=\\int4\\pi^2|\\xi|^2\\,\\overline{\\hat p}\n                    \\, (\\nabla\\cdot u)^\\wedge\\,d\\xi=0 .\n\\end{aligned}\n\\]')

include = r'\input{sections/defect_extensions}'
if include not in text:
    anchor = r'\input{sections/dissipation_clock}'
    assert text.count(anchor) == 1, 'Integrate the clock component first'
    text = text.replace(anchor, anchor+'\n\n'+include, 1)
summary = ('A second review-pending extension in Section~\\ref{de:section} proves '
           'unweighted defect regularity near exponent two and a quantitative '
           'defect/enstrophy finiteness equivalence on actual branches.\n')
if summary not in text:
    anchor = 'No arbitrary-data critical bound is proved here.'
    assert text.count(anchor) == 1
    text = text.replace(anchor, summary+anchor, 1)
text = replace(text, '(ii) By Lemma~\\ref{lem:hk},\n$\\|\\partial_i\\partial_ju_k\\|_2^2=\\int(2\\pi)^4\\xi_i^2\\xi_j^2|\\hat u_k|^2\\,d\\xi$.\nSumming over $i,j$ gives $\\int(2\\pi)^4|\\xi|^4|\\hat u_k|^2\\,d\\xi\n=\\|{-4\\pi^2}|\\xi|^2\\hat u_k\\|_2^2=\\|\\Delta u_k\\|_2^2$, and summing over $k$\ngives (ii).', '(ii) By Lemma~\\ref{lem:hk},\n\\[\n \\|\\partial_i\\partial_ju_k\\|_2^2\n =\\int(2\\pi)^4\\xi_i^2\\xi_j^2|\\hat u_k|^2\\,d\\xi.\n\\]\nSumming over $i,j$ gives\n\\[\n \\int(2\\pi)^4|\\xi|^4|\\hat u_k|^2\\,d\\xi\n =\\|{-4\\pi^2}|\\xi|^2\\hat u_k\\|_2^2=\\|\\Delta u_k\\|_2^2,\n\\]\nand summing over $k$ gives (ii).')
text = replace(text, '$D_3(t)\\le2\\int_{\\R^3}|u|\\,|\\nabla u|^2dx\\le2\\norm{u(t)}_\\infty\\norm{\\nabla u(t)}_2^2$,\nwhich is a continuous function of $t$', '\\[\n D_3(t)\\le2\\int_{\\R^3}|u|\\,|\\nabla u|^2dx\n \\le2\\norm{u(t)}_\\infty\\norm{\\nabla u(t)}_2^2,\n\\]\nwhose right-hand side is a continuous function of $t$')
text = replace(text, '$\\int_0^{s/\\nu}\\norm{\\nabla u(\\tau)}_2^2\\,d\\tau\n=\\nu^{-1}\\int_0^s\\norm{\\nabla u(\\sigma/\\nu)}_2^2\\,d\\sigma\n=\\nu\\int_0^s\\norm{\\nabla v(\\sigma)}_2^2\\,d\\sigma$, while', '\\[\n\\begin{aligned}\n \\int_0^{s/\\nu}\\norm{\\nabla u(\\tau)}_2^2\\,d\\tau\n &=\\nu^{-1}\\int_0^s\\norm{\\nabla u(\\sigma/\\nu)}_2^2\\,d\\sigma\\\\\n &=\\nu\\int_0^s\\norm{\\nabla v(\\sigma)}_2^2\\,d\\sigma,\n\\end{aligned}\n\\]\nwhile')
save('main.tex', old, text)
old = (root/'references.bib').read_text()
entry = r"""
@misc{HaaralaSarsa2022,
  author = {Akseli Haarala and Saara Sarsa},
  title = {Global second order Sobolev-regularity of {$p$}-harmonic functions},
  year = {2022},
  eprint = {2204.13550},
  archivePrefix = {arXiv},
  primaryClass = {math.AP},
  note = {Version 2, 28 August 2022; methodological comparison only}
}
"""
new = old if '{HaaralaSarsa2022,' in old else old.rstrip()+'\n'+entry
save('references.bib', old, new)
old = (root/'Makefile').read_text()
new = old
if 'main.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex' not in new:
    new = replace(new, 'main.pdf: main.tex references.bib sections/dissipation_clock.tex',
                       'main.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex')
if '\ncheck-defect:' not in new:
    new += '\n.PHONY: check-defect\ncheck-defect:\n\tpython3 tools/check_defect_extensions.py --integrated\n'
save('Makefile', old, new)
old = (root/'README.md').read_text()
heading = '## Defect extensions (2026-09-06; independent audit pending)'
new = old if heading in old else old+'\n'+heading+"""

`sections/defect_extensions.tex` is included in `main.tex`. It proves a
near-2 unweighted gradient/defect estimate by a uniform contraction and a
direct quotient-dissipation enstrophy bound. The latter supplies the reverse
finiteness implication between the fourth-power defect integral and the
squared-enstrophy integral on actual branches; the previous claim that this
separation question was undecided is superseded. These are author-checked
components, not an independently audited arbitrary-data regularity proof.

Run `make all clock check-clock check-defect`. The checks cover source
integrity and finite arithmetic tests, not mathematical verification in Lean.
The required arbitrary-data fourth-power or signed-pressure producer remains
open. No full-range weighted estimate or novelty claim is made.
"""
save('README.md', old, new)
# The standalone clock uses the same paragraph-breaking repair as the main text.
old = (root/'dissipation_clock.tex').read_text()
new = old if r'\emergencystretch' in old else old.replace(
    r'\allowdisplaybreaks', r'\allowdisplaybreaks'+'\n'+r'\setlength{\emergencystretch}{2em}', 1)
save('dissipation_clock.tex', old, new)
print('PASS: defect component, scope corrections, bibliography and build integration; no claim promotion.')

# This patch is generated from the research graph, not a hand-edited map.
import hashlib
import json
update = json.loads((root/'tools/defect_map_update.json').read_text())
old = (root/'proof_map.tex').read_text()
digest = hashlib.sha256(old.encode()).hexdigest()
new = old
if digest != update['target_map_sha256']:
    assert digest == update['base_map_sha256'], 'Concurrent proof-map change; regenerate rather than overwrite'
    new = new.replace('–', r'\textendash{}\allowbreak{}')
    for edit in update['replacements']:
        assert new.count(edit['old']) == 1, 'Ambiguous generated map patch'
        new = new.replace(edit['old'], edit['new'], 1)
    assert hashlib.sha256(new.encode()).hexdigest() == update['target_map_sha256']
save('proof_map.tex', old, new)
print('PASS: manuscript map equals the frozen research-generator output.')
