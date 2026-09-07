# Axial rigidity without recurrence and a necessary record-block condition

Date: 2026-09-07.
Frozen research input: `650855d1f50f42f9cb309cba22cbe2d22c106b7f`.
Status: complete author derivation over the explicitly scoped sources below;
independent mathematical audit and prior-art assessment pending.
Outcome: B, a scoped singularity reduction. NS-R3 is NOT PROVED.
No novelty claim, canonical graph promotion, manuscript or formalization change.

## 1. Terminal gate and precise improvement

The target remains the original unforced incompressible NS equation on R3,
every solenoidal Schwartz datum and every fixed positive viscosity nu. The
proof does not replace that equation by a forced response, a kinetic moment
system, a scalar inequality, or an Euler limit.

The preceding committed Type-I note supplies critical local energy from a
specified temporal amplitude bound on the globally mild equation. The prior
UNPUSHED axial-return note coupled that interface to a local axial theorem,
but required an NS-similarity return. The present proof removes recurrence
from the axial contradiction. The old unpushed patch is not applied over the
concurrent main update, and its pressure estimates are not counted again as
new progress.

The candidate rigidity actually proved is:

    U bounded ancient mild, ||U(s)||_infinity <= K/sqrt(1-s), s<=0,
    one locally axially equivariant time slice
      => U=0.                                                   (1.1)

The symmetry includes swirl. Neither a return, self-similarity, finite total
energy, spatial decay, global L3, nor a bound on accumulated strain is assumed.
The coefficient K is fixed across the entire ancient history; its existence
is NOT inferred for arbitrary singularities.

The source of new dynamical information in the proof chain is the original
canonical pressure relation, combined with the established nonlinear axial
Type-I singularity theorem. Weak compactness by itself is not the rigidity:
a nonzero profile is rescaled to a singular suitable limit, its symmetry and
energy bounds are retained, and the axial theorem contradicts that singularity.

The necessary property of an ACTUAL hypothetical singularity obtained below
is a finite-memory alternative at each sufficiently developed velocity record:
for every fixed upper transition duration A, either one of the preceding m_*
transitions has duration greater than A, or the local axial symmetry error is
at least eta>0. The constants do not depend on the datum or viscosity.

The complete scoped contradiction is

    Tstar<infinity + records ending longer and longer blocks with ell<=A
                  + vanishing one-slice local axial error
      => nonzero bounded ancient mild U with the decay in (1.1)
      => a suitable axial Type-I singular limit by blow-down
      => contradiction with Seregin's local axial theorem.       (1.2)

Every arrow is proved below or given by a precisely stated inspected source.
The first arrow RETAINS the block and geometry hypotheses. No theorem forces
all singularities into that subclass. This does not close non-axial profiles,
intermittent records without long uniformly bounded blocks, or slow records.

## 2. Solution conventions and analytic inputs

For the analytic argument set nu=1 and use

    U_s-Delta U+div(U tensor U)+grad p=0,    div U=0.              (2.1)

Ancient mild means the full heat/Oseen integral identity on every finite
subinterval of (-infinity,0]. The velocity is globally bounded in space on
such intervals. Bounded-data local mild theory extends a bounded terminal
slice a little past zero. Thus zero can be treated as an interior regular
slice; the extension is not a claim of global continuation.

The pressure gradient is the canonical one determined by the mild equation,

    p = sum R_i R_j(U_i U_j) modulo functions of time.             (2.2)

For bounded nondecaying slices the double Riesz transform is understood with
its local distributional term and a subtracted far kernel. A spatially linear
harmonic pressure, and the spatially constant acceleration it could produce,
are not allowed by the full mild identity.

The established inputs are the following, with their actual scopes.

[S1] KNSS bounded-data local mild existence and uniqueness, interior spatial
regularity and compactness on expanding past intervals. They apply without
global energy or decay assumptions. Uniformly bounded mild histories extend
through zero for a common positive time, and converge locally in each fixed
spatial derivative order after subsequence selection. Integrable spatial
Oseen tails and the integrable time factor (t-s)^(-1/2) preserve mildness.

