#!/usr/bin/env python3
"""Integrate pending defect results; never promote a theorem or overwrite a changed anchor."""
from pathlib import Path
import argparse
import re
root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--check', action='store_true')
a = p.parse_args()
def save(name, old, new):
    if a.check:
        assert old == new, f'integration missing: {name}'
    else:
        (root/name).write_text(new)
def append(name, title, body):
    old = (root/name).read_text()
    new = old if title in old else old.rstrip()+'\n\n'+title+'\n\n'+body.strip()+'\n'
    save(name, old, new)
append('PLAN.md', '## Defect extensions: spatial interval and quantitative no-separation (2026-09-06)', '''
The current paper task has produced full component proofs in
`navier-paper` `878dcff0d72c9b94e9bb344a0c8a96bf8fc37a19`, source
`sections/defect_extensions.tex`. These are author-checked and independently
unaudited; the separate candidate metadata does not promote graph nodes.

A uniform measurable-coefficient contraction now proves an unweighted
estimate `||sigma||_r <= A_r ||grad u||_r` on a fixed open interval around
2, for solenoidal H1 data with the additional Lr gradient hypothesis.
The proof handles the zero set without differentiating the unit direction,
uses the trace-free Hessian norm sqrt(2/3), and identifies the same Neumann
series in L2 and Lr. The sharp old L2 estimate is retained. This partially
answers the manuscript's beyond-L2 question; no all-exponent weighted
Calderon-Zygmund estimate is asserted.

The direct quotient clock is
`Y'+nu Z <= (4 S^3 C9^3/(3 nu^2)) D_Q Y`. Combining it with the accepted
HF25 inequality and energy gives, with
`Astar=8 S^3 C9^3 Q0/(3 nu^3)` and
`Lambda_sigma=C_sigma nu^-3 integral ||sigma||_2^4`,

    integral_0^t Y^2 <= E0 Y0/(2 nu) exp(Astar exp(Lambda_sigma(t))).

Together with the old reverse inequality, this excludes finite fourth-power
defect integral with divergent squared-enstrophy integral on an actual
branch, including its full lifespan. It supplies a nonendpoint suffix,
without ESS or any comparison of D_Q and D3. The lead was already identified
in the HF26 audit; the explicit proof and constants are now supplied.

This entry supersedes the historical claim that the separation is unsettled
in both directions, subject to independent review. It also corrects the
old implication wording: a condition implied by a classical gradient
condition is not thereby 'not weaker'; the new actual-branch reverse
implication requires its own proof. A graph transcription saying ninth
power of the L9 norm is corrected to the cube, as in its existing source.

The arbitrary-data producer remains absent. Spatial near-2 regularity does
not upgrade the energy-level square time integral to a fourth power; the
new enstrophy bound explicitly depends on that unknown fourth power.
Next substantive gate: audit these components, then derive the required
signed spacetime estimate from the vector equation. Formal phase fields,
privacy, and every open/terminal graph kind are unchanged.

Evidence, source checks, failed closure and independent-review obligations:
`research/evidence/2026-09-06-defect-extensions.md`.
''')
append('README.md', '## Near-2 defect continuation (2026-09-06)', '''
The manuscript now has complete author-checked component proofs of near-2
unweighted defect regularity and a quantitative reverse finiteness bound
from the fourth-power defect integral to the squared-enstrophy integral.
See `research/evidence/2026-09-06-defect-extensions.md`. Independent review
is pending; these are not an arbitrary-data regularity proof. The missing
producer and all terminal/gap statuses remain explicit in `PLAN.md`.
''')
append('docs/proof.md', '## Defect interval and quotient clock (2026-09-06; review pending)', '''
The component `sections/defect_extensions.tex` in the manuscript proves:

    d = -(3/4)(n tensor n-I/3):(T d + grad u),
    ||K_n||_(2->2) <= 1/2,
    ||sigma||_r <= A_r ||grad u||_r       (r in a fixed interval around 2),
    Y'+nu Z <= (4 S^3 C9^3/(3 nu^2)) D_Q Y.

The Neumann construction is simultaneous in L2 and Lr, so membership of the
unknown defect in Lr is proved rather than assumed. Neither derivatives of
n nor an all-exponent weighted Calderon-Zygmund theorem are used.

With `Astar=8 S^3 C9^3 Q0/(3 nu^3)` and the already defined
`Lambda_sigma=C_sigma nu^-3 integral ||sigma||_2^4`, the exact suffix is

    integral_0^t Y^2 <= (E0 Y0/(2 nu)) exp(Astar exp(Lambda_sigma(t))),
    integral_0^t ||sigma||_2^4 <= (1/16) integral_0^t Y^2.

Hence the two integral finiteness conditions cannot separate on an actual
selected branch, even at its full lifespan. The old undecided statement is
superseded by this author-checked proof, pending independent audit. The
suffix is nonendpoint and requires no comparison of the two dissipations.

These results still do not supply an arbitrary-data fourth-power bound.
The first is spatial and the second places the unknown fourth-power integral
on its right side. No gap is promoted. The complete proof, precise extra
integrability hypothesis, source attribution and review questions are indexed
in `research/evidence/2026-09-06-defect-extensions.md`.
''')
old = (root/'docs/proof-graph.yaml').read_text()
new = old
# Correct the prose attached to existing nodes, without changing their kinds.
new = new.replace("the ninth power of the representative's L9 norm", "the cube of the representative's L9 norm")
new = new.replace('so it is a change of observed quantity and not a weaker assumption.',
                  'so this one-way comparison alone proves no strict improvement; the pending quotient-clock supplement supplies a reverse finiteness implication on actual branches.')
