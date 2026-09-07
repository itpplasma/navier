# One-slice rigidity and finite-order three-dimensionality of fast records

Date: 2026-09-07.
Frozen input: `f0e5b4e7caec580800285c8f40d599191e7b36f8`.
Status: complete author derivation using the precisely scoped imports below;
independent mathematical audit pending. No novelty or priority claim.
Result: strict exclusion of asymptotically locally planar fast-record
concentration. NS-R3 is NOT PROVED. The general three-dimensional fast-record
case and the slow-record alternative remain open. No canonical graph promotion,
manuscript integration, or formal proof is made.

## 1. Selected mechanism and the exact contradiction it closes

The equation is the ORIGINAL unforced whole-space equation, with one fixed
positive viscosity nu and arbitrary solenoidal Schwartz initial data. Work
on its maximal classical mild branch [0,Tstar). No forced response, shell
model, kinetic surrogate, or inequality trajectory is substituted for it.

The terminal-reset record construction supplies a bounded ancient MILD
unit-viscosity limit when infinitely many dyadic record transitions have
bounded normalized duration. It retains two amplitude marks, not finite
energy, spatial decay, a critical integral norm, or a minimal critical orbit.

The new rigidity statement is:

> A bounded ancient mild three-dimensional NS solution which, on one time
> slice, is independent of a fixed spatial direction on one nonempty open
> ball is a single constant vector in space and time.

Its positive mechanism is spatial analyticity, forward uniqueness followed
by time-analytic continuation, and the two-dimensional ancient NS theorem.
The third velocity component is handled explicitly, rather than discarded.
The hardest internal step is propagation of a ONE-SLICE LOCAL symmetry to
an ancient three-component flow and elimination of that flow in the correct
nondecaying mild class. Section 4 proves it.

The complete contradiction proved in this note is

    finite Tstar AND locally planar fast-record concentration
      => a two-time-marked ancient mild U, locally planar at time zero
      => U is one constant vector
      => its half-amplitude past and unit-amplitude present contradict.

The first implication is the banked record extraction plus local convergence;
the second is Theorem 1 below; the last is arithmetic. We then prove uniform
finite-history and finite-jet versions, so the result excludes approximate
local planarity along actual record sequences, not only an exactly symmetric
ancient solution assumed from the outset.

This is a strict singularity reduction, NOT a complete contradiction from
Tstar<infinity alone. No statement that all blow-ups become planar is assumed
or proved. The existing input-only L-infinity_t L3_x consumer is not treated
as a decomposition or used as an unproved hypothesis here.

## 2. Exact normalization, record bounds, and solution class

Choose M0>||u0||_infinity and put Mn=2^n M0. When these levels are reached,
let tn be their FIRST hitting times for ||u(t)||_infinity. For n>=1 define

    ell_n = Mn^2 (tn-t_(n-1))/nu.

Choose any spatial maximum xn with |u(xn,tn)|=Mn and set

    U_n(y,s) = Mn^(-1) u(xn+(nu/Mn)y, tn+(nu/Mn^2)s),
    P_n(y,s) = Mn^(-2) p(xn+(nu/Mn)y, tn+(nu/Mn^2)s),
    L_n = Mn^2 tn/nu.                                      (2.1)

All terms in the equation scale by Mn^3/nu, so U_n has viscosity ONE,
nonlinearity coefficient ONE, and the original Leray mild formulation. There
is no moving mean, inviscid limit, or change of the parent viscosity. The
classical branch has spatially decaying continuous slices, so the nonzero
maximum is attained. A finite maximal time forces arbitrarily large records,
as in `terminal-reset/04-marked-ancient.md` and [S1, Section 6].

First hitting gives, on the entire available past,

    |U_n|<=1 on [-L_n,0],             |U_n(0,0)|=1,
    |U_n|<=1/2 on [-L_n,-ell_n].                           (2.2)

The Oseen estimate used in the banked record argument is, with a universal
C_K absorbing the time integral,

    Mn <= Mn/2 + C_K nu^(-1/2) Mn^2 sqrt(tn-t_(n-1)).

