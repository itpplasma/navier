# Nonconcentrating local returns cannot occur in marked ancient NS

Date: 2026-09-07.
Frozen repository input: `31b6f607ce9d268bf670d9413ce58e4612c3a29e`.
Status: complete author derivation from the scoped analytic inputs below;
independent mathematical audit and prior-art assessment pending.
Result category: B, a further scoped singularity reduction. NS-R3 is NOT
PROVED. No canonical graph promotion, formal proof, or novelty claim.

## 1. Terminal gate and what is actually proved

Keep the original unforced whole-space Navier--Stokes equation, one fixed
nu>0, and the maximal classical mild branch of any solenoidal Schwartz datum.
The existing fast-record extraction produces an ancient unit-viscosity MILD
solution U with

    |U(y,s)|<=1 for s<=0,       |U(0,0)|=1,
    |U(y,s)|<=1/2 for s<=-A,                              (1.1)

for a finite A. These bounds do not give global L2/L3 integrability, decay,
or a compact orbit modulo scaling. The slow-record alternative is separate.

The candidate rigidity proved here is that such a U cannot return locally
at a later slice to a translated/rotated/Galilean transform of an earlier
slice at the same or an EXPANDED spatial scale. Precisely, for s0<s1<=0,
0<lambda<=1, Q in SO(3), and a,b in R3, the relation

    U(y,s1)=lambda Q U(lambda Q^T(y-a),s0)+b               (1.2)

cannot hold on any nonempty open ball. Lambda is simultaneously the velocity
factor and the inverse spatial-length factor; lambda<1 expands rather than
concentrates the earlier profile. This convention matters.

Positive leverage: the transformation is an EXACT symmetry of the unforced
NS dynamics when its time dependence is correctly supplied. Spatial
analyticity turns the local slice relation into a global one; bounded mild
uniqueness and time analyticity extend it to the whole ancient past. Iteration
then either contracts the velocity to one constant (lambda<1) or returns a
peak to arbitrarily early times with vanishing net boost (lambda=1). Both
contradict (1.1). The boost/rotation interaction is proved, not ignored.

The complete contradiction chain is

    finite Tstar + a fast-record sequence with vanishing local return error
      -> a marked ancient mild U satisfying (1.2)
      -> a global ancient symmetry and its iterates
      -> contradiction with the two amplitude marks.              (1.3)

Compactness supplies the first arrow only AFTER the explicit fast-record
and local-return assumptions. The symmetry-iteration theorem supplies the
new rigidity, rather than compactness alone. Section 5 proves a uniform
finite-history theorem and Section 6 transfers it to actual NS records.

This removes a class of fully three-dimensional recurrent fast concentration;
it is not a theorem that every singularity must recur. In particular it does
NOT remove scale-contracting returns with lambda>1, nonreturning fast profiles,
or slow records. No input-only critical bound is obtained or renamed here.

## 2. Analytic inputs, exact class, and terminal time zero

A bounded ancient mild solution satisfies the heat/Oseen integral identity
on every finite subinterval of R3 x (-infinity,0]. No spatially linear harmonic
pressure may be chosen to generate an arbitrary time-dependent constant flow.

We use three established inputs, already relevant to the preceding record
note, and rechecked here in their primary texts:

* KNSS [S1], Section 4 and Lemma 6.1: bounded mild local existence/uniqueness,
  interior derivative bounds, and compactness on expanding past intervals.
* Grujic [S2], Theorem 3.1: bounded-data local mild solutions are spatially
  analytic at positive times. Restarting before each ancient slice makes
  that slice real analytic on all R3. Only the L-infinity analyticity
  theorem is used, not the paper's additional sparseness criterion.
* Dong--Zhang [S3], Theorem 3.1: a bounded whole-space mild NS solution is
  time analytic at interior times, with no decay or L3 hypothesis.

All three apply after time translation and, where necessary, parabolic
scaling. For a uniform velocity bound 1, local mild existence extends each
terminal slice across zero for a universal positive time, with velocity
bound 2. This makes zero an interior time for uniqueness, analyticity, and
compact convergence retaining the peak. No global existence is assumed.

For expanding histories, interior regularity and a diagonal subsequence give
local uniform convergence, including time zero after that extension. The
limit is mild: truncate the integrable spatial tails of the heat and Oseen
kernels and the integrable near-endpoint time factor (t-s)^(-1/2), pass to
local convergence on the retained compact set, and then remove the truncations.
Uniform global velocity bounds control the discarded terms. Thus no inherited
pressure tail, energy bound, or harmonic-pressure degree of freedom is added.

## 3. The exact transformed solution and backward propagation

