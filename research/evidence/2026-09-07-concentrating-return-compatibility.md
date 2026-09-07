# Concentrating returns: a common endpoint and discrete unrotated scales

Date: 2026-09-07.
Frozen research input: `b70c6486ae4087f5673c39b7b7bbd6e2df7b4d8d`.
Status: author derivation; independent mathematical audit pending.
Outcome: B, a scoped singularity reduction, NOT a proof of NS-R3.
No novelty/priority claim, canonical graph promotion, or formal proof.

## 1. Gate, mechanism, and exact remaining scope

Keep the original unforced whole-space NS equation, arbitrary solenoidal
Schwartz input and each fixed nu>0. Its first-record normalization is in
Section 8. The retained ancient class C_A consists of unit-viscosity MILD
solutions U on R3 x (-infinity,0], with

    |U(y,s)|<=1,  |U(0,0)|=1,  |U(y,s)|<=1/2 for s<=-A.       (1.1)

A common bounded local extension through zero is supplied by bounded-data
mild theory. Neither global finite energy nor spatial decay is inherited.
C_A might be empty. No existence of a nonconstant ancient solution is asserted.

The preceding note excludes a local return

    U(y,beta)=lambda Q U(lambda Q^T(y-a),alpha)+b,             (1.2)

when alpha<beta<=0 and 0<lambda<=1. In this note lambda>1: the return
CONCENTRATES the earlier profile. Here alpha,beta are times, a is a spatial
translation, b a velocity boost, and Q belongs to SO(3).

The selected rigidity X concerns competing concentrating returns. Every exact
return (1.2), even if initially known only on one open ball, forces a genuine
self-similar continuation of the tangent to a prospective future endpoint.
All such returns of one marked tangent must have the SAME endpoint and
backward limiting velocity. Unrotated returns must also have the same center
in that Galilean frame, and all their scale factors belong to ONE discrete
cyclic scaling group. In particular, two unrotated returns with irrational
logarithmic scale ratio are impossible.

Positive mechanism: actual NS symmetry, bounded mild uniqueness and
analyticity propagate the local copy relation. Symmetry constructs the
future continuation rather than assuming it. Oscillation amplification fixes
its endpoint, while backward decay fixes its drift. Spatial commutators and
the banked one-slice planar rigidity fix unrotated centers. A dense group of
scales would then produce a bounded stationary Leray profile. The nonlinear
Leray Liouville theorem [S4], not compactness or heat smoothing alone, excludes
that profile. The bounded-profile conclusion is CONSTANCY; mildness is used
to remove the remaining time-dependent constant, not an invented decay bound.

The completed scoped chain is

    finite Tstar + fast records with two incompatible local concentrating returns
      -> a marked ancient mild U with those returns
      -> X (common endpoint/drift and discrete unrotated scales)
      -> contradiction.

Section 7 makes the exclusion robust for approximate returns, including small
rotations and perturbations of the specified scales. Section 8 transfers it
to actual records, without assuming an ancient past for the parent solution.

This does NOT force recurrence, let alone two independent returns. A single
concentrating return, compatible powers of one scale, general rotated returns,
nonreturning fast evolution, and slow records are not excluded. The theorem
therefore does not close NS-R3. The rest of this note proves X and its exact
consumer rather than claiming an input-only critical estimate.

## 2. Inputs, local-to-global propagation, and the time domain

Use bounded mild existence/uniqueness and compactness [S1], spatial
analyticity in the bounded-data class [S2], and time analyticity for bounded
whole-space mild solutions [S3]. The preceding two record notes spell out
these interfaces. For expanding bounded histories, extend through zero by
a fixed positive time before taking local smooth limits, so the unit mark
survives. The heat/Oseen identity passes to the limit using integrable spatial
tails and the integrable near-time factor (s-r)^(-1/2). No global energy or
pressure-tail hypothesis is added.

