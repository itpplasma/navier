# R3 proof architecture through critical \(L^3\) control

Status: research architecture only, prepared before Phase I.  It is not a
proof of the lemma isolated below and does not claim a solution of the
Millennium problem.

## Claim and conventions

Fix \(\nu>0\).  Let \(u_0\in\mathcal S(\mathbb R^3;\mathbb R^3)\) be real
valued and divergence free.  The target is the unforced Cauchy problem

\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
 \qquad \nabla\cdot u=0,\qquad u(0)=u_0.                 \tag{NS}
\]

All spatial norms below are on \(\mathbb R^3\).  A maximal classical solution
means the unique local strong solution, smoothed for positive time, on
\([0,T_*)\), where \(0<T_*\leq\infty\).  Constants may depend on the complete
datum \(u_0\) and on \(\nu\), but never on a terminal time below \(T_*\).

The route has one manuscript-owned mathematical gap.  Everything after that
gap is a conditional suffix assembled from the exact balance below, the
Escauriaza--Seregin--Sverak (ESS) endpoint theorem, local strong existence,
and the energy identity.  Applicability of each published theorem still needs
the source-level audit required by the project.

## The exact reduction

For a smooth decaying solution put

\[
 Y(t)=\|u(t)\|_3^3,
 \quad
 D_3(t)=\int_{\mathbb R^3}
 \left(|u|\,|\nabla u|^2+|u|\,|\nabla |u||^2\right)\,dx,
\]

where the second integrand is defined to be zero at \(u=0\).  Testing (NS)
against \(|u|u\), first with \((|u|^2+\varepsilon)^{1/2}u\) and then sending
\(\varepsilon\downarrow0\), gives

\[
 {1\over3}Y'(t)+\nu D_3(t)
 =P_3(t):=\int_{\mathbb R^3}p\,u\cdot\nabla|u|\,dx.     \tag{1}
\]

Indeed, incompressibility makes the transport contribution
\(\frac13\int u\cdot\nabla|u|^3\) vanish, while

\[
 -\int \Delta u\cdot |u|u
 =\int |u||\nabla u|^2+|u||\nabla|u||^2.
\]

The pressure is fixed, harmlessly up to a function of time, by
\(p=R_iR_j(u_i u_j)\).  Constants added to \(p\) do not alter \(P_3\), since
\(\int\operatorname{div}(|u|u)=0\).  Thus (1) identifies a concrete term, not
an unspecified nonlinear remainder.

### First new missing lemma (uniform critical pressure absorption)

There exists a universal \(\theta\in[0,1)\) such that, for every \(\nu>0\),
divergence-free Schwartz datum \(u_0\), and finite horizon \(H>0\), one can
give a finite bound \(A(\nu,u_0,H)\) from the input data alone, for which
the maximal classical solution obeys, for every
\(0<\tau<\min\{H,T_*\}\),

\[
 \int_0^\tau P_3(t)\,dt
 \leq \theta\nu\int_0^\tau D_3(t)\,dt
      +A(\nu,u_0,H).                                   \tag{PA}
\]

The quantifiers include arbitrary large data. A proof must establish the
finiteness of the bound without defining it through an unbounded trajectory
supremum. A recipe using explicitly named initial norms would accomplish
this; uniformity on bounded initial Sobolev sets is an optional stronger
target. The remainder may not depend on \(\tau,T_*\), the trajectory, the
unknown supremum of \(\|u(t)\|_3\), or any higher solution norm whose
finiteness is equivalent to continuation.  Dependence on \(H\) is allowed,
but \(A(\nu,u_0,H)\) must be finite for every finite \(H\). No
smallness, symmetry, sign, spectral support, or modified nonlinearity is
allowed.  A proof with \(\theta=1\) gives no coercive spacetime estimate but
still bounds \(Y\) through (1); hence the strictly subunit value is included
to expose the proposed diffusion mechanism, while the weaker sufficient
statement is (PA) with \(\theta=1\).

Integrating (1) and applying (PA) yields the two simultaneous estimates

\[
 \sup_{0\leq t<\min\{H,T_*\}}\|u(t)\|_3^3
 \leq \|u_0\|_3^3+3A(\nu,u_0,H),                      \tag{2}
\]
\[
 3(1-\theta)\nu\int_0^{\min\{H,T_*\}}D_3(t)\,dt
 \leq \|u_0\|_3^3+3A(\nu,u_0,H),                      \tag{3}
\]

