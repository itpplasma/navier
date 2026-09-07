# Terminal tests: vorticity-entropy rigidity and generated covariance

Date: 2026-09-07.
Frozen research input: `07d5e483d403d268d3735bcf4eb30cb18685902f`.
Status: complete author derivations; independent mathematical audit pending.
No novelty or priority claim, canonical graph promotion, or formal proof.
NS-R3: NOT PROVED. Terminal obstruction: UNCHANGED.

The first result concerns spatially INTEGRATED nonlinear vorticity densities
on actual local whole-space NS solutions. It is not the previous classification
of velocity densities or the pointwise maximum-vorticity obstruction. The
second realizes a negative spatially INTEGRATED strain/covariance contraction
on an actual compact-data NS branch, with the covariance generated from zero
by its own stochastic inverse flow. It is not an arbitrary-matrix example.
Neither result is a singular solution or a positive regularity mechanism.

## 1. Terminal gate and distinct mechanisms tested

The inputs remain every solenoidal Schwartz u0 on R3 and every fixed nu>0,
with the original unforced equation. LOCAL, ENERGY and CONTINUATION close
NS-R3 once the classical branch has, for every finite H,

    sup_{0 <= t < min(H,Tstar)} ||u(t)||_3 <= C(u0,nu,H) < infinity.  (1)

Only the approach to a hypothetical finite Tstar needs a new bound: LOCAL
already handles the initial interval. This is the existing sufficient edge,
not a newly weaker criterion or a claim of a least criterion among all routes.
All constants may depend on the full prescribed datum, not a future solution
norm. A direct contradiction to finite Tstar is also admissible.

**Integrated vorticity entropy.** Try to find a fixed normalized C2 density
eta for which F_eta(u)=integral eta(curl u) is nonincreasing on every branch
and, together with energy, controls L3. This tests spatial cancellation of
stretching rather than a pointwise stretching estimate. A concrete smooth
critical-growth candidate and its entire consumer are in Section 2. The
hard step is universal monotonicity, not that consumer. Sections 3--7 prove
that the ONLY such normalized C2 monotone density is zero, without assuming
convexity, isotropy, evenness, or homogeneity. Thus replacing enstrophy by
another fixed vorticity-local density cannot supply this producer.

**Signed stochastic output.** The Constantin--Iyer representation [S1]
suggests bounding the signed mean Weber field itself:

    sup_{t < min(H,Tstar)} ||E[J(t)^T (u0 o A(t))]||_3
        <= C(u0,nu,H),                                      (2)

where A is the common-noise inverse flow and J=grad A. Leray boundedness on
L3 turns (2) directly into (1); LOCAL, CONTINUATION and ENERGY then finish.
This is only a target, not a proved or weaker terminal reduction. The
mean/covariance route [S2] retains strain in its exact equations. A proposed
repair was favorable strain contraction for the covariance actually generated
from zero. Section 8 falsifies that repair even after spatial integration.
No absolute-deformation estimate or mean/covariance infrastructure is promoted.
The signed output (2) itself is NOT disproved by this counterexample.

**Kinetic signed stress transfer.** The actual KPC remainder retains the
macroscopic convective flux. Taking absolute values again encounters the
same endpoint obstruction recorded in the preceding evidence: an L-infinity
L3 input leads to a near-time kernel (t-s)^(-1), while the energy consequence
u tensor u in L1_t L3_x cannot bound its supremum after convolution with
(t-s)^(-1/2). This attempt was stopped, not developed into a new representation.
It is neither a new stress no-go nor a falsification of a signed estimate
restricted to actual nonlinear Boltzmann trajectories.

**Finite-segment cascade cost.** A nonsummable energy cost for every extracted
singular cascade would contradict ENERGY directly. But merely assigning a
positive cost to each critical bubble does not do this: a bubble of radius r,
amplitude nu/r and duration r^2/nu has energy and integrated viscous loss of
order nu^2 r, summable over dyadic radii. This is dimensional accounting, NOT
construction of an actual NS cascade. The missing dynamical multiplicity/cost
and extraction theorem was not assumed. Existing single-channel and viscous-
mixing falsifiers were retained; no further instantaneous branching lemma
was pursued and no whole dynamical cascade architecture is ruled out here.