Fix one concentrating return and define

    r=lambda^2,  q=alpha-r beta,
    phi(s)=r s+q,
    T=(r beta-alpha)/(r-1)=beta+(beta-alpha)/(r-1).           (2.1)

Thus phi(s)=T+r(s-T) and T>beta, but positivity of T has NOT yet been proved.
The transformed field is

    V(y,s)=lambda Q U(lambda Q^T[y-a-b(s-beta)],phi(s))+b.     (2.2)

This is a solution of the SAME unforced equation: the time derivative of the
moving argument contributes -lambda^2 Q[(Q^T b).grad U], while the boost in
convection contributes the opposite term. The other terms have the common
factor lambda^3 Q, with pressure lambda^2 P composed with the argument.
Mildness follows by changes of variables in the heat/Oseen identity; the
Galilean change uses the constant-drift heat semigroup, whose transport term
is precisely the nonlinear cross term. This is the calculation in Section 3
of the preceding local-return note and works for every lambda>0 on the
common domain, not only lambda<=1.

Spatial analyticity first makes (1.2) global on the slice s=beta. Mild
uniqueness gives U=V just afterwards. Time analyticity of U and V AS MILD
SOLUTIONS then gives equality throughout their connected common domain.
On the original histories this includes

    s < min(0,phi^(-1)(0)),                                (2.3)

with the endpoint traces supplied by their local extensions. Both fields
are bounded on that common past. We do not infer joint analyticity merely
by composing separate space/time analytic functions with a moving argument.

## 3. A concentrating return fixes the future lifespan and backward drift

**Theorem 1.** If U in C_A satisfies (1.2) with lambda>1, then T in (2.1)
is positive. There are explicitly determined vectors v and xi such that

    W(z,s)=U(xi+z+v s,s)-v

obeys

    W(z,s)=lambda Q W(lambda Q^T z,T+lambda^2(s-T)).          (3.1)

It has a unique mild continuation to all s<T, bounded on each compact time
interval, with

    sup_(s<T) sqrt(T-s) ||W(s)||_infinity
        <= lambda sqrt(T) (1+|v|).                         (3.2)

The maximal future bounded-mild lifespan from the slice U(.,0) is exactly T,
and the continuation is unbounded near (xi+v T,T). Also

    ||U(.,s)-v||_infinity -> 0 as s -> -infinity,
    |v|<=1/2.                                              (3.3)

These assertions are conditional on the existence of U and its return. They
are not a construction of a Schwartz-data singularity or a claim of finite
energy for the continued tangent.

### 3.1 Positivity of the prospective endpoint

Let D(s)=sup_(x,y) |U(x,s)-U(y,s)|, so D(s)<=2 on s<=0. For the equality
U=V in (2.3), the spatial argument is a bijection and the boost cancels:

    D(s)=lambda D(phi(s)).                                 (3.4)

Suppose T<=0. For any s<beta, all inverse iterates
s_k=T+lambda^(-2k)(s-T) increase to T and are in the common domain.
Indeed phi^(-1)(0)=T(1-lambda^(-2))>=T. Equation (3.4) gives

    D(s_k)=lambda^k D(s)<=2.

Thus D(s)=0 for every s<beta. U is spatially constant on that past, and its
mild identity makes the constant independent of time. Time analyticity then
extends that constant throughout the original ancient interval, contradicting
(1.1). Therefore T>0. In particular phi(0)=(1-r)T<0, so U=V holds throughout
s<=0 and a little beyond zero.

### 3.2 Removing the boost and spatial translation

Define

    v=(I-lambda Q)^(-1)b,
    k=lambda Q^T(v beta-a)-v alpha,
    xi=(I-lambda Q^T)^(-1)k.                                (3.5)

The matrices are invertible since lambda>1 and Q is orthogonal. In particular
b=v-lambda Qv. Substituting U(x+v s,s)-v into (2.2) cancels the s-dependent
translation, because

    lambda Q^T(v-b)-lambda^2 v=0.

