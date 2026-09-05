# HF17: a cubic quotient functional that removes gradients

MODE / RESULT: **DISCOVER.**  The cubic distance from a velocity to the
closed \(L^3\) gradient subspace is coercive on solenoidal fields, invariant
under Navier--Stokes scaling, nonincreasing under heat flow, and Fréchet
differentiable.  Its derivative annihilates every admissible gradient,
including the pressure gradient when that gradient belongs to the stated
space.  No estimate for the remaining transport flux is obtained.

## 1. Definition and the minimizing representative

Let
\[
 X=L^3(\mathbb R^3;\mathbb R^3),\qquad
 \mathcal G_3=
 \overline{\{\nabla\phi:\phi\in C_c^\infty(\mathbb R^3)\}}^{\,L^3}.
                                                               \tag{1}
\]
For \(u\in X\), define
\[
 \mathcal Q(u)=\inf_{q\in\mathcal G_3}
 {1\over3}\int_{\mathbb R^3}|u+q|^3\,dx.             \tag{2}
\]

The space \(X\) is reflexive.  A minimizing sequence \(q_n\) makes
\(u+q_n\) bounded in \(X\), hence \(q_n\) bounded.  After taking a weakly
convergent subsequence, closed convexity of \(\mathcal G_3\) and weak lower
semicontinuity give a minimizer \(q(u)\).  Strict convexity of \(L^3\) makes
the minimizing representative
\[
 w(u)=u+q(u)                                         \tag{3}
\]
unique.

Equivalently, if \(\pi:X\to X/\mathcal G_3\) is the quotient map, then
\[
 \mathcal Q(u)={1\over3}\|\pi u\|_{X/\mathcal G_3}^3,
 \qquad \|w(u)\|_3=\|\pi u\|_{X/\mathcal G_3}.         \tag{4}
\]
Thus \(\mathcal Q\) depends only on the class of \(u\) modulo gradients.

First variation with respect to \(q\) at the minimizer gives
\[
 \boxed{\quad
 \int_{\mathbb R^3}|w|w\cdot q\,dx=0
 \quad\hbox{for every }q\in\mathcal G_3.
 \quad}                                               \tag{5}
\]
The pairing is legitimate because \(|w|w\in L^{3/2}\).  In distributional
language, (5) says
\[
 \operatorname{div}(|w|w)=0.                         \tag{6}
\]
This is a nonlinear divergence condition on the minimizing representative;
it does not imply that \(w\) is smooth.

## 2. Coercivity on solenoidal fields

Let \(\mathbb P\) be the Leray projection, bounded on \(L^3\), and suppose
\(u\in X\) is distributionally solenoidal, so \(\mathbb Pu=u\).
For \(\phi\in C_c^\infty\), \(\mathbb P\nabla\phi=0\), hence by closure
\[
 \mathbb Pq=0\qquad(q\in\mathcal G_3).
\]
Applying \(\mathbb P\) to (3) gives \(u=\mathbb Pw\), and therefore
\[
 \|u\|_3\le \|\mathbb P\|_{L^3\to L^3}\|w\|_3.        \tag{7}
\]
The admissible choice \(q=0\) supplies the other inequality:
\[
\boxed{\quad
 {1\over3\|\mathbb P\|_{3\to3}^3}\|u\|_3^3
 \le\mathcal Q(u)\le {1\over3}\|u\|_3^3.
\quad}                                               \tag{8}
\]
Thus \(\mathcal Q\) is quantitatively equivalent to the critical cubic norm
on the solenoidal subspace.

## 3. Homogeneity and Navier--Stokes scaling

Because \(\mathcal G_3\) is a linear space,
\[
 \mathcal Q(au)=|a|^3\mathcal Q(u)\qquad(a\in\mathbb R). \tag{9}
\]
For the Navier--Stokes spatial scaling
\[
 (\mathcal S_\lambda u)(x)=\lambda u(\lambda x),
 \qquad\lambda>0,
\]
the \(L^3\) norm is invariant.  Moreover
\[
 \mathcal S_\lambda(\nabla\phi)
 =\nabla[\phi(\lambda\,\cdot)],
\]
so \(\mathcal S_\lambda\) maps \(\mathcal G_3\) bijectively to itself.
Changing variables in (2) gives
\[
 \boxed{\quad
 \mathcal Q(\mathcal S_\lambda u)=\mathcal Q(u).
\quad}                                               \tag{10}
\]

## 4. Heat monotonicity

Let \(G_t=e^{t\Delta}\).  This is a contraction on \(L^3\).  It also
preserves the closed gradient space:
\[
 G_t\mathcal G_3\subset\mathcal G_3.                 \tag{11}
\]
For a generating gradient,
\(G_t\nabla\phi=\nabla G_t\phi\).  Although \(G_t\phi\) is not compactly
supported, it and its derivatives have rapid Gaussian decay; cutting off
the potential shows that \(\nabla G_t\phi\) is an \(L^3\) limit of gradients
of compactly supported smooth functions.  Boundedness of \(G_t\) extends
this conclusion to the closure in (1).

