# Smooth principal inversion does not solve the connected history problem

Date: 2026-09-08. Research input: ececd70fc6115318f78a2aca121254952d59529c.
Integration preserves 373bd3e0504df775434ad579607ded9481af624f.
Status: AUTHOR PROOFS, independent mathematical audit pending. No priority claim.
These are exact principal differential-operator results, NOT a full original-NS
inverse, autonomous Cauchy realization, or blowup construction.

## 0. Consumer and the first issue found

The preceding mixed-trace theorem controls values on each regular principal
fiber. It explicitly does not control slow-parameter derivatives or matching
between fibers. UE1/UE2 would need both. Clamping a zero of the growth rate to
an endpoint is not a smooth operation on parameters: even with smooth
coefficients, the resulting inverse can fail to be differentiable.

Section 1 proves a replacement with the same sharp order of value bound,
all fixed-order parameter derivatives, and no turning-point selection.
Section 2 extends it to the full nonzero-harmonic principal family. Section 3
then tests connected principal histories and proves that the local inverse
bound does NOT compose across two growth/decay pulses, even with a completely
free initial value. Independent pulse traces remain genuine constraints.

The exactification consumer would be:

    smooth fiber inverse + globally compatible common Cauchy trace
      + controlled mean/transverse equations and all inter-pulse products
      -> uniform full-PDE inverse -> convergent nonlinear correction
      -> one Schwartz datum and a preserved singularity.

Only the first item is proved here. The connected-history obstruction is
not a proof that the required specific trace array is unrealizable.

## 1. A root-free inverse with smooth parameter dependence

Let I=[0,L], L>=1, a real and C1, and assume

    a'(v) <= -kappa/L,  kappa>0.                              (1.1)

Set D_a=partial_v-a and D_a^*=-partial_v-a. Let h be the positive
homogeneous solution D_a h=0, normalized to have maximum one on I.

### Theorem 1 (least-norm inverse)

For every f in L2(I), there is exactly one x in H1(I) satisfying

    D_a x=f,  integral_I x h=0.                              (1.2)

For complex f use the complex Hilbert pairing. This is the L2-minimum-norm
solution among ALL solutions with arbitrary initial value. Denote it by R_a f.
Then

    ||R_a f||2 <= sqrt(L/kappa)||f||2,                        (1.3)
    ||R_a f||infinity <= 3 sqrt(pi L/(2 kappa))||f||infinity   (1.4)

when f is bounded. The order sqrt(L) cannot be improved uniformly in this
class. For smooth parameter families satisfying (1.1) uniformly, R_a is
smooth in the parameters, including when the zero of a crosses an endpoint.
If coefficient derivatives have polynomial bounds in L, every fixed-order
parameter and v derivative of the inverse has a polynomial bound in L.
This last assertion is local on a regular parameter patch; it does not
assert uniformity at a singular slow-label boundary.

Proof. Use the Dirichlet problem for

    H_a = D_a D_a^* = -partial_v^2+a^2-a',
    H_a y=f,  y(0)=y(L)=0.                                  (1.5)

Its form on H1_0 is coercive:

    <H_a y,y> = ||y'||2^2+||a y||2^2-integral a'|y|^2
               >= (kappa/L)||y||2^2.                        (1.6)

The elementary coercive variational problem gives a unique y; one-dimensional
elliptic regularity gives y in H2. Then x=D_a^*y solves D_a x=f.
Integration by parts, using y=0 at both endpoints and h'=a h, proves x is
orthogonal to h. Any other solution is x+c h, proving uniqueness and the
minimum-norm assertion. Moreover

    ||x||2^2=<f,y>,  ||y||2 <= (L/kappa)||f||2,

which proves (1.3). No boundary data for x have been independently specified.

For (1.4), let v_* be the maximum point of h. The solution x_0 of D_a x_0=f
with x_0(v_*)=0 satisfies the predecessor's oriented Gaussian-kernel bound

    ||x_0||infinity <= sqrt(pi L/(2 kappa))||f||infinity.