Its remaining spatial argument is lambda Q^T x+k. Shifting by xi, whose
fixed-point equation is xi=lambda Q^T xi+k, proves (3.1). This is a constant
Galilean frame, not an accelerating frame or an added force.

### 3.3 The continuation is constructed, not assumed

For any s<T choose an integer m>=0 large enough that
s_m=T+lambda^(2m)(s-T)<=0. Define

    W_ext(z,s)=lambda^m Q^m
      W(lambda^m (Q^T)^m z,s_m).                            (3.6)

The original (3.1) makes this independent of the sufficiently large choice
of m. On a neighborhood of any fixed s<T, use one common m with s_m<0.
Formula (3.6) there is an actual scaled/rotated mild NS solution. Definitions
agree on overlaps, giving a smooth mild solution on all s<T. Restoring v and
xi gives the original continuation, which is unique by bounded mild local
uniqueness. Relation (3.1) now holds for every s<T in both directions.

Every s<T can be carried by an integer scaling iterate into the fundamental
interval

    T-lambda^2 T <= s_base <= 0.

On that interval the original bound is ||W||_infinity<=1+|v|. The quantity
sqrt(T-s)||W(s)||_infinity is invariant under the iterates. This proves (3.2),
and also (3.3)'s uniform backward convergence. The older half-amplitude mark
then implies |v|<=1/2.

U(.,0) is not spatially constant: such a slice, by mild uniqueness and time
analyticity, would make the original marked history constant. Choose finite
z1,z2 with d=|W(z1,0)-W(z2,0)|>0. At

    s_j=T(1-lambda^(-2j)),
    z_(i,j)=lambda^(-j)Q^j z_i,

(3.6) gives

    |W(z_(1,j),s_j)-W(z_(2,j),s_j)|=lambda^j d.              (3.7)

Both physical points xi+v s_j+z_(i,j) tend to xi+v T. Thus at least one
velocity diverges along this pair, and there is no bounded mild continuation
through T. The constructed continuation exists until T, so T is precisely
its maximal future bounded-mild lifespan. QED.

**Corollary 1 (compatibility of arbitrary rotated returns).** Any two exact
concentrating local returns of one U in C_A have the same T and v in
(2.1)/(3.5). The first conclusion follows from uniqueness of the maximal
bounded-mild continuation of U(.,0); the second follows from the unique
uniform backward limit (3.3). There is no commutativity assumption on Q.

T is an output attached to the continued tangent. It is NOT proved to
coincide with a limit of Mn^2(Tstar-tn)/nu for the parent solution, nor is it
an input-only continuation time for that solution. The Type-I estimate (3.2)
is temporal and drift-subtracted; no spatial 1/|z| decay is asserted.

## 4. Unrotated returns must share a spatial center

**Theorem 2.** All exact concentrating local returns of U in C_A with Q=I
have the same xi in their common Galilean frame. Hence they have the same
space-time endpoint (xi+v T,T).

**Proof.** Corollary 1 already fixes T and v. In that common frame write the
spatial maps for two returns as

    f_i(x)=lambda_i x+(1-lambda_i)xi_i,
    phi_i(s)=T+lambda_i^2(s-T).

Both identities extend to the unique continuation s<T. To see this for the
second identity, its transformed continuation is defined for all s<T, since
phi_i preserves that interval. On every compact time interval both fields
are bounded mild, so time analyticity extends equality from the old common
past throughout s<T.

The affine time maps commute. Composing the spatial maps and inverses in
the order f_1 f_2 f_1^(-1) f_2^(-1) gives translation by

    h=(lambda_1-1)(lambda_2-1)(xi_1-xi_2).                  (4.1)

All velocity prefactors cancel. Thus h is a spatial period of the solution
at every s<T. Conjugating this identity by powers of the first similarity
gives periods lambda_1^(-j)h at every time. If h were nonzero, smoothness and
these periods would imply

    h.grad U=0

at each point and time: divide the zero increment over lambda_1^(-j)h by
lambda_1^(-j) and pass to the limit. The banked one-slice planar rigidity
would make the original marked U constant, a contradiction. Thus h=0,
and xi_1=xi_2. QED.

