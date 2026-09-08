# Every invariant decomposable convex Fourier cone is linear

Date: 2026-09-08. Frozen input main:
`e48fe621739c884ae8fc1ce882c3c8ba0c689c97`.
Status: AUTHOR PROOF; independent mathematical audit PENDING.
Scope: original unforced R3 Navier--Stokes at each fixed nu>0. A scoped
invariant-set obstruction, not a regularity proof or cascade construction.

## 0. Terminal gate and the exact improvement

The missing positive producer is still the every-upper-time, M-uniform
estimate, for one fixed finite q>3,

    integral_0^t Pi_q,M <= nu integral_0^t D_q,M + C(d,nu,H,N0,q).

With the exact RF identity and the Schwartz initial shell bound this gives
RF-q; RF-LQ-SYNTHESIS, RF-LOCAL-ID and Lorentz Fatou give a finite uniform
L^{3,q} bound on the classical branch; RF-LQ-CONTINUATION, LOCAL and ENERGY
then give NS-R3 including normalized pressure. This note supplies NO upper
bound on Pi, event extraction, turnover cost or link starting that chain.

Its consumer is instead a construction-class exclusion. The preceding
`2026-09-08-fourier-cone-obstruction.md` excludes ACUTE decomposable invariant
cones. Here acuteness is removed completely, and even pointedness is not
assumed: every such closed convex cone must be a real LINEAR subspace.
Therefore independently selectable pointwise Fourier inequalities cannot
provide a genuine one-sided invariant cone. Widening the polarization cone
beyond ninety degrees or adding linear directions does not repair that method.

This does not exclude non-decomposable correlated cones, nonconvex traps,
non-conical invariant sets, or full-state recurrence. In particular it does
not exclude the known nonzero linear odd sector. No independent review or
priority is claimed. The finite-dimensional measurable-cone argument below
is proved explicitly, rather than imported as an uninspected interface.

## 1. Statement and conventions

Let H=L2_sigma(R3;R3), with its real Hilbert inner product, and let
H_infty be the intersection of all integer H^m_sigma. Use the unitary angular
Fourier transform, with kappa=(2*pi)^(-3/2), and put

    Q(u)=-P div(u tensor u),
    B(v,w)=Q(v+w)-Q(v)-Q(w).

Thus B is symmetric bilinear, with no factor 1/2. The original equation is
u_t=nu Delta u+Q(u), and <u,Q(u)>=0 on H_infty. The pressure is always

    p_hat(xi)=-sum_(i,j) xi_i xi_j/|xi|^2 Fourier(u_i u_j)(xi), xi!=0.

Let P_E denote the L2 Fourier restriction to a measurable symmetric set
E=-E. A closed convex cone K in H is *decomposable* if P_E K is contained
in K for every such E. In particular it permits arbitrary deletion of
Fourier pieces, not just dyadic shells or a prescribed carrier list.
Its lineality L=K intersect (-K) is a closed real linear subspace.

**Theorem 1.** Fix nu>0. Suppose K is closed, convex, conic and decomposable.
Suppose every datum in K intersect H_infty has its local ORIGINAL NS solution
in K for some positive interval (allowed to depend on the datum). Then

    K=L; in particular K is a real linear subspace.       (1.1)

Consequently a pointed K, meaning K intersect (-K)={0}, is {0}.
Neither acuteness, a uniform angular aperture nor a uniform local lifespan
is assumed. This does not assert that every decomposable linear subspace
is invariant; invariance remains a necessary hypothesis.

The local invariance hypothesis is explicitly for H_infty data. Sharp
restrictions need not be Schwartz. A statement of invariance only for
Schwartz members of an arbitrary closed cone is not silently upgraded to
this hypothesis. The separate Schwartz packet-face obstruction in the
predecessor note remains valid without this upgrade.

## 2. The Fourier-hole implication, without acuteness

