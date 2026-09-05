# HF01 controller reconstruction

This note records the controller's mathematical work after the first Sol
attempts. All statements concern the original unforced R3 equation and the
maximal strong solution from divergence-free Schwartz data. The universal
high-pressure estimate remains unproved. Statements below are candidates for
independent audit before paper integration.

## Existential HF and global strong continuation

Let G mean that every such maximal strong solution has Tstar = infinity.
Let HF be the current manuscript's existential finite-horizon hypothesis,
with one universal theta in [0,1), and with J and the finite nonnegative
remainder allowed to depend on viscosity, the entire datum, and the finite
horizon. Then, using the imported endpoint theorem and local theory,

```text
HF is equivalent to G.
```

The forward direction is the reviewed paper argument. For the reverse,
assume G and fix nu,u0,H and J=0. On [0,H] the strong solution has bounded
high Sobolev norms by definition of its maximal strong lifespan and
persistence. The absolute pressure estimate

\[
 |Q_0(t)|\le C\|u(t)\|_6^3\|\nabla u(t)\|_2
\]

is therefore integrable. Set theta=0 and
\(A=\int_0^H|Q_0(t)|dt<\infty\). The HF inequality follows. The same
argument works for any preassigned theta in [0,1), since D3 is nonnegative.
This is a proof of equivalence conditional on G, not a method of proving G:
the unknown global continuation is used to justify the finiteness of A.

Consequently strict theta provides an additional dissipation bound in the
forward calculation, but does not make the existential finite-horizon
assertion logically stronger than G. An explicit dependence on a specified
finite list of initial norms would be additional quantitative information.
Nor is the assertion vacuous: without G, the required integral or supremum
may be infinite. This corrects the earlier informal distinction between a
mere critical bound and a supposedly strictly stronger existential HF.

The equivalence here is to global continuation of the selected strong
branch. Its implication to Clay alternative A is already audited. No new
converse from every conceivable globally smooth finite-energy solution
class to this Sobolev branch is needed or asserted.

## Repair of the amplitude split

The weighted Sol calculation proves, uniformly in J,
\[
 |Q_J|\le C U D_3,\qquad U=\|u\|_3,
\]
and a spatial integration-region split introduces the uncontrolled remainder
\(K\|u\|_4^4\). Splitting the source of pressure instead removes that
particular remainder.

Let \(E_0=\|u_0\|_2^2\), fix K>0, and set
\[
 B_K=\|u\mathbf1_{|u|>K}\|_3,\qquad
 p_J^\ell=(I-S_J)R_iR_j(u_i u_j\mathbf1_{|u|\le K}),
\]
\[
 p_J^h=(I-S_J)R_iR_j(u_i u_j\mathbf1_{|u|>K}).
\]
These are frequency-cutoff pressure components defined by Lp multipliers;
the discontinuous amplitude cutoff is never differentiated. Their sum is
the original high-output pressure. Uniform Calderon--Zygmund bounds give
\[
 \|p_J^\ell\|_3
 \le C\left(\int_{|u|\le K}|u|^6\right)^{1/3}
 \le C K^{4/3}E_0^{1/3}.                                    \tag{1}
\]
For \(f=|u|^{3/2}\), Sobolev and the weighted dissipation give
\(\|u\|_9^{3/2}\le C D_3^{1/2}\). Interpolating the high-amplitude
function between L3 and L9, without differentiating its indicator, yields
\[
 \|p_J^h\|_3\le C\|u\mathbf1_{|u|>K}\|_6^2
 \le C B_K^{1/2}\|u\|_9^{3/2}
 \le C B_K^{1/2}D_3^{1/2}.                                  \tag{2}
\]
The test factor satisfies
\[
 \|u\nabla|u|\|_{3/2}\le C U^{1/2}D_3^{1/2}.                  \tag{3}
\]
Thus, for every epsilon>0,
\[
 |Q_J|\le [\varepsilon+C(U B_K)^{1/2}]D_3
       +C\varepsilon^{-1}K^{8/3}E_0^{2/3}U.                  \tag{4}
\]
Unlike the previous spatial-region remainder, the final term is integrated
by energy. Indeed, for every tau<min(H,Tstar),
\[
 \int_0^\tau U\,dt
 \le H^{3/4}\left(\int_0^\tau U^4dt\right)^{1/4}
 \le C H^{3/4}\nu^{-1/4}E_0^{1/2}.                           \tag{5}
\]
The accumulated remainder in (4) is at most
\[
 C\varepsilon^{-1}K^{8/3}H^{3/4}\nu^{-1/4}E_0^{7/6}.          \tag{6}
\]

This repairs the L4-time-integrability obstruction in the first attempt.
The only unproved absorption input left in this method is a fixed K for
which U B_K is uniformly small through the possible endpoint.

That remaining input already encodes critical control. Since
\[
 U^3\le K E_0+B_K^3,
\]
a bound U B_K <= L implies, for X=U^3,
\[
 X^2\le K E_0 X+L^3,
\qquad
 X\le\frac{K E_0+\sqrt{K^2E_0^2+4L^3}}2.                    \tag{7}
\]
Thus even a finite bound on U B_K for one fixed K suffices directly for
critical boundedness. Proving such a bound remains a genuine global
continuation problem; the source split has removed an artificial extra
demand, not established a new arbitrary-data estimate.

## First invalid bridge in the proposed heat normal form

The Sol normal-form candidate defines high pressure as
\(-\langle\mathbb P Q_Jw,N\rangle\), where
\(w=|u|u\), \(N=(u\cdot\nabla)u\), and \(Q_J=I-S_J\).
This is not the correct high-pressure functional. Although
\(\langle w,N\rangle=0\), generally
\(\langle Q_Jw,N\rangle\ne0\). Frequency localization does not preserve
the transport cancellation.

