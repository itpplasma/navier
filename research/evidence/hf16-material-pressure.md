# HF16: material-pressure reorganization at fixed regularization

Status: exact analytic reorganization with one explicit imported estimate,
2026-09-05.

This note rewrites the high-output pressure evolution using its material
derivative. The identity is rigorous for the fixed radial regularization from
HF15 on compact classical intervals. A low-band advecting-field commutator is
then bounded using the audited Taylor commutator estimate. The bound
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
The independently reviewed `hf16-taylor-commutator.md` applies Taylor's
Proposition 7.2 to the order-one operators \(Q_JR_iR_j\partial_a\),
then rescales the fixed cutoff. It proves the sufficient bound
\[
 \|[v\cdot\nabla,Q_JR_iR_j]f\|_{3/2}
 \le C(2^J\|v\|_\infty+\|\nabla v\|_\infty)\|f\|_{3/2}.
\]
The constant is independent of J; the displayed cutoff factor is retained.
The stronger derivative-only premise in the frozen candidate is unnecessary.
Holder, Bernstein, the energy identity, and the HF15 uniform bound
\(\|F_{\eta,z}\|_3\le C_k\|u\|_3\) give
\[
 \left|\int F_{\eta,z}[S_Lu\cdot\nabla,T_J](u_i u_j)\right|
 \le M\|u\|_3^3,\qquad
 M=C_k(2^{J+3L/2}+2^{5L/2})E_0^{1/2}.
\]
This is uniform in eta and time, for input-selected J, L, and k.

The Gronwall step requires care. Assume, without claiming to prove it,
that the remaining aggregate has a uniform integrated absorption bound.
Integrate the coherent fixed-eta balance and drop its residual nonnegative
dissipation. For each fixed classical time t, pass eta to zero only in
functional endpoint values. The term \(M\int_0^t\|u\|_3^3\) is independent
of eta and finite on that compact interval. Thus
\[
 J(t)\le C_{\rm input}+M\int_0^t\|u(s)\|_3^3ds
 \le C_{\rm input}+6M\int_0^t J(s)ds.
\]
Unregularized coercivity and Gronwall give
\(J(t)\le C_{\rm input}e^{6Mt}\). No uniform coercivity of J_eta and no
differentiated eta limit are assumed. The independent review's endpoint-limit
extension validates this conditional suffix. The remaining aggregate bound
is still unproved.

## Relation to the low-pressure extraction

Writing \(p=p^H+p^L\) in the last two terms of (6) isolates the
\(\nabla p^L\) contributions already bounded in HF15. The remaining material
identity contains the full high-pressure gradient and both commutators in
(7). This reorganization does not replace
\(W=-N-\nabla p^H\) by a solenoidal field; indeed the earlier identity
\(\nabla\cdot W=\Delta p^L\) remains in force. No Leray orthogonality may be
applied to \(W\).

## Frontier record

**MODE / RESULT:** REPAIR. The exact material-pressure identities and the
sourced low-band commutator estimate are retained. Frozen inputs are at
`174a79c`; the independent reviews record the replacement and limit repair.

**FIRST GAP:** control the high-band advecting commutator and remaining
high-pressure gradient together with the heat remainder.

**SURVIVING CONDITIONAL SUFFIX:** an input-only remaining-aggregate absorption
bound gives Gronwall after the functional-value limit, as above.

**NON-CLAIMS:** no remaining-aggregate estimate, differentiated eta limit,
HF producer, or global regularity theorem is proved.
