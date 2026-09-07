# Temporal Type-I local-energy closure for concentrating-return tangents

Date: 2026-09-07.
Frozen research input: `5a3912806a6e3883afaacb746fa0b43638a580b0`.
Status: author derivation; independent mathematical audit pending.
Outcome: B, a scoped spatial-energy restriction on hypothetical singularities.
NS-R3 is NOT PROVED. No canonical graph promotion, formal proof, or novelty claim.

## 1. Terminal gate and the new producer

The equation remains original unforced NS on R3. The parent is the maximal
classical mild branch from one solenoidal Schwartz datum and fixed nu>0.
The preceding concentrating-return theorem gives the following conditional
object, without inheriting global finite energy from that parent:

* a marked ancient unit-viscosity mild U, |U|<=1 for s<=0,
  |U(0,0)|=1, and |U|<=1/2 for s<=-A;
* one exact concentrating local return, with factor lambda>1 and possibly
  a rotation, translation, and Galilean boost;
* an explicitly constructed continuation, with endpoint T>0, drift v,
  center xi, and |v|<=1/2, for which

    W(z,s)=U(xi+z+v s,s)-v,
    ||W(s)||_infinity <= K/sqrt(T-s),  s<T,
    K=lambda sqrt(T)(1+|v|).                              (1.1)

Here T and K describe that tangent, NOT the original parent's unknown
critical norm or its physical terminal time. The preceding theorem also
proves that W is unbounded at its future endpoint.

The selected new statement X is: every whole-space mild trajectory obeying
(1.1) has scale-uniform local energy, dissipation, cubic velocity, and
pressure-oscillation budgets on ALL backward cylinders ending at or before
T. In particular its drift-subtracted energy on every ball grows at most
linearly in radius. Endpoint local energy is produced, not presumed.

Positive leverage is the canonical NS pressure relation. With a_r(t) the
supremum of the squared L2 velocity over balls of radius r, its near and far
pressure contributions to cutoff energy work are BOTH bounded by

    C ||W(t)||_infinity a_r(t)/r.                         (1.2)

Thus the coefficient requires the first power of the temporal amplitude,
which is integrable up to a Type-I endpoint. An M(t)^2 Gronwall estimate
would instead diverge logarithmically. Section 3 proves (1.2), including
the far-pressure gauge and all spatial tails, on the actual mild equation.

The complete scoped contradiction is

    finite parent Tstar + a fast-record tangent with a concentrating return
                        + superlinear drift-subtracted spatial energy growth
      -> the genuine temporal Type-I continuation (banked theorem)
      -> X (proved here)
      -> linear energy growth, contradicting the specified superlinear growth.

Section 6 supplies a robust finite-history consequence; this is not only a
statement about an exactly symmetric object assumed without an adapter.
No theorem forcing ANY return, or a Type-I bound on the arbitrary parent,
is asserted. Compatible finite-local-energy return tangents, nonreturning
fast tangents and slow records still need a terminal contradiction.

## 2. Exact solution class and canonical pressure

Work at unit viscosity until Section 7. A mild solution satisfies the full
heat/Oseen integral identity on every compact time interval, not merely its
pairings with compact divergence-free tests. Assume it is bounded on each
such interval. Bounded mild regularity [S1, Section 4] supplies the smooth
spatial and time derivatives used below at every interior time. No spatial
decay, global L2/L3 membership, or uniform bound through T is assumed.

Write N(x)=1/(4 pi |x|) and K_ij(x)=partial_i partial_j N(x), x!=0.
The full distribution partial_i partial_j N includes its local delta term;
all occurrences of R_i R_j below mean the FULL double-Riesz operator,
with multiplier -xi_i xi_j/|xi|^2. Its L2 and L^(3/2) bounds are the ordinary
Calderon--Zygmund bounds. For the L2 bound Plancherel suffices.

