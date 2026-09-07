# Smooth-block transport repair on the unchanged projected NS equation

Date: 2026-09-07. Base ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df.
Author derivation with audit-requested scope repairs. Exact review inputs
and current verdict are recorded in 2026-09-07-smooth-block-audit.md.
Scope: full R3 Fourier-ball NS flow U_N, or the canonical classical branch
before its maximal time. No generic external advector is substituted.

## 1. Smooth blocks and the exact sixth-power functional

Fix a real radial nonincreasing smooth cutoff chi, equal to one on |xi|<=1
and zero on |xi|>=2. Put phi(xi)=chi(xi)-chi(2xi), lambda_k=2^k lambda_0,

    Delta_k=phi(D/lambda_k),  S_m=chi(D/lambda_m),
    u_k=Delta_k U,  L_k=||u_k||_2,  a_k=lambda_k^(1/2)L_k.

Then sum_k Delta_k=I on L2, each block is supported in
lambda_k/2 <= |xi| <= 2lambda_k, and S_m=sum_(j<=m)Delta_j.
The blocks overlap and are not orthogonal projections. All estimates below
have constants depending on this one fixed cutoff profile, not N or k.

Set q=6 and

    W=sum_k a_k^6,
    gamma_k=lambda_k^3 L_k^4=lambda_k a_k^4,
    A_U=sum_k gamma_k Delta_k^2,
    D_exact=sum_k gamma_k||grad u_k||_2^2,
    D=sum_k lambda_k^2 a_k^6.

Delta_k^2, rather than Delta_k, is necessary in A_U. For the actual equation

    U_t - nu Delta U + P_N P_Leray[(U.grad)U]=0,
    P_N U=U, div U=0,

the exact identity is

    (1/6)W' + nu D_exact = -b(U,U,A_U U),                   (1)
    b(a,b,c)=integral(a.grad)b . c,
    D_exact >= D/4.

This follows from (1/6)d||u_k||_2^6/dt=L_k^4<d_tu_k,u_k>.
It includes zero-norm blocks and the state dependence of gamma_k exactly.
There is no omitted derivative of a moving quadratic metric.

Because A_U U is both solenoidal and in the cutoff range, the outer Leray
and P_N projections disappear from the TESTED pairing in (1). This is not
a claim that those projections disappear from the block equations.

At a finite cutoff the positive-frequency end has only finitely many
nonzero blocks. Low-frequency sums converge using the geometric lambda_k
weights and L2. The classical continuum version follows on compact smooth
intervals from the same summations and high Sobolev bounds.

## 2. Keep the complete output-projection correction

Fix k and let

    V_k=S_(k-6)U,  H_k=U-V_k,
    C_k=[Delta_k,V_k.grad]U,
    R_k=Delta_k(H_k.grad U),
    Q_N=P_N P_Leray.

These are parts of the same actual field. In particular V_k is solenoidal.
The exact block equation, with no cutoff-interior assumption, is

    (d_t-nu Delta)u_k + V_k.grad u_k
      = -Q_N(C_k+R_k) + (I-Q_N)(V_k.grad u_k).             (2)

The last term retains the output-projection correction, including its
pressure component. It need not vanish pointwise, including when the
block crosses the cutoff boundary. However,

    <(I-Q_N)(V_k.grad u_k),u_k>=0,
    <Q_N(C_k+R_k),u_k>=<C_k+R_k,u_k>,
    <V_k.grad u_k,u_k>=0.

Here Q_N is the orthogonal projection onto the cutoff solenoidal subspace,
and u_k belongs to that subspace. Therefore the tested equation gives

    (1/6)d a_k^6/dt + nu gamma_k||grad u_k||_2^2
      = -gamma_k<u_k,C_k+R_k>.                            (3)

Equations (2)--(3) prove that the ensuing ENERGY estimates are uniform
even for blocks meeting |xi|=N. A pointwise transport equation obtained by
deleting the last term in (2) would be false. No modified equation or
cutoff adapter is used here.

## 3. The smooth commutator gives the missing low-strain gain