Here (2) is read on \([0,\min\{H,T_*\})\).  If \(T_*<\infty\), choose any
finite \(H>T_*\); this is the uniform endpoint bound used below.

Only (2) is needed for ESS.  Equation (3) is extra content that makes (PA)
a potentially stronger mechanism than a renamed assertion of (2).

## Complete conditional implication chain

1. Local strong theory gives a unique maximal solution on \([0,T_*)\).  For
   Schwartz data it is classical; standard cutoff and regularization
   arguments justify (1) on each compact subinterval.  It satisfies the
   energy equality
   \[
    \|u(t)\|_2^2+2\nu\int_0^t\|\nabla u(s)\|_2^2ds
    =\|u_0\|_2^2.                                      \tag{4}
   \]
2. Assume (PA).  If \(T_*<\infty\), choose a finite \(H>T_*\).  Then (1)
   gives (2) uniformly all the way to the maximal endpoint.  Thus
   \(u\in L^\infty((0,T_*);L^3)\), with essential supremum bounded by the
   displayed constant.
3. On every interval strictly below \(T_*\), the classical finite-energy
   solution is also a suitable weak solution: its local energy equality
   implies the local energy inequality.  No cylinder containing \(t=T_*\) is
   asserted at this stage.
4. Use the ESS theorem in its standard whole-space blow-up/continuation
   corollary: if a maximal finite-energy strong solution has \(T_*<\infty\),
   then \(\limsup_{t\uparrow T_*}\|u(t)\|_3=\infty\).  The uniform bound from
   step 2 contradicts this.  Equivalently, a source formulation proved first
   for suitable weak solutions must be accompanied by the published argument
   deriving this terminal-time continuation corollary; interior regularity
   only for \(t<T_*\) is insufficient.
5. Consequently \(T_*=\infty\).  Parabolic bootstrapping gives smooth
   \(u,p\) at every finite time, including compatibility with the smooth datum
   at \(t=0\).  Equation (4) supplies Clay's single uniform kinetic-energy
   bound, \(\int|u(x,t)|^2dx\leq\|u_0\|_2^2\), for every \(t\geq0\).

The ESS citation intended for the source audit is Escauriaza, Seregin and
Sverak, *\(L_{3,\infty}\)-solutions of Navier--Stokes equations and backward
uniqueness*, Russian Math. Surveys 58 (2003), 211--250,
doi:10.1070/RM2003v058n02ABEH000609.  The notation \(L_{3,\infty}\) there must
be checked against the theorem text: in this route the needed hypothesis is
\(L^\infty_tL^3_x\), not the Lorentz space \(L^{3,\infty}_x\).

Viscosity normalization causes no gap.  Setting \(s=\nu t\),
\(v(x,s)=u(x,t)/\nu\), and \(q(x,s)=p(x,t)/\nu^2\) transforms (NS) into the
unit-viscosity equation; finiteness of \(\|u\|_{L^\infty_tL^3_x}\) is
equivalent to finiteness of \(\|v\|_{L^\infty_sL^3_x}\).

This chain concerns \(\mathbb R^3\) only.  It does not silently prove the
periodic alternative, and bounded-domain versions introduce boundary terms
both in (1) and in the endpoint theorem.  At \(t=0\), no ESS endpoint argument
is needed because the datum and local solution are already smooth.  At a
putative finite \(T_*\), a bound merely on every \([0,T]\), with constants
diverging as \(T\uparrow T_*\), is insufficient; (PA) is deliberately uniform.

## Energy control and temporal concentration

Sobolev and interpolation give

\[
 \|u(t)\|_3^4\leq \|u(t)\|_2^2\|u(t)\|_6^2
 \leq C\|u_0\|_2^2\|\nabla u(t)\|_2^2.
\]

After integration and (4),

\[
 \int_0^T\|u(t)\|_3^4dt
 \leq {C\over2\nu}\|u_0\|_2^4                 \tag{5}
\]

for every \(T<T_*\).  This supercritical spacetime estimate permits
arbitrarily high, increasingly narrow \(L^3\) spikes and therefore does not
imply (2).  Any proposed anti-spike argument must quantify a persistence time
whose cost contradicts (5); critical scaling prevents that time from being a
function of the \(L^3\) height alone.

Elementary Calderon--Zygmund estimates also reveal the obstruction rather
than remove it.  For example,

\[
 \|p\|_3\lesssim\|u\|_6^2,
 \qquad
 |P_3|\leq\|p\|_3\|u\nabla|u|\|_{3/2}
 \lesssim\|u\|_6^3\|\nabla u\|_2.                     \tag{6}
\]

