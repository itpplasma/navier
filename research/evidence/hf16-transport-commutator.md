# HF16: transport commutator reduced to the T(1) theorem

Status: bounded analytic lemma with an explicit external theorem premise,
2026-09-05.

This note verifies the kernel, cancellation, and weak boundedness hypotheses
for the transport commutator used in HF16. Conditional only on the standard
T(1) theorem and its Calderon--Zygmund \(L^p\) consequence in the stated
form, it proves the required estimate uniformly in the high-output cutoff.

## Statement

Let
\[
 T_J=Q_JR_iR_j,
\]
where \(Q_J=I-S_J\) is formed from a fixed smooth real-even low-pass
profile. Let \(v\) be a smooth bounded divergence-free vector field with
\(\|\nabla v\|_\infty<\infty\) and enough decay to justify distributional
tests against constants. Define
\[
 C_{v,J}=[v\cdot\nabla,T_J].                                  \tag{1}
\]
Then, conditional on the abstract theorem stated below, for every
\(1<p<\infty\),
\[
 \boxed{\quad
 \|C_{v,J}f\|_p\le C_p\|\nabla v\|_\infty\|f\|_p,
 \quad}                                                       \tag{2}
\]
where \(C_p\) is independent of \(J\). The application
\(v=S_Lu\), with \(u\in H^m\), \(m\ge4\), satisfies all hypotheses.

## Uniform off-diagonal kernel

Let \(K_J\) be the distribution kernel of \(T_J\). Away from the diagonal,
the homogeneous Riesz kernel and the scaled smooth low-frequency correction
give
\[
 |\nabla K_J(x)|\le C|x|^{-4},\qquad
 |\nabla^2K_J(x)|\le C|x|^{-5},                               \tag{3}
\]
with constants independent of \(J\). For disjointly supported test
functions, integration by parts and \(\nabla\cdot v=0\) give the
off-diagonal kernel of (1):
\[
 K_{C}(x,y)=(v(x)-v(y))\cdot\nabla K_J(x-y).                  \tag{4}
\]
The Lipschitz estimate for \(v\) and (3) imply
\[
 |K_C(x,y)|\le C\|\nabla v\|_\infty|x-y|^{-3},                \tag{5}
\]
together with the standard first-difference kernel bounds of size
\(C\|\nabla v\|_\infty|x-y|^{-4}\). Thus the Calderon--Zygmund kernel
constants are uniform in \(J\).

Formula (4) is asserted only off the diagonal. The distributional operator
may contain a local multiplication term arising from the principal-value
normalization of the double Riesz transform. The argument below treats the
actual operator (1), so it neither discards nor guesses such a term.

## Cancellation

The symbol of \(T_J\) vanishes in a neighborhood of frequency zero, so
\(T_J1=0\) as a tempered distribution. Since
\((v\cdot\nabla)1=0\),
\[
 C_{v,J}1=0.                                                  \tag{6}
\]
This statement can equivalently be obtained by testing against cutoffs that
tend to one; the decay assumed on \(v\) removes the cutoff boundary terms.

The multiplier \(T_J\) is self-adjoint because its symbol is real and even.
The transport operator \(v\cdot\nabla\) is skew-adjoint because
\(\nabla\cdot v=0\). Therefore their commutator is self-adjoint:
\[
 C_{v,J}^*=C_{v,J},
\]
and hence
\[
 C_{v,J}^*1=0.                                                \tag{7}
\]
In particular both testing functions required by T(1) are zero, uniformly
in \(J\).

## Weak boundedness property

Let \(B=B(x_0,r)\), and let \(\phi,\psi\) be normalized smooth bump
functions supported in \(B\), with
\[
 \|\phi\|_\infty+\|\psi\|_\infty\le1,
 \qquad
 \|\nabla\phi\|_\infty+\|\nabla\psi\|_\infty\le C/r.
\]
A constant vector field commutes with \(T_J\). Subtract
\(v(x_0)\), use skew-adjointness of transport in the first commutator term,
and use the uniform \(L^2\) multiplier norm of \(T_J\). This gives
\[
 \begin{split}
 |\langle C_{v,J}\phi,\psi\rangle|
 &\le
 |\langle T_J\phi,(v-v(x_0))\cdot\nabla\psi\rangle|\\
 &\quad+|\langle T_J((v-v(x_0))\cdot\nabla\phi),\psi\rangle|\\
 &\le C\|\nabla v\|_\infty r^3.                              \tag{8}
 \end{split}
\]
Indeed each undifferentiated bump has \(L^2\) norm \(O(r^{3/2})\), while
\((v-v(x_0))\nabla\phi\) and the analogous \(\psi\) factor have
\(L^2\) norm \(O(\|\nabla v\|_\infty r^{3/2})\). This is the weak
boundedness property with the correct scaling and a constant uniform in
\(J\).

## Exact external premise and conclusion

The remaining imported statement is:

> **T(1) premise.** An operator on \(\mathbb R^3\) whose off-diagonal kernel
> has the standard Calderon--Zygmund size and first-difference bounds, which
> has the weak boundedness property, and for which \(T1,T^*1\in\mathrm{BMO}\),
> extends boundedly on \(L^2\), with norm controlled by those constants.
> An \(L^2\)-bounded operator with those kernel bounds extends boundedly on
> every \(L^p\), \(1<p<\infty\), with the corresponding controlled norm.

Equations (5)--(8) verify every hypothesis of this premise for
\(C_{v,J}/\|\nabla v\|_\infty\), uniformly in \(J\). The premise therefore
proves (2). No parity assumption on \(\nabla K_J\) is used; in particular,
the available theorem for even homogeneous degree-minus-four kernels is not
silently substituted for this odd derivative kernel.

For the project application, \(v=S_Lu\) is divergence free. Compact Fourier
support and \(u\in L^2\) make \(v\) smooth and vanishing at infinity, while
Bernstein gives
\[
 \|\nabla v\|_\infty\le C2^{5L/2}\|u\|_2.                    \tag{9}
\]
Taking \(p=3/2\) in (2) supplies exactly the conditional estimate used in
HF16.

## Frontier record

**MODE / RESULT:** REPAIR. The transport commutator estimate is reduced to
the precise T(1) theorem premise. All operator-specific hypotheses are
verified uniformly in \(J\).

**FIRST GAP:** verify a primary source for the exact T(1) and
Calderon--Zygmund consequences quoted above, including their stated weak
bump-testing convention. Until then, (2) remains a conditional imported
lemma.

**SURVIVING CONDITIONAL SUFFIX:** once that theorem is source-verified, the
HF16 low-band commutator becomes an unconditional input-coefficient
Gronwall term.

**NON-CLAIMS:** no estimate for the high-band advecting commutator, remaining
pressure-gradient or heat terms, HF, or regularity is asserted.
