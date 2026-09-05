# Independent audit of the HF10 pressure--speed evolution identity

**VERDICT: REPAIR.**  The regularized identity (12) and its integrated
zero-regularization limit (17) pass.  The later identification (18) as an
actual two-sided first variation \(DB(u)[V]\) is not justified at the zero set
of \(u\).  Replacing that notation by an explicitly defined nonlinear
contribution repairs the claimed mechanism without changing (12) or (17).

## Reviewed scope

I reviewed “research/evidence/hf10-pressure-speed-evolution.md” at SHA-256
“88140677030b35254ead3638f4a4b19eb9ee46bd7118f7ecbff2f1a21e21a177”,
relative to base commit
“4a377b5550a3fb46c0ad85933a72d7f3f44771e9”.  The scope is the exact
coefficient-one cancellation, pressure gauge, regularized differentiation,
viscous and nonlinear residuals, and passage to the integrated
\(\epsilon=0\) identity for an actual classical \(H^m\) solution on a fixed
compact interval.  Coercivity is outside this audit.

## Reconstruction of the valid identity

### 1. Finiteness and the pressure gauge

For \(m\ge4\), Sobolev multiplication and boundedness of the Riesz transforms
give

\[
 u_i u_j\in C_tH^m,\quad p=R_iR_j(u_i u_j)\in C_tH^m,
 \quad V=-\mathbb P(u\cdot\nabla u)\in C_tH^{m-1}.     \tag{A1}
\]

Also \(p,u\in C_tL^2\).  The pointwise inequalities

\[
 0\le r_\epsilon-\epsilon\le |u|,\qquad
 r_\epsilon^3-\epsilon^3\lesssim |u|^3+\epsilon|u|^2 \tag{A2}
\]

prove that \(F_\epsilon\) and
\(B_\epsilon=\int p(r_\epsilon-\epsilon)\) are finite.  The subtraction in
\(B_\epsilon\) is essential on \(\mathbb R^3\): the available information is
only \(p\in L^2\), so \(\int p r_\epsilon\), whose weight tends to the
nonzero constant \(\epsilon\) at spatial infinity, is not defined in general.
The analogous subtraction in \(F_\epsilon\) removes an infinite constant
density.

The choice \(p=R_iR_j(u_i u_j)\) fixes the spatial constant.  This matters
because adding a time-dependent constant changes the correction (when the
resulting integral is defined) and adds its time derivative.  The Riesz
representative is in \(L^2\), so no nonzero spatial constant belongs to the
chosen class.

### 2. Exact differentiated formulas

The map

\[
 F_\epsilon(u)={1\over3}\int(r_\epsilon^3-\epsilon^3)
\]

has derivative \(DF_\epsilon(u)[h]=\int r_\epsilon u\cdot h\).  Substitution
of \(u_t=\nu\Delta u-N-\nabla p\), integration by parts, and
\(\operatorname{div}u=0\) give

\[
 {d\over dt}F_\epsilon+\nu D_\epsilon
 =-\int r_\epsilon u\cdot\nabla p
 =\int p\,u\cdot\nabla r_\epsilon=P_\epsilon.         \tag{A3}
\]

Thus the pressure term has the sign and coefficient claimed in (7).

Since \(u_t\in C_tH^{m-2}\), multiplication gives
\(u_i u_{t,j}\in C_tH^{m-2}\), and hence

\[
 p_t=R_iR_j(u_{t,i}u_j+u_i u_{t,j})
    =2R_iR_j(u_i u_{t,j})\in C_tH^{m-2}.              \tag{A4}
\]

The second equality follows by swapping the dummy symmetric indices.  For
fixed \(\epsilon>0\), the Nemytskii map
\(u\mapsto r_\epsilon-\epsilon\) is differentiable in the needed Sobolev and
Lebesgue spaces with derivative \(n_\epsilon\cdot u_t\).  The product rule
therefore gives (9).  Substituting
\(u_t=\nu\Delta u+V\), and then
\(V=-N-\nabla p\) only in the term \(p n_\epsilon\cdot V\), gives

