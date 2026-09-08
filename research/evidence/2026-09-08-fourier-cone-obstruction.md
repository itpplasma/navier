# No independent acute Fourier cone for original whole-space NS

Date: 2026-09-08. Input main:
`77a489734e6f8c8b5db126d487ef729d55154fdb`.
Status: author proofs and exact algebra; independent mathematical audit PENDING.
No priority claim. No global regularity, blowup, regenerative turnover,
input-summable event cost, or terminal graph promotion is claimed.

## 0. Consumer gate and exact purpose

The positive terminal edge is unchanged: an input-only upper bound on
`integral_0^t (Pi_q,M - nu D_q,M)`, every upper time and uniformly in M,
feeds RF-q, RF-LQ-SYNTHESIS, RF-LOCAL-ID, RF-LQ-CONTINUATION, LOCAL and
ENERGY, including the normalized pressure and initial trace, to NS-R3.
The theorems here DO NOT supply this bound or a substitute producer.

They instead test an exact proposed ingredient of a NEGATIVE construction:
a positive invariant cone allowing independent activation of its Fourier
pieces. Theorem 1 eliminates every closed, acute, spectrally decomposable
cone on R3, not just one carrier geometry. Theorem 2 gives a finite-packet
version without spectral decomposability, and an actual Schwartz-data exit.
Theorem 3 quantifies how much full-state response is necessary to prevent
that particular exit. It is only a boundary tangency bound, not a turnover
cost. Section 6 proves explicitly why correlated pumps evade the argument.

Thus the implication actually obtained is

    independent acute Fourier-cone trapping for original NS
        -> zero cone (Theorem 1),

not

    regeneration -> loss -> RF-q.

This removes a construction class; it does not replace the missing PDE
estimate by an unknown quantity and call that a smaller positive gap.

## 1. Notation and the continuum cone theorem

Use the unitary angular-frequency Fourier transform, with convolution
factor kappa=(2pi)^(-3/2). Write

    Q(u)=-P div(u tensor u),
    C(v,w)=Q(v+w)-Q(v)-Q(w),
    H_infty=intersection_(m>=0) H^m_sigma(R3;R3).

Here P is the ORIGINAL Leray projection. The canonical pressure is
`p_hat=-sum xi_i xi_j/|xi|^2 Fourier(u_i u_j)` off zero; it is not a
separately chosen forcing. Pairings below are real L2 pairings. For every
u in H_infty, Q(u) is in H_infty and

    <u,Q(u)>=0.                                             (1.1)

These facts follow from the Sobolev product rule and transport integration
by parts. For example the large-radius cutoff error in (1.1) is bounded by
C/R times ||u||infinity ||u||2^2. No Fourier support truncation of the
trajectory is made.

A closed convex cone K in real L2_sigma is called ACUTE here if

    <v,w> >= 0 for every v,w in K.                          (1.2)

Call K SPECTRALLY DECOMPOSABLE if P_E K is contained in K for every
measurable symmetric set E=-E, where P_E is the orthogonal Fourier
restriction. This is a strong independence assumption: an arbitrary
frequency subset, not merely a whole prescribed packet, may be removed.
It is satisfied, for example, by pointwise acute cones of allowed Fourier
vectors with the reality constraint. It is NOT satisfied by a general
cone of correlated packet amplitudes.

**Theorem 1.** Fix nu>0. Suppose K is a closed, convex, acute, spectrally
decomposable cone in real L2_sigma(R3). Suppose the original local strong
NS solution from every datum in K intersect H_infty belongs to K on some
positive interval (which may depend on the datum). Then K={0}.

Only local invariance is assumed, not global existence. Its local-solution
hypothesis is explicitly for smooth finite-energy H_infty data; it is not
silently inferred from an invariance assertion restricted to Schwartz data.
Section 4 supplies a separate explicit Schwartz falsifier for a common
packet version. The proof is in Sections 2--3.

## 2. Fourier holes force the entire nonlinear vector field into the cone

For u in K intersect H_infty fix R>0. Partition B_R, up to null sets,
into finitely many symmetric measurable cells E_j with |E_j|<=eta. Such
partitions are obtained by pairing small cells in opposite half-balls.
Set r_j=P_(E_j)u and v_j=u-r_j=P_(E_j^c)u. Both are in K intersect H_infty.
Let U_j(t) be the original local NS solution from v_j. Its Fourier
restriction to E_j is initially zero. Since the Laplacian commutes with
P_(E_j), local strong differentiability into L2 gives

    P_(E_j)U_j(t)/t -> P_(E_j)Q(v_j) in L2 as t downarrow 0.

