# Dyadic pressure flux: a rigorous low/high reduction

Status: research evidence, 2026-09-05. The setting is the unforced
three-dimensional Navier--Stokes equation on \(\mathbb R^3\), with viscosity
\(\nu>0\), divergence-free Schwartz datum \(u_0\), and its maximal classical
solution \(u\) on \([0,T_*)\). This note tests the signed dyadic pressure-flux
proposal in architecture.md. It proves a reduction, not the missing
high-frequency estimate and not global regularity.

## 1. Pressure work and Littlewood--Paley splitting

Use a smooth homogeneous Littlewood--Paley partition
\(\sum_{j\in\mathbb Z}\Delta_j=I\) away from frequency zero and write
\[
 S_J=\sum_{j\leq J}\Delta_j,\qquad p_{\leq J}=S_Jp,\qquad
 p_{>J}=p-p_{\leq J}.
\]
For each positive time under consideration all expressions below can first be
computed for finite dyadic sums and then obtained by smooth approximation.
Fix the pressure modulo a function of time by
\[
 p=R_iR_j(u_i u_j).
\]
The exact critical balance from architecture.md is
\[
 {1\over3}{d\over dt}\|u(t)\|_3^3+\nu D_3(t)=P_3(t),
 \qquad
 P_3=\int_{\mathbb R^3}p\,u\cdot\nabla|u|\,dx,
\]
where
\[
 D_3=\int_{\mathbb R^3}
 \bigl(|u||\nabla u|^2+|u||\nabla|u||^2\bigr)\,dx.
\]
Define the signed low and high contributions
\[
 L_J(t)=\int p_{\leq J}\,u\cdot\nabla|u|\,dx,\qquad
 H_J(t)=\int p_{>J}\,u\cdot\nabla|u|\,dx.              \tag{1}
\]
Thus \(P_3=L_J+H_J\). The quantity to preserve is the single signed sum
\(H_J\), rather than
\(\sum_{j>J}|\int\Delta_jp\,u\cdot\nabla|u||\).

There is an equivalent cancellation identity. With \(\mathbb P\) the Leray
projector, \(N=(u\cdot\nabla)u\), and \(w=|u|u\),
\[
 \nabla p=-(I-\mathbb P)N,\qquad \int w\cdot N\,dx=0,
\]
so
\[
 P_3=-\int w\cdot\nabla p\,dx
     =\int w\cdot(I-\mathbb P)N\,dx
     =-\int \mathbb Pw\cdot N\,dx.                    \tag{2}
\]
Equation (2) is a real cancellation: the full transport pairing vanishes and
only the non-divergence-free part selected by pressure remains. It does not
give a sign or a derivative gain, because \(\mathbb P\) is order zero.

## 2. The low-frequency part is controlled by energy

The multiplier of \(S_JR_iR_j\) is integrable in frequency, with integral
bounded by \(C2^{3J}\). Its convolution kernel therefore gives the elementary
\(L^1\)-to-\(L^\infty\) estimate
\[
 \|p_{\leq J}(t)\|_\infty
 \leq C2^{3J}\|u(t)\otimes u(t)\|_1
 \leq C2^{3J}\|u_0\|_2^2.                             \tag{3}
\]
Although the Riesz transforms themselves are not bounded on \(L^1\), (3)
does not assert that endpoint estimate: the output has first been cut off at
frequency \(2^J\), and the bounded band-limited kernel is used directly.

