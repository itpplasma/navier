# HF09: aggregate all-band limit for the square energy

Status: bounded analytic repair at frozen base
`f0196f75b2c8dd92e2ea32199baf608753e23aa5`, 2026-09-05.

This note justifies the all-band and zero-regularization limits in the exact
square-energy identity on a compact interval of classical existence.  It
does not decompose the nonlinearity into paraproducts and makes no assertion
about the sign or size of the resulting aggregate remainder.

## Premise on the frame

Let \(Wv=(\Delta_jv)_{j\in\mathbb Z}\) be a smooth homogeneous tight
Littlewood--Paley analysis operator on \(\mathbb R^3\), acting componentwise.
The one external analytic premise used below is
\[
 W:L^3(\mathbb R^3)\longrightarrow L^3(\mathbb R^3;\ell^2)
 \quad\hbox{boundedly},                                      \tag{P}
\]
together with the tight-frame \(L^2\) identity.  The multipliers commute with
spatial derivatives.  Thus (P) also applies after a derivative.  If
\(P_n\) denotes restriction to finite sets \(I_n\uparrow\mathbb Z\), then
\(P_nWv\to Wv\) strongly in the displayed spaces: this follows first for a
fixed \(v\) by dominated convergence of the pointwise \(\ell^2\) tails, and
uniformly for \(v\) in a compact subset by uniform boundedness of \(P_nW\).

## Statement

Let \(0<T<T_*\), and let \(u\) be an actual classical unforced
Navier--Stokes solution on \(\mathbb R^3\times[0,T]\) satisfying
\[
 u\in C([0,T];H^m),\qquad u_t\in C([0,T];H^{m-2}),\qquad m\ge4.       \tag{1}
\]
Put
\[
 f=Wu,\qquad g=W[-\mathbb P(u\cdot\nabla u)],\qquad f_n=P_nf,
 \qquad g_n=P_ng,
\]
and, for \(\epsilon>0\),
\[
 s_{n,\epsilon}=(\epsilon^2+|f_n|_{\ell^2}^2)^{1/2},\qquad
 F_{n,\epsilon}={1\over3}\int
 (s_{n,\epsilon}^3-\epsilon^3)\,dx.                         \tag{2}
\]
Here and below the Euclidean velocity index is included in the Hilbert-array
norm.  Then
\[
 F_{n,\epsilon}(t)+\nu\int_0^tD_{n,\epsilon}(r)\,dr
 =F_{n,\epsilon}(0)+\int_0^tR_{n,\epsilon}(r)\,dr,            \tag{3}
\]
where
\[
 R_{n,\epsilon}=\int s_{n,\epsilon} f_n\cdot g_n\,dx,         \tag{4}
\]
\[
 D_{n,\epsilon}=\int s_{n,\epsilon}|\nabla f_n|^2\,dx
 +\int s_{n,\epsilon}|\nabla s_{n,\epsilon}|^2\,dx.        \tag{5}
\]
Both \(n\to\infty\) and then \(\epsilon\downarrow0\) pass through (3),
uniformly in its endpoint \(t\in[0,T]\).  The resulting identity is
\[
 {1\over3}\int |f(t)|^3dx
 +\nu\int_0^t\!\int
 \bigl(|f||\nabla f|^2+|f||\nabla|f||^2\bigr)\,dx\,dr
 ={1\over3}\int |f(0)|^3dx
 +\int_0^t\!\int |f|f\cdot g\,dx\,dr.                       \tag{6}
\]
The last integrand is the complete Leray-projected nonlinearity.  Formula
(6) does not assert convergence of any separately extracted pressure,
commutator, or paraproduct contribution.

## Proof

Sobolev multiplication and embedding in dimension three, with \(m\ge4\),
give
\[
 u\cdot\nabla u\in C([0,T];H^{m-1}),
\]
so the boundedness of the Leray projection on the Sobolev spaces implies
\(g\in C H^{m-1}(\ell^2)\).  In particular, uniformly on \([0,T]\),
\[
 f\in W^{1,3}(\ell^2)\cap W^{1,2}(\ell^2),qquad
 g\in L^3(\ell^2)\cap L^2(\ell^2).                            \tag{7}
\]
The frame premise and compactness of the images of \([0,T]\) in these
Banach spaces yield
\[
 f_n\to f\quad\hbox{in }C_t(W^{1,3}\cap W^{1,2}),\qquad
 g_n\to g\quad\hbox{in }C_t(L^3\cap L^2).                    \tag{8}
\]

