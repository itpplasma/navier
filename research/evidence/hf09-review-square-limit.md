# Independent audit of the HF09 all-band square-energy limit

**VERDICT: PASS.**

## Reviewed scope

I reviewed `research/evidence/hf09-square-limit.md` at SHA-256
`3583b436f0cdd3f7260115fc26842a0a9641bde24f0727f7b6e9a1945b1aee15`,
relative to base commit
`f0196f75b2c8dd92e2ea32199baf608753e23aa5`.  The reviewed claim is only the
passage from the exact positive-regularization, finite-band identity to the
aggregate all-band, zero-regularization identity (6) on a fixed compact
classical interval \([0,T]\subset[0,T_*)\).

The Littlewood--Paley vector-valued bound (P) and the tight-frame \(L^2\)
identity are premises, not conclusions of the candidate.  This audit checks
their use but does not independently prove (P).  It also does not review any
termwise pressure, commutator, or paraproduct limit, because the candidate
claims none.

## Dependency audit

### 1. The Sobolev hypotheses supply every space used

For \(m\ge4\) in dimension three, multiplication
\(H^m\times H^{m-1}\to H^{m-1}\) is continuous.  Hence

\[
 u\cdot\nabla u\in C_tH^{m-1},\qquad
 -\mathbb P(u\cdot\nabla u)\in C_tH^{m-1}.             \tag{A1}
\]

The Leray multiplier is bounded on every \(H^s\).  Sobolev embedding gives,
for \(h=u\), \(h=u_t\), \(h=\Delta u\), and the nonlinear term at the
derivative levels actually used,

\[
 h,\nabla h\in L^2\cap L^3                              \tag{A2}
\]

whenever those derivatives occur below.  More explicitly,
\(u_t,\Delta u\in C_tH^{m-2}\subset C_t(L^2\cap L^3)\), while \(u\) and the
nonlinearity have at least one additional spatial derivative in
\(L^2\cap L^3\).  Applying (P) componentwise, including after derivatives,
and applying the tight-frame identity in \(L^2\), gives

\[
 f\in C_t(W^{1,2}\cap W^{1,3}),\quad
 f_t\in C_t(L^2\cap L^3),\quad
 g\in C_t(L^2\cap L^3).                               \tag{A3}
\]

Thus the candidate's chain-rule pairings and every displayed spatial
integral are finite.  The hypothesis \(u_t\in C_tH^{m-2}\), together with the
equation, also justifies the asserted Hilbert-array evolution
\(f_t=\nu\Delta f+g\).

### 2. Finite-coordinate tails converge uniformly in time

For fixed \(h\in L^3\), pointwise monotone exhaustion of the \(\ell^2\)
coordinates and domination by \(|Wh|_{\ell^2}^3\) prove

\[
 \|(I-P_n)Wh\|_{L^3(\ell^2)}\longrightarrow0.          \tag{A4}
\]

The analogous \(L^2\) assertion follows directly from the tight-frame
identity, and the same arguments apply after one derivative.  The operators
\(P_nW\) are uniformly bounded in each relevant space.  A uniformly bounded
operator sequence converging strongly pointwise converges uniformly on a
compact subset: cover the compact set by finitely many small balls and use
the operator bound on each ball.  Since continuous images of \([0,T]\) are
compact, this proves precisely

\[
 f_n\to f\text{ in }C_t(W^{1,2}\cap W^{1,3}),\qquad
 g_n\to g\text{ in }C_t(L^2\cap L^3).                 \tag{A5}
\]

No unproved uniform tail assertion is hidden here.

### 3. The regularized chain rule is legitimate

Let \(X=L^2(\mathbb R^3;\ell^2)\cap L^3(\mathbb R^3;\ell^2)\).  For fixed
\(\epsilon>0\),

\[
 \Phi_\epsilon(h)={1\over3}\int
 [ (\epsilon^2+|h|^2)^{3/2}-\epsilon^3]
\]

is finite on \(X\), and its derivative is
\(A_\epsilon(h)=s_\epsilon(h)h\), interpreted in
\(L^2+L^{3/2}\).  The candidate's inequality (9) implies continuity of this
derivative under convergence in \(X\): the \(\epsilon\)-part pairs in
\(L^2\), and the terms linear in \(|a|+|b|\) pair by
\(L^3\cdot L^3\subset L^{3/2}\).  By (A3), each finite-coordinate curve is
\(C^1([0,T];X)\).  The ordinary Banach-space chain rule therefore applies.

Spatial integration by parts is also justified: finite-coordinate
\(f_n\) inherits the stated Sobolev regularity, and approximation by smooth
compactly supported functions gives

\[
 -\int s_{n,\epsilon}f_n\cdot\Delta f_n
 =\int s_{n,\epsilon}|\nabla f_n|^2
  +\int s_{n,\epsilon}|\nabla s_{n,\epsilon}|^2.       \tag{A6}
\]

The second term follows from
\(f_n\cdot\partial_\alpha f_n
=s_{n,\epsilon}\partial_\alpha s_{n,\epsilon}\).
This proves the finite-band identity without requiring a decomposition of
\(g_n\).

### 4. All-band diffusion and remainder convergence