Each left side is in K by invariance, decomposability and positive scalar
closure. Consequently P_(E_j)Q(v_j) is in K. Finite sums give

    g_eta=sum_j P_(E_j)Q(v_j) in K.                       (2.1)

This uses different ACTUAL initial states only to test universal cone
invariance. It does not reset one proposed cascade trajectory.

The divergence-form Fourier symbol and Cauchy--Schwarz give, for |xi|<=R,

    |Fourier(Q(u)-Q(v_j))(xi)|
       <= kappa R (||u||2+||v_j||2)||r_j||2
       <= 2 kappa R ||u||2 ||r_j||2.                     (2.2)

Indeed `u tensor u-v tensor v=r tensor u+v tensor r`; the matrix
contraction with xi has norm at most |xi|, and P_xi is a contraction.
The value at xi=0 can be set to zero. This estimate is valid with complex
Fourier vectors and the real-valuedness constraint.

By disjointness, Plancherel, and |E_j|<=eta,

    ||P_(B_R)Q(u)-g_eta||2^2
       <=4 kappa^2 R^2 ||u||2^2 sum_j |E_j| ||r_j||2^2
       <=4 kappa^2 R^2 eta ||u||2^4.                    (2.3)

First send eta to zero, then R to infinity. Closedness proves

    Q(u) in K for every u in K intersect H_infty.         (2.4)

There is no assumed common lifespan for all cells: each derivative is
computed at its own initial time. There is no finite-dimensional R3 flow.
Arbitrarily small Fourier-cell volume, rather than a lattice mode count,
is essential to (2.3).

Next set z=Q(u), which is in K intersect H_infty. For epsilon>0 put
w=u+epsilon z. By convex conic closure w is in K intersect H_infty, and
(2.4) also gives Q(w) in K. The exact energy cancellation and acuteness yield

    0=<w,Q(w)>=<u,Q(w)>+epsilon <z,Q(w)>,
    <u,Q(w)> >=0,             <z,Q(w)> >=0.

Thus <z,Q(w)>=0. Continuity of Q from H^2 to L2 along this smooth
one-parameter family, followed by epsilon downarrow 0, proves

    ||Q(u)||2^2=0.                                         (2.5)

This argument explains why energy conservation ALONE is insufficient:
(2.4), which is stronger than ordinary boundary tangency, came from
independent Fourier deletion and the atomless-volume estimate.

## 3. The exact Leray numerator makes a decomposable stationary cone trivial

We prove the additional assertion needed to finish Theorem 1:

    If u in H_infty and Q(P_E u)=0 for every symmetric E,
    then u=0.                                             (3.1)

It suffices here that the hypothesis hold for bounded E. We first record
and rederive the relevant part of the known two-wave classification [KY].
For real nonparallel p,q with |p|!=|q| and nonzero complex a,b satisfying
p.a=q.b=0, define

    A(p,q;a,b)=P_(p+q)[(q.a)b+(p.b)a].                     (3.2)

Then A=0 implies that both a and b are complex multiples of p cross q.
To see this, rotate so p=P e1, q=Q(cos(theta)e1+sin(theta)e2), with
P,Q>0 and 0<theta<pi. Write

    a=alpha e2+zeta e3,
    b=beta(-sin(theta)e1+cos(theta)e2)+omega e3.

The component of (3.2) perpendicular to p+q inside their plane is

    sin(theta)(Q^2-P^2) alpha beta / |p+q|,

and its e3 component is

    sin(theta)(Q alpha omega-P beta zeta).                (3.3)

If A=0, unequal lengths force alpha beta=0. If alpha=0, nonzero a
implies zeta!=0, and the second equation forces beta=0. The other case
is identical. Both polarizations are therefore normal to the plane.
This proof is valid over C, not only for real or helical polarizations.

Now suppose u is nonzero in (3.1), and write a(xi)=u_hat(xi). Choose
nonzero Lebesgue points p,q of a (also Lebesgue points of |a|^2), with
p,q nonparallel. Restrict u to small balls around +/-p and +/-q, calling
the two resulting real fields v_delta,w_delta. The restrictions and their
union have zero Q by hypothesis, so

    C(v_delta,w_delta)=0.                                 (3.4)

