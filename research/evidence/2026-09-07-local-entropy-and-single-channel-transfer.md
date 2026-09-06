# Terminal tests: local velocity entropy classification and single-channel transfer

Date: 2026-09-07.
Frozen research input: `0543d0c60b49d65d29ec80f66cacb3b7eaef9eb9`.
Status: complete author derivations; independent mathematical audit pending.
No novelty or priority claim, canonical graph promotion, or formal proof.
NS-R3: NOT PROVED. Terminal obstruction: UNCHANGED.

This note excludes two precise inference steps. The first is a classification
on actual local whole-space Navier--Stokes solutions, not just a snapshot
countermodel or a quadratic-functional result. The second concerns the
instantaneous nonlinear transfer of actual admissible initial data; it is
NOT a theorem about an entire evolving cascade. Neither proves blow-up.

## 1. Terminal gate and the mechanisms attacked

The target remains the original unforced equation on R3, all solenoidal
Schwartz data u0 and every fixed viscosity nu>0. LOCAL, ENERGY and
CONTINUATION in `docs/proof-graph.yaml` close the theorem once, for every
finite H, one proves from the inputs

    sup_{0 <= t < min(H,Tstar)} ||u(t)||_3 <= C(u0,nu,H) < infinity. (1.1)

This is the existing sufficient edge, not a new or strictly weaker criterion.
No least possible criterion among all regularity criteria is asserted.

**Nonlinear local-entropy mechanism.** Seek a fixed C2 density eta(z), with
eta(0)=0 and D eta(0)=0, such that F_eta(u)=integral eta(u(x)) dx is
nonincreasing on every classical branch and controls L3 together with energy.
For example, if constants A,B>=0 satisfy

    |z|^3 <= A |z|^2 + B eta(z) for every z in R3,                 (1.2)

then F_eta(u(t))<=F_eta(u0) and ENERGY give

    ||u(t)||_3^3 <= A ||u0||_2^2 + B F_eta(u0).

CONTINUATION excludes finite Tstar; LOCAL and ENERGY finish every NS-R3
clause. There is no extra unknown moment in this implication. The hardest
step is the universal monotonicity of the density, not the consumer.
Sections 2--6 prove that the only such monotone densities are nonnegative
multiples of kinetic energy. They cannot supply (1.2) or any L3 bound from
F_eta and energy alone. This rules out a nonlinear replacement of the local
velocity entropy, including eta(z)=|z|^3, not merely quadratic replacements.

**Full-vector cascade mechanism.** A genuinely dynamical theorem forcing a
nonsummable energy cost along every proposed singular cascade could instead
contradict ENERGY directly. The proposed shortest algebraic input was that
the Leray-projected interaction of noncollinear modes necessarily places a
uniform positive fraction in another daughter channel. Section 7 falsifies
that input, including a whole-space localized version. The stronger
finite-segment volume/branching mechanism in the existing architecture ledger
is not falsified: it would need an independent dynamical theorem and a
complete cascade-extraction/energy-accounting argument. None is proved here.

**Signed kinetic-memory mechanism.** The actual remainder in KPC Section 3
was also checked against its terminal consumer. Removing the pure macro
collision term still leaves the macroscopic convective flux. Estimating
that flux by absolute heat-kernel bounds and energy-class Holder estimates
returns an uncontrolled critical output: using L-infinity_t L3_x gives the
nonintegrable near-time kernel (t-s)^(-1), while the energy consequence
u tensor u in L1_t L3_x cannot control the supremum of its convolution with
(t-s)^(-1/2). These observations do not falsify a signed estimate restricted
to actual trajectories. The already-recorded L2-only stress obstruction is
not counted again as a new result, and no stress or adjoint infrastructure
was developed around the same failed estimate.

The durable change is the two scoped exclusions below. No proposed positive
producer in these attacks passed the terminal gate. In particular, this is
not a strict reduction of the remaining NS-R3 problem.

## 2. The local-entropy classification theorem

**Theorem E.** Fix nu>0. Let eta belong to C2(R3;R), with eta(0)=0 and
D eta(0)=0. Suppose that, for every real C_c^infinity solenoidal datum w,
the actual local classical unforced NS solution with viscosity nu satisfies

    F_eta(u(t)) <= F_eta(w)

for all sufficiently small t>=0. The permitted time interval may depend on
w. Then there is a constant c>=0 such that

    eta(z) = (c/2)|z|^2 for every z in R3.                        (2.1)

