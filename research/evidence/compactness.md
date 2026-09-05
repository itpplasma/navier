# Blow-up compactness and the ancient-solution alternative

Status: research evidence, checked 2026-09-05.  This note concerns the
unforced three-dimensional Navier--Stokes Cauchy problem on
\(\mathbb R^3\),
\[
 \partial_tu+u\cdot\nabla u+\nabla p=\nu\Delta u,
 \qquad \nabla\cdot u=0,
\]
with arbitrary smooth divergence-free rapidly decreasing initial data and
\(\nu>0\).  It gives reductions conditional on finite-time breakdown; it does
not prove that breakdown occurs or that it is impossible.

## 1. Exact rescaling and what energy does not control

For \(r>0\), a centre \((x_*,t_*)\), and fixed viscosity \(\nu\), set
\[
 u^{(r)}(y,s)=r\,u(x_*+ry,t_*+r^2s),\qquad
 p^{(r)}(y,s)=r^2p(x_*+ry,t_*+r^2s).
\]
This solves the same equation with the same \(\nu\).  Direct changes of
variables give
\[
 \|u^{(r)}(s)\|_{L^q(B_R)}
 =r^{1-3/q}\|u(t_*+r^2s)\|_{L^q(B_{rR}(x_*))},
\]
and, for \(I=(a,b)\),
\[
 \begin{aligned}
 \int_{B_R}|u^{(r)}(s)|^2dy
   &=r^{-1}\int_{B_{rR}(x_*)}|u(t_*+r^2s)|^2dx,\\
 \int_{I\times B_R}|\nabla u^{(r)}|^2\,dy\,ds
   &=r^{-1}\int_{(t_*+r^2I)\times B_{rR}(x_*)}|\nabla u|^2\,dx\,dt,\\
 \int_{I\times B_R}|u^{(r)}|^3\,dy\,ds
   &=r^{-2}\int_{(t_*+r^2I)\times B_{rR}(x_*)}|u|^3\,dx\,dt,\\
 \int_{I\times B_R}|p^{(r)}|^{3/2}\,dy\,ds
   &=r^{-2}\int_{(t_*+r^2I)\times B_{rR}(x_*)}|p|^{3/2}\,dx\,dt.
 \end{aligned}
\]
Thus the standard cylinder quantities
\[
 A(r)=r^{-1}\mathop{\rm ess\,sup}_{t_*-r^2<t<t_*}
       \int_{B_r(x_*)}|u|^2,
 \quad E(r)=r^{-1}\int_{Q_r}|\nabla u|^2,
\]
\[
 C(r)=r^{-2}\int_{Q_r}|u|^3,
 \quad D(r)=r^{-2}\int_{Q_r}|p-(p)_{B_r}|^{3/2}
\]
are scale invariant.  The unforced global energy inequality only yields
\[
 A(r)\le r^{-1}\|u_0\|_2^2,
 \qquad
 E(r)\le (2\nu r)^{-1}\|u_0\|_2^2.
\]
Both upper bounds diverge as \(r\downarrow0\).  It gives no uniform bound for
\(C(r)\) or \(D(r)\).  Consequently energy alone supplies neither the local
compactness nor the pressure compactness needed to pass a singular-scale
sequence to a suitable ancient limit.

There is also no useful repair by switching to the energy-preserving spatial
amplitude \(w^{(r)}=r^{3/2}u(x_*+ry,t_*+r^2s)\).  Substitution gives
\[
 \partial_sw^{(r)}+r^{-1/2}w^{(r)}\cdot\nabla w^{(r)}
 +\nabla \pi^{(r)}=\nu\Delta w^{(r)},
\]
after the corresponding pressure rescaling.  Hence an \(L^2\)-compact profile
decomposition is not a compactness theory for the original equation: its
nonlinear coefficient diverges instead of remaining one.

## 2. A mechanism that does work: point-picking in \(L^\infty\)