## 2. A fully specified entropy consumer, not a new producer

Put eta_*(z)=(1+|z|^2)^(3/4)-1 and F=integral eta_*(omega), omega=curl u.
This is C-infinity, convex and normalized. It grows quadratically at zero
and like |z|^(3/2) at infinity. Thus it does not silently demand an enstrophy
bound at high vorticity. Work in fixed mathematical units for the threshold 1.
On a classical interval, F is finite since u is bounded in all Sobolev norms.

Split omega=g+h with g=omega 1_{|omega|<=1}. Elementary one-variable estimates
for eta_* imply

    ||g||_2^2 <= C F,       ||h||_(3/2)^(3/2) <= C F.

Let B=(-Delta)^(-1) curl, v=B g and z=B h, so u=v+z in distributions and
a.e. The identity follows from div u=0 and the Fourier multipliers; no
harmonic polynomial is permitted by the L2 velocity and the indicated
potential classes. The kernel of B is bounded by C|x|^(-2). The ordinary
whole-space fractional integration estimate [S3], with dimension 3 and
kernel exponent 2, gives

    ||v||_6 <= C F^(1/2),       ||z||_3 <= C F^(2/3).

The two exponent pairs are (p,q)=(2,6) and (3/2,3); both are strict, not
endpoint weak-type claims. On |u|<=1, the cubic integral is at most ||u||_2^2.
On |u|>1 and |z|>=|u|/2 it is at most 8||z||_3^3. On the remaining set,
|v|>|u|/2>1/2 and |u|^3<=8|v|^3<=64|v|^6. Consequently

    ||u||_3^3 <= ||u||_2^2 + C(F^2+F^3).                       (3)

If F(t)<=F(0) held on every branch, (3) and ENERGY would give (1) with
M^3=||u0||_2^2+C(F(0)^2+F(0)^3), with no further uncontrolled quantity.
CONTINUATION would exclude finite Tstar, and LOCAL/ENERGY would supply
smooth pressure, the initial trace and every other NS-R3 clause. More
general densities with a proved analogous coercivity have the same consumer.
Theorem V below falsifies the monotonicity of eta_* and every nonzero
normalized C2 candidate, not inequality (3) or a controlled nonmonotone bound.
The threshold splitting and (3) are included solely to state the closing
implication; they are not counted as terminal mathematical progress.

## 3. The vorticity-density classification theorem

**Theorem V.** Fix nu>0 and eta in C2(R3;R), with eta(0)=0 and D eta(0)=0.
Suppose that for every real compact smooth solenoidal datum w, the ACTUAL
local classical NS solution from w satisfies

    d/dt integral eta(curl u(t,x)) dx at t=0 <= 0.             (4)

Then eta is identically zero. Conversely zero satisfies (4). In particular,
nonincrease on even a datum-dependent right-neighborhood of zero implies
the same conclusion. No common lifespan, convexity, isotropy, evenness,
homogeneity, or growth condition at infinity is assumed.

The normalization removes affine terms; those are not claimed to be
excluded. The density is the SAME for every datum and is independent of
position and time. This theorem does not classify nonsmooth densities or
functionals involving u, the full strain, other derivatives, or nonlocal terms.

### 3.1 Legitimate initial differentiation

Write omega=curl w and G_ij=partial_j w_i. LOCAL gives L2 differentiability
of curl u at zero and a uniform vorticity bound on a short classical interval.
On bounded sets, normalization and C2 regularity give |eta(z)|<=C|z|^2 and
|D eta(z)|<=C|z|. Taylor's integrated remainder is at most
C||curl u(t)-omega||_2^2=O(t^2), so differentiation under the integral is valid.

