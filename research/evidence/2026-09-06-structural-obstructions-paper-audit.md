# Structural-obstructions paper: proof audit and primary-source comparison

Date: 2026-09-06.
Scope: the owner's request to complete the proposed Theorem Q / Proposition GS
paper at paper level and push it privately. This is NOT another attempt to
claim arbitrary-data Navier--Stokes regularity.

Status: complete author-level derivations and same-session adversarial review;
independent external mathematical review not performed. The manuscript has no
unresolved project estimate as a hypothesis of either main theorem. This
status is not a Lean certificate or a priority certificate.

## 1. Frozen inputs and manuscript identity

Research input: `itpplasma/navier` at
`5d842f8ecb3fd344d4aaf97a8c66dfff4c156d37`.
Manuscript input: `itpplasma/navier-paper` at
`78e8adee65924d9c2229a931982363dc3ed261ba`.

The new standalone manuscript is
`itpplasma/navier-paper/structural-obstructions/main.tex`, titled
*Quadratic Lyapunov obstructions and instantaneous vorticity growth for the
three-dimensional Navier--Stokes equations*.
The paper source was committed at
`8a2d5ce561ad656c91abc99fdf5bcbc754281a82`; its fetched blob matches the
locally compiled source below. Its bibliography is included in the source;
no other repository or evidence file is needed to compile it. Existing
`navier-paper/main.tex` is not replaced.

Source SHA-256:
`c18db6c0b2ad2c96d10ccb0005c1c207d8f98d4e3865ba4a07273ef54e059f68`.
Source Git blob:
`4ef4967a694581315bd923875f3c7c778e2e6aa5`.

Evidence reconstructed, rather than merely cited as missing proofs:

- `2026-09-06-quadratic-local-energy-exclusions.md`, Sections 2--7;
- `2026-09-06-pointwise-vorticity-helicity-exclusions.md`, Sections 2--3;
- `2026-09-06-global-smooth-vorticity-falsifier.md`.

The two-balance curve, intrinsic tangents, local-energy-inequality examples,
pressure-jet example and helical-selection example remain preserved research
notes. They are not silently included among the theorems audited here.

## 2. Exact completed statements

### Theorem 1.1 (Theorem Q)

For fixed nu>0 and integer m>=1, no real symmetric bilinear form B continuous
on H^m_sigma(R3) can both satisfy B(v,v)>=c||v||_3^2 for c>0 and be
nonincreasing along every local classical original unforced NS solution from
solenoidal Schwartz data. The form may depend on viscosity, not on datum or
time. No spatial symmetry, locality or multiplier assumption is imposed.

The proof is entirely in Section 3 of the paper. It derives cancellation
from amplitude testing, constructs the translation and O(3) averages,
represents the averaged form by a measurable radial multiplier, proves the
localized triad identity, forces the scalar weight to be constant, and
contradicts L3 coercivity by critical scaling.

### Theorem 1.2 (Proposition GS, fully reconstructed)

For each nu>0 there are positive E_*,Y_*,gamma and odd smooth compactly
supported solenoidal data u_(0,N), N>=1, with exactly equal E=E_*, Y=Y_* and
maximum vorticity one; their initial supports lie in a fixed compact set,
and their initial velocities are uniformly bounded. Vorticity equals e3
near the origin. Every actual unforced solution is globally smooth, but
liminf_(t downarrow 0)(||omega_N(t)||_infinity-1)/t >= gamma N.
The common product E_*Y_* may be arbitrarily small.

Section 4 supplies all profiles and parameters, with no dependence on a
separate research-note proof. The small-product global argument is proved
in Lemma 2.1, using the energy identity, the standard enstrophy estimate,
Fourier Cauchy--Schwarz and the classical blowup alternative.

Corollaries 5.1 and 5.2 distinguish a finite scalar bound at every classical
state from a locally bounded scalar bound asserted only almost everywhere
in time. The local-vorticity-jet consequence is stated for the exhibited
maximizing point, not for the entire local velocity jet or a rule using all
maximizers and their remote geometry.

