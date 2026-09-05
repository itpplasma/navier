# HF04: a genuine-trajectory obstruction to energy-only spacetime absorption

Status: rigorous no-go theorem, 2026-09-05. The construction uses the audited
compactly supported solenoidal profile \(\phi\) from
hf02-r3-profile.md, for which
\[
 P_\phi:=P_3[\phi]>0.
\]
It produces genuine smooth Navier--Stokes trajectory segments. It does not
refute the current HF hypothesis, whose cutoff and finite remainder may
depend on the complete datum.

## Theorem

Fix \(E>0\), \(\nu>0\), \(H>0\), an integer \(J\), and finite
\(\theta\ge0\). Among all maximal smooth unforced Navier--Stokes solutions
on \(\mathbb R^3\) with Schwartz divergence-free initial data of kinetic
energy \(E\),
\[
 \sup_{u,\tau}
 \int_0^\tau\bigl(H_J(u(t))-\theta\nu D_3(u(t))\bigr)\,dt
 =+\infty,                                            \tag{1}
\]
where the supremum is over
\(0<\tau<\min\{H,T_*(u_0)\}\).

Thus no finite spacetime remainder depending only on
\((E,\nu,H,J,\theta)\) can prove fixed-cutoff high-frequency absorption
uniformly across data.

## 1. Uniform normalized trajectories as viscosity tends to zero

Choose an integer \(m\ge5\). For \(0<\mu\le\nu\), let \(v_\mu\) solve
\[
 \partial_sv_\mu+(v_\mu\cdot\nabla)v_\mu+\nabla q_\mu
 =\mu\Delta v_\mu,\qquad
 \nabla\cdot v_\mu=0,\qquad v_\mu(0)=\phi.             \tag{2}
\]
There are \(T>0\) and \(K<\infty\), depending on
\(\phi,m,\nu\) but not on \(\mu\), such that
\[
 \sup_{0\le s\le T}\|v_\mu(s)\|_{H^m}\le K.           \tag{3}
\]

For completeness, apply derivatives through order \(m\), pair with the same
derivatives, and use the standard commutator estimate and
\(H^m(\mathbb R^3)\hookrightarrow W^{1,\infty}\):
\[
 {1\over2}{d\over ds}\|v_\mu\|_{H^m}^2
 +\mu\|\nabla v_\mu\|_{H^m}^2
 \le C_m\|\nabla v_\mu\|_\infty\|v_\mu\|_{H^m}^2
 \le C_m\|v_\mu\|_{H^m}^3.                            \tag{4}
\]
The differential inequality gives a common lower lifespan and (3).
Equivalently, the usual Friedrichs or mild construction uses that the heat
semigroup is an \(H^m\) contraction uniformly in \(\mu\); (4) prevents
breakdown before that common time. No inviscid-limit theorem is used.

The equation and (3) also give
\[
 \|\partial_sv_\mu\|_{H^{m-2}}
 \le C_{\phi,m,\nu}                                   \tag{5}
\]
uniformly on \([0,T]\). Therefore
\[
 \|v_\mu(s)-\phi\|_{H^{m-2}}\le Cs.
\]
Interpolation with the uniform \(H^m\) bound yields
\[
 \|v_\mu(s)-\phi\|_{H^{m-1}}\le C s^{1/2}.            \tag{6}
\]

## 2. Uniform persistence of positive pressure work

The functional \(P_3\) is continuous, indeed locally Lipschitz, on bounded
subsets of \(H^{m-1}\) for \(m\ge5\). To see this, write
\[
 p[v]=R_iR_j(v_iv_j),\qquad
 g(v)=v\cdot\nabla|v|
     ={v_i v_j\over|v|}\,\partial_i v_j,
\]
with the quotient set to zero at \(v=0\). The map
\[
 A(z)={z\otimes z\over|z|},\qquad A(0)=0,
\]
is globally Lipschitz on \(\mathbb R^3\). Hence, on an \(H^{m-1}\)-bounded
set,
\[
 \|p[v]-p[w]\|_2
 \le C_K\|v-w\|_{H^{m-1}},\qquad
 \|g(v)-g(w)\|_2
 \le C_K\|v-w\|_{H^{m-1}}.                            \tag{7}
\]
Here the first estimate uses \(L^2\)-boundedness of the Riesz transforms and
\(\|vw\|_2\le\|v\|_\infty\|w\|_2\); the second follows from the Lipschitz
property of \(A\), \(H^{m-1}\hookrightarrow W^{1,\infty}\), and
\(\nabla v\in L^2\). Pairing \(p[v]\) with \(g(v)\) proves
\[
 |P_3[v]-P_3[w]|\le C_K\|v-w\|_{H^{m-1}}.             \tag{8}
\]

