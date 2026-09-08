# Convex Fourier-decomposable invariant cones for original NS are linear

Date: 2026-09-08.
Status: AUTHOR-PROOF CANDIDATE; independent mathematical audit PENDING.
No terminal, manuscript, formal, or independently reviewed graph status is promoted.
No priority claim. This is a scoped construction obstruction, not an NS-R3 proof.

## 0. Consumer and exact scope

The missing terminal producer remains the every-upper-time, cutoff-uniform bound

    integral_0^t Pi_(q,M) <= nu integral_0^t D_(q,M) + C(d,nu,H,N0,q)

for one fixed finite q>3. Its conditional consumer is RF-q,
RF-LQ-SYNTHESIS, RF-LOCAL-ID plus Lorentz Fatou, RF-LQ-CONTINUATION,
LOCAL and ENERGY. The result below DOES NOT supply that producer.
It excludes an independently loadable convex sign/polarization trapping
architecture. Correlated full-state sets, nonconvex cones and invariant linear
spaces remain possible. No inherited-exterior bound or turnover cost is proved.

## 1. The theorem

Let H be the real Hilbert space of real solenoidal L2 vector fields on R3,
and fix nu>0. Suppose C is a nonempty closed convex cone in H such that:

(F) P_E C is contained in C for every symmetric measurable frequency set E,
where P_E is orthogonal Fourier restriction.

(NS) For every bandlimited f in C, the local strong solution of the ORIGINAL
unforced NS equation from f stays in C on some positive interval, allowed to
depend on f. This is the full evolution with every generated mode and its
canonical pressure, not Fourier-projected dynamics.

**Theorem. C is a real linear subspace. Consequently every pointed such cone
is {0}, without an acuteness assumption.**

Bandlimited L2 fields belong to every spatial H^s and have the required local
strong solutions and L2 derivatives at zero. Hypothesis (NS) is explicitly
about these smooth finite-energy inputs. Invariance only for Schwartz elements
of C is NOT substituted: those elements need not be dense in a measurable
Fourier cone. The terminal Schwartz-data question remains unchanged.

## 2. Measurable fibers

Use the unitary angular Fourier transform, with real inner product
Re integral conjugate(a).b. Choose a measurable half of frequency space,
one representative of each pair {xi,-xi}. Its fiber

    H_xi = {a in C^3 : xi.a=0}

is real four-dimensional. Assumption (F), convexity and closure identify C
with the L2 sections of measurable closed convex cones C_xi in these fibers.
Reality gives C_(-xi)=conjugate(C_xi).

A direct representation proof avoids a regularity assumption on the fibers.
Take a countable L2-dense family in C, adjoining zero and every finite
nonnegative rational combination, and close its values pointwise. Every
member of C belongs to these pointwise cones by subsequential pointwise
convergence of L2 approximations. Conversely, for an L2 section f with values
in these cones, fix a positive L2 weight w and select measurably the first
countable-family value within w/n of f. Finite patchings belong to C by (F)
and addition. Their infinite patching is an L2 limit, dominated by |f|+w/n.
Letting n increase proves the converse by closedness.

Adjoin bounded, bounded-frequency truncations of this family using (F).
Their pointwise values remain dense outside a common null set. Distances
to the fibers are measurable. Their lineality spaces and orthogonal
projections are measurable too: lineality is the zero set of

    a -> dist(a,C_xi)+dist(-a,C_xi),

and its projection is obtained by rational-grid approximate minimization on
bounded balls followed by convergence to the unique minimizer. Measurable
orthonormal frames on coordinate patches can be used throughout.

## 3. Pair closure follows from an empty target band

For nonzero p,q,r=p+q and solenoidal a,b write

    B_(p,q)(a,b)=-i P_r[(q.a)b+(p.b)a].                 (1)

The dot products are complex bilinear. Positive Fourier normalization factors
do not affect cone membership. For almost every pair (p,q),

    B_(p,q)(C_p,C_q) is contained in C_(p+q).          (2)

