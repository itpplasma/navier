# Closed feedback: finite causal radius despite real dissipative regularity

Date: 2026-09-07. Frozen input: `49b67060edbda947f76cd1da290678096a415827`.
Workflow: `krystophny/prompts/skills/math-frontier/SKILL.md`, blob
`d32e4a8dcb1e5f06c3fc9b44620f6f4c8d0d562e`.
Status: author derivation; independent mathematical audit pending.
Outcome: architecture-level falsification in a specified Galerkin class.
NS-R3 is NOT PROVED. No strict singularity reduction or novelty claim.

## 0. Frontier packet and why this test is load-bearing

TERMINAL CLAIM: original unforced whole-space NS, every solenoidal Schwartz
initial velocity and every fixed positive viscosity, globally smooth velocity
and pressure with the initial kinetic-energy upper bound.

ESTABLISHED: the canonical local/energy/continuation suffix; the refinement
contract RF-SUM; a factorial causal remainder in a one-way shear/passive NS
sector; a bounded moving-metric repair of a one-way linearized strain sector.
Neither previous sector contains a closed nonlinear transfer cycle.

FIRST GAP: whether the causal all-amplitude estimate survives genuine closed
feedback. The tested stronger premise is a single homogeneous Volterra/tree
expansion about zero converging absolutely for every input amplitude. A
factorial coefficient bound with fixed geometric constants would imply it.

FALSIFIER: an invariant sector of the actual spherical Fourier--Galerkin
NS equation whose real dynamics are globally energy-bounded but whose
homogeneous amplitude series has finite radius. Complexification is used
only to analyze that series, never to claim physical NS blow-up.

CHECK: compute the FULL projected vector field, including all produced modes;
prove the amplitude obstruction at positive viscosity without a fitted pole;
then test restart and propagator repairs instead of retiring causal reduction.

The proof below falsifies the single-center analytic premise. It does not
falsify real-data RF-SUM, a summation procedure not requiring this convergent
series, causal memory in general, adaptive reconstruction, kinetic theory,
FEEC, or general geometric reduction. Those remain separate obligations.

## 1. A closed-feedback invariant sector of a full spherical Galerkin system

Work on the fixed torus (R/2pi Z)^3 with normalized volume measure. Let P_N
be orthogonal Fourier projection to wavevectors |k|<=N and let P be the Leray
projection. The equation is

    u_t + P_N P[(u.grad)u] = nu Delta u,   P_N u=u, div u=0.   (1.1)

It has the full ordinary quadratic convolution followed by projection, not
pseudospectral aliasing. All wavevectors in the ball are retained by P_N;
we do not manually delete inconvenient retained modes.

Fix an integer K>=1 and

    sqrt(5)K <= N < sqrt(8)K.                                (1.2)

For real a,b,c set

    psi = a cos(K x1)+b cos(2K x2)+c sin(K x1)sin(2K x2),
    u = (partial_2 psi,-partial_1 psi,0).                    (1.3)

The fields have zero mean, are solenoidal, and are independent of x3. Put
zeta=-Delta psi. The curl of (1.1) is

    zeta_t + P_N(u.grad zeta) = nu Delta zeta.                (1.4)

Curl is injective on the zero-mean solenoidal fields in this two-dimensional
sector and commutes with P_N. Thus (1.4) is equivalent to (1.1) there; no
pressure choice is used to suppress an interaction.

Write X=K x1 and Y=2K x2. Direct expansion gives the ENTIRE nonlinear scalar
flux, before projection:

    u.grad zeta = K^4[
        -6ab sin X sin Y
        +4ac cos Y -4ac cos(2X)cos Y
        -bc cos X +bc cos X cos(2Y)].                       (1.5)

The first, second and fourth displayed terms have wavevector lengths
sqrt(5)K, 2K, K. The other two have lengths sqrt(8)K and sqrt(17)K and are
strictly outside (1.2). There are no other modes. Consequently the sector
(1.3) is invariant under the FULL projection (1.1), and its exact ODE is

    a_t = -nu K^2 a + K^2 bc,
    b_t = -4nu K^2 b - K^2 ac,
    c_t = -5nu K^2 c + (6/5)K^2 ab.                         (1.6)

In particular every component feeds the other two. This is not the passive
sector of the previous proof. It is also not an exact continuum invariant
ansatz: the two explicitly discarded modes in (1.5) are generally nonzero.
The obstruction applies to an all-cutoff Galerkin assertion, which includes
(1.2); no continuum singularity is inferred from it.

Use dimensionless time s=nu K^2 t and variables

    x=sqrt(6/5) a/nu,   y=sqrt(6/5) b/nu,   z=c/nu.

Equation (1.6) becomes

    x'=-x+yz,   y'=-4y-xz,   z'=-5z+xy.                     (1.7)

All statements about this ODE are therefore uniform in K and in cutoffs
satisfying (1.2), after this EXACT viscous normalization. They do not concern
arbitrarily larger N: further modes enter at sqrt(8)K. The characteristic
velocity is of size nu K times the dimensionless amplitudes, not a fixed
velocity while K tends to infinity.

