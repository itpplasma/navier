# Restarted causal reconstruction and unavoidable conditioning in closed feedback

Date: 2026-09-07. Parent proof checkpoint:
`d8787ff4f65164e6339be673ad9f9646cd15bd37`.
Status: author derivation; independent mathematical audit pending.
NS-R3 and RF3/RF4 are NOT proved. No strict singularity reduction or novelty claim.
This is a repair and cost analysis of the closed-feedback test, not a claim
that an unbounded-dimensional fluid has a finite three-mode description.

## 0. Exact objective and the successful part

The companion `2026-09-07-closed-feedback-and-causal-radius.md` derives, from
full spherical Galerkin NS in its stated cutoff window, the normalized system

    x'=-x+yz,   y'=-4y-xz,   z'=-5z+xy.                    (0.1)

Real solutions are globally bounded by the energy
E=x^2+4y^2+3z^2, E'<=-2E, while a single zero-centered homogeneous causal
series has finite amplitude radius. The proper repair is not more terms in
that divergent series. The first theorem below constructs a finite sequence
of convergent causal charts for every real datum, with explicit remainder.
The second part proves that closed normal feedback can require EXPONENTIAL,
not merely polynomial, amplification/metric cost in the input amplitude.

The final section carries the restart argument to full finite-dimensional
Galerkin NS with every coupled mode retained. Its constants are explicit but
deteriorate with cutoff; this is where the attempted terminal proof stops.
A diverging upper bound is NOT an impossibility proof for the desired sharper
estimate. Only the two precisely stated branches below are pruned.

## 1. Finite causal restart for every real input of the coupled block

Write u'=-Du+B(u,u) as in the companion proof. For a prescribed local datum
v and local time tau, define

    V_1(tau)=exp(-D tau)v,
    V_n(tau)=sum_(p=1)^(n-1) integral_0^tau exp[-D(tau-r)]
                                          B(V_p(r),V_(n-p)(r)) dr. (1.1)

If ||v||_infinity<=R, the same induction as in the companion gives

    ||V_n(tau)||_infinity
        <= R exp(-tau)[R(1-exp(-tau))]^(n-1).               (1.2)

Let theta=R(1-exp(-tau)). When theta<1, the full series converges, solves
the original Volterra equation, and its order-M remainder satisfies

    ||u(tau)-sum_(n=1)^M V_n(tau)||_infinity
         <= R exp(-tau) theta^M/(1-theta),   M>=1.          (1.3)

No new forcing or time-polynomial truncation replaces the heat kernels.
Resonances and both nonlinear feedback directions occur in (1.1).

**Theorem 1 (global real causal atlas).** Let R0=sqrt(E(u(0))). Every real
solution of (0.1) is reconstructed by at most max(1,ceil(2R0)) causal charts
of the form (1.1), each with theta<=1/2. The last chart covers an infinite
future interval. In each chart the tail is at most

    2 R exp(-tau) 2^(-M).                                  (1.4)

The chart locations are determined by the initial bound R0, not an unknown
future norm. At every finite chart endpoint the next exact datum is the
convergent value of the preceding series. This is a constructive identity
for the real flow; using a finite truncation requires error propagation too.

**Proof.** The real energy law gives ||u(s)||_infinity<=R0 exp(-s). Suppose
a chart starts at s_j with R_j=R0 exp(-s_j). If R_j<=1/2, use it forever:
R_j(1-exp(-tau))<=1/2 for all tau>=0. Otherwise choose

    delta_j=-log(1-1/(2R_j)),   s_(j+1)=s_j+delta_j.         (1.5)

On this chart theta<=1/2, and the bound at the next start is

    R_(j+1)=R_j exp(-delta_j)=R_j-1/2.                      (1.6)

After at most ceil(2R0)-1 finite charts the final case is reached. If R0=0
the solution is zero and one chart is enough. Formula (1.3) gives (1.4).
Convergence on every closed chart and uniqueness join the original ODE
without crossing a convergence boundary. All chart bounds use the proved
real energy identity, never a complex energy norm. QED.

The number of charts is independent of K and of N INSIDE the companion's
invariant window after its viscous/amplitude normalization. It is not a
uniform assertion as N leaves that window and additional modes interact.

## 2. A propagator repair for the entire nonlinear block

Let u and v be real solutions of (0.1), with initial energy bounds R_u^2
and R_v^2. Their difference satisfies the EXACT equation

    (u-v)'=-D(u-v)+B(u+v,u-v).                              (2.1)

The semigroup is contractive at rate at least one in the max norm, and
||B(a,b)||_infinity<=||a||_infinity||b||_infinity. Therefore Volterra Gronwall
and ||u(r)||_infinity+||v(r)||_infinity<=(R_u+R_v)exp(-r) give

    ||u(t)-v(t)||_infinity
      <= exp[-(t-s)+(R_u+R_v)(exp(-s)-exp(-t))]
                                            ||u(s)-v(s)||_infinity. (2.2)

