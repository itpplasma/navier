# Recent sources for the unforced whole-space problem

Source search and statement inspection: 9 September 2026, Europe/Vienna.
Repository input: `ebd72debbffaf3950d7c0c4b41c40883a21bd360`, refreshed from
origin/main before editing. This ledger serves the project researcher deciding
which external estimates can feed UE1--UE4 or the positive continuation route.
PLAN remains the live allocation. No claim is promoted by this search.

The target is the original incompressible equation on R3 with fixed nu > 0,
zero force, canonical pressure, and one nonzero solenoidal Schwartz datum.
A negative result needs a finite classical endpoint; a positive result needs
an input-only critical bound for every admissible datum. Euler, forced flows,
rough weak solutions, and modified equations have separate applicability gates.
There is no collision operator in the fluid results below; the kinetic entries
explicitly identify their different models.

## Search coverage and evidence levels

The search covered general web results, author announcements and publication
pages, GitHub source, arXiv, and publisher records. It emphasized September
1--9, extended through August, and followed older references needed to assess
the new mechanisms. The complete August math.AP listing contained 841 entries;
the recent math.AP listing contained 277. Titles were screened for relevant
fluid, singularity, and kinetic work, and selected abstracts and theorem texts
were inspected. The recent physics.flu-dyn listing was also screened.

Reproducible listing URLs:

- https://arxiv.org/list/math.AP/2026-08?skip=0&show=2000
- https://arxiv.org/list/math.AP/recent?skip=0&show=2000
- https://arxiv.org/list/physics.flu-dyn/recent?skip=0&show=2000

Query families included recent unforced NS/Euler blowup; critical regularity;
viscosity transfer and self-similarity; hypodissipation; pressure and energy
concentration; computer-assisted stability; and kinetic/Fisher-information
limits. Author-page checks included Caltech, Buckmaster, Vicol, Palasek, and
the OpenAI release. News and social posts supplied discovery links only.
Publication dates were checked against primary submission histories where
available; a recent crawl or seminar does not make an old theorem new.
This is a broad search, not an exhaustive census of the web or all revisions.

**Inspection** below means the stated passages were read, not that their full
proofs were audited. **Author claim**, **project acceptance**, **independent
audit**, and **formal verification** are separate statuses. The existing
owner acceptance of OA-NS is retained. No new independent audit or Lean build
was performed. Abstract-only entries are leads, not theorem imports.

## OA-NS: OpenAI forced Navier--Stokes

