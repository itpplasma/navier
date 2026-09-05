# HF11: pressure entropy repairs coercivity, with an unresolved heat sign

MODE / RESULT: **REPAIR.**  Adding the pressure entropy
\(({-p})_+^{3/2}\) makes the coefficient-one pressure--speed functional
coercive at the static level.  Along smooth Navier--Stokes flow, a fixed
positive regularization has the exact evolution formula below.  Its heat
part is not manifestly dissipative: it contains mixed gradients and a
nonlocal pressure source of undetermined sign.  No heat-sign conclusion or
counterexample is claimed without a further exact argument.

CLAIM AND SCOPE: For a real solenoidal Schwartz field on \(\mathbb R^3\), set
\[
 r=|u|,\qquad p=R_iR_j(u_i u_j),\qquad
 \mathcal K(u)=\int_{\mathbb R^3}
 \left({r^3\over3}+pr+p_-^{3/2}\right),
 \quad p_-=(-p)_+.                                  \tag{1}
\]
The pressure uses the Fourier multiplier
\(-\xi_i\xi_j/|\xi|^2\).  Static coercivity holds for (1).  The differentiated
identity is first proved only for fixed positive regularizers; passage to an
unregularized derivative is kept separate from convergence of the integrated
functional.

EVIDENCE:

## 1. Static two-sided cubic control

If \(p\ge0\), the pointwise integrand in (1) is at least \(r^3/3\).  If
\(p<0\), write \(z=\sqrt{-p}\).  Young's inequality in the scaled form
\[
 rz^2\le {r^3\over6}+{2\sqrt2\over3}z^3             \tag{2}
\]
gives
\[
 {r^3\over3}+pr+p_-^{3/2}
 \ge {r^3\over6}+\left(1-{2\sqrt2\over3}\right)p_-^{3/2}.
                                                               \tag{3}
\]
The second coefficient is positive.  Hence
\[
 \mathcal K(u)\ge {1\over6}\|u\|_3^3.              \tag{4}
\]
Conversely, double Riesz transforms are bounded on \(L^{3/2}\), so
\[
 \|p\|_{3/2}\le C\|u\otimes u\|_{3/2}
 \le C\|u\|_3^2.                                   \tag{5}
\]
Hölder then bounds \(\int|p|r\) and \(\int p_-^{3/2}\) by
\(C\|u\|_3^3\).  Thus
\[
 {1\over6}\|u\|_3^3\le\mathcal K(u)
 \le C\|u\|_3^3.                                   \tag{6}
\]
This repairs the coefficient-one coercivity failure exhibited by the HF10
pressure--speed counterexample.

## 2. Integrable smooth regularization

