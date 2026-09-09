# Navier–Stokes manuscript

Private GitHub manuscript authority: `itpplasma/navier-paper`, containing a
self-contained mathematical manuscript and clickable proof map. The paper
gives a conditional route through signed high-frequency pressure control;
that estimate and the terminal regularity claim remain open.

Build both documents locally with `make`. The companion `../navier` owns the
dependency graph and live status; regenerate the map with
`python3 ../navier/tools/generate_map.py`. Fetch `origin` before source changes
and push signed commits. Both GitHub repositories remain private. The former
Navier Overleaf project was deleted on 2026-09-05; GitHub is the only remote
workflow. Formalization status is tracked in `../navier/PLAN.md`.

## Standalone continuation for review (6 September 2026)

[dissipation_budget_continuation.tex](dissipation_budget_continuation.tex)
retains cubic dissipation to give a direct nonendpoint continuation proof
from strict pressure absorption, extends the divergence-defect calculation
to the finite-exponent critical line, and reconstructs HF30's finite-horizon
comparison. Build it with `make continuation`.

These are component proofs with explicit project inputs, author self-checks,
and independent mathematical review still pending. The arbitrary-data
producer is not proved; `main.tex` and the generated claim map are unchanged.
The scope, verification script, and review tasks are recorded in
`../navier/research/evidence/2026-09-06-dissipation-budget-continuation.md`.

## Dissipation-clock component (2026-09-06)

`main.tex` now includes `sections/dissipation_clock.tex`; the same source
builds independently with `make clock`. Run `make check-clock` for the
arithmetic/source regression. The component derives a direct `(3,9)`
Serrin continuation bound from cubic dissipation and finite/logarithmic
dissipation barriers. These sharpened derivations await independent
mathematical audit and are not promoted graph claims. The arbitrary-data
pressure producer and the terminal theorem remain open.

The current user task explicitly authorizes manuscript edits and unsigned
commits in both private repositories. The research `PLAN.md` owns live
status; earlier read-only/signed-only restrictions are superseded for
this task. Formalization is not paused or declared complete.

## Defect extensions (2026-09-06; independent audit pending)

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


## Conformal inversion and moment component (2026-09-06)

`sections/conformal_moment.tex`, included in `main.tex`, contains a full
component proof, author-checked with independent mathematical audit pending.
Conformal pullback preserves the cubic gradient minimizer. Applying the
accepted div-curl estimate to the Leray projection of the inverted datum
proves `w,q in H1` and `sigma in L^(3/2)` when `|x| grad u in L2`.
The weighted energy argument establishes that hypothesis at every classical
time on the original Schwartz-data branch and gives input-only finite-horizon
integrated moment bounds, including `sigma in L2_t L^(3/2)_x`.

This answers the earlier spatial questions for this branch, not for every
bare H1 datum. The new spacetime norm is supercritical in Navier-Stokes
scaling: it does not supply DEFECT-L4 or any arbitrary-data regularity proof.
An explicit non-solution curve verifies why finiteness of the new budgets
alone does not imply the missing fourth-power time integral.

Run `make all clock check-clock check-defect check-conformal`. The conformal
check is a finite algebra/source regression, not an independent audit.
The anchor-checked integration tool replaces the older frozen-map
integrators for the current workflow; their historical evidence is retained.

## Signed defect and one-sided form clock (2026-09-06; audit pending)

The main manuscript now includes `sections/signed_defect.tex`. The exact
cancellation `integral sigma |w|^3 = 0` gives the three signed identities
`K = -integral V^T S(u) V = integral V^T B V = integral V^T B0 V`, with
`B0 = (R_i R_j sigma) + sigma I/3`. The direct entry is
`|K| <= (2/3) ||sigma||2 ||w||6^3`, reducing the fourth-power coefficient
from `(81/32) C6^4 a0^3` to `a0^3/2`, where `a0=9 C_S^2/8`.

