# HF13: far-field sign of the pressure-entropy variation

Status: bounded analytic evidence, 2026-09-05.

This note proves the angular sign and the nonlocal far-field Riesz asymptotic
needed by the proposed entropy mechanism. It does not duplicate the separate
high-frequency packet construction.

## Compact swirl and pressure tail

Let
\[
 U=f(r,z)e_\vartheta
\]
be a nonzero smooth compactly supported axisymmetric azimuthal field. Its
integrated quadratic stress is
\[
 \int U_iU_jdx=\operatorname{diag}(A,A,0),\qquad A>0.          \tag{1}
\]
Taylor expansion of the double-Riesz kernel away from the support gives,
with \(R=|x|\), \(\mu=x_3/R\), and \(C>0\),
\[
 p_U(x)=C(1-3\mu^2)R^{-3}+O(R^{-4}).                          \tag{2}
\]
The leading pressure is negative in the polar cones. For the entropy
derivative
\[
 e_U(x)=-{3\over2}\sqrt{(p_U(x))_-},
\]
the one-half Holder continuity of the positive-part square root yields
\[
 e_U(x)=-{3\over2}\sqrt C R^{-3/2}F(\mu)+O(R^{-2}),\qquad
 F(\mu)=\sqrt{(3\mu^2-1)_+}.                                  \tag{3}
\]
It also gives \(|e_U(x)|\le C_1(1+|x|)^{-3/2}\).

## Certified angular sign

Let \(a\) be the unique axisymmetric distributional solution on \(S^2\) of
\[
 (\Delta_{S^2}+3/4)a={3\over2}F.                              \tag{4}
\]
Uniqueness holds because \(3/4\ne l(l+1)\) for every integer \(l\ge0\).
Writing
\[
 F(\mu)=\sum_{l\ge0}F_lP_l(\mu),\qquad
 F_l={2l+1\over2}\int_{-1}^1F(\mu)P_l(\mu)d\mu,
\]
gives
\[
 a(1)={3\over2}\sum_{l=0,2,4,\ldots}
 {F_l\over3/4-l(l+1)}.                                       \tag{5}
\]

This number is positive without relying on quadrature. Put
\[
 I=F_0=\int_{1/\sqrt3}^1\sqrt{3\mu^2-1}d\mu.
\]
The integrand is concave on this interval and lies above its endpoint chord,
so
\[
 I\ge {\sqrt2\over2}\left(1-{1\over\sqrt3}\right)>{2\over7}.
                                                                    \tag{6}
\]
Thus the constant-mode contribution in (5) is greater than \(4/7\).

For the remaining modes, use the orthonormal Legendre functions
\(e_l=\sqrt{(2l+1)/2}P_l\) and put \(D_l=l(l+1)-3/4\). The odd
coefficients vanish. Since \(D_l\ge(7/8)l(l+1)\) for \(l\ge2\),
\[
 \sum_{l\ge2}{e_l(1)^2\over D_l^2}
 \le {32\over49}\sum_{l\ge2}{2l+1\over l^2(l+1)^2}
 ={8\over49}.                                                 \tag{7}
\]
Parseval and Cauchy--Schwarz bound the absolute contribution of all modes
\(l\ge2\) by
\[
 {3\sqrt2\over7}\sqrt{\|F\|_2^2-2F_0^2}
 <{3\sqrt{82}\over49},                                       \tag{8}
\]
because \(\|F\|_2^2=4/(3\sqrt3)<1\) and \(F_0>2/7\). Therefore
\[
 \boxed{\quad a(1)>{28-3\sqrt{82}\over49}>0.\quad}           \tag{9}
\]
The last sign follows from \(28^2>9\cdot82\).

## Riesz asymptotic at the pole

Define the homogeneous tail
\[
 e_\infty(x)=-{3\over2}\sqrt C |x|^{-3/2}F(x_3/|x|).
\]
A concrete inverse Laplacian is
\[
 \Psi(x)=\int_{\mathbb R^3}
 [\Gamma(x-y)-\Gamma(-y)]e_\infty(y)dy,                       \tag{10}
\]
where \(\Gamma\) is the Newton kernel. The subtraction makes the integral
converge at infinity, since the bracket is \(O(|y|^{-2})\); near zero and
near \(y=x\), the singularities are locally integrable. It follows that
\(-\Delta\Psi=e_\infty\). Scaling (10), up to an irrelevant additive
constant, and uniqueness of (4) give
\[
 \Psi(x)=\sqrt C R^{1/2}a(\mu).                               \tag{11}
\]
Second derivatives remove the additive constant and equal the double Riesz
transform. At the positive pole differentiation is purely radial, hence
\[
 R_3R_3e_\infty(0,0,R)
 =\partial_3^2\Psi(0,0,R)
 =-{1\over4}\sqrt C a(1)R^{-3/2}<0.                           \tag{12}
\]

It remains to transfer this homogeneous computation to the exact compact
swirl. Set
\[
 e_R(y)=R^{3/2}e_U(Ry).
\]
Equation (3) gives convergence to \(e_\infty(y)\) away from \(y=0\), and
the global pressure bound gives
\[
 |e_R(y)|\le C|y|^{-3/2}.                                    \tag{13}
\]
Near \(y=e_3\), the limiting pressure is strictly negative, so (2) and its
derivatives give local \(C^2\) convergence of \(e_R\) to \(e_\infty\).

Use the principal-value kernel formula for \(R_3R_3e_R(e_3)\). Split its
integral into a small ball about \(e_3\), a small ball about the origin, a
fixed intervening annulus, and the far tail. In the first region subtract
the first-order Taylor polynomial; local \(C^2\) convergence controls the
principal value (and the conventional local multiple of \(e_R(e_3)\), if
included in the kernel formula, converges directly). In the origin region the kernel is bounded and
\(|y|^{-3/2}\) is integrable. On the intervening annulus use dominated
convergence. In the far region the Riesz kernel is \(O(|y|^{-3})\), so
(13) supplies an integrable \(O(|y|^{-9/2})\) majorant. Thus
\[
 R^{3/2}R_3R_3e_U(Re_3)
 \longrightarrow R_3R_3e_\infty(e_3)
 =-{1\over4}\sqrt C a(1)<0.                                  \tag{14}
\]
In particular, \(R_3R_3e_U(Re_3)<0\) for all sufficiently large \(R\).
This argument uses the complete nonlocal pressure dependence; it makes no
inference from a local Hessian sign.

## Frontier record

**MODE / RESULT:** DISCOVER. The angular coefficient has the certified bound
(9), and the exact compact-swirl entropy derivative has the negative polar
far-field Riesz sign (14).

**FIRST GAP:** a separate packet argument must retain every other quadratic
term and prove that (14) dominates them. This note does not perform that
step.

**SURVIVING CONDITIONAL SUFFIX:** the sign producer (14) is available for an
all-\(k\) homogeneous-coupling heat test.

**NON-CLAIMS:** no high-frequency packet estimate, heat-monotonicity
counterexample for the full functional, Navier--Stokes trajectory statement,
HF estimate, or regularity result is asserted.