To prove (2), first take a,b as values of bounded sections in the countable
family at their Lebesgue points p,q. Restrict the sections independently to
balls B_epsilon(p), B_epsilon(q) and their reality partners. Their sum
f_epsilon belongs to C and is bandlimited. For nonparallel p,q the output
center r is distinct from the input centers and every competing pair center,
except the two orders (p,q),(q,p). A sufficiently small target ball is empty
initially. The actual local solution, (F), division by positive time, and
closedness therefore give

    P_target Q(f_epsilon) in C,
    Q(f)=-P[(f.grad)f].                                (3)

Indeed P_target u(t)/t converges in L2 to P_target Q(f_epsilon). The viscous
initial derivative vanishes on the empty target, rather than being deleted
from the original equation.

After writing xi=r+epsilon z and dividing the Fourier transform in (3) by
epsilon^3, the exact convolution tends uniformly on a fixed small z-ball to

    kappa B_(p,q)(a,b) (1_B1 * 1_B1)(z).               (4)

Boundedness and the Lebesgue-point L1 errors control both input errors
uniformly; the Leray symbol is smooth near r. The convolution factor in (4)
is bounded below by a positive constant on that ball.

Membership in the limiting fiber requires care because the fibers are only
measurable. Take simultaneous Lebesgue points of dist(v,C_xi) for a countable
dense collection of fixed vectors v in C^3. The distance is 1-Lipschitz in v,
so differentiation extends to every v. Conic homogeneity, (3), and (4) show
that the average distance of B_(p,q)(a,b) to C_xi on B_(c epsilon)(r) tends to
zero. Hence B_(p,q)(a,b) belongs to C_r. Almost every pair has good p,q,r,
since addition pulls frequency-null sets back to six-dimensional null sets.
Countability and continuity extend (2) simultaneously to all fiber inputs.

For the return pairs below intersect this full-measure set with its preimages
under (p,q)->(p+q,-q) and (p,q)->(p+q,-p). These are invertible linear maps.
Thus every instance used in one triad is legitimate almost everywhere.

## 4. Separate lineality before using energy

Define fiberwise

    L_p=C_p intersect (-C_p),
    P_p=C_p intersect L_p^perp,
    C_p=L_p direct_sum P_p.                            (5)

The decomposition follows by subtracting the projection onto L_p: both signs
of that projection lie in C_p. P_p is pointed in its real span V_p.

If one input belongs to lineality, both signs of that input are permitted in
(2), while the other is fixed. Real bilinearity gives

    B_(p,q)(L_p,C_q) subset L_(p+q),                   (6)

and likewise for lineality in the second input.

For r=p+q the exact full triad energy identity is

    Re <c,B_(p,q)(a,b)>
    + Re <a,B_(r,-q)(c,conjugate(b))>
    + Re <b,B_(r,-p)(c,conjugate(a))> = 0,             (7)

where <a,b>=conjugate(a).b. Expand (1) and use p.a=q.b=r.c=0, or extract this
triad's cubic coefficient in the original energy cancellation. All Leray
projections and both reverse channels are retained.

For a in P_p, b in P_q, c in L_r, the two return outputs in (7) lie in L_p
and L_q by (6). Their pairings vanish. Thus the forward output is orthogonal
to L_r; (2) then proves

    B_(p,q)(P_p,P_q) subset P_(p+q).                  (8)

This step is why acuteness of the entire cone is unnecessary.

## 5. Pointed pair products vanish

For a closed pointed finite-dimensional cone P in V=span(P), the central cone

    A=P intersect P^*,
    P^*={v in V : <v,z> >=0 for all z in P},

spans V. For P nonzero choose w in the interior of P^*. Its projection z onto
P satisfies w-z in -P^*, hence <z,c> >= <w,c> for c in P. Therefore z is still
in the interior of P^*. Adding a sufficiently small interior vector of P
produces a point in both interiors. Their relatively open intersection spans
V. The zero-dimensional case is immediate.

