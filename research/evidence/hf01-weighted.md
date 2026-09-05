# HF01: weighted pressure absorption and amplitude tails

## Frontier packet

**TERMINAL CLAIM.** For the unforced three-dimensional Navier--Stokes
equation on \(\mathbb R^3\), with arbitrary divergence-free Schwartz datum
\(u_0\), viscosity \(\nu>0\), and maximal classical solution on
\([0,T_*)\), prove the following. There is a universal
\(\theta\in[0,1)\) such that for every finite \(H>0\) one can specify an
integer \(J=J(\nu,u_0,H)\) and a finite input-only remainder
\(A(\nu,u_0,H,J)\) for which
\[
 \int_0^\tau Q_J(t)\,dt
 \le \theta\nu\int_0^\tau D_3(t)\,dt+A(\nu,u_0,H,J)    \tag{HF}
\]
for every \(0<\tau<\min\{H,T_*\}\). Here
\[
 Q_J=\int_{\mathbb R^3}p_{>J}u\cdot\nabla|u|\,dx,
 \qquad p_{>J}=P_{>J}R_iR_j(u_i u_j),
\]
and
\[
 D_3=\int_{\mathbb R^3}
 \left(|u||\nabla u|^2+|u||\nabla|u||^2\right)dx.
\]
The high-pass multipliers are smooth and uniformly bounded on
\(L^q\), \(1<q<\infty\).

**ESTABLISHED.** The exact cubic balance and the energy-controlled
low-output pressure estimate in frequency.md reduce pressure absorption to
(HF). Sobolev estimates on each compact classical interval justify all
expressions below.

**FIRST GAP.** Produce the strict universal absorption coefficient and an
input-only time-integrable remainder for arbitrary large data.

**FALSIFIER.** A coefficient containing the unknown
\(\sup_{t<T_*}\|u(t)\|_3\), a remainder containing an uncontrolled
continuation norm, or a cutoff selected from the future trajectory does not
prove (HF).

**MODE / RESULT.** REPAIR/FALSIFY. The weighted estimate below identifies a
valid critical-smallness mechanism. A genuinely different amplitude-level
split isolates two exact large-data obligations, neither of which follows
from energy. The route therefore stops at those obligations.

## Weighted cubic Sobolev structure

Put \(r=|u|\) and \(f=r^{3/2}\). The second term in \(D_3\) gives
\[
 \|\nabla f\|_2^2
 =\frac94\int r|\nabla r|^2\,dx
 \le \frac94D_3.                                      \tag{1}
\]
Sobolev applied to \(f\) consequently yields
\[
 \|u\|_9^{3/2}=\|f\|_6\le C\|\nabla f\|_2
 \le C D_3^{1/2}.                                     \tag{2}
\]
Interpolation between \(L^3\) and \(L^9\) gives
\[
 \|u\|_6^2
 \le \|u\|_3^{1/2}\|u\|_9^{3/2}
 \le C\|u\|_3^{1/2}D_3^{1/2}.                         \tag{3}
\]
Calderón--Zygmund boundedness, uniformly in \(J\), then gives
\[
 \|p_{>J}\|_3
 \le C\|u\otimes u\|_3
 =C\|u\|_6^2
 \le C\|u\|_3^{1/2}D_3^{1/2}.                         \tag{4}
\]

The other factor in the pressure work has the matching weighted estimate.
Since \(r\nabla r=(2/3)r^{1/2}\nabla f\),
\[
 \|u\nabla r\|_{3/2}
 \le C\|r^{1/2}\|_6\|\nabla f\|_2
 \le C\|u\|_3^{1/2}D_3^{1/2}.                         \tag{5}
\]
Combining (4) and (5) proves the strongest direct instantaneous estimate
provided by this weighted cubic structure:
\[
 \boxed{|Q_J(t)|\le C\|u(t)\|_3D_3(t)}.               \tag{6}
\]
The constant is universal and independent of \(J\). The identical argument
with \(p\) in place of \(p_{>J}\) bounds the full pressure work \(P_3\).

