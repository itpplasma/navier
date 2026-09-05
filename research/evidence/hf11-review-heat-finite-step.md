# HF11 independent audit: finite heat increase

Frozen input: base commit
`4338abe156ec7e13f1ef9fc18ad405a4e46f2991`, with sole review input
`research/evidence/hf11-heat-finite-step.md` at SHA-256
`326f24a3ffe0e1f46de065c493ce83dff2e5698b5137f21acf0ab7489333e516`.

## Verdict

**VERDICT: REPAIR.**  The construction and all load-bearing analytic estimates
are valid.  The statement at (2) leaves \(\nu\) free.  The proof in fact gives
the stronger and correctly quantified assertion
\[
 \exists h\in C_c^\infty(\mathbb R^3;\mathbb R^3),\quad
 \nabla\cdot h=0,\quad
 \forall \nu>0\ \exists t_\nu>0:
 \mathcal K(e^{\nu t_\nu\Delta}h)>\mathcal K(h).
\]
Thus this is an exact statement repair, not a defect in the mechanism.

## Dependency-order audit

The pressure convention is consistent.  With
\(R_iR_j=\partial_i\partial_j(-\Delta)^{-1}\), its kernel away from the
origin is
\[
 {1\over4\pi}{3y_i y_j-|y|^2\delta_{ij}\over |y|^5}.
\]
On the azimuthal swirl, \(U(y)\cdot y=0\), so contraction with
\(U_iU_j\) gives exactly the strictly negative integrand in (5).  Since the
support is separated from the origin, no principal-value or delta term enters
that evaluation.  Continuity then gives a ball on which \(p[U]\leq-c_*\).

The packet in (7) is a curl, is supported in that ball, and has the displayed
formula.  Its \(L^q\) norms are uniformly bounded.  Pointwise,
\[
 \bigl||w_N|-|\psi\cos(Nx_1)|\bigr|\leq C N^{-1}|\nabla\psi|,
\]
so weighted periodic averaging proves (8), including positivity of \(A_*\).
No unmentioned uniform oscillatory estimate is needed.

Disjoint support kills the quadratic pressure cross term pointwise:
\((U_i+bw_i)(U_j+bw_j)=U_iU_j+b^2w_iw_j\).  Hence (12) is exact.  Expanding
the pressure-speed term gives
\[
 \int (p[U]+b^2p[w_N])(|U|+b|w_N|)
 =\int p[U]|U|-bA_N
  +b^2\int p[w_N]|U|+b^3\int p[w_N]|w_N|.
\]
The last two integrals are uniformly bounded by the uniform \(L^3\) bound
and the \(L^3\times L^3\to L^{3/2}\) pressure estimate.  The cubic packet
term is \(O(b^3)\).  Finally,
\[
 \|p_-^{3/2}-q_-^{3/2}\|_1
 \leq C(\|p\|_{3/2}^{1/2}+\|q\|_{3/2}^{1/2})
       \|p-q\|_{3/2}
\]
and \(p[U+bw_N]-p[U]=b^2p[w_N]\), so the entropy error is uniformly
\(O(b^2)\).  This proves (13) with an \(N\)-independent constant.

For the heat step, direct differentiation of (7) gives
\(\|(\Delta+N^2)w_N\|_3=O(N)\).  Heat contraction in the displayed Duhamel
identity over \(t_N=s/(\nu N^2)\) gives (9); the same contraction and the
fundamental theorem of calculus give (10).  The constants after this time
choice do not depend on \(\nu\).  The pressure map and all three terms in
\(\mathcal K\) are locally Lipschitz on \(L^3\), and the relevant \(L^3\)
norms lie in one bounded set.  Thus the use of local Lipschitz continuity in
(14) is uniform in \(N\).

The error order in (15) is sufficient.  First fix \(s>0\), then choose \(a\)
so the uniform \(O(a^2)\) term is strictly below
\(a(1-e^{-s})A_*/4\), and finally choose \(N\) so that \(A_N>A_*/2\) and
the fixed-\(a\) heat-approximation error has the same strict bound.  The
resulting difference is positive.  Neither \(a\) nor \(N\), hence neither
\(h=U+aw_N\), depends on \(\nu\); only
\(t_\nu=s/(\nu N^2)\) does.  This proves the repaired quantified statement.

## Audit record

**REVIEWED SCOPE:** construction of a compactly supported smooth solenoidal
field for which the unregularized functional increases over a finite linear
heat step; kernel sign, exact pressure expansion, oscillatory bounds, heat
approximation, \(L^3\) continuity, and error quantifiers.

**FIRST BAD BRIDGE:** equation (2) is stated with an unquantified \(\nu\).

**REPLACEMENT ARGUMENT:** replace the statement by the quantified assertion
above.  The existing proof establishes it without any further hypothesis.

**CONDITIONAL SUFFIX THAT SURVIVES:** all analytic steps (3)--(15), and the
conclusion that universal heat monotonicity of \(\mathcal K\) is false.

**UNNECESSARY DEPENDENCIES:** none material.  The construction only needs a
nonzero compact azimuthal swirl separated from a packet ball and standard
Calderon--Zygmund and heat-contraction bounds.

**NON-CLAIMS:** this audit makes no assertion about a Navier--Stokes
trajectory, cancellation with the Euler term, HIGH-PRESSURE, continuation,
blowup, or global regularity.

**REOPENING CONDITION:** none after the displayed quantifier repair.
