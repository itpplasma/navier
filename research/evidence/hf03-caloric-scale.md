# HF03 repair: caloric spreading makes the incoming cubic mass small

Status: correction and mechanism test for a local pointwise Type-I regime.
This note retracts the universal “coefficient one prevents gain” conclusion
of the earlier cutoff test.  A backward caloric cutoff has a spatial spreading
factor that can make its incoming weighted cubic mass small.  The remaining
loss is computed explicitly: transport and pressure-boundary leakage are
critical and concentrate near the final parabolic time \(s=-t\sim r^2\).
No Type-I regularity or global high-pressure theorem is claimed.

## 1. Assumptions and the caloric cutoff

Normalize the candidate point to \((0,0)\).  Assume first, for a transparent
global calculation, the stronger pointwise Type-I envelope

\[
 |u(x,-s)|\leq {C_*\over\sqrt{|x|^2+s}},
 \qquad 0<s<R^2.                                      \tag{PTI}
\]

This is stronger than finite normalized enstrophy and is not derived from it.
The localization needed when (PTI) is known only in a finite cylinder is
handled in Section 6.

Let \(0\leq\chi\leq1\) be smooth, supported in \(B_2\), and equal to one on
\(B_1\).  Put \(\chi_r(x)=\chi(x/r)\) and

\[
 \eta_r(x,t)=e^{\nu(-t)\Delta}\chi_r(x),
 \qquad -R^2\leq t\leq0.                              \tag{1}
\]

Then

\[
 \partial_t\eta_r+\nu\Delta\eta_r=0,qquad
 \eta_r(x,0)=\chi_r(x).                               \tag{2}
\]

Writing \(s=-t\) and

\[
 \ell(s)=(r^2+\nu s)^{1/2},qquad
 A(s)=\left({r\over\ell(s)}\right)^3,                 \tag{3}
\]

the heat kernel gives, with constants depending only on \(\chi\) and \(\nu\),

\[
 0\leq\eta_r(x,-s)
 \leq C A(s)e^{-c|x|^2/\ell(s)^2},                    \tag{4}
\]

\[
 |\nabla\eta_r(x,-s)|
 \leq C{A(s)\over\ell(s)}e^{-c|x|^2/\ell(s)^2}.       \tag{5}
\]

For \(s\lesssim r^2\), one may replace the right side of (4) by the sharper
bound \(1\); estimates (4)--(5), with adjusted constants, suffice below.

## 2. Exact localized identity

For \(w=|u|u\) and

\[
 D_3=|u||\nabla u|^2+|u||\nabla|u||^2,
\]

the time-dependent localized cubic identity is

\[
\begin{aligned}
 {1\over3}{d\over dt}\int\eta_r|u|^3
 +\nu\int\eta_rD_3
 &=\int p\,\operatorname{div}(\eta_rw)
   +{1\over3}\int|u|^3u\cdot\nabla\eta_r\\
 &\quad+{1\over3}\int|u|^3
              (\partial_t\eta_r+\nu\Delta\eta_r).    \tag{6}
\end{aligned}
\]

The last term vanishes by (2).  Integrating from \(-R^2\) to \(-\delta\)
therefore gives

\[
\begin{aligned}
 {1\over3}\int\eta_r(-\delta)|u(-\delta)|^3
 +\nu\int_{-R^2}^{-\delta}\int\eta_rD_3
 &={1\over3}\int\eta_r(-R^2)|u(-R^2)|^3\\
 &\quad+\int_{-R^2}^{-\delta}\int
       p\operatorname{div}(\eta_rw)\\
 &\quad+{1\over3}\int_{-R^2}^{-\delta}\int
       |u|^3u\cdot\nabla\eta_r.                      \tag{7}
\end{aligned}
\]

The pressure pairing remains gauge invariant.  At a possibly singular final
time, (7) is used first with \(\delta>0\) and then with the appropriate weak
liminf; no classical trace at zero is assumed.