**Lemma 1 (local slice relation propagates along the NS symmetry).**
Let U be bounded ancient mild, let s0<s1<=0, 0<lambda<=1, Q in SO(3), and
a,b in R3. Suppose (1.2) holds on a nonempty open ball. Define

    phi(s)=s0+lambda^2(s-s1),
    z(y,s)=lambda Q^T[y-a-b(s-s1)],
    V(y,s)=lambda Q U(z(y,s),phi(s))+b.                  (3.1)

Then U=V on R3 x (-infinity,0].

**Proof.** First, V is a mild solution of the SAME unit-viscosity unforced
NS equation on its domain. The constant boost has to be accompanied by the
term -b(s-s1) in the moving argument; simply adding b at all times would
not be a symmetry. With transformed pressure

    P_V(y,s)=lambda^2 P_U(z(y,s),phi(s)),

the time derivative of V contains

    lambda^3 Q partial_s U
       -lambda^2 Q[(Q^T b) dot grad U],

and its convection contains

    lambda^3 Q[(U dot grad)U]
       +lambda^2 Q[(Q^T b) dot grad U].

The boost terms cancel. The Laplacian and pressure gradient both carry
lambda^3 Q; divergence remains zero. These are the original equations,
not rotating-frame equations with a Coriolis force.

For completeness, mildness is preserved as well as the differential equation.
Rotation, fixed translation, and parabolic scaling transform the heat/Oseen
identity by changes of variables. A Galilean translation transforms its heat
semigroup to the constant-drift semigroup exp((s-r)(Delta-b dot grad)).
The constant-drift Duhamel identity is equivalent to the ordinary heat
Duhamel identity with the extra term -b dot grad of the shifted velocity.
In the nonlinear equation that extra term is exactly the cross term in
P div[(f+b) tensor (f+b)], since div f=0. This proves the mild identity
for V, rather than inferring mildness from an arbitrary bounded weak solution.
All kernels and the bounded smooth fields on a compact time interval justify
these changes; constant transport commutes with the convolution operators.

Since s0<s1<=0 and lambda<=1,

    phi(0)=s0-lambda^2 s1 < (1-lambda^2)s1 <=0.           (3.2)

Thus V is defined and bounded on the entire ancient domain through zero;
indeed |V|<=lambda sup|U|+|b| there. The local extension of U supplies a
common open interval a little beyond zero for U and V. Their bound need
not be the same; both are finite, which is sufficient for the analytic
and uniqueness inputs.

Spatial analyticity turns (1.2) into equality of U(.,s1) and V(.,s1) on
all R3. Bounded mild uniqueness gives U=V on a nonempty forward time interval.
For each fixed y, apply time analyticity to U(y,.) and V(y,.) AS TWO MILD
SOLUTIONS. Their difference vanishes on an interval, so the real-analytic
identity theorem makes it vanish on the connected common ancient domain.

This last argument does NOT assert that composing separately space-analytic
and time-analytic U with a moving argument is automatically analytic. The
transformed field V has its own justified time analyticity as an NS solution.
Nor does forward uniqueness alone supply the backward step. QED.

## 4. The rigidity proof, including arbitrary Galilean boosts

**Theorem 2 (no nonconcentrating local return).** No solution satisfying
(1.1) can satisfy (1.2) on a nonempty open ball for any s0<s1<=0,
0<lambda<=1, Q in SO(3), and finite a,b. No bound or smallness assumption
on a or b is imposed in this exact theorem.

**Proof.** Lemma 1 gives the global identity U=V. Starting with any (y,s),
s<=0, define

    s_(j+1)=phi(s_j),
    y_(j+1)=lambda Q^T[y_j-a-b(s_j-s1)],
    s_0^iter=s,  y_0^iter=y.

Here the superscript distinguishes the starting iterate from the fixed
slice named s0. By (3.2) every iterate time remains in the ancient domain.
Repeated substitution gives, for k>=1,

    U(y,s)=(lambda Q)^k U(y_k,s_k)+B_k,
    B_k=sum_(j=0)^(k-1) (lambda Q)^j b.                 (4.1)

Spatial iterates may go to infinity. This is legitimate because both
amplitude marks in (1.1) are GLOBAL in space, not merely local bounds.

### Case 0<lambda<1

Orthogonality gives |(lambda Q)^k U(y_k,s_k)|<=lambda^k. The geometric sum
converges to

    c=(I-lambda Q)^(-1)b.

Letting k tend to infinity in (4.1) proves U(y,s)=c for every ancient point.
The matrix is invertible since its eigenvalues have modulus bounded below
by 1-lambda>0. The two marks require both |c|<=1/2 and |c|=1, a contradiction.
In fact this case proves constancy of ANY globally bounded ancient mild
solution having the stated local return, without the marks.