We reproduce the part of the predecessor proof needed here to make the
new argument's hypotheses explicit:

    u in K intersect H_infty  implies  Q(u) in K.         (2.1)

Fix R and partition B_R into finitely many symmetric measurable sets E_j
of volume at most eta. This is possible on the atomless space R3 by
partitioning a half-ball and pairing its cells with their negatives.
Put r_j=P_Ej u and v_j=u-r_j. Decomposability puts v_j in K intersect
H_infty. Its local original solution U_j has zero initial Fourier part in
E_j, so differentiability into L2 gives

    P_Ej U_j(t)/t -> P_Ej Q(v_j) in L2 as t decreases to 0.

The viscous term is zero in that hole. Closure and conicity put each limit
in K. Their finite sum g_eta belongs to K. The exact divergence-form
convolution, not a generic energy-cancelling bilinear map, gives

    |Fourier(Q(u)-Q(v_j))(xi)|
         <= 2 kappa R ||u||2 ||r_j||2,  |xi|<=R.

Indeed u tensor u-v_j tensor v_j=r_j tensor u+v_j tensor r_j,
||v_j||2<=||u||2, and the convolution is bounded by Cauchy--Schwarz.
Disjointness of the E_j then gives

    ||P_BR Q(u)-g_eta||2^2
         <= 4 kappa^2 R^2 eta ||u||2^4.                 (2.2)

First eta tends to zero, then R tends to infinity, proving (2.1).
No common lifespan over infinitely many holes and no assertion that the
restricted datum follows a projected dynamics is used.

## 3. Splitting off all reversible directions

Every P_E preserves L. Since it is self-adjoint, it also preserves L-perp;
the orthogonal projection onto L commutes with every P_E. Set

    C=K intersect L-perp.

Then C is closed, convex, pointed and decomposable, and

    K=L+C,  L perpendicular to C.                        (3.1)

For k in K, subtract its orthogonal projection onto L: the negative of
that projection is in K, so the remainder is in C. This proves (3.1).

For a bounded ball B_R write H_R=P_BR H, K_R=K intersect H_R,
L_R=L intersect H_R, C_R=C intersect H_R, and Q_R=P_BR Q. One also has
K_R=P_BR K, with lineality L_R and pointed part C_R. All elements of H_R
are in H_infty. Equation (2.1) gives

    Q_R(K_R) subset K_R,    <v,Q_R(v)>=0 for v in H_R.     (3.2)

The energy identity is unchanged since the test is already in H_R.
The map Q_R is a continuous quadratic map H_R to H_R: Bernstein and
divergence form give a bound C R^(5/2)||v||2||w||2 for its bilinear
polarization. It is used for algebraic testing only, never as a replacement
trajectory or an assumption that the original dynamics is bandlimited.

## 4. A strictly dual-positive section exists without a uniform aperture

Identify H_R on a measurable half-ball Omega_R with real finite-dimensional
Fourier fibers: C^3 as R^6, restricted by xi dot a=0; conjugate values fill
the other half. Real Fourier inner products become twice the integrals of
Re(conjugate(a) dot b). The zero-frequency/null boundary is irrelevant.

**Lemma 2.** Any closed convex pointed decomposable cone C_R has a
measurable fiber representation F(xi), consisting almost everywhere of
closed pointed finite-dimensional cones, and contains a section w with
|w_hat|<=1 such that, on every nonzero fiber,

    Re(conjugate(w_hat(xi)) dot z) >= delta(xi)|z|
    for every z in F(xi), with delta(xi)>0.               (4.1)

Set w_hat=0 and delta=0 on zero fibers. There is no positive uniform lower
bound on delta. The bounded Fourier section lies in H_R and hence H_infty.