[S2] Bounded-data spatial analyticity: Grujic, Theorem 3.1. Restarting before
a slice makes that slice real analytic on all of R3. Only this bounded-data
analyticity statement is used, not the paper's sparseness criterion.

[S3] Time analyticity of bounded whole-space mild NS, Dong--Zhang, Theorem
3.1. No L3 or decay condition is inserted. It is applied separately to two
actual mild solutions, not to an unjustified composition of separately
analytic functions.

[S4] Albritton--Barker, Lemma 2.2 and Proposition 2.3. Suitable solutions on
an outer cylinder with uniformly bounded L3 velocity and L^(3/2) pressure
have a subsequence converging strongly in local L3 and weakly in local
L^(3/2), including approach to the top time, to a suitable solution. If their
velocity suprema diverge on every smaller cylinder centered at the top
origin, that limit is singular there. This is persistence of singularities,
not a conclusion from weak compactness alone. Their reverse rescaling
argument motivates Section 5, whose symmetry and pressure adapters are given
explicitly here.

[S5] Seregin, Theorem 2.1. An axially symmetric SUITABLE weak solution on an
axial cylinder cannot have a Type-I singularity at the on-axis top center.
Type I is defined by finiteness of the minimum of the scale-invariant
energy limsups. The theorem permits swirl and does not require finite total
whole-space energy. It is NOT general three-dimensional Type-I regularity.

The pressure/local-energy mechanism at the frozen main is rederived in
Section 3 so the application does not assume that an ancient L-infinity
bound already implies critical local energy. In particular [S4, Remark 3.2]
explicitly warns about the p=infinity interface; it is not imported there.

## 3. Critical local energy from decay on the available past only

**Lemma 1.** Suppose U is bounded ancient mild through time zero and

    ||U(s)||_infinity <= K/sqrt(1-s),    s<=0,    K<infinity.       (3.1)

There are finite functions F(K), G(K) such that for EVERY z in R3, r>0 and
b<=0, with Q_r(z,b)=B_r(z) x (b-r^2,b),

    (1/r) ess sup_(b-r^2<s<b) integral_(B_r(z)) |U(s)|^2
      +(1/r) integral_(Q_r(z,b)) |grad U|^2 <= F(K),              (3.2)
    (1/r^2) integral_(Q_r(z,b)) (|U|^3+|p-(p)_(B_r(z))|^(3/2))
      <= G(K).                                                  (3.3)

No solution between zero and the notional time one is assumed. All estimates
are on cylinders contained in the available past. The number one in (3.1)
is a convenient positive time offset, not a new future lifespan.

### 3.1 Canonical pressure bound

For a bounded smooth solenoidal slice f, let

    h=||f||_infinity,    M_r=sup_z integral_(B_r(z)) |f|^2.

Fix z,r and a cutoff theta equal to one on B_(4r)(z), supported on B_(8r)(z).
On B_(2r)(z) write a representative of (2.2) as

    p_near = sum R_i R_j(theta f_i f_j),
    p_far(y) = sum integral [K_ij(y-x)-K_ij(z-x)]
                                      (1-theta(x)) f_i(x)f_j(x) dx. (3.4)

K_ij is the double-Riesz kernel away from its origin. The difference is
bounded by C r |x-z|^(-4). Its remote tail is absolutely integrable for
bounded f. The near term uses the FULL double-Riesz multiplier; the local
delta term of the differentiated Newtonian kernel is not dropped.

L2 multiplier boundedness and covering the fixed larger ball give

    ||p_near||_2 <= C h M_r^(1/2).

For the remote shell at radius 2^j r use a covering by C 2^(3j) radius-r
balls, Cauchy--Schwarz on each ball, and |f|^2<=h|f|. Then

    integral_shell |f|^2 <= C h 2^(3j) r^(3/2) M_r^(1/2),
    ||p_far||_(L-infinity(B_(2r)(z)))
       <= C h r^(-3/2) M_r^(1/2) sum_(j>=2)2^(-j).