## 3. The corrected incoming-face estimate

At \(t=-R^2\), (4) and (PTI) give

\[
\begin{aligned}
 \int\eta_r(x,-R^2)|u(x,-R^2)|^3dx
 &\leq C C_*^3\left({r\over R}\right)^3
 \int_{\mathbb R^3}{e^{-c|x|^2/R^2}\over
                         (|x|^2+R^2)^{3/2}}dx\\
 &\leq C C_*^3\left({r\over R}\right)^3.             \tag{8}
\end{aligned}
\]

The last integral is dimensionless after \(x=Ry\).  Thus the incoming cubic
mass really tends to zero as \(r/R\to0\).  The fact that it appears in (7)
with algebraic coefficient one does not prevent this spatial heat-kernel
gain.  This corrects the earlier no-go statement.

## 4. Exact transport-boundary scaling

The transport leakage in (7) is bounded by

\[
 \mathcal T_{r,R}
 \leq {1\over3}\int_0^{R^2}\int
       |u(x,-s)|^4|\nabla\eta_r(x,-s)|\,dx\,ds.        \tag{9}
\]

For fixed \(\nu>0\), \(\ell(s)^2\) is comparable to \(r^2+s\).  The radial
integral satisfies

\[
 \int_{\mathbb R^3}{e^{-c|x|^2/\ell(s)^2}\over(|x|^2+s)^2}dx
 \leq C_\nu s^{-1/2}.                                 \tag{10}
\]

Using (PTI), (5), and (10),

\[
 \mathcal T_{r,R}
 \leq C_\nu C_*^4
 \int_0^{R^2}{A(s)\over\ell(s)}s^{-1/2}ds.            \tag{11}
\]

Split at \(s=r^2\).  On \((0,r^2)\),
\(A(s)/\ell(s)\leq C_\nu/r\), while on \((r^2,R^2)\),
\(A(s)/\ell(s)\leq C_\nu r^3s^{-2}\).  Hence

\[
\begin{aligned}
 \mathcal T_{r,R}
 &\leq C_\nu C_*^4\left[
 {1\over r}\int_0^{r^2}s^{-1/2}ds
 +r^3\int_{r^2}^{R^2}s^{-5/2}ds\right]\\
 &\leq C_\nu C_*^4.                                  \tag{12}
\end{aligned}
\]

Both integrals approach nonzero constants as \(R/r\to\infty\).  More
precisely, the first equals \(2\), and the second equals
\(\frac23(1-(r/R)^3)\).  The incoming face gains \((r/R)^3\), but the
transport boundary does not.  Its loss comes from \(s\lesssim r^2\) and the
adjacent parabolic times \(s\gtrsim r^2\), where the cutoff has not spread far
enough to lower its gradient.

This is an upper-bound obstruction, not a constructed lower bound: cancellation
inside the signed transport integral remains possible.  Absolute Type-I
estimates alone provide no small factor.

## 5. Pressure boundary and active pressure work

Split the pressure contribution exactly as

\[
 \int p\operatorname{div}(\eta_rw)
 =\int\eta_r p,u\cdot\nabla|u|
  +\int p|u|u\cdot\nabla\eta_r.                       \tag{13}
\]

The two terms must remain paired when changing the pressure gauge.  The first
is the active signed local pressure work; caloric spreading supplies no sign
or absorption for it.

For the boundary term, a transparent scale computation results if one assumes
the pressure envelope

\[
 |p(x,-s)-c(-s)|\leq {P_*\over |x|^2+s}.               \tag{PPI}
\]

This is an additional diagnostic hypothesis, not a consequence of (PTI)
asserted here.  Equations (5), (10), (PTI), and (PPI) give

\[
\begin{aligned}
 \mathcal P^{\rm bd}_{r,R}
 &:=\left|\int_0^{R^2}\int
 (p-c)|u|u\cdot\nabla\eta_r\right|\\
 &\leq C_\nu P_*C_*^2
 \int_0^{R^2}{A(s)\over\ell(s)}s^{-1/2}ds\\
 &\leq C_\nu P_*C_*^2.                               \tag{14}
\end{aligned}
\]