No component is omitted or treated as prescribed external forcing. The
linearized propagator along a real solution with bound R0 obeys

    ||T(t,s)||_(infinity->infinity)
      <= exp[-(t-s)+2R0(exp(-s)-exp(-t))].                  (2.3)

This is genuinely closed-feedback tracking, but only in this finite sector.
The bound depends explicitly on the initial energy and not on an assumed
normal-strain integral. It is exponential rather than polynomial in R0.
It proves that the failure of the single-center series does not rule out
real causal reconstruction or bounded transient propagation.

Equations (1.3) and (2.2) supply explicit propagation of finite truncation
errors between charts. If approximate endpoint data are projected onto the
known real energy ellipsoid at their time, projection is nonexpansive in its
Hilbert norm and cannot increase distance to the exact endpoint. Constants
between that norm and the max norm are fixed in this three-dimensional block.
The projection is an approximation/error-control device, not a change in the
exact equation asserted by Theorem 1. No uniform infinite-level error sum
follows from these finite-dimensional constants alone.

## 3. Real closed feedback forces exponentially large transient amplification

A stronger obstruction than the previously tested one-way transient is
available in the SAME exact Galerkin sector. For A>0, take the exact real
base solution

    u_A(s)=(0,A exp(-4s),0).                                (3.1)

It is also an actual continuum shear before taking variations. Linearizing
(0.1) around it gives the invariant (x,z) perturbation plane

    dot p=-p+A exp(-4s)q,
    dot q=-5q+A exp(-4s)p.                                 (3.2)

Both directions of coupling are present, with positive product. These are
variations of the full Galerkin trajectories: its invariant sector was proved
without deleting any mode below the cutoff. They are not asserted to be an
invariant two-mode linearization of the continuum PDE, where extra modes enter.

Let the initial variation be (p,q)=(1,1). The system is cooperative. Compare
with

    dot w=[-5I+A exp(-4s)J]w,  J=[[0,1],[1,0]],  w(0)=(1,1).

The original generator differs from this one by diag(4,0), a nonnegative
matrix, so componentwise comparison applies. Since the comparison matrices
commute, its exact solution is

    w(s)=exp[-5s+(A/4)(1-exp(-4s))](1,1).                   (3.3)

Thus the Euclidean operator norm of the true propagator obeys

    ||T_A(s,0)||_2 >= exp[-5s+(A/4)(1-exp(-4s))].            (3.4)

At s0=log(2)/4 this becomes

    ||T_A(s0,0)||_2 >= 2^(-5/4) exp(A/8).                  (3.5)

**Theorem 2 (exponential lower conditioning cost).** No polynomial in A
can uniformly bound the amplification of these full coupled perturbations.
Moreover, suppose an absolutely continuous symmetric positive matrix M_A(s)
on [0,s0] makes every solution of (3.2) have nonincreasing M_A energy and
has uniform equivalence bounds

    m_A I <= M_A(s) <= C_A I,   m_A>0.

Then necessarily

    C_A/m_A >= 2^(-5/2) exp(A/4).                          (3.6)

**Proof.** Monotonicity gives
m_A||T_A(s0,0)v||^2 <= C_A||v||^2. Take the operator norm and apply (3.5).
An exponential eventually exceeds any fixed polynomial, proving both claims.
QED.

The theorem allows the metric to depend on A and time, and includes its
actual evolution through the assumed energy law. It does not rely on a
frozen-eigenvalue inference. Smooth parameter dependence of a polynomial
ODE, or direct difference quotients with (2.2), identifies (3.2) with
variations of actual nearby real nonlinear Galerkin trajectories.

The physical energy norm on this plane is a fixed multiple of p^2+3q^2;
replacing the Euclidean norm costs fixed factors and leaves the exponential
lower growth unchanged. s0 corresponds to physical time log(2)/(4nu K^2),
and the base physical speed is proportional to nu K A. The test covers
arbitrarily large dimensionless amplitude, not one fixed R3 datum.

This retires POLYNOMIALLY CONDITIONED universal repairs of the full coupled
block. It does NOT retire all input-controlled metrics: (2.3) permits an
exponential bound, and the theorem does not prove that such costs actually
accumulate along an arbitrary NS singular cascade.

### 3.1 The actual refinement source can excite the same feedback

The exponential lower cost is not restricted to an arbitrarily chosen normal
perturbation. Use coarse cutoff N_c=2K and a fine cutoff in the companion's
window. Prepare BOTH with the same real datum (x,y,z)(0)=(epsilon,A,0).
The coarse solution is exactly

    v_epsilon(s)=(epsilon exp(-s), A exp(-4s), 0).

