# Heat resonance obstructs static slaving; causal memory has a factorial refinement bound

Date: 2026-09-07. Research wave after planning commit
`dfd7abc866a7d548b24ffeac91bb092d258a1c0d` (original input `f0add720`).
Status: complete author derivations of the theorems stated below; independent
mathematical audit and prior-art assessment pending. No novelty claim.
NS-R3 is NOT proved. These are a scoped architecture obstruction and a positive
periodic calibration of the proposed refinement producer, NOT a strict
singularity reduction for whole-space arbitrary data.

## 1. Frontier-math packet and the first invalid bridge

MODE: FALSIFY -> REPAIR -> INTEGRATE, following krystophny/prompts at
2929639d8ed611917bd1086df002296a611a475b. The proof-audit checklist was read
and used for author rechecking; no independent reviewer or worker is claimed.

TERMINAL CLAIM: the unchanged NS-R3 statement and conditional critical-limit
suffix in PLAN and research/refinement-slow-manifold-contract.md.

FIRST TEST: can all modes above an arbitrary spectral cutoff be expressed
by a time-independent C2 invariant graph tangent to the low spectral space,
so that a second-order invariance correction removes their forcing?

EXACT OBSTRUCTION: a nonzero quadratic NS interaction has output decay rate
equal to the sum of the two input decay rates. The corresponding component
of the graph invariance equation reads 0=K, with K>0. The graph does not exist
even locally at zero for the particular cutoff family below.

REPAIR: retain the resonant evolution in an exact time-ordered Volterra
series, rather than divide by its zero denominator. In the SAME actual NS
sector, this yields a global-in-time factorial tail independent of the
Galerkin cutoff and an input-only critically weighted refinement sum.

REMAINING FIRST GAP: extending that bound to fully three-dimensional coupled
trajectories requires controlling signed strain and feedback; the special
sector has exactly zero such feedback. Theorems below do not supply it.
Neither the no-go nor the calibration replaces the original R3 target.

## 2. Exact projected equation and conventions

Use the fixed torus T3=(R/(2pi Z))^3 only for this calibration. All velocities
are real, solenoidal and have zero spatial mean. Let E_N be their Fourier
space with wavevectors |k|<=N, let P_N be its orthogonal projection, and set
A=-Delta and B_N(v,w)=P_N P_Leray[(v.grad)w]. Consider

    dot U_N+nu A U_N+B_N(U_N,U_N)=0,    nu>0.                  (2.1)

This is the exact Fourier--Galerkin equation, not a pseudospectral aliased
product. Spatially semidiscrete means time is not discretized. P_N commutes
with A and the Leray projection and is L2 orthogonal. Integration by parts
gives <B_N(U_N,U_N),U_N>=0, so

    (1/2)d||U_N||2^2/dt+nu||grad U_N||2^2=0.                  (2.2)

Thus the finite polynomial ODE has a global solution for every fixed N.
No mesh-uniform critical bound follows from this identity alone. For real
N>=1 the notation includes the modes in the closed Euclidean ball. All L2
norms below use the same fixed torus volume convention.

The infinite-cutoff sector in Section 4 is an exact smooth solution of the
ORIGINAL unforced periodic NS equation with p=0. It is not an R3 finite-energy
solution, not a forced Stokes solution, and not an arbitrary shell model.
Projection statements concern (2.1); the exact-sector statements concern NS.

## 3. A C2 static low/high manifold is obstructed at every integer cutoff

**Theorem 1.** Fix integer K>=1, viscosity nu>0 and finite N>=sqrt(2)K.
For (2.1) there is no C2 map Phi from a neighborhood of zero in E_K to
E_N intersect E_K^perp with

    Phi(0)=0, D Phi(0)=0,

whose graph is locally invariant. More precisely, no such Phi can have
invariance defect o(||v||^2) uniformly as v->0. In particular a polynomial
or analytic graph with a cubic-order invariance remainder is impossible.

**Proof.** Put lambda=nu K^2 and choose low eigenvectors

    X=(0,cos(Kx1),0),    Y=(0,0,cos(Kx2)),

and the high eigenvector

    Z=(0,0,cos(Kx1)sin(Kx2)).

The heat rates of X,Y are lambda,lambda, and that of Z is 2lambda. Its
wavevectors (plus/minus K,plus/minus K,0) have length sqrt(2)K, so Z is
retained at N but excluded at K. All three fields are solenoidal. Directly,

    (X.grad)X=(Y.grad)Y=(Y.grad)X=0,
    -(X.grad)Y=K Z.                                         (3.1)