Three-mode barotropic reductions and their geometric structure are established
prior art; see the source ledger. The formulas and projection range above
are derived explicitly and do not depend on borrowing a historical model.

## 2. Real solutions are globally dissipative

For real (x,y,z), define

    E=x^2+4y^2+3z^2.

Equation (1.7) gives exactly

    E'=-2(x^2+16y^2+15z^2) <= -2E.                          (2.1)

The cubic coefficients cancel: 2-8+6=0. The physical squared velocity norm
is (5nu^2 K^2/12)E. Similarly the inviscid quadratic invariant corresponding
to enstrophy is x^2+16y^2+15z^2 (its cubic cancellation is 2-32+30=0).
Writing J=x^2+16y^2+15z^2, its inviscid vector field also has the exact
geometric representation B(u,u)=(1/48) grad E cross grad J. Thus both
quadratic invariants and this Nambu representation are preserved before
adding the diagonal viscous dissipation. The failure below is not caused
by discarding these structural identities.

The real ODE has a polynomial, locally Lipschitz vector field; (2.1) bounds
all coordinates on every interval, so the elementary ODE extension argument
gives a unique global real solution. More precisely

    ||(x,y,z)(s)||_infinity <= sqrt(E(0)) exp(-s).            (2.2)

For the one-parameter REAL input (x,y,z)(0)=q(1,0,1), every real q therefore
has a global decaying solution. This fact is fully consistent with the
complex-amplitude obstruction in the next section.

## 3. The single homogeneous causal expansion has a finite radius

Let D=diag(1,4,5) and

    B(v,w)=((v2 w3+v3 w2)/2,
            -(v1 w3+v3 w1)/2,
             (v1 w2+v2 w1)/2).

Then (1.7) is u'=-Du+B(u,u), and ||B(v,w)||_infinity <=
||v||_infinity ||w||_infinity over both R and C. Its homogeneous expansion
for u(0)=q u_*, u_*=(1,0,1), is defined recursively by

    U_1(s)=exp(-Ds)u_*,
    U_n(s)=sum_(j=1)^(n-1) integral_0^s exp[-D(s-r)]
                                      B(U_j(r),U_(n-j)(r)) dr. (3.1)

These coefficients collect ALL binary interaction trees of a given degree.
There is no selection of a favorable ordering or dropped feedback branch.

### 3.1 There is a genuine local analytic solution, not only a formal series

An induction in (3.1) proves

    ||U_n(s)||_infinity <= exp(-s)(1-exp(-s))^(n-1).          (3.2)

For the induction step, the sum has n-1 terms. After multiplying the heat
factor, its integral is

    exp(-s)(n-1) integral_0^s exp(-r)(1-exp(-r))^(n-2) dr
      = exp(-s)(1-exp(-s))^(n-1).

Thus sum q^n U_n converges uniformly on [0,S] for
|q|(1-exp(-S))<1. Absolute convergence permits substitution in the Volterra
equation, and elementary uniqueness identifies it with the actual solution.
The series is the amplitude Taylor series, not an unrelated representation.

### 3.2 Positive comparison on an invariant real slice of the complexification

Set q=iA, A>=0, and write x=iX, y=Y, z=iZ. The complexified equations become

    X'=-X+YZ,   Y'=-4Y+XZ,   Z'=-5Z+XY,
    (X,Y,Z)(0)=(A,0,A).                                    (3.3)

The nonnegative octant is invariant until a possible blow-up. Define

    (Xhat,Yhat,Zhat)=exp(5s)(X,Y,Z),
    theta=(1-exp(-5s))/5.

The equations in theta are

    dXhat/dtheta = 4 Xhat/(1-5theta) + Yhat Zhat,
    dYhat/dtheta =   Yhat/(1-5theta) + Xhat Zhat,
    dZhat/dtheta = Xhat Yhat.                               (3.4)

All coefficients and quadratic couplings are nonnegative for 0<=theta<1/5.
Deleting the two nonnegative linear terms gives the comparison system

    p'=rq,   r'=pq,   q'=pr,   (p,r,q)(0)=(A,0,A),

whose explicit solution is

    p=q=A sec(A theta),   r=A tan(A theta)                  (3.5)

before theta=pi/(2A). Ordinary comparison, or monotone Picard iteration,
gives (Xhat,Yhat,Zhat)>=(p,r,q) componentwise while both exist.

There is also a COEFFICIENTWISE version, which avoids any assumption about
continuation of a complex solution through a pole. Expand (3.4) in A.
At degree one, the integrating factors of its diagonal linear terms are
at least one. At degree n>=2, the source is a sum of products of earlier
nonnegative coefficients. Induction and the positive integrating factors
show that each coefficient is at least the coefficient of (3.5), at each
fixed theta. All of these expansions are legitimate near A=0 by (3.2).