The fine solution obeys (0.1). The missing coarse-to-fine quadratic source is
EXACTLY

    F_epsilon(s)=(0,0,epsilon A exp(-5s)).                  (3.8)

It is determined by the coarse NS trajectory, not prescribed independently.
At epsilon=0 the fine and coarse flows are the same shear (3.1). Differentiate
the fine flow in epsilon: its (x,z) variation satisfies (3.2) with initial
value (1,0), and its y variation is zero. Comparison with the same commuting
matrix system used above now gives

    q(s)>=exp(-5s) sinh[(A/4)(1-exp(-4s))].                 (3.9)

The high component of the coarse variation is zero. Thus at s0=log(2)/4,

    liminf_(epsilon->0)
       ||u_epsilon(s0)-v_epsilon(s0)||_infinity/|epsilon|
         >=2^(-5/4) sinh(A/8).                             (3.10)

Real differentiability follows by subtracting the two polynomial ODEs on
this finite interval, applying (2.2), and passing the difference quotient;
the quadratic remainder is O(epsilon^2) on the input-controlled compact
energy ball. This is an actual pair of global real Galerkin trajectories.

**Corollary 2a (paired-source lower bound).** If for this faithful pair of
cutoffs, all A>0 and all sufficiently small epsilon an estimate

    ||u_epsilon(s0)-v_epsilon(s0)||_infinity
         <= L(A) integral_0^s0 ||F_epsilon(s)||_infinity ds

holds, then

    L(A)>=5*2^(-5/4) sinh(A/8)/A.                           (3.11)

Indeed the source integral is |epsilon| A(1-exp(-5s0))/5,
which is at most |epsilon| A/5; divide and use (3.10). No polynomial L(A)
can work for arbitrary A. Physical L2 energy/source norms are fixed weighted
versions of these coefficient norms, so only fixed constants change.

This prunes a POLYNOMIAL, source-linear estimate even for the true coarse
residual and fully paired feedback. It does not prune an input-dependent
exponential estimate, a nonlinear source estimate, or RF-SUM on one prescribed
refinement family. At finite epsilon, energy controls the eventual nonlinear
saturation; the derivative lower bound is not a claim of unbounded physical
amplification for a fixed nonzero perturbation. No R3 singularity is asserted.

## 4. The same restart argument for all finite Galerkin modes, with its cost

The previous repair is not inherently limited to three variables. Let H_N
be the full real zero-mean solenoidal space with |k|<=N on the fixed torus,
with its normalized L2 inner product. Let A_N=-Delta and let

    Q_N(v,w)=-(1/2)P_N P[(v.grad)w+(w.grad)v].

Then the FULL system is u'=-nu A_Nu+Q_N(u,u). Put

    m_N=#{k in Z^3:0<|k|<=N},
    c_N=N sqrt(m_N),    R_N=c_N||u_N(0)||2/nu.              (4.1)

Cauchy--Schwarz on Fourier coefficients gives
||v||infinity<=sqrt(m_N)||v||2; Parseval gives
||grad w||2<=N||w||2. Orthogonal projection is contractive, so

    ||Q_N(v,w)||2 <= c_N||v||2||w||2.                       (4.2)

No smooth continuum reference solution is used. For real solutions the exact
energy identity and the fixed-torus mean-zero Poincare inequality give

    ||u_N(t)||2 <= ||u_N(0)||2 exp(-nu t).                   (4.3)

These prove global existence at each finite N by the elementary bounded-ODE
extension argument. In normalized time s=nu t and variable
v=(c_N/nu)u_N, the linear semigroup is contractive at rate one, the bilinear
norm is at most one, and ||v(s)||2<=R_N exp(-s). Consequently Theorem 1's
proof applies word for word in the H_N norm:

**Theorem 3 (all-mode finite-cutoff restart).** Every real finite Galerkin
solution has an exact globally valid causal reconstruction with at most
max(1,ceil(2R_N)) charts, each with the geometric remainder (1.3)--(1.4),
in the normalized H_N norm. Its full variational propagator is bounded by

    exp[-(t-s)+2R_N(exp(-s)-exp(-t))]                       (4.4)

in normalized time. These constants are explicit in the projected datum,
nu, and N. The equations contain every retained nonlinear feedback term.

A finite precision realization can be certified too: use the same chart
locations and truncate each local expansion at degree M; at each finite
endpoint project radially onto the H_N ball of known radius R_N exp(-s).
The exact endpoint lies in that ball, so projection is nonexpansive relative
to it. Applying (4.4) to each real pair and adding local tails shows that,
with J<=max(1,ceil(2R_N)) charts, the piecewise reconstruction satisfies

    sup_(s>=0) exp(s)||v(s)-v_approx(s)||2
        <= 2 J R_N exp(2R_N) 2^(-M).                       (4.5)

