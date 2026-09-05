# HF01: concentration scales and temporal spike budgets

Status: exploratory evidence, 2026-09-05. Consider the maximal classical
solution of the unforced three-dimensional Navier--Stokes equation on
\(\mathbb R^3\), with viscosity \(\nu>0\) and divergence-free Schwartz datum.
Write
\[
 m(t)=\|u(t)\|_3,\qquad E_0=\|u_0\|_2^2.
\]
Assume \(E_0>0\); the zero-datum solution is trivial.
This note asks whether a record \(L^3\) spike must persist long enough to
violate an energy-level spacetime budget. It derives an exact conditional
anti-spike lemma and a scale-compatible counter-scenario to the energy-only
closure. It does not construct a Navier--Stokes singularity.

## 1. Two unconditional budgets

Energy, interpolation, and Sobolev give
\[
 \int_0^{T_*}m(t)^4\,dt\le {C\over\nu}E_0^2.           \tag{1}
\]
The upper endpoint is understood as a supremum over compact subintervals.

There is also a useful instantaneous lower bound for the weighted cubic
dissipation
\[
 D_3(t)=\int\bigl(|u||\nabla u|^2
                    +|u||\nabla|u||^2\bigr)\,dx.
\]
Put \(z=|u|^{3/2}\). Since
\[
 \|\nabla z\|_2^2={9\over4}
       \int |u||\nabla|u||^2\le {9\over4}D_3,
\]
Sobolev yields
\[
 \|u\|_9^3=\|z\|_6^2\le C D_3.                        \tag{2}
\]
Interpolation,
\[
 \|u\|_3\le \|u\|_2^{4/7}\|u\|_9^{3/7},
\]
then gives the scale-correct coercive inequality
\[
 D_3(t)\ge c\,{m(t)^7\over E_0^2}.                    \tag{3}
\]
Unlike \(\int\|\nabla u\|_2^2\), however, \(\int D_3\) is not controlled by
the energy identity. Equation (3) becomes useful only if a signed pressure
estimate first pays for some positive part of \(D_3\); using it before that
would be circular in the HF programme.

## 2. A rigorous active-frequency lower bound

Fix a smooth low-pass operator \(S_{\le N}\) at dyadic frequency \(N\).
Bernstein and energy imply
\[
 \|S_{\le N}u(t)\|_3
 \le C N^{1/2}\|u(t)\|_2
 \le C N^{1/2}E_0^{1/2}.                              \tag{4}
\]
Suppose \(m(t)=M\), and define an active frequency \(N(t)\) to be any dyadic
number for which
\[
 \|S_{\le N(t)}u(t)\|_3\ge {M\over2}.                 \tag{5}
\]
For a smooth snapshot such an \(N(t)\) exists, but it need not be uniformly
bounded along a putative singular sequence. Equations (4)--(5) force
\[
 N(t)\ge c\,{M^2\over E_0}.                           \tag{6}
\]
Thus energy supplies a floor on the concentration frequency. It supplies no
ceiling. This direction matters: a lower bound on \(N\) makes the parabolic
time \(N^{-2}\) shorter and therefore weakens every persistence argument.

## 3. Exact conditional anti-spike lemma

Let \(R_k=2^kR_0\), and suppose \(t_k<T_*\) is the first time
\(m(t_k)=R_k\). Let \(s_k<t_k\) be the last time before \(t_k\) at which
\(m(s_k)=R_k/2\). Continuity gives such a time once \(R_0\) is above the
initial norm. The intervals \(I_k=(s_k,t_k)\) are disjoint: \(t_k\le s_{k+1}\).
Moreover,
\[
 R_k/2<m(t)<R_k\quad(s_k<t<t_k).                       \tag{7}
\]

