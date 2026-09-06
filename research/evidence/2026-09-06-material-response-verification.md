# Material-response integration and verification record

Date: 2026-09-06. This records executed source/build checks, not an
independent mathematical audit or a completed arbitrary-data proof.

## Committed source and integrated main branches

The frozen proof is in `itpplasma/navier-paper` at
`2959003806907fa4742518bff741f24c592921e6`,
`sections/material_response.tex`, SHA-256
`54eb89147a08ee4403d8278fbe844bf396fb2978962cf156a6c5e547f4b90034`.
The finite regression script was committed at
`c3212286ed96d42421fb13dd0f19a4b2701a2282`.

Research integration: `5ee2b9880a7dfe27f990a9e3706bb3817f5ac8b3`.
Paper integration: `81f0cd1524e8a625e6ee46970d69e40e5a2e50bf`.
Both integrations were committed and pushed to main by the private
repository workflows after refreshing Git and running guarded integration.
Unsigned commits were explicitly authorized by the repository owner.
The workflows rebase and recheck before a normal, non-force push.
No generated PDF, source archive, credential, added authorship or formal
repository change was committed. Existing historical notes were preserved.

Research workflow run `34047280192` completed successfully, including
integration, the research-only structural verifier and regenerated map.
Paper workflow run `34047416248`, job `101524848189`, completed successfully,
including source integration, all seven regression suites, all document
builds, warning rejection, the final commit/rebase/recheck and push.
Successful research artifact: `9993481723`.
Successful paper artifact: `9993539389`.
Both were downloaded through the GitHub connector and replayed locally.

## Documents updated

Research: PLAN.md (including its live active task), README.md, docs/proof.md,
docs/proof-graph.yaml, docs/proof_map.tex, the new mathematical evidence,
the guarded integration script and the private integration workflow.
The new candidate is COROTATIONAL-MATERIAL-RESPONSE; its status is
`author-checked-independent-audit-pending`.

Paper: the new Section 16, main.tex abstract and proof boundary, Makefile,
README.md, references.bib, proof_map.tex, finite regression and guarded
integration scripts, and the private integration/build workflow.
The bibliography attributes classical one-form transport to Constantin and
Iyer without importing their stochastic theorem or claiming novelty.

## Exact-source replay and completed checks

All eight paper proof/integration/checker surfaces compared were byte-for-
byte equal to the locally validated versions. All seven corresponding
research integration/evidence/map surfaces also matched exactly.
The two generated map sources were byte-identical, with SHA-256
`9376cf076167cad82acf8ce79218d48101c6856e3ee8528157c3c9910fba3db7`.
Regenerating the research map after extraction changed no byte.

The default research/verify.py was rerun against the exact artifact
snapshots, not only with --research-only. It passed: 29 main claim records,
acyclic dependencies, evidence and status checks, manuscript labels across
8 TeX sources, 8 pending supplements and the formal manifest.
For the manifest check only, the actual navier-formal/lakefile.toml was
read through the connector; its Git blob SHA was verified as
`732cc1ab6aec6134b4c00aab6d4e231ec0ded7ee`.
This is not a Lean build or a verification of any Lean proof.

Both new integration scripts passed --check on the exact remote snapshots.
All seven paper regression targets passed again locally after extraction:
check-clock, check-defect, check-conformal, check-signed, check-shell,
check-dynamics and check-material. The new target includes exact rational
constants, weighted-projection/action algebra, rigid Fourier covariance,
and six nonlinear moving-metric finite-atom probes with a zero atom and
positive/negative perturbations. These are regressions, not proof audits.
The remote document builds rejected undefined references, undefined
citations and overfull boxes. Local builds also passed; new pages and
bibliography were rendered and visually inspected, with the remote
material-action page independently rendered for source-artifact comparison.

Remote PDFs: main.pdf has 137 pages, with Section 16 on pages 129--134;
proof_map.pdf has 19 pages; dissipation_clock.pdf has 4 pages. PDF SHA-256:

- main.pdf: `33cc2f87f51ac5f47bc0af742b4b871c1a69a7a2b3bbed01deaed23b22f76534`
- proof_map.pdf: `2f3661ab7ab6f5cb41c28e6caf3e638074f32a454ea187787e95c6cbaa29def5`
- dissipation_clock.pdf: `c02fbd6fd13aebb80997f16c3ea7d98b5106494bf4bd0e08fc005f4fc9e96d49`

## Mathematical boundary, unchanged by successful builds

The new proofs establish the moving-metric weighted response, a cubic
little-o remainder justifying a strong L2 natural derivative at zeros,
and an exact corotational response with an orthogonal diffusion-strain
action. The finite shell-residual law keeps its complete nonlocal
commutator. These are author-checked component results awaiting independent
audit, not a complete proof of the requested theorem.

No input-only endpoint bound on the action, the combined clock L_c, or the
fourth-power defect integral was established. The available pointwise
upper bound still contains weighted Delta u squared and squared strain;
energy/moment budgets do not supply the needed endpoint control. The
complete residual also retains commutator and refinement losses. All 29
main node classifications and both formal-phase statuses were preserved.
NS-R3, HIGH-PRESSURE, HIGH-STRAIN and DEFECT-L4 remain open.