Conversely, every density (2.1) has the required monotonicity.

There is no convexity, evenness, isotropy, growth-at-infinity, or homogeneity
assumption on eta. It may depend on the fixed viscosity, but is the SAME
density for all data and is independent of time and position. Derivatives
of u, nonlocal terms, and evolving or datum-dependent densities are outside
the theorem. The normalization removes affine terms; it also ensures
|eta(z)|<=C_K|z|^2 and |D eta(z)|<=C_K|z| on each bounded velocity range.
Thus F_eta is finite on every bounded L2 field encountered here.

### 2.1 Initial differentiation is legitimate

Use the canonical pressure

    p_w = sum_{i,j} R_i R_j(w_i w_j),
    -Delta p_w = sum_{i,j} partial_i partial_j(w_i w_j).

For a compact smooth w, this pressure is smooth, is O(|x|^(-3)) at infinity,
and has gradient O(|x|^(-4)). These follow by differentiating the Newtonian
kernel outside the support of w_i w_j; local smoothness follows from the
Poisson equation or the Fourier multiplier. In particular grad p_w is in
L1 and L2, and integral grad p_w=0. The last assertion follows by integrating
over expanding balls, whose pressure boundary term is O(R^(-1)).

LOCAL supplies differentiability of u at zero in L2, as well as a uniform
velocity bound on a short classical interval. The local bounds on D eta and
D2 eta imply, by Taylor's formula and L2 convergence, that

    d/dt F_eta(u(t)) at t=0 = integral D eta(w) dot partial_t u(0).

For example, the integrated Taylor remainder is bounded by
C ||u(t)-w||_2^2, which is O(t^2). The equation and integration by parts give

    d/dt F_eta(u(t)) at t=0 = -nu D_eta(w) - I_eta(w),             (2.2)

where

    D_eta(w) = sum_k integral D2 eta(w)[partial_k w,partial_k w],
    I_eta(w) = integral D eta(w) dot grad p_w.

No sign is presumed for D_eta. The convection term vanishes because
integral w dot grad eta(w)=0. Compact support and the normalization justify
the integrations by parts at the initial time.

## 3. Fixed-viscosity monotonicity forces exact pressure cancellation

For every kappa>0 take the distinct admissible datum w_kappa(x)=w(kappa x).
This is a dilation of INITIAL DATA, not a claimed solution symmetry.
The canonical pressure is p_w(kappa x). Changing variables gives

    D_eta(w_kappa) = kappa^(-1) D_eta(w),
    I_eta(w_kappa) = kappa^(-2) I_eta(w).

By (2.2) and the hypothesis of Theorem E,

    -nu kappa D_eta(w) - I_eta(w) <= 0.

Let kappa tend to zero with w and nu fixed. It follows that I_eta(w)>=0.
Next use w_sharp(x)=w(-x). This is another compact solenoidal datum, and
its canonical pressure is p_w(-x). Direct change of variables gives

    I_eta(w_sharp) = -I_eta(w).

Therefore

    I_eta(w)=0 for every compact smooth solenoidal w.             (3.1)

Evenness of eta is NOT used. Neither w -> w(-x) nor velocity sign reversal
is asserted to carry an NS solution into an NS solution. Only the validity
of both initial data and the derivative at their respective time zero is
needed. The viscosity never changes, and no inviscid solution or uniform
lifespan is assumed.

## 4. Compact constant-velocity plateaus probe every Hessian

Fix b in R3 and a smooth cutoff chi equal to one on B1 and zero outside B2.
Set

    A_b(x) = (1/2) b cross x,
    B_R(x) = curl[chi(x/R) A_b(x)].

Then B_R is smooth, compact and solenoidal, equals b on B_R(0), is uniformly
bounded in R, and obeys B_R(x)=B_1(x/R). Consequently

    ||grad p_{B_R}||_infinity = R^(-1)||grad p_{B_1}||_infinity.

Fix a compact solenoidal w and choose R large enough to contain its support
in the plateau. The cross stress is exactly b tensor w + w tensor b on all
of space. Its double divergence vanishes since div w=0. Thus, in the
canonical pressure convention,

    p_{B_R+w} = p_{B_R} + p_w.                                  (4.1)