Z is already solenoidal, so no pressure projection removes it. For
v=aX+bY the mixed quadratic coefficient of the full vector field is Kab Z;
its low projection is zero.

Let H=D^2 Phi(0)[X,Y]. The mixed ab coefficient of Phi(aX+bY) is H, with
no factor of two under this convention. Local invariance requires

    D Phi(v) F_low(v,Phi(v))=F_high(v,Phi(v)).                (3.2)

Because D Phi(0)=0, all quadratic interactions involving Phi contribute
only higher order. The mixed coefficient in (3.2) is consequently

    -2lambda H=-nu A H+K Z.                                 (3.3)

Project onto Z in L2. Self-adjointness of A and nu A Z=2lambda Z give

    -2lambda <H,Z>=-2lambda <H,Z>+K||Z||2^2,

a contradiction. C2 Taylor remainders suffice: Phi(v)=D^2 Phi(0)[v,v]/2
+o(||v||^2) and D Phi(v)=D^2 Phi(0)[v,.]+o(||v||). Thus the mixed
quadratic coefficient of the invariance defect cannot vanish for ANY Phi.
If that defect were o(||v||^2), its whole quadratic polynomial would vanish;
polarization would contradict (3.3). QED.

This also excludes any C2 invariant submanifold through zero tangent to E_K
with that dimension, since projection onto E_K gives a local graph by the
finite-dimensional inverse function theorem. It does NOT exclude a different
spectral selection including Z, time-dependent/history-dependent closure,
a less regular manifold, finite-error approximations retaining the quadratic
residual, or other kinetic slow manifolds. It is a failure of a specific
universal slaving premise, not a general inertial-manifold theorem.

The mechanism is the familiar homological resonance, not an asserted new
principle. For p+q=k its denominator is

    nu(|p|^2+|q|^2-|k|^2)=-2nu p.q.

Equation (3.1), rather than the denominator alone, proves nonzero forcing.
This is why merely checking diffusion eigenvalues or normal stability is
insufficient. The obstruction is present at arbitrarily small amplitude.
It therefore cannot be repaired by a smaller neighborhood with the same
C2 graph, tangent space, and invariance order.

For intuition ONLY, the resonant quadratic normal form

    dot a=-lambda a, dot b=-lambda b,
    dot c=-2lambda c+Kab

has the punctured graph Phi(a,b)=-(K/lambda)ab log(sqrt(a^2+b^2)/r0), r0>0.
It extends C1 but not C2 at zero. This scalar formula is not asserted to solve
the FULL NS graph problem; the rigorous full-sector repair follows next.

## 4. Repair inside the same NS dynamics, with all modes retained

Fix real amplitudes a0,b0, integer K>=1 and lambda=nu K^2. Use

    u(x,t)=(0,a(t)cos(Kx1),w(x1,x2,t)),
    a(t)=a0 exp(-lambda t),
    w(x1,x2,0)=b0 cos(Kx2).                                 (4.1)

Since the fields are independent of x3, their divergence is zero. Direct
substitution in ALL three NS components gives precisely

    partial_t w+a(t)cos(Kx1)partial_2 w
       =nu(partial_1^2+partial_2^2)w,                        (4.2)

and p=0 is a valid normalized pressure. In particular tr((grad u)^2)=0.
The shear equation has no feedback from w, but all advection of w in (4.2)
remains. Calling this triangular structure out explicitly prevents the
special model being passed off as general three-dimensional stretching.

Let H_K be the closed scalar L2 subspace generated by Fourier modes
(nK,+/-K,0), n in Z. The initial w0 lies in H_K. Both the heat semigroup
S(t)=exp(nu t Delta) and multiplication by cos(Kx1) followed by partial_2
preserve H_K. On this subspace,

    ||S(t)||_(L2->L2)<=exp(-lambda t),
    ||cos(Kx1)partial_2||_(L2->L2)<=K.                       (4.3)

The first statement uses the nonzero fixed transverse frequency K. The
second uses ||partial_2 f||2=K||f||2 and the bounded multiplier cos.
It would be FALSE with the same constant on arbitrary transverse frequencies.

For N>=K let P_N^s be the scalar Fourier cutoff and set
C_N=P_N^s cos(Kx1)partial_2 on H_K intersect range(P_N^s), with C_infinity
unprojected. Then ||C_N||<=K uniformly in N. It is skew-adjoint on this
subspace, because cos(Kx1) is independent of x2 and P_N^s is orthogonal.
The exact vector Galerkin equation (2.1) preserves (4.1), with

    dot w_N=nu Delta w_N-a(t)C_N w_N,    w_N(0)=w0.           (4.4)

