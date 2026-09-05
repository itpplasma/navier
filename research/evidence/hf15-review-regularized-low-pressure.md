# HF15 independent audit: regularized low-pressure extraction

Frozen input: base commit
`156b2dc95b40ce087fdb73172cb3767e1e5c0951`, with review input
`research/evidence/hf15-regularized-low-pressure.md` at SHA-256
`a71581ef9613c710ef08f5ff22243d2ca079acd7d882bf39e6a1c2893bbc4b9b`.

## Verdict

**VERDICT: PASS.**  The fixed radial regularization has the claimed derivative
bounds uniformly for \(0<\eta\le1\).  The exact split with
\(W=-N-\nabla p^H\) retains its nonzero divergence, and every occurrence of
\(\nabla p^L\) in the Euler derivative is isolated in \(A_\eta+B_\eta\).
Their time integrals have the stated input-only energy bounds, uniformly in
\(\eta\).  Convexity supplies the coherent nonnegative dissipation split.
The high-output aggregate (26) remains unestimated, as stated.

## Uniform scalar bounds

Convolving (2) over a product kernel supported at scale \(\eta\) gives
\[
 |D_vF_\eta(v,z)|
 \le C(|v|^2+|z|+\eta^2+\eta)
 \le C(|v|^2+|z|+\eta),
\]
and the value and \(z\)-tangent normalization does not change this derivative.
Thus (3), including its sole nonintegrable-looking constant term, is correct.
That term is paired only with \(\nabla p^L\), whose fixed-cutoff kernel is in
\(L^1\).

For \(z<0\), direct differentiation gives
\[
 \partial_r a_k={r\over s}\left(1-{h^2\over2s^2}\right),
 \qquad s^2=r^2+h^2.
\]
Both factors lie in \([0,1]\), so \(v\mapsto a_k(|v|,z)\) is one-Lipschitz;
the same is immediate for \(z>0\), where \(a_k=r\).  The explicit
square-root formula also gives the uniform half-Holder estimate (5) across
\(z=0\).

The centering in (6) is exact: the subtracted tangent is the convolution of
\(a_k(|y|,-s)\), using radial symmetry.  Comparing first in velocity at fixed
\(z-s\), and then in pressure, gives
\[
 |F_{\eta,z}(v,z)|\le |v|+C_k|z|^{1/2}
\]
with no \(\eta\)-dependent remainder.  Since
\(\|p^H\|_{3/2}\lesssim\|u\|_3^2\), this proves (8).

## Exact Euler split

The genuine Euler generator satisfies
\[
 V=-N-\nabla(p^L+p^H)=W-\nabla p^L,
 \qquad W=-N-\nabla p^H.
\]
Using \(\operatorname{div}N=-\Delta p\) gives
\(\operatorname{div}W=\Delta p^L\), so \(W\) is generally not solenoidal.
Substitution into both linear occurrences of \(V\) in (11) gives (12)--(13)
with the stated signs and factor two.  No integration by parts or
divergence-free cancellation involving \(W\) is used.

## Instantaneous and integrated bounds

The derivative of the fixed low-pass double-Riesz kernel is bounded near the
origin and has an integrable \(O(|x|^{-4})\) tail.  Scaling its
\(L^\infty,L^2,L^6,L^1\) norms gives respectively the four powers in (14).
Convolution against \(u_i u_j\in L^1\), of norm at most \(E\), proves those
estimates.

Using (3), Holder, and (14) yields
\[
 |A_\eta|\le C\left(2^{4J}E^2
 +2^{5J/2}E^{5/4}Y^{3/4}+\eta2^JE\right).
\]
Here \(\|p^H\|_2\lesssim\|u\|_4^2
\lesssim E^{1/4}Y^{3/4}\), so all exponents in (15) agree.  For the second
low term, multiplier boundedness and (8) give
\[
 |B_\eta|lesssim_k
 \|u\|_3\|u\|_2\|\nabla p^L\|_6
 \lesssim_k2^{7J/2}E^{7/4}Y^{1/4},
\]
using \(\|u\|_3\lesssim E^{1/4}Y^{1/4}\).  These constants are independent
of \(\eta\).

On \([0,\tau]\), \(E\le E_0\) and
\(\int_0^\tau Y\le E_0/(2\nu)\).  Holder in time gives
\[
 \int_0^\tau Y^{3/4}\le H^{1/4}(E_0/(2\nu))^{3/4},
 \qquad
 \int_0^\tau Y^{1/4}\le H^{3/4}(E_0/(2\nu))^{1/4}.
\]
Substitution proves (19)--(20), including the powers
\(E_0^2\nu^{-3/4}H^{1/4}\) and
\(E_0^2\nu^{-1/4}H^{3/4}\).  Since \(\eta\le1\), the remaining
\(\eta2^JE_0H\) term is also uniformly input-controlled.

## Coherent balance and remaining aggregate

The product convolution separates the velocity-only mollification of
\(|v|^3/3\).  Convolution preserves convexity, so its Hessian is positive
semidefinite and (22) gives \(\mathcal D_\eta\ge0\).  Extracting its heat
contribution as \(-\nu\mathcal D_\eta\), then inserting the exact Euler split,
gives (24).  Equation (25) is the same identity after algebraically adding and
subtracting \(L_J\); it does not claim that its bracket is controlled.

After applying the absolute bounds for \(A_\eta,B_\eta\), the only
uncontrolled combined term is exactly
\(\mathcal E_\eta^H+\mathcal H_\eta^{\rm rem}\).  A uniform one-sided bound
of this aggregate by a strict fraction of
\(\nu\int\mathcal D_\eta\) plus an input-only remainder would close the
regularized endpoint inequality.  Functional-value convergence could then
pass endpoint values without passing any individual differentiated term.
No such aggregate estimate is proved here.

## Audit record

**REVIEWED SCOPE:** uniform scalar derivative estimates; centered convolution;
fixed-cutoff kernel bounds; the exact non-solenoidal \(W\) split; every power
of \(E,Y,H,\nu,2^J\) in \(A_\eta,B_\eta\); convex dissipation; and the
coherent remaining high-output aggregate.

**FIRST BAD BRIDGE:** none.

**REPLACEMENT ARGUMENT:** none.

**CONDITIONAL SUFFIX THAT SURVIVES:** if the complete aggregate (26) receives
the stated uniform strict-absorption bound, (19)--(24), endpoint value
convergence, and static coercivity feed the existing conditional critical
bound.

**UNNECESSARY DEPENDENCIES:** no self-adjoint Riesz transfer, differentiated
\(\eta\)-limit, or divergence-free property of \(W\) is used.

**NON-CLAIMS:** no estimate for (26), differentiated regularization limit,
pressure absorption, HIGH-PRESSURE theorem, critical continuation bound, or
regularity result is established.

**REOPENING CONDITION:** none within the reviewed low-output extraction; the
next proof obligation is the uniform aggregate estimate for (26).