## 3. Adversarial proof review

This table records the mathematical checks in this session. It is an author
review, not an independent referee report or a mathematical test suite.

| Potential failure | Resolution in the paper |
| --- | --- |
| Velocity sign reversal falsely used as a solution symmetry | Section 3.1 varies admissible initial data aw; only the polynomial derivative at time zero is used. |
| Differentiation of a rough quadratic form | B is continuous on Hm and the smooth-data solution is differentiable there, with derivative nu Delta w-N(w). |
| Assuming a compact NS orbit | Section 3.2 takes a weak limit only of uniformly bounded bilinear forms. Dense-pair convergence extends by the common norm bound. |
| Translation averaging loses coercivity | Each translation preserves L3; the same lower bound survives averaging and pointwise pair limits. |
| Missing helicity in the scalar-symbol claim | The averaging group is O(3), including reflections. The transverse stabilizer is O(2), not SO(2). |
| Evaluating an a.e. symbol on exceptional axes | Section 3.3 constructs a Haar-averaged representative on almost every radius and every direction before using its stabilizer. |
| Uncontrolled distributions at zero frequency | The symbol comes from a bounded L2 operator after conjugating by (1-Delta)^(m/2); no delta distribution at zero is present. |
| Treating a periodic field as a whole-space datum | The test is curl(chi(x/L) A), with explicit cutoff errors. No periodic PDE theorem is transferred. |
| Assuming continuity of the multiplier | Lemma 3.2 uses Lebesgue points of q and q^2, a spherical-slice estimate, approximate identities and polynomial-tail bounds. |
| Losing derivatives in multiplier localization | The symbol has order at most 2m; the cutoff correction is controlled in H^(2m). |
| Missing pressure/Leray term in the triad pairing | q(D)W_L is solenoidal, so the L2 pairing legitimately removes the Leray projection. |
| An a.e. relation not implying constant weight | The change (k,l)->(sqrt(k^2+l^2),l) is a local diffeomorphism; Fubini then gives constancy. |
| Incorrect two-dimensional generalization | The triad has three velocity components. No contradiction to two-dimensional enstrophy conservation is asserted. |
| Treating overlapping central velocities as disjoint | Equation (44) uses the triangle inequality for energy. Only their vorticity supports are disjoint for the exact enstrophy sum. |
| A hidden cutoff-region vorticity maximum | Equation (40) computes the rotation-core curl and proves its global magnitude is at most one, with equality on the core. |
| Bounded rather than exactly identical scalar inputs | Two remote reservoirs with different Y/E ratios solve a nonsingular two-by-two system. Their velocity supports are disjoint. |
| Matching coefficients cease to be positive | Choose delta first, then r0; the coefficients remain in [3/4,5/4] uniformly in N. |
| Global regularity assumed for the test family | Lemma 2.1 proves it in the small-product region; E_*Y_*=C_R delta^4. No terminal NS theorem is used. |
| Diffusion ignored at a nonconstant vorticity point | The entire vorticity field is constant near the origin initially, so its gradient and Laplacian actually vanish there. |
| Differentiability of the supremum assumed | The pointwise expansion is a lower bound for the supremum. The theorem uses liminf, not an unproved derivative identity for the maximizer. |
| Time-zero exclusion does not address a.e. inequalities | Corollary 5.2 uses local boundedness of F, continuity of the tuple, local Lipschitz continuity of Omega and integration. |
| Compact initial support asserted to persist | The paper repeatedly restricts the common-support property to initial data. |
| Arbitrarily large derivative turned into blowup | The remainder and the time interval are N-dependent; no uniform-duration growth or norm inflation is inferred. |

No unsupported implication was found in this review of the two displayed
proofs. No claim is made that a same-session review replaces independent
mathematical scrutiny.

## 4. Prior-art conclusion: revise the earlier novelty assessment

