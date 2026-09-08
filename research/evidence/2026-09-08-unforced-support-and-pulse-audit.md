# Unforced exactification: support rigidity and the pulse-seed inverse obstruction

Date: 2026-09-08. Frozen input: `fedb45a640ea8537aa90578f2cafda9adca01756`.
Status: AUTHOR PROOFS; independent mathematical audit PENDING.
Integration preserves concurrent `694be9648450dbb1528232e08d20ec07ace302d0`.
Its causal pulse-inverse obstruction overlaps the audit here; that overlapping
statement is not counted as a second new result or independent review.
No terminal, canonical-graph, manuscript, or formal promotion.

## 0. Consumer, source scope, and distinction from the forced claim

UE1 needs a correction of the full projected residual, with an admissible
initial trace, that preserves concentration. This note rules out three
particular proposed shortcuts to that inverse: obtaining an unforced terminal
slab without changing the localized velocity; keeping an exact open heat
exterior/axisymmetric-core patch; and feeding a Gaussian pulse's seeding tail
back through the same zero-initial-amplitude inverse as a small perturbation.
The first two obstructions concern the ORIGINAL whole-space equation. The
third concerns the manuscript's PRINCIPAL pulse equation, not a theorem about
the full nonlinear PDE inverse. That boundary is essential.

[OA] is the owner's 165-page PDF, *Finite Time Blowup for Navier--Stokes*,
at https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf,
accessed 2026-09-08. Main statement, Sections 2--3, 6--7, the residual split in
9.2, and localization in 10.1 were inspected; pages 1, 5, 63, 74--75, 78, 80,
86--87 were also visually inspected. This is a targeted conversion audit,
NOT independent validation of its 165-page forced construction. The CDN
binary could not be retrieved into the local container; no binary hash or
full-text local audit is claimed. No third-party PDF is added to this repo.

The relevant exact source locations are:

* Theorem 1.1 and Proposition 10.1: the stated global velocity has fixed
  compact spatial support and blows up, with an external smooth force.
* Theorem 3.1 and Section 2.3: an open local exterior is independent of z;
  nonzero angular waves have support away from the axis.
* (7.2), (7.12), (7.16), Lemma 7.4: Gaussian growing/decaying homogeneous
  principal pulses; Q=2^(-ell), epsilon=Q^h, S_*=ell^2, L_s comparable to S_*.
* (7.40): the exact principal cutoff remainder is
  `(1-psi) f_m + psi' t_m`. For a homogeneous primary pulse it is `psi' t_h`.
* Proposition 9.3, (9.3), and its proof on p.105: Gaussian nonzero-harmonic
  cutoff tails stay in the additive flat residual, outside later forward
  pulse inputs. The manuscript does NOT claim to cancel them to zero.

The first invalid inference in the proposed direct conversion would be:
"flat in Q, therefore small after the same causal pulse inverse." Section 2
below disproves that inference exactly. This is NOT an error asserted in the
forced manuscript, which explicitly retains these terms as forcing.

No result here gives the input-only RF-q producer. A successful replacement
would still need UE1 -> UE2 (nonlinear exact cancellation) -> UE3 (one global
Schwartz trace) -> UE4 (singularity). The reviewed positive consumer is intact.

## 1. Rigidity of exact spatial patches for unforced positive-viscosity flow

Throughout this section, u is a real divergence-free classical finite-energy
whole-space NS solution on (a,b), with fixed nu>0 and u in C_t H^s on compact
subintervals for every s. The pressure is the canonical unforced pressure.
These hypotheses hold for the repository's classical branch before an endpoint.

### Lemma 1: spatial analyticity, with a proof of the version used here

For every a<t<b the field u(t,.) is real analytic on all of R3.

Proof. Fix s>3/2. For alpha>=0, the Fourier convolution inequality and
Cauchy--Schwarz give

    ||e^(alpha Lambda)(fg)||_Hs
       <= C_s ||e^(alpha Lambda)f||_Hs ||e^(alpha Lambda)g||_Hs.       (1.1)

To see the constant is independent of alpha, use |xi|<=|eta|+|xi-eta|,
<xi>^s<=C_s(<eta>^s+<xi-eta>^s), Young's L2*L1 inequality, and
integrability of <xi>^(-2s). Replacing Fourier transforms by their absolute
values proves the vector/tensor version as well.

Restart the mild equation at a regular time c<t. On a short interval [c,c+d]
use the norm

    ||v||_X = sup_(0<=r<=d) ||e^(lambda sqrt(nu r) Lambda) v(c+r)||_Hs,

where lambda>0 is fixed. The linear heat term is bounded by
`exp(lambda^2/4)||u(c)||_Hs`. Since sqrt(r)-sqrt(s)<=sqrt(r-s), the remaining
heat multiplier, including one divergence derivative, has operator norm at
most C_lambda/sqrt(nu(r-s)). The Leray projector has norm at most one at each
nonzero Fourier frequency. Thus (1.1) bounds the bilinear mild term by

    C_(s,lambda) sqrt(d/nu) ||v||_X ||w||_X.                       (1.2)