Consequently

    ||p-(p)_(B_(2r)(z))||_(L2(B_(2r)(z)))
       <= C h M_r^(1/2).                                        (3.5)

Subtracting a spatial mean costs at most a fixed factor. Different local
representatives in (3.4) have the same gradient and differ only by time
functions. To identify that gradient with the physical mild pressure,
differentiate the Oseen identity distributionally. First do this for a
spatially cut-off tensor and then remove the cutoff: the pressure-gradient
kernel has integrable |x|^(-4) tails, while its near part is a distribution
of finite order. This gives (2.1) with (3.4), rather than merely solving
its pressure Poisson equation and leaving an uncontrolled harmonic term.
This is the same pressure convention as the frozen main, Section 2.

### 3.2 Integrated energy before taking the spatial supremum

Choose 0<=chi<=1 supported on B2 and equal to one on B1, and let

    F_r(s)=sup_z integral chi((x-z)/r)|U(x,s)|^2 dx.

This is comparable to M_r(U(s)) by fixed coverings. It is measurable: center
suprema can be taken on a countable dense set. On each compact time interval
it is finite and bounded. No derivative of a maximizing center is taken.

The actual local energy equality with the fixed cutoff is

    integral chi_r |U(t)|^2 + 2 integral_a^t integral chi_r |grad U|^2
      = integral chi_r |U(a)|^2
        +integral_a^t integral |U|^2 Delta chi_r
        +integral_a^t integral (|U|^2+2p)U.grad chi_r.              (3.6)

A spatial pressure constant cancels since integral U.grad chi_r=0.
The diffusion and convective boundary terms are bounded by C r^(-2)F_r and
C h(s)F_r/r. By (3.5), the pressure term is bounded by

    C r^(-1) ||p-p_B||_(L2(B_(2r))) ||U||_(L2(B_(2r)))
       <= C h(s) F_r(s)/r.

After integration, taking the supremum over centers yields

    F_r(t)<=F_r(a)+C integral_a^t [r^(-2)+h(s)/r]F_r(s) ds.        (3.7)

Gronwall, and then (3.6) with its positive dissipation retained, bound both
F_r(t) and the local integrated dissipation by

    C F_r(a) exp(C[(t-a)/r^2 + r^(-1)integral_a^t h]).              (3.8)

The coefficient contains h, not h^2. This is a proved estimate on true mild
NS trajectories, not an assumption that energy alone controls a critical norm.

### 3.3 Choice of the starting slice

For a=b-r^2, b<=0, (3.1) gives

    F_r(a)<=C K^2 r^3/(1-b+r^2)<=C K^2 r,
    integral_a^b h(s) ds
       <=2K[sqrt(1-b+r^2)-sqrt(1-b)]<=2Kr.

Thus (3.2) holds with F(K)=C K^2 exp(C(1+K)), increasing C if necessary.
The bounds hold at every intermediate time by (3.8), not only at b.

For the cubic term use integral_B |U|^3<=h(s) F(K)r and integrate.
For pressure, Holder and (3.5) give

    integral_(B_r) |p-p_(B_r)|^(3/2)
       <=C r^(3/4) h(s)^(3/2) [F(K)r]^(3/4).

Since integral_a^b h(s)^(3/2)ds<=4 K^(3/2) r^(1/2), this proves (3.3),
for example with

    G(K)=C[K F(K)+K^(3/2)F(K)^(3/4)].

The smooth original U has legitimate local energy and pressure at each top
b<=0. Nothing about strong continuation at a prospective singular future
endpoint was used. Lemma 1 is proved. QED.

## 4. Propagation of a single local symmetry slice

For a unit vector e and c.e=0 define the axial equivariance generator

    A_(e,c)U(y,s)=[e cross (y-c)].grad U(y,s)-e cross U(y,s).       (4.1)

It is vector equivariance, including swirl, not componentwise independence
of the angular coordinate.

**Lemma 2.** If A_(e,c)U=0 on a nonempty open ball at one time s_a<=0,
then U is axially equivariant about c+R e at every ancient time.

