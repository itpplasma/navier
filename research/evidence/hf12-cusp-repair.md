# HF12: the pressure-speed cusp and a minimal coupling repair

MODE / RESULT: **FALSIFY / REPAIR.**  Conditional on the finite-step theorem
in hf11-heat-finite-step.md, the obstruction applies to every pressure-only
correction that is locally Hölder with exponent greater than \(1/2\) on
\(L^{3/2}\).  Such a correction cannot remove the linear negative-pressure
speed cusp.  A necessary local change is to replace \(pr\) by a coupling
\(g(r,p)\) whose right speed derivative at \(r=0\) is nonnegative when
\(p<0\).  The explicit coupling
\[
 g_\tau(r,p)=p\rho_\tau(r),\qquad
 \rho_\tau(r)=\sqrt{r^2+\tau^2}-\tau,\quad \tau>0,    \tag{1}
\]
does this and preserves static coercivity, but loses the exact
coefficient-one Euler cancellation by the displayed residual below.

CLAIM AND SCOPE: The source construction is the pending-review finite-step
candidate research/evidence/hf11-heat-finite-step.md, SHA-256
326f24a3ffe0e1f46de065c493ce83dff2e5698b5137f21acf0ab7489333e516.
The abstraction here does not independently promote that theorem.  Assuming
its remote background \(U\), packets \(w_N\), heat time
\(t_N=s/(\nu N^2)\), and estimates, the conclusions below are exact.

EVIDENCE:

## 1. Pressure-only corrections cannot remove the cusp

Let \(\mathfrak P:L^{3/2}(\mathbb R^3)\to\mathbb R\) be a pressure-only
functional satisfying, in a neighborhood of \(p_U\),
\[
 |\mathfrak P(q)-\mathfrak P(p_U)|
 \le C\|q-p_U\|_{3/2}^{\alpha}
 \quad\hbox{for some }\alpha>{1\over2}.              \tag{2}
\]
This includes every locally Lipschitz pressure functional, such as
\(\mathfrak P(p)=\int p_-^{3/2}\).

For the disjoint fields in the finite-step candidate,
\[
 p[U+bw_N]=p_U+b^2p[w_N],\qquad
 \sup_N\|p[w_N]\|_{3/2}<\infty.                      \tag{3}
\]
Therefore (2) gives, uniformly in \(N\),
\[
 \mathfrak P(p[U+bw_N])-\mathfrak P(p_U)
 =O(b^{2\alpha})=o(b).                              \tag{4}
\]
The speed-pressure term has the independently identified expansion
\[
 \int p[U+bw_N]|U+bw_N|
 =\int p_U|U|-bA_N+O(b^2),\qquad A_N\to A_*>0.       \tag{5}
\]
The cubic packet is \(O(b^3)\).  Hence every functional
\[
 \mathcal J_{\mathfrak P}(u)
 ={1\over3}\|u\|_3^3+\int p[u]|u|+\mathfrak P(p[u]) \tag{6}
\]
satisfies
\[
 \mathcal J_{\mathfrak P}(U+bw_N)
 =\mathcal J_{\mathfrak P}(U)-bA_N+o(b)             \tag{7}
\]
uniformly along the construction.  Replacing \(b=a\) by
\(b=e^{-s}a\) under the short high-frequency heat step reverses this linear
decrease.  The proof of the pending finite-step theorem then applies with
\(o(a)\) in place of \(O(a^2)\): choose \(a\) first, then \(N\).  Thus no
pressure-only correction satisfying (2) can make (6) universally
nonincreasing under the heat semigroup.

The exponent threshold in this argument is exact for its information:
pressure changes by \(O(b^2)\), so \(2\alpha>1\) is what makes the correction
smaller than the linear cusp.  The case \(\alpha\le1/2\) is not excluded;
such a correction could itself contribute at order \(b\).

## 2. Necessary local condition on a velocity-pressure coupling