\[
 p n_\epsilon\cdot V
 =-p\,u\cdot\nabla r_\epsilon-p n_\epsilon\cdot\nabla p. \tag{A5}
\]

This is exactly \(-P_\epsilon\) plus the last residual.  Equations
(A3)--(A5) establish (10)--(12), including both viscous corrections and both
nonlinear residuals.  A coefficient \(c\) multiplying \(B_\epsilon\) leaves
\((1-c)P_\epsilon\), so coefficient one is forced for this cancellation.

### 3. Every signed residual is integrable

The four right-hand terms of (12) are bounded, uniformly for
\(0<\epsilon\le1\) and time in \([0,T]\), by

\[
\begin{aligned}
 \left|\int(r_\epsilon-\epsilon)R_iR_j(u_i\Delta u_j)\right|
 &\le \|u\|_2 C\|u\|_\infty\|\Delta u\|_2,\\
 \left|\int p n_\epsilon\cdot\Delta u\right|
 &\le\|p\|_2\|\Delta u\|_2,\\
 \left|\int(r_\epsilon-\epsilon)R_iR_j(u_iV_j)\right|
 &\le\|u\|_2 C\|u\|_\infty\|V\|_2,\\
 \left|\int p n_\epsilon\cdot\nabla p\right|
 &\le\|p\|_2\|\nabla p\|_2.                          \tag{A6}
\end{aligned}
\]

These follow from \(|n_\epsilon|\le1\), (A2), the \(L^2\) Riesz bound, and
the product estimate \(\|u h\|_2\le\|u\|_\infty\|h\|_2\).  All norms on the
right are continuous and bounded on the compact interval by (1) and (A1).
Thus (A6) controls the signed terms themselves, without relying only on
pointwise value bounds or on Schwartz decay.

### 4. The integrated \(\epsilon\downarrow0\) passage

The maps

\[
 T_\epsilon(a)=(\epsilon^2+|a|^2)^{1/2}-\epsilon
\]

are contractions from \(L^2\) to \(L^2\), satisfy
\(0\le T_\epsilon(a)\le|a|\), and converge strongly to \(|a|\) for each
fixed input.  Uniform boundedness plus compactness of
\(u([0,T])\subset L^2\) gives

\[
 \sup_{t\in[0,T]}\|r_\epsilon(t)-\epsilon-|u(t)|\|_2\to0. \tag{A7}
\]

This and the uniform \(L^2\) bounds in (A6) pass the two terms containing
\(r_\epsilon-\epsilon\) uniformly in time.  For the two terms containing
\(n_\epsilon\), pointwise convergence
\(n_\epsilon\to n=(u/|u|)\mathbf1_{\{|u|>0\}}\), the bound
\(|n_\epsilon|\le1\), and the spacetime integrable majorants

\[
 |p||\Delta u|,\qquad |p||\nabla p|                  \tag{A8}
\]

give convergence in \(L^1(\mathbb R^3\times[0,T])\).  Their time primitives
therefore converge uniformly in the terminal time, since the supremum of a
primitive is bounded by the full spacetime \(L^1\) error.

For diffusion,

\[
 r_\epsilon|\nabla r_\epsilon|^2
 ={\sum_\alpha|u\cdot\partial_\alpha u|^2\over r_\epsilon}
 \le r_\epsilon|\nabla u|^2.                          \tag{A9}
\]

The Hilbert norm chain rule gives
\(\nabla|u|=n\cdot\nabla u\) on \(\{|u|>0\}\); coordinatewise Sobolev
zero-set calculus gives \(\nabla u=0\) almost everywhere on \(\{u=0\}\).
Thus the left side of (A9) converges pointwise to
\(|u||\nabla|u||^2\), including with value zero on the zero set.  For
\(0<\epsilon\le1\), both diffusion integrands are dominated in spacetime by

\[
 (1+|u|)|\nabla u|^2,                                 \tag{A10}
\]