Proof: spatial analyticity [S2] makes the generator zero on all of R3 at
that slice. If R_theta rotates about e, integration in theta gives

    U(c+R_theta(y-c),s_a)=R_theta U(y,s_a).

The two sides, expressed as rotated/translated velocity fields, are exact
mild NS solutions. Forward uniqueness gives equality on a nonempty time
interval after s_a. The terminal slice can be extended first if s_a=0.
Time analyticity [S3] for these two solutions propagates equality backwards
on their common connected ancient interval. This explicitly supplies the
backward step that forward uniqueness alone would not give. QED.

The canonical pressure admits an axially invariant representative: the Riesz
operator is rotation covariant, and the difference after a rotation is a
spatial constant. Subtracting the mean over a ball whose center is on the
axis removes that constant. This will be used before taking a suitable limit.

We will also use the already banked one-slice planar lemma [R1]: if a bounded
ancient mild field has partial_e U=0 on one open ball on one slice, it is a
single constant vector. Its nondecaying three-component scope matters.
Briefly, analyticity and uniqueness propagate the translation invariance;
the horizontal 2D ancient velocity is spatially constant by [S1, Theorem
5.1]; the remaining vorticity (partial_2 w,-partial_1 w,0) has EXACTLY zero
stretching and is a bounded ancient heat field after removing a constant
spatial drift. The Gaussian gradient bound from an arbitrarily early time
makes it spatially constant. Boundedness of w makes those derivatives zero,
and the full mild identity removes time-dependent constants. This is not
an assertion about the inviscid shear class in the earlier falsifiers.

## 5. The decisive Liouville argument: blow-down without recurrence

**Theorem 1.** Let U be bounded ancient mild on R3 x (-infinity,0], satisfy
(3.1), and have one locally axial slice as in Lemma 2. Then U=0.

### Proof, with the singular-limit and symmetry adapters

Lemma 2 makes U axial on its whole past. Translate a point of its axis to
the origin and rotate that axis to e3. These fixed changes preserve (3.1).
The transformed field, still denoted U, has the spatially fixed axial line
R e3. We do NOT center the blow-down on a potentially off-axis velocity peak.

Suppose U is not zero. There are finite y_* and s_*<0 with

    d=|U(y_*,s_*)|>0.

Nontriviality at time zero also gives such a negative time by continuity.
For integer k tending to infinity form actual unforced NS solutions

    V_k(x,t)=k U(kx,k^2 t),   -4<t<=0,
    q_k(x,t)=k^2 p(kx,k^2 t)-a_k(t),                            (5.1)

where a_k is the spatial average of the first pressure term on B2. Each
V_k is globally mild and smooth on this compact interval, although its
supremum bound need not be uniform in k. Its axis is exactly R e3 for all k.
The chosen q_k is axially invariant as explained after Lemma 2.

Lemma 1 and critical scaling give uniform A,E,C,D_0 on every cylinder in
the common domain. In particular, with the fixed pressure gauge above,

    sup_k (||V_k||_(L3(B2 x (-4,0)))
                 +||q_k||_(L^(3/2)(B2 x (-4,0)))) < infinity.     (5.2)

Apply [S4, Lemma 2.2] on this outer cylinder and, if desired, on a nested
sequence of interior cylinders. We obtain a SUITABLE limit (V,q) with
V_k -> V strongly in local L3 through approach to time zero and q_k -> q
weakly in local L^(3/2). Energy weak compactness also gives grad V_k weakly
in L2 on each smaller cylinder. The axial identities pass to distributions
for both velocity and pressure; hence (V,q) is an axially symmetric suitable
solution on an axial cylinder around (0,0).

For each fixed 0<r<1, lower semicontinuity gives

    (1/r) integral_(B_r x (-r^2,0)) |grad V|^2 <= F(K).           (5.3)

It suffices to pass along rational radii and enlarge balls to obtain the
same conclusion, up to a fixed factor, for all radii. Equivalently one may
use the weak convergence on each fixed smaller cylinder directly. Axial
cylinders and balls are comparable, so their normalized dissipation is
bounded as well. This is a finite Type-I energy bound, not its smallness.

