# HF13: conditional packet obstruction for the homogeneous coupling

MODE / RESULT: **CONDITIONAL FALSIFY.**  A negative directional double-Riesz
coefficient at a remote negative-pressure hole produces a finite heat-step
increase of the homogeneous functional \(\mathcal J_k\).  The packet argument
is complete under the explicit background premise below.  This note does not
construct that background.

## 1. Functional and conditional premise

Fix \(k>0\).  Write
\[
 r=|u|,\qquad q=p_-,
\]
\[
 \rho_k(r,p)=\sqrt{r^2+kq}-\sqrt{kq},\qquad
 g_k(r,p)=p\rho_k(r,p),                              \tag{1}
\]
and
\[
 \mathcal J_k(u)=\int_{\mathbb R^3}
 \left({r^3\over3}+g_k(r,p)+q^{3/2}\right)dx,
 \qquad p=R_iR_j(u_i u_j).                           \tag{2}
\]

Let
\[
 a_k(r,p)=\partial_pg_k(r,p)
 -{3\over2}\sqrt{p_-}\,\mathbf1_{\{p<0\}},            \tag{3}
\]
with its continuous scalar extensions at \(p=0\) and at \(r=0,p<0\).
Thus \(a_k(0,p)=-(3/2)\sqrt{-p}\) for \(p<0\), while
\[
 |a_k(r,p)|\le C_k(r+\sqrt{|p|}).                    \tag{4}
\]

Assume there are a compactly supported smooth solenoidal field \(U\), a ball
\(B\) disjoint from \(\operatorname{supp}U\), a unit vector \(e\), and
constants \(c,\eta>0\) such that
\[
 p_U:=R_iR_j(U_iU_j)\le-c\quad\hbox{on }B,            \tag{5}
\]
and, for a representative of the \(L^3\) function below,
\[
 A_e(x):=e_ie_jR_iR_j[a_k(|U|,p_U)](x)\le-\eta
 \quad\hbox{for almost every }x\in B.                \tag{6}
\]
Condition (6) is the unproved input.  It may be weakened to the existence of
a nonzero \(\chi\in C_c^\infty(B)\) for which
\(\int\chi^2A_e<0\).

## 2. A polarized solenoidal packet

Choose a unit vector \(\xi\perp e\) and a constant vector \(d\) such that
\(\xi\times d=e\).  For a nonzero real
\(\chi\in C_c^\infty(B)\), set
\[
 \psi_N=N^{-1}\chi(x)\sin(N\xi\cdot x),\qquad
 w_N=\nabla\times(\psi_Nd).                           \tag{7}
\]
Then \(w_N\) is smooth, compactly supported in \(B\), and solenoidal, and
\[
 w_N=\chi\cos(N\xi\cdot x)e+O_{L^s}(N^{-1})
 \quad(1\le s\le\infty).                              \tag{8}
\]
In particular all \(L^s\) norms used below are bounded uniformly in \(N\).
For \(0\le\alpha\le1\), define
\[
 u_{N,\alpha}=U+\alpha b w_N.                         \tag{9}
\]
Support separation gives the exact pressure identity
\[
 p(u_{N,\alpha})=p_U+\alpha^2b^2p_{w_N}.              \tag{10}
\]

## 3. The complete quadratic expansion

Put
\[
 H_k(r,p)=g_k(r,p)+p_-^{3/2}.
\]
The scalar pressure derivative is \(a_k=\partial_pH_k\).  It obeys, in
addition to (4), the half-Hölder estimate
\[
 |a_k(r,p')-a_k(r,p)|\le C_k\sqrt{|p'-p|}.            \tag{11}
\]
This follows directly from the two formulas for \(\partial_pg_k\) on
\(p>0\) and \(p<0\), including their matching continuous values at \(p=0\).
Consequently
\[
 |H_k(r,p+\zeta)-H_k(r,p)-a_k(r,p)\zeta|
 \le C_k|\zeta|^{3/2}.                               \tag{12}
\]
Since \(\|p_{w_N}\|_{3/2}\lesssim\|w_N\|_3^2\lesssim1\), (12) controls the
global pressure perturbation in \(L^1\), uniformly in \(N\):
\[
 \int\left|H_k(|U|,p_U+\alpha^2b^2p_{w_N})
 -H_k(|U|,p_U)-\alpha^2b^2a_k(|U|,p_U)p_{w_N}\right|
 \le C_kb^3.                                         \tag{13}
\]
This handles in particular the sets where \(p_U=0\) or \(p_U>0\); no
\(L^\infty\) estimate for \(p_{w_N}\) is used.

On \(B\), where \(U=0\) and \(p_U\le-c\), the small-speed expansion is
\[
 g_k(r,p_U)
 =-{\sqrt{(p_U)_-}\over2\sqrt k}r^2+O_{k,c}(r^4).
                                                               \tag{14}
\]
If the perturbation \(\alpha^2b^2p_{w_N}\) moves the pressure across zero on
a small exceptional set, (12) and
\(\|b^2p_{w_N}\|_{3/2}=O(b^2)\) bound its total contribution by \(O_k(b^3)\).
Equivalently, split where
\(|b^2p_{w_N}|\le c/2\), use the uniform Taylor expansion (14) there, and use
the cubic growth of \(H_k\) plus Chebyshev and Hölder on the complement.
It follows that, uniformly in \(N\) and \(\alpha\in[0,1]\),
\[
\begin{aligned}
 \mathcal J_k(u_{N,\alpha})
 =\mathcal J_k(U)+\alpha^2b^2 C_N+O_{k,U,\chi}(b^3), \tag{15}\\
 C_N=
 -{1\over2\sqrt k}\int_B\sqrt{(p_U)_-}|w_N|^2
 +\int_{\mathbb R^3}a_k(|U|,p_U)p_{w_N}.             \tag{16}
\end{aligned}
\]
The velocity-cubic packet is \(O(b^3)\), and all pressure-entropy variation
is already included in (13) and the \(a_k\) term of (16).