which is integrable because
\(u\in C_t(W^{1,2}\cap W^{1,3})\) and
\(\int|u||\nabla u|^2\le\|u\|_3\|\nabla u\|_3^2\).
Dominated convergence proves (15) in spacetime and uniform convergence of its
time primitive.

Finally,

\[
 0\le F_\epsilon-F\le C\epsilon\|u\|_2^2,\qquad
 |B_\epsilon-B|
 \le\|p\|_2\|r_\epsilon-\epsilon-|u|\|_2,            \tag{A11}
\]

uniformly on \([0,T]\).  Equations (A7)--(A11) prove the integrated identity
(17) for every terminal time in the fixed compact interval.  They do not
yield constants uniform as \(T\uparrow T_*\).

## First bad bridge and exact repair

The first unsupported implication is the sentence identifying (18) as

\[
 DB(u)[V]
 =-P_3+2\int |u|R_iR_j(u_iV_j)-\int p n\cdot\nabla p. \tag{A12}
\]

The norm factor is not generally two-sided directionally differentiable at
zeros of \(u\).  Formally differentiating
\(B(u)=\int p(u)|u|\) along an arbitrary direction \(V\), the one-sided
derivatives contain the additional zero-set terms

\[
 D_+B(u)[V]:\quad +\int_{\{u=0\}}p|V|,
 \qquad
 D_-B(u)[V]:\quad -\int_{\{u=0\}}p|V|,               \tag{A13}
\]

in addition to the common expression (A12), whenever these derivatives are
justified.  The stated hypotheses do not imply that this zero-set integral
vanishes.  In particular, although \(N=0\) almost everywhere on
\(\{u=0\}\), the Leray projection is nonlocal, so they do not imply
\(V=-\mathbb PN=0\) there.  Sobolev approximation does not remove (A13).

The exact repair is to define the nonlinear contribution extracted from the
integrated identity by

\[
 \mathcal N_B(u;V):=
 -P_3+2\int |u|R_iR_j(u_iV_j)-\int p n\cdot\nabla p,  \tag{A14}
\]

and replace “the nonlinear first variation \(DB(u)[V]\) is” by “the
nonlinear contribution from the pressure--speed correction in the integrated
identity is \(\mathcal N_B(u;V)\).”  Equation (17) proves precisely this
statement and needs no differentiability at \(u=0\).  If an actual
two-sided derivative is desired, a sufficient additional hypothesis is
\(pV=0\) almost everywhere on \(\{u=0\}\) (with the displayed domination);
that hypothesis is not needed for the corrected mechanism.

## Audit result

**FIRST BAD BRIDGE:** interpreting the valid limiting nonlinear contribution
in (18) as the actual two-sided derivative \(DB(u)[V]\) under only (1).

**EVIDENCE:** (A1)--(A6) reconstruct the pressure derivative, exact
coefficient-one cancellation, and all four signed residual bounds.
(A7)--(A11) establish the integrated \(\epsilon=0\) passage, including zero
sets and spacetime domination.  Formula (A13) exhibits the omitted one-sided
zero-set contribution.

**REPLACEMENT ARGUMENT:** definition (A14) and the replacement sentence above.

**CONDITIONAL SUFFIX THAT SURVIVES:** the complete regularized identity (12),
the integrated limiting identity (17), and the need to estimate the full
right-hand side all survive unaltered.  The coefficient-one cancellation of
\(P_\epsilon\), and hence of \(P_3\) inside the integrated limiting identity,
is exact.

**UNNECESSARY DEPENDENCIES:** preservation of Schwartz decay and any
pointwise differentiability of \(u/|u|\) are unnecessary.  Compact-interval
\(H^m\) regularity suffices for (12) and (17).

**NON-CLAIMS:** this audit establishes no coercivity, sign for the residual,
endpoint-uniform estimate, pressure absorption, HIGH-PRESSURE estimate,
critical continuation bound, or regularity theorem.

**REOPENING CONDITION:** to reinstate literal \(DB(u)[V]\) notation, prove
that the zero-set term in (A13) vanishes under the solution hypotheses, or
state an additional hypothesis that ensures it.  No reopening condition is
needed for the repaired integrated identity.