**Proof, including the measurable steps.** Choose a countable dense subset
of C_R and enumerate all its finite nonnegative rational combinations as
g_j, including zero. At each xi let F(xi) be the closure of their Fourier
values. Rational conic operations show that F is a closed convex cone.
Its distances are measurable, being infima of countably many measurable
functions. Every element of C_R has Fourier value in F almost everywhere,
by taking an almost-everywhere convergent subsequence of an L2 approximation.

Conversely any L2 section f with f_hat(xi) in F(xi) belongs to C_R.
For each n choose the first j with |g_j,hat-f_hat|<1/n, measurably in xi.
The resulting countable splice is an L2 section, bounded in magnitude by
|f_hat|+1/n on the finite-measure half-ball. Its finite partial splices,
with zero on the remainder, belong to C_R by decomposability and addition.
Dominated convergence and closure put the countable splice in C_R; letting
n grow proves the assertion. Real symmetry is restored for each splice.

We justify that F is pointed almost everywhere, rather than inferring it
without a selection argument. For a fixed rational vector a in R^6, the
unique minimizer of

    |z-a|^2 + m dist(z,F)^2 + m dist(-z,F)^2              (4.2)

is measurable in xi. To see this, evaluate on rational z, take the first
rational near-minimizer, and use strong convexity and continuity to pass
to the unique minimum. As m tends to infinity these minimizers converge
to the orthogonal projection of a onto F intersect (-F): boundedness
follows by comparison with z=0, both distances tend to zero, and the
unique nearest-point property identifies every convergent subsequence.
If fiber lineality were nonzero on positive measure, a countable choice of
a and a positive threshold would give a nonzero bounded measurable section
in F intersect (-F). By the representation just proved both signs of this
section belong to C_R, contradicting pointedness. Thus F is pointed a.e.

For each nonzero pointed fiber form

    D(xi)=conv(F(xi) intersect {|z|=1}).

This is compact in the finite-dimensional fiber (Caratheodory's elementary
finite-dimensional convex-hull fact suffices), and it excludes zero. A
convex combination of nonzero cone directions summing to zero would put
a nonzero vector and its negative in F. Let w_hat be the unique minimum-norm
point of D. It belongs to F, has norm at most one and has positive norm.
The minimizing inequality along the segment from w_hat to any unit z in F
is

    Re(conjugate(w_hat) dot z) >= |w_hat|^2.

Take delta=|w_hat|^2 to obtain (4.1).

For explicit measurability, normalize the nonzero g_j,hat. On a nonzero
fiber replace zero entries by the first nonzero normalized entry. These
form a countable dense set of its unit cone directions. Rational convex
combinations are dense in D. Their squared norms have a measurable infimum;
choose the first combination within 1/n of that infimum. The minimizing
inequality bounds its squared distance from w_hat by its excess squared
norm, so these choices converge measurably to w_hat. The fiber representation
then puts the bounded section w in C_R. This proves the lemma. QED.

## 5. Strict dual positivity kills the nonlinear output, including lineality

Let v belong to C_R and satisfy a strict inequality of the form (4.1) on
every nonzero fiber. Let pi_R be the projection onto L_R-perp in H_R.
By (3.2), pi_R Q_R(v) belongs to C_R. Energy and v perpendicular to L_R give

    0=<v,Q_R(v)>=<v,pi_R Q_R(v)>.

The integrand on the right is nonnegative and pointwise strictly positive
where pi_R Q_R(v) is nonzero, by (4.1). Hence pi_R Q_R(v)=0, or
z=Q_R(v) belongs to L_R. It is important not to stop here: a lineality output
could still be nonzero and energy-orthogonal to v.

Since both signs of z belong to K_R, v+t z belongs to K_R for EVERY real t.
Expand the pointed projection of its quadratic output:

    pi_R Q_R(v+t z)=t pi_R B_R(v,z)+t^2 pi_R Q_R(z) in C_R,
    B_R=P_BR B.