The following two estimates would exclude infinitely many record levels:
\[
 t_k-s_k\ge c_0N_k^{-2},                              \tag{P}
\]
\[
 N_k\le C_0\,{R_k^2\over E_0},                        \tag{C}
\]
where \(N_k\) is an active frequency at the top of the \(k\)-th doubling
interval and \(c_0,C_0\) are allowed finite input-dependent constants,
uniform in \(k\). Indeed, (7), (P), and (C) give
\[
 \int_{s_k}^{t_k}m(t)^4dt
 \ge {R_k^4\over16}\,c_0N_k^{-2}
 \ge {c_0E_0^2\over16C_0^2}.                          \tag{8}
\]
Summing (8) over infinitely many disjoint levels contradicts (1). Hence:

> A scale-\(N_k\) doubling-time bound (P), together with the scale-covariant
> cascade ceiling (C), implies a finite-horizon \(L^\infty_tL^3_x\) bound.

This is a concrete alternative producer of the critical estimate. It uses no
Type-I hypothesis in physical space, but (C) is itself new critical
information. Combining (6) and (C) says the active frequency is comparable
to the least frequency compatible with the spike's \(L^2\) energy:
\[
 N_k\simeq {R_k^2\over E_0}.                           \tag{9}
\]
The lower comparison is known; the upper comparison is not.

Estimate (P) also does not follow merely from continuity of the classical
solution. Critical scaling leaves \(M=\|u(t_k)\|_3\) invariant while changing
every parabolic time by an arbitrary factor, so the standard scale-covariant
local theory does not produce a time from \(M\) alone. A universal positive
doubling-time theorem depending only on \(M\) would itself be new strong
information, not an energy consequence. A frequency-explicit stability
theorem may naturally yield time \(N_k^{-2}\), but its constants must not
depend on a still higher unbounded norm. Moreover, the required form is a
lower bound on the full doubling interval, not just continuity in an
unspecified neighborhood of \(t_k\).

## 4. What weighted dissipation would charge

If only (P) and the lower bound \(m\ge R_k/2\) hold, (3) gives
\[
 \int_{s_k}^{t_k}D_3dt
 \ge c\,{R_k^7\over E_0^2N_k^2}.                      \tag{10}
\]
Under the cascade ceiling (C), the right side is at least \(cR_k^3\).
Therefore any signed high-frequency absorption with \(\theta<1\) would make
successive record levels increasingly expensive. This is consistent with,
but does not prove, the desired HF estimate: the exact balance says that a
positive pressure flux can pay the entire \(D_3\) charge.

Indeed, across a doubling interval,
\[
 \int_{s_k}^{t_k}P_3dt
 = {R_k^3-(R_k/2)^3\over3}
   +\nu\int_{s_k}^{t_k}D_3dt.                         \tag{11}
\]
Thus for every \(\theta<1\),
\[
 \int_{s_k}^{t_k}(P_3-\theta\nu D_3)dt
 \ge {7\over24}R_k^3.                                 \tag{12}
\]
Equation (12) is not a contradiction; it shows exactly why an actual
unbounded record sequence would violate any finite pressure-absorption
remainder. It cannot be used to prove that remainder.

## 5. A scale-admissible counter-scenario

The known budgets allow a rapid ultraviolet cascade. Take formal record
heights and active frequencies
\[
 R_k=2^kR_0,\qquad N_k={R_k^3\over E_0},\qquad
 \delta_k=cN_k^{-2}.                                  \tag{13}
\]
On disjoint intervals of lengths \(\delta_k\), let a scalar norm profile have
height comparable to \(R_k\). Then
\[
 \sum_k R_k^4\delta_k
 =cE_0^2\sum_kR_k^{-2}<\infty.                        \tag{14}
\]
It therefore obeys the only unconditional \(L^3\) spacetime restriction (1)
while its record heights diverge in the finite total time
\(\sum_k\delta_k<\infty\).