For sufficiently small d, the contraction argument in a ball of radius
2 exp(lambda^2/4)||u(c)||_Hs gives a solution in X. Local uniqueness identifies
it with the given classical solution. On a compact regular time interval
||u(c)||_Hs is bounded, so c can be chosen sufficiently close to t that t is
inside this common local interval. Exponential Fourier integrability at t
then gives a holomorphic extension to a nonzero spatial tube (use any strictly
smaller tube and Cauchy--Schwarz). In particular u(t,.) is real analytic. QED.

Spatial analyticity is classical prior art, not a novelty claim. For historical
context see Giga, *Weak and Strong Solutions of the Navier--Stokes Initial Value
Problem*, PRIMS 19 (1983), 887--910, DOI 10.2977/PRIMS/1195182014, and the
analyticity work cited there. The argument above supplies our precise R3
version rather than importing a boundary-domain result.

### Theorem 2: no exact heat-exterior patch or compactly supported snapshot

At a positive time in an unforced classical interval:

(a) If u vanishes on a nonempty spatial open set, then u is identically zero
at that time.

(b) If partial_z u vanishes on a nonempty spatial open set, then u is
identically zero at that time.

(c) If u is axisymmetric on a nonempty spatial open set, then u is globally
axisymmetric at that time. In particular it cannot simultaneously have an
exactly axisymmetric open core and a nonaxisymmetric annulus.

Proof. Each component of u and partial_z u is analytic. The identity theorem
on connected R3 gives (a). For (b) it gives partial_z u=0 globally. A z-independent
L2(R3) field is zero by Fubini.

For (c), let Jx=(-x2,x1,0). The rotation generator

    D_rot u = (Jx.grad)u - Ju

has analytic components. It vanishes on the open set, hence everywhere.
Integrating this first-order identity along rotations gives
u(R_theta x)=R_theta u(x). QED.

These statements allow arbitrary noncompact tails outside the open patch;
they do not merely prohibit compact support. An exact heat exterior
`K(r,t)e_theta` on an open patch satisfies the premise of (b). An exact
axisymmetric inner patch with nonaxisymmetric waves farther out violates (c).
An unforced repair must therefore change those patches, possibly by extremely
small but nonzero leakage. No quantitative lower bound on that leakage is
claimed. Flatness as t approaches the endpoint is NOT spatial vanishing on
an open set at a fixed earlier time.

### Corollary 3: no unforced terminal slab in the localized source construction

Let U be any smooth compactly spatially supported, divergence-free velocity
on [0,T), in a fixed compact set, with limsup_(t->T)||U(t)||_infinity=infinity.
Define its full projected residual

    F_U = partial_t U - nu Delta U + P div(U tensor U).             (1.3)

For every t_*<T, F_U is NOT identically zero on (t_*,T) x R3.

Proof. If it were zero there, U would be an unforced classical solution on
that interval, with pressure reconstructed canonically. At every interior
time its compact support and Theorem 2(a) would force U=0. This contradicts
the blowup lower limit. QED.

Thus the velocity asserted by [OA, Theorem 1.1] cannot already have a terminal
unforced time slab. This conclusion uses only its stated support/regularity
and blowup properties, not correctness of the whole construction. It concerns
P f, so changing the trial pressure or removing a gradient part of f cannot
evade it. It does not say P f is nonzero at every individual time.

## 2. A flat seed is not a perturbatively small causal input

The following exact ODE lemma applies on a principal-pulse fiber. It must
not be relabelled a full-PDE quasimode theorem.

### Theorem 4: Gaussian pulse cutoffs force a superalgebraic inverse cost

Let Q=2^(-ell), S=ell^2, and c_L S<=L<=C_L S. Let C_Q(v) be a smooth matrix
on [0,L], possibly restricted to a smoothly moving invariant plane. Suppose
there is a homogeneous solution h_Q'=C_Q h_Q with

    |h_Q(L/2)| >= c_0 > 0,
    |partial_v^j h_Q(v)| <= C_j S^(b_j)
                         exp[-c (v-L/2)^2/L]                      (2.1)

for each fixed j, with constants independent of ell. Let psi(v) be a smooth
cutoff, zero near both endpoints, one near the midpoint, with its derivatives
supported where |v-L/2|>=c_1 L and bounded by fixed powers of S. Put

    a_Q = psi h_Q,
    r_Q = (partial_v-C_Q)a_Q = psi' h_Q.                            (2.2)

