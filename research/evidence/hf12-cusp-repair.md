# HF12: the pressure-speed cusp and a minimal coupling repair

MODE / RESULT: **FALSIFY / REPAIR.**  Using the reviewed finite-step theorem
in hf11-heat-finite-step.md, the obstruction applies to every pressure-only
correction that is locally Hölder with exponent greater than \(1/2\) on
\(L^{3/2}\).  Such a correction cannot remove the linear negative-pressure
speed cusp.  Under the explicit expansion hypotheses below, a necessary local change is to replace \(pr\) by a coupling
\(g(r,p)\) whose right speed derivative at \(r=0\) is nonnegative when
\(p<0\).  The explicit coupling
\[
 g_\tau(r,p)=p\rho_\tau(r),\qquad
 \rho_\tau(r)=\sqrt{r^2+\tau^2}-\tau,\quad \tau>0,    \tag{1}
\]
does this and preserves static coercivity, but loses the exact
coefficient-one Euler cancellation by the displayed residual below.

CLAIM AND SCOPE: The source is the reviewed and repaired finite-step theorem
`hf11-heat-finite-step.md` at `d43dfe7`. The original HF12 candidate and
independent audit are frozen at `dd04732`. This version applies the centered
pressure estimate, expansion hypotheses, and Euler-identity repairs from
`hf12-review-cusp-repair.md`.

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
uniformly along the construction. For the actual heat endpoint
\(z_N=e^{\nu t_N\Delta}(U+aw_N)\), put \(\lambda=e^{-s}\).
The pressure map is locally Lipschitz from \(L^3\) to \(L^{3/2}\), so
\[
 \|p[z_N]-p_U\|_{3/2}\le o_N(1)+Ca^2.
\]
Apply the centered hypothesis (2) directly to this pressure, obtaining
\( |\mathfrak P(p[z_N])-\mathfrak P(p_U)|
\le C(o_N(1)+Ca^2)^\alpha\). No continuity between two moving pressure
arguments is assumed. The cubic and pressure-speed terms are locally
Lipschitz in \(L^3\), so their heat-endpoint expansion is the ideal damped
packet expansion plus \(o_N(1)\). Subtracting the static expansion gives
\[
 \mathcal J_{\mathfrak P}(z_N)-\mathcal J_{\mathfrak P}(U+aw_N)
 =a(1-\lambda)A_N+O(a^2)+O(a^{2\alpha})+o_N(1).
\]
Choose \(a>0\) sufficiently small and then \(N\) large. Since
\(2\alpha>1\), the increment is positive. Thus no pressure-only correction
satisfying (2) makes (6) universally nonincreasing under the heat semigroup.

The exponent threshold in this argument is exact for its information:
pressure changes by \(O(b^2)\), so \(2\alpha>1\) is what makes the correction
smaller than the linear cusp.  The case \(\alpha\le1/2\) is not excluded;
such a correction could itself contribute at order \(b\).

## 2. Necessary local condition on a velocity-pressure coupling

Replace \(pr\) by a scalar coupling \(g(r,p)\). This subsection requires
more than continuity of its derivative. On a compact negative pressure
interval containing the background values on the packet ball, assume
\[
 \sup_p\left|{g(r,p)-g(0,p)\over r}-\gamma(p)\right|\longrightarrow0
 \quad(r\downarrow0),
\]
with \(\gamma\) continuous and an integrable envelope for this expansion.
Also assume that replacing the background pressure by the actual packet or
heat-endpoint pressure changes the integrated coupling by \(o(b)\), uniformly
in the choose-amplitude-then-frequency order, and that the heat approximation
for the remaining coupling terms has the same control. These are explicit
hypotheses, not consequences of derivative continuity alone.

Under them, the first-order packet term is
\[
 b\int_B\gamma(p_U(x))|w_N(x)|\,dx.                 \tag{8}
\]
Heat damping replaces \(b\) by \(\lambda b\), \(0<\lambda<1\).
Localizing where \(\gamma(p_U)<0\) would therefore give a positive heat
increment. Universal heat nonincrease requires
\[
 \gamma(p)\ge0\quad\text{at each accessible negative pressure value}. \tag{9}
\]
This is a necessary condition under the stated expansion hypotheses, not
an unrestricted theorem about every scalar coupling. It is not sufficient
for heat monotonicity. The original coupling has \(\gamma(p)=p<0\).

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

The repaired coupling still need not decrease under heat. For every fixed
scale, `hf12-fixed-scale-obstruction.md` gives an independently audited
finite heat-step increase. Removing the linear cusp alone is insufficient.

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
The complete Euler contribution should be written directly, without
subtracting an unregularized derivative at velocity zeros. Set
\(r_\tau=\sqrt{r^2+\tau^2}\). Since \(V=-(u\cdot\nabla)u-\nabla p\),
\[
 \begin{aligned}
 D(F+B_\tau)(u)[V]={}&
 \int p\left(1-{r\over r_\tau}\right)u\cdot\nabla r
 -\int {p\over r_\tau}u\cdot\nabla p
 +\int\rho_\tau(r)p_V,                             \tag{14}
 \end{aligned}
\]
where \(B_\tau=\int p\rho_\tau(r)\). All terms are defined on velocity
zero sets. This follows from \(DF[V]=P_3\) and the transport contribution
\(-\int p(r/r_\tau)u\cdot\nabla r\) in (13). Only the original pressure
work was canceled by the old coupling; its other Euler terms never vanished.
The first term of (14) is precisely the pressure-work contribution restored
by smoothing. For the full functional in (11), add
\(-\frac32\int\sqrt{p_-}\,p_V\) to (14), by the differentiability of the
pressure entropy integral on \(L^{3/2}\). No sign or input-only bound for
this complete expression has been established.

FIRST GAP: Control the complete Euler expression (14), including its entropy term, or find a different
coupling satisfying the necessary cusp condition (9) while retaining a
usable pressure-work cancellation.  Static coercivity and removal of the
linear cusp do not provide that control.

SURVIVING CONDITIONAL SUFFIX: Pressure-only locally Lipschitz corrections are excluded as a
route to universal heat monotonicity.  The coupling (1) is a concrete
statically coercive replacement that removes the exact local obstruction and
exposes the new Euler remainder without claiming it is bounded.

NON-CLAIMS: This note does not prove the cited finite-step theorem anew,
exclude pressure corrections with Hölder exponent at most \(1/2\), prove heat
monotonicity for (1), bound the Euler remainder, establish a Navier--Stokes
estimate, prove HIGH-PRESSURE, or imply regularity.

NEXT DISTINCT ACTION: Evaluate (14), including its entropy term,
on the complete bounded-carrier or localized-packet families.  The test must
retain \(p_V\); estimating only the first term of (14) would repeat the
frozen-weight omission.