Fix c in R3 and r>0. Choose chi supported on B_(8r)(c), equal to one on
B_(4r)(c), and between zero and one. On B_(2r)(c) a canonical pressure
representative is

    p_c,r = p_near + p_far,
    p_near = sum_ij R_i R_j(chi u_i u_j),
    p_far(x) = sum_ij integral (1-chi(y))
                     [K_ij(x-y)-K_ij(c-y)] u_i(y)u_j(y) dy.  (2.1)

At any fixed interior time the far integral is absolutely convergent:
|K_ij(x-y)-K_ij(c-y)|<=C r |y-c|^(-4) on its support and u is bounded.
Differentiating removes the subtracted term. Thus the gradients from (2.1)
agree on overlapping balls and equal the canonical distribution
sum_ij partial_k partial_i partial_j N*(u_i u_j).

Here is why this is the actual pressure gradient, not just a solution of
its Poisson equation. On a compact time interval put f=u tensor u in the
full mild identity. In the kernel representation of exp(t Delta)P div f,
applying partial_t-Delta gives div f plus the canonical gradient above.
This can be checked first for compact f by Fourier transformation. For
bounded f, truncate f spatially and test against a compact smooth function.
The differentiated Newtonian kernel has integrable O(|y|^(-4)) tails;
the remaining compact part is a distribution of finite order. These facts
pass the identity to the cutoff limit. Equivalently one may apply the
heat operator directly to the Oseen representation as in [S1, (3.21)--(3.22)].
It follows that

    partial_t u-Delta u+div(u tensor u)+grad p_c,r=0.       (2.2)

There is no extra spatially constant acceleration. Such an acceleration
would not satisfy the FULL mild identity. Smoothness makes (2.2) the usual
local classical equation and justifies its local energy equality. Pressure
representatives on connected overlaps differ by functions of time only;
these cancel from cutoff work since integral u.grad phi=0. We use precisely
this freedom, not an arbitrary harmonic pressure.

The kernel-difference normalization and the distinction from an additional
time-dependent harmonic-pressure drift are established pressure structure;
compare [S2, Theorem 1 and Section 6]. Their role here is to fix the class,
not to import the new estimates as a theorem from that source.

## 3. The pressure-work lemma and its temporal closure

Let [a,b) be an interval on which u is mild as above. Put

    M(t)=||u(t)||_infinity,
    a_r(t)=sup_(c in R3) integral_(B_r(c)) |u(x,t)|^2 dx.   (3.1)

On each compact time interval these are finite and bounded. The supremum
in a_r can be taken over rational centers, since the ball integrals are
continuous in c. Hence it is measurable. In particular no differentiation
of a maximizing center or of a_r is required.

Covering by balls of radius r gives, for L>=r,

    integral_(B_L(c)) |u|^2 <= C(1+L/r)^3 a_r.             (3.2)

Applying this to (2.1), the L2 multiplier bound gives

    ||p_near||_2 <= C ||chi u tensor u||_2
                 <= C M a_r^(1/2).                      (3.3)

The constant is independent of c, r, and u; covering B_(8r) uses a fixed
number of radius-r balls. For the far part, sum the annuli of radii 2^k r:

    ||p_far||_(L-infinity(B_(2r)(c)))
      <= C r sum_(k>=2) (2^k r)^(-4) 2^(3k) a_r
      <= C a_r/r^3.                                     (3.4)

The convergent factor is sum 2^(-k). There is no far-field decay assumption
and no infinite-energy constant mode has been discarded without its gauge.

Take phi_c,r(x)=phi((x-c)/r), where 0<=phi<=1 is smooth, equals one on B1,
and is supported in B2. Its local energy equality is

    integral |u(t)|^2 phi_c,r
      +2 integral_a^t integral |grad u|^2 phi_c,r
    = integral |u(a)|^2 phi_c,r
      +integral_a^t integral |u|^2 Delta phi_c,r
      +integral_a^t integral (|u|^2+2p_c,r)u.grad phi_c,r.  (3.5)