The vorticity equation and compact support at time zero give exactly

    d/dt F_eta(u(t)) at zero = S_eta(w)-nu D_eta(w),           (5)
    S_eta(w)=integral D eta(omega) dot G omega,
    D_eta(w)=sum_j integral D2 eta(omega)[partial_j omega,partial_j omega].

The transport contribution is integral w dot grad eta(omega)=0. There is
no pressure term. Neither sign in (5) is assumed.

### 3.2 Two dilations force dissipation positivity and stretching sign

Use the different admissible initial data w_kappa(x)=kappa^(-1)w(kappa x).
Their vorticities are omega(kappa x), their velocity gradients are G(kappa x),
and direct changes of variables give

    S_eta(w_kappa)=kappa^(-3)S_eta(w),
    D_eta(w_kappa)=kappa^(-1)D_eta(w).

Thus (4) implies, for EVERY kappa>0,

    S_eta(w)-nu kappa^2 D_eta(w) <= 0.                        (6)

Letting kappa go to zero and to infinity, respectively, proves

    S_eta(w)<=0,       D_eta(w)>=0                           (7)

for every compact smooth solenoidal w. These are dilations of initial data,
not an asserted NS symmetry, inviscid limit, or uniform-lifespan theorem.
The viscosity remains the prescribed fixed positive number.

## 4. Compact curl probes force convexity; it need not be assumed

Fix b,h in R3 with h nonzero, and choose a unit n perpendicular to h. Let
chi be a nonzero real compact smooth cutoff. Choose a compact solenoidal B
whose curl is identically b on a neighborhood of supp chi. Explicitly,

    A_b(x)=-|x|^2 b/4,    curl A_b=(b cross x)/2,
    B=curl(theta A_b),

where theta is compact smooth and equals one on that neighborhood. Then
curl B=b there. For fixed a>0 and k tending to infinity set

    w_(k,a)=B+curl[(a/k^2)chi(x)h cos(k n.x)].                 (8)

These are genuine compact solenoidal velocities. On the perturbation support,
using h dot n=0 and curl curl=grad div-Delta gives uniformly

    omega_(k,a)=b+a chi h cos(k n.x)+O(a/k),
    partial_j omega_(k,a)=-ak n_j chi h sin(k n.x)+O(a).       (9)

All omitted coefficients are bounded for fixed chi,b,h,a. Off this support,
the contribution to D_eta is that of the fixed B. Divide D_eta(w_(k,a))>=0
by a^2 k^2. Uniform continuity of D2 eta on the bounded vorticity range and
(9) remove the error terms. Periodic averaging as k tends to infinity gives

    0 <= integral chi(x)^2 (1/(2pi)) integral_0^(2pi)
          D2 eta(b+a chi(x)h cos q)[h,h] sin(q)^2 dq dx.       (10)

For clarity, this averaging needs no periodic NS solution: approximate the
continuous periodic integrand uniformly on its compact parameter set by
finite trigonometric sums and apply the Riemann--Lebesgue lemma to each
nonzero carrier in x. Finally let a decrease to zero in (10). It follows that

    0 <= (1/2)(integral chi^2) D2 eta(b)[h,h].                 (11)

The choices of b and h were arbitrary. Therefore eta is convex. With its
normalization, eta>=0 everywhere. This is also a direct falsifier for any
nonconvex eta: choose b,h with negative Hessian, then small fixed a, large
finite k, and finally large finite kappa in (6) to obtain a positive actual
initial entropy derivative at fixed nu.

## 5. Rotations and compact irrotational strain test the integrated stretching

Average over normalized Haar measure on SO(3):

    eta_bar(z)=integral_SO(3) eta(Rz) dR.

Rotations of compact solenoidal initial velocities are admissible; the
vorticity transforms as R omega for proper rotations. Hence eta_bar is C2,
convex, normalized, radial and nonnegative, and inherits (4) and (7). Averaging
initial derivatives avoids needing a common local interval for all rotations.
If eta is nonzero, nonnegativity and continuity show that eta_bar is nonzero.
Write eta_bar(z)=f(|z|). Then f'(r)>=0 for r>=0 and f'(0)=0.