Consequently

    ell_n >= c_rec := (2 C_K)^(-2)>0,
    L_n >= c_rec sum_(j=1)^n 4^(n-j)
         = (c_rec/3)(4^n-1).                              (2.3)

The last inequality uses tn>=sum_(j=1)^n(tj-t_(j-1)); t0>=0.
It will make the eventual record threshold independent of the datum, nu,
and the chosen initial level.

For A>0 define the marked ancient class C_A by

    U is an ancient unit-viscosity mild solution on R3 x (-infinity,0],
    |U(y,s)|<=1 for s<=0,            |U(0,0)|=1,
    |U(y,s)|<=1/2 for s<=-A.                               (2.4)

Here mild means the Oseen integral identity on EVERY finite subinterval,
including the prescribed bounded initial slice of that subinterval. Bounded
ancient weak solutions with arbitrary harmonic-pressure drift are not silently
identified with this class.

Each U in C_A extends uniquely across time zero to a fixed interval [0,delta],
with bound 2, by bounded-data local mild existence. The same extension applies
to the normalized finite histories in (2.2). Delta>0 is universal. It ensures
that time zero is an interior regular time for compactness and analyticity.

If ell_n<=A along a sequence tending to infinity, (2.2)-(2.3) and bounded
mild compactness give a limit in C_A. The earlier half bound is retained
because s<=-A implies s<=-ell_n. This does not assert that EVERY singular
branch has such a sequence: ell_n may tend to infinity.

## 3. Precisely scoped analytic inputs and compactness

We use the following inspected primary-source statements.

**Bounded mild existence, uniqueness, regularity and ancient compactness.**
[S1, estimate (4.8), Proposition 4.1, Lemma 6.1] gives the bounded-data mild
fixed point, interior spatial/time derivative bounds, and compactness on
expanding backward intervals. Their hypotheses allow nondecaying bounded
whole-space velocities. By restarting on a short preceding interval, a
uniform bound on an ancient mild velocity gives uniform spatial derivative
bounds of every fixed order at every time. No global L2 or L3 norm is needed.

**Spatial analyticity.** [S3, Theorem 3.1] states that a bounded solenoidal
initial velocity has a unique local mild solution with a bounded holomorphic
extension to a strip of width comparable to sqrt(t), for a time comparable
to the inverse square of its initial supremum norm. Restarting shortly before
any slice proves that slice is real analytic on all R3. This is the L-infinity
version, not an L3 theorem applied to a limit lacking L3 control.

**Time analyticity.** [S2, Theorem 3.1] proves pointwise time analyticity for
bounded whole-space mild NS solutions, without decay or spatial integrability.
On its normalized slab the bound is

    sup_(0<t<=1) t^m ||partial_t^m U(t)||_infinity
       <= N^(m+1) m^m,       m>=1.                         (3.1)

Time translation and parabolic scaling apply it on each finite interior
slab. We use the real-analytic identity theorem in time at fixed spatial
points. We do NOT infer joint real analyticity merely from separate space
and time analyticity.

**Two-dimensional ancient rigidity.** [S1, Theorem 5.1] states that a bounded
ancient WEAK NS velocity on R2 is spatially constant, possibly a function
b(t). It does not itself classify all bounded three-dimensional ancient flows.
The time-dependent constant allowed in the weak class is dealt with below.

For clarity, the compactness needed here is stronger than bare weak energy
compactness. Extend the bounded histories across zero as above. Interior
bounds and a diagonal subsequence give convergence in C^k on every compact
set for every fixed k. The limit is mild: in its integral identity, the heat
kernel and the differentiated Oseen kernel have integrable spatial tails;
the latter's L1 norm is at most C(t-s)^(-1/2). Uniform velocity bounds permit
first truncating the time integral away from its upper endpoint and the
spatial convolution to a large ball, passing local convergence there, and
then removing both truncations. No pressure-tail hypothesis is added.
The same argument proves sequential compactness of C_A, including its marks.

## 4. The hardest lemma: one-slice local planarity forces constancy

**Theorem 1 (one-slice rigidity).** Let U be a bounded ancient mild solution
of unit-viscosity unforced NS on R3. Suppose at some time s0, at which the
solution is smooth through the slice, there are a unit vector e and a
nonempty open ball B such that

    partial_e U(y,s0)=0 for y in B.                        (4.1)

