# Navier–Stokes regularity programme

Private research on the three-dimensional incompressible Navier–Stokes
Millennium problem. Start with [PLAN.md](PLAN.md), the sole live status,
then [the dependency graph](docs/proof-graph.yaml).

The [literature dossier](literature/README.md) records source scope and
verification limits. The companion `../navier-paper` contains the manuscript
and clickable proof map. Its private GitHub repository is the manuscript
authority; the current owner-authorized task also permits unsigned commits.
Document builds and claim audits are recorded separately. The former
Navier Overleaf project was deleted at the owner’s request on 2026-09-05.
The independently audited argument remains conditional on signed
high-frequency pressure control. No solution or completed formalization is
claimed; formalization status is tracked in `PLAN.md`.

A standalone paper-proof continuation and its author checks are indexed in
[the 6 September dissipation-budget evidence](research/evidence/2026-09-06-dissipation-budget-continuation.md).
This is an unpromoted review input, not a second live status record. It gives
a direct continuation path from strict absorption without ESS and a larger
family of conditional defect criteria; no arbitrary-data estimate is claimed.


## Current paper continuation (2026-09-06)


`PLAN.md` now records the explicitly authorized writable paper workflow.
The manuscript includes a review-pending dissipation-clock component; see
`research/evidence/2026-09-06-dissipation-clock.md` for its exact scope.
It removes ESS from the strict-pressure suffix and admits finite/logarithmic
dissipation barriers, but supplies no arbitrary-data pressure producer.
Run `python3 research/verify.py` with the paper and formal repositories
present. `--research-only` is an explicitly narrower structural check.

## Near-2 defect continuation (2026-09-06)

The manuscript now has complete author-checked component proofs of near-2
unweighted defect regularity and a quantitative reverse finiteness bound
from the fourth-power defect integral to the squared-enstrophy integral.
See `research/evidence/2026-09-06-defect-extensions.md`. Independent review
is pending; these are not an arbitrary-data regularity proof. The missing
producer and all terminal/gap statuses remain explicit in `PLAN.md`.


## Conformal moment checkpoint (2026-09-06)

The review-pending `navier-paper/sections/conformal_moment.tex` now answers
two spatial questions on the Schwartz-data branch: the cubic representative
has finite L2 energy, and its divergence defect belongs to L^(3/2).
Conformal inversion, the accepted div-curl bound and a noncircular Hardy
argument give the snapshot theorem under `|x| grad u in L2`; weighted energy
on the original equation supplies input-only spacetime moment budgets.
The proof, precise quantifiers and source checks are indexed in
`research/evidence/2026-09-06-conformal-moment.md`.

The new time-square defect norm is supercritical. The arbitrary-data
critical temporal producer and NS-R3 remain unproved. Independent audit is
pending, no formal status changes, and the graph records a separate pending
component instead of promoting a claim. `PLAN.md` remains the live authority.


## Signed-defect missing-bound reduction (2026-09-06)

The frozen component `navier-paper/sections/signed_defect.tex` proves an
exact scalar cancellation and a signed trace-free Hessian representation.
It removes the Leray factor from the fourth-power coefficient and supplies
a one-sided quadratic-form clock with an explicit critical amplitude-tail
certificate. See `research/evidence/2026-09-06-signed-defect.md`.

The original defect integral is now bounded explicitly in terms of that
form clock. Its arbitrary-data, endpoint-uniform time bound is still
**unproved**; no critical or terminal claim is promoted. The source is
author-checked and awaits independent mathematical audit. The main
manuscript and generated map include this pending component; `PLAN.md`
records the remaining vector-evolution target.


## Speed-shell cancellation (2026-09-06; independent audit pending)

The paper now derives cancellation on every positive speed shell, a
measurable residual after removing speed-only functions, and scalar
corrections that leave signed work unchanged. The resulting effective-defect
and optimized form rates do not exceed their earlier counterparts.
Their endpoint-uniform time bound is still unproved. Full evidence and the
precise failed closure are in `research/evidence/2026-09-06-speed-shell.md`;
`PLAN.md` remains the sole live status. No open or formal claim is promoted.


## Regularized shell dynamics (2026-09-06; independent audit pending)

The new paper component proves natural-variable L2 time regularity, a
pressure-free weighted acceleration bound, and the exact evolution of
finite smooth speed-shell residuals with a positive ridge penalty.
`research/evidence/2026-09-06-shell-dynamics.md` records the proof and its
boundary: endpoint control of the evolution drivers and uniformity under
refinement remain unproved. `PLAN.md` is the sole live status. No open or
formal claim is promoted.

## Corotational material response (2026-09-06)

The paper now contains a full moving-metric response proof, including the
zero-set natural derivative, and an exact material law after removal of
rigid rotation. It isolates an orthogonal diffusion-strain action and
retains the nonlocal commutator in the finite shell-residual evolution.
These are author-checked component results, not an endpoint estimate;
independent audit remains pending. The next task is in `PLAN.md` and the
source/verification boundary is in
`research/evidence/2026-09-06-material-response.md`. All existing main claim
kinds and formal authorizations are preserved, including the open NS-R3,
HIGH-PRESSURE, HIGH-STRAIN and DEFECT-L4 nodes.