For sufficiently small delta, the four output neighborhoods centered at
+/-(p+q) and +/-(p-q) are disjoint. Integrate the Fourier transform of
(3.4) over B_(2delta)(p+q). Only the two ordered plus-pair contributions
occur. Divide by |B_delta|^2 and send delta to zero. The Leray symbol is
continuous near the nonzero p+q, and the two averages converge by the
Lebesgue-point property and Cauchy--Schwarz. The result is

    -i kappa A(p,q;a(p),a(q))=0.                           (3.5)

This is a continuum differentiation argument. It does not equate a
discrete Fourier polynomial to a finite-energy R3 field.

The nonzero set of an L2 Fourier transform has positive three-dimensional
measure. Choose p,q,r from its Lebesgue points so that p,q,r are linearly
independent and |q|,|r| differ from |p|. The excluded planes, lines and
spheres have measure zero. Apply (3.3)--(3.5) to p,q and to p,r:

    a(p) in C (p cross q) intersect C (p cross r)={0},

contradicting the choice of p. This proves (3.1).

To finish Theorem 1, a nonzero member of K would have a nonzero restriction
u=P_(B_R)v in K intersect H_infty for some finite R. Its every further
symmetric restriction has zero Q by (2.5). Assertion (3.1) gives u=0,
a contradiction. Thus K={0}. QED.

The hypotheses matter. Periodic finite-mode shears and Beltrami fields do
not contradict the theorem: their spectral measure is atomic and they are
not nonzero L2(R3) fields. A stationary compact Euler flow is not required
to remain stationary after arbitrary Fourier deletion. The invariant real
odd sector is a linear space containing both u and -u, so is not acute.

## 4. Fixed-packet faces: a separate Schwartz-data obstruction

The previous theorem demands much more independence than a prescribed
packet cone. The following finite lemma does NOT assume decomposability.
Let f1,f2,f3 be real solenoidal orthonormal Schwartz fields satisfying

    inner(f_i,Delta f_j) = 0 for i!=j,
    inner(f_i,Q(f_j)) = 0 for all i,j.                     (4.1)

These are exact vanishing identities, not favorable-sign assumptions. Define

    c1=<f1,C(f2,f3)>, c2=<f2,C(f3,f1)>, c3=<f3,C(f1,f2)>.

Polarizing (1.1) gives

    c1+c2+c3=0.                                            (4.2)

**Theorem 2.** If a convex cone contains each nonnegative ray R_+ f_i,
is contained in the three halfspaces <u,f_i>>=0, and is locally invariant
under original NS, then c1=c2=c3=0.

Proof. At u=b f2+c f3, b,c>0, the absent coordinate has derivative
`d_t<u,f1>=bc c1`. Both the viscous cross term and the self-pumps vanish
by (4.1). Tangency requires c1>=0. The other two faces give c2,c3>=0;
(4.2) finishes the proof. No restriction on allowed exterior states of
the proposed cone was made. The failure is at actual initial states
that conic convexity requires it to contain. QED.

### 4.1 A nonzero original-NS triple of Schwartz packets

Set

    p=(1,0,0), q=(0,1,0), r=(1,1,0),
    a=(0,1,1), b=(-1,0,-1), c=(0,0,1).

Choose a real radial nonnegative phi in C_c^infinity(B1), positive near
zero, and phi_delta(xi)=delta^(-3/2)phi(xi/delta). Define raw packets

    F_(k,v),hat(xi)=-i P_xi v phi_delta(xi-k)
                    +i P_xi v phi_delta(xi+k),             (4.3)

and normalize f1=F_(p,a)/||F_(p,a)||2, f2=F_(q,b)/||F_(q,b)||2,
f3=F_(r,c)/||F_(r,c)||2. For 0<delta<1/4 they are Schwartz, real,
odd and exactly solenoidal. Their supports are disjoint. Every self-sum
support lies near 0 or +/-2k and misses every tested packet, since the
corresponding center distances are at least one and 3delta<1. Thus (4.1)
holds EXACTLY, although Q(f_i) need not vanish outside the tested packets.

The complete carrier calculation gives unnormalized cyclic coefficients

    (c1,c2,c3)_carrier=(-2,-2,4).                          (4.4)