Let \(w=u+q(u)\) be the minimizer.  Then
\[
 G_tu+G_tq(u)
\]
is an admissible representative of the class of \(G_tu\).  Hence
\[
\boxed{\quad
 \mathcal Q(G_tu)
 \le {1\over3}\|G_tw\|_3^3
 \le {1\over3}\|w\|_3^3
 =\mathcal Q(u).
\quad}                                               \tag{12}
\]
This is a genuine global heat-semigroup inequality and uses no
differentiability or smoothness of \(w\).

## 5. Fréchet derivative and exact pressure cancellation

The quotient \(Y=X/\mathcal G_3\) is uniformly smooth because it is a
quotient of the uniformly smooth space \(L^3\).  Therefore
\(y\mapsto\|y\|_Y^3/3\) is Fréchet differentiable, including with derivative
zero at \(y=0\).  Pulling this function back by the bounded quotient map
\(\pi\) proves that \(\mathcal Q\) is Fréchet differentiable on \(X\).

The derivative can be identified without an abstract representative.
Equation (5) says
\[
 j(w):=|w|w\in\mathcal G_3^\perp\subset L^{3/2}.      \tag{13}
\]
Moreover,
\[
 \|j(w)\|_{3/2}=\|w\|_3^2,\qquad
 \langle j(w),u\rangle
 =\langle j(w),w\rangle=\|w\|_3^3.                  \tag{14}
\]
Thus \(j(w)\) is exactly the norming functional for the quotient class
\(\pi u\), with the normalization appropriate to the cubic power.  It
follows that
\[
\boxed{\quad
 D\mathcal Q(u)[h]
 =\int_{\mathbb R^3}|w(u)|w(u)\cdot h\,dx
 \qquad(h\in L^3).
\quad}                                               \tag{15}
\]
At \(\pi u=0\), one has \(w=0\), and (15) again gives the zero derivative.

Combining (5) and (15) gives the exact gradient invariance
\[
 D\mathcal Q(u)[q]=0\qquad(q\in\mathcal G_3).         \tag{16}
\]
In particular, whenever a pressure representative has
\(\nabla p\in\mathcal G_3\),
\[
 \boxed{\quad D\mathcal Q(u)[-\nabla p]=0.\quad}      \tag{17}
\]
For a smooth rapidly decreasing velocity, the associated pressure gradient
belongs to \(\mathcal G_3\): mollify its potential and cut it off, with the
cutoff error converging in \(L^3\).  More generally, (17) is asserted exactly
under the membership condition in (1), rather than from a formal integration
by parts.

## 6. What remains for Navier--Stokes

For a sufficiently regular Navier--Stokes velocity for which the indicated
directions lie in \(L^3\),
\[
 u_t=\nu\Delta u-(u\cdot\nabla)u-\nabla p,
\]
formula (15) and (17) give only
\[
 {d\over dt}\mathcal Q(u)
 =\nu D\mathcal Q(u)[\Delta u]
 -\int |w|w\cdot (u\cdot\nabla)u.                   \tag{18}
\]
Heat monotonicity implies the heat directional derivative is nonpositive
when this derivative exists.  In particular, if \(\Delta u\in L^3\), then
\[
 D\mathcal Q(u)[\Delta u]
 =\lim_{t\downarrow0}{\mathcal Q(G_tu)-\mathcal Q(u)\over t}\le0. \tag{19}
\]
It supplies no sign or input-only bound for
the transport flux
\[
\boxed{\quad
 \mathfrak T(u)=
 -\int_{\mathbb R^3}|w(u)|w(u)\cdot(u\cdot\nabla)u.
\quad}                                               \tag{20}
\]
The minimizer \(w\) is only an \(L^3\) metric representative.  No derivative
of \(w\), weighted heat-dissipation identity, integration by parts in
\(\mathfrak T\), or pressure estimate is justified by the variational
construction alone.

## 7. Frontier record

CLAIM AND SCOPE: Equations (3)--(17) hold on \(L^3\), with coercivity (8)
restricted to solenoidal fields.  Heat monotonicity (12) holds for the full
semigroup.  Pressure cancellation holds for gradients belonging to the
closed space (1).

EVIDENCE: Reflexivity and strict convexity give the unique representative;
the quotient norm gives Fréchet differentiability; Leray boundedness gives
coercivity; invariance of the gradient space gives scaling and heat
contraction; the Euler condition (5) identifies the derivative and kills
gradients exactly.

FIRST GAP: control the transport flux (20) along arbitrary-data classical
Navier--Stokes trajectories by quantities available from the input.  This is
a rewritten critical nonlinear gap.

SURVIVING CONDITIONAL SUFFIX: Any one-sided input-only spacetime estimate for
(20), strong enough to combine with (12), would control the coercive critical
functional \(\mathcal Q\).  No such estimate is supplied here.

NON-CLAIMS: No smoothness of the minimizer, weighted heat dissipation,
transport-flux sign, pressure absorption, HIGH-PRESSURE theorem, critical
continuation bound, regularity result, or novelty claim is asserted.

NEXT DISTINCT ACTION: derive structural information about the nonlinear
projection \(u\mapsto w(u)\) that can be used in (19), without differentiating
the merely \(L^3\) representative.
