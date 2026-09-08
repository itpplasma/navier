# Full-state NS returns: material-vorticity defect and compact-class exclusion

Date: 2026-09-08. Frozen input: `89e121f53c31da9e546fda3130ffd281983c2a63`.
Status: AUTHOR PROOF; independent mathematical audit PENDING. No canonical
proof-graph, manuscript, formal or terminal promotion. No priority claim.

## 0. Consumer gate and scope

This is a construction-obstruction theorem for the ACTUAL full-state flow,
not another proposed sufficient regularity criterion. Its consumer is the
negative construction lane: Theorem 3 excludes sufficiently small-viscosity
finite blocks, and therefore indefinite high-amplitude returns, in a stated
compact, localized class. It does not exclude every full-state recurrent set.
Theorem 4 proves why the resulting tail escape is not a critical-norm cost.

The missing terminal producer is still, for one fixed finite q>3,

    integral_0^t Pi_q,M <= nu integral_0^t D_q,M + C(d,nu,H,N0,q),

at EVERY upper time t<=H uniformly in M. Its complete existing consumer is
RF identity and Schwartz initial shells -> RF-q -> RF-LQ-SYNTHESIS ->
RF-LOCAL-ID and Lorentz Fatou -> RF-LQ-CONTINUATION -> LOCAL and ENERGY ->
original NS-R3 with normalized pressure. None of the new theorems supplies
that producer, an alternative continuation bound, or singularity extraction.

The material-vorticity/small-power mechanism has substantial prior art [CT].
The statements proved here concern nonperiodic variable-scale full-state NS
return blocks, include the exact viscous defect, cancel amplitude gain using
FULL energy, and derive their inviscid limit instead of assuming it. Neither
an immediate Taylor coefficient nor N composed with N is used.

## 1. Exact augmented return map, including effective viscosity

Use the fixed radial Q_K of PLAN, supported in 2K/3<|xi|<5K/3, with symbol
between zero and one. Work with real solenoidal H^s(R3) fields, integer s>=6,
and smooth solution intervals. Let a=K^(1/2)||Q_K u(t)||2>0. In a translated
coordinate chart define the ENTIRE normalized state and its evolution by

    V(y)=u(t,x+y/K)/(a K),       mu=nu/a,
    W(tau,y)=u(t+tau/(a K^2),x+y/K)/(a K).                (1.1)

Then ||Q_1 V||2=1 and, exactly,

    W_tau+P[(W.grad)W]=mu Delta W,     div W=0.            (1.2)

The canonical pressure is sum_ij R_i R_j(W_i W_j); it equals the physical
canonical pressure divided by a^2 K^2. There is no freely specifiable harmonic
pressure and no independently reset pressure variable. All tails, parents,
side modes and reverse channels belong to W.

For any theta>0 inside this solution's lifespan, lambda>1, c in R3 and
O in SO(3), write w=W(theta), and, provided Q_lambda w is nonzero, set

    g=sqrt(lambda)||Q_lambda w||2,
    Vplus(z)=(g lambda)^(-1) O^T w(c+Oz/lambda),
    muplus=mu/g.                                        (1.3)

These equations define an exact partial return map R_(theta,lambda,c,O) on
(V,mu), not on a finite carrier ansatz. It satisfies ||Q_1 Vplus||2=1.
The physical next scale and amplitude are lambda K and g a. Composition,
with the corresponding translated/rotated chart, gives the SAME original
solution with the SAME positive physical nu. In particular, repeated gain
g>=g0>1 sends effective viscosity to zero, not to a fixed positive value.

Local H^s well-posedness makes (1.3) well defined on its lifespan domain;
continuous specified selectors for theta, lambda, c and O give a single
partial map. No universal event-selection rule or global domain is claimed.
Euler mu=0 is a separate boundary map where its smooth local flow exists.
Theorem 3 constructs the required finite Euler boundary blocks from actual
positive-viscosity NS blocks; it assumes no global Euler theorem.

## 2. A finite-turnover inequality with the entire viscous correction

Let Omega=curl W and let Phi_tau(y) be the material flow of W, with
J_tau(y)=D Phi_tau(y). Smoothness and bounded velocity/gradient on a compact
time interval give a global diffeomorphism, det J_tau=1. The ORIGINAL NS
vorticity equation is

    (partial_tau+W.grad)Omega=(Omega.grad)W+mu Delta Omega.

