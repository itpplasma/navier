# HF14: replacing full pressure by high-output pressure in the boundary functional

Status: bounded analytic reduction, 2026-09-05.

This note compares the homogeneous pressure-coupled functional formed with
the full Riesz pressure to the same functional formed with its high-output
part. The error is a fixed-cutoff, energy-controlled boundary term after an
arbitrarily small cubic loss. The estimate is uniform in the coupling
parameter \(k>0\).

## Setup

Let \(S_J\) be a fixed real-even smooth low-pass multiplier with symbol
\(\chi(2^{-J}\xi)\), where \(\chi\) is smooth, compactly supported, and one
near the origin. Put
\[
 p=R_iR_j(u_i u_j),\qquad p^L=S_Jp,\qquad p^H=(I-S_J)p.         \tag{1}
\]
For a scalar field \(\pi\), define
\[
 q_\pi=(-\pi)_+,
\]
\[
 g_k(r,\pi)=\pi\left(\sqrt{r^2+kq_\pi}-\sqrt{kq_\pi}\right),  \tag{2}
\]
\[
 \mathcal J_k[u;\pi]=\int_{\mathbb R^3}
 \left({|u|^3\over3}+g_k(|u|,\pi)+q_\pi^{3/2}\right)dx.      \tag{3}
\]
Assume only \(u\in L^2\cap L^3\), and write \(E=\|u\|_2^2\).

## Low-output kernel bounds

The convolution kernel of \(S_JR_iR_j\) has the scaling
\[
 K_J(x)=2^{3J}K_0(2^Jx).                                      \tag{4}
\]
Although the double-Riesz symbol is directional at the origin, its product
with the smooth low-pass is bounded and compactly supported in frequency.
Its inverse transform is bounded locally and has the standard
\(O(|x|^{-3})\) Riesz tail. Consequently
\[
 K_0\in L^q(\mathbb R^3)\quad\hbox{for every }q>1,             \tag{5}
\]
and
\[
 \|K_J\|_q=C_q2^{3J(1-1/q)}.                                  \tag{6}
\]
This can also be seen by writing the kernel as the principal-value Riesz
kernel convolved with the Schwartz kernel of \(S_0\), splitting at
\(|x|/2\), and using cancellation in the near part. No \(L^1\) kernel claim
is needed.

Since \(u_i u_j\in L^1\), Young's inequality gives
\[
 \boxed{\quad
 \|p^L\|_q\le C_q2^{3J(1-1/q)}E,
 \qquad 1<q<\infty.
 \quad}                                                       \tag{7}
\]
In particular,
\[
 \|p^L\|_{3/2}\le C2^JE,\qquad
 \|p^L\|_2\le C2^{3J/2}E.                                    \tag{8}
\]
The high-output multiplier is uniformly bounded on \(L^{3/2}\), so
\[
 \|p^H\|_{3/2}\le C\|u\|_3^2.                                \tag{9}
\]

## Uniform scalar Lipschitz bound

For fixed \(r\ge0\), the map \(\pi\mapsto g_k(r,\pi)\) is continuous and
piecewise differentiable. If \(\pi>0\), its derivative is \(r\). If
\(\pi<0\), set \(s=\sqrt{r^2+k(-\pi)}\) and
\(h=\sqrt{k(-\pi)}\). Direct differentiation gives
\[
 \partial_\pi g_k=(s-h){2s-h\over2s}.                         \tag{10}
\]
Both factors are nonnegative, and
\[
 0\le\partial_\pi g_k\le s-h\le r.                            \tag{11}
\]
The one-sided derivatives agree at \(\pi=0\) when \(r>0\), while the
claim at \(r=0\) follows directly from \(g_k(0,\pi)=0\). Hence, for every
\(k>0\),
\[
 \boxed{\quad
 |g_k(r,\pi_1)-g_k(r,\pi_2)|\le r|\pi_1-\pi_2|.
 \quad}                                                       \tag{12}
\]

## Boundary replacement estimate

Applying (12), Cauchy--Schwarz, and (8) gives
\[
 \left|\int g_k(|u|,p)-g_k(|u|,p^H)dx\right|
 \le\|u\|_2\|p^L\|_2
 \le C2^{3J/2}E^{3/2}.                                       \tag{13}
\]
For the entropy use the pointwise inequality
\[
 |a_-^{3/2}-b_-^{3/2}|
 \le C|a-b|\left(|a|^{1/2}+|b|^{1/2}\right).                 \tag{14}
\]
Since \(p=p^H+p^L\), Holder's inequality and (8)--(9) yield
\[
 \begin{split}
 \left|\int p_-^{3/2}-(p^H)_-^{3/2}dx\right|
 &\le C\|p^L\|_{3/2}
 \left(\|p^H\|_{3/2}^{1/2}+\|p^L\|_{3/2}^{1/2}\right)\\
 &\le C2^JE\|u\|_3+C2^{3J/2}E^{3/2}.                         \tag{15}
 \end{split}
\]
Combining (13)--(15), and then applying Young's inequality to the first
term on the last line, proves that for every \(\delta>0\),
\[
 \boxed{\quad
 |\mathcal J_k[u;p]-\mathcal J_k[u;p^H]|
 \le\delta\|u\|_3^3+C_\delta2^{3J/2}E^{3/2},
 \quad k>0.
 \quad}                                                       \tag{16}
\]
The constants are independent of \(k\). They depend on the fixed cutoff
profile, and \(C_\delta\) also depends on \(\delta\).

## Consequences and scope

The pointwise Young argument for the pressure entropy applies to any scalar
\(\pi\), so both \(\mathcal J_k[u;p]\) and
\(\mathcal J_k[u;p^H]\) separately obey
\[
 \mathcal J_k[u;\pi]\ge {1\over6}\|u\|_3^3.                  \tag{17}
\]
Estimate (16) additionally shows that replacing the full pressure by the
high-output pressure changes endpoint values only by an arbitrarily small
cubic term plus the explicit fixed-\(J\) energy remainder. On a classical
Navier--Stokes trajectory, \(E(t)\le E(0)\), so the latter is input-controlled
at every endpoint.

This is a static boundary comparison. It neither differentiates the
functional nor transfers a heat-sign counterexample from full pressure to
high-output pressure. The far-field mechanism for the full pressure does not
automatically survive \(I-S_J\), and (16) supplies no spacetime pressure
absorption estimate.

## Frontier record

**MODE / RESULT:** REPAIR. Full-pressure and high-output homogeneous boundary
functionals differ by (16), uniformly in \(k\), with an energy-only fixed-
cutoff remainder after a small cubic loss.

**FIRST GAP:** derive and control the differentiated high-output functional;
the static comparison does not determine its heat or Euler remainder.

**SURVIVING CONDITIONAL SUFFIX:** any independently obtained estimate for the
high-output functional may replace its endpoint values by the full-pressure
ones using (16), or conversely, while absorbing the chosen \(\delta\) into
the static cubic coercivity.

**NON-CLAIMS:** no derivative identity, heat sign, no-go theorem, HF estimate,
or regularity conclusion is asserted.