Then a_Q(0)=0, ||a_Q||_infinity>=c_0, but, for every fixed j,N,

    ||partial_v^j r_Q||_infinity <= C_j' S^(b_j') exp(-c' S),
    Q^(-N)||partial_v^j r_Q||_infinity -> 0.                        (2.3)

Consequently the zero-initial-value inverse cannot have a bound with only
any fixed algebraic loss in Q, even if its input norm contains any fixed
finite number of v derivatives. Its norm on these inputs is at least
`c exp(c' S)/S^b` for that derivative order.

Proof. Equation (2.2) is the exact product rule. On every derivative support
of psi, (2.1) has the factor exp(-c' S). Leibniz gives (2.3). The logarithm of
Q^(-N) S^b exp(-c' S) is

    N ell log 2 + 2b log ell - c' ell^2 -> -infinity.

Existence and uniqueness for the linear initial-value problem show that its
response to r_Q is exactly a_Q. The asserted inverse lower bound follows.
If the plane constraint is n(v).h_Q(v)=0, it also holds for a_Q and r_Q; this
residual is in the dynamical tangent plane, not a removable normal pressure
term. QED.

For the manuscript's principal system, C_Q=A_Phi-d I at harmonic m=1.
The uniform moving-frame bounds, (7.16), and Lemma 7.4 give (2.1). Fixed slow
or physical derivatives add only polynomial S factors and fixed Q powers,
which do not change flatness. This application relies on those inspected
principal bounds, not on the uninspected correctness of every later PDE step.

### Corollary 5: exact zero-trace cancellation deletes the primary pulse

The unique solution of

    (partial_v-C_Q) w_Q = -r_Q,  w_Q(0)=0

is w_Q=-a_Q. Hence a_Q+w_Q=0 throughout [0,L], including its leading quadratic
covariance. There is no small, zero-trace correction of this particular seed
residual that preserves the homogeneous primary pulse.

This explains rather than contradicts [OA]'s weighted inverse. In a norm
that divides by the Gaussian envelope P(v), psi' h_Q/P is NOT a flat input.
The polynomial bounds in Proposition 7.2 are envelope-weighted; they are not
bounds on arbitrary unweighted flat sources. The source explicitly keeps
these Gaussian tails out of subsequent forward wave inputs in Section 9.2.

### Proposition 6: exact free-trace filling DOES repair the principal seed

Under Theorem 4's hypotheses, suppose in addition that psi=1 throughout
|v-L/2|<=c_2 L for a fixed c_2>0. Set

    w_Q=(1-psi)h_Q,   w_Q(0)=h_Q(0).                              (2.4)

Then

    (partial_v-C_Q)w_Q=-r_Q,   a_Q+w_Q=h_Q,                        (2.5)
    ||partial_v^j w_Q||_infinity <= C_j S^(b_j) exp(-c'' S).        (2.6)

Thus a correlated, nonzero but flat initial trace repairs this principal
residual with a flat correction and preserves the whole homogeneous pulse.
Proof: (2.5) is the product rule; (2.6) follows because 1-psi is supported
in the Gaussian tails. No inverse estimate or limiting procedure is needed.

More generally every correction of -r_Q is

    w_Q(v)=-a_Q(v)+Phi_Q(v,0)c_Q,                                (2.7)

where Phi_Q is the full homogeneous fundamental matrix and c_Q the initial
trace. Setting c_Q=h_Q(0) gives (2.4); setting c_Q=0 gives Corollary 5. The
unstable transfer of an initial trace and the large causal forcing response
are the SAME exact linear dynamics, not conflicting estimates.

This completes principal seed cancellation with a freely assigned trace on
ONE pulse interval. It removes neither the other PDE residual terms nor the
need to continue its nonzero tails beyond the interval. In particular the
countably many values h_Q(0), prescribed at different pulse-start times,
cannot be chosen independently in an unforced Cauchy problem. They must be
the traces of ONE full preceding evolution with its inherited exterior and
feedback. The angular preparation note tests precisely that attempted
initialization, first for the original linearized operator and then for
the complete nonlinear equation.

## 3. Forcing audit outcome and unresolved route

UE0's terminal-slab shortcut is excluded by Corollary 3. The support-compatible
unforced completion of the source's exact open patches is excluded by
Theorem 2. At the principal pulse step, the first explicitly retained seeding
term is psi' h_Q; Theorem 4 and Corollary 5 exclude treating it as a small
zero-trace causal correction merely because it is flat.

Other flat terms remain: base-series summation, mean/potential cutoffs, and
final spatial and initial-time localization. Their full solenoidal parts
must still be included in any redesigned inverse. This note does not claim
that psi' h_Q is the only full forcing term, or that its principal tangent
projection is by itself the entire global Leray-projected residual.

The surviving route must allow nonzero interior/exterior leakage and solve
a global FREE-INITIAL-TRACE problem. The quantitative tests for its pulse
preparation are in `2026-09-08-angular-preparation-obstruction.md`.
No unforced counterexample, input-only critical producer, or independently
audited terminal theorem has been obtained. These are conversion obstructions,
not a refutation of the forced manuscript or a proof of unforced regularity.

The companion `2026-09-08-mixed-trace-principal-inverse.md` proves a positive
logarithmic-loss principal inverse after changing the trace constraints. Its
simultaneous realization by one whole-space Cauchy datum remains unproved.

The final integration also preserves the concurrent formal-core update
`dd074604f04ebd705583df8dba1d9d3e53df0793`; no formal file or status is promoted.