Thus J'_tau=(grad W)(tau,Phi_tau)J_tau and variation of constants gives

    Omega(theta,Phi_theta(y))
      = J_theta(y) Omega(0,y)
        +mu integral_0^theta J_theta(y)J_r(y)^(-1)
                              Delta Omega(r,Phi_r(y)) dr. (2.1)

Define eta(Phi_theta(y))=J_theta(y)Omega(0,y), E=Omega(theta)-eta, and

    ell=log esssup_y ||J_theta(y)^(-1)||op >=0,
    I_p(v)=integral_R3 |curl v|^p,
    S_p(v)=I_p(v)/||v||2^p,           0<p<=1.             (2.2)

For the following nontrivial inequalities assume 0<I_p(V)<infinity and
||E||_Lp^p<infinity. The zero-defect Euler case needs only I_p(V)<infinity.
Because Phi preserves volume and |J_theta z|>=exp(-ell)|z|,

    integral |eta|^p >= exp(-p ell) I_p(V).

The pointwise subadditivity |eta|^p<=|Omega(theta)|^p+|E|^p gives

    I_p(w) >= exp(-p ell)I_p(V)-||E||_Lp^p.              (2.3)

This proof does not differentiate a singular power at a vorticity zero and
does not use a false Minkowski/Jensen inequality for p<1.

The exact return scalings and FULL energy inequality are

    I_p(Vplus)=lambda^(3-2p)g^(-p)I_p(w),
    ||Vplus||2^p=lambda^(p/2)g^(-p)||w||2^p,
    ||w||2<=||V||2.                                     (2.4)

Put eps=exp(p ell)||E||_Lp^p/I_p(V). If eps<1, (2.3)--(2.4) prove:

**Theorem 1 (viscosity-explicit full-turnover bound).**

    S_p(Vplus) >= lambda^(3-5p/2) exp(-p ell)
                                      (1-eps) S_p(V).   (2.5)

The amplitude gain g cancels exactly. No upper or lower estimate of g is
used in (2.5). Diffusion is not assigned a favorable sign: all its possible
material cancellation is contained in E. Even E depends on the full NS flow,
not on a separately evolved Euler approximation.

For consecutive returns with eps_n<1, the exact finite telescope is

    log[S_p(V_N)/S_p(V_0)]
      >= (3-5p/2) sum_(n<N) log lambda_n
           -p sum_(n<N) ell_n +sum_(n<N) log(1-eps_n).   (2.6)

This is a distortion/viscous-defect alternative, not an input-summable cost.

### 2.1 One sufficient bound for the defect, not an assumed diffusion sign

Suppose theta<=Theta, integral ||grad W||infinity<=L1,
integral ||W||infinity<=D, and for a real m with mp>3,

    sup_(tau,y) (1+|y|)^m |Delta Omega(tau,y)|<=B_m.

The material propagator in (2.1) has norm at most exp(L1); displacement is
at most D. Consequently, with volume measured in the original label y,

    ||E||_Lp^p <= [mu Theta exp(L1) B_m(1+D)^m]^p
                       8pi/[(mp-1)(mp-2)(mp-3)].        (2.7)

The displayed constant is the exact integral of (1+|y|)^(-mp) in R3.
An initial lower bound for I_p(V) then makes eps=O(mu^p). Weighted tube
bounds in this sufficient test are NOT proved from arbitrary initial data.
The next theorem avoids assuming them or smallness of E in Lp altogether.

## 3. Finite-block exclusion without a viscous Lp-defect assumption

Fix s>=6, 1<lambda0<=Lambda<infinity, g0>1, Theta>0, and M,L,B>0. Let K be
a COMPACT subset of real solenoidal L2(R3), consisting of states satisfying

    ||Q_1 V||2=1,    ||V||Hs<=M,    I_p(V)<=B.            (3.1)

Choose one 0<p<=1 for which

    r=lambda0^(3-5p/2) exp(-p L)>1.                      (3.2)

This is possible for any finite L if uniform I_p localization is available
at sufficiently small p. Equivalently p<3 log(lambda0)/[(5/2)log(lambda0)+L].
Condition (3.1) at this p is essential, not a consequence of H^s compactness.

A length-N admissible block consists of V_0,...,V_N in K, positive mu_n,
and their COMPLETE NS intervals W_n of durations 0<theta_n<=Theta, such that
(1.3) holds at each step,

    lambda_n in [lambda0,Lambda],    g_n>=g0,
    mu_(n+1)=mu_n/g_n,
    sup_(n,tau<=theta_n) ||W_n(tau)||Hs<=M,
    log sup_y ||D Phi_(n,theta_n)(y)^(-1)||op <=L.        (3.3)