Then U is a single constant vector on its ancient domain. A terminal slice
with bounded data is permitted by the local extension described above.
No finite energy, decay, periodicity, or critical integral bound is assumed.

**Proof.** Spatial analyticity makes every component of partial_e U(.,s0)
real analytic on the connected space R3. Vanishing on B therefore gives
vanishing on all R3. In particular, for each real h,

    U(y+h e,s0)=U(y,s0) for every y.

The translated solution and the original solution are bounded mild solutions
with the same data at s0. Local uniqueness makes them equal on a nonempty
forward interval. For fixed y and h their difference is analytic in time
throughout the connected ancient interval, extended a little beyond s0.
The time-analytic identity theorem makes the difference zero on the entire
interval. This is the BACKWARD step; forward uniqueness alone would not
justify it. Applying this argument to each h proves translation invariance
in direction e at all ancient times.

Rotate coordinates so e=e3, and write

    U(x,t)=(v1(x1,x2,t),v2(x1,x2,t),w(x1,x2,t)).             (4.2)

The horizontal field v=(v1,v2) is a bounded ancient weak solution of the
TWO-dimensional NS equation. One direct justification uses a compact
horizontal solenoidal test phi(x1,x2,t), multiplies it by a compact function
eta(x3) of integral one, and sets the third test component to zero. This is
a three-dimensional solenoidal test. Integrals of eta' and eta'' vanish,
so the three-dimensional weak identity becomes exactly the two-dimensional
identity. No pressure convention at infinity or finite-energy reduction is
being assumed. Theorem 5.1 of [S1] now gives v(x1,x2,t)=b(t).

It remains to eliminate w; omitting this step would leave a 2D3C gap.
The vorticity is

    Omega=(partial_2 w,-partial_1 w,0).

It is uniformly bounded on the entire ancient domain by the interior
spatial derivative bounds for bounded ancient mild U. Its stretching is
EXACTLY zero:

    (Omega dot grad)U=(0,0,
       (partial_2 w)(partial_1 w)-(partial_1 w)(partial_2 w))=0.

The actual NS vorticity equation therefore gives

    partial_t Omega+b(t) dot grad_H Omega=Delta_H Omega.    (4.3)

Let B'(t)=b(t) and put F(z,t)=Omega(z+B(t),t). This change of variables is
applied to (4.3), not asserted to be an unforced NS symmetry with arbitrary
acceleration. F is a bounded ancient caloric field on R2. For any a<t,
bounded heat uniqueness and the Gaussian gradient estimate give

    ||grad_H F(t)||_infinity
       <= C(t-a)^(-1/2)||F(a)||_infinity.

Let a tend to minus infinity. Thus F, and hence Omega at each time, is
spatially constant. Since w is bounded on all R2, its now constant first
spatial derivatives must be zero. Consequently Omega=0 and U is spatially
constant at every time. Finally the MILD identity, whose nonlinear spatial
divergence is then zero, gives U(t)=U(a) for every a<t. U is one constant
vector in time as well. This completes the proof. QED.

**Corollary 1.** No member of C_A is independent of any one fixed spatial
direction on any open ball on any one time slice. Otherwise Theorem 1 and
the two bounds 1/2 and 1 in (2.4) contradict each other.

This proves more than nonzero curl somewhere in the amplification slab.
A three-component planar shear can have nonzero curl, but cannot satisfy
this one-slice condition as a marked positive-viscosity ancient mild flow.
It says nothing against the stationary EULER shear in the earlier
vanishing-effective-viscosity record construction.

## 5. Uniform local separation and a finite-order witness at the peak

Let |.|_F denote the Euclidean norm of the FULL ordered derivative tensor.
For example, the entries of partial_e grad^(m-1) U are
partial_e partial_(i1)...partial_(i_(m-1)) U_j, summed over all ordered
indices and all components. This convention is rotation invariant.

**Theorem 2 (uniform ancient gaps).** For every finite A>0 and every R>0
there is gamma(A,R)>0 such that every U in C_A obeys

    min_(|e|=1) integral_(B_R) |partial_e U(y,0)|^2 dy
       >= gamma(A,R).                                    (5.1)