On the other hand,

    |V_k(y_*/k,s_*/k^2)|=kd.

These points lie in EVERY fixed smaller backward cylinder centered at (0,0)
for all sufficiently large k. Smoothness makes the essential supremum there
at least kd/2. Thus

    ||V_k||_(L-infinity(Q_r(0,0))) -> infinity  for every r>0.     (5.4)

By [S4, Proposition 2.3], (5.2), the strong/weak convergences, and (5.4)
force V to be singular at (0,0). This invocation is essential: the proof
does not simply assume nontriviality or singularity passes under weak limits.
The cited proposition proves the implication using local pressure splitting
and epsilon regularity if the putative limit were regular.

We have constructed an axially symmetric SUITABLE singularity at an ON-AXIS
point, with (5.3). Seregin's Theorem 2.1 [S5] says that such a singularity
must instead have infinite Type-II energy limsups. This is a contradiction.
Therefore U=0. QED.

There is no actual singular Schwartz-data solution asserted by this proof.
The local suitable singular limit is an auxiliary consequence of the assumed
nonzero ancient object, then contradicted in the exact class of [S5]. The
original target is neither weakened to weak existence nor replaced by a
local problem. Swirl has not been set to zero at any step.

## 6. A uniform finite-history gap, even for axes escaping to infinity

Fix K>=1, R>0 and B>=0. For a history W and s_a in [-B,0] let

    E_ax(W;e,c,s_a)=integral_(B_R) |A_(e,c)W(y,s_a)|^2 dy,
    |e|=1, c.e=0.                                             (6.1)

There is NO upper bound on |c| in the following theorem.

**Theorem 2.** There exist L_*>B and eta>0, depending only on K,R,B, such
that every globally mild history on [-L,0], L>=L_*, with

    |W|<=1, |W(0,0)|=1,
    ||W(s)||_infinity<=K/sqrt(1-s),   -L<=s<=0,                  (6.2)

has E_ax>=eta for every e,c,s_a in (6.1).

Proof: otherwise take histories of lengths tending to infinity and errors
tending to zero. Bounded mild extension through zero, interior estimates,
and diagonal compactness give local C1 convergence to an ancient U retaining
|U(0,0)|=1 and (3.1). After a subsequence e_j and s_(a,j) converge.

If c_j stays bounded, pass to its limit. The error tending to zero yields
A_(e,c)U=0 on B_R on the limiting slice. Theorem 1 contradicts the unit peak.

If |c_j| tends to infinity, put d_j=(e_j cross c_j)/|c_j|. These are unit
vectors because c_j.e_j=0. Rearranging (4.1) yields

    partial_(d_j) W_j
      =[(e_j cross y).grad W_j-e_j cross W_j-A_(e_j,c_j)W_j]
          /|c_j|.                                             (6.3)

On the fixed ball and time window the first two terms are uniformly bounded
in L2 by interior regularity. The final term has L2 norm tending to zero.
Thus partial_(d_j)W_j tends to zero in L2. A subsequence d_j converges to a
unit vector d, and local C1 convergence gives partial_d U=0 on the ball on
one slice. The banked planar lemma in Section 4 makes U constant. The decay
(3.1) forces that constant to be zero, again contradicting the unit peak.
These two alternatives exhaust the axes. The theorem follows. QED.

The constants are qualitative; no effective values are claimed. There is
no uniformity as K or B tend to infinity or R tends to zero. Escaping axes
are dealt with by a proved planar limit, not assumed compact in parameter
space. This extension is stronger than the bounded-axis version in the old
unpushed axial-return note.

## 7. Long bounded blocks of genuine velocity records supply the decay

Restore the original viscosity nu>0 and arbitrary solenoidal Schwartz u0.
Let M0>||u0||_infinity, Mn=2^n M0, and let tn be the FIRST time the classical
branch reaches ||u(tn)||_infinity=Mn, whenever that record exists. Choose any
maximizing point xn; spatial decay of the original classical slice ensures
attainment. Set

    ell_n=Mn^2(tn-t_(n-1))/nu,
    U_n(y,s)=Mn^(-1)u(xn+(nu/Mn)y,tn+(nu/Mn^2)s).                (7.1)