For clarity the real odd convention is u_hat=i b. The cross-source from
parents p,q is supported at +/-r with b_source(r)=-2 e3. The sources
from q,r include both +/-p and +/-(p+2q); those from r,p include both
+/-q and +/-(2p+q). The latter side coefficients do not vanish. At old
carriers the new vector also need not have its old polarization. None of
these modes or vector components is discarded in the packet construction.

Let Phi=||phi||2 and J=integral phi(z)(phi*phi)(z) dz>0. Rescaling the
finite packet convolution at each center, using smoothness of P away
from zero, proves

    ci = kappa J delta^(3/2) (-2,-2,4)_i
                   /(4 sqrt(2) Phi^3) + O(delta^(5/2)).   (4.5)

The normalization product tends to 4 sqrt(2) Phi^3. In particular there
is a delta0>0 for which c1,c2<0<c3 for every 0<delta<delta0. No numerical
value of delta0 is asserted without an explicit bump-dependent remainder.
Reflection interchanging x1,x2 sends f1 to -f2, f2 to -f1 and f3 to f3.
Orthogonal covariance and (4.2) therefore give the exact identity

    (c1,c2,c3)=(-beta,-beta,2beta),   beta>0.               (4.6)

Fix such a delta. For every nu>0 and b,c>0, the ACTUAL original solution
from d=b f2+c f3 satisfies

    <u(t),f1>=-beta bc t+o(t)<0

for all sufficiently small positive t. The datum is admissible real
solenoidal Schwartz data, with finite energy. Viscosity, the normalized
pressure, and all generated exterior are included by local original NS.
This is an exact failure of a proposed halfspace/cone, not a singularity.
Re-signing the three packet axes multiplies every ci by the common sign
product, so every orthant still has a strictly outgoing face.

## 5. Exact full-state price of repairing the outgoing face

**Theorem 3.** Use the normalized packets (4.6). At an actual smooth
state write

    u=b f2+c f3+h,   <h,f_i>=0 (i=1,2,3), b,c>0,
    e=||h||2, L=||grad f1||infinity,Frobenius,
    d=||Delta f1||2, V=sqrt(b^2+c^2).

If its missing coordinate is inward-pointing, `d_t<u,f1>>=0`, then

    beta bc <= L(2 V e+e^2)+nu d e.                       (5.1)

Proof. The exact derivative at this state is

    -beta bc+nu<h,Delta f1>+<f1,C(b f2+c f3,h)+Q(h)>.

Integration by parts in the divergence form and Cauchy--Schwarz give the
last two terms in absolute value at most the right side of (5.1).
The pressure is removed only in this solenoidal testing. All h-h and
h-parent interactions and the viscous off-packet response are retained.
This proves the claimed necessary condition. QED.

Equivalently e is at least the positive root of

    L e^2+(2LV+nu d)e-beta bc=0.                           (5.2)

This is a full-state boundary bound, not merely a statement that some side
mode exists. For b=c=A, sufficiently small delta, and A>=nu d/beta,
it implies e>=c_phi A, with c_phi>0 independent of small delta: (4.5)
gives beta>=c delta^(3/2), Fourier inversion gives L<=C delta^(3/2),
and substituting e/A into (5.1) proves the assertion. Constants can
explicitly depend on the fixed bump. The critical amplitude is not assumed
small.

Under L2-normalized frequency dilation f^K(x)=K^(3/2)f(Kx), beta and L
both scale by K^(5/2), while d scales by K^2. The threshold consequently
has the correct amplitude/viscosity ratio A K^(1/2)/nu. For a fixed
relative-width packet the ratio L/beta is unchanged.

IMPORTANT LIMITS: e here is a full L2 exterior norm. Its lower bound is
not automatically a critical angular-exterior lower bound, because h
can have low frequencies. Nor is it a loss of kinetic energy, angular
entropy, dissipation, or an input-summable resource. The same exterior
may help at many different faces. No turnover duration or summation is
proved. Replacing this distinction by an event-cost claim would be false
reasoning.

## 6. The correlated-pump escape is real, but is not a full NS cell

The exact energy-cancelling abstract triad

    x'=-beta yz, y'=-beta zx, z'=2beta xy                   (6.1)