The planar input here is the full three-component result in the preceding
one-slice note: spatial/time analytic propagation, the two-dimensional
ancient theorem for horizontal velocity, the exact stretching cancellation
for the third component's vorticity, and mildness to remove time-dependent
constants. No two-dimensional hypothesis on the present U was assumed.
This argument makes no assertion that rotated returns share the same xi.

## 5. The hardest remaining lemma in this reduction: the scale group is discrete

**Theorem 3 (discrete unrotated scale group).** Suppose U in C_A has at
least one unrotated concentrating local return. In the common frame from
Theorems 1--2 there is a number lambda_0>1 such that the set of all positive
scale symmetries of the continued flow is precisely

    {lambda_0^j : j in Z}.                                (5.1)

Every unrotated concentrating local return has lambda=lambda_0^j for some
positive integer j. In particular two such returns cannot have
log(lambda_1)/log(lambda_2) irrational.

**Proof.** Translate the common endpoint time to zero and let
w(z,t)=U(xi+z+v(T+t),T+t)-v, for t<0. Consider

    H={h in R : w(z,t)=exp(h)w(exp(h)z,exp(2h)t)
                    for all z in R3 and t<0}.              (5.2)

Compositions and inverses show H is an additive subgroup. Continuity of w
shows H is closed: for h_j->h pass to the limit at any fixed (z,t), whose
transformed time stays strictly negative. H contains the positive log scale
of the given return. A nonzero closed additive subgroup of R is either
h_0 Z with h_0>0 or all of R. For completeness, if its positive elements have
positive infimum, closedness attains that infimum and Euclidean division
shows every element is an integer multiple. If their infimum is zero,
integer multiples of arbitrarily small positive elements approximate every
real number, so closedness gives R.

If H=R, take exp(h)=(-t)^(-1/2) in (5.2). Then

    w(z,t)=(-t)^(-1/2)F(z/sqrt(-t)),  F(z)=w(z,-1).         (5.3)

F is smooth and globally bounded, because -1 is an interior time of the
constructed continuation. Substitution into the actual NS equation gives

    -Delta F+(F.grad)F+(1/2)y.grad F+(1/2)F=-grad P,
    div F=0.                                              (5.4)

P is the smooth pressure on the slice t=-1; no spatial integrability or
chosen harmonic pressure is needed to apply the following theorem.

Chae--Wolf [S4, Theorem 1.2 and Remark 1.3] imply that every smooth bounded
solution F of (5.4) is CONSTANT. Their theorem uses a positive threshold
on the local L^q tail for q>3/2. For bounded F, choose the threshold larger
than ||F||_infinity: that tail is empty. It is important that the conclusion
here is constant, not zero by a nonexistent L^p decay assumption.

By (5.3), w is now spatially constant at every time. Its MILD identity on
any finite interval makes it time independent. The only time-independent
field of the form F/sqrt(-t) is zero. Thus the original U is the constant v,
contradicting (1.1). This rules out H=R. Taking lambda_0=exp(h_0) proves (5.1).
Theorem 2 places every other unrotated return in this same centered group,
so all its scales are positive integer powers of lambda_0. QED.

This uses a nonlinear Leray Liouville input, not a classification of all
bounded ancient three-dimensional NS flows. In particular it does not
eliminate a nontrivial discrete group. No quantitative lower bound on
lambda_0-1, uniform over C_A, has been established here.

## 6. Exact exclusions supplied by the three theorems

There is no U in C_A with either of the following configurations:

(i) two concentrating local returns, with arbitrary rotations, whose computed
T values differ, or whose computed backward drift vectors v differ;

(ii) two unrotated concentrating local returns with different Galilean
centers, or with irrational logarithmic scale ratio.

All times, translations and boosts in this exact assertion may be arbitrary
finite values consistent with alpha<beta<=0. Each equality may be known
on just one nonempty ball; the two balls need not be the same. The preceding
analyticity argument makes each global before compositions are used.