Its energy equation and the fixed x2 frequency give

    ||w_N(t)||2<=exp(-lambda t)||w0||2.                     (4.5)

No smallness of a0,b0 or division by a resonance was used.

## 5. Global causal reconstruction with a factorial tail

Put

    alpha=|a0|/(nu K),
    A_t=alpha(1-exp(-lambda t)),
    (T_N f)(t)=-integral_0^t S(t-s)a(s)C_N f(s) ds,
    W_(0,N)(t)=S(t)w0,
    W_(m,N)=T_N W_(m-1,N), m>=1.                            (5.1)

This is a time-ordered causal expansion, not a Taylor series in physical time
and not an instantaneous slaving map. At each finite N it uses EXACT projected
convection, including transfers back towards lower x1 frequencies.

**Theorem 2.** For every N>=K, including N=infinity, the exact solution exists
smoothly for all t>=0 and for every integer M>=0 satisfies

    ||w_N(t)-sum_(m=0)^M W_(m,N)(t)||2
       <= ||w0||2 exp(-lambda t) A_t^(M+1)/(M+1)!,           (5.2)
    ||W_(m,N)(t)||2
       <= ||w0||2 exp(-lambda t) A_t^m/m!.                  (5.3)

The constants are independent of N and of the observation horizon. Alpha can
be any finite number. The estimate includes the critical-amplitude ordering
|a0|=alpha nu K without assuming alpha small. No inviscid-uniform statement
is claimed as nu->0 with a0 fixed.

**Proof.** The ordered integration region for T_N^m is
0<s_m<...<s_1<t. By (4.3), the product of heat norms and a final factor
exp(-lambda s_m) is exp(-lambda t). Each advection factor contributes
|a0|K exp(-lambda s_i). Since the remaining integrand is symmetric in the
s_i, integration over the ordered simplex is 1/m! times its integral over
the cube. Therefore if ||f(s)||2<=B exp(-lambda s),

    ||T_N^m f(t)||2<=B exp(-lambda t) A_t^m/m!.              (5.4)

For f=W_0 this gives (5.3). The series sum W_m converges uniformly in
weighted L2 on [0,infinity), since A_t<=alpha. It solves the Volterra equation
w=W_0+T_N w. Uniqueness follows from the same iterated estimate applied to a
zero-initial difference, or integral Gronwall on any finite interval.

For N=infinity every W_m has |k1|<=mK and |k2|=K. Thus its H^s norm is
bounded by a constant times (1+K^2(m^2+1))^(s/2) times the L2 bound in (5.3).
The factorial series converges for every fixed s and finite alpha. The
constructed w is smooth in space; the equation gives all time derivatives,
including at t=0 for the trigonometric datum. Integration by parts is now
legitimate and proves (4.5) also for this infinite-cutoff solution. This
constructs the global periodic NS solution; it does not assume its existence.

Finally iterate the EXACT Volterra equation M+1 times:

    w_N=sum_(m=0)^M W_(m,N)+T_N^(M+1)w_N.

Apply (5.4) to w_N using its stronger contractive bound (4.5). This proves
(5.2) without an extra exp(alpha) factor in the remainder. QED.

When N>=sqrt(2)K the first resonant coefficient is explicitly

    W_(1,N)(x,t)=a0 b0 K t exp(-2lambda t)
                                  cos(Kx1)sin(Kx2).          (5.5)

The secular factor t is retained and bounded, not divided away. The higher
W_m include further exact advection and are not inferred from this first
coefficient. For N=K, C_N w0=0 and w_K is the free heat solution, correctly
recording the cutoff omission instead of declaring (5.5) present there.

## 6. An input-only critical refinement certificate in this sector

**Theorem 3.** Let N_j=2^j K, j>=0, and let u_(N_j) solve (2.1) with the SAME
initial datum (4.1), independent of j. Then

    sum_(j>=0) N_j^(1/2)
       sup_(t>=0)||u_(N_(j+1))(t)-u_(N_j)(t)||2
       <= 2 sqrt(K)||w0||2 alpha exp(alpha).                (6.1)

In particular the proposed RF-SUM is proved for this periodic sector with
h_j=N_j^(-1). This is a benchmark success, not RF-SUM for arbitrary data or R3.

