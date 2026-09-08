# Navier--Stokes: regenerative turnover after exterior escape and spectral mixing

This is the sole live status record. NS-R3 remains original unforced incompressible
Navier--Stokes on R3, every real solenoidal Schwartz datum, fixed positive viscosity,
global smooth velocity and normalized pressure. It is NOT PROVED. No infinite
original-NS cascade, turnover contraction, arbitrary-data RF-q producer, or continuum
hexagon turnover certificate has been obtained.

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: no-atom-full-state-block-cost-2026-09-08
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: original-nonlinearity-critical-producer-unresolved
active_architecture: full-real-vector-regeneration-with-nonperturbative-exterior
complete_terminal_route: none-established
terminal_status: not-proved
terminal_obstruction: input-only-critical-bound-not-produced
dominant_research_nut: vanishing-energy-regenerative-core-with-inherited-exterior
refinement_wave: reviewed-conditional-consumer-preserved
run_status: no-atom-block-cost-and-noncompact-class-exclusion-no-terminal-breakthrough
averaging_gate: exact-proof-assumptions-not-lane-names
averaging_audit: preceding-proof-repair-required
averaging_repair: author-proof-independent-audit-pending
incumbent_producer_class: averaging-invariant-budgets-remain-excluded
circuit_results: author-proof-independent-audit-pending
immediate_fractional_leakage: refuted-in-stated-varying-input-class
clean_six_carrier_embedding: refuted-in-stated-pairwise-clean-ring-class
side_ring_automatically_stabilizes: refuted-at-initial-critical-curvature
cartesian_phase_escape: refuted-by-exact-odd-invariance
helical_phase_torque: not-refuted-and-not-controlled
diagonal_signed_helicity_producer: refuted-when-budget-vanishes-on-zero-histories
common_meridional_ring_closure: refuted-by-full-second-jet
minimal_degree_side_ladder: all-orders-author-proof-with-viscosity
indefinite_original_ns_cascade: neither-constructed-nor-excluded
local_pressure_restoring_sign: refuted-with-arbitrary-remote-trace-free-hessian
pressure_results: author-proof-independent-audit-pending
narrow_miller_packet_shadowing: excluded-if-critical-exterior-is-uniformly-small
narrow_packet_result: author-proof-independent-audit-pending
finite_original_ns_spectral_cascade: arbitrarily-many-finite-events-author-proof
finite_mixing_cascade_concentrating: false-in-stated-varying-input-class
regenerative_critical_cascade: not-constructed
mixing_result_audit: independent-mathematical-audit-pending
acute_decomposable_fourier_cone: proved-trivial-author-audit-pending
convex_decomposable_fourier_cone: proved-linear-author-audit-pending
independent_packet_orthant: outgoing-face-for-nonzero-clean-triad
cone_boundary_exterior_cost: necessary-L2-amplitude-not-turnover-or-summable-cost
correlated_full_state_cones: not-generally-excluded
full_source_scale_cycle: exact-source-map-only-author-audit-pending
full_time_tree_equals_source_composition: refuted-at-four-leaf-order
full_state_return_map: exact-partial-augmented-map-author-proof
localized_compact_return_class: excluded-at-high-amplitude-in-stated-class
material_vorticity_turnover: exact-viscous-defect-bound-author-audit-pending
small_power_vorticity_tail_implies_critical_cost: refuted-by-Schwartz-satellites
no_atom_ns_endpoint: vanishing-viscosity-and-dissipation-author-proof
full_state_block_cost: positive-normalized-viscous-cost-in-stated-class
noncompact_bounded_enstrophy_returns: excluded-in-stated-class-author-audit-pending
input_summable_critical_regeneration_cost: not-produced
regenerative_turnovers_certified: 0
source_symbolic_checker: repaired-tuple-comparison-10-checks
secondary_goal: MIC-R3
secondary_goal_status: kinetic-and-microscopic-interfaces-remain-separately-gated
formal_work_this_run: deferred
public_release: false
```

## 1. Exact terminal edge and complete consumer

For actual whole-space projected flows, N_j=2^j N0 and
`e_j=u_(N_(j+1))-u_(N_j)`, the exact full-error identity is

    (1/q) Wq_M' + nu Dq_M = Piq_M,
    Piq_M=sum_j N_j^(q/2)||e_j||2^(q-2)
                    [<F_j,e_j>-b(e_j,u_j,e_j)].

For one fixed finite q>3 the missing input-only estimate remains

    integral_0^t Piq_M <= nu integral_0^t Dq_M+C(d,nu,H,N0,q)

for EVERY upper time t<=H and uniformly in M. Schwartz initial shells have
bounded Wq_M(0), so this gives RF-q. RF-LQ-SYNTHESIS gives a uniform finite
L^{3,q} bound; RF-LOCAL-ID and Lorentz Fatou identify the classical branch;
RF-LQ-CONTINUATION excludes a finite endpoint; LOCAL and ENERGY supply the
normalized pressure, initial trace and NS-R3. No new result below supplies this
upper estimate for arbitrary data.

Before pursuing any lemma X, write explicitly how X plus already proved nodes
implies this boxed producer or another accepted critical continuation producer.
If X merely introduces another unknown critical norm, strain clock, tail budget
or unproved singularity reduction of comparable difficulty, it is not the main task.

## 2. Quantitative narrow-packet escape: small exterior is impossible for a singular replica

Base result: commit `0837bef4240d65ace63b03c90fbe06f8e21819d1`.
Evidence: `research/evidence/2026-09-08-narrow-packet-escape.md`.
AUTHOR proof, independent mathematical audit PENDING. No canonical promotion.
The preceding PLAN before that theorem remains archived at
`research/history/PLAN-before-narrow-packet-2026-09-08.md`.

For a symmetric Fourier set Gamma assume shell volume at most M L^(12/5) and

    |p cross q| <= A |p|^(4/5)|q|,    |p|<=|q|, p,q in Gamma.

The exact original-NS symmetrized symbol gives

    |T(g)| <= C_Gamma ||grad g||2 ||Lambda^(1/2)g||2
                                      ||Lambda^(3/2)g||2,
    C_Gamma=C_* A sqrt(M),

and for h=u-P_Gamma u the full mixed estimate, with all exterior/reverse
interactions retained,

    |T(u)-T(P_Gamma u)| <= C_mix ||Lambda^(1/2)h||2
                                          ||Lambda^(3/2)u||2^2.

Hence the hypothesis

    ||Lambda^(1/2)h||2 <= nu/(4 C_mix)

forces an input-controlled H^(1/2) bound through the ordinary energy integral
of enstrophy. Narrow Miller-type packet combs with axial frequencies 2^m and
transverse radii / packet widths O((sqrt(3))^m) therefore cannot support blowup
while their critical exterior remains uniformly perturbative. Any singular
shadowing of that architecture must repeatedly carry a NONPERTURBATIVE high
critical exterior. The result allows arbitrary phases and polarizations and
retains reverse interactions. It does not control the required exterior or
prove that its appearance has an input-summable cost.

Fixed relative-width packets, changing axes, broad angular repopulation,
large exterior tails and genuinely full-vector regenerative cells remain alive.
Do not return to a narrow common-axis packet ansatz and assume its exterior is
small; that branch is now rigorously excluded in its stated class.

## 3. Full-duration original-NS spectral mixing: spectral gain is not regeneration

Evidence: `research/evidence/2026-09-08-full-duration-mixing-cascade.md`.
Frozen proof input `c2c34f870ed0fad5f14030629c5bbf5363006f98`; integrated here on top of
the newer narrow-packet theorem. AUTHOR proof, independent mathematical audit
PENDING. The auxiliary shear/slow-variation architecture is prior art; the new
claims are the quantitative full-equation transfer statements and RF adapter.

For any prescribed finite J, nu,H>0, finite q>3 and 0<eta<1/100 there are real
central-odd compactly supported smooth solenoidal R3 data and an ACTUAL original
NS solution smooth through a finite sequence

    s_*=2/A,    t_j=3*8^j/A<=H,    K_j=8^j,    0<=j<=J,

such that, writing E0=||d||2^2,

    ||1_(|D|>11/10)u(s_*)||2^2 >= E0/4,
    || |D|^(1/2)u(s_*)||2^2 >= (6/5)|| |D|^(1/2)d||2^2,

and at the later times

    ||1_(K_j<|D|<=6K_j)u(t_j)||2^2 >= E0/3,
    ||1_(|D|>K_(j+1))u(t_j)||2^2 <= E0/100,
    C(u(t_(j+1))) >= 5 C(u(t_j)),
    C(u)=|| |D|^(1/2)u||2^2.

The disjoint bands imply at least 97E0/300 new energy above the next threshold
between successive observations. The whole finite sequence can simultaneously
have

    ||(-Delta-1)d||2 <= eta||d||2,
    2nu integral_0^t_J ||grad u||2^2 <= eta E0,
    sup_t ||(u-u_P)^h||2 <= eta||d||2,
    sup_t | ||u(t)||_(3,q)/||d||_(3,q)-1 | <= eta.

All generated 3D modes and all return terms of the actual equation are retained
through a full H^s residual/stability estimate. Small `u-u_P` horizontal loading
measures the driving planar pump only; it does NOT mean small total feedback.
The auxiliary two-way Fourier ladder is infinite, not hand-truncated.

The data depend on J and eta, and t_(j+1)=8t_j: this is NOT an accumulating or
self-regenerating cascade. The daughter does not reproduce its driver. The
critical Lorentz norm stays almost unchanged. These examples may even be chosen
inside the published Chemin--Gallagher global-smooth slowly-varying class.
Thus repeated forward spectral transfer and large squared-Hhalf growth alone do
NOT diagnose concentrating regeneration or approach to blowup.

The result reaches the actual RF integrand in the opposite direction. With the
repository's cycles-frequency convention and N0=1/pi,

    sup_M integral_0^t_j [Pi_q,M-nu D_q,M]
      >= (E0^(q/2)/q)[c_q K_j^(q/2)-B_q eta^q],

with explicit c_q,B_q in the proof. This is a LOWER bound. It refutes no
arbitrary full-input upper remainder C(d,nu,H,N0,q).

The exact passive high-frequency ladder has zero self-regeneration: its daughter
cannot drive the next daughter. This is the decisive distinction from the next
negative construction. Energy-unitarity, small viscosity cost, small driver
loading and many spectral births can coexist with nonconcentrating smooth flow.

## 4. ONE dominant nut: a genuine critically timed regenerative turnover carrying the exterior

The two new obstructions point to the same target. A candidate singular cell
must simultaneously:

1. transfer order-one critical amplitude forward on a scale-local nonlinear
   clock, not a fixed coarse mixing clock;
2. make the daughter capable of driving the NEXT transfer;
3. retain the nonperturbative angular exterior required by Section 2;
4. retain all parents, side daughters, difference channels, reverse channels,
   pressure, changing polarization and inherited broad tails;
5. repeat on shrinking physical time scales compatible with viscosity;
6. either force growth of an accepted critical norm, or produce an input-summable
   loss/cost that feeds Section 1.

Do not assume a narrow packet shadow with a small exterior. Do not infer
regeneration merely from growth of H^(1/2), enstrophy, frequency moments or a
high-pass energy fraction. Do not reset a daughter to a clean initial packet.
The second cell must start from the ENTIRE actual output of the first.

### 4.1 Regeneration diagnostic that passive mixing cannot fake

Fix a smooth radial multiplier psi supported in (2/3,5/3), equal to one on
[3/4,3/2], 0<=psi<=1. Let Q_K have symbol psi(|xi|/K) in angular frequency,
let v_K=Q_Ku and define

    a_K(u)=K^(1/2)||v_K||2,
    gamma_K(u)=||Q_(2K) P[(v_K.grad)v_K]||2
                         /(K^(5/2)||v_K||2^2),

with gamma_K=0 if v_K=0. This is a diagnostic of the ACTUAL trajectory, never
a replacement equation. If G is the Schwartz kernel of Q_1, then

    gamma_K(u) a_K(u) <= 2||G||_(3/2,q') ||u||_(3,q),
    1/q+1/q'=1.

Thus a recursion with a_K growing without bound while gamma_K stays bounded
below would force growth of the very finite-Lorentz norm used by the terminal
consumer. The passive mixing example has high-frequency gamma_K=0 and cannot
fake this. No converse or singularity-extraction theorem is claimed.

### 4.2 Explicit finite falsification hurdle, not a mandatory architecture

In angular Fourier variables take sigma=(1,1,1), the six permutations S of
(2,1,0), K0=sqrt(5), a fixed even nonnegative smooth bump phi in the unit ball,

    phi_delta(xi)=delta^(-3/2)phi(xi/delta),
    f_delta_hat(xi)=-i P_xi sum_(k in S)
                    (P_k sigma)[phi_delta(xi-k)-phi_delta(xi+k)],
    d=A f_delta,    delta=2^(-m), m>=5,    nu=1/100.

These are exact real odd solenoidal Schwartz data. A useful concrete question is
to find parameters and actual smooth times 0=t0<t1<t2, K_r=2^rK0, with
`gamma0=gamma_K0(d)>0`, such that for r=0,1

    a_(K_(r+1))(u(t_(r+1))) >= (6/5)a_(K_r)(u(t_r)),
    gamma_(K_(r+1))(u(t_(r+1))) >= gamma0/2,

and

    1/[10 gamma0 a_(K_r)(u(t_r)) K_r^2]
       <= t_(r+1)-t_r
       <= 10/[gamma0 a_(K_r)(u(t_r)) K_r^2].

The SECOND leg must evolve the complete actual u(t1), including the
nonperturbative exterior. Proving this finite benchmark is not enough for an
indefinite cascade; it would need a robust output-neighborhood/shadowing theorem
with tail inheritance. Refuting it eliminates only this family and thresholds.
The model has MAXIMUM FLEXIBILITY to abandon this family immediately if a
better exact cell, positive turnover identity, concentration-compactness
extraction, pressure-multipole budget, packet algebra, microlocal mechanism or
other original-NS-specific architecture is more promising.

### 4.3 Retained periodic full-ring hurdle

The earlier periodic hexagon remains a secondary falsification test: nu=1/100,
initial coefficients -i P_k(1,1,1) at permutations of (2,1,0) plus reality,
E0=72/5 and S0=36sqrt(5)/5. Numerical Galerkin discovery suggests a time
tau<=1/4 with at least E0/5 outside the parents and at least 1.1*S0 squared
Hhalf/2, but there is still no continuum remainder/lifespan certificate.
Straight high-Sobolev posteriori bounds on the measured discarded residual were
not small enough in the current diagnostics. This is not a proof of failure.

A positive one-turnover event is now only a prerequisite. The decisive issue is
whether the resulting full state regenerates another critically timed driver,
or whether the mandatory exterior/polarization/pressure response carries an
input-summable loss.

## 4a. New exact cone obstruction, not a regenerative-event theorem

Evidence: `research/evidence/2026-09-08-fourier-cone-obstruction.md`.
AUTHOR proof; independent mathematical audit PENDING. No canonical promotion.

For original R3 NS at every fixed nu>0, a closed convex acute L2 cone that
permits arbitrary symmetric Fourier restrictions and is locally invariant
for its smooth finite-energy data must be ZERO. A Fourier-hole argument
first puts the entire quadratic vector field into the cone; acuteness and
energy cancellation force it to vanish; the exact unequal-length Leray
pair classification and Lebesgue differentiation then force zero Fourier
support. This is a continuum theorem, not a finite Galerkin classification.

Separately, three independently activatable orthonormal Schwartz packets
with zero measured self-pumps have cyclic coefficients summing to zero,
so a nonzero triad forces an outgoing face in every fixed-sign orthant.
The explicit packet triple has coefficients (-beta,-beta,2beta). Repairing
its negative face with the actual exterior h requires

    beta bc <= ||grad f1||infinity (2 sqrt(b^2+c^2)||h||2+||h||2^2)
                   +nu ||Delta f1||2 ||h||2.

This is a snapshot full-state L2 tangency bound, NOT angular-critical
control, viscous expenditure, a turnover loss or an input-summable budget.
The same exterior can be reused. Correlated amplitudes evade independent
activation: the exact abstract triad with x=y is a positive pump, but its
full original-NS packet realization still has nonzero side and polarization
outputs. It is not a closed NS cell. Odd phase-line invariance is preserved.

Consequent branch cut: do not seek a nontrivial invariant acute cone with
arbitrary Fourier deletion, or an invariant independently loaded clean
packet orthant with a nonzero triad. Correlated full-state invariant sets,
sign changes and non-decomposable packet architectures remain live. The
terminal nut in Section 4 and the signed RF-q upper producer are unchanged.

## 4b. Acuteness-free classification: every decomposable invariant convex cone is linear

Evidence: `research/evidence/2026-09-08-convex-cone-linearity.md`.
AUTHOR proof; independent mathematical audit PENDING. No canonical promotion.

For a fixed nu>0, let K be a closed convex cone in real L2_sigma(R3),
closed under EVERY symmetric measurable Fourier restriction. Assume local
invariance under the original NS flow for every member in the intersection
of all integer H^m spaces. Then

    K = K intersect (-K): K is a real LINEAR subspace.

In particular every pointed such cone is zero. Acuteness and any uniform
polarization aperture are unnecessary. The proof splits off lineality,
builds a measurable strictly dual-positive section in the pointed Fourier
fibers, kills a possible lineality output with a two-sided energy test,
and exhausts the nonuniform dual margins. The predecessor's original Leray
pair rigidity then kills the whole pointed component. Its Fourier-hole
argument concerns actual unprojected NS, not Galerkin closure.

Widening a pointwise polarization cone or adding arbitrary linear directions
therefore cannot repair an independently deletable one-sided cone. The real
odd sector is a sharp surviving LINEAR example. Nondecomposable correlated
cones, non-conical sets, nonconvex traps and return-time-only invariance are
not excluded. Invariance merely for Schwartz members is not silently promoted
to the stated all-H^m hypothesis after sharp Fourier deletion.

This supplies no turnover cost, angular-exterior budget, event extraction or
RF-q upper bound. The one dominant terminal nut remains the correlated full-
state regenerative return of Section 4, retaining the mandatory exterior.

## 4c. Full source cycles are possible; complete flow recurrence is different

Evidence: `research/evidence/2026-09-08-source-cycles-and-newborn-efficiency.md`
at the refreshed input `89e121f53c31da9e546fda3130ffd281983c2a63`.
The exact planar field U=(sin(x+y),sin(2x)-sin(x+y),0) obeys
N(N(U))=(1/5)U(2.), with the difference channel indispensable. Schwartz
approximations retain the inherited source error. This kills any universal
no-go based on original quadratic source copying alone.

The full four-leaf time tree is not N composed with N: its copied carriers
have different gains and it creates an exterior carrier. The ring's newborn
packet efficiency can exceed 0.51 of the parent's, but newborn amplitude
tends to zero. Neither result is a critically timed regenerative turnover.
The actual full-state return, not source composition, remains the object.

## 4d. New full-state finite-block exclusion and its sharp critical limitation

Evidence: `research/evidence/2026-09-08-full-state-vorticity-return.md`.
AUTHOR proof; independent mathematical audit PENDING. No canonical promotion.
The material small-power mechanism has Chae--Tsai prior art; no priority claim.

For the ENTIRE original NS state set V(y)=u(t,x+y/K)/(a K),
a=K^(1/2)||Q_K u(t)||2 and mu=nu/a. Evolve W with viscosity mu over theta,
then define

    g=sqrt(lambda)||Q_lambda W(theta)||2,
    Vplus(z)=(g lambda)^(-1) O^T W(theta,c+Oz/lambda),
    muplus=mu/g.

This is an exact partial augmented map, with canonical pressure and all
exterior retained. No globally defined event selector or recurrent set exists
in the proof. Growing a forces an Euler boundary; it is not suppressed.

For 0<p<=1 let S_p(V)=integral|curl V|^p / ||V||2^p. The exact material
Cauchy formula, with the entire viscous defect E, gives on a full interval

    S_p(Vplus) >= lambda^(3-5p/2) exp(-p ell)(1-eps) S_p(V),
    ell=log sup||D Phi_theta^(-1)||op,
    eps=exp(p ell)||E||_Lp^p/integral|curl V|^p <1.

FULL energy cancels g. This is not an input-summable critical cost.

A stronger finite-block theorem needs NO small viscous Lp-defect assumption.
Fix a full-state L2-compact class with ||Q_1 V||2=1, uniform H^s bounds
(s>=6), integral|curl V|^p<=B, and uniformly H^s-bounded full normalized
flow intervals of duration <=Theta and endpoint compression <=L. Let
lambda in [lambda0,Lambda], lambda0>1, g>=g0>1, and

    r=lambda0^(3-5p/2)exp(-p L)>1,
    b=(4/9)Momega^(p-2)M^(-p).

For any integer N with b r^N>B there is mu_*>0 forbidding N consecutive
returns in this class starting at mu<mu_*. The proof derives a complete
finite Euler boundary block by GLOBAL L2 convergence, retains energy and
canonical pressure, bounds translations rather than discarding exterior,
and contradicts its material-volume inequality. The threshold is qualitative,
not numerically validated. This excludes indefinite high-amplitude returns
in the stated localized compact class, not arbitrary full-state recurrence.

Under the other class hypotheses a putative infinite return must accumulate
unbounded small-power vorticity mass outside every fixed normalized ball.
But exact Schwartz satellites h_R=R^(-3/2-beta)h((x-R^2 e1)/R), with
0<beta<3/p-5/2, tend to zero in all H^s and finite L^{3,q} while their
vorticity Lp mass diverges. Thus this forced tail mass is NOT a critical
Lorentz-growth detector or a positive expenditure. At the critical power
p=6/5 the favorable geometric exponent itself vanishes.

Consequent branch cut: no uniformly localized smooth compact high-amplitude
trap as quantified above; no promotion of small-power tail growth alone to
RF-q. Still live are noncompact or tail-accreting full-state returns, loss of
uniform normalized smoothness/compression, and a genuinely critical dynamical
cost. No positive regenerative turnover, shadowing or blowup-event extraction
is certified. The dominant nut is the full-state return with this inherited
exterior, either shadowed concentration or a REQUIRED critical cost plus
extraction and the complete Section 1 consumer.

## 4e. Full-state block cost WITHOUT spatial compactness or small-power tails

Evidence: `research/evidence/2026-09-08-no-atom-regenerative-blocks.md`.
AUTHOR proof using the directly inspected Chae--Wolf Euler no-energy-atom
corollary; independent mathematical audit PENDING. No canonical promotion.

A new uniform endpoint lemma retains the full local NS energy identity:
uniform finite energy and `(T-t)||grad u||infinity<=A`, together with
viscosity AND total dissipation tending to zero, cannot produce an endpoint
energy atom. The proof takes only LOCAL strong limits, controls the remote
canonical pressure by its actual kernel, and passes the final energy via
an integrable time-flux bound. No global energy tightness is assumed.
The Euler no-atom result is imported prior art, not a new theorem claimed here.

For the existing full-state map, fix theta in [theta0,Theta], lambda>=lambda0>1,
g>=g0>1 and a uniform bound L for grad W in L-infinity on every WHOLE normalized
interval. Bound ||V||2 only at the first and final endpoints by M0, and require
final gamma_1>=gamma_*>0. Then constants N_*,mu_*,delta_*>0 forbid any block
of N>=N_* returns, initial mu<=mu_*, with normalized viscous expenditure

    Dblock=2 mu integral_block ||grad u||2^2 <= delta_*.

Thus a sufficiently long return must pay a positive full-interval viscous
cost IN THIS CLASS. No compactness, small-power vorticity, uniform compression,
upper scale/gain ratio, or intermediate normalized-energy bound is used.
The proof derives its Type-I bound from the actual clocks, rather than
assuming Type I for hypothetical arbitrary NS blowup.

If also ||grad W||2<=M1 throughout the full tubes, exact energy scaling gives

    Dblock <= [2 Theta M1^2 M0^2/(1-g0^(-1))] mu.

This excludes long high-amplitude returns even in NONCOMPACT classes, and
excludes an infinite orbit with recurrent jointly energy-bounded/efficient
endpoints under those uniform tube bounds. It strictly removes the predecessor's
spatial-compactness and small-power-tail assumptions. All exterior, reverse
channels, rotations, phases and pressure are retained. Thresholds are qualitative;
no numeric N_* or positive regenerative turnover is certified.

The physical cost is `(a_start^2/K_start) Dblock`. That weight can vanish.
Ordinary energy summability therefore does NOT bound the number of normalized
costs. No arbitrary blowup-event extraction or RF-q producer follows.
The one dominant nut is now a full-state critically regenerative return outside
these bounds, especially a vanishing-energy critical core with inherited bulk
and unbounded normalized full energy: construct and shadow it, or prove a
REQUIRED critical cost with extraction and the complete Section 1 consumer.
Unbounded normalized gradients or failure of the fixed clocks also remain live.

## 5. Preserved exclusions and surviving mechanisms

Preserved exact negative scopes:

* critically large first birth need not create a fixed immediate leakage fraction;
* the pairwise-clean hexagon necessarily creates a stronger side ring and that
  side ring initially contributes with the SAME dangerous critical sign;
* real central-odd data preserve a Cartesian imaginary Fourier line and zero
  signed helicity at every frequency, while actual RF work can be arbitrarily
  large on varying inputs;
* isolated clean equal-length two-carrier pumps reduce to a 2D3C passive sector
  and do not regenerate their planar driver;
* remote compact swirls prescribe the full trace-free pressure Hessian while
  fixing the entire local velocity germ, with the proved distance/energy cost;
* zero-centered entire causal reconstruction, polynomially conditioned moving
  metrics and polynomial source-linear response fail in their stated classes;
* narrow Miller-type packet replication with uniformly perturbative critical
  exterior is excluded by Section 2.

Still alive: full-turnover back reaction with a nonperturbative exterior,
helical/polarization angle frustration, unsigned angular broadening, nonlocal
pressure multipole histories, material-cotangent frequency dynamics, a
trajectory-selected quantized event cost, a stronger minimal-blowup extraction,
and a genuine full-vector scale-repeating NS cell. None is presumed correct.

The exact Tao discriminator remains original convolution support k=p+q with the
actual Leray numerator. Tao's assigned same-carrier pump coefficient violates
that support identity. The narrow-packet theorem additionally uses the exact
small-angle numerator. The mixing theorem additionally uses an exact 2D3C
transport reduction. None of these discriminators alone yields the positive
RF-q producer.

## 6. Validation and remote-write discipline

For the narrow-packet theorem, the previous run reported 1889 new exact
assertions plus 54 circuit, 45 pressure and 82 phase-ring assertions, with the
research-only verifier, syntax and whitespace passing on the full source tree.
Those checks belong to commit `0837bef4240d65ace63b03c90fbe06f8e21819d1`.

For the mixing theorem, `python3 research/check_turnover_mixing.py` passes 97
exact arithmetic/symbolic assertions: the complete shear equation and
Laplacian, infinite-ladder Taylor rows through degree eight, exact moments,
strict rational half-line inequalities, slow-coordinate divergence correction,
all residual components including vertical pressure, and scaling/RF constants.
It does NOT certify the analytic PDE adapter, the parameter limits, the imported
Chemin--Gallagher theorem, an independent mathematical audit, the hexagon
continuum turnover, scale regeneration or the RF-q upper bound.

For the cone theorem, the current run passed 2577 exact assertions over
1296 rational pair cases, and reran the 54 circuit, 45 pressure, 1889
narrow-packet, 97 mixing and 82 order-eight phase-ring assertions. The
full source snapshot's Git tree was checked equal to the live base tree;
`research/verify.py --research-only` passed with 29 canonical records and
8 pending supplements. Python syntax and whitespace were checked locally.
The CI workflow now also executes the cone, narrow-packet and mixing checks.
These are algebraic/structural checks, not validation of the continuum proof.

The acuteness-free extension passed 4568 exact assertions, including 59
nonacute rational cones, and reran all six preceding exact checkers with
the counts above. The full-checkout research-only verifier, Python syntax
and whitespace checks passed. Its separate exact checker,
`research/check_convex_cone_linearity.py`, covering symbolic quadratic energy
coefficients, nonacute rational cone margins, the two-sided lineality test,
exhaustion powers and sharpness examples. Its finite identities do not certify
the measurable-fiber construction or the continuum theorem. CI includes it.

The full-state-return theorem adds 116 exact symbolic/arithmetic assertions.
The full local source tree was reconstructed from the connected CI artifact
plus the four newer files and checked equal to input tree
`643b78c7286f8cb02901ea6a0f3ab1ba1cd67e29` before editing. The rational source
checker actually reports 12,351 assertions over 384 geometries at this input,
not the historical 12,357. The symbolic predecessor initially CRASHED on tuple
subtraction; its componentwise repair now passes 10 checks, not 11. The note
preserves these qualifications rather than silently validating old counts.

This run also passed the 204 Tao, 54 circuit, 45 pressure, 1889 narrow-packet,
97 mixing, 2577 acute-cone, 4568 convex-cone and 82 order-eight ring assertions.
The full-checkout research-only verifier, Python syntax and git diff --check
passed. CI now includes the source, repaired symbolic and new full-state
checkers. These are finite identity/integrity checks, not continuum validation.
Proof graphs remain unchanged and no independent audit is claimed.

The no-atom block contribution passed 341 exact finite identity checks over
24 rational clock sequences. The complete local source tree was recovered
from the connected CI artifact for 9c69d763 and its Git tree was checked equal
to e7fa62f6ed6589339fe48d2fd8d7ec5f29bceb1e before editing. All 11 predecessor
checkers above were rerun with the same actual counts (including 12,351 source
and 10 symbolic checks); the order-eight ring check again passed 82 assertions.
The full-checkout research-only verifier passed with 29 claim records and
8 pending supplements. Python syntax and git diff --check passed separately
after the combined test command reached its execution timeout following the
successful verifier output. No missing test is inferred from that timeout.
CI now includes the new checker. Finite identities do not validate the Euler
source theorem, compactness, endpoint limits, or qualitative PDE thresholds.

No independent mathematical audit is claimed for the new 2026-09-08 theorems.
No canonical graph, manuscript or formal status is promoted. Refresh main before
every write, preserve newer commits, use only ordinary fast-forward updates and
never force-push.