For R_N=0 both trajectories are identically zero. For R_N>0, each local tail,
multiplied by exp(s), is at most 2R_N 2^(-M). Subsequent propagation has
at most the factor exp(2R_N) because the integrals of the two input-controlled
amplitude envelopes telescope across chart intervals. Summing over at most
J injections proves (4.5), including intermediate observations in each chart.
The finite approximation need not solve the unmodified ODE exactly; its
residual is controlled by this error theorem, and the M->infinity limit is
the exact equation. No modified equation is substituted into NS-R3.

### Why this is not the desired cutoff-uniform theorem

For N>=1, m_N<= (2 floor(N)+1)^3-1, so c_N is of order at most N^(5/2).
At fixed input L2 norm the resulting sufficient R_N and chart/propagator
bounds deteriorate with N. This is the precise cost of the argument, not a
proof that the actual optimal estimates must deteriorate at that rate.
Improving (4.2) on actual paired refinement errors remains possible and open.
Taking the series order M=M(N) large enough can make the TIME/reconstruction
error (4.5) small at each N. It does not bound the difference of the two EXACT
spatially projected solutions u_N and u_(2N). Their vector fields differ by
precisely the source and feedback in (5.1), which must be controlled separately.

The fixed-torus spectral gap in (4.3) is also load-bearing. It is not uniform
when the box expands to R3. Theorem 3 is therefore a finite-cutoff proof and
repair of analytic reconstruction, NOT a whole-space regularity theorem,
not RF-SUM, and not a proof of a globally finite-dimensional inertial manifold.

## 5. The remaining signed problem, with the full feedback retained

For actual nested Galerkin trajectories U (fine) and v (coarse), w=U-v obeys

    dot w+nu A w+B(v,w)+B(w,v)+B(w,w)=F,
    F=-(I-P_coarse)B(v,v),                                 (5.1)

with all fields embedded in the fine space. w generally contains resolved
corrections too. Its exact energy equation is

    (1/2)d||w||2^2/dt+nu||grad w||2^2
       =<F,w>-integral (w.grad)v.w.                        (5.2)

The all-mode restart theorem replaces an unjustified global analytic series
by a valid real construction, but it estimates precisely the two terms in
(5.2) through a cutoff-dependent bilinear norm. The needed repair at RF3
is stronger: retain their NS-specific correlation and derive a summable
critical error or an equivalent consumed output without the growing c_N.
An unknown future strain integral or metric condition number is not that repair.

The exponential lower bound (3.6) says not to require polynomially cheap
normal contraction of arbitrary trajectories. Corollary 2a goes further:
the TRUE refinement source can excite exponential feedback, so source pairing
alone does not guarantee a polynomial source-linear estimate. The source in
a general refinement sequence need not attain this worst case at every level;
proving how its size, amplification, and nonlinear saturation combine across
levels is still open. A jointly estimated resolved/unresolved block or a
nonlinear cumulative error bound is not excluded. The needed correlation
must be proved on the actual sequence, not assumed from passivity or geometry.

## 6. Frontier verdict and review requirements

MODE / RESULT: FALSIFY then REPAIR. The single-center entire-amplitude branch
fails; finite real causal restart succeeds for every finite Galerkin system.
The polynomial-condition metric and polynomial source-linear subbranches
fail on a fully coupled invariant block, while an explicit exponential real
propagator bound survives.

FIRST GAP: an input-controlled critical estimate for the paired source,
feedback and reconstruction in (5.1), uniform in refinement and large domain.
No bound proving RF-SUM or another terminal output was obtained.

SURVIVING CONDITIONAL SUFFIX: that actual critical bound, plus faithful
consistency/trace/energy/R3 passage and canonical continuation, yields NS-R3.
The causal-radius theorem is NOT placed as a logical prerequisite of NS-R3;
it prunes an attempted proof method only.

NON-CLAIMS: no physical finite-time blow-up, no new singularity class excluded,
no general impossibility for kinetic/symplectic/metriplectic/FEEC methods,
no polynomially bounded optimal costs asserted, no independent audit or Lean
proof. The three-mode calculations are geometric Fourier-model tests with
standard prior art, not advertised as a new physical model.

NEXT DISTINCT ACTION: estimate the actual paired forcing and feedback, rather
than another unforced worst-case normal propagator. A proposed metric must
have a proved input-controlled equivalence constant, and any restart or
resummation must include its interlevel reconstruction cost. Do not repeat
the static-C2, unit-contraction, entire-amplitude, polynomial-condition or polynomial-source-linear
premises now defeated in their exact stated classes.

All calculations are printed here and in the companion. Sources and historical
scope are in its Section 5. Regression checks are finite exact algebra only.
Independent review should first check the comparison in (3.3), the metric
condition-number implication, the normalization in (4.1)--(4.4), and the
finite-precision restart propagation in (4.5). No terminal node is promoted.