Diffusion and convection errors are at most C r^(-2) a_r and
C r^(-1) M a_r, respectively. By (3.3), the absolute near-pressure work is
at most C M a_r/r. By (3.4) and Cauchy--Schwarz, the far-pressure work is
at most

    C a_r^(3/2)/r^(5/2) <= C M a_r/r,                    (3.6)

where the LAST inequality uses the always-valid bound

    a_r <= |B1| r^3 M^2.                                (3.7)

It is a pointwise-in-time amplitude bound, not a hypothesized Morrey bound.
This proves the claimed first-power coefficient (1.2).

**Lemma 1 (uniformly local energy from integrable amplitude).** For a<t<b,

    a_r(t) <= C a_r(a) exp[C((t-a)/r^2
                              +(1/r)integral_a^t M(s)ds)],       (3.8)

and the same upper bound, with a possibly larger universal C, controls

    sup_c integral_a^t integral_(B_r(c)) |grad u|^2.       (3.9)

Proof: discard the positive term in (3.5), use (3.2)--(3.7), and take the
supremum over c AFTER integration. This gives

    a_r(t) <= C a_r(a)
                +C integral_a^t (r^(-2)+M(s)/r) a_r(s) ds.

Ordinary integral Gronwall proves (3.8). Inserting it back into (3.5) proves
(3.9), since the integral of g(s)exp(integral_a^s g) is its exponential
minus one. First work with t bounded away from b; if integral_a^b M<infinity,
the bounds are uniform as t approaches b and monotone convergence passes
the dissipation integral to that endpoint. QED.

This is not a local regularity or continuation criterion: it concludes
local ENERGY finiteness, not bounded velocity or global regularity.
It is used as a proved producer in the singularity restriction below.

## 4. Temporal Type-I gives all critical local budgets

**Theorem 2.** Let u be an ancient unit-viscosity mild solution on t<T,
bounded on every compact time interval, and suppose

    ||u(t)||_infinity <= K/sqrt(T-t) for all t<T, K<infinity.     (4.1)

Then a function F(K)=C K^2 exp[C(1+K)], with universal C sufficiently large,
has the following properties. For every r>0, center c, and top time tau<=T,
with a=tau-r^2,

    sup_(a<t<tau) integral_(B_r(c)) |u(t)|^2 <= F(K) r,
    integral_a^tau integral_(B_r(c)) |grad u|^2 <= F(K) r.       (4.2)

Moreover

    integral_a^tau integral_(B_r(c)) |u|^3 <= 2K F(K) r^2,      (4.3)
    integral_a^tau integral_(B_r(c)) |p-(p)_(B_r(c))|^(3/2)
       <= C[K F(K)+F(K)^(3/2)] r^2.                           (4.4)

Thus the supremum over all such cylinders of the conventional quantities
A+E+C+D is bounded solely in terms of K. The same single canonical pressure
modulo time constants is used; a different physical pressure is not chosen
for each cylinder. No spatial 1/|x| pointwise estimate is claimed.

Proof: set d=T-tau>=0. At the starting time,

    a_r(a) <= |B1| K^2 r^3/(d+r^2) <= |B1| K^2 r.

The coefficient in Lemma 1 obeys

    (tau-a)/r^2=1,
    (1/r) integral_a^tau M(s)ds
       <= (2K/r)(sqrt(d+r^2)-sqrt(d)) <= 2K.              (4.5)

Lemma 1 therefore gives (4.2). Multiplying the energy bound by M(s) and
integrating gives (4.3).

For (4.4), use the same near/far split on B_r(c). The L^(3/2) double-Riesz
bound, covering, and |u|^3<=M|u|^2 imply

    integral_(B_r(c)) |p_near|^(3/2) <= C M a_r.

The far contribution is at most C a_r^(3/2)/r^(3/2). With (4.2) and (4.5),
its time integral and that of the near contribution are bounded by the
right side of (4.4). Subtraction of the actual spatial mean costs only a
universal factor, by Jensen and the triangle inequality. All estimates
were first proved below tau; integrability and monotone convergence give
tau=T as well. QED.