Shrinking \(T\), independently of \(\mu\), equations (6)--(8) give
\[
 P_3[v_\mu(s)]\ge {P_\phi\over2}
 \quad(0\le s\le T,\ 0<\mu\le\nu).                    \tag{9}
\]
Moreover (3) directly implies
\[
 D_3(v_\mu(s))
 \le2\|v_\mu(s)\|_\infty\|\nabla v_\mu(s)\|_2^2
 \le C_D                                             \tag{10}
\]
on the same interval, uniformly in \(\mu\).

## 3. Exact rescaling to fixed initial energy

Let \(a\ge1\) tend to infinity and set
\[
 N={a^2\|\phi\|_2^2\over E},\qquad
 \mu={\nu\over a}.
\]
For all sufficiently large \(a\), \(\mu\in(0,\nu]\). Define
\[
 u_a(x,t)=aN\,v_\mu(Nx,aN^2t),\qquad
 p_a(x,t)=a^2N^2q_\mu(Nx,aN^2t).                      \tag{11}
\]
Substitution into (2) shows that \((u_a,p_a)\) solves the original equation
with viscosity \(\nu\). Its initial datum is compactly supported, smooth, and
divergence free, and
\[
 \|u_a(0)\|_2^2
 ={a^2\over N}\|\phi\|_2^2=E.                         \tag{12}
\]

The normalized solution exists at least until \(s=T\), so the original
solution exists at least until
\[
 \tau_a={T\over aN^2}.                                \tag{13}
\]
Since \(N\simeq a^2\), \(\tau_a\simeq a^{-5}\), and
\(\tau_a<H\) for all sufficiently large \(a\).

At corresponding times \(s=aN^2t\), exact amplitude and spatial scaling give
\[
 P_3[u_a(t)]=a^4N^2P_3[v_\mu(s)],\qquad
 D_3[u_a(t)]=a^3N^2D_3[v_\mu(s)].                     \tag{14}
\]
Changing time variables in (14),
\[
\begin{aligned}
 \int_0^{\tau_a}
 \bigl(P_3[u_a]-\theta\nu D_3[u_a]\bigr)\,dt
 &=a^3\int_0^T
 \bigl(P_3[v_\mu]-\theta\mu D_3[v_\mu]\bigr)\,ds.
                                                               \tag{15}
\end{aligned}
\]
By (9)--(10), once \(a\) is also large enough that
\(\theta(\nu/a)C_D\le P_\phi/4\),
\[
 \int_0^{\tau_a}
 \bigl(P_3[u_a]-\theta\nu D_3[u_a]\bigr)\,dt
 \ge {TP_\phi\over4}\,a^3.                            \tag{16}
\]

## 4. Removing the fixed low-output pressure

The standard band-limited pressure estimate and energy equality give
\[
 \left|\int_0^\tau L_J(u(t))\,dt\right|
 \le C2^{3J}E^2\left({\tau\over2\nu}\right)^{1/2}      \tag{17}
\]
for every smooth solution with initial squared \(L^2\) norm \(E\).
Applying (17) at \(\tau=\tau_a\simeq a^{-5}\),
\[
 \left|\int_0^{\tau_a}L_J(u_a(t))\,dt\right|
 =O_{E,\nu,J,\phi,T}(a^{-5/2}).                       \tag{18}
\]
Since \(H_J=P_3-L_J\), equations (16)--(18) yield
\[
 \int_0^{\tau_a}
 \bigl(H_J(u_a)-\theta\nu D_3(u_a)\bigr)\,dt
 \ge {TP_\phi\over4}a^3-o(1)
 \longrightarrow+\infty.                             \tag{19}
\]
This proves (1).

## Exact scope

The sequence consists of actual unforced smooth Navier--Stokes solutions on
the time intervals being integrated, all with exactly the same initial
kinetic energy \(E\). Thus even time integration and viscosity do not produce
a fixed-\(J\) absorption remainder uniform over all data at fixed energy.

The initial critical norm is not uniform:
\[
 \|u_a(0)\|_3=a\|\phi\|_3\longrightarrow\infty.
\]
Higher initial norms also diverge, and the interval length tends to zero.
The current HF hypothesis allows its cutoff and finite remainder to depend
on the complete datum. Therefore this theorem does not refute HF, does not
control one fixed trajectory near its maximal time, and does not imply
blow-up.

## Frontier record

**MODE / RESULT:** FALSIFY. Fixed energy, a fixed output cutoff, and a fixed
finite dissipation coefficient cannot yield a uniform spacetime absorption
remainder, even on genuine smooth solution segments.

**FIRST GAP:** none for theorem (1). The universal-data HF route still needs
a datum-dependent mechanism or a relation between successive times along one
trajectory.

**SURVIVING CONDITIONAL SUFFIX:** any viable estimate must use more of the
datum than kinetic energy, choose scales from that datum, or exploit temporal
structure not uniform across these increasingly large-critical-norm inputs.

**NON-CLAIMS:** no common datum, uniform \(L^3\) input bound, singularity, or
failure of the stated datum-dependent HF hypothesis is proved.
