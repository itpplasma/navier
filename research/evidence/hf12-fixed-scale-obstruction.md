# HF12: every fixed speed scale admits a heat-step increase

MODE / RESULT: **FALSIFY.**  For every fixed \(\tau>0\), the coercive
fixed-scale functional
\[
 \mathcal J_\tau(u)=\int_{\mathbb R^3}
 \left({|u|^3\over3}+p(u)\rho_\tau(|u|)+p(u)_-^{3/2}\right)dx,
 \qquad
 \rho_\tau(s)=\sqrt{\tau^2+s^2}-\tau,                 \tag{1}
\]
where \(p(u)=R_iR_j(u_i u_j)\), is not monotone under the linear heat
semigroup.  There are a compactly supported smooth solenoidal field \(h\)
and \(t>0\) such that
\[
 \mathcal J_\tau(e^{t\Delta}h)>\mathcal J_\tau(h).    \tag{2}
\]

This is a fixed-\(\tau\), static heat-semigroup obstruction.  It does not
address a state-dependent scale or the full Navier--Stokes evolution.

## 1. Remote negative-pressure background

Use the compactly supported azimuthal field from HF11:
\[
 U(x)=f(r)g(z)e_\vartheta,
\]
with cylindrical support \(1<r<2\), \(|z|<1\).  It is smooth and
divergence free and vanishes on the Euclidean unit ball.  Since
\(y\cdot U(y)=0\), the off-support double-Riesz kernel gives
\[
 p_U(0)
 =-\int_{\mathbb R^3}{|U(y)|^2\over4\pi|y|^3}\,dy<0. \tag{3}
\]
Fix a ball \(B\Subset\{|x|<1\}\) and \(c>0\) such that
\[
 U=0,\qquad p_U\le-c\quad\hbox{on }B.                \tag{4}
\]
Choose a nonzero real \(\chi\in C_c^\infty(B)\), and define
\[
 \psi_N=N^{-1}\chi(x)\sin(Nx_1),\qquad
 w_N=\nabla\times(\psi_Ne_3).                        \tag{5}
\]
Then
\[
 w_N=-\chi\cos(Nx_1)e_2+O_{C^k}(N^{k-1})
\]
at derivative order \(k\), and in particular
\[
 \sup_N\|w_N\|_q<\infty\quad(1\le q\le\infty).       \tag{6}
\]
The supports of \(U\) and \(w_N\), including all their derivatives, are
disjoint.

For parameters \(M>0\), \(0<b\le1\), and \(0\le\alpha\le1\), put
\[
 h_{N,\alpha}=MU+\alpha b w_N.                       \tag{7}
\]
Pointwise support separation gives the exact pressure decomposition
\[
 p(h_{N,\alpha})=M^2p_U+\alpha^2b^2p_{w_N}.          \tag{8}
\]

## 2. Static expansion uniform in the carrier

The elementary identity
\[
 \rho_\tau(s)={s^2\over\sqrt{\tau^2+s^2}+\tau}
\]
implies, uniformly for \(0\le s\le b\sup_N\|w_N\|_\infty\) once \(b\) is
sufficiently small relative to \(\tau\),
\[
 \rho_\tau(s)={s^2\over2\tau}
 +O\!\left({s^4\over\tau^3}\right).                  \tag{9}
\]
Thus the background-pressure coupling on \(B\) is
\[
\begin{aligned}
 M^2\int_Bp_U\rho_\tau(\alpha b|w_N|)
 ={}&{\alpha^2b^2M^2\over2\tau}
       \int_Bp_U|w_N|^2\\
 &+O\!\left({M^2b^4\over\tau^3}\right).              \tag{10}
\end{aligned}
\]

Periodic averaging and (5) give
\[
 A_N:=\int_B(-p_U)|w_N|^2\longrightarrow
 A:={1\over2}\int_B(-p_U)\chi^2>0.                  \tag{11}
\]

All other changes from the background value
\(\mathcal J_\tau(MU)\) have lower amplitude order.  More precisely, for
\(\alpha\in[0,1]\),
\[
\begin{aligned}
 \mathcal J_\tau(h_{N,\alpha})
 =\mathcal J_\tau(MU)
 -{\alpha^2b^2M^2\over2\tau}A_N+E_{N,\alpha},        \tag{12}\\
 |E_{N,\alpha}|
 \le C_\tau\left(
 Mb^2+b^3+{b^4\over\tau}
       +{M^2b^4\over\tau^3}\right).                  \tag{13}
\end{aligned}
\]
Here \(C_\tau\) is independent of \(M\ge1\), \(b\le1\), \(N\), and
\(\alpha\); harmless fixed powers of \(\tau\) are displayed separately only
where they matter in the parameter choice.

To verify that (13) includes every nonlocal term, first
\[
 \|p_{w_N}\|_{3/2}\le C\|w_N\|_3^2\le C.             \tag{14}
\]
The coupling of this pressure change to the remote velocity is bounded by
\[
 \alpha^2b^2
 \left|\int p_{w_N}\rho_\tau(M|U|)\right|
 \le C Mb^2,                                         \tag{15}
\]
using \(0\le\rho_\tau(s)\le s\).  Its self-coupling on \(B\) is
\(O(b^4/\tau)\) by (9), (6), and (14).  The cubic packet term is
\(O(b^3)\).