Consequently,
\[
 |L_J(t)|
 \leq \|p_{\leq J}(t)\|_\infty
       \|u(t)\|_2\|\nabla u(t)\|_2
 \leq C2^{3J}\|u_0\|_2^3\|\nabla u(t)\|_2.             \tag{4}
\]
For every \(0<\tau<\min\{H,T_*\}\), the energy equality and Cauchy--Schwarz in
time yield
\[
 \begin{aligned}
 \left|\int_0^\tau L_J(t)\,dt\right|
 &\leq C2^{3J}\|u_0\|_2^3
       H^{1/2}\left(\int_0^\tau\|\nabla u\|_2^2dt\right)^{1/2}\\
 &\leq C2^{3J}\|u_0\|_2^4\left({H\over2\nu}\right)^{1/2}
 =:A_{\rm low}(\nu,u_0,H,J).                           \tag{5}
 \end{aligned}
\]
This bound is uniform in \(\tau\) and \(T_*\), depends only on displayed input
data, and requires no critical solution norm. Hence low output frequencies
are not the pressure-absorption obstruction.

## 3. Exact additional estimate sufficient for critical control

Fix any integer \(J=J(\nu,u_0,H)\) specified a priori. It is sufficient to
prove that there are a universal \(\theta<1\) and a finite explicit
\(A_{\rm high}(\nu,u_0,H,J)\), independent of \(\tau,T_*\), and of unknown
trajectory norms, such that
\[
 \int_0^\tau H_J(t)\,dt
 \leq \theta\nu\int_0^\tau D_3(t)\,dt
      +A_{\rm high}(\nu,u_0,H,J)                       \tag{HF}
\]
for every \(0<\tau<\min\{H,T_*\}\). Combining (1), (5), and (HF) gives the
pressure-absorption hypothesis (PA) in architecture.md with
\[
 A=A_{\rm low}+A_{\rm high}.
\]
The exact \(L^3\) balance then gives
\[
 \sup_{0\leq t<\min\{H,T_*\}}\|u(t)\|_3^3
 \leq \|u_0\|_3^3+3(A_{\rm low}+A_{\rm high}),         \tag{6}
\]
and also controls \((1-\theta)\nu\int D_3\). Thus (HF), for just one
input-determined finite cutoff, is a concrete sufficient producer of the
critical continuation bound.

A superficially weaker tail statement can also suffice: if
\[
 \limsup_{J\to\infty}\sup_{\tau<\min\{H,T_*\}}
 \left\{\int_0^\tau H_Jdt-\theta\nu\int_0^\tau D_3dt\right\}
 \leq A_{\rm tail}(\nu,u_0,H),                         \tag{7}
\]
with a quantitative input-only modulus allowing selection of a finite \(J\),
then (HF) follows. Mere pointwise convergence \(H_J(t)\to0\) for every
regular \(t<T_*\) is insufficient: it supplies neither uniformity as
\(t\uparrow T_*\) nor an integrable majorant.

## 4. Why absolute dyadic energy estimates fail

At fixed time the standard absolute estimate is
\[
 |P_3|
 \leq \|p\|_3\|u\|_6\|\nabla u\|_2
 \leq C\|u\|_6^3\|\nabla u\|_2.                        \tag{8}
\]
It follows from Calderon--Zygmund boundedness
\(\|p\|_3\lesssim\|u\otimes u\|_3=\|u\|_6^2\).
Energy controls \(\|\nabla u\|_2\) only in \(L^2_t\), while the right side of
(8) behaves like \(\|\nabla u\|_2^4\) after Sobolev. This is not integrable
from energy. Applying (8) separately to dyadic pieces and summing their
absolute values adds an \(\ell^1\) Besov requirement and cannot improve the
energy bookkeeping.

Critical concentration gives a sharper falsifier. Let
\(\phi\in\mathcal S(\mathbb R^3;\mathbb R^3)\) be divergence free and set
\[
 u_N(x)=N\phi(Nx),\qquad p_N(x)=N^2p_\phi(Nx).
\]
This is the spatial part of the exact Navier--Stokes scaling. Directly,
\[
 \|u_N\|_3=\|\phi\|_3,\quad
 \|u_N\|_2^2=N^{-1}\|\phi\|_2^2,\quad
 D_3[u_N]=N^2D_3[\phi],\quad P_3[u_N]=N^2P_3[\phi].
                                                                    \tag{9}
\]
For a fixed \(J\), (4) applied at the snapshot \(u_N\) gives
\[
 |L_J[u_N]|
 \leq C2^{3J}\|u_N\|_2^3\|\nabla u_N\|_2
 =O_{\phi,J}(N^{-1}).
\]
Thus, whenever \(P_3[\phi]\ne0\),
\[
 H_J[u_N]=N^2P_3[\phi]+O_{\phi,J}(N^{-1}).             \tag{9a}
\]
The energy tends to zero while the high signed pressure work and cubic
dissipation have critical size \(N^2\); their ratio has a nonzero
scale-invariant limit.

