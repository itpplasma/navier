# HF11: an increasing finite heat step for the unregularized functional

Status: bounded analytic mechanism test, 2026-09-05.

This note shows that the unregularized pressure-entropy functional
\[
 \mathcal K(u)=\int_{\mathbb R^3}
 \left({|u|^3\over3}+p[u]|u|+p[u]_-^{3/2}\right)dx,
 \qquad p[u]=R_iR_j(u_i u_j),                                  \tag{1}
\]
need not decrease under the linear heat semigroup, even for smooth compactly
supported solenoidal initial data.  This is stronger than a sign failure for
one fixed regularization and avoids differentiating the speed at a zero set.

## Statement

There is \(h\in C_c^\infty(\mathbb R^3;\mathbb R^3)\),
\(\nabla\cdot h=0\), such that for every \(\nu>0\) there is
\(t_\nu>0\) with
\[
 \mathcal K(e^{\nu t_\nu\Delta}h)>\mathcal K(h).                \tag{2}
\]
The pressure in (1) is always the fixed Riesz-transform representative.
This explicit viscosity quantifier is the sole repair from
`hf11-review-heat-finite-step.md`; the original candidate and review are
frozen at `3a5844d`.

## A remote swirl with negative pressure

In cylindrical coordinates \((r,\vartheta,z)\), choose a nonzero smooth
nonnegative function \(f(r,z)\) supported in a small torus disjoint from a
ball about the origin, and put
\[
 U=f(r,z)e_\vartheta.                                           \tag{3}
\]
Because the support stays away from the axis, \(U\) is smooth and compactly
supported; axisymmetry and the absence of radial and vertical components give
\(\nabla\cdot U=0\).  The double-Riesz kernel has the form
\[
 K_{ij}(y)=c{3y_i y_j-|y|^2\delta_{ij}\over|y|^5},\qquad c>0.   \tag{4}
\]
At \(x=0\), the vector \(U(y)=f(y)e_\vartheta(y)\) is orthogonal to \(y\).
As the support excludes the kernel singularity,
\[
 p[U](0)=\int K_{ij}(-y)U_i(y)U_j(y)dy
 =-c\int {|U(y)|^2\over|y|^3}dy<0.                             \tag{5}
\]
The pressure is smooth in the gap between the origin and the torus.  Hence,
after shrinking the ball, there are a ball \(B\), a number \(c_*>0\), and a
positive separation between \(B\) and \(\operatorname{supp}U\) such that
\[
 p[U]\le-c_*\quad\hbox{on }B.                                  \tag{6}
\]

## Solenoidal high-frequency packet

Choose real \(\psi\in C_c^\infty(B)\), \(\psi\ne0\), and set
\[
 w_N=\nabla\times\left(N^{-1}\psi(x)e_3\sin(Nx_1)\right).      \tag{7}
\]
Then \(w_N\in C_c^\infty(B)\), \(\nabla\cdot w_N=0\), and
\[
 w_N=-\psi e_2\cos(Nx_1)
 +N^{-1}\bigl((\partial_2\psi)e_1-(\partial_1\psi)e_2\bigr)
       \sin(Nx_1).
\]
In particular, for every fixed \(1<q<\infty\),
\[
 \sup_N\|w_N\|_q<\infty,\qquad
 A_N:=\int(-p[U])|w_N|dx\longrightarrow
 {2\over\pi}\int(-p[U])|\psi|dx=:A_*>0.                       \tag{8}
\]
The last limit is the elementary periodic averaging of \(|\cos(Nx_1)|\).

For fixed \(s>0\), put \(t_N=s/(\nu N^2)\).  The explicit formula (7) gives
\(\|(\Delta+N^2)w_N\|_3\le C N\).  Duhamel's formula gives
\[
 e^{\nu t_N\Delta}w_N-e^{-s}w_N
 =\nu\int_0^{t_N}e^{\nu(t_N-\sigma)\Delta}
       e^{-\nu N^2\sigma}(\Delta+N^2)w_N\,d\sigma.
\]
The \(L^3\)-contraction of the heat semigroup therefore gives
\[
 \|e^{\nu t_N\Delta}w_N-e^{-s}w_N\|_3=O_s(N^{-1}).              \tag{9}
\]
Also
\[
 \|e^{\nu t_N\Delta}U-U\|_3
 \le \nu t_N\|\Delta U\|_3=O_s(N^{-2}).                        \tag{10}
\]