Estimate (6) absorbs the high pressure whenever
\[
 C\sup_{0<t<\min\{H,T_*\}}\|u(t)\|_3<\nu.              \tag{7}
\]
This recovers a critical small-data mechanism. It does not prove (HF) for
large data because (7) assumes the critical bound that the pressure route is
supposed to produce. Taking \(J\) large does not help in (6): the
\(L^3\)-operator norm of \(P_{>J}R_iR_j\) is bounded but does not tend to
zero uniformly on \(L^3\).

## A large-data amplitude split

Fix a level \(K>0\), independent of time, and define
\[
 U(t)=\|u(t)\|_3,\qquad
 B_K(t)=\|u(t)\mathbf 1_{\{|u(t)|>K\}}\|_3.
\]
Split the spatial integral defining \(Q_J\) into
\(\{r\le K\}\) and \(\{r>K\}\). This differs genuinely from a dyadic output
split: it tries to attach the dangerous coefficient only to the large
velocity tail.

On the low-amplitude region, weighted Young inequality gives, for every
\(\varepsilon>0\),
\[
\begin{aligned}
 \left|\int_{\{r\le K\}}p_{>J}u\cdot\nabla r\,dx\right|
 &\le \varepsilon\int_{\{r\le K\}}r|\nabla r|^2dx
   +C\varepsilon^{-1}\int_{\{r\le K\}}r|p_{>J}|^2dx\\
 &\le \varepsilon D_3
   +C\varepsilon^{-1}K\|p_{>J}\|_2^2\\
 &\le \varepsilon D_3
   +C\varepsilon^{-1}K\|u\|_4^4.                      \tag{8}
\end{aligned}
\]
The last line uses the uniform \(L^2\) multiplier bound and
\(\|u\otimes u\|_2=\|u\|_4^2\).

On the high-amplitude region, the localized version of (5) is
\[
 \|\mathbf1_{\{r>K\}}u\nabla r\|_{3/2}
 \le C B_K^{1/2}D_3^{1/2}.                            \tag{9}
\]
Together with (4), this yields
\[
 \left|\int_{\{r>K\}}p_{>J}u\cdot\nabla r\,dx\right|
 \le C(U B_K)^{1/2}D_3.                               \tag{10}
\]
Thus the exact level-split estimate is
\[
 \boxed{|Q_J|
 \le \left(\varepsilon+C(U B_K)^{1/2}\right)D_3
       +C\varepsilon^{-1}K\|u\|_4^4.}                 \tag{11}
\]

This separates two demands. The coefficient becomes absorbable if one has an
input-only level \(K=K(\nu,u_0,H)\) such that
\[
 \operatorname*{ess\,sup}_{0<t<\min\{H,T_*\}}
 U(t)B_K(t)
 \le \left(\frac{\theta\nu-\varepsilon}{C}\right)^2,  \tag{12}
\]
for some \(0<\varepsilon<\theta\nu\). The residual is admissible only if
\[
 \int_0^\tau\|u(t)\|_4^4dt
 \le R(\nu,u_0,H)<\infty                              \tag{13}
\]
uniformly for every \(\tau<\min\{H,T_*\}\), with \(R\) specified from the
inputs rather than the unknown trajectory. Under (12)--(13), integration of
(11) proves (HF), with
\[
 A=C\varepsilon^{-1}K R.
\]
This is a valid conditional repair and states its exact consumers.

## The residual exceeds energy control

The energy identity does give a nearby spacetime estimate. Interpolation
between \(L^2\) and \(L^6\), followed by Sobolev, yields
\[
 \|u\|_4^{8/3}
 \le C\|u\|_2^{2/3}\|\nabla u\|_2^2.
\]
Consequently
\[
 \int_0^\tau\|u(t)\|_4^{8/3}dt
 \le C\nu^{-1}\|u_0\|_2^{8/3}.                        \tag{14}
\]
The exponent required by (13) is \(4\), not \(8/3\). On a finite time
interval, an \(L_t^{8/3}\) bound does not imply an \(L_t^4\) bound. Hence the
low-amplitude residual in (11) is not controlled by energy.