The normalized equation has viscosity and nonlinear coefficient both one.
First hitting gives |U_n|<=1 over its available past and |U_n(0,0)|=1.
The heat contraction and Oseen estimate on each record interval give

    Mn/2 <= C_K nu^(-1/2)Mn^2 sqrt(tn-t_(n-1)),
    ell_n>=c_rec=(2C_K)^(-2)>0.                                (7.2)

This is the existing record estimate [R1], not an assumed upper bound.

Suppose a record n ends a block of m<=n transitions satisfying

    ell_n,ell_(n-1),...,ell_(n-m+1) <= A.                       (7.3)

In the coordinates of U_n the earlier record n-j occurs at

    sigma_j=-(sum_(k=0)^(j-1) 4^k ell_(n-k)),   0<=j<=m.

Consequently

    (c_rec/3)(4^j-1)<=-sigma_j<=(A/3)(4^j-1),                  (7.4)
    ||U_n(s)||_infinity<=2^(-j) when s<=sigma_j
                          and the original time is available. (7.5)

For s in [sigma_(j+1),sigma_j], 0<=j<m, combine (7.4)--(7.5):

    (1-s)||U_n(s)||_infinity^2
      <=4^(-j)[1+(A/3)(4^(j+1)-1)]
      <=1+4A/3.                                               (7.6)

Therefore the entire history restricted to [sigma_m,0] satisfies (6.2) with

    K_A=sqrt(1+4A/3),
    L=-sigma_m >= (c_rec/3)(4^m-1).                            (7.7)

This is the promised producer of ancient backward decay: it comes from the
actual record history, not from a future critical norm, recurrence, or a
Type-I assumption on the whole parent. In particular earlier times outside
the chosen block, and all future times after tn, need no upper transition bound.

## 8. Necessary finite-memory loss of axial symmetry at actual records

**Theorem 3 (record-block exclusion).** Fix A,R>0 and B>=0. There exist an
integer m_*=m_*(A,R,B)>=1 and eta=eta(A,R,B)>0 with the following property.
For every original classical whole-space NS branch, every n>=m_* for which
the records exist, and EVERY maximizing xn, if

    ell_(n-j)<=A,   j=0,...,m_*-1,                             (8.1)

then

    inf_(|e|=1, c.e=0, s_a in [-B,0])
      integral_(B_R) |[e cross (y-c)].grad U_n(y,s_a)
                                      -e cross U_n(y,s_a)|^2 dy
        >= eta.                                               (8.2)

The infimum allows axes at arbitrary distances. The physical observation
times in this formula exist, because m_* is chosen to supply a history longer
than B. All constants are independent of u0,nu,M0,n and the maximizing point.

Proof: use Theorem 2 with K_A from (7.7), and choose m_* large enough that
(c_rec/3)(4^m_*-1)>=L_*. Under (8.1), equations (7.4)--(7.7) provide all its
finite-history hypotheses. Apply Theorem 2. QED.

Equivalently, small local axial error at a record forces SOME one of the
preceding m_* normalized transition durations to exceed A. This is a necessary
joint geometric/time-history restriction, not a regularity criterion claimed
to close the arbitrary-data problem.

In physical variables put t_a=tn+nu s_a/Mn^2 and
c_phys=xn+(nu/Mn)c. The error in (8.2) is exactly

    (Mn/nu^3) integral_(B_(R nu/Mn)(xn))
       |[e cross (x-c_phys)].grad u(x,t_a)-e cross u(x,t_a)|^2 dx. (8.3)

Thus all powers of viscosity, amplitude, and length are fixed; (8.2) is
dimensionless under the original NS scaling. The original datum need NOT
be axial. Directions, axes and observation slices may vary between records.