start = new.index('  - id: DEFECT-L4\n')
end = new.index('  - id: QUOTIENT-DEFECT-CRITERION\n', start)
block = new[start:end]
review = ('Open. The pointwise bound ||sigma||_2 <= (1/2)||grad u||_2 implies the defect condition from the classical gradient condition, not the opposite by itself; earlier not-weaker wording reversed that implication. '
          'The independently unaudited QUOTIENT-DISSIPATION-CLOCK supplement now proves a quantitative reverse finiteness implication on actual selected branches, excluding the previously undecided separation. '
          'This is a pending component proof, not a node promotion or a strict improvement over classical trajectory criteria. The energy budget still supplies only the square time integral; no arbitrary-data fourth-power producer is proved.')
block, count = re.subn(r'^    review: .*$', '    review: '+review, block, flags=re.M)
assert count == 1
new = new[:start]+block+new[end:]
new = new.replace('Conditional consumer; DEFECT-L4 is unproved and is not weaker than classical criteria.',
                  'Conditional consumer; DEFECT-L4 is unproved. No strict improvement over classical trajectory criteria is claimed; see the pending quantitative quotient-clock supplement.')
if '  - id: NEAR2-DEFECT-REGULARITY\n' not in new:
    assert 'candidate_supplements:\n' in new
    new = new.rstrip()+'''
  - id: NEAR2-DEFECT-REGULARITY
    title: Near-2 unweighted defect regularity
    status: author-checked-independent-audit-pending
    source_repository: itpplasma/navier-paper
    source_commit: 878dcff0d72c9b94e9bb344a0c8a96bf8fc37a19
    source_path: sections/defect_extensions.tex
    evidence: research/evidence/2026-09-06-defect-extensions.md
    paper_labels: ['de:fixedpoint', 'de:near2']
    scope: A uniform spatial exponent interval with an additional gradient integrability hypothesis; not an all-exponent weighted estimate or a temporal producer.
  - id: QUOTIENT-DISSIPATION-CLOCK
    title: Quotient clock and no finiteness separation
    status: author-checked-independent-audit-pending
    source_repository: itpplasma/navier-paper
    source_commit: 878dcff0d72c9b94e9bb344a0c8a96bf8fc37a19
    source_path: sections/defect_extensions.tex
    evidence: research/evidence/2026-09-06-defect-extensions.md
    paper_labels: ['de:quotient-clock', 'de:no-separation']
    scope: Quantitative defect-enstrophy finiteness equivalence on actual branches; no arbitrary-data fourth-power estimate and no node promotion.
'''
save('docs/proof-graph.yaml', old, new)
print('PASS: plan, README, proof dossier and pending defect metadata; all claim kinds unchanged.')
# Break long dash-joined names inside the generated diagram, rather than
# hiding overfull-box diagnostics or modifying generated claims by hand.
old = (root/'tools/generate_map.py').read_text()
needle = "'^': r'\\textasciicircum{}'}"
replacement = "'^': r'\\textasciicircum{}', '–': r'\\textendash{}\\allowbreak{}'}"
new = old
if replacement not in old:
    assert old.count(needle) == 1, 'Changed map escaping table'
    new = old.replace(needle, replacement, 1)
save('tools/generate_map.py', old, new)