OpenAI, *Finite Time Blowup for Navier--Stokes*, released 8 September 2026.
[Paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
[release](https://openai.com/index/navier-stokes-solution/),
[Lean repository](https://github.com/openai/NavierStokesAndEuler).

Theorem 1.1: for every nu > 0 there is a smooth spacetime-compact force,
zero initial velocity, and a smooth R3 solution on [0,1) with uniformly
bounded kinetic energy and unbounded velocity as t approaches 1. Velocity
and pressure share a fixed compact spatial support. Corollary 10.6 supplies
the periodic counterpart. These are forced alternatives C/D; no unforced
implication follows. Inspection this search: Theorem 1.1 and introduction;
PLAN Section 2 records the earlier residual and localization inspection.

Project acceptance: accepted forced research input at the owner's direction.
Full mathematical audit: not performed here. Formal status: PLAN Section 8
records the earlier local kernel replication at
`8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`; the remote main still pointed to
that commit on this search. This is inherited evidence, not a new build.

Consumer: UE1--UE4's forced reference architecture and the existing
forced-insensitivity falsifier. First missing input is an autonomous
common-data construction cancelling the full projected force. Flat residuals
and small seeds do not cancel it. Viscosity is arbitrary but fixed; no uniform
inviscid transfer estimate is supplied.

## GDA-E: Caltech Euler profile and stability framework

Adarsh Ganeshram, Valentin Duruisseaux, Anima Anandkumar, *Stable Singularity
of the Euler Equations on R3*, announced 7 September 2026.
[Paper](https://tensorlab.cms.caltech.edu/users/anima/euler/Euler.pdf),
[author announcement](https://tensorlab.cms.caltech.edu/users/anima/euler.html).
Companion: Valentin Duruisseaux, Adarsh Ganeshram, Robert J. George, Anima
Anandkumar, *Stability Framework for the Singularity of the Euler Equations
on R3* ([paper](https://tensorlab.cms.caltech.edu/users/anima/euler/Euler-stability.pdf)).

Scope: unforced, axisymmetric Euler with swirl on R3, viscosity zero, a
traveling rescaled profile at concentration exponent lambda = 1/2.
Inspection: main §§4.5--4.9, Supplement §§1.2, 3.7--3.8, and companion
equations (9)--(11) and stability framework. Theorem 1 is conditional on
certified full damping and nonlinear/residual constants satisfying

    Lambda_3 delta + Lambda_R/delta < Lambda_stab.

The full quantitative certificate remains unfinished. Physical reconstruction
also assumes existence for all rescaled times; the main paper explicitly
requires a well-posedness/continuation argument. No independently audited
unconditional Euler theorem or replicated formal certificate is recorded here.

Project assessment: the invariant-neighborhood strategy is a possible UE1/UE2
alternative. For physical velocity u = tau^(lambda-1) V(x/tau^lambda), the
relative viscous coefficient is nu tau^(1-2lambda). At lambda = 1/2 it stays
constant. An exact Euler trial leaves projected NS residual -nu Delta u.
The first NS task is a viscous stability estimate absorbing that defect,
uniform through the endpoint. A Schwartz datum in the stability class and
whole-space exterior matching remain separate requirements. No such transfer
is established by either paper.

## OA-E: OpenAI unforced Euler common-data construction

OpenAI, *Finite Time Blowup for the Euler Equation*, released 8 September
2026 ([paper](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf)).
The release and Lean repository are the same as OA-NS; this is a distinct
theorem and construction. The [detailed September 9 inspection](openai-euler-transfer-2026-09-09.md)
extends the initial statement reading through the history inverses, pressure,
correction, scale induction and limiting datum, with a pinned Lean trail.
It is not a complete or independent proof audit.

Theorem 1.1 claims one smooth compactly supported solenoidal R3 datum whose
unforced Euler evolution has finite maximal lifespan, unbounded gradient,
and divergent time-integrated maximum vorticity. The construction iterates
exact Euler flows with initial increments summable in every fixed H^m norm
and a common compact support. Displacement boundary-value problems prepare
packet histories. An upper pressure-Hessian bound supplies coercivity;
signed pressure increments preserve that bound. Section 6 takes one smooth
initial-data limit and argues by stability against hypothetical continuation.

This is the closest new source to UE1's common-Cauchy-trace problem. Its
history construction supplies a concrete reference for a viscous history
calculation before another independent pulse inverse. It does not solve that problem for NS: viscosity adds
nu Delta u to Lagrangian acceleration and diffusion to the packet equations.
The first transfer task is to retain these terms and prove uniform viscous
history, pressure, correction, and initial-summability estimates. Increasing
packet frequency also increases diffusion. Auxiliary viscosity removed in
§3.6 is not a positive-viscosity terminal theorem.

Status: author theorem; source passages inspected; advertised Lean
formalization at the pinned repository; Euler kernel replication and
statement-faithfulness audit not performed by this search. The owner's
acceptance of OA-NS is not silently extended to this different theorem.

## AB-E: Alpöge--Buckmaster forced Euler

Levent Alpöge and Tristan Buckmaster, *Blowup for the Euler Equations with
Smooth Forcing*, publicly announced September 7--8, 2026.
[Paper](https://cims.nyu.edu/~tristanb/euler.pdf),
[repository](https://github.com/tristanbuckmaster/fluid_lean).
The retrieved PDF has no author line; attribution is from the public
announcement and repository. Inspection: Theorem 1.1 and §1.2.

For each prescribed ring radius r0 > 0 and height z0, the theorem constructs
smooth compactly supported axisymmetric data with swirl and a force smooth
through the finite endpoint, on R3. Circulation and meridional velocity stay
bounded while circulation gradient and vorticity diverge. The construction
uses transported oscillations and higher-order corrections to keep force
increments summable in all mixed derivatives.

Consumer: comparison of cascade geometry and exact nonlinear transport in
UE1. First uncontrolled terms for our target are both the projected force
and ordinary viscosity. Forced Euler and its Boussinesq/IPM companions do
not furnish autonomous NS preparation. Status: author theorem, statement
inspection only; no new mathematical audit or formal replication. The
separate hypodissipative announcement is not imported without a precise
public theorem and proof.

## GWX: One-component critical continuation

Maotuo Guo, Wendong Wang, Shiyang Xiong, *A Critical Chemin--Lerner
Regularity Criterion via One Velocity Component for the Three-Dimensional
Navier--Stokes Equations*, 3 September 2026,
[arXiv:2609.03877v1](https://arxiv.org/abs/2609.03877v1).
Inspection: Theorem 1.1, Corollary 1.5, and the frequency/slab proof outline.

For a finite-energy suitable weak solution of unforced R3 NS at normalized
viscosity, fix 2 < p < infinity and m = 3p/(p-2). The theorem assumes

    sum_{j in Z} ||Delta_j u^3||_{L^p(0,T;L^m(R3))} < infinity

and concludes regularity through T. The corollary applies to maximal L3-mild
solutions with L2 intersect L3 data. Frequency/slab matching produces
summable kernels while retaining separated pressure contributions.

Consumer: a possible alternative positive continuation suffix, particularly
if an anisotropic producer controls one velocity component. The first missing
input is the displayed frequency-summed bound from the datum at arbitrary
amplitude. It is not the existing RF-q bound, nor is it supplied by energy.
Smallness and constants in local estimates require an application audit;
viscosity restoration also needs the usual exact rescaling. Status: author
theorem, selected statement inspection, independent audit/formal status
not established. No replacement of the reviewed RF-q suffix is made.

## G-DIR: Directional strain and core history

Zoran Grujic, *On Decay of the Local Mean Oscillations of the Vorticity
Direction in Critical Navier-Stokes Flows*, 4 September 2026,
[arXiv:2609.05720v1](https://arxiv.org/abs/2609.05720v1).
Inspection: Assumptions 5.1--5.6, Theorem 5.7, Corollary 5.8.

The setting is a critical spatial point-concentration geometry in original
3D NS: vorticity magnitude comparable to |x|^-2 on a moving annulus, controlled
profile gradient and drift, a radial inflow condition, and a directional cap
condition. The theorem transfers a temporal modulus at the inner core to
spatial directional control. Uniform logarithmically weighted bmo additionally
requires the stated critical gradient bound and a uniform logarithmic core
modulus. Tangential strain must satisfy

    |P_(xi perpendicular) S xi| <= Lambda |x|^-2 |log |x||^-3.

Corollary 5.8's constant depends on k, nu, R0, Lambda, Lambda0, C1; this is
not an input-only estimate. The first missing inputs for us are the core
history and tangential-strain depletion, plus extraction of this geometry.
The operator distinguishes tilting from stretching, making it a useful
diagnostic for a concentrating candidate. Applying the companion regularity
criterion requires a separate statement audit. Status: author theorem;
selected statements inspected; independent audit and formal proof unverified.

## PV-RSS and CIV: Self-similarity restrictions

Ben Pineau and Vlad Vicol, *On Rotated Backwards Self-Similar Solutions of
the Incompressible 3D Navier-Stokes Equations*, first submitted 10 July,
revised 6 August 2026,
[arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619v2).
Inspection: Theorem 1.4, Type-I convention (1.9)--(1.10), and §1.5.
For normalized-viscosity R3 NS with a C2 globally rotating self-similar
profile and |u(x,t)| <= C/(|x|+sqrt(-t)), the theorem excludes sufficiently
small or large rotation speed, with thresholds depending on C. It leaves
intermediate rotation speeds open. Its local approximate-self-similarity
criterion is another potential exclusion test, with additional hypotheses.
Consumer: filter candidate geometries before a numerical search. It neither
excludes all rotating cascades nor supplies arbitrary-data regularity.
Status: author theorem, selected statement inspection only.

Peter Constantin, Mihaela Ignatova, Vlad Vicol, *On Putative Self-Similarity
for Incompressible 3D Euler*, 19 February, revised 20 July 2026,
[arXiv:2602.17570v3](https://arxiv.org/abs/2602.17570v3).
Inspection: Theorems 3.8--3.9 and 4.3--4.5 and the profile conventions
(3.5), (3.8), in the author-hosted text and current arXiv text.
Within those whole-space profile classes, outgoing-flow hypotheses force
gamma >= 1/2; the axisymmetric theorem also gives this lower bound under
its smoothness and far-field assumptions. A nonzero-swirl meridional fixed
point forces gamma = 1/2. This explains why changing the Caltech exponent
below 1/2 is not an automatic viscosity workaround. It is not a theorem
about every non-self-similar Euler cascade. Status: author theorem, selected
statement inspection; no independent audit or formal verification here.

## H-ATOM: Pressure and common-parent adjoints

Hao Huang, *Full-Tail Dynamical Rigidity Forced by Atomic Navier-Stokes
Energy Concentration*, 4 August 2026,
[arXiv:2608.04138v1](https://arxiv.org/abs/2608.04138v1), and
*Endpoint Energy Atoms Force Local Pressure Concentration in
Three-Dimensional Navier-Stokes Flow*, 31 August 2026,
[arXiv:2608.30715v1](https://arxiv.org/abs/2608.30715v1).
Inspection: first paper's Theorem 2.3 and budget discussion; second paper's
Theorem A and scope remark. Both concern unforced NS on the flat torus and
assume a positive point atom in an endpoint kinetic-energy measure.

The first claims a common adjoint and uniform late-tail saturation, forcing
failure of a parent-dependent delayed second-order budget. The second derives
relative pressure work and local pressure concentration from the atom.
Potential consumers: the positive route's extraction/rigidity separation and
full-state pressure diagnostics. Two gates remain: R3 adaptation and proof
that the singular scenario being studied actually creates an energy atom.
Vanishing-energy concentrating cores need not do so. Neither an atom-exclusion
criterion nor a parent-defined budget is an input-only regularity producer.
Status: author theorems, selected statement inspection; independent audits
and formal verification not established.

## Additional screened sources

These entries record scope decisions and useful secondary leads. Unless
explicitly stated, only primary metadata and abstracts were inspected.

| Source and date | Scope and project use |
| --- | --- |
| Gancedo--Hidalgo-Torné, [2609.05193v1](https://arxiv.org/abs/2609.05193v1), Sep 4 | Theorem 1.1 inspected: global helical mild vorticity solutions on R2 x T from divergence-free helical L1 vorticity, in a time-weighted Kato class. Positive-time Sobolev smoothing; velocities can have infinite energy. A symmetry benchmark, not R3 arbitrary-data regularity. |
| Coiculescu, [2609.06313v1](https://arxiv.org/abs/2609.06313v1), Sep 6 | Linearized 2D Euler ill-posedness around nonradial homogeneous power-law steady states in rotational L2 classes, alpha in (0,1). A warning about linearization spaces, not smooth-data nonlinear 3D NS blowup. |
| Cissé, [2609.03164v1](https://arxiv.org/abs/2609.03164v1), Sep 2 | Equation (1) and abstract inspected: torus NS with additional localized damping -chi K(t)u. Coercivity yields energy decay in the weak class; equation and norm differ from our target. |
| Nguyen--Wang, [2608.20068v1](https://arxiv.org/abs/2608.20068v1), Aug 20 | Moving Hill vortices, localized exterior and temporal corrections produce torus weak solutions in C_t L2 with gradient in C_t L^(6/5+0.00005). Useful localization ideas; no classical singular evolution from one Schwartz datum. |
| Zhao, [2608.17383v2](https://arxiv.org/abs/2608.17383v2), Aug 18 / Aug 27 revision | Compactly supported stationary distributional L2 NS solutions with L1 pressure, using logarithmic Mikado profiles. This rough class does not contradict the project's classical compact-support obstruction. |
| Gazzola, [2608.18802v1](https://arxiv.org/abs/2608.18802v1), Aug 19 | Forced 2D examples when force assumptions needed for strong regularity fail. Not smooth-force 3D or unforced blowup. |
| Chen--Hou, [2608.15174v1](https://arxiv.org/abs/2608.15174v1), Aug 15 | Clarification distinguishes a raw nonlocal Poisson error from the weighted profile residual in their boundary Euler proof. Abstract and introductory clarification inspected. Useful residual-audit discipline; no new whole-space NS theorem. |
| Mahithitarmmatorn, [2608.16915v1](https://arxiv.org/abs/2608.16915v1) | Primary history reports Jul 24 despite the August identifier. Exact stochastic-Weber covariance dynamics on T3 and explicit obstructions; the abstract leaves regularity gaps open. A representation is not a critical producer. |
| Wu, [2609.05021v2](https://arxiv.org/abs/2609.05021v2), Sep 4 / Sep 7 revision | Fisher-information balances for continuity and Fokker--Planck equations; Burgers and 2D numerical applications. No hard-sphere Boltzmann hydrodynamic-uniform critical bound is stated in the abstract. |
| Li--Xiong, [2608.27864v1](https://arxiv.org/abs/2608.27864v1), Aug 28 | Small-data two-component elastic hard-sphere Boltzmann limit to coupled Vlasov--NS, uniform in thermal-speed and mass ratios in a specified joint regime. Different limiting equation and data size; not K-CRIT or MIC-R3. |
| Gervais, [2607.18939v1](https://arxiv.org/abs/2607.18939v1), Jul 21 | Quantitative NSF limits for non-bilinear BGK, nonlinear Fokker--Planck and Boltzmann--Fermi--Dirac collisions. Potential kinetic-interface lead; full lifespan, domain and uniformity hypotheses not inspected, so not an import or an arbitrary-data producer. |
| Palasek, [2605.13827v1](https://arxiv.org/abs/2605.13827v1), May 13 | Forced viscous shell-model blowup and a separate inviscid unforced case. Embedding in the actual nonlinearity is still a gate. This is older background, not September progress. |
| Palasek, [2509.18595](https://arxiv.org/abs/2509.18595), Sep 23, 2025 | Arbitrary growth for a family of smooth global torus NS solutions bounded initially in BMO^-1. Useful against norm-only proposed budgets; not one finite-time singular solution. |
| Hou--Wang--Yang, [2509.25116v2](https://arxiv.org/abs/2509.25116v2), Sep 2025 / Mar 19, 2026 revision | Metadata rechecked; no newer revision found. The existing dossier records the theorem's singular initial datum and positive-time smoothness. Validated operator methods remain useful; it does not supply a Schwartz-data counterexample. |
| Córdoba--Martínez-Zoroa--Zheng, [2407.06776](https://arxiv.org/abs/2407.06776), Jul 2024 | Forced fractional dissipation of order alpha < (22-8 sqrt(7))/9, rather than the ordinary Laplacian of order 2. The Aug 21, 2026 seminar is not a new ordinary-viscosity theorem. |

No full proof audit of miscellaneous web claims of global regularity was
performed. Search-result titles and self-reported proof status were not used
as evidence of a solution. None of the inspected sources supplies the missing
fixed-positive-viscosity unforced theorem.

## Transfer priorities

OA-E's connected history and initial-data summability now have a
[detailed source inspection](openai-euler-transfer-2026-09-09.md), retaining
the exact pressure assumptions and distinguishing viscosity in the correction
from physical viscosity. The next estimate is its fixed-viscosity history map. Its
potential chain is:

    viscous history/correction estimates + one Schwartz datum
      -> exact unforced R3 flow -> singular lower bound
      -> LOCAL uniqueness and finite maximal lifespan -> counterexample.

The first uncontrolled contribution is viscous diffusion through the entire
packet prehistory; inviscid displacement coercivity does not estimate it.
Any bound must be uniform as the number of stages grows and the endpoint is
approached, with dependence on viscosity and fixed construction parameters
explicit. No such estimate was proved in this literature search.

GDA-E provides a second architecture to test only after including viscosity
in both profile residual and weighted stability operator, with PV-RSS/CIV
used to screen the precise proposed profile class. GWX and G-DIR are possible
positive-route tools when their input bounds can be produced. H-ATOM preserves
the distinction between extracting a singular object and proving its rigidity.
These are source recommendations; PLAN continues to allocate UE1.

## Frozen source fingerprints

SHA-256 of the bytes retrieved on 9 September 2026. PDFs and generated text
were kept outside the repository; only metadata and original notes are stored.
Unversioned PDFs are identified by these hashes rather than assumed immutable.

| Source | SHA-256 |
| --- | --- |
| OA-NS | `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f` |
| GDA-E main | `1ae24144b5e9b6d586a3dd130cda961bb8f83039aca13eb3f29d467ca6299b28` |
| GDA-E companion | `9d5d6e1044fccf0c50542087b3ebc65a475c1ceb51f96ccce226817672d57ebb` |
| OA-E | `a0c234518e6c489e16996805023eb2e75c00b7c03455f7a3a5be2c124954bfdd` |
| AB-E | `97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8` |
| GWX v1 | `a5366441fc18a4a28a695c6d989ba52868dc198240bd2f3726d92228f73f4087` |
| G-DIR v1 | `8992921597f73ee851f34e6d787c0ca486428a883416a1f621d8b8dd3c4040a7` |
| PV-RSS v2 | `379591aa3c1036c9140702ebe71aaab309fe207439a57db5ceff893f15d0ae8e` |
| CIV v3 | `81e987a26db35ea87eda860e26c5470025f9105beefb8369467d054bef6900ae` |
| CIV author-hosted PDF | `983ca7af1df00e07853219fc2aaecf3033b54027f3fe3a9fa74943b5486bd458` |
