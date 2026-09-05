# HF11: a positive heat direction for the regularized pressure entropy

MODE / RESULT: **FALSIFY.**  The heat contribution in the fixed-regularizer
HF11 identity does not have a universal dissipative sign.  There are fixed
\(\epsilon,\delta>0\) and smooth compactly supported solenoidal fields
\(u_N\) on \(\mathbb R^3\) for which
\[
 D\mathcal K_{\epsilon,\delta}(u_N)[\Delta u_N]>0.   \tag{1}
\]
This is a static heat-generator counterexample.  It does not address the
Euler part of the evolution or the unregularized functional.

CLAIM AND SCOPE: Use the HF11 regularization
\[
 r_\epsilon=(\epsilon^2+|u|^2)^{1/2},\quad
 \rho_\epsilon=r_\epsilon-\epsilon,\quad
 \mathcal K_{\epsilon,\delta}(u)
 =\int\left\{{r_\epsilon^3-\epsilon^3\over3}
       +p\rho_\epsilon+\Phi_\delta(p)\right\},        \tag{2}
\]
where \(p=R_iR_j(u_i u_j)\) and \(\Phi_\delta\) is the smooth convex
pressure entropy normalized by
\(\Phi_\delta(0)=\Phi_\delta'(0)=0\).  In particular,
\[
 |\Phi_\delta'(q)|\le C\sqrt{|q|}                    \tag{3}
\]
with an absolute constant for the mollified construction in HF11.

EVIDENCE:

## 1. A compact background with negative pressure in a velocity-free ball

In cylindrical coordinates \((r,\vartheta,z)\), choose nonzero real
\(f,g\in C_c^\infty\) with
\[
 \operatorname{supp}f\subset(1,2),\qquad
 \operatorname{supp}g\subset(-1,1),
\]
and set
\[
 U(x)=f(r)g(z)e_\vartheta.                           \tag{4}
\]
This field is smooth, compactly supported, and divergence-free; its support
stays away from the cylindrical axis.  It vanishes on the unit ball.  Since
\(y\cdot U(y)=0\), the off-support kernel of the double Riesz transform gives
\[
 \begin{aligned}
 p_U(0)
 &=R_iR_j(U_iU_j)(0)\\
 &=\int_{\mathbb R^3}
 {3(y\cdot U(y))^2-|y|^2|U(y)|^2\over4\pi|y|^5}\,dy\\
 &=-\int_{\mathbb R^3}{|U(y)|^2\over4\pi|y|^3}\,dy<0.             \tag{5}
 \end{aligned}
\]
The pressure is smooth off \(\operatorname{supp}U\).  Hence there are a ball
\(B\Subset\{|x|<1\}\) and \(c>0\) such that
\[
 U=0\quad\hbox{and}\quad p_U\le-c\quad\hbox{on }B.   \tag{6}
\]

## 2. A bounded high-frequency solenoidal perturbation

Choose a nonzero real \(\chi\in C_c^\infty(B)\).  For integers \(N\ge1\), put
\[
 \psi_N(x)=N^{-1}\chi(x)\sin(Nx_1),\qquad
 w_N=\nabla\times(\psi_Ne_3)
      =(\partial_2\psi_N,-\partial_1\psi_N,0).        \tag{7}
\]
Then \(w_N\in C_c^\infty(B)\), \(\nabla\cdot w_N=0\), and
\[
 w_N=-\chi\cos(Nx_1)e_2
 +N^{-1}\sin(Nx_1)(\partial_2\chi,-\partial_1\chi,0). \tag{8}
\]
More precisely, the estimates needed below are
\[
 \|w_N\|_q\le C_q,\quad
 \|\Delta w_N\|_q\le C_qN^2,\quad
 \|w_N\cdot\Delta w_N+N^2\chi^2\cos^2(Nx_1)\|_q
 \le C_qN                                                     \tag{9}
\]
for every \(1\le q\le\infty\).

Fix \(\epsilon_0>0\).  For an amplitude \(a>0\), to be chosen below, define
\[
 u_N=U+aw_N,\qquad \epsilon=a\epsilon_0.             \tag{10}
\]
The supports of \(U\) and \(w_N\), including those of all their derivatives,
are separated.  Therefore
\[
 p(u_N)=p_U+a^2p_{w_N},\qquad
 R_iR_j(u_{N,i}\Delta u_{N,j})
 =R_iR_j(U_i\Delta U_j)
  +a^2R_iR_j(w_{N,i}\Delta w_{N,j}),                 \tag{11}
\]
with no linear cross term.

## 3. Exact leading positive contribution

The heat directional derivative can be used before integration by parts:
\[
 \begin{aligned}
 D\mathcal K_{\epsilon,\delta}(u)[\Delta u]
 ={}&\int\left(r_\epsilon+{p\over r_\epsilon}\right)
             u\cdot\Delta u\\
 &+2\int\left(\rho_\epsilon+\Phi_\delta'(p)\right)
             R_iR_j(u_i\Delta u_j).                 \tag{12}
 \end{aligned}
\]
On \(B\), \(r_\epsilon=a(\epsilon_0^2+|w_N|^2)^{1/2}\).
Split \(p=p_U+a^2p_{w_N}\) in the first line of (12).  The contribution with
\(p_U\) is
\[
 T_N=a\int_B p_U\,
 {w_N\cdot\Delta w_N\over(\epsilon_0^2+|w_N|^2)^{1/2}}.          \tag{13}
\]
Equations (8)--(9), periodic averaging in the \(x_1\) variable, and dominated
convergence give
\[
 {T_N\over aN^2}\longrightarrow
 Q:=-\int_Bp_U(x)\,
 \left\langle{\chi(x)^2\cos^2\theta\over
  (\epsilon_0^2+\chi(x)^2\cos^2\theta)^{1/2}}\right\rangle_\theta dx>0.
                                                               \tag{14}
\]
Strict positivity uses (6) and \(\chi\not\equiv0\).

## 4. Uniform bounds for every remaining term

All constants below may depend on \(U,\chi,\epsilon_0,\delta\), but not on
\(a\le1\) or \(N\).  Calderón--Zygmund boundedness and (9) give
\[
 \|p_{w_N}\|_{3/2}\le C,\qquad
 \|R_iR_j(w_{N,i}\Delta w_{N,j})\|_{3/2}\le CN^2.    \tag{15}
\]
The cubic-speed term supported in \(B\) is \(O(a^3N^2)\).  The
\(a^2p_{w_N}\) part of the pressure--speed derivative there is also
\(O(a^3N^2)\), using the lower bound
\((\epsilon_0^2+|w_N|^2)^{1/2}\ge\epsilon_0\), Hölder, and (15).

For the pressure-evolution term, (3), (11), and
\[
 \|\Phi_\delta'(p_U+a^2p_{w_N})\|_3
 \le C\|p_U+a^2p_{w_N}\|_{3/2}^{1/2}\le C             \tag{16}
\]
show that the high-frequency source contributes \(O(a^2N^2)\).
The \(\rho_\epsilon\) factor on \(B\) is \(O(a|w_N|)\), giving
\(O(a^3N^2)\); away from \(B\), its pairing with the nonlocal high-frequency
source is still \(O(a^2N^2)\) by its fixed uniform \(L^3\) bound.  All terms
containing only \(U,\Delta U\), as well as their changes caused by
\(a^2p_{w_N}\), are \(O(1)+O(a^2)\).  The lower-order envelope errors in
(13) are \(O(aN)\).

Consequently (12)--(16) give constants \(C_1,C_2,C_3\), independent of
\(a,N\), such that
\[
 D\mathcal K_{a\epsilon_0,\delta}(u_N)[\Delta u_N]
 \ge aN^2Q-C_1aN-C_2(a^2+a^3)N^2-C_3.               \tag{17}
\]
Choose \(a>0\) so small that
\(C_2(a^2+a^3)\le aQ/4\).  This fixes the positive regularizer
\(\epsilon=a\epsilon_0\).  Then choose \(N\) large enough that the last two
lower-order terms consume at most \(aN^2Q/4\).  Equation (17) proves (1).

FIRST GAP: none for failure of universal heat monotonicity of the
fixed-positive-regularizer functional.

SURVIVING CONDITIONAL SUFFIX: The HF11 pressure entropy remains statically
coercive.  What fails is the proposed inference that its full heat direction
must be nonpositive.  Any modified-energy use must control the positive
pressure-speed heat interaction together with the entropy pressure-source
term; scalar convexity alone cannot do so.

NON-CLAIMS: This construction does not pass
\(\epsilon,\delta\downarrow0\), compute the Euler derivative, produce a
Navier--Stokes trajectory obstruction, disprove HIGH-PRESSURE, or imply
blow-up or failure of global regularity.  The counterexample concerns the
instantaneous heat generator of the explicitly regularized functional.

NEXT DISTINCT ACTION: Determine whether the full Navier--Stokes nonlinear
contribution can compensate this positive heat direction in a spacetime
identity, or whether a different coercive correction has a genuinely
dissipative heat variation.