**Endpoint trace.** The theorem supplies a unique weak L2_loc trace u(T).
Indeed u is uniformly L2 on each compact set. For a compact smooth vector
test psi, (2.2) shows that the derivative of integral u.psi is time integrable
up to T: the Laplacian term can be transferred to psi, the quadratic term
uses local L2 energy, and the pressure term uses (4.4). A time-dependent
pressure constant pairs to zero with div psi. The scalar pairings are
Cauchy, giving the weak trace. Weak lower semicontinuity passes local energy
inequalities to it. This asserts neither strong L2 convergence nor smooth
continuation through T. The trace also has integral_(B_r(c))|u(T)|^2<=F(K)r.

At any fixed t<T, choose tau>t sufficiently close with tau<=T and t>tau-r^2.
Then (4.2) gives the all-center spatial bound

    sup_c integral_(B_r(c)) |u(x,t)|^2 dx <= F(K) r
                 for EVERY r>0.                        (4.6)

This is linear energy growth, not finite total energy and not global L3.

## 5. What concentrating-return singularities are now excluded

Apply Theorem 2 to the banked W in (1.1). On the original marked interval,
translations of observation centers give

    sup_c integral_(B_r(c)) |U(y,s)-v|^2 dy <= F(K) r,
                     s<=0, r>0.                         (5.1)

All the cylinder budgets in (4.2)--(4.4) also hold in the constant Galilean
frame through the tangent's actual future endpoint. Hence no marked tangent
with a concentrating return can exhibit

    sup_(c,r) r^(-1) integral_(B_r(c)) |U(y,s)-v|^2 = infinity   (5.2)

on even one slice. In particular superlinear bulk energy growth is excluded.
This conclusion was NOT assumed in the preceding return theorem. It is
produced by the actual pressure work and temporal Type-I bound, not by
incorrect inheritance of the parent's global finite energy.

A concrete geometric consequence: a nonconstant such U cannot have two
linearly independent spatial periods on a single time slice. The same
periods hold for U-v. Since that slice is not identically v (otherwise mild
uniqueness and time analyticity contradict the marks), one small ball has
positive energy. Its translates by the rank-two period lattice give order
R^2 disjoint equal-energy balls inside a ball of radius R. This contradicts
(5.1). These are periodic directions, not directions of continuous
translation invariance; fully three-dimensional fields can have them.
The more general packing consequence is that disjoint fixed-radius balls,
each carrying at least e>0 of |U-v|^2 energy inside B_R, number at most
F(K)(R+r)/e. No compulsory branching property is deduced from that upper bound.

## 6. Robust finite-history and actual-record adapter

The all-radius conclusion (5.1) is for the LIMIT. It must not be claimed
uniformly over all radii in finite-energy prelimit fields after subtracting
a nonzero constant v. We now give the correct fixed-observation statement.

Fix A,R_ret,B,delta,D,r_obs,Z>0, with B>=delta, and a compact scale interval

    1+sigma <= lambda <= Lambda,  sigma>0.

Observe a local return between times -B<=alpha<beta<=0 with beta-alpha>=delta,
rotation Q in SO(3), translation |a_vec|<=D and arbitrary boost b_vec. Put

    E_ret(W)=integral_(B_R_ret) |W(y,beta)
         -lambda Q W(lambda Q^T(y-a_vec),alpha)-b_vec|^2 dy,
    v_par=(I-lambda Q)^(-1)b_vec,
    T_max=B/((1+sigma)^2-1),
    K_max=(3/2)Lambda sqrt(T_max).                         (6.1)

**Theorem 3.** There exist eta>0 and finite L_*>max(A,B), depending only on
the fixed parameters, such that every unit-viscosity mild W on [-L,0],
L>=L_*, satisfying the usual marks

    |W|<=1, |W(0,0)|=1, |W|<=1/2 for s<=-A,