The broad quadratic-energy principle must NOT be advertised as new.
Goulart--Chernyshenko already explain the large-amplitude cancellation
mechanism, and Darrow--Carlson--Goluskin explicitly discuss the energy-only
quadratic restriction. Lee's older truncated-inviscid invariant result is
also directly relevant. The manuscript now gives credit before stating
its more precise whole-space scope.

The possible contribution of Theorem 1.1 is its particular continuum R3
formulation with finite Sobolev continuity and no imposed symmetry, and the
complete localization proof. This session did not establish priority for
that generality. A direct deduction from older literature might further
reduce the novelty assessment; the paper makes no priority claim.

For Theorem 1.2, no exact match for the conjunction of fixed E,Y,Omega,
common compact initial support, unchanged local vorticity jet, global
smoothness and unbounded initial maximum growth was located in the accessed
sources. This is a search result, not proof of novelty. Its underlying
nonlocal-strain mechanism is known, and the global-smooth upgrade uses a
standard small-data estimate, not a new arbitrary-data existence theorem.

### Source ledger (accessed 2026-09-06)

Only primary papers, publisher records or author-hosted versions support the
comparisons. Sources used as context are not imported as proof obligations.

| Source | Access and precise role |
| --- | --- |
| Goulart--Chernyshenko, Physica D 241 (2012), 692--704; doi:10.1016/j.physd.2011.12.008; arXiv:1101.1043v2 | Full public text, particularly Section 1.2, and the author's Oxford metadata page inspected. Prior large-amplitude/leading-degree obstruction; not treated as a theorem with the exact R3/Hm hypotheses here. |
| Darrow--Carlson--Goluskin, arXiv:2606.18232v1, 16 June 2026 | Full HTML and PDF inspected. Introduction explicitly states the energy-only quadratic restriction for typical fluid systems and discusses exceptional geometries. This directly corrects the earlier optimistic novelty assessment. |
| Jon Lee, J. Math. Phys. 16 (1975), 1367--1373; doi:10.1063/1.522705 | Publisher metadata and indexed abstract inspected. Finite-dimensional inviscid Fourier setting; reflection assumptions affect helicity. Full proof was not accessible in this session, so its sharpest possible implication for the continuum theorem is NOT certified. |
| Kraichnan, J. Fluid Mech. 59 (1973), 745--752; doi:10.1017/S0022112073001837 | Publisher abstract and metadata inspected. Context for helical truncated dynamics; no theorem from it is used to replace the manuscript's symbol proof. |
| Lu--Doering, Indiana Univ. Math. J. 57 (2008), 2693--2728; doi:10.1512/iumj.2008.57.3716 | Journal metadata and full author-uploaded text inspected. Analytic bounds with numerical three-dimensional extremizers; not a rigorous finite-time NS blowup result or the exact fixed-scalar maximum-vorticity theorem. The journal issue records the ending page as 2728. |
| Kang--Yun--Protas, J. Fluid Mech. 893 (2020), A22; arXiv:1909.00041 | Authors' arXiv record and publisher record inspected. Numerical finite-time enstrophy optimization; distinct observable and conclusion. |
| Constantin--Fefferman, Indiana Univ. Math. J. 42 (1993), 775--789; doi:10.1512/iumj.1993.42.42034 | Journal first-page/abstract PDF directly inspected, including a screenshot. Quantitative coherence conditions in the high-vorticity region; not merely a constant direction on an N-dependent small ball. No conflict is asserted. |
| Buaria--Pumir--Bodenschatz, Nature Communications 11 (2020), 5852; doi:10.1038/s41467-020-19530-1 | Full primary text inspected. Nonlocal strain and numerical/statistical attenuation context, not a universal deterministic scalar maximum principle. |
| Tao, Analysis & PDE 6 (2013), 25--107; doi:10.2140/apde.2013.6.25; arXiv:1108.1165 | Exact Theorem 5.4, its smooth-data continuation, and Corollary 5.8 inspected in the PDF, including screenshots. This is the local existence/regularity/blowup-alternative input. The manuscript supplies viscosity rescaling and gluing. |
| Tao, J. Amer. Math. Soc. 29 (2016), 601--674; arXiv:1402.0290 | Primary arXiv abstract inspected for the scope comparison: a modified averaged equation, not the original equation of these theorems. |