In particular, finite Tstar is incompatible with a sequence n_j tending to
infinity on which (i) the length of a trailing block satisfying ell<=A tends
to infinity for one fixed A, and (ii) the local axial error tends to zero.
No exact or approximate return of a profile is required.

## 9. Relation to concentrating returns and the previous unpushed proof

The stronger Liouville statement also closes the exact axial-return case of
the preceding unpushed proof. The committed concentrating-return construction
[R2] gives a drift v, time T>0 and a continuation with

    ||U(.,s)-v||_infinity<=K/sqrt(T-s),    s<=0,
    U(.,s)->v uniformly as s->-infinity.

If U has one locally axial slice, Lemma 2 gives the corresponding full
symmetry. Its uniform backward limit v must be parallel to that axis.
Hence W(x,s)=U(x+v s,s)-v is axially symmetric about the same line, satisfies
the globally mild equation, and has a bound K'/sqrt(1-s), with finite
K'=K max(1,T^(-1/2)). Theorem 1 makes W=0. Then U=v is constant, contradicting
the half-to-one marks. This covers one concentrating return with arbitrary
fixed rotation and boost and includes swirl; no future singular-point
localization or off-axis-circle argument is now needed. The previously
committed theorem covers nonconcentrating returns without the axial premise.

The bounded-parameter, finite-history sum-of-errors consequence from the
old unpushed note follows by the same compactness argument: a vanishing
return error bounds the boost, and produces an exact return in the limit;
a bounded-axis local axial error produces Lemma 2. Its proof is not counted
as a second terminal advance here. The main addition is Section 8, which
covers a subclass of NONRETURNING fast histories as well.

## 10. Adversarial checks and exact residual gap

Scaling: (7.1), (7.4), (7.6), and (8.3) retain the original nu and amplitude
factors. A radius-r packet still has a physical viscous-energy cost of order
nu^2 r, or nu^3/Mn at a velocity record. No new nonsummable energy cost is
asserted, and no global L3 estimate is extracted from the local energy bound.

Smooth localized data: an initial compact field can be exactly axial on a
ball. That alone supplies neither the long normalized past nor the bounded
record block required by Theorem 3. The result is not an instantaneous
symmetry restriction on all admissible initial data. Finite histories of a
fixed smooth flow can satisfy a decay estimate with K growing with their
length; the theorem keeps K (or A) fixed, so that is not a counterexample.

Stokes and Beltrami tests: nonzero heat modes grow backward and fail the
ancient decay. A spatially constant bounded mild field is constant in time
and also fails the decay unless zero. Arbitrary locally helical fields are
not excluded. The single-channel interaction already in the repository does
not supply a long record block with a vanishing axial error and is untouched.

Pressure and equation class: the bounded differential solution
U(x,s)=a/sqrt(1-s), p(x,s)=-a.x/[2(1-s)^(3/2)] would falsify (3.2) and
Theorem 1 if arbitrary harmonic-pressure accelerations were allowed. It is
NOT a mild solution with canonical pressure; the mild identity for its
constant spatial tensor forces time-independent velocity. This is a scope
check, not a new no-go theorem or a singularity of NS-R3. Forced stress,
kinetic Fisher, scalar-inequality and vanishing-viscosity Euler countermodels
retain their distinct scopes.

Symmetry: vector equivariance includes swirl. All observations concern a
fixed axis on each tested slice, not an axis varying with position. Slice
time is kept in a fixed compact normalized window. Axes escaping to infinity
are handled by the proved planar alternative (6.3), rather than overlooked.
No invariance of the physical rest frame under arbitrary non-axial boosts
is claimed for the generator test.

Persistence: large values of V_k at shrinking cylinders are not alone called
a singular limit. Suitable compactness, fixed pressure gauges and the exact
persistence proposition are all invoked. The blow-down is centered on the
symmetry axis, so its singular limit meets Seregin's on-axis theorem without
an unstated moving-axis or off-axis argument.