Divide by t>0 and let t decrease to zero; then repeat with t<0, dividing
by -t. Closure puts both signs of pi_R B_R(v,z) in the pointed cone C_R.
Thus B_R(v,z) belongs to L_R. Now extract the linear coefficient in t of

    <v+t z,Q_R(v+t z)>=0.

It says

    ||z||2^2 + <v,B_R(v,z)>=0.

The second term is zero by orthogonality. Therefore z=0. We have proved

    Q_R(v)=0 for every such strictly dual-positive v.    (5.1)

This two-sided lineality test is what excludes the proposed repair by
adding arbitrary unconstrained linear polarization directions.

## 6. Exhaustion extends vanishing to the entire pointed component

Take any f in C_R and use the section w and margin delta from Lemma 2.
Let E_n be the symmetric measurable set on nonzero fibers where

    delta>=1/n,   |f_hat|<=n,

and put f_n=P_En f. These sets exhaust every nonzero fiber up to null sets,
so f_n tends to f in L2. For 0<=epsilon<1/(2n^2), conicity gives
w+epsilon f_n in C_R and, for every z in its fiber,

    Re(conjugate(w_hat+epsilon f_n,hat) dot z)
           >= (delta-epsilon |f_n,hat|)|z| >0

whenever z is nonzero. Outside E_n the original strict margin remains.
Equation (5.1) therefore applies throughout this epsilon interval:

    Q_R(w)+epsilon B_R(w,f_n)+epsilon^2 Q_R(f_n)=0.

A quadratic polynomial vanishing on an interval has all coefficients zero,
so Q_R(f_n)=0. Continuity on H_R and L2 convergence imply

    Q_R(f)=0 for EVERY f in C_R.                         (6.1)

No uniform interior of the cone, uniform positive delta or bound on the
future strain was needed. The spectral exhaustion is essential: a fixed
positive epsilon need not work simultaneously over all fibers.

## 7. Original Leray rigidity finishes the proof

Let f be in C with Fourier support in B_r. Apply (6.1) with R=2r. Since
Q(f) has Fourier support in B_(2r), it follows that Q(f)=0. The same holds
for every symmetric Fourier restriction of f, since it too belongs to C
and is bandlimited. The following elementary rigidity, proved in Section 3
of the predecessor note, then gives f=0:

    Q(P_E f)=0 for every symmetric E  implies f=0 on R3. (7.1)

Here are the decisive details. At two nonparallel nonzero carrier vectors
p,q and nonzero complex polarizations a perpendicular to p, b perpendicular
to q, let

    A=P_(p+q)[(q dot a)b+(p dot b)a].

If |p|!=|q|, A=0 forces both a and b to be complex multiples of p cross q.
Choose coordinates p=P e1, q=Q(cos(theta)e1+sin(theta)e2), and write

    a=alpha e2+zeta e3,
    b=beta(-sin(theta)e1+cos(theta)e2)+omega e3.

The in-plane and normal coefficients of A are respectively

    sin(theta)(Q^2-P^2)alpha beta/|p+q|,
    sin(theta)(Q alpha omega-P beta zeta).

The first forces alpha beta=0; the second and nonzero polarizations force
alpha=beta=0. This calculation is also the unequal-length case of the
inspected Kishimoto--Yoneda classification; see Section 9.

To apply it to (7.1), restrict f to disjoint balls around +/-p and +/-q
at Lebesgue points of f_hat. Polarize (7.1), integrate the zero cross source
over B_(2eta)(p+q), and divide by |B_eta|^2. Only the positive p,q pairing
contributes there for sufficiently small eta. Continuity of the Leray
symbol away from zero and Lebesgue differentiation give A=0 at almost
every such pair. If f were nonzero, its Fourier nonzero set would have
positive three-dimensional measure. Fubini permits selecting three linearly
independent points p,q,r with |p| different from both |q| and |r|, for which
both pair equations hold. Then f_hat(p) belongs to the two distinct complex
lines generated by p cross q and p cross r, whose intersection is zero.
This contradicts f_hat(p)!=0 and proves (7.1).