Moreover there are a finite integer K(A)>=2 and eta(A)>0 such that

    min_(|e|=1) sum_(m=1)^K(A)
       |partial_e grad^(m-1) U(0,0)|_F^2 >= eta(A).         (5.2)

These are uniform existence statements for constants; no numerical values
or effective rate in A or R are claimed. If C_A is empty the inequalities
are vacuous and any positive constants may be chosen.

**Proof of (5.1).** Otherwise choose U_j in C_A and unit e_j with the
integrals tending to zero. Compactness gives U_j -> U in C^1 locally and,
after a subsequence, e_j -> e. The marks pass to U. The limit integral is
zero, so the continuous field partial_e U(.,0) vanishes on B_R. Theorem 1
makes U constant, contradicting its marks. QED.

**Proof of (5.2).** If no finite K has a positive uniform lower bound, choose
U_j in C_A and e_j in the unit sphere for which the sum through order j is
less than 1/j. Use compactness in every fixed derivative order and e_j -> e.
For the resulting marked U, ALL spatial derivatives of partial_e U vanish
at the origin. Spatial analyticity makes partial_e U zero in a neighborhood.
Theorem 1 again contradicts the marks. Hence a finite K and positive eta
exist. QED.

The condition K>=2 is essential rather than cosmetic. At the unit speed
maximum, U(0,0)^T grad U(0,0)=0, because grad |U|^2=0. Thus the 3 by 3
Jacobian has rank at most two and has a nonzero spatial null direction.
The first-order-only version of (5.2) is always false for a member of C_A.
The theorem concerns a finite HIGHER jet, not a pointwise full-rank claim.

## 6. Finite history suffices: no infinite-past hypothesis on the parent

**Theorem 3 (finite-memory form).** Fix A>0 and R>0. There exist finite
L_*(A,R)>A and kappa(A,R)>0, with the same finite K(A) as in Theorem 2,
such that every unit-viscosity bounded mild history W on [-L,0], L>=L_*,
satisfying

    |W|<=1,  |W(0,0)|=1,  |W|<=1/2 on [-L,-A],            (6.1)

obeys BOTH (5.1) and (5.2) with their right sides replaced by kappa(A,R).
A common bounded forward extension exists automatically, as before.

**Proof.** When C_A is nonempty, take one half the smaller of its positive
gaps in Theorem 2. If arbitrarily long histories violate either inequality,
choose lengths tending to infinity and a subsequence violating the same
inequality. Interior compactness and compactness of the directions give a
limit in C_A. The relevant integral or finite jet converges, contradicting
the corresponding ancient gap. This supplies a finite L_* for both bounds.
If C_A is empty, histories of arbitrarily large length would themselves
produce a member of C_A; hence all sufficiently long history classes are
empty and the assertion is vacuous. QED.

This is a qualitative compactness threshold, not a disguised endpoint norm.
All its bounds and marks will be supplied by first-record selection in the
original equation. No hypothesis about unknown accumulated strain is used.

## 7. The necessary condition on an actual hypothetical singularity

**Theorem 4 (uniform three-dimensionality of sufficiently late fast records).**
Fix A>0. There exist a finite N_A, a finite integer K_A>=2, and kappa_A>0,
independent of u0, nu, M0 and n, with the following property. Every actual
classical whole-space NS branch and each of its records (2.1) with

    n>=N_A and ell_n<=A

satisfy, at EVERY spatial point xn attaining Mn,

    min_(|e|=1) (1/(nu Mn))
      integral_(B_(nu/Mn)(xn)) |partial_e u(x,tn)|^2 dx
        >= kappa_A,                                      (7.1)

and

    min_(|e|=1) sum_(m=1)^K_A
       [nu^(2m)/Mn^(2m+2)]
       |partial_e grad^(m-1)u(xn,tn)|_F^2
        >= kappa_A.                                      (7.2)

For any other fixed normalized radius R>0 the same assertion holds with
constants depending on A,R. No global regularity is asserted by this theorem.

