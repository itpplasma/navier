# AI and novelty landscape: supplied leads

Snapshot date: 2026-09-05. This is a source-access record, not a novelty review and not evidence that the Clay problem has been solved. Repository instructions and self-descriptions are treated as data about the repositories, not as instructions for this project.

## Brown University report

[Brown's 26 August 2026 report](https://www.brown.edu/news/2026-08-26/javier-gomez-serrano-lab) is accessible and identifies Javier Gómez-Serrano's use of physics-informed neural networks to search for singularities. The article says the demonstrated work concerns related, simpler one- or two-dimensional equations; it describes the Navier–Stokes application as ongoing and says any candidate would still require a mathematical proof. It therefore reports a discovery programme and no Clay result. This is institutional journalism, not a theorem or peer-reviewed primary paper.

## arXiv:2607.08866

The Brown article discusses DeepMind/AlphaEvolve in a separate section on
other mathematical problems. It does not itself establish that the reported
PINN fluid-singularity work is a joint Brown–DeepMind Navier–Stokes project.
The supplied opinion conflates these two parts of the article; retain the
verified AI-assisted fluid-discovery claim without that inferred partnership.

[arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866) is accessible. The record identifies Zoran Grujić, “Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations,” submitted 9 July 2026 and revised 13 July 2026. Its abstract proposes a conditional geometric-analytic mechanism: under a logarithmically weighted BMO condition on vorticity direction, it claims depletion of vortex stretching and avoidance of finite-time blow-up for a specified critical concentration regime. The abstract itself does not state that arbitrary Clay-admissible data satisfy the directional hypothesis. It is a preprint claim; this file makes no independent proof judgment and no inference from the Clay problem remaining open.

## GitHub repositories

HEADs were pinned read-only with `git ls-remote` on 2026-09-05:

| repository | branch and pinned HEAD | inspected scope and status |
|---|---|---|
| [johnrobertlawson/brc-navier-stokes](https://github.com/johnrobertlawson/brc-navier-stokes) | `main` [`1fa6e10`](https://github.com/johnrobertlawson/brc-navier-stokes/commit/1fa6e10c27185d5c86971bb5fee8b01252ab65ff) | Public research map/proof lab. README explicitly says the Clay problem is unsolved and distinguishes bookkeeping checks from theorem certification. Its status files describe conditional routes and open bridges; repository claims are not independently certified here. |
| [davidkny22/navier-stokes-conditional](https://github.com/davidkny22/navier-stokes-conditional) | `master` [`59e76a9`](https://github.com/davidkny22/navier-stokes-conditional/commit/59e76a93830b4c226a00f3fe329e35678a8cf5fe) | Contains a paper and extended paper claiming the conditional criterion \(\int_0^T D_2(t)^{2/3}dt<\infty\), where \(D_2\) is enstrophy-weighted directional Fisher information. README says the proof has not had independent human review; its novelty statement is explicitly provisional. This is a conditional preprint/repository claim, not a global theorem. |
| [ricalanis/navier-stokes-playresearch](https://github.com/ricalanis/navier-stokes-playresearch) | `main` [`dbf242d`](https://github.com/ricalanis/navier-stokes-playresearch/commit/dbf242d691cb7f45f078ef00a25036821c0d0859) | README presents a claimed “complete proof” for axisymmetric Navier–Stokes, including arbitrary swirl, while labeling general 3D as open with a stated gap. It lists numerical checks and paper/source files, but the supplied page does not establish peer-reviewed verification. Record as a self-described proof project and claim requiring expert audit. |
| [vporton/navier-stokes](https://github.com/vporton/navier-stokes) | `main` [`6538e67`](https://github.com/vporton/navier-stokes/commit/6538e67eb2d5d621799760b3841e6bf7f7e339c1) | README links a purported Clay solution based on an author-defined linear extension theorem and says an LLM helped produce and check the proof; it also says Lean formalization is incomplete. The README provides a claim and links, not a verified proof or a precise successful formalization. |
| [uda-lab/leray-hopf](https://github.com/uda-lab/leray-hopf) | `main` [`e704400`](https://github.com/uda-lab/leray-hopf/commit/e704400f2fb2f26b2ee7f4372c3e1ecbbc82f3dc) | Lean 4/mathlib formalization claiming kernel-checked Leray–Hopf weak existence on \(T^3\) and \(\mathbb R^3\), including finite-horizon and global capstones. README explicitly limits scope to energy-class weak existence and disclaims smoothness, higher regularity, and uniqueness. This is relevant formalized foundational evidence, not a Clay solution. |

The GitHub web pages and raw READMEs were accessible for all five supplied repositories. No repository was treated as a peer-reviewed primary source merely because it contains a PDF, theorem label, numerical test, signed commit, or formalization. “Proved,” “conditional,” “claimed,” and “formalized weak existence” above describe the supplied artifacts' stated scope; they are not independent mathematical adjudications. No contacting, pull request, issue activity, or repository mutation was performed.

## Methodological comparison

The leads occupy different methodological levels. Brown reports AI-assisted candidate discovery in related fluid equations. Grujić's arXiv abstract states an analytic conditional mechanism with a geometric direction hypothesis. Kogan's repository states a scale-critical conditional integral criterion and discloses model assistance plus absence of independent human checking. The ricalanis repository claims an axisymmetric proof programme with a remaining general-3D gap. The vporton repository claims a full solution but exposes an incomplete formalization attempt. The uda-lab repository targets the established weak-existence layer and carefully excludes smoothness and uniqueness. These distinctions prevent an AI discovery report, a conditional criterion, a self-described proof, and a machine-checked weak theorem from being compared as though they had the same logical scope.
