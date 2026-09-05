# HF14 independent audit: radial scalar regularization

Frozen input: base commit
`6697f297b085c95cf0258761f9090f2b3e40e618`, with review input
`research/evidence/hf14-regularization.md` at SHA-256
`d8d981dbb0598b1eb0b934eb6038abfa26da668fc3ebff12bc1959a969774ec2`.

## Verdict

**VERDICT: PASS.**  The four-variable product mollification and subtraction of
the value and \(z\)-tangent at the origin give a globally smooth radial
density with a vanishing first jet at \((0,0)\).  It has the claimed
\(\eta\)-uniform integrable value bound, converges pointwise and in functional
value to \(F_k\), and supports the complete fixed-\(\eta\) chain-rule balance
on each compact classical \(H^m\) interval.  No differentiated
\(\eta\downarrow0\) limit follows, and none is claimed.

## Scalar and mollifier estimates

The elementary coupling bound
\(|g_k(r,z)|\le |z|r\), followed by Young's inequality, gives (3).  Direct
differentiation on the smooth regions gives (4).  The pressure derivative has
matching limits at \(z=0\) and at \(r=0,z<0\); its explicit square-root terms
are uniformly one-half Holder in \(z\), proving (5) with a constant independent
of \(r\).

Convolution with a radial kernel in \(v\) preserves rotational invariance.
Thus \(\nabla_v\widetilde F_\eta(0,z)=0\) for every \(z\), and the two
subtractions in (8) give
\(F_\eta(0,0)=0\) and \(DF_\eta(0,0)=0\).  On a fixed compact range, ordinary
Taylor's theorem therefore gives the quadratic value, linear first-derivative,
and bounded Hessian estimates (11).  These are the correct fixed-regularizer
hypotheses; a value-growth condition alone would not suffice.

For the uniform value estimate, convolution preserves the one-half Holder
seminorm of the \(z\)-derivative.  Hence the second bracket in (13), after
subtracting its tangent at zero, is bounded by \(C_k|z|^{3/2}\), uniformly in
\(\eta\).

For the first bracket, when \(r\ge\eta\), integrating the convolved velocity
derivative along the segment from zero to \(v\) gives
\[
 C_k(r^3+r^2+|z|r).
\]
The apparent mollifier errors \(\eta^2r\) and \(\eta r\) are absorbed by
\(r^3\) and \(r^2\) because \(r\ge\eta\) and \(0<\eta\le1\).  When
\(r\le\eta\), differentiating the convolution kernel and using (4) gives
\[
 \|D^2_{vv}\widetilde F_\eta\|
 \le C_k(1+\eta+|z|/\eta).
\]
Radiality removes the first-order velocity term at zero, so Taylor's theorem
gives \(C_k(r^2+|z|r^2/\eta)\le C_k(r^2+|z|r)\).  Young's inequality then
proves
\[
 |F_\eta(v,z)|\le C_k(r^3+r^2+|z|^{3/2})
\]
with no \(\eta\)-dependence.  This verifies the delicate near-zero part of
(12).

Approximate-identity convergence gives
\(\widetilde F_\eta(v,z)\to F_k(v,z)\).  The value subtraction tends to zero,
and continuity of the extended pressure derivative at the origin gives
\(\partial_z\widetilde F_\eta(0,0)\to0\).  Thus (17) holds.  For
\(u\in L^2\cap L^3\) and \(z\in L^{3/2}\), (12) supplies the integrable
majorant \(|u|^3+|u|^2+|z|^{3/2}\), proving (18) by dominated convergence.

## Fixed-regularizer evolution

On a compact interval with (19), Sobolev multiplication and boundedness of
the fixed multipliers give the regularities in (21), including a common
pointwise compact range for \((u,z)\).  The compact-range bounds (11) imply
that \(F_\eta(u,z)\) is integrable and that its time derivative pairs
\(DF_\eta(u,z)\in L^2\) with \((u_t,z_t)\in L^2\).