and E_ret(W)<=eta obeys

    sup_(|c|<=Z) integral_(B_r_obs(c)) |W(y,0)-v_par|^2 dy
                      <= [F(K_max)+1] r_obs.             (6.2)

Proof: otherwise choose lengths tending to infinity, return errors tending
to zero and violations of (6.2). The boosts are bounded because

    |b_vec| |B_R_ret|^(1/2)
       <= (1+Lambda)|B_R_ret|^(1/2)+E_ret^(1/2).

All return parameters and a sequence of violating observation centers have
convergent subsequences. The inverse defining v_par is uniformly bounded:
|(I-lambda Q)z|>=(lambda-1)|z|>=sigma|z|. Bounded mild compactness, with the
standard common forward extension across zero, gives a marked ancient U.
The return-source arguments stay in a fixed compact ball. Both the return
and observation integrals therefore pass to the limit. The limit has an
exact concentrating local return. The banked theorem gives 0<T<=T_max and
|v|<=1/2, hence K<=K_max. Formula (5.1) contradicts the limiting energy at
least [F(K_max)+1]r_obs. Choosing F increasing proves the assertion. QED.

For actual first records M_n=2^n M0 at t_n and any maximizer x_n, set

    U_n(y,s)=u(x_n+(nu/M_n)y,t_n+(nu/M_n^2)s)/M_n,
    ell_n=M_n^2(t_n-t_(n-1))/nu,
    L_n=M_n^2 t_n/nu.

The existing Oseen record bound gives L_n>=(c_rec/3)(4^n-1). Therefore all
sufficiently late records with ell_n<=A and the small single-return error
in Theorem 3 obey (6.2), with thresholds independent of u0, nu, M0 and x_n.
The physical observation is exactly

    integral_(B_r(c)) |U_n(y,0)-v_par|^2 dy
      = (M_n/nu^3) integral_(B_(nu r/M_n)(x_n+nu c/M_n))
                          |u(x,t_n)-M_n v_par|^2 dx.      (6.3)

Thus a fast-record sequence with the stated single return and a persistent
violation of this produced energy ceiling is ruled out on actual unforced
whole-space NS. This is an added singularity restriction, not a conditional
criterion postulating the desired energy ceiling as an input.

## 7. Adversarial tests and why this does not close NS-R3

Scaling: at general viscosity the lemma has nu/r^2+M/r in its exponent;
its dissipation is nu times the gradient integral. Normalize an ancient
Type-I field by v(y,s)=u(y,nu^(-1)s)/nu, or use the physical record scaling
in (6.3). For the original coordinates the energy ceiling has the form
C nu^2 r when ||u(t)||_infinity<=K sqrt(nu/(T-t)). No nu is suppressed in
the parent-to-tangent adapter.

Non-mild test: u(x,t)=c/sqrt(T-t) with
p(x,t)=-c.x/[2(T-t)^(3/2)] is a smooth differential-equation solution below
T but is not mild. It has infinite endpoint local energy. The additional
linear pressure does NOT satisfy (2.1); it is precisely what the full mild
identity excludes. It cannot be inserted into Theorem 2 as a counterexample.

Localized smooth data: Lemma 1 permits arbitrarily large amplitude and any
bounded smooth initial data, and does not assert their future Type-I bound.
Concentration packets obey its exact dimensions. Nearly linear and Beltrami
solutions obey the same local pressure estimate on their lifespans. None
supplies an arbitrary-data Type-I producer. The recorded single-channel
NS interaction is not contradicted and no instantaneous branching is assumed.

Forcing and local-energy countermodels: (3.3)--(3.6) use p generated by the
ACTUAL tensor u tensor u with no external force. An arbitrary causal stress,
a scalar energy/enstrophy curve, or local energy inequality with unrelated
pressure cannot be substituted. The prior Fisher, entropy, covariance,
Euler-shear, and forced-Stokes exclusions retain their exact scopes.