Since eta_bar is even, changing w to -w reverses S_eta_bar: both G and omega
change sign, G omega does not, and D eta_bar changes sign. Combining this
with S_eta_bar<=0 from (7) gives

    S_eta_bar(w)=0 for EVERY compact smooth solenoidal w.     (12)

Fix one such w and any real symmetric trace-free matrix A. There is a compact
smooth solenoidal v that equals Ax on a neighborhood of supp w. One explicit
construction is

    v=curl[theta(x)(-x cross (Ax)/3)],                        (13)

with theta compact smooth and one on that neighborhood. Indeed, for a
homogeneous divergence-free polynomial B_m of degree m,

    curl[-x cross B_m/(m+2)]=B_m.

Symmetry of A gives curl v=0 on supp w, and grad v=A there. Off supp w,
w and its derivatives vanish. Thus subtracting the three exact stretching
integrals has NO annulus remainder:

    S_eta_bar(w+v)-S_eta_bar(w)-S_eta_bar(v)
        = integral D eta_bar(omega_w) dot A omega_w.          (14)

All three left terms vanish by (12). Put h(r)=f'(r)/r for r>0 and extend
continuously by h(0)=f''(0). Then

    integral h(|omega_w|) omega_w dot A omega_w=0             (15)

for every compact w and every symmetric trace-free A. Equation (15) says
that the weighted integrated vorticity second tensor must always be scalar.
It retains spatial cancellations; it is not a pointwise argument.

## 6. A compact three-dimensional test contradicts that tensor constraint

Let psi in C_c^infinity(R2) and chi in C_c^infinity(R) be real, with chi=1
on a nonempty interval. For every finite L>0 the field

    w_L(x,y,z)=(chi(z/L) partial_y psi,
               -chi(z/L) partial_x psi, 0)                  (16)

is compact, smooth and solenoidal on R3. Its vorticity is exactly

    omega_L=(L^(-1)chi'(z/L) partial_x psi,
             L^(-1)chi'(z/L) partial_y psi,
             -chi(z/L) Delta_xy psi).                       (17)

Apply (15) with A=diag(-1/2,-1/2,1), divide by L, and put s=z/L. The bounded
vorticity range and compact supports allow dominated convergence as L tends
to infinity, yielding

    0=integral_R2xR f'(|chi(s)Delta psi|)|chi(s)Delta psi| dx dy ds.  (18)

The integrand is nonnegative. If f is nonconstant, convexity and f(0)=0
supply r0>0 with f'(r0)>0. Choose psi compact smooth with Delta psi=r0 on
a small open disk (multiply a suitable quadratic by a cutoff equal to one
there). On that disk and the interval where chi=1 the integrand in (18) is
strictly positive. This is impossible. Hence f=0 and eta_bar=0.

Since eta>=0, a zero spherical average at every radius forces eta=0 pointwise.
This proves Theorem V. Every velocity used before each limiting argument is
compactly supported in all three dimensions. No infinite-energy planar flow
or affine velocity was inserted into the hypothesis.

## 7. Actual entropy-growth counterexamples and the precise retirement

The proof yields actual local NS violations for every excluded density.
The nonconvex case was described after (11). For convex nonzero eta, the
radial average is nonzero. Choose psi, chi and a sufficiently large FINITE L
so that the right side of (14) for w_L and A is nonzero. At least one of
w_L, v, w_L+v then has nonzero S_eta_bar. Reversing that whole datum when
necessary makes S_eta_bar positive. Choose a sufficiently small FINITE
kappa to make S_eta_bar-nu kappa^2 D_eta_bar positive. The average initial
derivative over rotated versions of this compact datum is positive, so at
least one rotation has positive initial derivative for the original eta.
LOCAL supplies its actual solution, and differentiability gives entropy
growth for sufficiently small positive time. All parameters are fixed before
LOCAL is applied; nu never varies.