The exact functional to use is
\[
 \mathcal H_J(u)=\langle Q_J w(u),(I-\mathbb P)N(u)\rangle
 =\int(p-S_Jp)u\cdot\nabla|u|.                               \tag{8}
\]
The real-even cutoff and orthogonal Leray projector are self-adjoint on L2
and bounded on the dual L3/L(3/2) spaces used below. Equation (8) follows
from \(\nabla p=-(I-\mathbb P)N\) and integration by parts; it does not
discard any truncated transport term.

## Corrected normal form and an energy-controlled transport term

Let \(G_s=e^{\nu s\Delta}\), \(a=\nu^{-1}2^{-2J}>0\), and define
\[
 \mathcal B_J(u)=-\int_a^\infty\mathcal H_J(G_su)ds.            \tag{9}
\]
The estimate \(|\mathcal H_J(v)|\le C\|v\|_6^3\|\nabla v\|_2\)
and heat bounds imply
\[
 |\mathcal B_J(u)|\le C\nu^{-1}2^{2J}\|u\|_2^4.               \tag{10}
\]
For v,h in the strong Sobolev class, the derivative of (8) is
\[
 D\mathcal H_J(v)[h]
 =\langle Q_J Dw(v)[h],(I-\mathbb P)N(v)\rangle
  +\langle Q_Jw(v),(I-\mathbb P)((h\cdot\nabla)v
                                      +(v\cdot\nabla)h)\rangle,\tag{11}
\]
where \(|Dw(v)[h]|\le2|v||h|\), including at v=0. Holder and multiplier
bounds give the useful derivative estimate
\[
 |D\mathcal H_J(v)[h]|\le C\left(
  \|v\|_6^2\|h\|_6\|\nabla v\|_2
  +\|v\|_6^3\|\nabla h\|_2\right).                         \tag{12}
\]
In particular, for \(v=G_su,h=G_sz\), the right side is bounded by
\(C(\nu s)^{-2}\|u\|_2^3\|z\|_2\). Integrating from positive a proves
the differentiability of (9) on L2, locally uniformly in u. It also
justifies the time chain rule along compact strong-solution intervals.

Since \(D\mathcal B_J(u)[\nu\Delta u]=\mathcal H_J(G_a u)\), the
projected equation gives
\[
 \mathcal H_J(u)=\frac d{dt}\mathcal B_J(u)
    +[\mathcal H_J(u)-\mathcal H_J(G_a u)]
    +D\mathcal B_J(u)[\mathbb P N(u)].                        \tag{13}
\]

The original attempt claimed that the last term lacks an energy-only
bound. The positive heat cutoff permits a better estimate. Set
\(h_s=G_s\mathbb P\operatorname{div}(u\otimes u)\). Fourier transformation
gives \(|\widehat{u\otimes u}|\le C\|u\|_2^2\), and hence
\[
 \|\nabla h_s\|_2\le C(\nu s)^{-7/4}\|u\|_2^2,
 \qquad \|h_s\|_6\le C(\nu s)^{-7/4}\|u\|_2^2.               \tag{14}
\]
For the first bound, integrate \(|\xi|^4 e^{-2\nu s|\xi|^2}\) in
three dimensions and take the square root; the Leray multiplier has norm
at most one. The second bound is the homogeneous Sobolev inequality.
Also \(\|G_su\|_6+\|\nabla G_su\|_2\le C(\nu s)^{-1/2}\|u\|_2\).
Substitution in (12) yields
\[
 |D\mathcal H_J(G_su)[h_s]|
 \le C(\nu s)^{-13/4}\|u\|_2^5.
\]
Therefore the exact transport remainder in (13) satisfies
\[
 |D\mathcal B_J(u)[\mathbb PN(u)]|
 \le C\nu^{-1}2^{9J/2}\|u\|_2^5.                            \tag{15}
\]
Along a solution its time integral is bounded by
\(CH\nu^{-1}2^{9J/2}E_0^{5/2}\). This is an admissible energy-controlled
finite-horizon remainder; its derivation never bounds the unsmoothed
nonlinearity in L2 by energy.

## The remaining short-heat defect

The corrected construction has only one uncontrolled term:
\[
 R_J(u)=\mathcal H_J(u)-\mathcal H_J(G_a u).                    \tag{16}
\]
The smoothed pressure work itself obeys
\[
 |\mathcal H_J(G_a u)|\le C2^{4J}\|u\|_2^4.                   \tag{17}
\]
Consequently, for fixed finite J, replacing the target H_J by R_J changes
its signed time integral only by an energy-controlled remainder. The
normal form has not weakened the unknown HF estimate: its short-heat
defect retains exactly the uncontrolled active scales.

This is a concrete repair of two failed steps, not a new monotonicity law.
The missing next mechanism must control R_J on actual trajectories, or
construct a different functional covering arbitrarily short heat times
without requiring the unknown critical norm. Starting the heat inverse at
zero removes R_J formally but destroys the energy-only integral estimate
used in (10); smooth-snapshot finiteness at zero does not provide a uniform
continuation bound.

## Type-I steering and scope

The user suggested a Type-I regime as a major intermediate test. The
controller checked Lei--Ren's published introduction and Theorem D:
[primary publisher text](https://doi.org/10.1016/j.aim.2024.109654).
Bounded scale-invariant dissipation at one point is stated there as an open
general regularity problem. Their improved one-point regularity theorem is
axisymmetric. A one-point hypothesis must seek regularity at that point;
it cannot directly produce the global whole-space HF estimate. A separate
Sol lane is deriving the necessary localized cubic identity and boundary
errors. This test does not replace the original arbitrary-data goal or
justify a forecast of journal acceptance.