The same schedule is compatible with the scaling of concentrated
divergence-free packets
\[
 u_k(x)=R_kN_k\phi(N_kx),
\]
where \(\phi\) is a fixed Schwartz divergence-free profile normalized in
\(L^3\). At a snapshot,
\[
 \|u_k\|_3\simeq R_k,\qquad
 \|u_k\|_2^2\simeq {R_k^2\over N_k}
                 ={E_0\over R_k},                    \tag{15}
\]
\[
 \|\nabla u_k\|_2^2\simeq R_k^2N_k.
\]
If such a packet persists for its parabolic time \(N_k^{-2}\), its ordinary
energy-dissipation cost scales as
\[
 N_k^{-2}\|\nabla u_k\|_2^2
 \simeq {R_k^2\over N_k}={E_0\over R_k},              \tag{16}
\]
which is summable. Its \(L^4_tL^3_x\) cost is the summable quantity in (14).
The chosen frequencies exceed the energy floor (6) by a factor \(R_k\), so
they violate precisely the proposed ceiling (C).

This construction is an exact scaling counter-scenario, not a sequence of
snapshots cut from one Navier--Stokes trajectory. It proves that the scalar
energy, \(L^4_tL^3_x\), parabolic-persistence, and ordinary dissipation
bookkeeping alone cannot exclude record blowup. A PDE argument must prevent
the escape \(N_kE_0/R_k^2\to\infty\), or exploit signed flux in a way absent
from those budgets.

For comparison, packet scaling gives
\[
 D_3[u_k]\simeq R_k^3N_k^2,\qquad
 P_3[u_k]\simeq R_k^4N_k^2
\]
when the fixed profile has nonzero pressure work. Over \(N_k^{-2}\), these
cost \(R_k^3\) and \(R_k^4\), respectively. They are not constrained by
energy; pressure can balance weighted dissipation and growth exactly as in
(11). No sign follows from this snapshot calculation.

## 6. Stronger cascade-budget repair

A ceiling at every record time is more than necessary. Define the
dimensionless ultraviolet excess
\[
 \Lambda_k={N_kE_0\over R_k^2}\ge c.                  \tag{17}
\]
Under (P), the contribution of the \(k\)-th doubling interval to (1) is
\[
 \int_{s_k}^{t_k}m^4dt
 \ge cE_0^2\Lambda_k^{-2}.                            \tag{18}
\]
Consequently the strictly weaker condition
\[
 \sum_{k:\,t_k<H}\Lambda_k^{-2}=\infty                \tag{CB}
\]
already rules out infinitely many record levels before any finite horizon
\(H\). A uniform ceiling \(\sup_k\Lambda_k<\infty\) implies (CB), but is not
required.

This isolates the minimal new cascade budget for the persistence route:

1. prove the scale-explicit doubling-time estimate (P);
2. prove that active frequencies along record doublings cannot have
   square-reciprocal ultraviolet excess summable as in (13).

Neither assertion is contained in energy. The counter-scenario has
\(\Lambda_k=R_k\) and \(\sum\Lambda_k^{-2}<\infty\), so (CB) is sharp for the
particular lower bound (18): weakening divergence to mere
\(\Lambda_k\to\infty\) gives no contradiction.

## Frontier record

**MODE / RESULT:** FALSIFY/REPAIR. Energy forces the active-frequency floor
(6), and a frequency-explicit persistence estimate plus the cascade budget
(CB) would yield the missing critical bound.

**FIRST GAP:** establish (P) and (CB) for actual arbitrary-data
Navier--Stokes record intervals. Neither follows from energy or critical
scaling.

**SURVIVING CONDITIONAL SUFFIX:** (P)+(CB) contradict the finite
\(L^4_tL^3_x\) budget if record heights are unbounded, hence give
\(L^\infty_tL^3_x\) on each finite horizon and feed the existing endpoint
continuation theorem.

**NON-CLAIMS:** the packet schedule is not a PDE solution, does not establish
blowup, and does not refute a signed trajectory estimate. The weighted
dissipation lower bound (3) is unconditional, but its time integral is not
energy-controlled.

**NEXT DISTINCT ACTION:** derive (P) from a frequency-localized mild
stability estimate and test whether the nonlinear energy flux can prove
(CB), or else construct an actual smooth trajectory segment whose active
frequency excess grows as fast as the schedule (13).