Subtract (3.1) for B_R+w and B_R, using (4.1):

    0 = integral [D eta(B_R+w)-D eta(B_R)] dot grad p_{B_R}
        + integral D eta(B_R+w) dot grad p_w.                    (4.2)

The first integrand is supported in the fixed support of w; its integral
is O(R^(-1)). In the second term D eta(B_R+w) is uniformly bounded and
converges pointwise to D eta(b+w). Since grad p_w is in L1, dominated
convergence proves

    integral D eta(b+w) dot grad p_w = 0.                        (4.3)

This passage does NOT insert an infinite-energy constant flow into the
hypothesis. Every datum used before taking the limit is compactly supported.

Replace w by a v, with v compact and solenoidal. Use p_{av}=a^2 p_v,
subtract the zero term D eta(b) dot integral grad p_v, divide by a^3 and
let a tend to zero. The C2 Taylor expansion, uniform on the support of v,
gives

    integral (M v) dot grad p_v = 0,
    M = D2 eta(b),                                              (4.4)

for every such v and for EVERY b in velocity space.

## 5. The only constant matrices satisfying (4.4) are scalar matrices

The real symmetric matrix M can be diagonalized by an orthogonal coordinate
change. Solenoidality, pressure, compact support and (4.4) transform
covariantly, so assume M=diag(m1,m2,m3).

The following finite trigonometric field is a calibration, not yet an
admissible whole-space datum. Put

    psi(x,y)=cos x+cos y+cos(x+y),
    A=(0,0,psi),
    U=curl A=(-sin y-sin(x+y), sin x+sin(x+y), 0).

Its zero-mean periodic pressure is

    p_U = -cos x-cos y-(1/2)cos(x+y)-(1/2)cos(x-y)
          -(1/5)cos(2x+y)-(1/5)cos(x+2y).

Direct differentiation verifies
-Delta p_U=sum_{i,j} partial_i U_j partial_j U_i. If angle brackets denote
periodic mean, elementary sine/cosine orthogonality yields

    <U1 partial_1 p_U>=-1/4,
    <U2 partial_2 p_U>= 1/4,
    <U3 partial_3 p_U>=0.

Hence

    <(M U) dot grad p_U> = (m2-m1)/4.                            (5.1)

### 5.1 Whole-space localization, including the zero frequency

Let theta be a nonnegative, nonzero C_c^infinity function and let

    theta_L(x)=theta(x/L),
    v_L=curl(theta_L A)=theta_L U+R_L,
    R_L=grad theta_L cross A.

These are actual admissible compact initial data. Boundedness of A and U
and their derivatives gives

    ||R_L||_2+||grad R_L||_2 = O(L^(1/2)),
    ||grad v_L||_2 = O(L^(3/2)),
    ||v_L tensor v_L-theta_L^2 U tensor U||_2 = O(L^(1/2)).       (5.2)

L2 boundedness of the double Riesz transform makes the last pressure error
O(L^(1/2)). After integrating (4.4) by parts as
I_M(v_L)=-integral p_{v_L} div(Mv_L), its contribution is O(L^2).
Also

    div(Mv_L)=theta_L div(MU)+an L2 error of size O(L^(1/2)).

The product U_i U_j has finitely many Fourier carriers. For each nonzero
carrier q and each double-Riesz symbol m_ij(xi)=-xi_i xi_j/|xi|^2,
Plancherel and dominated convergence give

    ||R_i R_j(theta_L^2 exp(i q.x))
           -m_ij(q) theta_L^2 exp(i q.x)||_2 = o(L^(3/2)).       (5.3)

Indeed, the squared norm divided by L^3 is, in unitary Fourier convention,

    integral |m_ij(q+zeta/L)-m_ij(q)|^2
                         |Fourier(theta^2)(zeta)|^2 d zeta,

which tends to zero. The symbols are bounded and continuous at q!=0.

The ZERO carrier must not be discarded. Write C_ij=<U_i U_j> and
P0=sum R_i R_j(C_ij theta^2). Its whole-space contribution is P0(x/L),
by homogeneity of the multiplier. When paired with the leading divergence,
the normalized integral is

    integral P0(y) theta(y) div(MU)(L y) dy.

It tends to zero: theta P0 is in L1 and div(MU) is a finite trigonometric
sum with zero mean, so the Riemann--Lebesgue lemma applies to every carrier.
The L2 errors in (5.2) contribute O(L^2), including for this zero mode.