Double Riesz transforms are self-adjoint, so
\[
 \int a_k(|U|,p_U)p_{w_N}
 =\int R_iR_j[a_k(|U|,p_U)](w_N)_i(w_N)_j.            \tag{17}
\]
The bound (4), \(U\in L^3\), and \(p_U\in L^{3/2}\) imply
\(a_k(|U|,p_U)\in L^3\); hence the right side is a legitimate
\(L^3\)-\(L^{3/2}\) pairing.  Periodic averaging in (8) now gives
\[
 C_N\longrightarrow C_*:=
 -{1\over4\sqrt k}\int_B\sqrt{(p_U)_-}\chi^2
 +{1\over2}\int_B\chi^2A_e.                          \tag{18}
\]
Both terms are strictly negative under (5)--(6).  Thus \(C_*<0\).

## 4. Turning the static coefficient into a heat increase

Fix \(\sigma>0\), and put
\[
 t_N={\sigma\over N^2},\qquad \lambda=e^{-\sigma}\in(0,1). \tag{19}
\]
The Fourier-shift argument for a smooth modulated envelope gives
\[
 \|e^{t_N\Delta}w_N-\lambda w_N\|_3\to0,\qquad
 \|e^{t_N\Delta}U-U\|_3\to0.                         \tag{20}
\]
Thus
\[
 e^{t_N\Delta}u_{N,1}-u_{N,\lambda}\to0
 \quad\hbox{in }L^3.                                 \tag{21}
\]

The functional \(\mathcal J_k\) is locally Lipschitz on \(L^3\).  Indeed,
\[
 \|p(u)-p(v)\|_{3/2}
 \le C(\|u\|_3+\|v\|_3)\|u-v\|_3,                   \tag{22}
\]
while the scalar derivatives satisfy
\[
 |\partial_rg_k|\le|p|,\qquad
 |\partial_pH_k|=|a_k|\le C_k(r+\sqrt{|p|}).          \tag{23}
\]
Hölder applied along the line segment between two inputs proves the local
Lipschitz bound, including the cusps by approximation.  Hence
\[
 \mathcal J_k(e^{t_N\Delta}u_{N,1})
 -\mathcal J_k(u_{N,\lambda})\to0.                   \tag{24}
\]

Choose \(b>0\) so small that the uniform \(O(b^3)\) errors in (15), at
\(\alpha=1\) and \(\alpha=\lambda\), consume less than
\((1-\lambda^2)|C_*|b^2/8\).  Then choose \(N\) large enough that
\(C_N\le C_*/2<0\) and the error in (24) consumes less than the same amount.
Subtracting (15) at \(\alpha=1\) from its value at \(\alpha=\lambda\) gives
\[
\begin{aligned}
 \mathcal J_k(e^{t_N\Delta}u_{N,1})
 -\mathcal J_k(u_{N,1})
 &=(\lambda^2-1)b^2C_N+O(b^3)+o_N(1)>0.             \tag{25}
\end{aligned}
\]
Thus \(h=u_{N,1}\) is a compactly supported smooth solenoidal heat-step
counterexample for this fixed \(k\).

## 5. Scope

CLAIM AND SCOPE: Under the explicit background hypothesis (5)--(6), for the
fixed \(k>0\) there exist \(h\in C_c^\infty(\mathbb R^3;\mathbb R^3)\) with
\(\nabla\cdot h=0\) and \(t>0\) satisfying
\[
 \mathcal J_k(e^{t\Delta}h)>\mathcal J_k(h).
\]

EVIDENCE: The global Nemytskii estimate (12)--(13) handles every pressure
variation, including positive-pressure and cusp regions.  Self-adjointness
moves the nonlocal pressure perturbation onto the exact coefficient \(a_k\);
the polarized packet then gives the negative coefficient (18).  Local
\(L^3\) continuity transfers this static comparison to a finite heat step.

FIRST GAP: construct, or refute the existence of, a compact solenoidal
background satisfying (5)--(6).  This note proves only the conditional
consumer.

SURVIVING CONDITIONAL SUFFIX: Any verified background with the stated
negative directional coefficient rules out universal heat monotonicity of
the corresponding homogeneous \(\mathcal J_k\).

NON-CLAIMS: The background premise is not proved here.  No statement is made
for every \(k\), for the Euler residual, for a Navier--Stokes trajectory, for
HIGH-PRESSURE, or for regularity.

NEXT DISTINCT ACTION: evaluate
\(e_ie_jR_iR_j[a_k(|U|,p_U)]\) on an explicit remote-pressure background,
with a certified sign on a velocity-free negative-pressure ball.