The pressure identity (23) has the correct signs and factor two.  Smooth
radiality makes \(\beta_\eta=f_r^\eta/r\) smooth at \(r=0\).  The first four
terms of (26) are integrable because the corresponding entries of the
four-variable Hessian are bounded on the actual range and
\(\nabla u,\nabla z\in L^2\).  For the pressure source,
\(f_z^\eta=O_{\eta,M}(|u|+|z|)\in L^2\), while
\[
 \|Q_JR_iR_j(G_{ij})\|_2
 \lesssim \|\nabla u\|_\infty\|\nabla u\|_2.
\]
The Euler source is handled identically using
\(\|u_iV_j\|_2\le\|u\|_\infty\|V\|_2\).  Sobolev approximation then
justifies the integrations by parts.  Consequently (24)--(26) form one
coherent fixed-\(\eta\) balance for the actual trajectory class.

## Closure check for the coherent regularized balance

Let
\[
 A_\eta(v)=\varphi_\eta*{|\cdot|^3\over3}(v)-
              \left(\varphi_\eta*{|\cdot|^3\over3}\right)(0).
\]
Convolution preserves convexity, so
\[
 D_\eta(u):=\int
 \nabla^2A_\eta(u)[\partial_\ell u,\partial_\ell u]\ge0. \tag{R1}
\]
Linearity of the product convolution and normalization separates this
velocity-only cubic part from the other regularized terms.  Its heat
contribution is exactly \(-\nu D_\eta\).  Define
\(\mathcal H_\eta=-\nu D_\eta+\mathcal H^\eta_{\rm rem}\) and
\[
 \mathcal R_\eta=
 \mathcal E_\eta-L_J+\mathcal H^\eta_{\rm rem}.
\]
The coherent exact identity is then
\[
 {d\over dt}\mathcal J^\eta_{k,J}+\nu D_\eta
 =L_J+\mathcal R_\eta.                                  \tag{R2}
\]

If one independently proves, uniformly in \(\eta\),
\[
 \int_0^\tau\mathcal R_\eta
 \le\theta\nu\int_0^\tau D_\eta+A,
 \qquad 0\le\theta<1,                                  \tag{R3}
\]
with \(A\) depending only on the permitted inputs, integration yields
\[
 \mathcal J^\eta_{k,J}(\tau)
 +(1-\theta)\nu\int_0^\tau D_\eta
 \le \mathcal J^\eta_{k,J}(0)+\int_0^\tau L_J+A.       \tag{R4}
\]
The nonnegative dissipation can be dropped.  The fixed-cutoff low-output
bound controls the integral of \(L_J\), and functional-value convergence at
the initial and terminal times passes the resulting uniform endpoint bound
to \(\mathcal J_{k,J}\).  Static coercivity then bounds
\(\|u(\tau)\|_3^3\).  No convergence of the differentiated identities is
required.  The unproved content is precisely the uniform aggregate estimate
(R3); the regularization does not supply it.

## Audit record

**REVIEWED SCOPE:** radial product mollification; origin normalization;
uniform value majorant, especially \(r\le\eta\); pointwise and functional
value convergence; and finiteness and validity of every term in the fixed
regularized \(H^m\) chain rule.  The review also checks the conditional
closure (R1)--(R4), without asserting the unproved aggregate bound (R3).

**FIRST BAD BRIDGE:** none.

**REPLACEMENT ARGUMENT:** none.

**CONDITIONAL SUFFIX THAT SURVIVES:** the generic HF14 balance is rigorous for
this explicit fixed regularizer, and its functional values converge to those
of the homogeneous cusp functional.

**UNNECESSARY DEPENDENCIES:** no separate cubic-growth assumption is needed
for the fixed-\(\eta\) chain rule once global \(C^2\) radiality, vanishing
first jet, compact-range Hessian bounds, and the actual compact \(H^m\)
trajectory are used.

**NON-CLAIMS:** no convergence of first or second derivatives as
\(\eta\downarrow0\), limiting differentiated identity, favorable sign,
high-output estimate, pressure absorption, continuation, or regularity result
is established.

**REOPENING CONDITION:** none within the reviewed fixed-regularizer and
functional-value scope.