does not preserve the full positive orthant, consistently with Theorem 2.
But x=y=s is invariant, and setting X=sqrt(2)s reduces it to

    X'=-beta Xz,             z'=beta X^2.                 (6.2)

The correlated cone x=y>=0,z>=0 is invariant. For X(0)=A,z(0)=0,

    X(t)=A sech(beta A t), z(t)=A tanh(beta A t).

It is precisely an energy-conserving pump, despite (4.2) and the absence
of coordinate self-squares in (6.1). Thus those two algebraic facts alone
cannot exclude a correlated cascade architecture. The invariant
x^2-y^2 also shows exactly why equal parent loading matters in this
isolated triad.

Adding viscous diagonal terms -nu x,-nu y,-2nu z preserves x=y and its
positive cone. It is still only a calibration ODE. For the actual carrier
triple (4.3), (6.1) is NOT its closed equation: the side outputs and changing
parent polarizations in Section 4 are nonzero, and finite-width diffusion
also produces off-packet response. No original-NS pump realization or
second turnover is inferred from this ODE.

Theorems 1--3 therefore force a viable cone construction to abandon the
relevant independent-activation assumptions, retain correlations with
its inherited exterior, or allow sign/phase/polarization changes. They do
not show that such correlated full-state recurrence is impossible.

## 7. Exact original-operator discriminator and source audit

The ORIGINAL support rule and incompressibility give zero self-pumping
from a single narrow carrier packet into any disjoint same-annulus packet
whose support misses 0 and +/-2k. This is the exact property used in
(4.1); the small-cell estimate (2.2) uses the actual convolution symbol;
(3.3) uses its Leray numerator. Energy cancellation itself is shared with
averaged operators and is not a discriminator.

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier--Stokes equation*, arXiv:1402.0290v3,
https://arxiv.org/html/1402.0290v3 . Sections 5.1, 6 and Table 1 were
inspected. The table assigns the same-level (1,1,2,0,0,0) coefficient
epsilon and the two reverse entries -epsilon/2. In the repository's
packet normalization this gives a nonzero same-annulus self-pump
`epsilon (1+epsilon0)^(5n/2)`, whereas original support gives zero.
This is the already identified discriminator, not a newly claimed one.
Tao's packet-amplitude cone need not be stable under arbitrary Fourier
holes; Theorem 1 must not be applied to it by merely changing an operator
name. Section 6 also directly demonstrates the correlated-pump escape.

[KY] N. Kishimoto and T. Yoneda, *Characterization of three-dimensional
Euler flows supported on finitely many Fourier modes*, arXiv:2110.08039v1,
https://arxiv.org/html/2110.08039v1 . Lemma 2.1, Proposition 2.2 and their
proofs were inspected. The unequal-length polarization classification
used in (3.3) is established prior art and is rederived here. Their
finite-mode global classification is NOT an R3 finite-energy theorem
being imported to replace the Lebesgue-point argument in Section 3.

The finite-Lorentz consumer and current packet/mixing/pressure no-go
results retain their recorded repository statuses. A targeted prior-art
search is not an exhaustive novelty assessment. The new continuum cone
argument and packet boundary application require independent review.

## 8. Checks, failed extensions, and the remaining terminal nut

`research/check_fourier_cone.py` passed 2577 exact assertions, including
1296 deterministic rational pair cases. It checks the two-wave numerator
over symbolic complex polarizations, deterministic rational calibrations,
all outputs of the concrete triple, cyclic coefficients and all orthant
re-signings, the correlated-pump identities, and scaling exponents.
It does NOT certify Lebesgue differentiation, the continuum cone proof,
the packet Taylor remainder, local PDE existence, or an independent audit.

Failed extensions proved here, rather than silently assumed:

* independent orthant no-go does not extend to correlated triads (6.1);
* fixed packet coordinates do not close under the full vector equation;
* a necessary exterior L2 amplitude is not an expended or summable cost.

There is no new finite-time singular solution or arbitrary-data regularity
proof. The single dominant terminal nut remains a critically timed,
concentration-producing regeneration with the entire inherited state:
construct a scale-repeating correlated full-vector NS cell with controlled
errors, or prove an original-NS-specific summable loss for every such
regenerative event AND extract those events into the signed RF-q producer.
The first missing positive theorem is the latter extraction-and-summation
statement; no theorem in this note is claimed to replace it.