The attempted full completion still needs a genuinely general producer.
For a non-axial limit, (5.3) is only bounded critical energy and Seregin's
consumer does not apply. There is no proof that every singularity has a
locally axial slice, a return, or arbitrarily long bounded record blocks.
Isolated fast transitions can be separated by large ell, and ell_n->infinity
is still permitted by the established statements. No unproved assertion
about those cases is placed inside Theorems 1--3.

Thus NS-R3 is NOT proved. The strictly added exclusion is simultaneous local
axial concentration and long blocks of bounded normalized transitions, even
without recurrence, plus the previously unpushed exact axial-return consequence.
A future proof must handle the remaining non-axial and intermittent/slow
cases; this note neither assumes them away nor renames an unknown critical norm.

## 11. Sources, provenance and review requirements

[R1] Repository `research/evidence/2026-09-07-one-slice-record-rigidity.md`,
with `terminal-reset/04-marked-ancient.md`: bounded mild record selection,
record-duration lower bound, and the precisely scoped one-slice planar lemma.
The paper proof of the planar lemma is recalled in Section 4.

[R2] Repository `research/evidence/2026-09-07-concentrating-return-compatibility.md`:
actual continued mild tangent and uniform backward drift limit. It is used
only for the additional consequence in Section 9, not Theorems 1--3.

[R3] Repository `research/evidence/2026-09-07-temporal-type-I-local-energy.md`,
blob `578b7f305eb40048244e206a6efb01eae155ba9c` at the frozen main: canonical
pressure and first-power amplitude local-energy mechanism. Section 3 above
reconstructs the necessary estimate on the already available past; it does
not claim this estimate a second time as new progress.

The previous unpushed artifact is
`2026-09-07-temporal-type-i-and-axial-returns.md`, local snapshot commit
`59b3880b79e7fd5720cb0db80d7bc44d7daae106`. It is provenance, not a remote
commit or an independently certified theorem. Its exact axial-return target
is included as a consequence of the stronger Theorem 1 here.

[S1] G. Koch, N. Nadirashvili, G. Seregin, V. Sverak, *Liouville theorems for
the Navier-Stokes equations and applications*, Acta Math. 203 (2009), 83--105.
https://arxiv.org/html/0709.3599v1
Sections 3--6, bounded mild regularity, Theorem 5.1, Lemma 6.1 inspected.

[S2] Z. Grujic, *A geometric measure-type regularity criterion for solutions
to the 3D Navier-Stokes equations*, Nonlinearity 26 (2013), 289--296.
https://arxiv.org/html/1111.0217v1
Theorem 3.1: bounded-data spatial analyticity. The sparseness criterion is
not applied as an arbitrary-data producer.

[S3] H. Dong, Q. S. Zhang, *Time analyticity for the heat equation and
Navier-Stokes equations*, J. Funct. Anal. 279 (2020), 108563.
https://arxiv.org/html/1907.01687v2
Theorem 3.1: bounded whole-space MILD solutions, no decay hypothesis.

[S4] D. Albritton, T. Barker, *On local Type I singularities of the
Navier-Stokes equations and Liouville theorems*.
https://arxiv.org/html/1811.00502v2
Definition 2.1, Lemma 2.2, Proposition 2.3 including its pressure argument,
and the reverse rescaling in Theorem 1.1 inspected. Remark 3.2 explicitly
does not supply the p=infinity local-energy implication; Section 3 supplies
that interface from the frozen repository's canonical-pressure mechanism.

[S5] G. Seregin, *Local regularity of axisymmetric solutions to the
Navier-Stokes equations*, Anal. Math. Phys. 10 (2020), 46.
https://arxiv.org/html/2006.04140v1
Definitions 1.3 and 1.7, Proposition 1.4, Section 2's axial cylinder and
pressure convention, and Theorem 2.1 inspected. Swirl is allowed; general
non-axial regularity is not asserted by that theorem or this note.

Primary text inspection and the displayed author proof are not independent
mathematical review. Audit especially the full mild pressure identification,
all-center pressure bound, suitable singularity persistence, fixed-axis
blow-down, and the direction of the record-time inequalities in (7.4)--(7.6).
No mathematical certification is inferred from symbolic or repository checks.
