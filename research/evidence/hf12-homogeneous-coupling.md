# HF12: homogeneous pressure--speed cusp coupling

Status: analytic mechanism test, 2026-09-05.

This note tests a homogeneous replacement for the fixed-scale smoothing of
the pressure--speed term.  It derives the exact scalar derivatives and the
Euler cancellation defect away from the cusps.  It proves no closed
Navier--Stokes estimate or heat monotonicity.

## Definition and static control

Put
\[
 r=|u|,\qquad q=p_-=(-p)_+,
\]
and, for \(k>0\), define
\[
 \rho_k(r,p)=\sqrt{r^2+kq}-\sqrt{kq},\qquad
 g_k(r,p)=p\rho_k(r,p),                                       \tag{1}
\]
\[
 \mathcal J_k(u)=\int_{\mathbb R^3}
 \left({r^3\over3}+g_k(r,p)+q^{3/2}\right)dx,\qquad
 p=R_iR_j(u_i u_j).                                           \tag{2}
\]
Under positive amplitude scaling, \(r\mapsto ar\), \(p,q\mapsto a^2p,a^2q\),
so every term in (2) is cubic.  Also \(0\le\rho_k\le r\).  On \(p\ge0\),
\(g_k=pr\ge0\).  On \(p<0\), \(g_k=-q\rho_k\ge-qr\).  The same pointwise
Young inequality as for the uncoupled pressure entropy therefore gives
\[
 {r^3\over3}+g_k(r,p)+q^{3/2}
 \ge {r^3\over6}+\left(1-{2\sqrt2\over3}\right)q^{3/2}.      \tag{3}
\]
Consequently
\[
 \mathcal J_k(u)\ge {1\over6}\|u\|_3^3,                       \tag{4}
\]
and the usual double-Riesz \(L^{3/2}\) bound also gives
\(\mathcal J_k(u)\le C\|u\|_3^3\), with \(C\) independent of \(k\).

## Exact scalar derivatives

For \(r>0\) and \(p\ne0\), set
\[
 s=\sqrt{r^2+kq},\qquad h=\sqrt{kq}.
\]
If \(p>0\), then
\[
 g_k=pr,\qquad \partial_rg_k=p,\qquad \partial_pg_k=r.          \tag{5}
\]
If \(p<0\), then
\[
 g_k=-q(s-h),
\]
and direct differentiation gives
\[
 \boxed{\quad
 \partial_rg_k={pr\over s},\qquad
 \partial_pg_k=(s-h){2s-h\over2s}.
 \quad}                                                       \tag{6}
\]
Indeed, \(\partial_q(s-h)=k/(2s)-h/(2q)\), and
\(\partial_pg_k=(s-h)+q\partial_q(s-h)\), which factors as in (6).
In the small-speed region \(r\ll h\),
\[
 g_k(r,p)=-{\sqrt q\over2\sqrt k}r^2
          +O\left({r^4\over k^{3/2}\sqrt q}\right).           \tag{7}
\]
Thus the cusp is quadratic in velocity at fixed negative pressure, rather
than a multiple of \(|u|\).

Let
\[
 a_k(r,p)=\partial_pg_k(r,p)-{3\over2}\sqrt q\,
                   \mathbf1_{\{p<0\}},                        \tag{8}
\]
so explicitly
\[
 a_k(r,p)=
 \begin{cases}
 r,&p>0,\\
 (s-h)(2s-h)/(2s)-(3/2)\sqrt q,&p<0.
 \end{cases}                                                   \tag{9}
\]
The second term in (8) is the derivative of \(q^{3/2}\) with respect to
\(p\).

## Euler contribution and cancellation defect

Let
\[
 N=(u\cdot\nabla)u,\qquad V=-\mathbb P N=-N-\nabla p,\qquad
 p_V=2R_iR_j(u_iV_j).                                         \tag{10}
\]
At points where \(r>0\) and \(p\ne0\), the formal first variation of (2)
in the Euler direction is
\[
 \int r u\cdot V
 +\int {\partial_rg_k\over r}u\cdot V
 +\int a_k p_V.                                               \tag{11}
\]
The transport part of the first integral vanishes after spatial integration,
and its pressure part is
\[
 P_3=\int p\,u\cdot\nabla r.                                  \tag{12}
\]
For the second integral define
\[
 \beta_k(r,p)={\partial_rg_k\over r}
 =\begin{cases}p/r,&p>0,\\p/s,&p<0.
 \end{cases}                                                   \tag{13}
\]
Using \(u\cdot N=r\,u\cdot\nabla r\), the part on \(p>0\) cancels the
corresponding part of \(P_3\) exactly.  On \(p<0\) it cancels only the
fraction \(r/s\).  Hence the complete Euler contribution is
\[
 \boxed{\begin{aligned}
 \mathcal E_k(u)={}&
 \int_{\{p<0\}}p\left(1-{r\over s}\right)
                       u\cdot\nabla r\,dx\\
 &-\int \beta_k(r,p)u\cdot\nabla p\,dx
 +2\int a_k(r,p)R_iR_j(u_iV_j)\,dx.
 \end{aligned}}                                               \tag{14}
\]
This is an algebraic identity wherever the scalar derivatives exist.  A
rigorous integrated evolution for arbitrary smooth fields requires smoothing
near \(r=0\) and \(p=0\), followed by explicit domination.  In particular,
on \(p>0\) the term \(pr\) retains the speed cusp at \(u=0\); (7) removes
that cusp only where \(p<0\).  Formula (14) is therefore not asserted as an
unregularized Frechet derivative on fields with velocity zero sets.

