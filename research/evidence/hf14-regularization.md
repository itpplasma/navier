# HF14 repair: an integrable radial scalar regularization

MODE / RESULT: **REPAIR.**  A concrete radial convolution in
\((u,z)\in\mathbb R^3\times\mathbb R\), followed by value and \(z\)-tangent
normalization, gives a smooth integrable density for which the complete
generic HF14 evolution is rigorous on compact classical intervals.  The
regularized functional values converge to the homogeneous cusp functional.
No convergence of differentiated identities is asserted.

## 1. The nonsmooth density and its scalar bounds

Fix \(k>0\), and define
\[
 F_k(v,z)={|v|^3\over3}+g_k(|v|,z)+z_-^{3/2},         \tag{1}
\]
where
\[
 g_k(r,z)=z\left(\sqrt{r^2+kz_-}-\sqrt{kz_-}\right). \tag{2}
\]
The elementary bounds from the homogeneous coupling are
\[
 |g_k(r,z)|\le |z|r,\qquad
 |F_k(v,z)|\le C(r^3+|z|^{3/2}).                     \tag{3}
\]
Where the scalar derivatives exist,
\[
 |\nabla_vF_k(v,z)|\le r^2+|z|,\qquad
 |\partial_zF_k(v,z)|\le C_k(r+\sqrt{|z|}).           \tag{4}
\]
The pressure derivative
\[
 a_k(r,z)=\partial_zF_k(v,z)
\]
has its continuous extensions at \(z=0\) and at \(r=0,z<0\), and satisfies
the uniform half-Hölder estimate
\[
 |a_k(r,z_1)-a_k(r,z_2)|
 \le C_k|z_1-z_2|^{1/2}.                              \tag{5}
\]
This follows directly from the explicit formulas for \(g_{k,z}\) on
\(z>0\) and \(z<0\); the one-sided values match at \(z=0\).  The bound is
also the scalar Nemytskii estimate used in the HF13 packet expansion.

## 2. Radial four-variable mollification

Let \(\varphi\in C_c^\infty(\mathbb R^3)\) be nonnegative, radial, even, and
of integral one, and let \(\psi\in C_c^\infty(\mathbb R)\) be nonnegative,
even, and of integral one.  Take both supports in the unit ball and set
\[
 \varphi_\eta(y)=\eta^{-3}\varphi(y/\eta),\qquad
 \psi_\eta(s)=\eta^{-1}\psi(s/\eta).                 \tag{6}
\]
Define
\[
 \widetilde F_\eta(v,z)
 =\iint F_k(v-y,z-s)\varphi_\eta(y)\psi_\eta(s)\,dy\,ds,
                                                               \tag{7}
\]
and normalize it by
\[
 F_\eta(v,z)=\widetilde F_\eta(v,z)
 -\widetilde F_\eta(0,0)
 -\partial_z\widetilde F_\eta(0,0)\,z.               \tag{8}
\]

Then \(F_\eta\in C^\infty(\mathbb R^4)\).  Radiality of \(\varphi\) and of
\(F_k\) in \(v\) makes \(F_\eta\) radial in \(v\), and hence
\[
 \nabla_vF_\eta(0,z)=0.                              \tag{9}
\]
The normalization gives
\[
 F_\eta(0,0)=0,\qquad \partial_zF_\eta(0,0)=0.       \tag{10}
\]
The subtracted linear term in (8) need not be integrable by itself.  It is
the normalized density \(F_\eta(u,z)\) as a whole that is integrable.

For fixed \(\eta>0\) and \(M<\infty\), Taylor's theorem and (9)--(10) give
\[
\begin{aligned}
 |F_\eta(v,z)|&\le C_{\eta,M}(|v|^2+z^2),\\
 |DF_\eta(v,z)|&\le C_{\eta,M}(|v|+|z|),\\
 |D^2F_\eta(v,z)|&\le C_{\eta,M},
 \qquad |v|+|z|\le M.                                \tag{11}
\end{aligned}
\]
These are the derivative bounds needed for the fixed-regularizer evolution;
mere cubic value growth would not suffice.

## 3. A uniform integrable majorant for functional values

For \(0<\eta\le1\), the normalized densities also satisfy
\[
 \boxed{\quad
 |F_\eta(v,z)|
 \le C_k\bigl(|v|^3+|v|^2+|z|^{3/2}\bigr),
 \quad}                                               \tag{12}
\]
with a constant independent of \(\eta\).

Here is a proof.  Split
\[
\begin{aligned}
 F_\eta(v,z)={}&
 [\widetilde F_\eta(v,z)-\widetilde F_\eta(0,z)]\\
 &+[\widetilde F_\eta(0,z)-\widetilde F_\eta(0,0)
      -\partial_z\widetilde F_\eta(0,0)z].            \tag{13}
\end{aligned}
\]
Convolution preserves (5), so the second bracket is bounded by
\(C_k|z|^{3/2}\).

For \(r=|v|\ge\eta\), (4) and the support of the mollifier give
\[
 |\widetilde F_\eta(v,z)-\widetilde F_\eta(0,z)|
 \le C_k(r^3+r^2+|z|r).                              \tag{14}
\]
For \(r\le\eta\), radiality gives zero first derivative at \(v=0\).
Differentiating the mollified radial cusp, using (4), yields on the segment
from \(0\) to \(v\)
\[
 \|D^2_{vv}\widetilde F_\eta(\cdot,z)\|
 \le C_k\left(1+\eta+{|z|\over\eta}\right).           \tag{15}
\]
Consequently the first bracket in (13) is bounded by
\[
 C_k\left(r^2+{|z|r^2\over\eta}\right)
 \le C_k(r^2+|z|r),                                  \tag{16}
\]
because \(r\le\eta\).  Finally Young's inequality
\(|z|r\le C(|z|^{3/2}+r^3)\) proves (12).