No full terminal proof follows. F(K) need not be small. Linear spatial energy
growth does not imply finite global energy, global L3 or pointwise 1/|x|
decay: even at the level of smooth solenoidal fields, unit bumps placed along
a line can have uniformly O(r) ball energy but infinite total cubic norm.
This is only a norm-separation test, NOT an NS counterexample. Accordingly
the spatial Type-I assumptions in [S4] have NOT been established here.

Choosing a more remote starting time in (3.8) does not make the estimate
small: the starting energy decreases but the diffusion and transport exponent
grows. The scale-invariant constants in (4.2)--(4.4) likewise give no
nonsummable cost for successive parent packets. Such a cost still scales
as nu^3/M_n. No arbitrary singularity has been proved recurrent. Fast
nonreturning and slow-record cases have not acquired (4.1) in this note.

## 8. Source comparison, status, and required review

[S1] G. Koch, N. Nadirashvili, G. Seregin and V. Sverak,
Liouville theorems for the Navier-Stokes equations and applications,
Acta Math. 203 (2009), 83--105; arXiv:0709.3599v1.
https://arxiv.org/html/0709.3599v1
Inspected (3.21)--(3.22), Section 4's full bounded mild definition, interior
regularity, and Lemma 6.1. These give the exact class and compactness, not
the Type-I-to-local-energy conclusion proved above.

[S2] P. G. Fernandez-Dalgo and P. G. Lemarie-Rieusset,
Characterisation of the pressure term in the incompressible Navier-Stokes
equations on the whole space, DCDS-S 14 (2021), 2917--2931;
arXiv:2001.10436v1. https://arxiv.org/html/2001.10436v1
Inspected Theorem 1, the kernel-difference pressure, harmonic-drift freedom,
and mild formulation in Section 6. The printed heat-limit typo in the
v1 Proposition 3.1 is not used; its intended large-heat-time condition is
stated correctly in Theorem 1. Our mild-pressure identification is given
explicitly in Section 2, with no appeal to a Poisson equation alone.

[S3] D. Albritton and T. Barker, On local Type I singularities of the
Navier-Stokes equations and Liouville theorems, J. Math. Fluid Mech. 21
(2019), article 43; arXiv:1811.00502.
https://arxiv.org/html/1811.00502
Inspected Definitions/estimates (1.1)--(1.5), Lemmas 2.5--2.6, Theorem 3.1
and Remark 3.2. IMPORTANT: Remark 3.2 explicitly warns that the temporal
L-infinity Type-I bound alone does not appear to guarantee the critical
local energy package, or even endpoint local energy. We do NOT cite that
paper as proving Theorem 2. This note supplies a separate author argument
using the first-power pressure-work estimate on the full whole-space mild
class. That point needs particular independent scrutiny; source comparison
is not independent certification and no priority claim is made.

[S4] B. Pineau and V. Vicol, On rotated backwards self-similar solutions
of the incompressible 3D Navier-Stokes equations, arXiv:2607.09619.
https://arxiv.org/html/2607.09619
Inspected (1.9)--(1.10), Theorems 1.4, 1.6--1.7 and their spatial Type-I
hypotheses. Their nonexistence theorem is NOT applied to a merely temporal
bound or to (4.6). No new literature theorem is promoted into the graph.

Required independent audit: reconstruct (2.2) from the FULL Oseen identity;
check the uniform-center far-pressure estimate and the use of (3.7);
check supremum-after-integration and endpoint pressure integrability;
check every time/radius/viscosity factor and the fixed-observation order
in Theorem 3. This is a same-session author derivation, not its own audit.

NS-R3/CRITICAL remain gaps. This note proves a producer for the stated
spatial-energy restriction on return tangents, not the full paper proof
requested for the arbitrary-data terminal theorem. Existing evidence,
kinetic/microscopic contracts, manuscripts, and formalization are preserved.