For the entropy, the pointwise inequality
\[
 |x_-^{3/2}-y_-^{3/2}|
 \le C\bigl(|x|^{1/2}+|y|^{1/2}\bigr)|x-y|           \tag{16}
\]
and Hölder imply
\[
\begin{aligned}
 &\left|\int
 \left[(M^2p_U+\alpha^2b^2p_{w_N})_-^{3/2}
       -(M^2p_U)_-^{3/2}\right]\right|\\
 &\hspace{25mm}\le C(Mb^2+b^3).                      \tag{17}
\end{aligned}
\]
Equations (10), (15), and (17) prove (12)--(13).  In particular, the
pressure entropy is fully retained; its perturbation is \(O(Mb^2)\), one
power of \(M\) below the leading negative term.

## 3. A finite heat step

Fix any \(\sigma>0\), set
\[
 t_N={\sigma\over N^2},\qquad \lambda=e^{-\sigma}\in(0,1). \tag{18}
\]
The Fourier-shift formula for a modulated smooth envelope gives, for every
\(1<q<\infty\),
\[
 \|e^{t_N\Delta}w_N-\lambda w_N\|_q\longrightarrow0. \tag{19}
\]
For completeness, write each leading oscillation as
\(\chi e^{\pm iNx_1}\).  In the demodulated Fourier variable, its transform
after heat evolution has the multiplier
\[
 e^{-\sigma|\xi\pm Ne_1|^2/N^2}\widehat\chi(\xi).
\]
This multiplier converges pointwise to \(e^{-\sigma}\), with all polynomially
weighted errors dominated by the Schwartz transform of \(\chi\).  Fourier
inversion and Sobolev embedding prove (19); the \(N^{-1}\) envelope terms in
(5) converge to zero by heat-semigroup contraction.  Also
\[
 e^{t_N\Delta}(MU)\longrightarrow MU\quad\hbox{in }L^3. \tag{20}
\]
Therefore
\[
 e^{t_N\Delta}h_{N,1}-h_{N,\lambda}\longrightarrow0
 \quad\hbox{in }L^3.                                 \tag{21}
\]

For fixed \(\tau>0\), \(\mathcal J_\tau\) is locally Lipschitz on \(L^3\).
Indeed,
\[
 \|p(u)-p(v)\|_{3/2}
 \le C(\|u\|_3+\|v\|_3)\|u-v\|_3,                   \tag{22}
\]
\(\rho_\tau\) is one-Lipschitz and bounded by its argument, and (16)
controls the pressure entropy.  Hence (21), with the uniformly bounded
\(L^3\) norms of the two sequences, gives
\[
 \mathcal J_\tau(e^{t_N\Delta}h_{N,1})
 -\mathcal J_\tau(h_{N,\lambda})\longrightarrow0.    \tag{23}
\]
This proves the finite-step comparison without differentiating the
functional or requiring derivative bounds for the heat-evolved packet.

Subtracting (12) at \(\alpha=1\) from (12) at
\(\alpha=\lambda\) gives
\[
\begin{aligned}
 \mathcal J_\tau(h_{N,\lambda})
 -\mathcal J_\tau(h_{N,1})
 \ge{}&{(1-\lambda^2)b^2M^2\over2\tau}A_N\\
 &-2C_\tau\left(
 Mb^2+b^3+{b^4\over\tau}
       +{M^2b^4\over\tau^3}\right).                  \tag{24}
\end{aligned}
\]

Choose the parameters in order.  First choose \(M\) sufficiently large,
depending on \(\tau,\sigma,U,\chi\), that the \(Mb^2\) term is at most one
eighth of the limiting leading term.  Then choose \(b>0\) sufficiently
small, depending on the fixed \(M,\tau\), that the remaining three errors
consume at most another one eighth.  Finally choose \(N\) sufficiently large
that \(A_N\ge A/2\) and the error in (23) consumes at most one eighth.
The right side of
\[
\begin{aligned}
 \mathcal J_\tau(e^{t_N\Delta}h_{N,1})
 -\mathcal J_\tau(h_{N,1})
={}&
 \bigl[\mathcal J_\tau(e^{t_N\Delta}h_{N,1})
       -\mathcal J_\tau(h_{N,\lambda})\bigr]\\
 &+\bigl[\mathcal J_\tau(h_{N,\lambda})
       -\mathcal J_\tau(h_{N,1})\bigr]               \tag{25}
\end{aligned}
\]
is then strictly positive.  Taking \(h=h_{N,1}\) and
\(t=t_N>0\) proves (2).

## 4. Scope and frontier consequence

CLAIM AND SCOPE: For each separately fixed \(\tau>0\), (2) holds for some
compactly supported smooth divergence-free \(h\) and a positive finite heat
step.  The field and heat time may depend on \(\tau\).

EVIDENCE: The strict negative remote pressure (3)--(4), uniform static
expansion (12)--(17), packet heat limit (19), and local \(L^3\) continuity
(22)--(23) give a complete analytic certificate.  No numerical sign is used.

FIRST GAP: none for universal heat monotonicity at a prescribed constant
speed scale.  The construction does not address a scale selected from the
state or changing along the evolution.

SURVIVING CONDITIONAL SUFFIX: A pressure-entropy correction can remain
statically coercive, but freezing the speed regularization at any positive
\(\tau\) does not make it heat-monotone for all solenoidal fields.

NON-CLAIMS: This does not treat a homogeneous state-dependent scale, the
Euler/nonlinear evolution, a Navier--Stokes trajectory estimate,
HIGH-PRESSURE, critical continuation, blow-up, or global regularity.

NEXT DISTINCT ACTION: A scale-covariant repair would have to couple \(\tau\)
to the state.  Its extra scale-derivative terms and coercivity must be derived
before the present fixed-scale obstruction can be compared with it.