Retire fixed normalized C2 vorticity-local INTEGRATED monotone entropies as
universal endpoint producers. Neither anisotropy nor permitting a nonconvex
density nor appealing to integrated stretching cancellation evades the theorem.
A kinetic claim that transfers precisely to such universal monotonicity with
matched initial data is likewise incompatible with the actual fluid examples.
This is stronger in premise class than the old pointwise-vorticity exclusion,
but it is not a strict reduction of the NS terminal problem.

Do not extend the exclusion to densities depending on both u and omega,
full strain or higher derivatives, nonlocal functionals, nonsmooth densities,
datum/time-dependent weights, delayed estimates, or controlled NONMONOTONE
production. Also, a separately dissipating combined energy/entropy functional
is not covered merely because its summands occur here. These require their
own endpoint mechanism and are not thereby established alternatives.

## 8. Actual generated covariance can have negative integrated strain work

**Theorem C.** For every fixed nu>0 there is a real compact smooth solenoidal
u0 such that, on its actual local unforced whole-space NS branch, the covariance
Q of the stochastic inverse-flow Jacobian has Q(0)=0, Q>=0, and

    integral_R3 tr(S(t,x)Q(t,x)) dx < 0                      (19)

for all sufficiently small positive t. Here S=sym grad u. In particular,
positivity of this actual generated covariance does not make the strain term
dissipative, even after spatial integration.

### 8.1 Exact equations and whole-space justification

On a compact classical interval use ONE common spatially constant Brownian
motion for all labels in

    dX(t,a)=u(t,X(t,a))dt+sqrt(2nu)dW_t,    X(0,a)=a,
    A(t)=X(t)^(-1),    J=grad A,    M=E J,
    Q=E[(J-M)^T(J-M)],    G=grad u,
    D_u=partial_t+u dot grad-nu Delta.

There is no stochastic force in the NS equation: this is an auxiliary
representation of the deterministic branch. Bounded smooth derivatives of
u on the chosen interval give a pathwise smooth flow: subtract sqrt(2nu)W_t
and solve the ordinary differential equation with the spatially translated
velocity. Its Jacobian and inverse satisfy finite local derivative bounds.
This justifies the differentiations and expectations below; it is not an
estimate uniform up to an unknown Tstar.

The inverse map obeys the stochastic transport equation in Ito form.
Differentiation gives

    dJ=(-u dot grad J+nu Delta J-JG)dt
                         -sqrt(2nu)sum_k partial_k J dW_k.

Therefore

    D_u M+MG=0,                           M(0)=I.            (20)

Apply Ito's product rule to J^T J. The quadratic variation
2nu sum_k (partial_k J)^T(partial_k J) combines with the two Laplacians
into nu Delta(J^T J). Thus C=E[J^T J] satisfies
D_u C+G^T C+CG=0. On the other hand, the ordinary product rule for D_u gives

    D_u(M^T M)+G^T M^T M+M^T MG
        =-2nu sum_k (partial_k M)^T(partial_k M).

Subtracting proves the exact covariance equation

    D_u Q+G^T Q+QG=2nu sum_k (partial_k M)^T(partial_k M),
    Q(0)=0.                                                   (21)

Its trace contains the term in question:

    D_u tr Q+2 tr(SQ)=2nu |grad M|^2.                         (22)

These identities agree with [S2, Sections 2--3], which is stated on T3.
The calculation above supplies the whole-space version on the LOCAL class;
no torus regularity conclusion is imported. Positive semidefiniteness is
also immediate from the actual covariance definition.

For the forthcoming integrated Taylor expansions there is no unverified
tail passage. Write V=M-I. Equation (20) is a linear parabolic equation for
V with zero initial value and source -G. On a compact classical interval,
u and all its spatial/time derivatives have the Sobolev bounds in LOCAL.
Differentiated energy estimates give V in every H^m. The source in (21)
then belongs to every H^m, and the same estimates give Q in every H^m.
Differentiating these equations in time, taking sufficiently many spatial
derivatives first, gives the Taylor expansions below in L2. Products with
S in L2 are consequently integrable, with controlled remainders. These
arguments are used only locally to certify the counterexample.

