# HF16: sourced transport-commutator bound with cutoff dependence

Status: bounded analytic lemma using a verified primary proposition,
2026-09-05.

This note replaces the unsourced derivative-only commutator premise in HF16
by a direct application of Michael Taylor's Proposition 7.2, equation (7.2),
followed by an explicit dilation. The resulting bound contains the full
Lipschitz norm and therefore an additional \(2^J\|v\|_\infty\) term. That
term is harmless for the intended input-coefficient estimate.

## Verified external premise

In [Taylor, *Pseudodifferential Operators and Nonlinear PDE*, Proposition
7.2, equation (7.2)](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/msripde.pdf),
the following statement appears: if \(1<p<\infty\) and
\(P\in OPBS^1_{1,1}\), then
\[
 \|[P,f]g\|_p\le C\|f\|_{\operatorname{Lip}^1}\|g\|_p.       \tag{T}
\]
The source's \(\operatorname{Lip}^1\) norm is the full inhomogeneous norm,
so the application below retains both \(\|f\|_\infty\) and
\(\|\nabla f\|_\infty\). The proposition, rather than a parity-restricted
homogeneous-kernel theorem, is the imported result.

## Algebraic reduction

Let
\[
 T_J=Q_JR_iR_j,
\]
where \(Q_J=I-S_J\) is defined by a fixed smooth cutoff profile. For a
smooth vector field \(v\), set
\[
 C_{v,J}=[v\cdot\nabla,T_J].                                  \tag{1}
\]
Since \(T_J\) commutes with derivatives, define the first-order
constant-coefficient operators
\[
 P_{J,a}=T_J\partial_a.
\]
Direct expansion with the convention \([A,B]=AB-BA\) gives
\[
 \boxed{\quad
 [v\cdot\nabla,T_J]F
 =-\sum_a[P_{J,a},v_a]F+T_J((\nabla\cdot v)F).
 \quad}                                                       \tag{2}
\]
Indeed,
\[
 [P_{J,a},v_a]F
 =T_J((\partial_av_a)F)+T_J(v_a\partial_aF)
   -v_aT_J\partial_aF,
\]
and summing proves (2). Thus for divergence-free \(v\),
\[
 C_{v,J}F=-\sum_a[P_{J,a},v_a]F.                              \tag{3}
\]

For each fixed \(J\), the symbol of \(P_{J,a}\) is smooth, is of order
one, and belongs to the class required by (T). No principal-value kernel
normalization is used in (2)--(3).

## Dilation and the exact cutoff loss

Write the multiplier symbol of \(T_J\) as
\[
 t_J(\xi)=t_0(2^{-J}\xi).
\]
Then
\[
 p_{J,a}(\xi)=i\xi_a t_0(2^{-J}\xi)
             =2^Jp_{0,a}(2^{-J}\xi).                          \tag{4}
\]
Conjugate by the spatial dilation \(y=2^Jx\). Under this conjugation,
\[
 \widetilde v_a(y)=v_a(2^{-J}y),\qquad
 \|\widetilde v_a\|_\infty=\|v_a\|_\infty,
\]
and
\[
 \|\nabla\widetilde v_a\|_\infty
 =2^{-J}\|\nabla v_a\|_\infty.
\]
Applying (T) to \(P_{0,a}\), restoring the factor \(2^J\) from (4), and
undoing the dilation gives
\[
 \|[P_{J,a},v_a]F\|_p
 \le C_p\left(2^J\|v_a\|_\infty
                    +\|\nabla v_a\|_\infty\right)\|F\|_p.   \tag{5}
\]
The constant depends on the fixed cutoff profile and \(p\), but not on
\(J\). Combining (3) and (5) proves
\[
 \boxed{\quad
 \|[v\cdot\nabla,T_J]F\|_p
 \le C_p\left(2^J\|v\|_\infty
                    +\|\nabla v\|_\infty\right)\|F\|_p,
 \quad \nabla\cdot v=0.
 \quad}                                                       \tag{6}
\]
The dilation is part of this note; the source does not itself assert
uniformity in \(J\).

## Low-band application

Let \(v=S_Lu\), where \(L\) is fixed from the input. The low-pass preserves
divergence freedom, and Bernstein gives
\[
 \|v\|_\infty\le C2^{3L/2}\|u\|_2,
 \qquad
 \|\nabla v\|_\infty\le C2^{5L/2}\|u\|_2.                   \tag{7}
\]
Take \(p=3/2\) in (6), \(F=u_i u_j\), and use
\[
 \|F\|_{3/2}\le\|u\|_3^2.
\]
For the audited fixed regularizer,
\[
 \|F_{\eta,z}(u,z)\|_3\le C_k\|u\|_3
\]
uniformly in \(0<\eta\le1\). Holder's inequality therefore yields
\[
 \boxed{\begin{aligned}
 &\left|\int F_{\eta,z}(u,z)
 [S_Lu\cdot\nabla,T_J](u_i u_j)dx\right|\\
 &\qquad\le C_k
 \left(2^{J+3L/2}+2^{5L/2}\right)
 E_0^{1/2}\|u(t)\|_3^3.
 \end{aligned}}                                               \tag{8}
\]
Here the Navier--Stokes energy inequality was used only to replace
\(\|u(t)\|_2\) by \(E_0^{1/2}\).

For input-selected \(J,L,k\), the coefficient in (8) is finite and depends
only on those inputs, the cutoff profiles, and the initial kinetic energy.
It is therefore an admissible Gronwall coefficient if every other term in
the modified-energy inequality has already been controlled. It is not a
strict viscous absorption and gives no bound for the high-band advecting
commutator.

## Frontier record

**MODE / RESULT:** REPAIR. The HF16 low-band transport commutator has the
sourced estimate (8). The earlier stronger derivative-only, uniform-\(J\)
claim is unnecessary.

**FIRST GAP:** control the high-band advecting commutator and the remaining
high-pressure gradient together with the heat remainder.

**SURVIVING CONDITIONAL SUFFIX:** the low-band commutator may be included as
an input-dependent term in the fixed-\(\eta\) identity. Gronwall is applied
only after integration and the functional-value limit, using coercivity of
the unregularized functional; see the endpoint-limit extension in
`hf16-review-material-pressure.md`. No uniform regularized coercivity is assumed.

**NON-CLAIMS:** Taylor's proposition is not said to provide the dilation
uniformity; no high-output absorption, HF estimate, or regularity theorem is
asserted.