The Fourier support of V_k lies in |xi|<=lambda_k/32. Choose a fixed finite
block enlargement u_k^*=sum_(|j-k|<=4)u_j. Frequency support and the
partition identity show

    C_k=[Delta_k,V_k.grad]u_k^*.

For example, the first commutator term can only see input frequencies in
[15lambda_k/32,65lambda_k/32], while the second sees Delta_k U. The chosen
enlargement equals the identity throughout these frequencies.

Let K_k be the convolution kernel of Delta_k. Integration by parts and
div V_k=0 give exactly

    [Delta_k,V_k.grad]f(x)
      = integral grad K_k(y) . (V_k(x-y)-V_k(x)) f(x-y) dy.

The mean-value estimate and scaling of the Schwartz kernel yield

    ||C_k||_2
      <= C_phi ||grad V_k||_infinity ||u_k^*||_2
      <= C_phi ||grad V_k||_infinity sum_(|j-k|<=4)L_j.     (4)

Indeed integral |y||grad K_k(y)|dy is independent of k. This is the
specific repair of the sharp-projection obstruction: no factor lambda_k
times ||V_k||_infinity remains.

Next split R_k exactly as

    R_k=Delta_k(H_k.grad V_k)+Delta_k(H_k.grad H_k).

In the first term only the same fixed enlargement of H_k can contribute,
so its L2 norm is at most

    C_phi ||grad V_k||_infinity sum_(|j-k|<=4)L_j.          (5)

Combining (4)--(5), the low-frequency strain contribution to (3) is bounded
by

    C_phi ||grad V_k||_infinity
                    a_k^5 sum_(|j-k|<=4)a_j,              (6)

with the harmless adjacent lambda ratios included in C_phi. This is
uniform in N, including the cutoff-crossing blocks by Section 2.

## 4. Remaining high-pair transfer and its frequency gain

The remaining signed term is kept as

    T_k = <u_k,Delta_k(H_k.grad H_k)>.

Since H_k is solenoidal, H_k.grad H_k=div(H_k tensor H_k).
The L1-to-L2 norm of the derivative convolution kernel is C_phi lambda_k^(5/2).
Decompose H_k=sum_(j>k-6)u_j. Frequency triangles show that the contributing
input pairs have both indices at least k-C0 and their indices differ by
at most C0, where one may fix C0=12. Therefore

    ||Delta_k(H_k.grad H_k)||_2
      <= C_phi lambda_k^(5/2)
           sum_(j>=k-C0) L_j sum_(|i-j|<=C0)L_i.           (7)

This includes genuinely high-high-to-low output; it is not replaced by a
near-output interaction. Multiplication by gamma_k L_k gives

    gamma_k |T_k|
      <= C_phi lambda_k^2 a_k^5
           sum_(j>=k-C0) 2^(k-j) a_j a_j^*,              (8)
    a_j^*=sum_(|i-j|<=C0)a_i.

The factor 2^(k-j) is an actual summable output-frequency gain for pairs
well above the output. At comparable indices, (8) has size lambda_k^2 a^7.
The corresponding diffusion has size nu lambda_k^2 a^6. Thus the
scale-local critical amplitude a/nu remains at comparable frequencies.

All the vector products in (7) are the actual NS products. Pressure was
eliminated only in the solenoidal pairing; incompressibility supplied the
derivative on the low output. No scalar interaction is assumed to replace
the Leray geometry.

## 5. Smooth transport and comparable-scale production

Bernstein for the actual low part gives

    ||grad V_k||_infinity
      <= C_phi sum_(l<=k-6) lambda_l^2 a_l.

After the finite-neighbor Holder bounds, the sum of (6) is consequently
bounded by a constant times

    sum_k lambda_k^2 a_k^6
                   sum_(l<=k+C0) 2^(2(l-k)) a_l.          (9)

This low-frequency kernel has TWO powers of the separation. The sharp
block estimate without the commutator gain had only one. For the earlier
low shear with amplitude A and frequency one acting on frequencies K,
the new low transport coefficient is O(A), rather than O(AK). This is a
real removal of that specific boundary obstruction.