Let
\[
 r_\epsilon=(\epsilon^2+|u|^2)^{1/2},\qquad
 \rho_\epsilon=r_\epsilon-\epsilon,\qquad \epsilon>0.           \tag{7}
\]
For \(\phi(q)=q_-^{3/2}\), choose an even nonnegative scalar mollifier
\(\chi_\delta\in C_c^\infty(\mathbb R)\) of mass one and define
\[
 \Phi_\delta(q)=(\chi_\delta*\phi)(q)
  -(\chi_\delta*\phi)(0)
  -(\chi_\delta*\phi)'(0)q.                         \tag{8}
\]
Then \(\Phi_\delta(0)=\Phi_\delta'(0)=0\),
\(\Phi_\delta''\ge0\), and
\[
 |\Phi_\delta'(q)|\le C_\delta|q|\quad(|q|\le1),
 \qquad |\Phi_\delta'(q)|\le C\sqrt{|q|}.           \tag{9}
\]
The second bound is uniform in \(\delta\):
\(\phi'(q)=-\frac32\sqrt{q_-}\) is Hölder-\(1/2\), convolution preserves
that seminorm, and (8) subtracts the derivative at zero.  Integrating (9)
also gives \(|\Phi_\delta(q)|\le C|q|^{3/2}\) uniformly.
The subtraction of both the value and tangent at zero is needed:
it makes \(\Phi_\delta(q)=O_\delta(q^2)\) as \(q\to0\), so the entropy is
integrable at spatial infinity even though a Riesz pressure need not be in
\(L^1\).

Define
\[
 \mathcal K_{\epsilon,\delta}(u)=
 \int\left\{{r_\epsilon^3-\epsilon^3\over3}
             +p\rho_\epsilon+\Phi_\delta(p)\right\}.            \tag{10}
\]
For a smooth Schwartz field, (10) and every pairing below are finite.  As
\(\epsilon,\delta\downarrow0\), the three terms converge to those of (1):
the first by dominated convergence, the second by Hölder using
\(0\le\rho_\epsilon\le r\), and the third in \(L^1\) from scalar mollification
and \(p\in L^{3/2}\).  This proves convergence of functional values; it does
not by itself prove convergence of their derivatives.

## 3. Exact fixed-regularizer evolution

Let \(u\in C([0,T];H^m(\mathbb R^3))\),
\(u_t\in C([0,T];H^{m-2}(\mathbb R^3))\), \(m\ge4\), be a classical
solution on a compact interval strictly before its maximal endpoint, of
\[
 u_t=\nu\Delta u+V(u),\qquad
 V(u)=-\mathbb P((u\cdot\nabla)u).                  \tag{11}
\]
No preservation of Schwartz decay is assumed. At fixed positive
\(\epsilon,\delta\), the pressure and its time derivative belong to
\(L^2\), while \(\rho_\epsilon\) and \(\Phi_\delta'(p)\) belong to
\(H^1\cap L^2\). Here \(\Phi_\delta''\) is bounded for fixed
\(\delta\), and \(\Phi_\delta'(0)=0\). Sobolev embedding gives
\(\nabla u\in L^\infty\cap L^2\), so \(G_{ij}\in L^2\).
These bounds justify the displayed pairings, differentiation, and
integration by parts by Sobolev approximation on the compact interval.
They do not assert uniform derivative bounds as the regularizers vanish.
This is the applicability repair from `hf11-review-pressure-entropy.md`;
the original candidate and audit are frozen at `f3e7605`.

Differentiating the Riesz pressure and using symmetry in \(i,j\) gives
\[
 p_t=2R_iR_j(u_i u_{j,t})
 =\nu\Delta p-2\nu R_iR_j(\partial_k u_i\partial_k u_j)
   +2R_iR_j(u_iV_j).                                \tag{12}
\]
Indeed, applying \(\Delta\) to \(u_i u_j\) accounts for the two
\(u_i\Delta u_j\) terms and the two gradient-product terms.

Put
\[
 w_{\epsilon,\delta}
   =\rho_\epsilon+\Phi_\delta'(p),
 \qquad G_{ij}=\partial_k u_i\partial_k u_j.         \tag{13}
\]
Direct differentiation of (10) yields the exact identity
\[
 {d\over dt}\mathcal K_{\epsilon,\delta}(u)
 =\mathcal H_{\epsilon,\delta}(u)
  +\mathcal E_{\epsilon,\delta}(u),                 \tag{14}
\]
where the Euler/nonlinear contribution is
\[
 \boxed{\begin{aligned}
 \mathcal E_{\epsilon,\delta}(u)={}&
 \int\left(r_\epsilon+{p\over r_\epsilon}\right)u\cdot V\\
 &+2\int w_{\epsilon,\delta}R_iR_j(u_iV_j),
 \end{aligned}}                                    \tag{15}
\]
and the full heat contribution is
\[
 \boxed{\begin{aligned}
 {\mathcal H_{\epsilon,\delta}(u)\over\nu}={}&
 -\int r_\epsilon\bigl(|\nabla u|^2+|\nabla r_\epsilon|^2\bigr)\\
 &-\int {p\over r_\epsilon}
       \bigl(|\nabla u|^2-|\nabla r_\epsilon|^2\bigr)
 -2\int\nabla p\cdot\nabla r_\epsilon\\
 &-\int\Phi_\delta''(p)|\nabla p|^2
 -2\int w_{\epsilon,\delta}R_iR_j(G_{ij}).
 \end{aligned}}                                    \tag{16}
\]

To verify (16), the velocity part of the heat derivative is
\[
 \begin{aligned}
 \int\left(r_\epsilon+{p\over r_\epsilon}\right)u\cdot\Delta u
 ={}&-\int r_\epsilon(|\nabla u|^2+|\nabla r_\epsilon|^2)\\
 &-\int{p\over r_\epsilon}
       (|\nabla u|^2-|\nabla r_\epsilon|^2)
 -\int\nabla p\cdot\nabla r_\epsilon.
 \end{aligned}                                     \tag{17}
\]
The \(\Delta p\) part of (12) contributes
\[
 \int w_{\epsilon,\delta}\Delta p
 =-\int\nabla r_\epsilon\cdot\nabla p
  -\int\Phi_\delta''(p)|\nabla p|^2,               \tag{18}
\]
and its remaining heat source is the last term in (16).  Equations
(17)--(18) account for the factor two in the mixed gradient.

## 4. What the heat identity establishes

The first and fourth terms of (16) are nonpositive.  The other three groups
do not have a sign from the stated hypotheses:

* \(p/r_\epsilon\) changes sign, although
  \(|\nabla u|^2-|\nabla r_\epsilon|^2\ge0\);
* \(-2\nabla p\cdot\nabla r_\epsilon\) is a genuine mixed term;
* the nonlocal scalar
  \(R_iR_j(G_{ij})\) has no pointwise sign and is paired with
  \(w_{\epsilon,\delta}\), which also changes sign in general.

Thus convexity \(\Phi_\delta''\ge0\) proves only the displayed
pressure-gradient dissipation.  It does not prove
\(\mathcal H_{\epsilon,\delta}\le0\), and estimating the unsigned terms does
not prove that the heat contribution is positive on some field.  Formula
(16) is the exact remaining object; a sign theorem or counterexample requires
an additional complete argument.

There is a separate zero-set issue at \(\epsilon=0\).  The map
\(u\mapsto\int p(u)|u|\) need not have a two-sided directional or Frechet
derivative when \(u=0\) on a set where the chosen direction is nonzero; the
one-sided speed derivative changes there.  Accordingly, (15)--(16) are
asserted as classical derivative identities only for \(\epsilon,\delta>0\).
An integrated \(\epsilon,\delta\downarrow0\) balance may be extracted under
separate domination estimates, but the limiting Euler integrand must not be
relabeled as an unqualified \(D\mathcal K(u)[V]\).

FIRST GAP: Determine the sign of the complete heat expression (16), either by
a grouping that controls all three indefinite groups or by an explicit smooth
solenoidal snapshot for which it is positive.  Static coercivity (6) does not
resolve this derivative question.

SURVIVING CONDITIONAL SUFFIX: The pressure entropy is a valid static coercive
repair retaining the coefficient-one term \(\int p|u|\).  Any modified-energy
route may use (6) and the exact regularized evolution (14)--(16), conditional
on separately controlling the full heat and nonlinear remainders.

NON-CLAIMS: No dissipative sign for (16), unregularized Frechet derivative,
closed Navier--Stokes estimate, pressure absorption, critical spacetime bound,
regularity theorem, or global conclusion is established.

NEXT DISTINCT ACTION: Test (16) on an analytically tractable smooth
divergence-free family, retaining the Riesz source exactly.  A numerical sign
search can nominate a field but cannot replace an analytic certificate.
