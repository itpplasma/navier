# HF16: material-pressure reorganization at fixed regularization

Status: exact analytic reorganization with one explicit imported estimate,
2026-09-05.

This note rewrites the high-output pressure evolution using its material
derivative. The identity is rigorous for the fixed radial regularization from
HF15 on compact classical intervals. A low-band advecting-field commutator is
then bounded conditionally on a stated Calderon commutator estimate. The bound
is an input-dependent Gronwall coefficient, not a terminal absorption.

## Material derivative of high-output pressure

Let
\[
 T_J=Q_JR_iR_j,\qquad z=T_J(u_i u_j),\qquad
 N=(u\cdot\nabla)u,
\]
and write the Navier--Stokes equation as
\[
 u_t=\nu\Delta u-N-\nabla p.
\]
Pressure differentiation and the product rule give
\[
 z_t=\nu\Delta z-2\nu T_J(G_{ij})
      -2T_J(u_iN_j)-2T_J(u_i\partial_jp),                     \tag{1}
\]
where \(G_{ij}=\partial_\ell u_i\partial_\ell u_j\). Symmetry in
\(i,j\) gives
\[
 2T_J(u_iN_j)=T_J(u\cdot\nabla(u_i u_j)).                     \tag{2}
\]
Consequently the exact material-pressure identity is
\[
 \boxed{\begin{aligned}
 (\partial_t+u\cdot\nabla)z={}&
 \nu\Delta z-2\nu T_J(G_{ij})\\
 &+[u\cdot\nabla,T_J](u_i u_j)
 -2T_J(u_i\partial_jp).
 \end{aligned}}                                               \tag{3}
\]
The commutator convention is \([A,B]=AB-BA\); this fixes the plus sign in
(3).

## Exact Euler identity for the fixed regularizer

Let \(F_\eta(v,z)\) be the audited smooth radial regularization of the
homogeneous high-output density, with \(k>0\), \(J\), and
\(0<\eta\le1\) fixed. Let \(\mathcal E_\eta\) denote its Euler contribution,
so viscosity is omitted at this stage. Using (3) without its first line,
\[
 \begin{split}
 \mathcal E_\eta={}&
 \int D_vF_\eta(u,z)\cdot(-N-\nabla p)dx\\
 &+\int F_{\eta,z}(u,z)
 \left(-u\cdot\nabla z+[u\cdot\nabla,T_J](u_i u_j)
              -2T_J(u_i\partial_jp)\right)dx.                 \tag{4}
 \end{split}
\]
The two transport terms combine by the chain rule:
\[
 D_vF_\eta(u,z)\cdot(u\cdot\nabla u)
 +F_{\eta,z}(u,z)u\cdot\nabla z
 =u\cdot\nabla F_\eta(u,z).                                  \tag{5}
\]
Its integral vanishes because \(u\) is divergence free and the normalized
fixed-\(\eta\) density is integrable. Therefore
\[
 \boxed{\begin{aligned}
 \mathcal E_\eta={}&
 \int F_{\eta,z}(u,z)[u\cdot\nabla,T_J](u_i u_j)dx\\
 &-2\int F_{\eta,z}(u,z)T_J(u_i\partial_jp)dx
 -\int D_vF_\eta(u,z)\cdot\nabla p dx.
 \end{aligned}}                                               \tag{6}
\]
Thus no transport term or pressure-gradient term has been dropped. Combining
(6) with the audited fixed-\(\eta\) heat identity gives the full evolution;
(6) itself is only its Euler part.

For an actual classical solution on \([0,T]\) with
\[
 u\in C([0,T];H^m),\qquad u_t\in C([0,T];H^{m-2}),\qquad m\ge4,
\]
all terms are legitimate. The fixed regularizer has bounded derivatives on
the bounded range of \((u,z)\), its normalization gives the required
\(L^2\)-based decay, and the multipliers are bounded on the relevant Sobolev
spaces. Hence (3)--(6) follow by Sobolev approximation and integration by
parts, without Schwartz persistence and without taking \(\eta\) to zero.

## Low-band advecting-field commutator

Fix another input-selected integer \(L\), put
\[
 v=S_Lu,\qquad w=u-v,
\]
and use linearity in the advecting field:
\[
 [u\cdot\nabla,T_J](u_i u_j)
 =[v\cdot\nabla,T_J](u_i u_j)
  +[w\cdot\nabla,T_J](u_i u_j).                               \tag{7}
\]
The following standard-looking estimate is the sole external premise in
this subsection and must be independently verified in the exact cutoff
convention before use:
\[
 \boxed{\quad
 \|[v\cdot\nabla,Q_JR_iR_j]f\|_{3/2}
 \le C\|\nabla v\|_\infty\|f\|_{3/2},
 \quad \nabla\cdot v=0,
 \quad}                                                       \tag{C}
\]
with \(C\) independent of \(J\). Formally, its kernel is
\((v(x)-v(y))\cdot\nabla K_J(x-y)\); the Lipschitz difference restores an
order-zero Calderon--Zygmund kernel. This explains the claimed scaling but
is not recorded here as a substitute for verification of the full
\(L^{3/2}\) theorem, including the smooth cutoff part.

The audited regularizer bound is
\[
 \|F_{\eta,z}(u,z)\|_3\le C_k\|u\|_3,                         \tag{8}
\]
uniformly in \(0<\eta\le1\). Bernstein at the fixed input frequency gives
\[
 \|\nabla S_Lu\|_\infty
 \le C2^{5L/2}\|u\|_2.                                      \tag{9}
\]
Assuming (C), Holder's inequality, (8), and (9) yield
\[
 \begin{split}
 &\left|\int F_{\eta,z}(u,z)
       [v\cdot\nabla,T_J](u_i u_j)dx\right|\\
 &\qquad\le C_k2^{5L/2}E(t)^{1/2}\|u(t)\|_3^3\\
 &\qquad\le C_k2^{5L/2}E_0^{1/2}\|u(t)\|_3^3.                \tag{10}
 \end{split}
\]
This coefficient depends only on \(k,L\), the cutoff profiles, and the
initial kinetic energy. It is uniform in \(J\), \(\eta\), and the terminal
time. It can act as a Gronwall coefficient if every other term has already
been controlled. It is not a strict viscous absorption and does not bound
the high-band commutator with advecting field \(w\).

## Relation to the low-pressure extraction

Writing \(p=p^H+p^L\) in the last two terms of (6) isolates the
\(\nabla p^L\) contributions already bounded in HF15. The remaining material
identity contains the full high-pressure gradient and both commutators in
(7). This reorganization does not replace
\(W=-N-\nabla p^H\) by a solenoidal field; indeed the earlier identity
\(\nabla\cdot W=\Delta p^L\) remains in force. No Leray orthogonality may be
applied to \(W\).

## Frontier record

**MODE / RESULT:** DISCOVER. Equations (3) and (6) give a cusp-safe exact
material-pressure reorganization at fixed \(\eta\). Conditional on (C), the
low-band advecting commutator has the input-only coefficient bound (10).

**FIRST GAP:** verify (C) in the precise smooth-cutoff convention, then
control the high-band advecting commutator and the remaining high-pressure
gradient together with the heat remainder. The low-pressure pieces alone do
not close the estimate.

**SURVIVING CONDITIONAL SUFFIX:** once (C) is verified, (10) is a legitimate
Gronwall term with an input-selected coefficient.

**NON-CLAIMS:** no estimate for the remaining high-output aggregate, strict
absorption, differentiated \(\eta\)-limit, HF estimate, or regularity theorem
is asserted.