Replace \(pr\) by a scalar coupling \(g(r,p)\), and suppose the right
derivative \(g_r(0+,p)\) exists and is continuous in \(p\) on the negative
pressure range used by the remote background.  On the ball where
\(U=0\), \(p_U<0\), and the packet is supported, disjointness and
\(p[U+bw_N]=p_U+O_{L^{3/2}}(b^2)\) give the formal first-order term
\[
 b\int_B g_r(0+,p_U(x))\,|w_N(x)|\,dx.               \tag{8}
\]
Under the same local continuity and domination needed to justify this
expansion, heat damping replaces \(b\) by \(\lambda b\), \(0<\lambda<1\).
For a universally nonincreasing heat functional, (8) therefore cannot be
negative for packets localized near any point.  The necessary pointwise
condition is
\[
 \boxed{\quad g_r(0+,p)\ge0\quad\text{for every accessible }p<0.\quad}       \tag{9}
\]
The original coupling \(g(r,p)=pr\) has \(g_r(0+,p)=p<0\), which is exactly
the failed cusp.  Condition (9) is necessary for this mechanism; it is not
sufficient for heat monotonicity.

## 3. A minimal smooth-speed repair

The coupling (1) is smooth as a function of the velocity vector because
\(\rho_\tau(|u|)=\sqrt{\tau^2+|u|^2}-\tau\), and
\[
 \partial_r g_\tau(r,p)={pr\over\sqrt{r^2+\tau^2}},
 \qquad \partial_r g_\tau(0,p)=0.                   \tag{10}
\]
It removes the linear cusp.  It also preserves the HF11 static coercivity:
for \(p<0\), \(0\le\rho_\tau(r)\le r\) implies
\(p\rho_\tau(r)\ge pr\), while for \(p\ge0\) this term is nonnegative.
Consequently
\[
 \int\left\{{|u|^3\over3}+p\rho_\tau(|u|)+p_-^{3/2}\right\}
 \ge {1\over6}\|u\|_3^3.                            \tag{11}
\]
The matching cubic upper bound follows as before from
\(\rho_\tau(r)\le r\) and Riesz boundedness.

## 4. Exact Euler-cancellation defect

Let \(V=-\mathbb P((u\cdot\nabla)u)\), and write
\[
 p_V:=Dp(u)[V]=2R_iR_j(u_iV_j).                     \tag{12}
\]
For fixed \(\tau>0\), the repaired coupling has the classical directional
derivative
\[
 D\!\left[\int p\rho_\tau(r)\right][V]
 =\int {p\over\sqrt{r^2+\tau^2}}\,u\cdot V
   +\int\rho_\tau(r)p_V.                            \tag{13}
\]
Where the unregularized derivative is legitimate, its corresponding formula
is
\[
 D\!\left[\int pr\right][V]
 =\int {p\over r}\,u\cdot V+\int r p_V.             \tag{14}
\]
Thus the exact defect introduced into any coefficient-one cancellation is
\[
 \boxed{\begin{aligned}
 \mathcal D_\tau(u;V)={}&
 \int p\left({1\over\sqrt{r^2+\tau^2}}-{1\over r}\right)u\cdot V\\
 &+\int\left(\sqrt{r^2+\tau^2}-\tau-r\right)p_V .
 \end{aligned}}                                    \tag{15}
\]
Formula (15) is asserted on \(\{r>0\}\) under hypotheses that justify (14);
equivalently, (13) is the globally valid fixed-\(\tau\) formula and should be
used at velocity zero sets.  If an earlier identity gives exact cancellation
between \(D(\|u\|_3^3/3)[V]\) and \(D(\int pr)[V]\), replacing \(pr\) by
\(p\rho_\tau(r)\) leaves precisely \(\mathcal D_\tau(u;V)\).  No sign or
closure for this defect follows from (15).

FIRST GAP: Control the full repaired Euler defect (13), or find a different
coupling satisfying the necessary cusp condition (9) while retaining a
usable pressure-work cancellation.  Static coercivity and removal of the
linear cusp do not provide that control.

SURVIVING CONDITIONAL SUFFIX: Subject to review of the cited finite-step
candidate, pressure-only locally Lipschitz corrections are excluded as a
route to universal heat monotonicity.  The coupling (1) is a concrete
statically coercive replacement that removes the exact local obstruction and
exposes the new Euler remainder without claiming it is bounded.

NON-CLAIMS: This note does not prove the cited finite-step theorem anew,
exclude pressure corrections with Hölder exponent at most \(1/2\), prove heat
monotonicity for (1), bound \(\mathcal D_\tau\), establish a Navier--Stokes
estimate, prove HIGH-PRESSURE, or imply regularity.

NEXT DISTINCT ACTION: Evaluate (13) together with the cubic Euler derivative
on the complete bounded-carrier or localized-packet families.  The test must
retain \(p_V\); estimating only the first line of (15) would repeat the
frozen-weight omission.