The Taylor coefficients of sec and tan at zero are nonnegative in their
nonzero parities: this follows from their differential equations
(sec)'=sec*tan and (tan)'=sec^2 with initial values 1 and 0. Their series
have radius pi/2, since cos has its first zeros at +/-pi/2 and the numerator
of sec does not vanish there. These facts can also be used directly in the
positive coefficient comparison.

For a fixed S>0, the amplitude series of (3.3) consequently diverges at
A>=pi/[2theta(S)], in at least one component. Since the diagonal substitution
(x,y,z)=(iX,Y,iZ) preserves the absolute values of coefficient vectors and
q=iA only changes scalar coefficient phases, the radius r(S) of (3.1) obeys

    1/(1-exp(-S)) <= r(S)
      <= 5pi/[2(1-exp(-5S))] < infinity.                   (3.6)

The lower bound refers to uniform convergence on [0,S]; the upper bound
already holds when observing at s=S. No sharpness of either bound is claimed.

### 3.3 Exact branch exclusion

**Theorem 1.** In the actual spherical Galerkin systems (1.1)--(1.2), the
homogeneous zero-centered causal series cannot converge absolutely at every
real input amplitude on any fixed positive normalized horizon. In particular
there do not exist finite constants C_S,L_S, independent of degree n, with

    ||U_n||_(C([0,S];l-infinity)) <= C_S L_S^n/n!

(or any coefficient majorant having infinite amplitude radius).

Proof: any such majorant would make (3.1) an entire function of complex q,
contradicting (3.6). Absolute convergence at every real amplitude likewise
forces infinite complex radius for a power series, giving the same contradiction.
All real solutions nevertheless exist globally by (2.1). QED.

This does not say no globally valid expansion or resummation can exist.
It excludes this single-center homogeneous power series and its purported
all-amplitude factorial bound. The earlier passive-sector series is unaffected:
its linear dependence on the advected field prevents the closed binary tree
feedback that appears in (3.1).

For completeness, (3.5) also proves actual finite-time growth to infinity
of the complexified ODE when A>5pi/2, no later than

    S_A=-(1/5) log(1-5pi/(2A)).                              (3.7)

This is only a secondary analytic check. It is NOT real Navier--Stokes blow-up,
NOT a finite-energy R3 solution, and NOT a counterexample to NS-R3.

## 4. Exact scope and the required repair

The decisive negative conclusion is limited to a universal analytic
implementation that would have to cover every faithful cutoff, hence (1.2).
It is not necessary that this finite sector be invariant at all larger cutoffs
for it to disprove that implementation. Conversely, no inference concerning
a limiting continuum singularity follows from the finite sector.

The upper radius bound does not depend on a small numerical error, unknown
future strain, or a formal infinite series assumed convergent. It follows
from the exact Galerkin projection, a positive comparison, and elementary
analytic majorants. The fixed horizon S corresponds to physical time
S/(nu K^2), with nu fixed. The datum amplitude in (1.3) changes with q;
this is a universal-amplitude test, not a sequence from one fixed R3 datum.

The surviving repair is causal restart or another controlled nonperturbative
summation: use local series where their remainder is valid and explicitly
account for propagation and reconstruction between intervals. This requires
real bounds, not analyticity for all complex amplitudes. The following
research wave must establish those costs and their interlevel behavior.

## 5. Sources and review boundary

[P1] Edward N. Lorenz, Maximum Simplification of the Dynamic Equations,
Tellus 12 (1960), 243--254, DOI 10.1111/j.2153-3490.1960.tb01307.x.
https://onlinelibrary.wiley.com/doi/abs/10.1111/j.2153-3490.1960.tb01307.x
Publisher abstract/metadata inspected. It describes a three-component
barotropic Fourier model and elliptic-function solutions. This note does
not claim novelty of a three-mode reduction and imports no uninspected
coefficient or positive-viscosity theorem from that paper.

[P2] A. Bihlo, R. O. Popovych, Symmetry justification of Lorenz' maximum
simplification, arXiv:0805.4061. https://arxiv.org/abs/0805.4061
Abstract inspected; provenance for symmetry-based finite-mode selection.
No source statement from it is required for the explicit calculation above.

[P3] C. Foias, L. Hoang, J.-C. Saut, Navier and Stokes meet Poincare and Dulac,
arXiv:1711.07184. https://arxiv.org/html/1711.07184
Sections 1.2--1.4 and the normal-form scope inspected. Its regular-solution
long-time normal forms are not an all-amplitude zero-centered theorem of
the sort excluded here. No regularity conclusion is imported from them.

[R1] The repository's resonant-slaving/causal-refinement note and normal-
transient/metric-repair note at the frozen input; their exact scopes remain
unchanged. The present feedback test concerns a different, closed system.

The exact finite Fourier and rational coefficient checks accompanying the
integration are regression oracles, not universal proof or independent review.
Audit especially cutoff faithfulness, the streamfunction/velocity convention,
the coefficientwise complex comparison, and the distinction between a real
flow and an amplitude power series. NS-R3 and RF3/RF4 remain unproved.
