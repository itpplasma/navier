# HF10: evolution of the pressure--speed correction

Status: analytic mechanism test at frozen base
`4a377b5550a3fb46c0ad85933a72d7f3f44771e9`, 2026-09-05.

This note derives the exact evolution of a critical cubic correction for an
actual classical solution of the unforced three-dimensional Navier--Stokes
equation on \(\mathbb R^3\).  It tests cancellation of the cubic pressure
work.  It does not claim a sign or coercivity for the resulting functional.

## Setup and pressure gauge

Fix \(0<T<T_*\), and assume
\[
 u\in C([0,T];H^m),\qquad u_t\in C([0,T];H^{m-2}),\qquad m\ge4.       \tag{1}
\]
Write
\[
 N=(u\cdot\nabla)u,\qquad
 p=R_iR_j(u_i u_j),\qquad V=-\mathbb P N.                         \tag{2}
\]
The pressure in (2) is the fixed Riesz-transform representative, not a
pressure modulo a time-dependent spatial constant.  This choice is essential
because the correction below is not gauge invariant.  With the convention
in (2),
\[
 u_t=\nu\Delta u+V=\nu\Delta u-N-\nabla p.                       \tag{3}
\]
For \(\epsilon>0\), set
\[
 r_\epsilon=(\epsilon^2+|u|^2)^{1/2},\qquad
 n_\epsilon={u\over r_\epsilon},                                \tag{4}
\]
\[
 F_\epsilon={1\over3}\int(r_\epsilon^3-\epsilon^3)\,dx,
 \qquad B_\epsilon=\int p(r_\epsilon-\epsilon)\,dx.             \tag{5}
\]
Both integrals are finite: the first density is bounded by a constant times
\(|u|^3+\epsilon|u|^2\), while \(r_\epsilon-\epsilon\le |u|\) and
\(p,u\in L^2\).  No spatial decay beyond (1) is assumed.

## Exact regularized identity

Define
\[
 \begin{split}
 D_\epsilon={}&\int r_\epsilon|\nabla u|^2\,dx
                 +\int r_\epsilon|\nabla r_\epsilon|^2\,dx,\\
 P_\epsilon={}&\int p\,u\cdot\nabla r_\epsilon\,dx.             \tag{6}
 \end{split}
\]
Then
\[
 {d\over dt}F_\epsilon+\nu D_\epsilon=P_\epsilon.               \tag{7}
\]
Indeed, the transport contribution is the integral of
\(-u\cdot\nabla((r_\epsilon^3-\epsilon^3)/3)\), and the pressure
contribution is \(-\int r_\epsilon u\cdot\nabla p=P_\epsilon\).

The fixed pressure representative is differentiable along the solution and
\[
 p_t=R_iR_j(u_{t,i}u_j+u_i u_{t,j})
     =2R_iR_j(u_i u_{t,j}).                                    \tag{8}
\]
The second equality follows by exchanging the symmetric indices \(i,j\).
Consequently
\[
 {d\over dt}B_\epsilon
 =2\int(r_\epsilon-\epsilon)R_iR_j(u_i u_{t,j})\,dx
   +\int p\,n_\epsilon\cdot u_t\,dx.                           \tag{9}
\]
Substitution of (3) gives
\[
 \begin{split}
 {d\over dt}B_\epsilon={}&
  2\nu\int(r_\epsilon-\epsilon)R_iR_j(u_i\Delta u_j)\,dx\\
 &+\nu\int p\,n_\epsilon\cdot\Delta u\,dx
  +2\int(r_\epsilon-\epsilon)R_iR_j(u_iV_j)\,dx\\
 &-P_\epsilon-\int p\,n_\epsilon\cdot\nabla p\,dx.            \tag{10}
 \end{split}
\]
Here the occurrence of \(-P_\epsilon\) is exact, since
\[
 n_\epsilon\cdot N
 ={u\over r_\epsilon}\cdot(u\cdot\nabla u)
 =u\cdot\nabla r_\epsilon.                                    \tag{11}
\]
Adding (7) and (10) proves
\[
 \boxed{\begin{split}
 {d\over dt}(F_\epsilon+B_\epsilon)+\nu D_\epsilon={}&
 2\nu\int(r_\epsilon-\epsilon)R_iR_j(u_i\Delta u_j)\,dx\\
 &+\nu\int p\,n_\epsilon\cdot\Delta u\,dx\\
 &+2\int(r_\epsilon-\epsilon)R_iR_j(u_iV_j)\,dx
 -\int p\,n_\epsilon\cdot\nabla p\,dx.
                                                               \tag{12}
 \end{split}}\]
Thus the coefficient-one combination cancels the original pressure work for
every \(\epsilon>0\).  A coefficient \(c\) in front of \(B_\epsilon\)
would leave \((1-c)P_\epsilon\), so this cancellation fixes the coefficient.
It also creates the last two nonlinear terms in (12), whose sum has no sign
established here.

## Justification and removal of the regularization