### Case lambda=1

Now s_k=s-k tau with tau=s1-s0>0, and

    B_k=sum_(j=0)^(k-1) Q^j b.

Taking norms in (4.1) and using |U|<=1 gives |B_k|<=2 for every k. Let P
be the orthogonal projection onto Fix(Q). Since P Q^j=P,

    P B_k=k P b.

Boundedness therefore gives P b=0. For an orthogonal matrix,
Ran(I-Q)=Fix(Q)^perp: the orthogonal complement of the range is
ker(I-Q^T)=Fix(Q). Thus b=(I-Q)c for some finite c, and

    B_k=(I-Q^k)c.                                        (4.2)

There are integers k_j tending to infinity with Q^(k_j)->I. One elementary
proof uses the rotation angle theta: when theta/(2pi) is rational, take
multiples of its period; otherwise the pigeonhole approximation to k theta
modulo 2pi supplies a sequence tending to zero modulo 2pi. Consequently
B_(k_j)->0. This also covers Q=I, in which case boundedness already gave b=0.

For k_j large enough, s-k_j tau<=-A. By (4.1), orthogonality, and the earlier
half-amplitude bound,

    |U(y,s)| <= 1/2 + |B_(k_j)|.

Let j tend to infinity and then use (y,s)=(0,0). This gives 1<=1/2.
The boost is not assumed absent, and the rotation is not assumed to have
finite order. QED.

The limiting case lambda=0, needed only in compactness below, is also
impossible: its slice relation is U(y,s1)=b on a ball. Spatial analyticity
makes that slice constant globally, and uniqueness plus time analyticity
identify the whole ancient solution with the constant mild solution b.
The marks again contradict each other. Lambda=0 is not called an NS scaling.

## 5. A uniform gap for long finite histories

Fix A>0, R>0, B>=delta>0, and D>=0. For a bounded history W define

    E(W;lambda,Q,a,b,s0,s1)
      = integral_(B_R) |W(y,s1)
          -lambda Q W(lambda Q^T(y-a),s0)-b|^2 dy.       (5.1)

The allowed parameters are

    -B<=s0<s1<=0,  s1-s0>=delta,
    0<lambda<=1,  Q in SO(3),  |a|<=D,  b in R3.        (5.2)

This is a geometric local-return error, not a new controlled critical norm.

**Theorem 3 (finite-history separation).** There exist finite
L_*=L_*(A,R,B,delta,D)>max(A,B) and eta=eta(A,R,B,delta,D)>0 such that every
unit-viscosity mild history on [-L,0], L>=L_*, with

    |W|<=1,   |W(0,0)|=1,   |W|<=1/2 on [-L,-A],        (5.3)

satisfies E>=eta for EVERY parameter choice (5.2). The constants are
qualitative; no numerical rate or effective formula is claimed.

**Proof.** If this were false, choose L_j>=j+max(A,B) and histories W_j
satisfying (5.3), with allowed parameters and E_j<1/j. The boosts are
automatically bounded, despite their unrestricted parameter range. With
v_R=|B_R|, the L2 triangle inequality gives

    |b_j| sqrt(v_R) <= 2 sqrt(v_R)+sqrt(E_j).            (5.4)

All other parameters lie in compact sets after adjoining lambda=0.
Take a subsequence on which they converge. In particular the two limiting
times remain separated by at least delta.

Extend W_j across zero by bounded mild local theory. The compactness package
in Section 2 gives a locally uniform ancient mild limit U retaining all
three marks. The source spatial arguments lambda_j Q_j^T(y-a_j) lie in
B_(R+D), and both times lie in [-B,0]. Local uniform convergence and the
uniform continuity supplied by compactness therefore pass (5.1) to its
limit. If lambda_*>0, the limit satisfies (1.2) on B_R, contradicting
Theorem 2. If lambda_*=0, the boundedness of W_j makes the multiplied source
term tend uniformly to zero, leaving the impossible constant-slice relation.

A vanishing integral gives pointwise equality on the ball because the limit
fields are continuous. This proves the theorem. If the marked ancient class
is empty, the same argument shows that sufficiently long finite histories
are empty; the theorem remains correctly vacuous in that case. QED.

The positive lower time separation delta and bounded normalized displacement
D are essential to this assertion of UNIFORMITY. They are not restrictions
on the exact theorem. The proof supplies no uniform bound as delta->0,
B->infinity, R->0, or D->infinity.

## 6. Actual fixed-viscosity singularity consequence