The last assumption may be replaced by the stronger integral bound
integral_0^theta_n ||grad W_n||infinity<=L. No uniform rapid decay during the
intervals and no estimate of eps_n is required.

Let Momega>0 be a common upper bound for ||curl V||infinity on the H^s ball
in (3.1), for example its Sobolev embedding constant times M, and set

    b=(4/9) Momega^(p-2) M^(-p)>0.                     (3.4)

**Theorem 2 (Euler full-state block).** Every length-N version of (3.1)--(3.3)
with mu=0 obeys

    b r^N <= S_p(V_N) <= B.                             (3.5)

Indeed ||Q_1 V||2=1, solenoidality and the support lower bound 2/3 give
||curl V||2^2>=4/9. Since |curl V|^2<=Momega^(2-p)|curl V|^p, (3.4) is a lower
bound for S_p(V). Its upper bound is B because ||V||2>=1. Equation (2.5)
with E=0 and (3.2) then proves (3.5). Euler energy is exactly conserved; the
weaker energy inequality already used in (2.5) suffices.

**Theorem 3 (original-NS finite-block exclusion).** Choose ANY integer N>=1
with b r^N>B. There exists mu_*>0, depending only on K and the displayed
class constants, such that NO admissible length-N positive-viscosity block
has mu_0<mu_*.

Consequently no one original fixed-positive-nu NS solution has an infinite
sequence of these full-state returns with the same K and class constants.
No fixed point, finite period, fixed geometry, fixed scale ratio, fixed phase,
fixed polarization, small exterior, or Type I bound is assumed.

### Proof of Theorem 3: derive and retain the entire Euler boundary block

Suppose length-N blocks with mu_0^(j)->0 exist. Take subsequences of their
finitely many states using compactness of K in GLOBAL L2, and of their theta,
lambda and O parameters. All states converge in L2, uniformly bounded in H^s.
Interpolation gives convergence in H^(s-epsilon) for every epsilon>0. Their
limits remain in K. In particular their full annular norm is one and their
I_p bound is preserved (also directly by Fatou for the curls). Small-power
tail mass need not converge; only this upper bound is used. The velocity
converges globally in Sobolev and critical norms, so a nonperturbative critical
exterior is not projected away or lost in a merely local limit.

The gain parameters are bounded without a carrier approximation. From (2.4),
energy, ||V_(n+1)||2>=1 and lambda<=Lambda,

    g_n^2 <= lambda_n ||V_n||2^2 <= Lambda M^2.          (3.6)

Take further subsequences so every g_n converges in [g0,sqrt(Lambda)M].
Every mu_n tends to zero because mu_n<=mu_0 g0^(-n).

Here is a global, nonformal inviscid passage through the possibly variable
intervals. Write X_j(r)=W_n^(j)(theta_n^(j) r) for 0<=r<=1. Then

    partial_r X_j=-alpha_j P[(X_j.grad)X_j]+beta_j Delta X_j,
    alpha_j=theta_n^(j), beta_j=theta_n^(j)mu_n^(j)>=0.

For z=X_j-X_k, the transport by X_j cancels in the L2 pairing. Use

    P[(X_j.grad)X_j-(X_k.grad)X_k]
                       =P[(X_j.grad)z+(z.grad)X_k].

Keeping beta_j Delta z dissipative, the remaining parameter differences
are bounded using the UNIFORM H^s bound. One obtains

    d_r ||z||2 <= C_(M,Theta) ||z||2
                  +C_M (|alpha_j-alpha_k|+|beta_j-beta_k|). (3.7)

The inequality at zero norm follows by regularization. Thus X_j is Cauchy
in C([0,1];L2), not just locally in space. Interpolation gives convergence
in C([0,1];H^(s-epsilon)). The limit X obeys

    partial_r X=-theta_* P[(X.grad)X],                    (3.8)

with initial state V_n^*, and is a smooth enough finite-energy Euler flow.
If theta_*=0 it is simply constant. No Euler lifespan was presumed: (3.7),
the common H^s bound and the limit equation construct the entire finite
interval. The products and canonical Riesz pressures converge globally in
sufficient Sobolev spaces. Full-state energy is retained in the strong L2
limit; no unrecorded energy or pressure-bearing exterior is removed.