**Proof.** Use Theorem 3 with R=1 and choose N_A such that
(c_rec/3)(4^N_A-1)>=L_*(A,1). Formula (2.3) gives the required history
length. If ell_n<=A, (2.2) gives all of (6.1) for W=U_n. Apply Theorem 3.
The changes of variables are exactly

    integral_(B_R) |partial_e U_n(y,0)|^2 dy
       = (1/(nu Mn)) integral_(B_(R nu/Mn)(xn))
                             |partial_e u(x,tn)|^2 dx,
    grad_y^m U_n(0,0) = nu^m Mn^(-m-1) grad_x^m u(xn,tn).

They prove (7.1)-(7.2). None of the constants depended on which maximizing
point was chosen. QED.

In particular, a finite-time singularity CANNOT have a sequence of records
n_j -> infinity, with ell_(n_j)<=A<infinity, and directions e_j for which

    (1/(nu M_(n_j))) integral_(B_(R nu/M_(n_j))(x_(n_j)))
       |partial_(e_j) u(x,t_(n_j))|^2 dx -> 0              (7.3)

for even ONE fixed R>0. Directions may rotate with j. No global approximate
symmetry or small directional norm on all of R3 is required. Equivalently,
a fast marked tangent cannot be locally two-dimensional at its terminal
slice. The finite-jet statement additionally rules out loss of a spatial
direction to arbitrarily high derivative order at the concentration center.

Thus the sharpened exhaustive alternative is

    Tstar<infinity
      => either ell_n -> infinity,
         or there are infinitely many fast records, and for every finite A
         all sufficiently late records with ell_n<=A obey (7.1)-(7.2).
                                                               (7.4)

In the first branch the existing banked conclusion is

    (Tstar-t) H(t)^2/nu -> infinity,
    H(t)=sup_(0<=s<=t)||u(s)||_infinity.

This is a RUNNING maximum statement, not a silently substituted bound on
||u(t)||_infinity. The slow alternative is neither excluded nor weakened by
Theorems 1--4. In the second branch, one-slice locally planar concentration
has now been removed; genuinely three-dimensional fast profiles remain.

## 8. Adversarial checks and exact scope

**Scaling and concentration packets.** Equations (7.1)-(7.2) are dimensionless
under the fixed-viscosity NS scaling, including the factors of nu. Arbitrary
smooth compact concentration packets do not satisfy the long-history
amplification premise merely by being concentrated. No estimate is asserted
for all divergence-free snapshots or all initial data at time zero.

**Highly localized data and first-order degeneracy.** Compact velocities can
have planar plateaus initially. They have no automatically long normalized
past with the two marks. Positive-time spatial analyticity alone forbids
exact open-set symmetry for many finite-energy slices, but supplies NO uniform
separation under blow-up rescaling. The ancient rigidity and the two marks
are what produce that separation here. The mandatory null direction of the
first derivative at a speed maximum was explicitly retained in Section 5.

**Nearly linear and helical configurations.** The bounded ancient heat class
is constant, so it cannot supply the two amplitude marks. Nonconstant exact
Beltrami heat evolutions at positive viscosity grow without bound backwards;
finite-time helical configurations are not thereby excluded. The theorem
assumes no helicity sign, alignment sign, or pointwise stretching monotonicity.
It does not classify all fully three-dimensional near-Beltrami tangents.

**The recorded single-channel interaction.** The trigonometric field
V=(cos y,cos x,cos x+cos y) and its compact localizations remain valid
instantaneous NS interaction tests. They have no proved arbitrarily long
bounded history with these amplitude marks. Theorems 1--4 neither refute that
calculation nor assert compulsory daughter channels at a single interaction.
They concern the original equation throughout an amplification history.

**Energy-class concentration and summability.** A normalized cylinder with
an order-one gradient integral has physical integrated viscous loss of order
nu^3/Mn. Indeed nu integral |grad_x u|^2 dx dt equals
(nu^3/Mn) integral |grad_y U_n|^2 dy ds. Dyadic costs of that order are
summable. These new geometric gaps do NOT change that scaling or create a
nonsummable energy cost. They are not an energy contradiction or an L3 bound.