## Exact disjoint-support expansion

The functional \(\mathcal K\) is locally Lipschitz on \(L^3\).  Indeed,
the pressure map is locally Lipschitz from \(L^3\) to \(L^{3/2}\), and
\[
 \|p_-^{3/2}-q_-^{3/2}\|_1
 \le C\bigl(\|p\|_{3/2}^{1/2}+\|q\|_{3/2}^{1/2}\bigr)
          \|p-q\|_{3/2}.                                      \tag{11}
\]
The cubic and pressure-speed terms obey the analogous standard Hölder
bounds.

Because \(U\) and \(w_N\) have disjoint supports, for \(0\le b\le1\),
\[
 |U+bw_N|=|U|+b|w_N|,\qquad
 p[U+bw_N]=p[U]+b^2p[w_N].                                    \tag{12}
\]
Expanding the first two terms of (1) exactly and using (11) for the entropy
term gives, uniformly in \(N\),
\[
 \mathcal K(U+bw_N)=\mathcal K(U)-bA_N+O(b^2).                 \tag{13}
\]
For clarity, every omitted term is harmless: the cubic packet is \(O(b^3)\);
the terms \(b^2\int p[w_N]|U|\) and
\(b^3\int p[w_N]|w_N|\) are bounded by the uniform \(L^3\) norm of
\(w_N\); and the entropy change is \(O(b^2)\) by (11) and
\(\|b^2p[w_N]\|_{3/2}=O(b^2)\).

Fix \(s>0\) and write \(\lambda=e^{-s}<1\).  From local Lipschitz continuity
and (9)--(10), for each fixed \(a\in(0,1]\),
\[
 \mathcal K(e^{\nu t_N\Delta}(U+aw_N))
 =\mathcal K(U+a\lambda w_N)+o_{N\to\infty}(1).                \tag{14}
\]
Applying (13) at \(b=a\lambda\) and \(b=a\) yields
\[
 \begin{split}
 &\mathcal K(e^{\nu t_N\Delta}(U+aw_N))-\mathcal K(U+aw_N)\\
 &\qquad=a(1-\lambda)A_N+O(a^2)+o_{N\to\infty}(1).             \tag{15}
 \end{split}
\]
The constant in \(O(a^2)\) is independent of \(N\).  Choose \(a>0\) so
small that this error is less than
\(a(1-\lambda)A_*/4\), and then choose \(N\) large enough that
\(A_N>A_*/2\) and the last error has the same bound.  The right-hand side of
(15) is positive.  Taking \(h=U+aw_N\) proves (2).

## Scope

This is an exact finite-step statement for the true linear heat evolution of
a smooth compactly supported solenoidal field.  It does not depend on a
regularized derivative or assign a derivative to \(|u|\) on a zero set.  It
shows that static coercivity of \(\mathcal K\) cannot be combined with a
universal claim that its heat part is nonincreasing.

The heat trajectory is not a Navier--Stokes trajectory: the nonlinear Euler
contribution is absent.  Thus (2) does not determine the sign of the full
Navier--Stokes derivative, disprove a possible cancellation between its heat
and Euler parts, establish pressure absorption, or bear on global regularity.

## Frontier record

**MODE / RESULT:** FALSIFY.  Unregularized \(\mathcal K\) can increase over a
finite interval of the linear heat flow.

**FIRST GAP:** any modified-energy use must control the complete heat
contribution together with the nonlinear contribution; convexity of the
pressure entropy does not give heat monotonicity.

**SURVIVING CONDITIONAL SUFFIX:** the static coercivity of \(\mathcal K\)
survives unchanged.

**NON-CLAIMS:** no Navier--Stokes trajectory counterexample, endpoint
estimate, HF bound, blow-up, or regularity conclusion is asserted.