It has exactly the same near-final order-one loss as transport.  A formulation
using scale-invariant annular \(L^{3/2}\) pressure bounds gives the same
conclusion after a dyadic shell sum: bounded leakage depending on the pressure
constant, without a factor tending to zero in \(r/R\).  That annular bound
must be proved from local pressure decomposition and outer data; harmonicity
alone does not supply the cubic-flux estimate.

Therefore even a hypothetical strict signed estimate for the first term of
(13) leaves the order-one absolute errors (12) and (14).  The caloric cutoff
repairs the incoming face, but moves the first unresolved boundary issue to
the near-final parabolic layer.

## 6. Finite spatial domain and heat-kernel tails

The global use of (PTI) in (8)--(14) must not be imported silently into a
local Type-I problem.  Suppose instead that (PTI) is known only on
\(B_{4R}\times(-R^2,0)\).  Choose a fixed cutoff \(\zeta_R\), equal to one on
\(B_{2R}\) and supported in \(B_{3R}\), and use

\[
 \widetilde\eta_r=\zeta_R\eta_r.                      \tag{15}
\]

Then

\[
 (\partial_t+\nu\Delta)\widetilde\eta_r
 =\nu(2\nabla\zeta_R\cdot\nabla\eta_r
              +\eta_r\Delta\zeta_R),                 \tag{16}
\]

supported in \(B_{3R}\setminus B_{2R}\).  For
\(0<s<R^2\), (4)--(5) on that annulus give

\[
 |(\partial_t+\nu\Delta)\widetilde\eta_r|
 \leq C_\nu {r^3\over R^5}.                          \tag{17}
\]

The resulting error is bounded by

\[
 C_\nu {r^3\over R^5}
 \int_{-R^2}^0\int_{B_{3R}\setminus B_{2R}}|u|^3.     \tag{18}
\]

Under local (PTI), the spacetime integral is \(O(C_*^3R^2)\), so (18) is
\(O(C_*^3(r/R)^3)\).  The incoming estimate (8), restricted to \(B_{3R}\),
has the same gain.  Thus a local truncation is compatible with the repair.

If no pointwise control is assumed on the outer annulus, (18) remains
conditional on its finite scaled \(L^3\) norm.  Similarly, pressure terms
outside the local cylinder require a fixed outer \(L^{3/2}\) pressure bound.
These are explicit outer-data hypotheses, not consequences of the inner
Type-I statement.

## 7. Result and next exact gap

**Corrected result.**  Backward caloric spreading changes the incoming cubic
mass from critical order one to

\[
 O\!\left(C_*^3(r/R)^3\right).
\]

The prior universal coefficient-one no-go is therefore false and is retracted
for this mechanism.

**Exact surviving loss.**  Absolute estimates for transport leakage and,
under an explicit pressure hypothesis, pressure-boundary leakage satisfy

\[
 |\mathcal T_{r,R}|\lesssim C_\nu C_*^4,qquad
 |\mathcal P^{\rm bd}_{r,R}|lesssim C_\nu P_*C_*^2,   \tag{19}
\]

with no decay as \(r/R\to0\).  The integral calculation locates this loss at
\(s\lesssim r^2\), not at the incoming face.  The active signed pressure work
also remains unestimated.

**Next repair target.**  A viable continuation of the caloric route must find
a signed cancellation or a hybrid cutoff that reduces the near-final
transport and pressure boundary layer while retaining the incoming
\((r/R)^3\) gain.  Treating (19) as small for arbitrary \(C_*\), or assuming a
global pressure envelope, would be circular.

**Scope.**  This note concerns the stronger pointwise Type-I test only.  It
does not establish the analogous estimates from finite normalized enstrophy,
does not prove a CKN contraction, and does not prove the global high-pressure
hypothesis or any Clay alternative.