Translations cannot diverge. Indeed the endpoints w_j=X_j(1) are precompact
in L2 by (3.7). The states V_(n+1)^(j) are also precompact in L2, have norm
at least one, and (3.6) bounds all scale and gain factors above and below.
Choose a fixed ball carrying, uniformly, a positive amount of their L2 mass.
By (1.3) this mass is carried by a fixed-radius ball about c_n^(j) in w_j,
with uniformly positive size. If |c_n^(j)|->infinity this contradicts uniform
L2 tightness of the convergent w_j. Hence a subsequence of c_n^(j) converges.
Rotations, bounded dilations and translations act continuously on L2, so
(1.3) passes to the limit as an EXACT full-state Euler return.

Finally (3.7) and interpolation give uniform C^1 convergence in space and
time after the interval reparameterization. The uniform H^s bound gives a
uniform C^2 bound. The integral equations for the flows and their Jacobians
then imply uniform convergence of D Phi and its inverse on R3. The endpoint
compression bound ell<=L passes to the limit. Thus all N limiting Euler
returns obey Theorem 2. This contradicts b r^N>B, proving Theorem 3. QED.

For a fixed physical nu, repeated g>=g0 makes mu_n=nu/a_n->0; any sufficiently
late length-N block would contradict the theorem. The clock bounds allow
physical intervals on the requested nonlinear scale. The proof imposes only
their upper normalized duration, so also covers a specified positive lower
clock bound. The threshold mu_* is a compactness existence constant, not a
computed or interval-certified numerical threshold.

### 3.1 Precise exterior escape alternative

Under the compact-L2 and uniform smooth-tube/compression assumptions, an
infinite high-amplitude return orbit must have

    sup_n integral |curl V_n|^p = infinity               (3.9)

for EVERY p satisfying (3.2); an eventual bound would let Theorem 3 apply to
late blocks. With uniformly bounded curl, every fixed ball contributes at
most its volume times Momega^p. Thus (3.9) occurs outside every fixed ball,
not by unbounded core vorticity inside that ball.

Otherwise the orbit must lose full-state L2 compactness, bounded scale ratios,
or normalized smooth-tube/compression bounds. This is not the earlier narrow
Fourier-packet theorem: no angle, carrier count, planarity or cone is imposed.
But the small-power exterior mass is NOT necessarily nonperturbative in a
critical velocity norm, as the following sharp obstruction shows.

## 4. Critical-invisible exterior: a sharp limit of this mechanism

**Theorem 4.** For every 0<p<6/5 there are real solenoidal compactly supported
smooth normalized states V_R with ||Q_1 V_R||2=1, converging to a nonzero
normalized f in every H^s and in every finite L^{3,q}, but

    integral |curl V_R|^p -> infinity.

Choose nonzero real solenoidal f,h in C_c^infinity(R3), normalize f by
||Q_1 f||2=1, and put, for 0<beta<3/p-5/2,

    h_R(x)=R^(-3/2-beta) h((x-R^2 e1)/R),
    c_R=||Q_1(f+h_R)||2,       V_R=(f+h_R)/c_R.          (4.1)

Such f,h are curls of nonzero compact smooth vector potentials. For large R
their supports are disjoint. Exact change of variables gives

    ||partial^alpha h_R||2=R^(-beta-|alpha|)||partial^alpha h||2,
    ||h_R||_(3,q)=R^(-beta-1/2)||h||_(3,q),
    integral |curl h_R|^p=R^(3-(5/2+beta)p) I_p(h).       (4.2)

Thus c_R->1, V_R->f in all the claimed velocity topologies, while disjoint
vorticity supports make the small-power integral diverge. All inputs are
Schwartz. This is a static obstruction, not an actual recurrent NS orbit.

In particular no upper bound for I_p follows merely from bounded energy,
critical Lorentz norm, or even simultaneous bounds in every H^s. No critical
lower cost follows from each unit increase of small-power vorticity mass.
This rules out promoting (3.9) alone to a Lorentz-blowup detector or an
input-summable RF-q expenditure. It does NOT disprove a dynamical estimate
which uses additional exact information about the actual regenerated state.

The homogeneity obstruction is visible in (2.5) itself: under critical NS
scaling v_lambda(x)=lambda v(lambda x),

    S_p(v_lambda)=lambda^((5/2)p-3) S_p(v).

The critical choice p=6/5 erases the favorable geometric factor, while the
compression factor need not improve. S_p is deliberately a localization
functional used for a negative construction theorem, NOT a new critical
functional satisfying the positive-lane admission test.