Thus every bandlimited element of C is zero. Spectral truncation and closure
give C={0}. The orthogonal decomposition (3.1) now gives K=L, completing
Theorem 1. QED.

## 8. Sharpness, falsification and limitations

The nonzero closed real linear sector

    O={u in H : u(-x)=-u(x)}

is decomposable and invariant under original NS. Its Fourier coefficients
are purely imaginary real vectors, and uniqueness preserves the central
odd symmetry. The new theorem is compatible with this exact counterexample
to the stronger assertion K={0} without pointedness. It neither forces Q
itself to vanish on a permitted linear sector nor makes its trajectories
regular for arbitrary amplitude.

Likewise a finite-dimensional cone with lineality can have a nonzero
energy-cancelling quadratic vector field mapping the cone into itself:
for K={(x,y,z):z>=0}, Q=(yz,-xz,0). The pointed component is the z-axis
and Q vanishes there; the full cone's Q is nonzero. The final original-R3
Fourier rigidity, not convex geometry alone, rules out its analogue here.

A correlated NS-like triad x'=-yz, y'=-xz, z'=2xy preserves x=y>=0,z>=0.
It is NOT stable under independent coordinate deletion. Its quadratic
vector field need not itself lie in that cone: local invariance gives
only tangency, and the Fourier-hole proof is precisely the missing step.
The packet version also has nonzero side outputs. This leaves genuinely
correlated full-state regenerative cells, with inherited exterior, alive.

A bounded non-conical invariant set is outside the theorem; an L2 ball is
an immediate example. An invariant set merely at selected return times,
a cone allowed to change with the state/time, or invariance only under a
fixed family of coarse shell projections also need not satisfy the hypotheses.
No angular/exterior dissipation, turn duration or count of regenerative
events follows from (1.1). The dual margin may approach zero without any
uniform rate; it has not produced a quantitative critical budget.

## 9. Primary-source inspection and exact checking scope

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier--Stokes equation*, arXiv:1402.0290v3 (2015 version),
https://arxiv.org/html/1402.0290v3 . Inspected the original-symbol formulas,
the averaged-model reduction and the pump gate; (1.3)--(1.4) give the original trilinear symbol, and (5.3) gives the assigned
pump x'=-alpha xy, y'=alpha x^2. His averaged equation shares energy
cancellation but not the original atomless convolution-hole estimate and
Leray pair constraints used together here. A packet-amplitude cone is not
silently assumed decomposable under arbitrary Fourier holes. No conclusion
about his invariant sets follows merely by replacing an operator name.

[KY] N. Kishimoto and T. Yoneda, *Characterization of three-dimensional
Euler flows supported on finitely many Fourier modes*, arXiv:2110.08039v1,
https://arxiv.org/pdf/2110.08039 . Inspected Theorem 1.4, Lemma 2.1 and
Proposition 2.2 with its proof (printed pp6, 8--9). The unequal-length
pair formula in Section 7 is prior art, rederived here. Their finite-mode
classification is not an R3 finite-energy result imported to replace (7.1).

`research/check_convex_cone_linearity.py` checks the quadratic energy
coefficient identities, exact nonacute cone sections and margins, exhaustion
powers, the two-sided pointed/lineality algebra, and the surviving linear
and correlated examples. It does not certify the measurable representation,
Lebesgue-point limit, local PDE theory, arbitrary cones, or independent
mathematical correctness. Those remain paper-proof obligations as provided
above, awaiting independent review. This note adds no canonical graph node.

The single dominant terminal task remains a CORRELATED full-state return:
construct a scale-repeating concentration-producing original-NS cell on its
shrinking critical clock, with the mandatory exterior and summable errors;
or prove an input-summable original-specific cost and complete extraction
of those events into the every-upper-time signed RF-q producer. The theorem
here excludes independent convex one-sided traps, not that remaining task.
