# Current status of the Navier–Stokes Millennium problem

**Historical cutoff.** The status conclusions below describe the September 5
search. For the September 7--8 releases and the September 9 source search, see
[the source update](recent-progress-2026-09.md) and [PLAN](../PLAN.md).
The project accepts OpenAI's forced NS result as directed by the owner;
the original unforced whole-space target remains unresolved in this project.

**Cut-off and coverage.** This note records a source search performed on 5 September 2026 (Europe/Vienna). I checked the Clay Mathematics Institute problem page and Fefferman's official problem statement, then searched arXiv and publisher pages for 2024–2026 work on regularity, weak-solution nonuniqueness, convex integration, and computation. This is a focused status note, not an exhaustive bibliography. Search results and publication metadata can change; preprints are identified as such.

## Clay's status and exact target

Clay currently labels the Navier–Stokes problem **Unsolved**: [Clay's current problem page](https://www.claymath.org/millennium/navier-stokes-equation/) (accessed 5 September 2026). The official statement is Charles Fefferman, “Existence and Smoothness of the Navier–Stokes Equation,” in the [Clay Millennium Prize Problems volume](https://www.claymath.org/library/monographs/MPPc.pdf), pp. 57–66 (statement issued with the Millennium problems in 2000; the PDF is the current Clay-hosted edition).

Fefferman's equations are the incompressible system

\[
 \partial_t u_i+\sum_j u_j\partial_{x_j}u_i
 =\nu\Delta u_i-\partial_{x_i}p+f_i,\qquad
 \nabla\!\cdot u=0,\qquad u(x,0)=u_0(x),
\]

with positive viscosity \(\nu>0\). On \(\mathbb R^3\), the data are smooth, divergence-free, and rapidly decreasing together with the prescribed force; the accepted solution class is smooth \(p,u\) for all \(t\ge0\), with bounded kinetic energy. The periodic alternative uses smooth periodic data and asks for smooth periodic solutions for all time. Clay permits four logically separate outcomes: global smooth existence on \(\mathbb R^3\), global smooth existence on the periodic domain, or a smooth-data finite-time breakdown example in either setting. In the two existence alternatives the force is specifically \(f\equiv0\); in the breakdown alternatives the force may be a smooth rapidly decreasing (or periodic) prescribed force (Fefferman, pp. 63–64).

Thus a result about rough initial data, a weak solution, a modified equation, a forced equation, a bounded domain, a special symmetry, or a numerical trajectory does not by itself answer the Clay question. The distinction matters especially for recent nonuniqueness results: nonuniqueness of weak solutions is compatible with the possibility that every smooth Clay datum has a unique global smooth solution.

## Weak and strong solution results

Leray's classical theorem gives global finite-energy weak solutions in three dimensions, but uniqueness and smoothness of arbitrary such solutions remain open. Fefferman's statement explains the weak formulation and records this gap (pp. 65–66). In two dimensions, global smooth well-posedness is known; the unresolved problem is three-dimensional.

The landmark peer-reviewed convex-integration result is Buckmaster and Vicol, “Nonuniqueness of weak solutions to the Navier–Stokes equation,” *Annals of Mathematics* 189 (2019), 101–144 ([journal page](https://annals.math.princeton.edu/2019/189-1/p03), published online 11 January 2019). It constructs nonunique finite-kinetic-energy weak solutions for the unforced 3D equation on \(\mathbb T^3\), and connects the construction to a vanishing-viscosity limit for dissipative weak Euler solutions. The solutions are far below the smooth class required by Clay.

Albritton, Brué, and Colombo, “Non-uniqueness of Leray solutions of the forced Navier–Stokes equations,” *Annals of Mathematics* 196 (2022), 415–455 ([journal page](https://annals.math.princeton.edu/2022/196-1/p03), published online 26 May 2022), exhibit two distinct suitable Leray solutions with zero initial velocity and the same body force. The abstract and theorem use a force in an integrability class (in particular \(f\in L^1_tL^2_x\)), constructed through an unstable self-similar vortex-ring background; this is a **forced** weak-solution result. It does not contradict Clay's unforced existence alternatives, whose force is \(f\equiv0\), and it does not supply a smooth-data breakdown example. Their later “Gluing Non-unique Navier–Stokes Solutions” ([Annals of PDE, published 4 October 2023](https://doi.org/10.1007/s40818-023-00155-8)) transfers the forced Leray nonuniqueness mechanism to bounded domains.

Recent extensions broaden the weak-solution phenomenon:

* Miao, Nie, and Ye, “Non-uniqueness of weak solutions to the Navier–Stokes equations in \(\mathbb R^3\)” ([arXiv:2412.10404](https://arxiv.org/abs/2412.10404), arXiv v1 submitted 6 December 2024), report finite-energy weak nonuniqueness in the whole space, plus infinitely many energy-dissipating weak solutions in a smooth bounded domain. The date is confirmed by both the arXiv metadata and the v1 PDF header. This is an arXiv preprint and does not establish Clay's smooth-data alternative.
* Miao and Zhao, “Nonuniqueness analysis on the Navier–Stokes equation in \(C_tL^q\) space” ([arXiv:2501.09698](https://arxiv.org/abs/2501.09698), v1 16 January 2025; v3 20 February 2025), construct infinitely many nontrivial weak solutions from zero data in a range \(2<q\ll3\), using intermittent convex integration. The stated class is explicitly weaker than the smooth/finite-energy regularity targeted by Clay.
* Coiculescu and Palasek, “Non-uniqueness of smooth solutions of the Navier–Stokes equations from critical data,” *Inventiones Mathematicae* 244 (2026), 165–219 ([DOI and publication record](https://doi.org/10.1007/s00222-025-01396-z); published 12 December 2025, issue date April 2026), construct one datum in the critical space \(BMO^{-1}\) with two distinct global solutions smooth for every \(t>0\). The initial datum is critical and generally rough, so this sharpens the boundary of critical-data well-posedness without resolving smooth rapidly decreasing data.
* Cheskidov, Zeng, and Zhang, “Existence and non-uniqueness of weak solutions with continuous energy to the 3D deterministic and stochastic Navier–Stokes equations,” *Advances in Mathematics* 490 (2026), 110845 ([publisher record](https://doi.org/10.1016/j.aim.2026.110845); April 2026), claim infinitely many global weak solutions with continuous energy for arbitrary finite-energy divergence-free data on the torus, including a stochastic extension. This is again a weak-solution result.

The 2025–2026 literature therefore changes the map of nonuniqueness, especially near critical spaces, while leaving the Clay regularity/uniqueness question for smooth data untouched. Claims in papers or repositories that state “global regularity” must be checked for the initial-data space, domain, forcing, viscosity, and whether “solution” means weak, Leray–Hopf, mild, strong, or classical.

## Regularity and partial-regularity progress

Conditional criteria continue to narrow where a singularity could occur. Lei and Ren, “Quantitative partial regularity of the Navier–Stokes equations and applications,” *Advances in Mathematics* 445 (2024), 109654 ([DOI](https://doi.org/10.1016/j.aim.2024.109654); published May 2024), give a logarithmic improvement of the Caffarelli–Kohn–Nirenberg partial-regularity theorem and quantitative intervals of regularity for suitable weak solutions. A 2025 *Journal of Differential Equations* paper, “A localized criterion for the regularity of solutions to Navier–Stokes equations” ([DOI](https://doi.org/10.1016/j.jde.2024.09.028); volume 415, 15 January 2025), develops localized Ladyzhenskaya–Prodi–Serrin-type criteria. These are conditional or partial results; neither supplies global control for arbitrary smooth 3D data.

## Computation and computer-assisted analysis

Numerics can certify a particular computation under an a-posteriori error test, but cannot turn an unverified simulation into a global theorem. Chernyshenko, Constantin, Robinson, and Titi, “A posteriori regularity of the three-dimensional Navier–Stokes equations from numerical computations” ([arXiv:math/0607181](https://arxiv.org/abs/math/0607181), arXiv v1 published 7 July 2006; the v2 manuscript is dated 18 September 2006), prove that a Galerkin/numerical trajectory passing their closeness test guarantees a corresponding strong solution on the tested finite interval. Their theorem is conditional on the computation and interval and does not prove global regularity.

The most directly relevant recent computational claim found in this search is Hou, Wang, and Yang, “Nonuniqueness of Leray–Hopf solutions to the unforced incompressible 3D Navier–Stokes Equation” ([arXiv:2509.25116](https://arxiv.org/abs/2509.25116), arXiv v1 submitted 29 September 2025; v2 revised 19 March 2026). I inspected the arXiv metadata, the v2 PDF abstract, and the theorem and definitions in the full text. Their theorem constructs infinitely many suitable Leray–Hopf solutions on \(\mathbb R^3\times[0,1]\) with the same compactly supported initial datum \(u_{\rm loc}\in C^\infty(\mathbb R^3\setminus\{0\})\cap L^q\) for every \(q<3\); the datum is singular at the origin, while the solutions are smooth for positive times. The equation is unforced, but this still does not contradict Clay: Clay requires every **smooth** rapidly decreasing datum, whereas this theorem deliberately uses scale-critical singular data and only proves a finite interval. The authors describe a rigorous computer-assisted proof based on a self-similar profile, an unstable eigenpair, high-precision numerics, and validated finite-rank operator estimates. As of this search it is an arXiv preprint; independent verification, journal publication, and acceptance by the Clay process were not located.

Hou's numerical study “Nearly self-similar blowup of generalized axisymmetric Navier–Stokes equations” ([arXiv:2405.10916](https://arxiv.org/abs/2405.10916), v1 17 May 2024; v3 29 June 2025) concerns generalized/rescaled axisymmetric models with solution-dependent or multiple viscosity coefficients and reports vorticity growth of order \(10^{30}\). It is evidence about those generalized models, not a finite-time singularity for the exact Clay system. The same distinction applies to numerical Euler blowup: Euler has \(\nu=0\), is not one of Clay's seven prizes, and its computational behavior cannot settle viscous 3D Navier–Stokes.

## Euler versus Navier–Stokes

Euler is obtained by setting \(\nu=0\), removing viscous diffusion; Navier–Stokes has \(\nu>0\). Fefferman explicitly notes that the corresponding 3D Euler existence problem is also open but is not a Clay prize problem (p. 59). Convex integration originated in Euler constructions and has been adapted to weak Navier–Stokes solutions, but an Euler weak-solution nonuniqueness theorem or Euler numerical blowup scenario is not a Navier–Stokes breakdown proof. Conversely, a Navier–Stokes weak nonuniqueness result does not exhibit the smooth finite-time breakdown required by Clay.

## Status at the cut-off

No accepted proof of either Clay alternative was located by 5 September 2026: neither global smooth existence for every admissible smooth 3D datum nor a qualifying finite-time breakdown example. The Clay page still marks the problem unsolved. The strongest recent developments located concern (i) weak or Leray–Hopf nonuniqueness, including an unforced computer-assisted preprint claim, (ii) nonuniqueness from critical rough data despite smoothness for positive times, and (iii) sharper conditional/partial regularity criteria. Verification gap: I did not find an official Clay announcement addressing the 2025–2026 papers, nor a peer-reviewed publication for the Hou–Wang–Yang computer-assisted claim by the search cut-off.

## Prior-art comparison (2026-09-05)

This section records what a bounded prior-art source check on 5 September 2026
established about the works nearest to the pressure route of this programme.
Each source below was opened at its primary text, arXiv abstract page,
publisher record, Zenodo record, or repository README; the tag [DI] means the
statement was read there, [MO] means only the bibliographic identity was
verified. Failure to find a match is not evidence of priority, and no priority
is claimed.

The cubic balance itself is published. Tran, Yu, and Dritschel,
"Velocity–pressure correlation in Navier–Stokes flows and the problem of
global regularity," *Journal of Fluid Mechanics* 911 (2021), A18,
[DOI](https://doi.org/10.1017/jfm.2020.1033), record in their equation (2.2)
the evolution of the $L^q$ norm for $q\ge3$ with driving term
$(q-2)\int p|u|^{q-3}u\cdot\nabla|u|$ and two weighted dissipation terms; at
$q=3$ and unit viscosity this is the identity $\frac13X'+\nu D_3=P_3$ used
here [DI, full text read]. They also split the space into high- and
low-velocity regions, absorb the low-velocity part of the driving term into
the dissipation with constant $\frac12$, and prove conditional criteria
(Theorem 3.1) involving a velocity–pressure correlation coefficient
$\Gamma_q$. Their threshold is defined implicitly through the solution's own
norms at each time; ours is a frequency cutoff chosen from the data, and the
low part is removed by an energy-only bound rather than absorbed. The "Yu" in
this paper is Xinwei Yu (Alberta), not the Runlong Yu of the 2026 preprints
below.

Signed pressure–flux work with a scale chain and telescoping is public prior
art at the level of mechanism. Runlong Yu,
[arXiv:2606.25322](https://arxiv.org/abs/2606.25322) (24 June 2026), proves for
suitable weak solutions on parabolic cylinders a coarse-grained resolution
lemma and an exact fixed-chain depletion theorem for
$G^\ell=\Pi^\ell+\operatorname{div}(P^\ell U^\ell)$, with a weighted
telescoping inequality over a finite chain of scales; its Remark 4.2 states
that the theorem is unconditional only at fixed chain length and fixed filter
length and does not assert summability as the chain grows [DI, abstract and
HTML body]. The companion audit
[arXiv:2606.25341](https://arxiv.org/abs/2606.25341) states that the framework
"do[es] not by themselves provide a coercive estimate excluding a surviving
obstruction" and that "no unconditional single-scale domination by a signed
combined-work detector is available" [DI, abstract], and
[arXiv:2606.12756](https://arxiv.org/abs/2606.12756) gives a conditional local
defect-cascade reduction [DI, abstract]. All three are local CKN statements;
none makes an assertion about $L^\infty_tL^3_x$ on $\mathbb R^3$.

Frequency-localised criteria are older. Bradshaw and Grujić, "Frequency
Localized Regularity Criteria for the 3D Navier–Stokes Equations," *Archive
for Rational Mechanics and Analysis* 224 (2017), no. 1, 125–133,
[DOI](https://doi.org/10.1007/s00205-016-1069-9),
[arXiv:1501.01043](https://arxiv.org/abs/1501.01043), prove two
Littlewood–Paley localised criteria for Leray–Hopf weak solutions, one of them
restricted to a finite frequency window whose lower bound diverges as $t$
approaches an initial singular time [DI abstract; article body not reachable,
Springer returns an authentication redirect]. Their localised object is the
velocity and their window moves in time.

Pressure criteria are older still and are all conditional on an absolute norm.
Chae and Lee, *Nonlinear Analysis* 46 (2001), 727–735,
[DOI](https://doi.org/10.1016/S0362-546X(00)00163-2), and Berselli and Galdi,
*Proceedings of the AMS* 130 (2002), 3585–3595,
[DOI](https://doi.org/10.1090/S0002-9939-02-06697-2), give the criterion
$\int_0^T\|p\|_{L^s}^{2s/(2s-3)}dt<\infty$, $s>3/2$ [identities from Crossref;
content read in citing primary sources]. Zhou, *Mathematische Annalen* 328
(2004), 173–192, [DOI](https://doi.org/10.1007/s00208-003-0478-x), gives
criteria in terms of the pressure in a generic domain; its body was not
reachable in this search, and the pressure-gradient condition often quoted
under the year 2004 is stated in citing sources for a different Zhou paper,
*Proceedings of the AMS* 134 (2006), 149–156,
[DOI](https://doi.org/10.1090/S0002-9939-05-08312-7). Beirão da Veiga,
*Chinese Annals of Mathematics, Series B* 16 (1995), 407–412, is a
velocity-gradient class, $\nabla u\in L^q_tL^p_x$ with $2/q+3/p\le2$ and
$p\in(3/2,\infty)$, not a pressure criterion. Mixed pressure–velocity criteria
in Lorentz spaces are Beirão da Veiga and Yang, *Chinese Annals of
Mathematics, Series B* 42 (2021), 1–16, for the whole space and torus, and 43
(2022), 51–58, for the non-slip boundary value problem on a bounded domain;
only the 2021 paper matches the domain used here.

Self-published claims and public repositories were checked for identity and
scope only. Taghizadeh, "A Local Monotonicity Reduction of the 3D
Navier–Stokes Regularity Problem to a Single Remaining Barrier," Zenodo
preprint v3, 3 February 2026,
[DOI](https://doi.org/10.5281/zenodo.18468477), reduces global regularity to
the behaviour of a local monotonicity functional as the scale vanishes; it is
a self-published preprint, stated as submitted to a journal, and is not used
here [DI, record page]. A ResearchGate manuscript by Cox announcing global
regularity at the critical endpoint could not be opened (HTTP 403) and is
therefore recorded as unverified, with no statement about its content. Public
repositories were read at their READMEs only, never as mathematical sources:
`johnrobertlawson/brc-navier-stokes` states that the problem is unsolved and
that passing checks do not certify a theorem; `davidkny22/navier-stokes-conditional`
(David Kogan) states a conditional criterion in an enstrophy-weighted
directional Fisher information and notes that expert review would be needed;
the `navier_stokes_millennium` subproject of `lizizatt/scratch` states that it
does not claim a solution and that its validator checks structure, not
mathematical truth; `vporton/navier-stokes` claims a solution obtained with an
LLM from the author's own extension theorem. Clay still lists the problem as
unsolved, so no such claim is treated as accepted. The DeepMind and
Gómez-Serrano programme on unstable singularities
([arXiv:2509.14185](https://arxiv.org/abs/2509.14185), 17 September 2025)
concerns self-similar singularity profiles for Euler-type and model equations,
not a Navier–Stokes regularity theorem, and is recorded as context.

Verification gaps in this comparison: the Bradshaw–Grujić article body, the
Zhou 2004 article body, the Beirão da Veiga 1995 article, and the Cox
manuscript were not reachable; MathSciNet and zbMATH full records require
authentication and were not used. The comparison is therefore a bounded
search, and its negative findings support no priority claim.