A one-sided variational form rate `b_nu(B0)` and an explicit critical
amplitude threshold `kappa_nu` satisfy
`0 <= b_nu <= kappa_nu <= a0^3 ||sigma||2^4/(6 nu^3)`.
Finite accumulated form rate suffices for continuation and supplies an
explicit bound for the original missing integral. The arbitrary-data
bound on this new rate is **not proved**. Both directions and all cutoff,
measurability, scaling and constant calculations are explicit in the source.

This is an author-checked, independently unaudited component, not a
promotion of DEFECT-L4 or NS-R3. `make check-signed` runs finite algebra and
source checks; it is not an independent mathematical audit.


## Speed-shell cancellation and effective defect (2026-09-06; audit pending)

The new source `sections/speed_shell.tex` proves
`integral_{|w|>k} sigma=0` for every k>0, with an L^(3/2) flux cutoff and
no finite-energy assumption on w. Thus sigma annihilates every L2 function
of speed. Projecting the scalar signed-work field chi off the closed speed
subspace gives a measurable factor delta in [0,1] and
`|K| <= (2/3) delta ||sigma||2 ||w||6^3`. Finite speed-shell averages
bound the residual, converging under nested refinement.

Speed-dependent scalar corrections `h(|w|)sigma I` leave the signed work
unchanged. Their countable form-rate infimum beta satisfies
`0<=beta<=b_nu(B0)`. With
`c_nu=min(3 beta, a0^3 delta^4 ||sigma||2^4/(2 nu^3))` and `L_c=integral c_nu`,

    Q(t)+nu/2 integral D <= Q0 exp(L_c(t)),
    integral ||sigma||2^4 <= E0 Y0/(32 nu) exp(Astar exp(L_c(t))).

The last implication retains the pending quotient-clock dependency.
The bound on L_c from arbitrary initial data is NOT proved; delta<=1 only
returns the old unknown fourth-power integral. No temporal derivative of
the moving speed projection is assumed. Full proofs, cutoff and
measurability details, and the stopping point are in the source.
These are author-checked components, not an independent audit or promotion
of any open claim. `make check-shell` is a finite algebra/source regression.

## Natural-variable time regularity and regularized shell dynamics (2026-09-06)

`sections/shell_dynamics.tex` proves, with independent audit pending,

    ||V1-V0||2^2 <= 9/8 integral (|w0|+|w1|)|f1-f0+g|^2,

for every admissible gradient g. On each compact classical interval this
gives V in W^(1,infinity)(time;L2) and the pressure-free bound

    ||V_t||2^2 <= 9/4 integral |w| |nu Delta u-(u dot grad)u|^2.

Finite smooth speed features with a positive ridge penalty give an exactly
differentiable residual R, retain `K=<sigma,residual>`, and decrease to the
full speed-projection residual at each fixed time. The source proves its
exact evolution and quantitative derivative bound in the correct dual
spaces. It does not differentiate the sharp moving projection.

This closes a fixed-regularization temporal-calculus obstacle, not the
arbitrary-data fourth-power bound: endpoint control of the derivative
driver and uniformity as the ridge penalty vanishes remain unproved.
No graph node or predecessor audit is promoted. `make check-dynamics`
checks finite algebra and source integrity, not mathematical correctness.

## Strong corotational material response (2026-09-06)

`sections/material_response.tex` proves a moving-metric response for the
cubic minimizer and a strong natural-variable derivative in L2, including
velocity zeros. Pullback by the actual flow gives an exact corotational
material law. Its diffusion-strain responses are orthogonal in the fixed
weighted space, with `action <= ||U||2^2 <= 9 action/8`. The finite
shell-residual equation retains the complete nonlocal Riesz/rotation
commutator rather than discarding it as transport.

These component proofs are author-checked and await independent audit.
The weighted acceleration and strain action are locally finite, not
bounded from arbitrary data uniformly at the endpoint. The original
critical estimate remains unproved; no graph gap or predecessor audit is
promoted. `make check-material` tests source integrity, exact constants,
projection/covariance algebra and six nonlinear finite-atom response probes
including a zero atom; it is not an analytic proof or an independent audit.