Combining these facts and averaging the remaining finite trigonometric
products proves the genuine whole-space limit

    L^(-3) integral (M v_L) dot grad p_{v_L}
        -> (integral theta^3) <(M U) dot grad p_U>.              (5.4)

Equation (4.4) makes the left side zero for every L. Since integral theta^3
is positive, (5.1) implies m1=m2. Permuting the coordinate planes gives
m1=m2=m3. Thus

    D2 eta(b)=c(b) I for every b in R3.                          (5.5)

## 6. Completion, actual counterexamples and precise entropy exclusion

The off-diagonal derivatives in (5.5) vanish, so each partial_i eta depends
only on the single coordinate z_i. The equal diagonal derivatives, for
arbitrary independent choices of z1,z2,z3, force those one-variable second
derivatives to equal a SINGLE constant c. This uses only C2 regularity,
not third derivatives. With the stated normalization,

    eta(z)=(c/2)|z|^2.

Its initial derivative is -nu c ||grad w||_2^2. Applying the hypothesis to
any nonzero compact solenoidal w gives c>=0. ENERGY proves the converse,
completing Theorem E.

The proof also constructs a violating actual local NS solution whenever
eta is not of the permitted form. If eta is not quadratic of scalar type,
some b has a nonscalar Hessian. Select the corresponding coordinate plane
in (5.1) and a sufficiently large finite L to make (4.4) nonzero. A small
nonzero a then makes the shifted integral in (4.3) nonzero. For a large
finite R, the difference expansion used in (4.2) shows that at least one
of B_R+a v_L and B_R has nonzero
I_eta. Reflect that datum in space when necessary to arrange I_eta(w)<0.
Finally choose kappa small enough that

    d/dt F_eta(u_{w_kappa}(t)) at t=0
       = kappa^(-2)[-I_eta(w)-nu kappa D_eta(w)] > 0.             (6.1)

All parameters are chosen in this order and are finite before applying
LOCAL. Every resulting datum is compact, smooth and solenoidal and the
viscosity is the prescribed fixed nu. A negative scalar quadratic is
already contradicted by its viscous derivative without this construction.
These are entropy-growth examples, NOT singular NS solutions. For the
concrete candidate eta(z)=|z|^3, D2 eta(e1)=diag(6,3,3), so the normalized
triad pressure work in (5.1) is -3/4 before the positive cutoff factor.

The surviving energy density cannot give critical coercivity, even when
energy is supplied as a second input. For any fixed nonzero compact
solenoidal phi, put phi_lambda(x)=lambda^(3/2) phi(lambda x). Then

    ||phi_lambda||_2^2=||phi||_2^2,
    F_eta(phi_lambda)=(c/2)||phi||_2^2,
    ||phi_lambda||_3=lambda^(1/2)||phi||_3 -> infinity.            (6.2)

In particular no surviving density satisfies (1.2). More generally, these
same two scalar values cannot give any finite uniform bound for L3.

### 6.1 Kinetic scope and what is not excluded

A kinetic entropy argument which transfers, with the matched initial value,
to F_eta(u(t))<=F_eta(u0) for one fixed local velocity density on EVERY
prepared fluid datum is subject to Theorem E. It cannot evade (6.2) merely
by making eta nonlinear. This is a conditional application of the theorem,
not a claim that every kinetic entropy has such a limit.

The exclusion does not cover spatial derivatives, nonlocal terms, genuine
trajectory information, datum-dependent densities, explicit time dependence,
or nonmonotone bounds with input-controlled additive production or a larger
multiplicative constant. The theorem is also not a classification of all
Euler invariants or all NS Lyapunov functionals. The existing quadratic
functional theorem has a different scope, including nonlocal quadratic
forms; neither theorem should be silently enlarged into the union of both
sets of premises.

## 7. A second architecture test: no compulsory second daughter channel

The full-vector cascade route cannot obtain branching just from the
existence of noncollinear modes and the Leray projection. An exact
calibration uses

    V=(cos y, cos x, cos x+cos y),
    p_V=sin x sin y.

Here div V=0, and direct differentiation gives

    (V dot grad)V+grad p_V=(0,0,-sin(x+y)).                      (7.1)