**Proof.** Induction on m shows that W_(m,infinity) has x1 frequencies nK,
|n|<=m, and transverse frequencies +/-K. Heat does not increase support;
each multiplication by cos(Kx1) shifts n by one. Therefore if

    N>=K sqrt(M^2+1),

all coefficients W_(m,N), 0<=m<=M, coincide EXACTLY with their infinite-cutoff
values. This statement includes the intermediate projections at every step.
For N_j=2^jK choose M_j=2^j-1 (also M_0=0). Then
sqrt(M_j^2+1)<=2^j, so the two adjacent solutions have the same first M_j+1
coefficients. Apply (5.2) twice and cancel those coefficients:

    ||u_(N_(j+1))(t)-u_(N_j)(t)||2
       <=2||w0||2 exp(-lambda t) alpha^(2^j)/(2^j)!.         (6.2)

The shear components are identical at every resolution. Multiplying by
sqrt(N_j), taking the time supremum, and summing yields the left side of
(6.1) bounded by

    2sqrt(K)||w0||2 sum_j sqrt(2^j)alpha^(2^j)/(2^j)!.

The dyadic summands are a subset of nonnegative integer summands, and
sqrt(n)<=n for n>=1. Consequently the sum is at most
sum_(n>=1)n alpha^n/n!=alpha exp(alpha). This proves (6.1). QED.

For clarity, the L3 consumer in this calibration needs no assumed finite-
element theorem. A band-limited trigonometric field f with |k|<=N obeys
||f||infinity<=C N^(3/2)||f||2 by Cauchy--Schwarz over Fourier coefficients.
Then ||f||3<=||f||2^(2/3)||f||infinity^(1/3)<=C N^(1/2)||f||2.
The difference of adjacent solutions has cutoff N_(j+1)=2N_j, so (6.1)
gives an absolutely convergent sum of L-infinity_t L3 differences. The coarse
term is finite and the limit is the exact smooth solution constructed above.
No numerical fitting of a convergence rate is part of this proof.

What makes this possible is bounded skew advection on the invariant fixed-
transverse-frequency sector and the integrable shear amplitude. The heat
resonance that prevents static C2 slaving does not prevent causal convergence.
The factorial high-order tail is not a claim about the general NS Picard
series, whose nonlinear operator is not bounded on this same Hilbert space.

## 7. The attempted extension and its first unsupported implication

To move towards RF3, consider independent coarse and fine trajectories v,U
on a common fine spectral space and w=U-v. With B=P_f P_Leray[(.grad).],

    dot w+nu A w+B(v,w)+B(w,v)+B(w,w)=F,
    F=-(I-P_c)B(v,v).                                      (7.1)

The error is not purely high frequency. The exact energy identity is

    (1/2)d||w||2^2/dt+nu||grad w||2^2
       =<F,w>-integral (w.grad)v . w.                       (7.2)

Theorem 2 used that the drift on w is skew and its operator norm is bounded
by a fixed transverse frequency times a prescribed integrable shear. Neither
property holds for the FULL operator in (7.1): B(w,v) contains strain; B(w,w)
is nonlinear even though its self-pairing vanishes; the relevant derivative
cost is not confined to the original K. Absolute values in (7.2) return
||grad v||infinity. Its finite value at each mesh is not a uniform estimate.

It is therefore INVALID to transplant the factorial bound (5.2) to (7.1)
with alpha replaced by a known energy norm. No proof or counterexample to a
more subtle signed cross-scale estimate is supplied here. This is the first
OPEN implication, not a demonstrated impossibility of RF3.

Matched resolved/unresolved energy feedback remains worth investigating, but
for actual projections P_c U rather than an independent coarse solution the
resolved equation changes as well. One must derive that equation and the
critical weighted pairings before using a passivity identity. Critical
weights need not share the energy cancellation. This is the strongest
surviving task; building more static graphs or enlarging the shear theorem
by cosmetic special cases would not address it.

## 8. Exact branch decisions

PROVED CLOSED: universal time-independent C2 spectral low-mode slaving with
Phi(0)=D Phi(0)=0 and o(||v||^2) invariance error for every cutoff. Theorem 1
falsifies it for each integer coarse K and N>=sqrt(2)K in a faithful
energy-preserving Galerkin family. It cannot be repaired by more Taylor
orders with the same variables. Retaining a quadratic residual is allowed,
but requires its own tracking bound rather than calling it third order.