The following conditional reduction avoids the energy scaling gap.  Normalize
\(\nu=1\) by writing \(u(x,t)=\nu v(x,\nu t)\); undoing this normalization does
not change the conclusion.  Suppose a classical mild solution has maximal
lifespan \((0,T)\), \(T<\infty\).  Put
\(h(t)=\|u(t)\|_\infty\) and
\(H(t)=\sup_{0\leq s\leq t}h(s)\).  Choose record times
\(t_k\uparrow T\), numbers \(\gamma_k\downarrow1\), and points \(x_k\) such
that
\[
 M_k=|u(x_k,t_k)|\ge H(t_k)/\gamma_k.
\]
Finite maximal lifespan forces \(M_k\to\infty\).  Define
\[
 v_k(y,s)=M_k^{-1}u(x_k+M_k^{-1}y,t_k+M_k^{-2}s).
\]
Then
\[
 |v_k|\le\gamma_k\quad(-M_k^2t_k<s\le0),
 \qquad |v_k(0,0)|=1,
\]
and \(-M_k^2t_k\to-\infty\).  Interior estimates for uniformly bounded mild
solutions give a locally uniformly convergent subsequence on every compact
subset of \(\mathbb R^3\times(-\infty,0]\).  Its limit \(v\) is a bounded
ancient mild solution satisfying
\[
 |v|\le1,\qquad |v(0,0)|=1.
\]
This is Proposition 6.1 of Koch--Nadirashvili--Seregin--Sverak (KNSS), with
the construction and compactness stated in their Lemma 6.1
([primary preprint, Sections 4 and 6](https://arxiv.org/abs/0709.3599)).
Their hypotheses are a finite-time singularity of a whole-space mild solution
arising from bounded initial data.  Clay data lie in that initial class; the
use here remains conditional on a finite maximal classical lifespan.

This mechanism proves a genuine alternative:

> finite-time breakdown of the Clay-data mild solution implies existence of a
> nonzero bounded ancient mild solution on
> \(\mathbb R^3\times(-\infty,0]\).

It does not say that the ancient solution is suitable with globally finite
energy, has spatial decay, or has a zero trace at \(s=0\).  Those properties
do not follow from the displayed bounds.

## 3. Falsification of the proposed energy-rigidity closure

A tempting closure is: retain the original finite energy through the zoom,
deduce that the ancient limit decays at spatial infinity, and then invoke a
Liouville theorem.  The first implication fails.  At the point-picking scale
\(r_k=M_k^{-1}\),
\[
 \int_{B_R}|v_k(y,s)|^2dy
 =M_k\int_{B_{R/M_k}(x_k)}
       |u(x,t_k+M_k^{-2}s)|^2dx
 \le M_k\|u_0\|_2^2.
\]
The right side diverges.  It gives no bound uniform in \(k\), no global
\(L^2\) bound for \(v\), and no spatial-tail estimate.  In particular it does
not exclude a constant limit.  Nonzero constant vector fields are bounded
ancient mild solutions.  They are locally suitable, so merely adding local
suitability also does not produce rigidity.

The concentration forced by nontriviality is only scale-relative.  Local
uniform convergence and \(|v(0,0)|=1\) imply, for some fixed \(R,c>0\),
\[
 \int_{B_{R/M_k}(x_k)}|u(x,t_k)|^2dx\ge cM_k^{-1}.
\]
This lower bound tends to zero and is fully compatible with the fixed global
energy.  It is not a positive atom of kinetic energy at the singular point.

KNSS explicitly identify the remaining obstruction: in general dimension
three, classification of bounded ancient mild solutions is open, while their
Liouville conclusions cover two dimensions and restricted axisymmetric
classes.  Their paper also notes constants as the immediate obstruction after
Proposition 6.1 ([primary preprint](https://arxiv.org/abs/0709.3599)).  Thus the
proposed universal statement “every bounded ancient mild solution in 3D is
constant” cannot be imported as a theorem; and even if it were proved, one
would still need an inherited scale-invariant condition excluding the
nonzero constants.

## 4. What is sufficient for a suitable ancient limit

For rescalings about cylinders \(Q_{r_k}(x_k,t_k)\), a standard sufficient
compactness package on each fixed \(Q_R\) is a uniform bound of the form
\[
 \mathop{\rm ess\,sup}_{s\in(-R^2,0)}\int_{B_R}|u_k|^2
 +\int_{Q_R}|\nabla u_k|^2
 +\int_{Q_R}(|u_k|^3+|p_k-(p_k)_{B_R}|^{3/2})\le C_R,
\]
together with the local energy inequality.  The equation then controls a
negative-Sobolev time derivative; weak energy compactness plus local strong
compactness (typically \(L^3_{\rm loc}\), after interpolation) permits passage
through the nonlinearity and local energy inequality.  A singular-point
epsilon-regularity lower bound at the normalized cylinder is additionally
needed to prevent the limit from being zero.  The upper compactness bounds
and the lower nontriviality bound play different roles; neither implies the
other.

Uniform control of \(A(r_kR),E(r_kR),C(r_kR),D(r_kR)\) for each fixed \(R\)
would provide this package after rescaling.  Such a Type-I/Morrey-scale
assumption is extra information.  The global energy inequality gives only
the divergent estimates in Section 1.  Caffarelli--Kohn--Nirenberg partial
regularity supplies epsilon-regularity and smallness implications for suitable
weak solutions, but it does not supply these missing uniform upper bounds at
an arbitrary singular sequence; its primary source is
[Caffarelli--Kohn--Nirenberg, CPAM 35 (1982), 771--831](https://doi.org/10.1002/CPA.3160350604).

At the critical \(L^3\) endpoint, a uniform
\(L^\infty_tL^3_x\) bound does furnish scale-invariant control and enough
tightness for the Escauriaza--Seregin--Sverak blow-up/backward-uniqueness
argument.  Their theorem concludes regularity, rather than deriving that
critical bound from energy
([primary paper and DOI](https://doi.org/10.1070/RM2003v058n02ABEH000609)).
Accordingly, importing this route into the arbitrary-data problem simply
relocates the first gap to proving the uniform critical bound.

## 5. Exact surviving conditional suffix and first gap

**Surviving reduction.**  If a smooth Clay-data solution has finite maximal
time, the point-picking construction produces a nonzero bounded ancient mild
solution.  If instead one assumes uniform scale-invariant local energy,
dissipation, velocity, and pressure bounds at a singular sequence, suitable
compactness plus an epsilon-regularity lower bound produces a nontrivial
suitable ancient limit.

**First unsupported implication.**  No argument here derives from the global
energy inequality an inherited critical bound that both (i) gives compactness
or spatial control of the blow-up limit and (ii) excludes constants and every
other nonzero bounded ancient solution.  Nor is there a general 3D Liouville
theorem classifying all bounded ancient mild solutions.  Either result would
require new mathematical results; neither is established by the cited sources.

**Non-claims.**  This note does not rule out type-II, multi-scale, spatially
escaping, or non-self-similar concentration.  It does not upgrade a local
suitable limit to a finite-energy ancient solution.  It does not turn a
conditional critical-norm criterion into an a priori estimate for arbitrary
data.

**Next distinct action.**  Any attempted repair should state one explicit
scale-invariant quantity inherited from arbitrary finite-energy evolution and
prove both its compactness consequence and its exclusion of constant ancient
limits.  Without such a quantity, further ancient-solution classification does
not close the Clay alternative.