For completeness, let A=max_k a_k. Equations (8)--(9) give

    |b(U,U,A_U U)| <= C_phi A D.                          (10)

For (8), bound one of its two high amplitudes by A and use
a_k^5 a_i <= (5/6)a_k^6+(1/6)a_i^6. Summing the geometric kernel and
the fixed index-neighbor ranges places both terms under C A D. Equation
(9) is immediate from the summable kernel. This supplies a complete
uniform estimate, but arbitrary amplitude does not make C A less than nu.

The exact signed total still has the form

    -b(U,U,A_U U)=-(1/2)<U,[A_U,U.grad]U>.                 (11)

Its instantaneous multiplier has a symbol smooth on R3 minus {0},
with the uniform annular kernel estimates proved above:

    m_U(xi)=sum_k gamma_k phi(xi/lambda_k)^2.

For low advecting frequencies, differences of this symbol have the
mean-value gain proved in Section 3. At comparable frequencies its
gamma_k=lambda_k a_k^4 coefficients retain state-dependent differences;
the mean-value argument supplies no small parameter there. Equation (11)
retains their signs, while (10) discards them. No sign for (11) or
input-only temporal control of its comparable-frequency part is proved.

## 6. Independent comparison with the existing energy clock

A short direct bound makes the lack of a new temporal producer explicit.
Let G=||grad U||_2^2. Finite overlap and the annular support give

    sum_k lambda_k^2 L_k^2 <= C_phi G.

Bernstein, the L2 contraction of Delta_k, and gamma_k=lambda_k a_k^4 give

    ||A_U U||_3
      <= sum_k gamma_k ||Delta_k^2 U||_3
      <= C_phi sum_k lambda_k a_k^5
      <= C_phi A^3 G.

Hence the existing vector Sobolev inequality and Holder imply

    |b(U,U,A_U U)| <= C_phi A^3 G^2 <= C_phi W^(1/2) G^2.

From (1), regularizing sqrt(W) at zero if necessary,

    sqrt(W(t)) <= sqrt(W(0)) + C_phi integral_0^t G(s)^2 ds. (12)

Thus this absolute estimate returns to precisely the squared-enstrophy
clock already encountered for the sharp cubic norm. Energy controls
integral G, not integral G^2. Smoothing repairs the certified boundary
loss but does not itself improve this temporal integrability.

Under dyadic NS dilation, or simultaneous dilation of the dyadic grid,
W is invariant and D and nonlinear production scale quadratically. For
arbitrary continuous dilation with a fixed grid the resulting Besov norms
are equivalent, not necessarily equal. Precisely, for U_r(x)=r U(r x),
W_(lambda_0)(U_r)=W_(lambda_0/r)(U). The seventh amplitude degree of the
nonlinear W derivative matches a times the sixth-degree diffusion. Treating the trilinear flux alone as the full
degree of W' would drop the state-dependent fourth-power weights.

## 7. Handoff

PROVED REPAIR: smooth-block low transport is controlled by low strain with
a cutoff-uniform kernel bound; the extra separation factor is genuine.
The projection correction is retained in the equation and vanishes only
in the exact energy pairing, even at the cutoff boundary.

FIRST GAP: signed spacetime control of the remaining comparable-frequency
portion of (11), together with its high-pair tail (8), at arbitrary critical
amplitude. Its absolute estimate is (10) or (12), not a terminal producer.

STRUCTURAL PAYOFF: the earlier sharp-shell low-strain falsifier does not
obstruct this repaired functional. The new information is one additional
power of frequency separation in low-high transport. No new sign or
temporal budget has been obtained for interactions at comparable scales.

NEXT DISTINCT ACTION: exploit actual signed comparable-frequency transfer
or another trajectory constraint. Repeating absolute bounds that end at
A D or integral G^2 would revisit the same unresolved critical quantity.

NON-CLAIMS: no critical producer or NS-R3 conclusion, no modified
equation, no cutoff-interior restriction hidden in a
uniform claim, and no inference of small amplitude from fine resolution.