Use the original first-record construction, with M0>||u0||_infinity,
Mn=2^n M0, first hitting times tn, and any point xn with |u(xn,tn)|=Mn:

    ell_n=Mn^2(tn-t_(n-1))/nu,
    U_n(y,s)=Mn^(-1)u(xn+(nu/Mn)y,tn+(nu/Mn^2)s),
    L_n=Mn^2 tn/nu.                                      (6.1)

The equation for U_n has viscosity one. First hitting gives

    |U_n|<=1 on [-L_n,0],  |U_n(0,0)|=1,
    |U_n|<=1/2 on [-L_n,-ell_n].                          (6.2)

For clarity, the existing universal-history calculation is repeated. The
heat contraction and Oseen bilinear estimate on [t_(n-1),tn] give

    Mn/2 <= C_K nu^(-1/2) Mn^2 sqrt(tn-t_(n-1)).

Hence ell_n>=c_rec=(2C_K)^(-2)>0 and

    L_n >= c_rec sum_(j=1)^n 4^(n-j)
         = (c_rec/3)(4^n-1).                             (6.3)

This is input-independent record information, not an assumed critical bound.

**Theorem 4 (no asymptotically nonconcentrating local return at fast records).**
For every choice of A,R,B,delta,D as in Section 5, there are N<infinity and
eta>0, independent of u0,nu,M0,n and the maximizing point, such that every
record with n>=N and ell_n<=A satisfies

    inf_(parameters (5.2)) E(U_n;parameters) >= eta.      (6.4)

**Proof.** Choose N so that (c_rec/3)(4^N-1)>=L_* from Theorem 3. Equations
(6.2)-(6.3) give the long bounded history. Because ell_n<=A, s<=-A implies
s<=-ell_n and therefore supplies the half mark in (5.3). Apply Theorem 3.
This works for every maximizing point and every allowed datum/viscosity. QED.

The physical scaling can be checked without convention-dependent shorthand.
Put t_i=tn+nu s_i/Mn^2 for i=0,1, and define

    x_earlier(x)=xn+lambda Q^T[x-xn-(nu/Mn)a].

Then

    E(U_n;parameters)
      = (Mn/nu^3) integral_(B_(R nu/Mn)(xn))
          |u(x,t_1)-lambda Q u(x_earlier(x),t_0)-Mn b|^2 dx.
                                                               (6.5)

The factor follows from dy=(Mn/nu)^3 dx and the velocity factor Mn^(-1).
It is dimensionless. In particular no different parent viscosity, force,
periodic boundary condition, or alternative equation has entered the result.

Thus a finite-time singularity cannot admit n_j->infinity with ell_(n_j)<=A
and a return error (6.5) tending to zero under the stated controlled
normalized times and displacements. Parameters may change with j, including
the direction of rotation, the boost, and lambda tending to zero or one.
No global small return error is required: one fixed normalized ball suffices.

## 7. Stress tests and the exact limit of the argument

**Constants and parasitic flows.** Constant mild solutions permit local
returns and are not classified as impossible. They fail the half-to-one
marks. Time-dependent spatial constants allowed by an arbitrary linear
harmonic pressure are not bounded mild solutions in this argument.

**Local smooth data, small time gaps, and distant packets.** Smooth localized
NS data can have very small local change over short intervals. This does
not violate (6.4), whose normalized separation is bounded below and whose
whole bounded marked history grows with the record number. Nearby-in-time
returns as delta->0 are not excluded. Nor is a uniform result asserted for
translations escaping to infinity: source and target packets could then
have different local limits. The |a|<=D restriction is explicit.

**Galilean covariance.** A nonzero constant velocity difference is not
illegitimately dropped. Formula (3.1) uses the necessary moving argument;
(4.1)-(4.2) prove the iterated boost is harmless in the exact contradiction;
(5.4) proves compactness of boosts in the approximate contradiction. No
small-strain estimate or operator norm of a stochastic deformation is used.

**Helical and single-channel configurations.** A nonconstant Beltrami heat
mode at fixed positive viscosity becomes unbounded backwards, so it cannot
supply the bounded marked ancient history. Finite-time helical solutions
and the recorded instantaneous single-channel interactions remain valid
in their original scopes. This theorem does not assert instantaneous
branching or a sign for pressure or vortex stretching. Its conclusion can
apply to a fully three-dimensional local return; no lost spatial direction
is a premise.

**The critical boundary lambda>1.** This is NOT silently included. At that
factor, (4.1) has a growing rather than contracting coefficient. Its time map
has fixed point

    s_c=(lambda^2 s1-s0)/(lambda^2-1)>s1.                 (7.1)