### 8.2 The actual small-time coefficient

From (20), M_t(0)=-G0. From (21), Q_t(0)=Q_tt(0)=0. Differentiating its
source twice at zero gives

    Q_ttt(0)=4nu C0,
    C0=sum_k (partial_k G0)^T(partial_k G0).

All terms involving Q or its first two time derivatives vanish there,
including transport and diffusion. Hence, in L2,

    Q(t)=(2nu/3)t^3 C0+O(t^4),    S(t)=S0+O(t),              (23)

and

    integral tr(S(t)Q(t))
       =(2nu/3)t^3 integral tr(S0 C0)+O(t^4).                (24)

It remains to construct compact solenoidal u0 with the last cubic integral
strictly negative. Choosing arbitrary independent S and Q would not suffice.

### 8.3 An explicit cubic coefficient and a compact localization

First use the bounded trigonometric calibration field, not as an admissible
whole-space datum,

    U(x,y,z)=(sin y,0,sin x+sin(x+y)),
    P(x,y,z)=(0,-cos x-cos(x+y),-cos y),    curl P=U.

Write G_U=grad U, S_U=sym G_U and C_U=sum_k (partial_k G_U)^T(partial_k G_U).
All derivatives in z vanish. Consequently C_U has zero third row/column,
and the only contributing entries of S_U are (S_U)_12=(cos y)/2 and its
transpose. Direct differentiation gives

    (C_U)_12=(sin x+2sin(x+y))sin(x+y),
    tr(S_U C_U)=cos y [sin x sin(x+y)+2sin^2(x+y)].            (25)

The mean over a 2pi-periodic cell is EXACTLY 1/4: the first term averages
to <sin^2 x><cos^2 y>=1/4 and the other terms average to zero.

Choose a nonnegative nonzero theta in C_c^infinity(R3) and set

    W_L=curl[theta(x/L)P(x)].                                (26)

This is compact and solenoidal. Boundedness of all derivatives of P gives,
uniformly on its support of volume O(L^3),

    grad W_L=theta(x/L)G_U+O(L^(-1)),
    partial_k grad W_L=theta(x/L)partial_k G_U+O(L^(-1)).

Thus the cubic integral differs from integral theta(x/L)^3 tr(S_U C_U)
by O(L^2). Finite trigonometric averaging in (25) proves

    L^(-3) integral tr(S_(W_L) C_(W_L))
         -> (1/4) integral theta^3 > 0.                     (27)

There is no nonlocal multiplier or omitted zero-frequency pressure term
in (27): its integrand is the displayed local polynomial in derivatives.
Choose one sufficiently large finite L and take u0=-W_L. Then S0 reverses
sign and C0 does not, so integral tr(S0 C0)<0. Apply LOCAL at the prescribed
fixed nu and use (24). This proves (19), with the covariance generated from
its required zero initial value by the same actual NS branch.

### 8.4 What this does and does not exclude

Retire any estimate that drops +2 integral tr(SQ) in (22) as a nonnegative
term merely because Q is positive semidefinite, starts at zero, and comes
from the actual inverse flow. The last two restrictions do NOT repair the
sign, as (19) proves. This is stronger than an indefinite-matrix warning.
[S2] itself already identifies an indefinite strain term; no favorable-sign
claim is attributed to that source. The refuted assertion was a candidate
repair tested here.

Theorem C does not exclude a quantitative signed strain bound, a different
covariance weighting, cancellations in the full mean Weber output (2), or
all stochastic regularity mechanisms. Mean/covariance representations and
local bounds alone still do not supply (2). The earlier absolute-deformation
failure is not counted a second time as a new no-go.

## 9. Adversarial checks and remaining obligations

Theorem V was tested against affine normalizations, nonconvex densities,
anisotropic convex densities, viscosity scaling, curl compatibility, the
annulus where a strain cutoff acquires vorticity, lack of periodic or affine
finite-energy data, and the order of the high-frequency/amplitude/elongation
limits. Convexity is derived using curl-compatible probes rather than assumed;
(14) subtracts the annulus contribution exactly; all violating data are compact
before LOCAL is used. No pressure-triad or isotropy hypothesis is hidden.