Therefore no estimate of the form
\[
 \left|\int_0^\tau H_Jdt\right|
 \leq \varepsilon(J)\,\nu\int_0^\tau D_3dt
      +F(\|u_0\|_2,\nu,H),\qquad \varepsilon(J)\to0,    \tag{10}
\]
can be justified from instantaneous energy size and frequency separation
alone. A family of scaled snapshots is not a family of trajectories with
one fixed datum, so (9) does not refute the spacetime assertion (HF).
It does refute the proposed proof mechanism that obtains a small high tail
solely from energy and Bernstein factors.

The same scaling diagnoses termwise absolute summation. Any order-zero
commutator estimate applied to (2) is critical under (9); it has no factor
decaying with the active shell. To create such a factor one must use
additional regularity, a temporal cancellation across the parabolic life
\(N^{-2}\) of the packet, or a signed interaction law between shells. None
of those follows from the energy identity by the calculations above.

## 5. One cancellation attempt and its limit

Identity (2) repairs one overly crude step: instead of estimating pressure as
an unrelated scalar, retain its origin as the gradient projection of the
transport term. Since Fourier projections commute with \(I-\mathbb P\),
\[
 H_J=\int P_{>J}w\cdot(I-\mathbb P)N\,dx.
\]
Dyadically, this suggests summing
\[
 \sum_{j>J}\int \Delta_jw\cdot(I-\mathbb P)N\,dx
\]
with its sign before estimating. Orthogonality permits replacement of \(N\)
by neighboring output frequencies, so widely separated output shells do not
interact directly. This reduces the prospective estimate to neighboring
shells plus the high--high-to-low part already placed in \(L_J\), whose
aggregate is controlled by (5).

The repair stops here. Neighboring critical shells have no sign forced by
incompressibility, and (9) shows that the Leray projection supplies no small
factor. Turning their signed time integral into
\(\theta\nu\int D_3\) plus an energy-level remainder is precisely (HF), not a
consequence of almost orthogonality. Calling the shell sum telescoping without
an explicit boundary functional \(B_j(t)\) satisfying
\[
 \operatorname{flux}_j(t)=\frac{d}{dt}B_j(t)
                          +\operatorname{error}_j(t)
\]
with summable errors would leave the required implication unproved. No
such functional is constructed here.

## Frontier record

**Mode / result:** FALSIFY/REPAIR. The low output-frequency pressure work is
removed with the explicit input-only bound (5), leaving the exact signed
high-tail producer (HF).

**First gap:** prove (HF) for every arbitrary-data classical trajectory.
Energy, frequency localization, Leray-projection cancellation, and
almost-orthogonality do not prove it.

**Surviving conditional suffix:** (HF) plus (5) implies (PA), hence the
finite-horizon critical \(L^3\) bound (6) and the conditional ESS continuation
chain already recorded in architecture.md.

**Non-claims:** scaled snapshots in (9) are a mechanism falsifier, not
Navier--Stokes blow-up solutions and not a refutation of (HF). No signed
telescoping law, universal \(\theta<1\), or new a priori trajectory estimate
has been established.

**Unresolved new producer:** an input-only estimate for the signed time
integral of the aggregate high-frequency pressure flux, exploiting actual
Navier--Stokes evolution rather than absolute shell bounds.