The parents are the two noncollinear wavevector pairs +/-e1 and +/-e2,
with polarizations (0,1,1) and (1,0,1), respectively. The projected
nonlinearity is NONZERO but has only the pair +/-(e1+e2). The difference
channel +/-(e1-e2) is identically absent. These are real divergence-free
vector interactions of the original equation, not scalar shell dynamics.
Viscosity contributes -nu V at the parent carriers and is not confused
with the nonlinear output in (7.1).

### 7.1 Compact whole-space data with arbitrarily small off-channel fraction

One bounded periodic vector potential is

    A_V=(-sin y, sin x, sin y-sin x),  curl A_V=V.

With the same cutoff theta_L, let w_L=curl(theta_L A_V). As above,
w_L is compact, smooth and solenoidal. Write N(w)=(w dot grad)w and let P
be the spatial Leray projection. Product differentiation gives

    ||N(w_L)-theta_L^2 N(V)||_2=O(L^(1/2)).

The trigonometric polynomial N(V) has only nonzero carriers. Applying the
bounded Leray multiplier and the proof of (5.3), now to its matrix symbol,
yields

    ||P N(w_L)-theta_L^2(0,0,-sin(x+y))||_2=o(L^(3/2)).          (7.2)

Fix two disjoint small Fourier balls around +(e1+e2) and -(e1+e2), avoiding
all other named carriers, and let Pi_plus be their Fourier projection.
The modulated field on the right of (7.2) has L2 norm asymptotic to a
positive constant times L^(3/2), and its fraction outside these balls tends
to zero. Consequently

    ||(I-Pi_plus) P N(w_L)||_2 / ||P N(w_L)||_2 -> 0.            (7.3)

The input w_L is correspondingly concentrated at the four parent carriers;
the cutoff corrections have relative L2 size O(L^(-1)). Equation (7.3)
refutes a universal positive lower bound on an additional daughter fraction
for such whole-space localized interactions. Each w_L is a legitimate
initial state for the actual local NS equation at the fixed viscosity.

This does NOT establish a closed finite Fourier subsystem, a sustained
one-way cascade, or a blow-up solution. Subsequent interactions can produce
other modes. It does not rule out a branching/volume theorem over a specified
finite amplification segment with additional dynamical hypotheses. It
retires only instantaneous, geometry-only compulsory branching, including
a uniform version asserted for arbitrarily accurate localized mode packets.

## 8. Research-state change and remaining terminal obligations

Retire the fixed C2 velocity-local nonlinear entropy producer whose asserted
monotonicity and coercivity would close (1.1). Retire the asserted uniform
second-channel fraction from noncollinearity and Leray geometry alone.
Preserve all earlier valid results and their distinct counterexample scopes.
Neither exclusion removes the actual nonlinear term from the equation.

The remaining terminal obligation is still an arbitrary-data input-derived
critical bound such as (1.1), or a complete direct contradiction to finite
Tstar. The existing LOCAL/ENERGY/CONTINUATION suffix remains available.
For kinetic closure, K_res's producer and its exact GSR/truncated-moment/
Leray identification adapter remain to be supplied. The additional particle
and infinite-volume obligations are downstream and do not substitute for
that analytic edge. The full-vector alternative still needs an actual
finite-segment dynamical mechanism, extraction and nonsummable accounting;
(7.1) cannot supply these. No positive architecture is declared proved.

Theorem E and (7.3) have author derivations and self-checks only. Independent
mathematical review and prior-art assessment are pending. Canonical graph
nodes, manuscripts, formalization, previous evidence and microscopic
contracts are not changed by this note.

## 9. Provenance and source boundaries

Repository inputs inspected: the live PLAN, AGENTS, `docs/proof.md`, the
terminal portion of `docs/proof-graph.yaml`, `research/verify.py`, KPC/KCH,
`literature/kinetic-hilbert-scope.md`, the terminal-reset architecture ledger,
and the recent intrinsic-record, viscous-mixing, quadratic/local-energy,
pointwise-vorticity/helicity and prepared-Fisher/stress-output evidence.

For background only, Terence Tao, "Conserved quantities for the Euler
equations" (2014-02-25), was inspected at the author's original page:
https://terrytao.wordpress.com/2014/02/25/conserved-quantities-for-the-euler-equations/
It discusses energy, helicity and pressure-gradient cancellations. It is
NOT cited as proving Theorem E, the compact-plateau argument, or (7.3).
The classification and localized-transfer statements above are derived in
this note; no claim of their novelty or independent certification is made.