PROVED VIABLE IN THE NAMED TEST: causal elimination retaining resonance, all
projected advection and the original datum. Theorems 2--3 give a complete
input-only, global-time, cutoff-uniform reconstruction and refinement bound
for (4.1). No small critical Reynolds number is needed in that sector.

OPEN, NOT RETIRED: other retained spectral selections, nonsmooth invariant
manifolds, history-dependent nonlinear manifolds, FEEC reductions, kinetic
normal contraction, geometric signed estimates for full NS, and RF3/RF4.
No finite experiment and no failure of the absolute-value estimate excludes
them. A different graph assertion reopens only with the precise resonance
or regularity premise that avoids Theorem 1.

The graph in Theorem 1 is a graph of dynamical low/high Fourier variables.
It is NOT the Dirac graph of pointwise observables from the previous no-go.
The reasons for failure are different and must not be merged.

## 9. Adversarial checks, prior art and audit status

Scaling: lambda=nu K^2 and alpha=|a0|/(nu K). Keeping alpha fixed while K grows
is the critical-amplitude test. The remainder is uniform after division by
||w0||2 and rescaling time by lambda. It does not imply an inviscid limit.

Signs: the NS vector field is MINUS projected convection. Equation (3.1)
therefore gives positive Kab Z; (5.5) has the same sign. Reversing that sign
still obstructs a graph, but would be a false reconstruction coefficient.

Cutoff edges: N=sqrt(2)K includes the resonant mode under the closed-ball
convention. N=K omits it. M=0, a0=0, b0=0 and j=0 are explicitly valid.
For a0=0 all refinements coincide, as (6.1) states. C_N is compressed
orthogonally, not an aliased collocation matrix, so its skew property holds
at the truncation boundary.

Mild versus classical: (5.1) constructs a mild scalar solution; factorial
convergence with polynomial Fourier weights gives smoothness and justifies
its energy identity. There is no assumed unknown continuum solution in the
error estimate. Global-time convergence uses the integral of the explicit
shear amplitude, not generic heat-kernel smoothing of a nonlinear solution.

Periodicity: the field is independent of x3 and periodic. No localization to
Schwartz R3 data is asserted, and no R3 asymptotic limit follows from this
benchmark. This is enough to falsify the UNIVERSAL spectral-closure premise,
not to refute or prove NS-R3. Box, FEEC, kinetic and particle adapters remain
unproved specifications in the separate contract.

Prior art: NS homological resonances and normal forms are established theory;
see Foias--Hoang--Saut, https://arxiv.org/html/1711.07184. Normal invariance
and tracking are distinct in Burby--Klotz, Section VI.1,
https://arxiv.org/html/2006.06636v1. These sources provide context, not an
unprinted step in Theorems 1--3. Volterra simplex estimates, skew transport
and Fourier Bernstein estimates are elementary and are proved here in the
needed scope. No discovery priority is claimed for this specialization.

A standard-library rational oracle `research/check_resonant_memory.py`
checks the resonance numerator/denominator, compressed skew matrices, exact
low-order exponential-polynomial Duhamel coefficients, cutoff support, and
factorial-envelope recurrence. Its finite range is stated by its output.
Those checks do not prove the universal PDE assertions, establish prior art,
or constitute independent mathematical review. The proof-audit checklist
was applied by the same author context; independent audit remains pending.

## 10. Cycle verdict and next distinct action

MODE / RESULT: a precise static-slaving falsification followed by a positive
causal-memory repair and critical-refinement theorem in an exact NS sector.
CLAIM AND SCOPE: Theorems 1--3 above, periodic Galerkin/all-mode sector only.
EVIDENCE: complete derivations, exact-rational finite regression oracle.
FIRST GAP: input-only control of full three-dimensional signed strain and
retained feedback in (7.1)--(7.2), with critical weights across all resolutions.
SURVIVING CONDITIONAL SUFFIX: a genuine general RF-SUM plus the contract's
consistency/whole-space/energy/trace interfaces implies NS-R3 via the banked
continuation theorem. No such general RF-SUM is proved.
NON-CLAIMS: no NS-R3 proof, no strict singularity reduction, no all-data
convergence rate, no FEEC implementation, no kinetic realization or MIC-R3.
NEXT DISTINCT ACTION: derive a paired, time-integrated estimate for the full
resolved/unresolved feedback, including B(w,v), in one faithful fine-space
system; check whether a critically weighted correction controls the term
without an unknown strain integral. If not, retain the exact open term;
do not present another passive sector as a solution of that obligation.