## Size and location of the defect

The first term of (14) is the precise loss of the original pressure-work
cancellation.  With \(x=r/\sqrt{kq}\) on \(p<0\), its pointwise absolute
value is bounded by
\[
 \begin{aligned}
 q\left(1-{r\over s}\right)r|\nabla r|
 &=\sqrt k\,q^{3/2}
 x\left(1-{x\over\sqrt{1+x^2}}\right)|\nabla r|\\
 &\le C_0\sqrt k\,q^{3/2}|\nabla r|,                          \tag{15}
 \end{aligned}
\]
where, writing \(y=(\sqrt5-1)/2\),
\(C_0=y^2/\sqrt{1+y}\) is the supremum of the displayed scalar function.
Thus the defect has an absolute \(O(\sqrt k)\), rather than \(O(k)\),
bound by a simpler homogeneous integral.  The order \(\sqrt k\) is sharp
at the scalar level: take \(r=x\sqrt{kq}\) with fixed \(x>0\).

Smallness in (15) does not mean uniform relative cancellation.  On the cusp
region
\[
 r^2\le kq,
\]
one has \(r/s\le1/\sqrt2\), and therefore
\[
 1-r/s\ge1-1/\sqrt2.                                         \tag{16}
\]
A fixed positive fraction of the local pressure work is left uncancelled
there.  Moreover the other two terms of (14) are not multiplied by a small
power of \(k\).  In particular \(a_k\to r-(3/2)\sqrt q\) on \(p<0\) for
fixed \(r>0\) as \(k\downarrow0\), while \(a_k=r\) on \(p>0\).
Therefore (15) alone supplies no closure, even if the integral on its
right-hand side were otherwise controlled.

## Small-parameter heat obstruction

The controller's extension, checked in
`hf12-review-homogeneous-coupling.md`, compares this functional with the
original \(\mathcal K\). On \(p<0\),
\[
 0\le g_k(r,p)-pr
 =q\bigl(r-\sqrt{r^2+kq}+\sqrt{kq}\bigr)
 \le\sqrt{k}\,q^{3/2}.
\]
On \(p\ge0\), the difference vanishes. Consequently
\[
 0\le\mathcal J_k(u)-\mathcal K(u)\le\sqrt{k}E_p(u),
 \qquad E_p(u)=\int p[u]_-^{3/2}.
\]
Choose the fixed \(h,t\) in the reviewed HF11 heat counterexample and write
\(\Delta=\mathcal K(e^{t\Delta_x}h)-\mathcal K(h)>0\). Then
\[
 \mathcal J_k(e^{t\Delta_x}h)-\mathcal J_k(h)
 \ge\Delta-\sqrt{k}E_p(h)>0
\]
for all sufficiently small \(k>0\). This excludes universal heat monotonicity
in that parameter regime; it does not decide arbitrary or large \(k\).
The frozen scalar candidate and audit are preserved at `7afbff8`.

## Scope

The homogeneous coupling retains static cubic coercivity and softens the
velocity cusp in the negative-pressure region.  It does not establish a
favorable heat sign.  Replacing its remaining cusps by a fixed smoothing
scale would justify a classical differentiated identity, but would break the
exact homogeneity and would not by itself prove heat monotonicity.

## Frontier record

**MODE / RESULT:** DISCOVER/FALSIFY.  The exact Euler identity (14) exposes a
transport cancellation defect.  It is absolutely \(O(\sqrt k)\) in the form
(15), but loses a fixed fraction of cancellation in the region
\(r^2\lesssim k p_-\); the remaining Riesz residual is not \(k\)-small.

**FIRST GAP:** obtain a one-sided bound for all of (14), together with the
full heat contribution, using quantities already controlled by the input.

**SURVIVING CONDITIONAL SUFFIX:** the pointwise static coercivity (3) and the
exact away-from-cusps scalar identities survive independently of any
dynamical estimate.

**NON-CLAIMS:** no unregularized derivative across zero sets, heat
monotonicity, pressure absorption, HF estimate, or regularity theorem is
asserted.