That value estimate follows directly from (1.1) by integrating exp[-kappa
(v-s)^2/(2L)] in the stable direction on each side of v_*. It is used only
pointwise in the parameter, not differentiated. Orthogonal projection gives

    R_a f=x_0-h <x_0,h>/||h||2^2.                            (1.7)

The logarithm of h is concave and h(v_*)=1. Therefore
h((v+v_*)/2)^2>=h(v). Changing variables and integrating yields

    integral_I h <= 2 integral_I h^2.

Thus the second term of (1.7) has supremum norm at most 2||x_0||infinity,
proving (1.4), also when the maximum is at an endpoint.

For sharpness take a=-(v-L/2)/L and f=1. The solution x_0 centered at L/2
is odd about L/2, whereas h is even, so x_0=R_a f. For L>=4,

    |x_0(L/2+sqrt(L))| >= exp(-1/2)sqrt(L).

This follows by integrating over a segment of length sqrt(L), on which
the oriented integrating factor is at least exp(-1/2).

For parameter regularity, (1.5) has a fixed Dirichlet domain. Its inverse
satisfies ||H_a^{-1}||_(L2->L2)<=L/kappa. The parameter derivatives of H_a
are multiplication by the corresponding derivatives of a^2-a'. Differentiating
H_a y=f gives, for a multi-index alpha,

    H_a d_theta^alpha y = d_theta^alpha f
       -sum_(0<beta<=alpha) binom(alpha,beta)
           d_theta^beta(a^2-a') d_theta^(alpha-beta)y.       (1.8)

Induction, (1.6), and (1.8) give polynomial L bounds for y and y' at every
fixed parameter order. The identity y''=(a^2-a')y-f gives higher v derivatives.
Finally x=-y'-a y gives the asserted estimates for x. Difference quotients
justify the differentiation at the first step; induction yields smoothness.
All required constants depend only on kappa, the derivative order, and the
stated coefficient bounds, not on the position or existence of a root.
For L depending smoothly on the slow label, pull back to [0,L_ref] first;
a bounded positive length ratio and its polynomially bounded derivatives
preserve the argument. QED.

### An actual nonsmoothness of the old trace choice

Take a_theta(v)=theta-v/L and f=1. For theta<0 the clamped turning point is
zero and x_theta(0)=0. For small theta>0 it is L theta and

    x_theta(0)=-integral_0^(L theta) exp(-theta s+s^2/(2L)) ds.

The left parameter derivative at theta=0 is zero, the right derivative is
-L. Thus differentiating the old clamped trace is not legitimate in general.
The preceding value theorem was not false: it expressly made no such
parameter-derivative claim. The root-free inverse repairs this extension.

## 2. The full principal family, with fixed-order parameter derivatives

Consider the source's two-component principal equations in a regular moving
frame, as in [OA, (7.17)] and the preceding evidence note:

    z_m'=[diag(lambda,-lambda)+E-m^2 d I]z_m+g_m, m!=0,
    lambda=lambda0/sqrt(1+y^2),
    d_ref=lambda0(1+y^2)/(1+u_*^2)^(3/2),
    y=u_*/2+u_*v/L.                                         (2.1)

Assume lambda0,u_* lie in fixed compact subsets of (0,infinity),
||E||infinity+||d-d_ref||infinity<=C/L, and all needed v and parameter
derivatives of the pulled-back coefficients are polynomially bounded in L.
Those are hypotheses on a REGULAR patch, not a claim of a uniform bound
through every source collar or every changing global label.

### Theorem 2 (smooth all-harmonic principal right inverse)

There exist fixed m0,L0 and C such that for L>=L0 these equations have a
linear right inverse with

    ||z_m||infinity <= C sqrt(L)||g_m||infinity  (m!=0),
    ||z_m||infinity <= C m^(-2)||g_m||infinity   (|m|>=m0).  (2.2)

The choice for |m|<m0 is the pair of conditions

    integral z_(m,+) h_(a_m)=0,  z_(m,-)(0)=0,
    a_m=lambda-m^2 d_ref;                                  (2.3)

for high harmonics it is z_m(0)=0. This selection is smooth in all the
regular slow parameters, without switching conditions when a root crosses
an endpoint. For every fixed parameter order alpha and v order j there
are C_(alpha,j),N_(alpha,j), independent of m,L, such that

    ||d_theta^alpha partial_v^j z_m||infinity
      <= C_(alpha,j) L^N_(alpha,j) (1+|m|)^(2j)
           sum_(beta<=alpha, k<=j)
                ||d_theta^beta partial_v^k g_m||infinity.   (2.4)

Consequently any fixed harmonic-weighted l1 family with the corresponding
finite input sums has an all-order principal inverse. Flatness in Q remains
flat at each fixed derivative order when L is comparable to log(1/Q)^2.
No transverse PDE is solved by treating a transverse coordinate as a parameter.

Proof. Direct differentiation gives a_m'<=-kappa0 m^2/L and
b_m=-lambda-m^2 d_ref<=-m^2 d0 for uniform positive kappa0,d0.
On the finite low-harmonic range use diag(R_(a_m),T_(b_m)), where T_b is
the ordinary zero-left-trace inverse for b<=-d0. Its supremum norm is O(sqrt L).
Absorb -m^2(d-d_ref) into E; on this fixed finite range its norm is O(1/L).
The Neumann series converges in C(I;C2) for all L>=L0. It imposes precisely
(2.3), proves (2.2), and is smooth because Theorem 1 is smooth.
Differentiate the Neumann equation; the baseline inverse and all its fixed
parameter derivatives have polynomial bounds from Theorem 1 and the stable
variation-of-constants formula. Inverting I-T E at every step costs at most
2. This proves polynomial derivative estimates in the low range.

For the infinite high range do NOT perturb by an unbounded m^2/L error.
Use d>=d0/2 and choose m0 so the Hermitian part of the EXACT matrix in (2.1)
is <=-d0 m^2/4. Its forward propagator is then bounded by
exp[-d0 m^2(v-s)/4]. This proves the second estimate in (2.2).
A parameter derivative solves the same zero-left-data equation with source
consisting of a derivative of g_m plus coefficient derivatives times lower
parameter derivatives of z_m. Each differentiated coefficient costs at most
m^2 times a polynomial in L. The propagator integral gains m^(-2), and
induction shows that every parameter derivative of z_m is bounded by
C_alpha L^N_alpha m^(-2) sum_(beta<=alpha)||d_theta^beta g_m||infinity.
Finally use the differential equation repeatedly for v derivatives; each
such step loses at most a factor (1+|m|)^2 and a polynomial in L. This proves
(2.4). Summation against any fixed nonnegative harmonic weights is justified
by the displayed absolute bounds. Conjugate inputs at m,-m give conjugate
outputs since the frame and the trace conditions are real. QED.

The algebraic normal equation reconstructs the principal pressure, exactly
as in the predecessor's (3.8)-(3.9). Its denominator is i k m |n_Phi|^2.
On the stated regular patch this preserves the same type of fixed-order
bounds, with the explicit 1/(k|m|) factor at value level. This is not yet
the canonical whole-space pressure for a completed NS solution.

For a SCALAR homogeneous Gaussian pulse h, cutoff a=psi h and residual
r=psi' h, the minimum-norm correction of -r is

    w=(1-psi)h-c h,
    c=integral(1-psi)h^2/integral h^2.                       (2.5)

Thus a+w=(1-c)h. If the cutoff derivatives occur a distance comparable to
L from the pulse maximum, and h has two-sided Gaussian envelope bounds,
0<=c<=C sqrt(L)exp(-c0 L). The denominator is at least c1 sqrt(L), by the
lower envelope bound near the maximum. The pulse is preserved up to an
exponentially small amplitude change. The full coupled two-component system
is covered by (2.2), but an exact scalar formula such as (2.5) is NOT asserted
for an arbitrary matrix E or arbitrary prescribed whole-PDE covariance.

## 3. Continuing after the positive result: two connected pulses defeat it

### Theorem 3 (no small free-data inverse over a connected two-pulse history)

There is a smooth scalar coefficient a_L on [0,L], uniformly bounded with
all fixed-order derivative bounds polynomial in L, and a source g_L flat
at every algebraic Q order when L=ell^2, Q=2^-ell, such that EVERY solution
of z'-a_L z=g_L, even with completely unrestricted initial value, satisfies
||z||infinity>=1/2. Meanwhile ||g_L||C^k<=C_k L^N_k exp(-L/2).
Hence no right inverse with fixed polynomial Q loss exists on all such
connected histories. This is NOT a theorem about all possible coupled NS
histories or a claim about the monodromy of the source's actual construction.

Proof. Set

    h_L(v)=exp[-L cos^2(2 pi v/L)],
    a_L=h_L'/h_L=2 pi sin(4 pi v/L).                         (3.1)

Choose a fixed smooth chi(s), zero for s<=3/8 and one for s>=5/8, and put

    z_0(v)=chi(v/L)h_L(v),
    g_L(v)=L^(-1)chi'(v/L)h_L(v).                           (3.2)

On the support of chi', cos^2(2pi v/L)>=1/2, so g_L and every fixed-order
derivative have the displayed exponentially small bound. The first and
second maxima of h_L, at L/4 and 3L/4, both have value one. All solutions
of the inhomogeneous equation are z=z_0+c h_L, c in C, and hence

    z(L/4)=c,  z(3L/4)=1+c.                                 (3.3)

The triangle inequality implies max(|c|,|1+c|)>=1/2. This proves the lower
bound. The source is raw-flat because exp(-ell^2/2) dominates every fixed
power of 2^-ell, including any fixed derivative loss. Near each peak,
a_L' is negative of order 1/L; between them it becomes positive. Thus the
single-turning-point theorem applies locally but its hypothesis fails on
the connected history. There is no contradiction between Theorems 1 and 3.
The same example embeds diagonally in a two-component system with a damped
second component. Its free homogeneous initial value does not cure (3.3).
QED.

More generally, wherever h!=0 the EXACT compatibility identity is

    z(t2)/h(t2)-z(t1)/h(t1)=integral_t1^t2 g(s)/h(s) ds.     (3.4)

For N peaks in one homogeneous scalar channel, one initial constant fixes
all homogeneous peak amplitudes; N-1 independent differences are fixed by
(3.4). Separate small inverses choosing each peak value independently do
not solve this one connected problem. Different actual NS angular channels,
nonlinear transfer between them, and infinite-dimensional initial data can
change the compatibility problem; none is excluded by this scalar theorem.

## 4. Decision after the follow-through

The principal slow-parameter issue is repaired on regular patches. The
connected-history test is negative, even after freeing the initial trace.
Do not spend the next run merely adding formal orders to independent pulse
inverses. Determine the common-data compatibility of the ACTUAL coupled
mean, transverse, exterior and pulse system, allowing geometry changes.
A specific compatible nonlinear orbit, not surjectivity for arbitrary arrays,
is sufficient. Finite-list solutions with uncontrolled common-data norms,
independent late resets, or density of a linear trace range do not supply it.

No full-PDE inverse, input-only RF-q producer, hypothetical-blowup extraction,
certified positive regenerative turnover or NS-R3 resolution is proved here.

## Source inspection and checks

[OA] OpenAI, Finite Time Blowup for Navier--Stokes, supplied CDN PDF,
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Inspected (7.14)-(7.20), including the rendered printed p.78. The retrieved
PDF now has 166 physical pages; previous repository provenance says 165.
The forced theorem is accepted as requested by the owner. No claim of a new
independent source-proof or Lean audit is made. The new inverse proofs above
are self-contained; the operator factorization/minimum-norm method is
classical. Novelty is asserted only relative to the repository, not literature.
The exact checker tests identities and finite algebra, not the analytic
estimates, countable convergence, or a numerical Navier--Stokes trajectory.