Since convolution approximates the continuous function \(F_k\),
\(\widetilde F_\eta(v,z)\to F_k(v,z)\).  Also
\(\widetilde F_\eta(0,0)\to0\), and (5) implies
\(\partial_z\widetilde F_\eta(0,0)\to a_k(0,0)=0\).
Thus
\[
 F_\eta(v,z)\longrightarrow F_k(v,z)                 \tag{17}
\]
pointwise.

If \(u\in L^2\cap L^3\) and \(z\in L^{3/2}\), (12) and dominated convergence
give the functional-value limit
\[
 \int F_\eta(u,z)\longrightarrow\int F_k(u,z).       \tag{18}
\]
No derivative convergence follows from (12).

## 4. Rigorous fixed-\(\eta\) evolution

Let \(u\) be an actual classical Navier--Stokes solution on a fixed compact
interval \([0,T]\), with
\[
 u\in C([0,T];H^m),\qquad
 u_t\in C([0,T];H^{m-2}),\qquad m\ge4.               \tag{19}
\]
Fix the smooth high-output pressure
\[
 z=p_H=Q_JR_iR_j(u_i u_j).                           \tag{20}
\]
Sobolev multiplication and multiplier boundedness give
\[
\begin{aligned}
 &u,z\in C_tH^m,\qquad
 u_t,z_t\in C_tH^{m-2},\\
 &u,z\in C_t(L^2\cap L^\infty),\qquad
 \nabla u,\nabla z\in C_tL^2.                        \tag{21}
\end{aligned}
\]
The pointwise range of \((u,z)\) is contained in a fixed compact set.
Equations (11) and (21) show that
\[
 \mathcal J^\eta_{k,J}(u):=\int F_\eta(u,p_H)         \tag{22}
\]
is finite and differentiable along the solution.  Its derivative pairings
are integrable because \(DF_\eta(u,z)=O_{\eta,M}(|u|+|z|)\) and
\((u_t,z_t)\in L^2\times L^2\).

Write \(r=|u|\), let \(f^\eta(r,z)=F_\eta(v,z)\), and set
\[
 \beta_\eta={f^\eta_r\over r},
\]
using the smooth extension at \(r=0\) supplied by (9).  With
\[
 V=-\mathbb P((u\cdot\nabla)u),\qquad
 G_{ij}=\partial_\ell u_i\partial_\ell u_j,
\]
pressure differentiation gives
\[
 z_t=2Q_JR_iR_j(u_i u_{t,j})
 =\nu\Delta z-2\nu Q_JR_iR_j(G_{ij})
   +2Q_JR_iR_j(u_iV_j).                              \tag{23}
\]
The exact fixed-\(\eta\) balance is
\[
 {d\over dt}\mathcal J^\eta_{k,J}
 =\mathcal H_\eta+\mathcal E_\eta,                   \tag{24}
\]
where
\[
\begin{aligned}
 \mathcal E_\eta={}&
 \int\beta_\eta u\cdot V
 +2\int f^\eta_zQ_JR_iR_j(u_iV_j),                   \tag{25}\\
 {\mathcal H_\eta\over\nu}={}&
 -\int\beta_\eta|\nabla u|^2
 -\int(f^\eta_{rr}-\beta_\eta)|\nabla r|^2\\
 &-2\int f^\eta_{rz}\nabla r\cdot\nabla z
 -\int f^\eta_{zz}|\nabla z|^2\\
 &-2\int f^\eta_zQ_JR_iR_j(G_{ij}).                  \tag{26}
\end{aligned}
\]

Every term is finite under (19).  The Hessian coefficients in the first four
terms are bounded on the actual range by (11).  For the last term,
\(f^\eta_z=O_{\eta,M}(|u|+|z|)\in L^2\), while
\[
 \|Q_JR_iR_j(G_{ij})\|_2
 \le C_J\|\nabla u\|_\infty\|\nabla u\|_2<\infty.     \tag{27}
\]
The analogous estimate with \(u_iV_j\) proves finiteness of the last Euler
term.  Integration by parts is justified by Sobolev approximation, (11), and
these \(L^2\) bounds.

Equations (24)--(26) are one coherent regularized balance.  The
away-from-cusps algebra for the original \(F_k\) is a separate formal identity;
it is not mixed into (24).

## 5. Exact scope

CLAIM AND SCOPE: The convolution (6)--(8) gives a concrete smooth radial
regularization.  For every fixed \(\eta>0\), (24)--(26) are rigorous on a
compact \(H^m\) classical interval.  Functional values converge by (18) when
\(z=p_H\).

EVIDENCE: Radiality and normalization give the quadratic small-field bounds
(11); (12)--(18) give an \(\eta\)-uniform integrable majorant and value
convergence; (19)--(27) verify every derivative and source pairing in the
fixed-\(\eta\) evolution.

FIRST GAP: pass the complete differentiated balance (24)--(26) to
\(\eta\downarrow0\), or obtain estimates uniform in \(\eta\).  Functional
value convergence alone does not provide either conclusion.

SURVIVING CONDITIONAL SUFFIX: The exact generic HF14 identity is rigorous for
the explicit fixed regularization.  The unregularized high-output Euler
formula remains valid only as away-from-cusps algebra until a domination
argument is supplied.

NON-CLAIMS: No unregularized Euler or heat derivative, regularized-identity
limit, favorable sign, high-output pressure estimate, critical bound,
continuation theorem, or regularity conclusion is asserted.

NEXT DISTINCT ACTION: identify a grouping in (25)--(26) whose estimates are
uniform under the radial regularization; otherwise the cusp limit remains the
first analytic obstruction.