For fixed \(\epsilon>0\), the first diffusion integrand is controlled in
\(L^1\) by

\[
 \epsilon|\nabla h|^2+|h||\nabla h|^2.                \tag{A7}
\]

Strong convergence in \(W^{1,2}\cap W^{1,3}\) makes the two terms continuous
in \(L^1\): use the \(L^2\) square difference for the first and
Hölder with exponents \(3,3,3\) for the second.  For the norm-gradient term,

\[
 s_\epsilon(h)|\nabla s_\epsilon(h)|^2
 ={\sum_\alpha|\langle h,\partial_\alpha h\rangle|^2
   \over s_\epsilon(h)}
 \le s_\epsilon(h)|\nabla h|^2.                      \tag{A8}
\]

An almost-everywhere convergent subsequence has pointwise convergence in
(A8).  The right sides are uniformly integrable because their
\(\epsilon|\nabla h_n|^2\) parts converge in \(L^1\), while their
\(|h_n||\nabla h_n|^2\) parts converge in \(L^1\) by the preceding Hölder
estimate.  Vitali and the subsequence criterion yield convergence for the
full sequence.  Continuity of these functionals combined with (A5) makes the
convergence uniform in time.

For the aggregate remainder, expansion of
\(s_\epsilon(f_n)f_n\cdot g_n-s_\epsilon(f)f\cdot g\), inequality (9), and
Hölder give convergence from the \(L^2\) and \(L^3\) factors in (A5).  The
candidate's bound (12) is uniform on the compact time interval.  Therefore
the integrands converge uniformly in time, and their time primitives converge
uniformly in the endpoint \(t\).  This verifies the entire \(n\to\infty\)
passage while keeping \(g\) aggregate.

### 5. Removal of the regularization, including the zero set

The scalar estimates in (13) and
\(|s_\epsilon(f)-|f||\le\epsilon\) give uniform-in-time convergence of the
energy, remainder, and first diffusion terms using the bounded
\(C_tL^2\) norms of \(f,g,\nabla f\).

For an \(\ell^2\)-valued Sobolev map, the norm is a Lipschitz scalar
composition.  Its weak derivative obeys

\[
 \partial_\alpha|f|
 ={\langle f,\partial_\alpha f\rangle\over|f|}
 \quad\text{a.e. on }\{|f|>0\}.                       \tag{A9}
\]

Each scalar coordinate of \(f\) has weak gradient zero almost everywhere on
its zero set.  A countable intersection over the shell and velocity
coordinates therefore gives \(\nabla f=0\) almost everywhere on
\(\{f=0\}\).  Thus

\[
 {\sum_\alpha|\langle f,\partial_\alpha f\rangle|^2
  \over(\epsilon^2+|f|^2)^{1/2}}
 \longrightarrow |f||\nabla|f||^2                   \tag{A10}
\]

pointwise almost everywhere, with both sides set to zero on \(\{f=0\}\).
For \(0<\epsilon\le1\), (A8) supplies the spacetime majorant

\[
 (1+|f|)|\nabla f|^2.                                 \tag{A11}
\]

It is integrable because \(f\in C_tW^{1,2}\cap C_tW^{1,3}\), with
\(\int|f||\nabla f|^2\le\|f\|_3\|\nabla f\|_3^2\).
Dominated convergence in spacetime proves \(L^1_t\) convergence of the
second diffusion term.  Hence

\[
 \sup_{0\le t\le T}\left|\int_0^t(H_\epsilon-H_0)\,dr\right|
 \le\int_0^T|H_\epsilon-H_0|\,dr\longrightarrow0,    \tag{A12}
\]

which is exactly the claimed uniformity in the endpoint of the integrated
identity.  It is not an estimate uniform as \(T\uparrow T_*\).

## Audit result

**FIRST BAD BRIDGE:** none in the reviewed bounded limit lemma.

**EVIDENCE:** (A1)--(A3) derive every time, Sobolev, and integrability
condition used from the stated hypotheses.  (A4)--(A5) prove uniform
all-band array-tail convergence.  (A6) validates the regularized chain rule
and diffusion identity.  (A7)--(A8) establish all-band diffusion convergence.
The Hilbert-valued norm chain rule, zero-set argument, spacetime domination,
and primitive estimate are made explicit in (A9)--(A12).

**REPLACEMENT ARGUMENT:** none required.

**CONDITIONAL SUFFIX THAT SURVIVES:** the aggregate identity (6) is valid on
each fixed compact classical interval under premise (P).  A separately
proved one-sided estimate for its complete aggregate remainder could be
inserted into that identity.

**UNNECESSARY DEPENDENCIES:** the proof needs no preservation of Schwartz
decay, no pressure/commutator decomposition, and no endpoint-uniform bound.
The stated \(m\ge4\) is sufficient; optimizing it is unnecessary for this
claim.

**NON-CLAIMS:** this audit does not prove the external Littlewood--Paley
premise (P), convergence of any individual pressure or paraproduct term, a
bound uniform up to \(T_*\), signed pressure absorption, critical control,
regularity, or the Clay claim.

**REOPENING CONDITION:** none for the reviewed limit passage.  Any promotion
that removes premise (P), separates the aggregate remainder termwise, or
claims endpoint-uniform control requires a new proof and audit.