## 5. What the theorem does and does not remove

The excluded class comprises high-amplitude full-state return blocks in a
fixed L2-compact class with a sufficiently small-p vorticity bound and uniform
smooth normalized intervals satisfying (3.2). Arbitrary nonperiodic carrier
geometry, correlated phase/polarization and inherited exterior are permitted
inside that class. This kills, in particular, uniformly smooth uniformly
rapidly vorticity-localized compact trapping classes in the high-amplitude
regime. It does not exclude compactness solely in a velocity/critical topology:
Theorem 4 shows exactly why that distinction is substantive.

Alive: noncompact exterior-bearing returns; small-power-tail-accreting returns;
large normalized internal distortion or derivative growth; unbounded scale
jumps; finite-amplitude or finite numbers of turns; and a critical dynamical
cost not inferred from small-power tail mass. No general two-turnover
obstruction, robust regenerative two-cell, shadowing theorem or blowup-event
extraction has been established. The map in Section 1 has no proved recurrent
set; Theorem 3 excludes only the stated high-amplitude class.

The exact Tao-breaking identity is the material vorticity equation behind
(2.1), for the SAME transported velocity and its curl, plus the positive
Laplacian defect. A generic assigned energy-cancelling cascade has an additional
curl forcing in (2.1), not just mu Delta Omega. The published averaged operator
[T] cannot obey this original material identity for every real solenoidal
Schwartz input: otherwise the difference between its quadratic source and
the original Leray source would be curl-free, divergence-free and L2, hence
zero by Fourier transformation. But the inspected packet test gives

    <N(psi_(1,n)),psi_(2,n)>=0,
    <C_Tao(psi_(1,n),psi_(1,n)),psi_(2,n)>
                         =epsilon*(1+epsilon0)^(5n/2)!=0.

Thus an additional material curl forcing is necessary for that operator.
This is a discriminator on the exact proof identity, not merely on a lane
name. Energy cancellation alone would not prove our theorem.
This discriminator still does not furnish the missing critical estimate.

ONE remaining dominant nut: prove an actual full-state regenerative return
statement allowing the noncompact or tail-accreting exterior that cannot be
uniformly localized away. Either construct a concentrating scale-repeating
orbit with full NS shadowing, or charge its REQUIRED critical regeneration
(not the critical-invisible mass in Theorem 4) to an input-summable budget,
with blowup-event extraction and the complete continuation consumer in Section 0.

## 6. Source inspection, reproducibility and audit boundary

[CT] D. Chae and T.-P. Tsai, *On discretely self-similar solutions of the
Euler equations*, arXiv:1304.7414v1, Section 2, Theorem 2.1 and its full proof,
https://arxiv.org/html/1304.7414v1 . Inspected directly on 2026-09-08. It treats
time-periodic Euler similarity profiles with bounded first derivatives,
spatial decay, and vorticity in every sufficiently small positive L^q. The
small-q volume-versus-stretching mechanism is prior art. Our proofs above
are self-contained; no periodicity theorem is substituted for the finite-
block passage (3.7), and no publication priority is claimed for its ingredients.

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier-Stokes equation*, arXiv:1402.0290v3, Introduction and definition of the
averaged operator, https://arxiv.org/html/1402.0290v3 . Inspected directly;
assigned rotations/dilations/multipliers preserve energy cancellation, not
the asserted original material transport law. The concrete pump mismatch is
also checked by the repository's inspected Tao packet audit and checker.

The input source-cycle and newborn-efficiency proof and both exact checkers
were read. The rational source checker passes 12,351 assertions over 384 geometries,
not the historical report's 12,357. At the frozen input, the
symbolic checker CRASHES on tuple subtraction in eq(a,b,label), rather than
completing its previously reported run. Comparing tuple components repairs
that execution defect; the current script then reports 10 checks, not 11.
This repair does not strengthen its finite-jet claims into a turnover theorem.
The discovery_regeneration_turnovers.py file mentioned in the input evidence
is absent from that remote source tree; no execution of it is claimed here.

The new checker passes 116 assertions covering finite symbolic differential
identities, return scaling, the material variation-of-constants cancellation, the volume integral,
small-power algebra and the satellite scaling. It does NOT certify compactness,
PDE existence, the global inviscid passage, independent review or NS regularity.
These analytic obligations are supplied by the author proof above and remain
subject to independent mathematical audit. No independent worker was available.