Since \(f_t=\nu\Delta f+g\), the same finite-coordinate equation holds for
\(f_n\).  The integral functional in (2) is continuously differentiable
along this curve.  Indeed its derivative is the pairing with
\[
 A_\epsilon(z)=(\epsilon^2+|z|^2)^{1/2}z,
\]
and
\[
 |A_\epsilon(a)-A_\epsilon(b)|
 \le C(\epsilon+|a|+|b|)|a-b|.                               \tag{9}
\]
Thus the derivative pairing is controlled by the \(L^2\) norms for the
\(\epsilon\)-part and by \(L^3\)-\(L^{3/2}\) duality for the quadratic
part.  Applying the ordinary chain rule and integrating the Laplacian by
parts gives (3)--(5).  This derivation uses the aggregate \(g_n\), so no
frequency interaction has been omitted.

For completeness, the diffusion passage is a continuity statement for the
norm map on a Hilbert-valued Sobolev space.  For \(h\in
W^{1,3}(\ell^2)\cap W^{1,2}(\ell^2)\),
\[
 \partial_\alpha(\epsilon^2+|h|^2)^{1/2}
 ={\langle h,\partial_\alpha h\rangle\over
       (\epsilon^2+|h|^2)^{1/2}},                              \tag{10}
\]
and hence
\[
 0\le s_\epsilon(h)|\nabla s_\epsilon(h)|^2
 \le s_\epsilon(h)|\nabla h|^2.                              \tag{11}
\]
Strong convergence in \(W^{1,3}\cap W^{1,2}\), (10), and (11) imply
continuity of each integral in (5): the cubic part is controlled by
\(\|h\|_3\|\nabla h\|_3^2\), and the regularizing part by
\(\epsilon\|\nabla h\|_2^2\).  One may prove the second integral first
along an a.e.-convergent subsequence; these bounds give uniform
integrability, hence convergence, and the usual subsequence criterion gives
the full sequence.  Equations (8)--(9) similarly imply convergence of (4),
uniformly in time, using
\[
 \epsilon\|f_n\|_2\|g_n\|_2
 +\|f_n\|_3^2\|g_n\|_3                                      \tag{12}
\]
as a uniform bound.  The energy terms converge by the same \(L^2\) and
\(L^3\) estimates.  All these bounds are uniform in \(n\) and integrable in
time on the finite interval, proving the \(n\to\infty\) passage in (3).

It remains to remove \(\epsilon\).  For \(r\ge0\),
\[
 0\le {1\over3}\bigl((\epsilon^2+r^2)^{3/2}-\epsilon^3-r^3\bigr)
 \le C\epsilon r^2,                                          \tag{13}
\]
so the energy error is at most \(C\epsilon\|f\|_2^2\).  Also
\[
 |s_\epsilon(f)-|f||\le\epsilon,
\]
which makes the remainder error at most
\(\epsilon\|f\|_2\|g\|_2\), uniformly in time.  The first diffusion
term converges with error at most
\(\epsilon\|\nabla f\|_2^2\).  Finally the Hilbert-valued Sobolev norm
chain rule gives
\[
 \nabla|f|={\langle f,\nabla f\rangle\over|f|}
 \quad\hbox{on }\{|f|>0\},
\]
and \(\nabla f=0\) almost everywhere on \(\{f=0\}\).  Consequently the
second integrand in (5) converges pointwise to
\(|f||\nabla|f||^2\), with zero value on the zero set, and (11) is dominated
for \(0<\epsilon\le1\) by
\[
 (1+|f|)|\nabla f|^2\in L^1([0,T]\times\mathbb R^3).          \tag{14}
\]
Dominated convergence completes the \(\epsilon\downarrow0\) passage and
proves (6).

## Scope

The proof uses only Sobolev regularity on the compact interval and does not
assume that Navier--Stokes evolution preserves Schwartz decay.  Its constants
depend on the \(C_tH^m\) bounds on \([0,T]\).  It supplies no estimate
uniform as \(T\uparrow T_*\), no endpoint control, and no new producer for a
one-sided bound on the aggregate remainder.

## Frontier record

**MODE / RESULT:** REPAIR.  The differentiated finite-band identity has a
rigorous all-band and \(\epsilon=0\) integrated limit on every compact
classical interval, provided the stated square-function premise (P).

**FIRST GAP:** none for this bounded analytic limit.  Any useful sign or
endpoint estimate for the aggregate remainder remains separate.

**SURVIVING CONDITIONAL SUFFIX:** an independently proved one-sided bound on
the aggregate remainder in (6) may be applied to the exact identity.

**NON-CLAIMS:** no individual paraproduct limit, sign calculation, endpoint
producer, blow-up exclusion, or global regularity result is asserted.