The weighted structure gives another exact expression for the missing
integrability:
\[
 \|u\|_4^4
 \le \|u\|_3^{5/2}\|u\|_9^{3/2}
 \le C U^{5/2}D_3^{1/2}.                              \tag{15}
\]
Using (15) in time requires critical control of \(U\) and additional control
of \(D_3\); inserting it into (11) therefore does not close the estimate.
Likewise, (12) is a uniform integrability statement for the critical density
\(|u|^3\) whose modulus is weighted by the unknown total \(L^3\) norm.
Energy supplies no such amplitude-tail modulus.

A time-dependent level \(K(t)\) can always be chosen after inspecting a
regular snapshot so that \(B_{K(t)}(t)\) is small. That observation is
nonuniform as \(t\uparrow T_*\), and the resulting residual
\(K(t)\|u(t)\|_4^4\) has no input-only integral bound. Choosing the fixed
level from the future trajectory would violate the quantifiers in (HF).

## Amplitude and critical-scaling tests

For a fixed nonzero divergence-free Schwartz field \(\phi\), set
\(u_A=A\phi\) at one time. Its associated normalized pressure is
\(p_A=A^2p_\phi\), and
\[
 P_3[u_A]=A^4P_3[\phi],\qquad
 D_3[u_A]=A^3D_3[\phi],\qquad
 \|u_A\|_3=A\|\phi\|_3.                               \tag{16}
\]
Whenever \(P_3[\phi]\ne0\), the ratio
\(|P_3[u_A]|/D_3[u_A]\) grows linearly in \(A\). Thus no universal
instantaneous inequality \(|P_3|\le\theta\nu D_3+C\), with a remainder
independent of amplitude, can hold on all divergence-free Schwartz
snapshots. This is a snapshot obstruction, not a Navier--Stokes trajectory
counterexample and not evidence of blowup.

The level split reflects the same scaling. For every fixed \(K\), dominated
convergence gives \(A^{-1}B_K[u_A]\to\|\phi\|_3\) as \(A\to\infty\), so the
coefficient in (10) is of order \(A\). Choosing
\(K\ge A\|\phi\|_\infty\) removes that tail, but the instantaneous residual
in (8) is then of order
\(K\|u_A\|_4^4=O(A^5)\), larger than the \(O(A^4)\) pressure work. This does
not refute a time-integrated input-dependent estimate, but it prevents the
level split from creating an amplitude-uniform instantaneous absorption law.

Under the exact Navier--Stokes spatial scaling
\[
 u_N(x)=N\phi(Nx),
\]
the quantities \(P_3\) and \(D_3\) both scale as \(N^2\), while
\(\|u_N\|_3\) is invariant. Estimate (6) and the tail coefficient in (10)
are therefore critical. Frequency localization or rescaling alone cannot
create the strict factor \(\theta<1\).

## First unsupported implication

The first unsupported step is either of the following large-data assertions:

1. an input-only uniform tail modulus (12), or
2. the input-only \(L_t^4L_x^4\) estimate (13).

Both together would prove HF01 through (11), but neither follows from the
energy identity, the weighted cubic dissipation, or the fixed high-output
cutoff. Condition (13) is itself supercritical:
\(2/4+3/4=5/4>1\). Condition (12) prevents critical amplitude
concentration and already contains \(U(t)\), the norm whose boundedness is
the continuation target. Claiming either without a new argument would
disguise the terminal assumption.

## Surviving conditional suffix

If a new theorem supplies (12) and (13) with an a priori fixed \(K\), then
(11) proves (HF) for any fixed \(J\), hence for an input-selected \(J\).
The low-frequency bound in frequency.md then yields full signed pressure
absorption, the exact cubic balance gives a finite-horizon
\(L^\infty_tL^3_x\) bound, and endpoint continuation excludes finite maximal
time. This suffix is conditional on the two unproved large-data inputs.

## Non-claims and next distinct action

No universal \(\theta<1\), HF01 estimate, or global regularity theorem is
proved here. The amplitude families are arbitrary smooth snapshots, not
constructed solution segments. The new reusable result is the exact weighted
estimate (6) and its amplitude-tail refinement (11).

A distinct next action is to seek a **time-integrated good/bad-level
decomposition** that charges times when \(U(t)B_K(t)\) is large directly to
energy dissipation, while estimating the complementary times by (11). Such
an argument must produce an input-only measure or dissipation bound for the
bad-time set and must not choose \(K\) from the unknown future trajectory.