The following robust consequence uses a single fixed observation ball for
convenience and is what directly excludes approximate singularity patterns.

## 7. A robust two-return gap on long finite histories

Fix A,R>0, B>=delta>0, D>=0, and two numbers Lambda_1,Lambda_2>1 with
log(Lambda_1)/log(Lambda_2) irrational. For a history W define

    E_i = integral_(B_R) |W(y,beta_i)
          -lambda_i Q_i W(lambda_i Q_i^T(y-a_i),alpha_i)-b_i|^2 dy.
                                                               (7.1)

**Theorem 4.** There are epsilon>0, eta>0 and finite L_*>max(A,B) such that
every unit-viscosity mild history on [-L,0], L>=L_*, with

    |W|<=1,  |W(0,0)|=1,  |W|<=1/2 on [-L,-A],             (7.2)

satisfies E_1+E_2>=eta for all parameters obeying

    -B<=alpha_i<beta_i<=0,  beta_i-alpha_i>=delta,
    |a_i|<=D,  b_i in R3,
    |lambda_i-Lambda_i|<=epsilon,  lambda_i>1,
    Q_i in SO(3),  ||Q_i-I||_op<=epsilon.                  (7.3)

Thus the excluded class is robust: the actual scales need not have an
irrational log ratio, and the actual rotations need not be identically zero.
The constants are qualitative, depend only on the displayed fixed parameters,
and have no asserted effective values.

**Proof.** Negating the assertion gives histories W_j of lengths tending to
infinity, with E_(1,j)+E_(2,j)->0, lambda_(i,j)->Lambda_i and Q_(i,j)->I.
Choose, for instance, epsilon_j<=1/j also smaller than
min_i(Lambda_i-1)/2. The boosts are automatically bounded. With V_R=|B_R|,

    |b_(i,j)| sqrt(V_R)
      <= (1+lambda_(i,j))sqrt(V_R)+sqrt(E_(i,j)).           (7.4)

The times, translations and boosts therefore have convergent subsequences,
and the limiting times retain their separation delta. Extend the histories
through zero by bounded mild theory and take an ancient local smooth limit
U retaining the marks. Source arguments in (7.1) stay in one fixed spatial
ball, since lambda_(i,j) is bounded and |a_(i,j)|<=D. Local uniform convergence
passes both integrals to zero. Continuity of U makes both limiting equalities
pointwise on B_R. They are unrotated concentrating returns with scales
Lambda_1,Lambda_2. Theorem 3 contradicts their irrational log ratio. QED.

A useful fixed pair is Lambda_1=2, Lambda_2=3: a rational log ratio would
imply 2^q=3^p for positive integers p,q, contrary to unique prime factorization.
This is an example of a forbidden PAIR of returns, not an exclusion of a
single dyadic or triadic concentrating cascade.

Similarly, Corollary 1 gives a uniform two-return gap for compact parameter
families with lambda_i bounded away from one and bounded above, and with
|T_1-T_2| bounded below by a positive constant. The formulas are then
continuous on that parameter family, and the same compactness proof applies.
No uniformity over unbounded times, translations or scaling factors is claimed.

## 8. Transfer to the original whole-space arbitrary-data branch

For the original nu>0 branch choose M0>||u0||_infinity and Mn=2^n M0, let tn
be the first hitting times of ||u(t)||_infinity=Mn, and choose ANY maximizer
xn. Use the exact fixed-viscosity normalization

    ell_n=Mn^2(tn-t_(n-1))/nu,
    U_n(y,s)=Mn^(-1)u(xn+(nu/Mn)y,tn+(nu/Mn^2)s),
    L_n=Mn^2 tn/nu.                                       (8.1)

First hitting gives |U_n|<=1, |U_n(0,0)|=1 and |U_n|<=1/2 for
s<=-ell_n. The banked heat/Oseen record estimate gives

    ell_n>=c_rec>0,
    L_n>=(c_rec/3)(4^n-1).                                (8.2)

