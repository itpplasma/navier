# HF15: uniform low-pressure bounds for the radial regularization

MODE / RESULT: **REPAIR.**  The explicit radial \(C^\infty\) regularization
from HF14 has derivative bounds uniform in \(0<\eta\le1\).  They put every
low-pressure Euler term into an energy-controlled finite-horizon remainder.
The remaining high-pressure Euler and heat sum is still uncontrolled.

## 1. Uniform scalar derivative bounds

Fix \(k>0\), and write
\[
 F_k(v,z)={|v|^3\over3}+g_k(|v|,z)+z_-^{3/2}.
\]
Let \(F_\eta\) be its product convolution with a radial \(v\)-mollifier and
an even \(z\)-mollifier at scale \(\eta\), normalized by
\[
 F_\eta(v,z)=\widetilde F_\eta(v,z)
 -\widetilde F_\eta(0,0)
 -\partial_z\widetilde F_\eta(0,0)z.                 \tag{1}
\]

For the nonsmooth density,
\[
 |D_vF_k(v,z)|\le |v|^2+|z|.                         \tag{2}
\]
Convolution and support at scale \(\eta\le1\) therefore give
\[
 \boxed{\quad
 |D_vF_\eta(v,z)|
 \le C(|v|^2+|z|+\eta).
 \quad}                                               \tag{3}
\]
The normalization in (1) does not affect the \(v\)-derivative.

Let \(a_k(r,z)=\partial_zF_k(v,z)\), with its continuous scalar extensions.
For \(z>0\), \(a_k=r\).  For \(z<0\), put
\[
 s=\sqrt{r^2+kz_-},\qquad h=\sqrt{kz_-}.
\]
The explicit formula
\[
 \partial_zg_k=s-\frac32h+{h^2\over2s}
\]
gives
\[
 \partial_r a_k
 ={r\over s}\left(1-{h^2\over2s^2}\right)\in[0,1].   \tag{4}
\]
The entropy term is independent of \(r\).  Hence
\(v\mapsto a_k(|v|,z)\) is one-Lipschitz for every fixed \(z\).  The scalar
formulas also give
\[
 |a_k(r,z_1)-a_k(r,z_2)|
 \le C_k|z_1-z_2|^{1/2}.                              \tag{5}
\]

Since
\[
 \partial_zF_\eta(v,z)
 =\iint\left[
 a_k(|v-y|,z-s)-a_k(|y|,-s)\right]
 \varphi_\eta(y)\psi_\eta(s)\,dy\,ds,                \tag{6}
\]
where radial symmetry permits replacing \(-y\) by \(y\), equations
(4)--(5) imply
\[
 \boxed{\quad
 |\partial_zF_\eta(v,z)|
 \le |v|+C_k\sqrt{|z|}.
 \quad}                                               \tag{7}
\]
This bound is independent of \(\eta\).  In particular, for
\(z=p^H=Q_JR_iR_j(u_i u_j)\),
\[
 \|\partial_zF_\eta(u,z)\|_3
 \le C_k\|u\|_3,                                     \tag{8}
\]
because
\(\|\sqrt{|z|}\|_3=\|z\|_{3/2}^{1/2}\lesssim\|u\|_3\).

## 2. Exact low-pressure decomposition

Let
\[
 p^L=S_Jp,\qquad p^H=Q_Jp=z,\qquad
 N=(u\cdot\nabla)u,
\]
and split the genuine Euler generator as
\[
 V=-N-\nabla p=W-\nabla p^L,\qquad
 W=-N-\nabla p^H.                                    \tag{9}
\]
The replacement field is generally not divergence free:
\[
 \operatorname{div}W=\Delta p^L.                     \tag{10}
\]

