# A grade-`N` quadratic collar pressure requires a grade-`N/2` ancestor

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@be1fdc2d02a6e68fbe8f02e25e8ef35341b83be8`.

**Status: exact angular-convolution theorem plus quantitative `L^1` stress estimate and an exact noncancellation symbol example. Independent mathematical audit and novelty assessment pending.** This packet does not construct a physical collar mechanism. It determines what angular content any such direct quadratic-pressure mechanism must already possess.

## 1. Prediction before the test

The sparse-collar criticality theorem leaves an exponentially sparse energy window. A possible escape would be that low-complexity collar velocity creates the high parent harmonic nonlocally through pressure.

Prediction: quadratic angular arithmetic forbids that bootstrap. To create pressure grade `N`, at least one velocity factor must already have angular grade at least `N/2`. However incompressibility itself should not annihilate such a cross interaction once the required ancestor exists.

## 2. Exact angular ancestry

Let `Pi_m` be the standard rotation-Fourier projection around the source axis and decompose

    u = sum_(m in Z) u_m.                                 (2.1)

For fixed integer `N>=1`, define

    u_L = sum_(2|m|<N) u_m,
    u_H = u-u_L.                                          (2.2)

Angular grades add under tensor products. If `2|m|<N` and `2|l|<N`, then

    |m+l| < N.                                            (2.3)

Hence exactly

    Pi_(+/-N)(u_L tensor u_L)=0.                          (2.4)

For an axisymmetric collar cutoff `chi`, which preserves angular grade,

    Pi_N[chi u tensor u]
      = Pi_N[chi(u_H tensor u + u_L tensor u_H)].         (2.5)

Thus every grade-`N` quadratic stress term has at least one velocity ancestor of angular grade `|m|>=N/2`.

This is independent of radial support, amplitude, viscosity and the pressure kernel.

## 3. Quantitative stress and pressure consequence

The angular projector is an `L^1` contraction by its group-average definition, and `0<=chi<=1`. Therefore Cauchy--Schwarz gives

    ||Pi_N(chi u tensor u)||_1
      <= ||u_H tensor u||_1 + ||u_L tensor u_H||_1
      <= 2 ||u_H||_2 ||u||_2.                            (3.1)

For a classical unforced branch with initial energy `E0`,

    ||u||_2 <= E0^(1/2),                                  (3.2)

so

    ||Pi_N(chi u tensor u)||_1
      <= 2 E0^(1/2) ||u_H||_2.                            (3.3)

Rotation equivariance of the Newton/Leray pressure operator means the existing separated collar estimate can be applied to this grade alone. If its grade-`N` operator norm is `K_N(r,R)` and a direct pressure signal of size `A_N` is required, then necessarily

    ||u_H||_2 >= A_N/[2 E0^(1/2) K_N(r,R)].               (3.4)

At the pressure-allowed source collar from the preceding packet,

    A_N = exp[-C L+o(L)],
    K_N = exp[-(kappa/2)L+o(L)],                          (3.5)

so (3.4) only forces

    ||u_H||_2
      >= exp[-(C-kappa/2)L+o(L)] / [2 E0^(1/2)].          (3.6)

For `kappa<2C` this ancestor norm is exponentially small. Thus angular ancestry is a structural requirement, not by itself a critical-norm obstruction.

## 4. Incompressibility gives no universal pressure-symbol cancellation

A negative collar theorem cannot simply assert that divergence-free factors have zero quadratic pressure coupling. Consider the exact Fourier data

    p=(1,0,0),       a=(0,1,0),
    q=(0,1,0),       b=(1,0,0).                           (4.1)

Then

    p.a=0,      q.b=0,                                    (4.2)

so each wave is divergence free. For `k=p+q=(1,1,0)`, the symmetric cross stress has pressure numerator

    2(k.a)(k.b)=2,                                        (4.3)

while `|k|^2=2`. With the usual pressure sign its scalar coefficient is exactly

    -1.                                                    (4.4)

Therefore the divergence-free quadratic pressure symbol is genuinely nonzero once appropriate angular/frequency ancestors are present.

## 5. Frontier consequence

The direct collar-pressure mechanism cannot create a source parent of angular grade `N` from a velocity field whose entire angular spectrum lies strictly below `N/2`. It must inherit or first generate a high-grade ancestor. Repeating the arithmetic along a quadratic genealogy gives the familiar factor-two ancestry; it does not eliminate that hierarchy.

Conversely, the exact nonzero symbol example rules out a universal algebraic non-attainability theorem based only on incompressibility. Any stronger negative result must use physical localization, whole-history propagation, preparation cost, or the complete adjoint.

This is the second serious collar mechanism in the current run. The first showed that energy/support-size/`L^3` bounds leave an exponentially sparse window; this packet shows that pressure in that window merely relocates UE1 to high-grade exterior ancestry rather than producing the parent from low modes. Per the diversification rule, further local collar algebra is not the next attack. The next primary negative mechanism is the **complete physical adjoint / full-history control cost**.

No common Schwartz trace, collar parent-supply construction, unforced correction, singularity preservation, or `NS-R3` theorem is claimed.

Companion checker: `research/check_collar_angular_ancestry.py`.
