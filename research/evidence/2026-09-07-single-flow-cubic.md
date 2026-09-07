Controller-retained worker snapshot, 2026-09-07. Original worker file: single-flow-cubic.md;
SHA256 `6cb8cff951460069d49d194eb136f87b83af1c77c1af359bc490b97db4327eec`.
Author derivation with independent mathematical audit PENDING. This
record is evidence for further research, not an established graph theorem.
The original worker text follows unchanged. PLAN alone allocates work.

# One-flow cubic band balance: exact cancellation and the remaining clock

Date: 2026-09-07. Worker evidence; author derivation, audit pending.
Repository base: `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
The earlier `critical-output.md` remains frozen and unmodified.
No canonical status, source claim, manuscript or formalization is changed.

## 1. Scope

Consider ONE actual whole-space spectrally projected unforced NS flow U_N,
with orthogonal spherical cutoff P_N commuting with derivatives and Leray:

    U_t + P_N P_Leray[(U.grad)U] = nu Delta U,
    P_N U = U, div U = 0.

The algebra below holds for sufficiently regular L2 trajectories, including
the strong bandlimited trajectories of the root's whole-space model. Fix
lambda_k=2^k N0 and use the sharp orthogonal shells

    u_k = Delta_k U,  lambda_k/2 < |xi| <= lambda_k,
    L_k = ||u_k||_2,  a_k=lambda_k^(1/2)L_k,
    W = sum_(k in Z) a_k^3.

The previously derived sharp-shell inequality gives ||U||_3^3 <= C W.
Only an input-only bound for W uniformly in N would be terminal progress.
For any fixed J the low part has the immediate energy bound

    sum_(k<=J) a_k^3 <= lambda_J^(3/2)||U||_2^3.

Thus the low coarse term introduces no new critical obligation. For
projected Schwartz input, W_N(0) <= W(u_initial) < infinity uniformly in N.

## 2. Exact nonlinear variational multiplier

Set

    w_k = lambda_k^(3/2)L_k = lambda_k a_k,
    A_U = sum_k w_k Delta_k,
    D_exact = sum_k lambda_k^(3/2)L_k ||grad u_k||_2^2.

Then

    (1/3) W' + nu D_exact = -b(U,U,A_U U) =: F,              (1)
    b(a,b,c)=integral (a.grad)b . c.

Indeed (1/3)d L_k^3/dt=L_k<d_t u_k,u_k>. The derivative at L_k=0 is
zero, so the formula does not divide by an unproved nonzero band norm.
The state dependence of A_U is already accounted for by this derivative:
there is no omitted time derivative of a proposed quadratic metric.
The Leray and outer P_N disappear from this pairing because A_U U is
solenoidal and belongs to the same cutoff space as U.

The transport operator T_U=U.grad is skew in this real L2 pairing. Thus

    F = -(1/2)<U,[A_U,T_U]U>
      = -(1/2) sum_(p,q,k) (w_k-w_q)b(u_p,u_q,u_k).         (2)

Equation (2) is the exact cancellation obtained by subtracting equal triad
weights. It includes every Leray-compatible interaction of the actual
single field; it is not a comparison-flow estimate. The Fourier supports
restrict every nonzero summand to triangles whose two highest frequencies
are comparable. But even for neighboring shells the difference w_k-w_q
contains L_k and L_q, so comparable wavevector lengths do not make that
difference small or give it a sign. Low frequency transport across a sharp
shell boundary is part of [A_U,T_U]; it has not been discarded.

At a finite upper cutoff all displayed sums converge: the low-frequency
Bernstein factors are geometric, and Cauchy--Schwarz controls the low L2
coefficients. One may alternatively prove (1)--(2) with finitely many
lower shells removed and pass to the low-frequency limit in these bounds.

The exact diffusion controls the critical weighted dissipation

    D_exact >= (1/4) D,
    D = sum_k lambda_k^2 a_k^3.                             (3)

## 3. A complete cutoff-uniform upper estimate

Write G=||grad U||_2^2. A direct bound on the exact remaining term is

    |F| <= C G^2.                                         (4)

The proof does not require an L3 multiplier bound for sharp projections.
For each shell, Fourier inversion and interpolation give

    ||u_k||_3 <= C_B lambda_k^(1/2)L_k,
    C_B = [(2pi)^(-3/2)(4pi/3)^(1/2)]^(1/3).

Consequently

    ||A_U U||_3
      <= sum_k lambda_k^(3/2)L_k ||u_k||_3
      <= C_B sum_k lambda_k^2 L_k^2
      <= 4 C_B G.

Let S be a valid vector Sobolev constant in ||U||_6 <= S||grad U||_2;
the existing project lemma gives S=sqrt(3) C_S in its scalar-constant
notation. Holder then gives

    |b(U,U,A_U U)|
      <= ||U||_6 ||grad U||_2 ||A_U U||_3
      <= 4 S C_B G^2.

The Sobolev input is the existing H1(R3) vector-field result in
`research/evidence/cp02-energy-enstrophy.md`, `lem:sobolev`, with its
recorded density extension and inspected source ledger; no new literature
interface is asserted here. Constants are independent of N, N0, time,
amplitude and nu. In particular,

    W(t) + 3nu integral_0^t D_exact
      <= W(0) + 12 S C_B integral_0^t ||grad U||_2^4.        (5)

This is an actual universal upper estimate, but it is not an arbitrary-data
critical bound: energy supplies only

    2nu integral_0^H G <= ||U(0)||_2^2,

not a uniform bound on integral G^2. All cutoff dependence has been removed
from (5); the missing temporal integrability has not been removed.

For comparison, the standard enstrophy inequality has G' <= C nu^(-3)G^3.
At positive G it bounds (log G)' by the same unbounded G^2 clock. Thus (5)
returns to the existing enstrophy obstruction, expressed through a weaker
critical spatial norm. It must not be counted as a second independent
producer or as an improvement in temporal integrability.

## 4. Exact high-low sharp-boundary test

This tests the specific proposed repair

    |nonlinear W production| <= C ||grad U_low||_infinity W

for a sharp-band cube with C independent of high frequency. The repair is
FALSE in an exact family of full spherical Galerkin NS flows. This does
not refute W bounds, smooth-filter alternatives, or the R3 target.

Use the normalized fixed torus (R/2pi Z)^3 and integer K=2^m, m>=2. Take

    U=(0, A(t) cos x,
           B(t) sin(Ky) + C(t) cos x cos(Ky)).

The field is solenoidal and independent of z. The high component cannot
feed back into the first two components because its advective derivative
is U_3 partial_z. The full nonlinear third component is exactly

    AK B cos x cos(Ky)
      -(AK C/2) sin(Ky) -(AK C/2) cos(2x)sin(Ky).

For a FULL spherical cutoff satisfying

    sqrt(K^2+1) <= N < sqrt(K^2+4),

only the last displayed term is discarded. There are no other nonlinear
modes. Hence the exact projected NS amplitude equations are

    A'=-nu A,
    B'=-nu K^2 B +(AK/2)C,
    C'=-nu(K^2+1)C -AK B.                                 (6)

The normalized shell L2 norms are |A|/sqrt(2), |B|/sqrt(2), |C|/2.
With N0=1, their sharp upper radii are respectively 1, K, 2K. Therefore

    W = |A|^3/(2sqrt(2))
        +K^(3/2)(|B|^3+|C|^3)/(2sqrt(2)).

At a time where A,B,C>0 the nonlinear derivative is

    W'_nonlinear
      = [3 A K^(5/2)/(2sqrt(2))] BC(B/2-C).                 (7)

Choose B=4c, C=c, c>0. If W_high denotes the two high terms of W, then

    W'_nonlinear/W_high = (12/65) AK.                      (8)

But ||grad U_low||_infinity=|A|. Letting K grow proves that the suggested
uniform strain-only bound is false. The ratio of W to W_high tends to one
for fixed A,c, so including the low W term does not rescue the assertion.

All interactions responsible for (7) belong to the same projected field.
The two high frequencies K and sqrt(K^2+1) are separated by a vanishing
relative gap but lie on opposite sides of the sharp radius K. Their band
weights remain distinct. A claimed factor 1/K from the low/high separation
would therefore erase an actual sharp-projector commutator contribution.

There is no hidden instability conclusion: for fixed A and nu, diffusion
at rate nu K^2 dominates this AK transfer at sufficiently large K. Equation
(7) has either sign (vary B/2-C), so the nonlinear part is not a universal
Lyapunov cancellation. At each fixed K, sufficiently large A also makes
the full initial derivative positive despite viscosity. This only rejects
automatic sign and the stated strain-only repair; it does not reject an
input-dependent dissipative estimate.

The torus is used solely to falsify an alleged universal Fourier/Galerkin
algebraic estimate covering this class. No transfer of this test to R3 is
asserted, and no periodic conclusion replaces the original terminal target.

## 5. The first unresolved signed contribution

The smallest exact remaining object in this single-flow formulation is

    -1/2 integral_0^t sum_(p,q,k)
        (lambda_k a_k-lambda_q a_q)b(u_p,u_q,u_k) ds.       (9)

The desired producer must control (9), allowing the exact diffusion (3),
using original input and nu uniformly in cutoff. Discarding its signs gives
(5), hence the same unresolved integral G^2. Equal-weight subtraction
already produced every skew cancellation available at this level; it does
not imply that other nonlinear spacetime information cannot control (9).

The sharp-boundary test says that high-low separation alone cannot replace
the relevant commutator by low strain for this functional. It does not
exclude grouping adjacent sharp shells or using a smooth energy partition
to remove this particular boundary effect. Even after such a repair, the
state-dependent near-diagonal transfer must still be estimated, and the
critical scale concentration is not addressed merely by smoothing filters.

## 6. Handoff

MODE / RESULT: exact single-flow reformulation, a proved cutoff-uniform
upper bound, and a scoped falsifier of a sharp-projector strain estimate.

FIRST GAP: input-only signed control of (9), or another bound for W that
does not require the unbounded squared-enstrophy clock. No such bound was
produced in this period.

SURVIVING CONDITIONAL SUFFIX: uniform W_N implies uniform L3 of the actual
cutoff flow; root's local classical identification and banked continuation
then close the unchanged terminal target.

NEXT DISTINCT ACTION: a smooth energy partition can test whether its
commutator removes the certified sharp-boundary effect. The main producer
must then use signed temporal transfer beyond absolute triad estimates;
repeating an absolute bound yielding integral G^2 is the same mechanism.

NON-CLAIMS: no NS regularity proof, no new integrability of G, no independent
audit, no novelty claim for Besov estimates, no rejection of all spectral
or single-flow methods, and no inference from this periodic test to R3
singularity behavior.