All differentiations and integrations by parts above are valid under (1).
For example, Sobolev multiplication gives \(p\in C H^m\),
\(p_t\in C H^{m-2}\), and \(V\in C H^{m-1}\).  The four terms on the
right of (12) are absolutely integrable, uniformly on \([0,T]\), by the
representative bounds
\[
 \begin{split}
 \|(r_\epsilon-\epsilon)\|_2
   \|R_iR_j(u_i\Delta u_j)\|_2
 &\le \|u\|_2\,C\|u\|_\infty\|\Delta u\|_2,\\
 \|p\|_2\|\Delta u\|_2,
 \qquad
 \|u\|_2\,C\|u\|_\infty\|V\|_2,
 \qquad
 \|p\|_2\|\nabla p\|_2.                                    \tag{13}
 \end{split}
\]
These estimates also justify (8)--(10) by standard Sobolev approximation;
they require no preservation of Schwartz decay.

Let
\[
 r=|u|,\qquad n={u\over|u|}\mathbf1_{\{|u|>0\}},\qquad
 F={1\over3}\int|u|^3\,dx,\qquad B=\int p|u|\,dx.               \tag{14}
\]
The maps \(r_\epsilon-\epsilon\to r\) converge in \(L^2\), uniformly for
\(t\in[0,T]\).  One way to see the uniformity is that the scalar maps are
uniformly Lipschitz on \(L^2\), converge for each fixed input by dominated
convergence, and \(u([0,T])\) is compact in \(L^2\).  Also
\(n_\epsilon\to n\) pointwise, with \(|n_\epsilon|\le1\).  Hence (13) and
dominated convergence pass the time-integrated form of (12) to
\(\epsilon\downarrow0\), uniformly in the terminal time \(t\in[0,T]\).
The standard norm chain rule gives \(\nabla r=n\cdot\nabla u\) off the zero
set and \(\nabla u=0\) almost everywhere on that set.  Therefore
\[
 D_\epsilon\longrightarrow
 D_3:=\int\bigl(r|\nabla u|^2+r|\nabla r|^2\bigr)\,dx,           \tag{15}
\]
while
\[
 0\le F_\epsilon-F\le C\epsilon\|u\|_2^2,\qquad
 B_\epsilon\longrightarrow B.                                 \tag{16}
\]
It follows that, for every \(t\in[0,T]\),
\[
 \begin{split}
 &(F+B)(t)+\nu\int_0^tD_3(s)\,ds\\
 &=(F+B)(0)+\int_0^t\!\Bigg[
 2\nu\int rR_iR_j(u_i\Delta u_j)\,dx
 +\nu\int p\,n\cdot\Delta u\,dx\\
 &\hspace{44mm}
 +2\int rR_iR_j(u_iV_j)\,dx
 -\int p\,n\cdot\nabla p\,dx\Bigg]ds.                         \tag{17}
 \end{split}
\]
The nonlinear contribution from the pressure--speed correction in the
integrated identity, with \(V=-\mathbb P(u\cdot\nabla u)\), is
\[
 \mathcal N_B(u;V)
 =-P_3+2\int rR_iR_j(u_iV_j)\,dx
       -\int p\,n\cdot\nabla p\,dx,                            \tag{18}
\]
where \(P_3=\int p\,u\cdot\nabla r\,dx\). This is the contribution
extracted from (17), not an assertion of a two-sided derivative of B at an
arbitrary snapshot. At zeros of u, such a derivative can acquire distinct
one-sided terms involving p|V|. The integrated identity avoids that claim;
see `hf10-review-pressure-speed-evolution.md` for the exact scope repair.

## What the cancellation does not provide

Both \(F\) and \(B\) are invariant under the Navier--Stokes spatial scaling.
Calderon--Zygmund boundedness gives only
\[
 |B(u)|\le \|p\|_{3/2}\|u\|_3\le C\|u\|_3^3.                  \tag{19}
\]
The constant in (19) is not shown to be smaller than the coefficient
\(1/3\) in \(F\).  Thus (19) does not make \(F+B\) coercive, and (12) or
(17) gives no critical bound unless the new nonlinear residual and the two
viscous correction terms receive an additional one-sided estimate.

## Frontier record

**MODE / RESULT:** DISCOVER.  The critical correction \(B=\int p|u|\)
produces an exact coefficient-one cancellation of \(P_3\), including at the
regularized level, but replaces it by the explicit residual in (17).

**FIRST GAP:** prove a useful one-sided estimate for the complete right-hand
side of (17), or establish an exact obstruction to such an estimate.  No
sign of its nonlinear part is inferred in this note.

**SURVIVING CONDITIONAL SUFFIX:** if the complete right-hand side of (17) is
bounded above by a strict fraction of \(\nu D_3\) plus an input-only
time-integrable remainder, and if \(F+B\) is separately given a coercive
lower bound, the identity can feed a critical continuation estimate.

**NON-CLAIMS:** no coercivity, pressure absorption estimate, endpoint-uniform
producer, HF estimate, or global regularity conclusion is asserted.