**Prior countermodels.** The slow-record comparison curve has a nonzero NS
curl residual and is not used as a solution. The periodic viscous-mixing
family has varying parent viscosities, unbounded parent times and an
inviscid centered limit; it is not in this fixed-unit-viscosity ancient
class. Its Euler shear falsifier remains valid in its precise scope. The
forced Stokes stress counterexample and kinetic Fisher/entropy exclusions
are unaffected. No countermodel class is promoted to unforced NS.

**Mild versus weak and global versus local.** Time-dependent constant weak
flows with harmonic-pressure drift are excluded by the MILD identity, not
by a tacit decay assumption. Local space-time NS solutions without a global
bounded mild past do not satisfy Theorem 1's hypotheses. The local planar
condition is on one FIXED direction on an open set, not a direction field
which may vary with position. Quantitative minimization over directions
allows rotation from one record to another, not pointwise adaptive directions.

## 9. What changed, and the strictly smaller remaining obstruction

Previously, the marked-record evidence forced some nonzero curl in a
bounded amplification slab, with a quantitative rotational witness on a
sufficiently large ball. It did not state or prove the one-slice local
symmetry propagation, the orientation-uniform fixed-ball gap, the finite
higher-jet witness, or their universal late-record transfer.

The new result excludes exactly the local-planarity sequences (7.3), and
also the finite-jet collapse ruled out by (7.2), on actual fast records.
The proof uses established analyticity/Liouville theorems and supplies their
nondecaying, three-component, one-slice and record-history adapters explicitly.
It is not advertised as a new general Liouville theorem or as new priority
for the underlying analytic theory. It does not establish existence of
any nonconstant ancient flow or of any finite-time singularity.

The remaining cases are (i) genuinely three-dimensional fast marked
concentration obeying these gaps, and (ii) slow records ell_n -> infinity.
A complete NS-R3 proof must still exclude both using an additional actual-NS
dynamical mechanism. One cannot simply assume that blow-up planarizes, turn
the finite-jet lower bound into nonsummable energy loss, or replace the slow
case by the fast case. This note closes a specified geometric contradiction,
not either of those additional implications.

Independent review of Theorems 1--4 remains necessary. Same-session algebra,
source checks and document checks are author checks only. NS-R3/CRITICAL
remain gaps in the canonical graph; kinetic and microscopic contracts and
all earlier mathematical evidence are preserved.

## 10. Sources and inspection record

[S1] G. Koch, N. Nadirashvili, G. Seregin and V. Sverak,
*Liouville theorems for the Navier--Stokes equations and applications*,
Acta Math. 203 (2009), 83--105.
https://arxiv.org/html/0709.3599v1
Inspected Sections 4--6: mild estimate (4.8), Proposition 4.1, Theorem 5.1,
Lemma 6.1 and the record/blow-up construction. Only the TWO-dimensional
Liouville conclusion is imported; the 2D3C adapter is proved in Section 4.

[S2] H. Dong and Q. S. Zhang, *Time analyticity for the heat equation and
Navier--Stokes equations*, J. Funct. Anal. 279 (2020), 108563.
https://arxiv.org/html/1907.01687v2
Theorem 3.1, its bounded MILD hypotheses, estimate (3.1), the kernel argument
and the warning about non-mild flows were inspected. No decay or L3 assumption
is inserted into its application.

[S3] Z. Grujic, *A geometric measure-type regularity criterion for solutions
to the 3D Navier--Stokes equations*, Nonlinearity 26 (2013), 289--296.
https://arxiv.org/pdf/1111.0217
Theorem 3.1 and Remark 3.1 were inspected in text and rendered PDF page 5
(zero-based page 4). ONLY bounded-data spatial analyticity and its local mild
scope are used. The paper's sparseness regularity criterion is not imported
as an arbitrary-data producer. This source states the L-infinity estimate
in the earlier Grujic--Kukavica/Guberovic/Kukavica analytic theory.

Repository inputs inspected include AGENTS, PLAN, docs/proof.md and the
canonical graph; terminal-reset/01--05, compactness.md, intrinsic records
and the viscous-mixing falsifier; KCH, KPC, the programme graph and kinetic
source ledger; the prepared Fisher/stress, local velocity-entropy/single-
channel and integrated vorticity-entropy/covariance evidence; and the latest
serious commits. research/verify.py was also read. These inspections do not
independently certify any earlier author-only theorem.
