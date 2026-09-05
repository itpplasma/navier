# HF03: fixed-energy obstruction to instantaneous high-tail absorption

Status: rigorous static no-go result, 2026-09-05. Let \(H_J(u)\) denote the
signed pressure work above one fixed Littlewood--Paley output cutoff \(J\):
\[
 H_J(u)=\int_{\mathbb R^3}(I-S_J)p[u]\,
                   u\cdot\nabla|u|\,dx,
 \qquad p[u]=R_iR_j(u_i u_j).
\]
Let
\[
 D_3(u)=\int_{\mathbb R^3}
 \bigl(|u||\nabla u|^2+|u||\nabla|u||^2\bigr)\,dx.
\]

## Theorem

For every \(E>0\), \(\nu>0\), integer \(J\), and finite
\(\theta\ge0\),
\[
 \sup\left\{
 H_J(u)-\theta\nu D_3(u):
 u\in C_c^\infty(\mathbb R^3;\mathbb R^3),\
 \nabla\cdot u=0,\ \|u\|_2^2=E
 \right\}=+\infty.                                    \tag{1}
\]

This is an instantaneous fixed-energy obstruction. It does not concern
solutions evolving from one datum and does not refute the time-integrated HF
hypothesis.

## 1. Positive profile and amplitude choice

The independently audited construction in hf02-r3-profile.md supplies a
real compactly supported smooth divergence-free field
\(\phi\) such that
\[
 P_\phi:=P_3[\phi]>0.
\]
Put
\[
 e_\phi=\|\phi\|_2^2,\qquad d_\phi=D_3(\phi).
\]
For amplitude \(a>0\),
\[
 P_3[a\phi]=a^4P_\phi,\qquad
 D_3(a\phi)=a^3d_\phi.                                \tag{2}
\]
Choose \(a\) once and for all so that
\[
 c_*:=a^4P_\phi-\theta\nu a^3d_\phi>0.                \tag{3}
\]
This is possible because \(P_\phi>0\) and \(\theta\nu d_\phi<\infty\).

For \(N\ge1\), define the concentrated packet
\[
 w_N(x)=aN\phi(Nx).
\]
Exact scaling gives
\[
 \|w_N\|_2^2={a^2e_\phi\over N},\qquad
 P_3[w_N]=a^4N^2P_\phi,\qquad
 D_3(w_N)=a^3N^2d_\phi,                               \tag{4}
\]
and
\[
 \|\nabla w_N\|_2^2=a^2N\|\nabla\phi\|_2^2.           \tag{5}
\]

## 2. Exact energy reservoir

Choose any nonzero
\(\psi\in C_c^\infty(\mathbb R^3;\mathbb R^3)\) with
\(\nabla\cdot\psi=0\), and translate it once so that its support has positive
distance from the origin. For all sufficiently large \(N\), the supports of
\(w_N\) and \(\psi\) are disjoint. Write \(e_\psi=\|\psi\|_2^2\), and set
\[
 b_N=\left({E-a^2e_\phi/N\over e_\psi}\right)^{1/2},
 \qquad z_N=b_N\psi,\qquad u_N=w_N+z_N.                \tag{6}
\]
Then \(b_N\to(E/e_\psi)^{1/2}\), so \(b_N\) remains bounded above and away
from zero, and
\[
 u_N\in C_c^\infty,\qquad \nabla\cdot u_N=0,\qquad
 \|u_N\|_2^2=E.                                       \tag{7}
\]

Because the supports are disjoint, the pointwise cross tensor vanishes:
\[
 w_N\otimes z_N+z_N\otimes w_N=0.
\]
Thus there is no cross-pressure source and
\[
 p[u_N]=p[w_N]+p[z_N].                                \tag{8}
\]
Likewise the weighted dissipation is exactly additive,
\[
 D_3(u_N)=D_3(w_N)+D_3(z_N)
         =a^3N^2d_\phi+O_{E,\psi}(1).                 \tag{9}
\]

## 3. Nonlocal pressure interactions are negligible

Although (8) has no cross source, each self-pressure is nonlocal and can pair
with the other component. Put
\[
 g(v)=v\cdot\nabla|v|=\operatorname{div}(|v|v).
\]
Disjointness gives \(g(u_N)=g(w_N)+g(z_N)\), and hence
\[
\begin{aligned}
 P_3[u_N]
 &=P_3[w_N]+P_3[z_N]\\
 &\quad+\int p[w_N]g(z_N)\,dx
       +\int p[z_N]g(w_N)\,dx.                        \tag{10}
\end{aligned}
\]