Theorem C was tested against the transpose convention G_ij=partial_j u_i,
the common-noise Ito correction, the requirement Q(0)=0, the actual-flow
rather than arbitrary-matrix premise, and passage to a global integral.
The expansion is in L2, the velocity sign reversal applies to initial data
rather than a claimed NS symmetry, and the periodic calibration is localized
before any actual NS solution is invoked. The trigonometric mean in (25)
and the curl in (26) were also checked symbolically; that computation is not
a replacement for the displayed proof or an independent review.

No positive producer in these attacks closes (1), so the terminal obstruction
is UNCHANGED. The direct route still needs an input-only critical bound near
a possible finite maximal time, or an equally explicit contradiction to such
a time. If the kinetic route is chosen, it needs its actual signed nonlinear
K_res producer plus the already-listed GSR preparation/moment/uniqueness
application audit. The stochastic route needs (2) or a genuinely weaker
specified sufficient signed output estimate, not just (20)--(22). A cascade
route needs actual extraction and nonsummable dynamical energy accounting.
These are alternatives, not cumulative new prerequisites for NS-R3.

The scoped new retirement is limited to Theorems V and C. Preserve the
canonical graph, all previous evidence, kinetic/microscopic contracts,
manuscripts and formalization. No claim of independent audit or new formal
coverage is made. Structural validation is separate from mathematical proof.

## 10. Source and inspection record

[S1] P. Constantin and G. Iyer, A stochastic Lagrangian representation of the
3-dimensional incompressible Navier--Stokes equations, arXiv:math/0511067.
Author-hosted text: https://www.math.cmu.edu/~gautam/research/papers/200511-detsns.pdf
Theorem 2.2, Remark 2.3 and Theorem 2.6 were inspected in text and rendered
pages 4--5. These give the representation and local framework, not a global
arbitrary-data estimate. The auxiliary flow uses common translational noise;
only smooth local branches are used in this note. The whole-space moment
calculation is supplied in Section 8, rather than inferred from periodicity.

[S2] T. Mahithitarmmatorn, Exact mean--covariance dynamics of the Weber field
in the stochastic Lagrangian representation of the 3D Navier--Stokes equations,
arXiv:2608.16915v1, https://arxiv.org/html/2608.16915v1 .
The primary HTML's Sections 2--3 and its limitation statements were inspected.
Its setting is smooth periodic NS on an existing time interval. The covariance
identity and indefinite strain term are prior structure, not new identities
claimed here. Theorem C's compact whole-space realized-sign counterexample
is separately derived. No global regularity claim is imported or attributed.

[S3] A. Kassymov, M. Ruzhansky and D. Suragan, Hardy--Littlewood--Sobolev and
Stein--Weiss inequalities on homogeneous Lie groups, arXiv:1810.11439v1,
https://arxiv.org/pdf/1810.11439 . The ordinary Euclidean statement in
Theorem 1.2 was inspected, including rendered page 1; Theorem 2.1 also
contains it as the additive-group case. In the paper's kernel convention,
N=3, lambda=2 and 1/q=1/p-1/3 give exactly the two pairs used in Section 2.
Only this classical inequality is used; no sharp constant, kinetic theorem,
or endpoint weak-type extension is assumed.

Repository inputs read include PLAN, AGENTS, docs/proof.md, the terminal
portion of the canonical graph, research/verify.py, KPC and KCH, the kinetic
source ledger, the terminal reset, the recent velocity-entropy/single-channel
proof, pointwise-vorticity/helicity evidence, and the viscous-mixing falsifier.
The prepared-Fisher/stress and older exclusions were also checked against
PLAN and the recent serious commit history. They retain their original scopes.
Source inspection and author self-checks are not independent mathematical
audit. No exhaustive prior-art assessment or novelty claim is made.