Primary retrieval locations:

- https://arxiv.org/html/1101.1043v2
- https://users.ox.ac.uk/~engs1373/GC_2012.html
- https://arxiv.org/html/2606.18232v1
- https://pubs.aip.org/aip/jmp/article/16/7/1367/224847/Isolating-constants-of-motion-for-the-homogeneous
- https://doi.org/10.1017/S0022112073001837
- https://iumj.org/article/4718/
- https://www.researchgate.net/publication/243105429_Limits_on_Enstrophy_Growth_for_Solutions_of_the_Three-dimensional_Navier-Stokes_Equations
- https://arxiv.org/abs/1909.00041
- https://iumj.s3-us-west-2.amazonaws.com/abstracts/42034_abs.pdf
- https://www.nature.com/articles/s41467-020-19530-1
- https://arxiv.org/pdf/1108.1165
- https://arxiv.org/abs/1402.0290

Search families included quadratic Navier--Stokes Lyapunov impossibility,
Euler energy/helicity invariant classification, fixed energy and enstrophy
maximum-vorticity growth, and nonlocal strain with bounded vorticity. Public
web and arXiv searching were performed. A subscription MathSciNet/zbMATH
search, an exhaustive literature search, and outside expert consultation
were NOT performed. No mathematical result is promoted on the basis of a
negative search alone.

## 5. Scope corrections and research disposition

Two wording corrections matter beyond bibliographic priority.

First, the conjunction of these no-go results does not prove that every
successful regularity proof must use a particular nonlocal/spacetime/full-
datum mechanism. Nonlinear functionals, datum-adapted forms, time-dependent
forms, nonmonotone estimates, quantitative geometry and other unexcluded
mechanisms remain possible. The paper states only class-specific exclusions.

Second, large initial vorticity growth is compatible with global regularity.
The shrinking coherence radius and N-dependent short-time remainder must
stay explicit. The counterfamily is neither a singular NS solution nor an
arbitrary-data regularity theorem. Do not use its scalar matching to claim
that all higher initial norms or future supports are controlled.

The standalone paper now has full proofs on the page, rather than a list of
lemmas deferred to research files. The review found no remaining internal
proof obligation for those two statements. Independent expert review and
priority assessment remain separate pending tasks. No public submission,
release, authorship change or outside contact is authorized or performed.

NS-R3: NOT PROVED. Terminal obstruction: UNCHANGED.
The original conditional manuscript and every earlier evidence file are
preserved. The terminal proof graph and formalization are not changed.

## 6. Mechanical verification scope

The new standalone source was compiled with
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
The build has no undefined references/citations, no multiply defined labels,
no overfull boxes and no LaTeX errors. Two underfull bibliography line
warnings are cosmetic. All twelve rendered pages were visually inspected
in contact sheets, with a detailed inspection of the measurable-localization
page; PDF links and text boundaries were checked. Generated PDFs and build
products are not repository source and are not committed.

Research-only structural validation uses the verified source artifact from
GitHub Actions run 34047280192, artifact 9993481723. Its ZIP SHA-256 is
`58242a5844358e8e2805debe7dea563e1f6fe9ac9ead21f3db1dd56519f1b4a3`;
its source commit is `5ee2b9880a7dfe27f990a9e3706bb3817f5ac8b3`.
The connector comparison to the frozen current input shows that the graph,
verifier and graph-referenced inputs are unchanged; changes consist of PLAN
and additional research evidence/history. The locally overlaid PLAN and
this new audit passed the unchanged `python research/verify.py --research-only`
verifier; manuscript-wide labels and formal coverage were explicitly skipped. This is
not a full fresh checkout, a manuscript-wide build, or a mathematical proof
certificate. Exact blob hashes and the changed-file comparison delimit the
scope of this integrity check.