The normalized equation has viscosity and nonlinear coefficient both one.

**Corollary 2 (necessary exclusion at actual fast records).** Fix the
parameters of Theorem 4. There are N<infinity, epsilon>0 and eta>0,
independent of u0,nu,M0,n and xn, such that for every n>=N with ell_n<=A,
the two errors (7.1), evaluated on U_n, satisfy E_1+E_2>=eta for all (7.3).

Indeed choose N so that the lower bound in (8.2) is at least L_*. First
hitting supplies the whole finite history (7.2), including its half mark
because ell_n<=A. Theorem 4 applies. No ancient-time hypothesis is assumed
for the parent solution and no critical norm is used to choose N.

In physical variables, for t_(i,-)=tn+nu alpha_i/Mn^2 and
t_(i,+)=tn+nu beta_i/Mn^2, put

    x_(i,-)(x)=xn+lambda_i Q_i^T[x-xn-(nu/Mn)a_i].

Then the exact conversion is

    E_i=(Mn/nu^3) integral_(B_(R nu/Mn)(xn))
      |u(x,t_(i,+))-lambda_i Q_i u(x_(i,-)(x),t_(i,-))-Mn b_i|^2 dx.
                                                               (8.3)

Consequently finite Tstar cannot have a sequence of fast records with BOTH
of these robustly incompatible concentrating return errors tending to zero.
This is the stated contradiction chain in Section 1 on actual unforced NS.

## 9. Adversarial checks and limitations of the attempted completion

Scaling: (8.1) and (8.3) retain every nu and Mn factor. The record, error,
rotation and logarithmic-ratio assertions are dimensionless under NS scaling.
T in Sections 2--5 is a normalized tangent time, not an uncontrolled physical
endpoint substituted into an estimate.

Local smooth data: a compact field can contain approximately repeated or
nearly planar pieces initially. It does not thereby have the arbitrarily
long bounded two-mark history used here. No universal instantaneous geometric
restriction or entropy law is asserted for all admissible initial data.

Nearly linear/Beltrami tests: nonzero heat modes are unbounded backward in
time; spatial constants fail the two marks. Finite-interval helical NS data
are not excluded. No favorable strain, helicity, pressure-work or covariance
sign is assumed. The recorded single-channel nonlinear interaction remains
valid and is not a sustained marked pair of the kind ruled out here.

Mildness is indispensable. The field U(y,s)=c/sqrt(T-s), with
p(y,s)=-c.y/[2(T-s)^(3/2)], solves the differential equations and has every
unrotated scaling about T. Taking |c|=sqrt(T) and A>=3T gives the two marks
on s<=0. It is NOT mild: a spatially constant mild solution is constant in
time. This explicit excluded-class test explains both the mild hypothesis
and why the bounded Leray-profile conclusion cannot be stated as zero
before the mild identity is used. It is not an NS-R3 counterexample.

Parameter degenerations: positive time separation and bounded observation
parameters are retained in Theorem 4. Its epsilon may be small and its eta
may deteriorate with these parameters. The theorem does not say that a small
irrational perturbation of arbitrary return parameters has a uniform cost
independent of the observed history. It gives a gap for each fixed parameter
family as stated. Rotated return groups are not classified by Theorem 3.

The central single-return obstruction survives: (3.6) constructs a possible
future Type-I tangent continuation rather than contradicting its existence.
No spatial decay was obtained. The recent Pineau--Vicol RSS/RDSS theorems
[S5] require a spatial Type-I bound of the form C/(|z|+sqrt(-t)), and further
rotation/period restrictions. Equation (3.2) is only the temporal supremum
bound and does not meet that source's spatial hypothesis. Those theorems
were therefore NOT inserted as an unsupported terminal step. Even the
unrotated stationary-profile theorem [S4] applies only after a DENSE scale
group produces (5.3); a discrete scale group does not make the profile
stationary in similarity time.