For the fixed-\(\eta\) regularized functional
\[
 \mathcal J^\eta_{k,J}(u)=\int F_\eta(u,p^H),
\]
its exact Euler contribution is
\[
 \mathcal E_\eta
 =\int D_vF_\eta(u,z)\cdot V
 +2\int F_{\eta,z}(u,z)Q_JR_iR_j(u_iV_j).             \tag{11}
\]
Substituting (9) gives the algebraic identity
\[
 \boxed{\quad
 \mathcal E_\eta=\mathcal E_\eta^H-A_\eta-B_\eta,
 \quad}                                               \tag{12}
\]
where
\[
\begin{aligned}
 \mathcal E_\eta^H
 &:=\int D_vF_\eta(u,z)\cdot W
 +2\int F_{\eta,z}(u,z)Q_JR_iR_j(u_iW_j),\\
 A_\eta&:=\int D_vF_\eta(u,z)\cdot\nabla p^L,\\
 B_\eta&:=2\int F_{\eta,z}(u,z)Q_JR_iR_j
                  (u_i\partial_jp^L).                \tag{13}
\end{aligned}
\]
No divergence-free cancellation is applied to \(W\).

## 3. Instantaneous low-pressure estimates

Write
\[
 E=\|u\|_2^2,\qquad Y=\|\nabla u\|_2^2.
\]
The fixed-cutoff kernels give
\[
\begin{aligned}
 \|\nabla p^L\|_\infty&\le C2^{4J}E,&
 \|\nabla p^L\|_2&\le C2^{5J/2}E,\\
 \|\nabla p^L\|_6&\le C2^{7J/2}E,&
 \|\nabla p^L\|_1&\le C2^JE.                         \tag{14}
\end{aligned}
\]
The last estimate is legitimate because the derivative of the
low-pass double-Riesz kernel has an integrable \(O(|x|^{-4})\) tail; its
\(L^1\) norm scales as \(2^J\).

Using (3) and (14),
\[
\begin{aligned}
 |A_\eta|
 &\le C\left[
 E\|\nabla p^L\|_\infty
 +\|z\|_2\|\nabla p^L\|_2
 +\eta\|\nabla p^L\|_1\right]\\
 &\le C\left[
 2^{4J}E^2
 +2^{5J/2}E^{5/4}Y^{3/4}
 +\eta2^JE\right].                                   \tag{15}
\end{aligned}
\]
Here
\[
 \|z\|_2\lesssim\|u\|_4^2\lesssim E^{1/4}Y^{3/4}.    \tag{16}
\]

For \(B_\eta\), self-adjointness is not needed; Hölder, multiplier
boundedness, (8), and (14) give
\[
\begin{aligned}
 |B_\eta|
 &\le C\|F_{\eta,z}(u,z)\|_3
       \|u\nabla p^L\|_{3/2}\\
 &\le C_k\|u\|_3\|u\|_2\|\nabla p^L\|_6\\
 &\le C_k2^{7J/2}E^{7/4}Y^{1/4}.                    \tag{17}
\end{aligned}
\]
All constants are independent of \(0<\eta\le1\).

## 4. Time-integrated energy remainder

Let \(u\) be an actual classical unforced Navier--Stokes solution on
\([0,\tau]\), where \(0<\tau<\min(H,T_*)\), with the compact-interval
\(H^m\) regularity, \(m\ge4\), used in HF14.  The energy identity gives
\[
 E(t)\le E_0,\qquad
 \int_0^\tau Y(t)\,dt\le {E_0\over2\nu}.              \tag{18}
\]
Integrating (15), using Hölder in time on the \(Y^{3/4}\) term, yields
\[
\boxed{\begin{aligned}
 \int_0^\tau|A_\eta(t)|\,dt
 \le C_k\bigl[
 &2^{4J}E_0^2H
 +2^{5J/2}E_0^2\nu^{-3/4}H^{1/4}\\
 &+\eta2^JE_0H\bigr].
\end{aligned}}                                       \tag{19}
\]
Likewise (17) gives
\[
\boxed{\quad
 \int_0^\tau|B_\eta(t)|\,dt
 \le C_k2^{7J/2}E_0^2\nu^{-1/4}H^{3/4}.
\quad}                                               \tag{20}
\]
These are finite input-only remainders, uniformly for \(0<\eta\le1\) and
all terminal times \(\tau<\min(H,T_*)\).

## 5. Coherent balance and remaining gap