Let \(d>0\) be a fixed lower bound on the distance between the two supports.
Away from its source, the kernel of \(R_iR_j\) is smooth and bounded by
\(C|x-y|^{-3}\). Since
\[
 \|w_N\otimes w_N\|_1=\|w_N\|_2^2=O(N^{-1}),
\]
one has on \(\operatorname{supp}z_N\)
\[
 \|p[w_N]\|_\infty\le C_dN^{-1}.                      \tag{11}
\]
Also
\[
 \|g(z_N)\|_1
 \le\|z_N\|_2\|\nabla z_N\|_2=O_{E,\psi}(1),
\]
so
\[
 \left|\int p[w_N]g(z_N)\right|=O(N^{-1}).            \tag{12}
\]

In the other direction, \(p[z_N]\) is smooth and harmonic on a fixed
neighborhood of \(\operatorname{supp}w_N\). Its gradient there is bounded
uniformly in \(N\), because \(\|z_N\otimes z_N\|_1\le E\) and the supports
remain a fixed distance apart. Integration by parts gives
\[
\begin{aligned}
 \left|\int p[z_N]g(w_N)\right|
 &=\left|\int\nabla p[z_N]\cdot |w_N|w_N\,dx\right|\\
 &\le C_{d,E,\psi}\|w_N\|_2^2=O(N^{-1}).              \tag{13}
\end{aligned}
\]
The possible distributional local term in the double Riesz kernel does not
enter (11) or (13), because the evaluation and source supports are disjoint.

Finally \(P_3[z_N]=b_N^4P_3[\psi]=O_{E,\psi}(1)\). Therefore
\[
 P_3[u_N]=a^4N^2P_\phi+O_{E,a,\phi,\psi}(1).          \tag{14}
\]

## 4. Fixed low-output work is lower order

Write
\[
 L_J(u)=\int S_Jp[u]\,u\cdot\nabla|u|\,dx,
 \qquad H_J(u)=P_3[u]-L_J(u).
\]
The truncated pressure kernel estimate gives, for every smooth finite-energy
field,
\[
 |L_J(u)|
 \le C2^{3J}\|u\|_2^3\|\nabla u\|_2.                  \tag{15}
\]
For \(u_N\), exact energy (7), disjointness, and (5) give
\[
 \|\nabla u_N\|_2^2
 =a^2N\|\nabla\phi\|_2^2+O_{E,\psi}(1),
\]
and hence
\[
 |L_J(u_N)|\le C_{E,J,a,\phi,\psi}N^{1/2}=o(N^2).
                                                                    \tag{16}
\]
This estimate includes all low-pass nonlocal interactions; no unsupported
frequency orthogonality between the packet and reservoir is used.

## 5. Divergence of the excess

Combining (3), (9), (14), and (16),
\[
\begin{aligned}
 H_J(u_N)-\theta\nu D_3(u_N)
 &=N^2\bigl(a^4P_\phi-\theta\nu a^3d_\phi\bigr)
   +O(N^{1/2})+O(1)\\
 &=c_*N^2+o(N^2)\longrightarrow+\infty.               \tag{17}
\end{aligned}
\]
Every \(u_N\) lies in the class in (1) and has exactly the prescribed kinetic
energy \(E\). This proves the theorem.

## Exact scope

Equation (1) rules out every instantaneous inequality of the form
\[
 H_J(u)\le\theta\nu D_3(u)+F(E,\nu,J,\theta)
\]
with a finite remainder depending only on kinetic energy and the displayed
fixed parameters, even when \(\theta\) is arbitrarily large but finite.
The obstruction uses amplitude to make signed pressure work dominate weighted
dissipation, concentration to amplify the positive excess by \(N^2\), and a
separated reservoir to keep total energy exactly fixed.

The result does not rule out a remainder depending on additional initial
norms, a cutoff chosen from the full datum, cancellation after time
integration, or an estimate restricted to actual Navier--Stokes trajectories.
In particular it does not refute the current spacetime HF hypothesis.

## Frontier record

**MODE / RESULT:** FALSIFY. The fixed-energy instantaneous absorption
mechanism is rigorously impossible for every fixed cutoff and finite
dissipation coefficient.

**FIRST GAP:** none for the static theorem. The trajectory-level signed time
integral remains open.

**SURVIVING CONDITIONAL SUFFIX:** a successful HF producer must use temporal
evolution, more input information than energy, or a datum-dependent cutoff in
a way not reducible to a fixed-\(J\) instantaneous estimate.

**NON-CLAIMS:** the sequence is not one solution trajectory, has no uniform
higher initial norm, and proves neither blow-up nor failure of spacetime
absorption.