This point can lie strictly AFTER zero, outside the available bounded ancient
history. For example s1=0 gives s_c=-s0/(lambda^2-1)>0. Iterating towards
that future point is not licensed by an ancient solution defined through
zero. Iterating backwards instead multiplies the old velocity by lambda^k
and does not contradict the earlier half bound. This is the precise gap
for concentrating/self-similar returns, not an estimate claimed to fail
for an unrelated equation. No actual NS counterexample is asserted.

**Energy and kinetic scopes.** Neither a critical norm nor finite global
energy is inherited by U. The physical viscous loss of an order-one normalized
packet is still nu^3/Mn times its normalized gradient integral, and dyadic
costs remain summable. No dissipation contradiction follows from (6.4).
The prepared Fisher/stress, entropy, Euler-shear and other repository
falsifiers keep their separate premise classes; no kinetic quantity is used
as a producer in this proof.

## 8. Remaining terminal implication, without a false completion claim

The preceding commit excluded locally planar fast-record concentration.
The present proof separately excludes nonconcentrating local returns of
fast marked concentration, including cases with all three spatial directions
active. It gives a proved necessary dynamical property with a uniform
finite-history/actual-record adapter, not a new continuation criterion.
The word 'return' always has the explicit meaning (1.2) or (5.1)-(5.2).
It does not mean arbitrary concentration-compactness or recurrence modulo
concentrating dilations.

For Tstar<infinity, either ell_n has a bounded subsequence or ell_n->infinity.
In the first case the surviving fully three-dimensional fast profiles must
also obey (6.4) for every fixed choice of its parameters. In the second case
the existing running-maximum conclusion is unchanged:

    (Tstar-t) H(t)^2/nu -> infinity,
    H(t)=sup_(0<=r<=t)||u(r)||_infinity.

There is still no theorem forcing either class into the forbidden return
configuration. In particular, the argument does not exclude genuinely
nonreturning fast evolution or lambda>1 concentrating returns, and does not
exclude slow records. Compactness of a selected set must not be used to
assume a recurrent evolving orbit; that shortcut was already retired.
An additional actual-NS theorem excluding these remaining cases is required
to conclude Tstar=infinity and invoke LOCAL/ENERGY for all NS-R3 clauses.

No complete arbitrary-data proof was obtained in this run. These remaining
arrows, rather than the known continuation suffix, prevent a terminal claim.
The new theorem is stored as author evidence pending independent audit;
NS-R3 and CRITICAL remain gaps. No manuscript or formalization is changed.

## 9. Sources, source scope, and author checks

[S1] G. Koch, N. Nadirashvili, G. Seregin and V. Sverak,
Liouville theorems for the Navier--Stokes equations and applications,
Acta Math. 203 (2009), 83--105; arXiv:0709.3599v1.
https://arxiv.org/html/0709.3599v1
Inspected the mild definition and Oseen kernels in Sections 3--4, local
bounded-data theory, Proposition 4.1 and Lemmas 4.1/6.1. These are analytic
and extraction inputs, not a general three-dimensional Liouville theorem.

[S2] Z. Grujic, A geometric measure-type regularity criterion for solutions
to the 3D Navier--Stokes equations, Nonlinearity 26 (2013), 289--296;
arXiv:1111.0217v1, Theorem 3.1.
https://arxiv.org/html/1111.0217v1
Only bounded-data spatial analyticity is used. The solenoidal-data and
mild-solution context is retained. No sparseness hypothesis or resulting
regularity criterion is imported as an arbitrary-data producer.

[S3] H. Dong and Q. S. Zhang, Time analyticity for the heat equation and
Navier--Stokes equations, J. Funct. Anal. 279 (2020), 108563;
arXiv:1907.01687v2, Theorem 3.1.
https://arxiv.org/html/1907.01687v2
Inspected the bounded whole-space MILD statement, the derivative bound,
and its proof via the Stokes representation. No spatial-integrability
assumption is added. It applies to V itself, avoiding an unsupported
joint-analyticity inference for the moving composition in (3.1).

Repository inputs are the refreshed PLAN/AGENTS/proof dossier, canonical
terminal suffix and prior evidence already read in the preceding run, and
the committed one-slice record proof re-read at the frozen revision. The
kinetic contracts, programme map and earlier scoped failures remain in force.

Author checks cover the transformed equation and its mild class; the domain
inequality (3.2); extension through zero; the affine recurrence and matrix
sum; the cases lambda->0 and lambda=1; irrational rotations; unbounded boost
parameters; local-to-global propagation; uniform compactness of source
arguments; and the physical factors in (6.3) and (6.5). These checks are not
an independent mathematical audit. No novelty assessment is asserted.