The physical cost of one critical packet remains of order nu^3/Mn. Neither
common-endpoint compatibility nor the return gap turns these dyadic costs
into a nonsummable quantity. There is no proof that every singularity has
any return. Slow records ell_n->infinity remain completely untouched, with
only the banked running-maximum consequence (Tstar-t)H(t)^2/nu->infinity.

All earlier counterexamples keep their premise classes. In particular,
vanishing-viscosity Euler-shear limits, forced Stokes responses, kinetic
Fisher counterexamples and scalar inequality curves are not treated as
original unforced whole-space singular NS solutions.

The strictly smaller remaining recurrent class has compatible T and v;
unrotated exact returns have a common center and a discrete scale group.
The robust pair exclusions add genuine necessary conditions to fast records.
Compatible concentrating returns, general rotated returns, nonreturning fast
profiles and slow records still need new dynamical arguments. NS-R3 and
CRITICAL remain gaps. This is not an end-to-end proof and not claimed novelty
relative to the general self-similar-solution literature.

## 10. Source and verification record

[S1] Koch, Nadirashvili, Seregin and Sverak, Liouville theorems for the
Navier-Stokes equations and applications, Acta Math. 203 (2009), 83--105.
https://arxiv.org/html/0709.3599v1
Section 4, Lemma 6.1, Remark 6.1 and the record construction were inspected.
The two-dimensional theorem is used through the banked 2D3C one-slice adapter.
No general three-dimensional ancient Liouville assertion is imported.

[S2] Grujic, A geometric measure-type regularity criterion for solutions to
the 3D Navier-Stokes equations, Nonlinearity 26 (2013), 289--296.
https://arxiv.org/html/1111.0217v1
Theorem 3.1's bounded-data spatial analyticity statement was inspected.
Its separate sparseness criterion is not used as a producer.

[S3] Dong and Zhang, Time analyticity for the heat equation and Navier-Stokes
equations, J. Funct. Anal. 279 (2020), 108563.
https://arxiv.org/html/1907.01687v2
Theorem 3.1's bounded MILD hypotheses and derivative bound were inspected.
No spatial integrability or decay is required by this input.

[S4] Chae and Wolf, On the Liouville type theorems for self-similar solutions
to the Navier-Stokes equations, Arch. Ration. Mech. Anal. 225 (2017), 549--572.
https://arxiv.org/html/1609.06962v1
Equation (4), Theorem 1.2 and Remark 1.3 were inspected directly. For a=1/2
and bounded smooth F, the superlevel-set hypothesis is empty above a threshold
larger than ||F||_infinity, and the conclusion is F=constant. The last mildness
step making that constant zero in (5.3) is proved in this note.

[S5] Pineau and Vicol, On rotated backwards self-similar solutions of the
incompressible 3D Navier-Stokes equations, arXiv:2607.09619v1 (2026-07-10).
https://arxiv.org/html/2607.09619v1
Theorems 1.4, 1.6 and the Type-I definition (1.10) were inspected for scope;
Sections 4--5 were examined for a possible weighted Bernoulli closure.
No theorem from this source is needed in the proved chain. Its spatial
hypotheses cannot be supplied by the purely temporal bound (3.2).

Repository inputs: refreshed main, current PLAN/proof dossier, AGENTS and
canonical graph interfaces, the two preceding one-slice/local-return notes,
and the terminal-reset, intrinsic-record, kinetic and falsification scopes
already read in the present conversation. The latest proof and PLAN contents
were refreshed at the frozen input rather than taken from a named old head.

Author checks include the sign of T and its common domain, invertibility and
Galilean-center formulas, independence of the continuation index, local
oscillation blowup versus mere global escape, uniqueness of backward drift,
spatial commutator and shrinking periods, closedness of the scale group,
constant-versus-zero in [S4], compactness of boosts and transformed arguments,
and the exact physical error scaling. Same-session checks are not independent
review. Repository structural validation is reported separately; no test or
schema check certifies the PDE proof.