For a in A_p, b in A_q, c in A_r all three terms of (7) are nonnegative by
(8) and duality. Each is consequently zero. Vary c over A_r. The forward
output belongs to P_r subset V_r and is orthogonal to the spanning set A_r,
so it vanishes. Real bilinearity and span(A_p)=V_p, span(A_q)=V_q extend this to

    B_(p,q)(a,b)=0 for every a in P_p, b in P_q,        (9)

for almost every pair. Thus the pointed part has no pair production, not just
zero total energy work.

## 6. Unequal-frequency Leray algebra excludes pointed L2 sections

For nonparallel p,q of unequal lengths choose real orthonormal coordinates

    p=P e1, q=Q(c e1+s e2), P,Q>0, s>0, c^2+s^2=1,
    a=alpha e2+beta e3,
    b=gamma(-s e1+c e2)+delta e3.

The four polarization coefficients may be complex. With
 t_r=-Q s e1+(P+Q c)e2, direct substitution into (1) gives

    t_r.B_(p,q)(a,b)=-i s alpha gamma (Q^2-P^2),
    e3.B_(p,q)(a,b)=-i s(Q alpha delta-P gamma beta).  (10)

For a,b nonzero and B=0, the first equation gives alpha gamma=0. The second
then forces alpha=gamma=0: if alpha=0, beta is nonzero, forcing gamma=0;
if gamma=0, delta is nonzero, forcing alpha=0. Both polarizations are normal
to the p,q plane. In particular q.a=0.

Suppose f is a nonzero L2 section of P_p and S is its positive-measure nonzero
support. By (9) and Fubini choose p in S with f(p) nonzero such that the pair
product vanishes for almost every q in S. The q parallel to p or with |q|=|p|
form null sets. Equation (10) therefore implies q.f(p)=0 for almost every
q in S. Those real q lie in a proper real hyperplane, or the intersection of
two hyperplanes, because at least one of Re f(p), Im f(p) is nonzero. This
contradicts the positive measure of S.

Every pointed L2 section is consequently zero. Project the countable
generating sections from Section 2 onto L_p^perp; these are measurable L2
sections of P_p and vanish. Their fiberwise density forces P_p={0} almost
everywhere. Equation (5) gives C_p=L_p almost everywhere, proving that C is
real linear. QED.

## 7. Adversarial limits and exact discriminator

The theorem uses original convolution r=p+q, its actual Leray coefficient,
atomless whole-space frequency measure, and both returns. It is not an
energy-only argument. The energy-conserving toy system

    x'=-xy, y'=x^2

preserves the non-linear-subspace cone y>=0. Its lineality x-axis feeds its
pointed direction through a square pump; ordinary equal damping also
preserves that cone. This is not an NS solution or a counterexample to
regularity. It shows exactly why energy cancellation alone is insufficient.
Independent distinct-carrier sign variation in (6), coupled to (1), excludes
this step for original NS; same-carrier original self-convection is zero by
solenoidality. Assigned averaged-operator square pumps need not respect these
conditions. No quantitative claim about the entirety of Tao's construction
is imported here.

Nonperturbative exterior modes are not deleted, but neither are they controlled
or shown to incur a summed cost. Invariant linear sectors such as central oddness
survive. Correlated full-state trapping regions survive. No finite or infinite
regenerative cascade has been constructed. No RF-q upper bound, replacement
continuation producer, turnover recurrence theorem, or independent audit follows.

The remaining dominant theorem-sized problem is still actual regenerative
turnover with the complete inherited state: either prove an input-summable
original-NS-specific cost with full event extraction and the continuation
consumer, or construct a repeatable full-vector cell with controlled inherited
exterior and summable shadowing defect on shrinking nonlinear clocks.