The right side of (6) is not controlled by (4) or by \(D_3\) with an
integrable energy-level remainder.  Treating it by Young's inequality and
then assuming the resulting higher norm is finite would be circular.

## Independent stronger mechanisms worth testing

These are separate ways one might prove (PA), or bypass it with a stronger
statement.  None is asserted.

* **Instantaneous pressure coercivity.**  Prove
  \(P_3(t)\leq\theta\nu D_3(t)+g_{u_0,\nu}(t)\), where
  \(\theta<1\) and \(g\in L^1(0,\infty)\) has an a priori integral bound.
  This implies (PA) directly and localizes the required cancellation in time.
* **Dyadic flux summability.**  Decompose \(P_3\) into interactions at output
  frequency \(2^j\), prove that high--high-to-low and neighboring-shell
  contributions admit a signed telescoping part plus an \(\ell^1_jL^1_t\)
  error controlled by (4), and recover (PA) after summing.  A bound on each
  absolute interaction separately is unlikely to work: it discards precisely
  the pressure cancellation being sought.
* **Quantified anti-spike persistence with a frequency scale.**  If
  \(\|u(t_0)\|_3=M\), locate a scale \(N(t_0)\) carrying a fixed portion of
  that norm and prove persistence for \(cN^{-2}\), together with an
  energy-dissipation cost at least \(cM^4N^{-2}\).  To contradict (5), a
  second estimate must prevent \(N\) from escaping too rapidly.  Merely
  proving persistence at an unspecified scale does not suffice.
* **Critical concentration exclusion.**  A uniform theorem excluding
  concentration of a fixed \(L^3\) mass in every parabolic ball approaching
  \(T_*\) would combine with epsilon regularity to bypass the global pressure
  balance and is logically stronger than ruling out one self-similar profile.

## Falsifiers and audit tests

For a proposed explicit recipe \(A\), the earliest decisive falsifier is a
family of genuine smooth unforced solutions \(u^{(n)}\), a fixed finite
horizon \(H\), times \(\tau_n<\min\{H,T_*^{(n)}\}\), and data for which the
recipe values \(A(\nu,u_0^{(n)},H)\) stay uniformly bounded, but

\[
 \int_0^{\tau_n}P_3^{(n)}dt-\theta\nu
 \int_0^{\tau_n}D_3^{(n)}dt\longrightarrow+\infty.
\]

Tests on arbitrary divergence-free snapshots can refute an instantaneous
coercivity proposal, but cannot refute the spacetime lemma because snapshots
need not lie on one Navier--Stokes trajectory.  Numerical tests can discover
such a mechanism or sign failure but cannot prove the universal lemma.

Reject a purported proof immediately if it contains any of the following:

* replacing \(P_3\) by \(|P_3|\) and invoking an estimate whose remainder
  requires \(L^\infty_tL^3_x\), \(L^1_tL^\infty_x\), or a higher continuation
  norm;
* replacing the uniform remainder in (PA) by a functional that depends on
  \(T_*\), \(\tau\), the full trajectory, or its unknown critical supremum;
* using (5) as if time integrability implied an essential supremum;
* importing small-data, axisymmetric, averaged, hyperdissipative, forced,
  periodic, or bounded-domain results into the arbitrary-data R3 claim;
* confusing ESS's \(L^\infty_tL^3_x\) endpoint with weak spatial
  \(L^{3,\infty}_x\), or obtaining regularity only away from \(t=T_*\);
* asserting that a blow-up-rate lower bound contradicts (5) without proving
  enough temporal persistence for its peaks.

## Frontier record

**Mode / result:** DISCOVER/REPAIR; the route is reduced to the signed pressure
absorption lemma (PA), with an exact critical balance and falsifiers.

**Established conditional suffix:** (PA) implies (2); (2) plus suitability and
the terminal-time ESS theorem excludes finite \(T_*\); local continuation and
energy equality then give the R3 conclusion.

**First gap:** prove (PA) for every divergence-free Schwartz datum and its
maximal unforced R3 solution, with the stated non-circular dependence.

**Non-claims:** (PA) is unproved; the source audit and exact maximal-solution
form of ESS/GKP are recorded separately in `literature/critical-criteria.md`
and `review-pressure.md`. No Phase I formalization has begun and no Clay
alternative is settled.

**Next distinct action:** attack (PA) through signed dyadic pressure flux while
an independent falsification pass searches for smooth trajectory segments
with positive pressure work overwhelming \(D_3\).