The original density splits as
\[
 F_k(v,z)={|v|^3\over3}+H_k(v,z).
\]
Accordingly its product convolution and normalization split \(F_\eta\) into
a radial speed part
\[
 \Phi_\eta(v)=
 \left({|\cdot|^3\over3}*\varphi_\eta\right)(v)
 -\left({|\cdot|^3\over3}*\varphi_\eta\right)(0)     \tag{21}
\]
and a regularized coupling part.  Since \(|v|^3/3\) is convex,
\[
 \mathcal D_\eta
 :=\int D_v^2\Phi_\eta(u)
       [\partial_\ell u,\partial_\ell u]\ge0.         \tag{22}
\]
Separate this term from the exact heat contribution by writing
\[
 \mathcal H_\eta=-\nu\mathcal D_\eta
 +\mathcal H_\eta^{\rm rem}.                         \tag{23}
\]
The fixed-\(\eta\) identity is therefore
\[
\boxed{\quad
 {d\over dt}\mathcal J^\eta_{k,J}
 +\nu\mathcal D_\eta
 =\mathcal E_\eta^H+\mathcal H_\eta^{\rm rem}
  -A_\eta-B_\eta.
\quad}                                               \tag{24}
\]
Equivalently, adding and subtracting the known low pressure work
\[
 L_J=\int p^L u\cdot\nabla|u|
\]
gives
\[
 {d\over dt}\mathcal J^\eta_{k,J}
 +\nu\mathcal D_\eta
 =L_J+
 [\mathcal E_\eta-\!L_J+\mathcal H_\eta^{\rm rem}]. \tag{25}
\]
Equation (24) makes the stronger bookkeeping point: every occurrence of
\(\nabla p^L\) in the regularized Euler derivative is contained in
\(A_\eta+B_\eta\), and (19)--(20) control both.  The standard low-output
estimate separately controls the time integral of \(L_J\); equation (25)
does not assert that its bracket is known.

Thus, after energy-controlled low terms are removed, the first uncontrolled
sum is exactly
\[
 \boxed{\quad
 \mathcal E_\eta^H+\mathcal H_\eta^{\rm rem}.
 \quad}                                               \tag{26}
\]
It contains only the high-pressure replacement field \(W\), the high-output
pressure variation, and the regularized heat coupling.  Since \(W\) is not
solenoidal, no Euler cancellation may be imported into (26).

Functional-value convergence
\[
 \int F_\eta(u,p^H)\to\mathcal J_{k,J}(u)             \tag{27}
\]
is enough to pass endpoint values after integrating (24).  It does not pass
the individual differentiated terms.  A sufficient remaining input would be
a one-sided bound for the integrated sum (26), uniform in \(\eta\), together
with the already proved bounds (19)--(20).  No such bound is proved here.

## 6. Frontier record

CLAIM AND SCOPE: Equations (3), (7)--(8), and (12)--(20) rigorously eliminate
the low-pressure Euler gradients from the fixed-\(\eta\) balance using only
energy and the fixed cutoff.  Equations (21)--(26) give the coherent
dissipation split.

EVIDENCE: The velocity Lipschitz estimate (4), pressure half-Hölder estimate
(5), and centered convolution formula (6) make the scalar bounds uniform in
\(\eta\).  Fixed-cutoff kernel estimates and the energy identity give
(19)--(20).

FIRST GAP: prove a one-sided spacetime estimate for the complete sum (26),
uniformly in the scalar regularization and with an input-selected cutoff.
This is the rewritten high-frequency producer gap.

SURVIVING CONDITIONAL SUFFIX: If such a bound absorbs a strict fraction of
\(\nu\mathcal D_\eta\) with an input-only remainder, then integrating (24),
using (19)--(20), and passing only endpoint functional values through (27)
would give a bound for the limiting coercive functional.  This is a
conditional implication, not a proved criterion or producer.

NON-CLAIMS: No estimate for (26), regularized derivative limit, favorable
heat sign, pressure absorption, HIGH-PRESSURE theorem, critical continuation
bound, or regularity result is asserted.

NEXT DISTINCT ACTION: test the complete high-pressure sum (26), with the
non-solenoidal divergence error retained, on explicit compact packets.
