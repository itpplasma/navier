# HF06: R3 short-time creation of speed gradients

Status: rigorous regime diagnostic, 2026-09-05. This constructs smooth
compactly supported divergence-free data whose initial speed-gradient ratio
is arbitrarily small, while the ratio becomes order one on the data's own
parabolic time scale. It does not produce blow-up or refute the signed HF
estimate.

## 1. Periodic shear with heat-generated speed variation

Fix \(0<\varepsilon<1/4\), and put
\[
 \vartheta(z)=z+\varepsilon\sin 2z,\qquad
 v(z)=(\cos\vartheta(z),\sin\vartheta(z),0).           \tag{1}
\]
Then \(v(z+\pi)=-v(z)\), so both horizontal components have zero mean over
\([0,2\pi]\), and \(|v|=1\). Also
\[
 |v'(z)|^2=\vartheta'(z)^2,\qquad
 \partial_z(\vartheta'(z)^2)\not\equiv0.              \tag{2}
\]

Let
\[
 w_s=e^{s\partial_z^2}v.
\]
Taylor expansion in every periodic \(C^m\) norm gives
\[
 w_s=v+sv''+O(s^2).
\]
Since \(v\cdot v''=-|v'|^2\),
\[
 |w_s|=1-s\vartheta'^2+O(s^2),\qquad
 \partial_z|w_s|=-s\partial_z(\vartheta'^2)+O(s^2).
                                                               \tag{3}
\]
Choose one sufficiently small \(s_0>0\). Then \(w_{s_0}\) is bounded away
from zero and
\[
 \left\langle|\partial_z|w_{s_0}||^2\right\rangle>0.  \tag{4}
\]
The denominator
\(\langle|w_{s_0}'|^2\rangle\) is also positive.

This effect is purely diffusive. The periodic field \(v(z)\) has zero
transport nonlinearity because it has no vertical component and depends
only on \(z\).

## 2. Compact solenoidal embedding

The zero means allow periodic primitives \(A_1,A_2\) satisfying
\[
 A_1'=\sin\vartheta,\qquad A_2'=-\cos\vartheta.
\]
Thus
\[
 \nabla\times(A_1(z),A_2(z),0)=v(z).
\]
Choose a nonnegative nonzero envelope
\(a\in C_c^\infty(\mathbb R^3)\), and define
\[
 u_{0,k}=\nabla\times\left({a(x)\over k}
                 (A_1(kz),A_2(kz),0)\right).          \tag{5}
\]
Then \(u_{0,k}\in C_c^\infty\), \(\nabla\cdot u_{0,k}=0\), and
\[
u_{0,k}=a(x)v(kz)+k^{-1}r_k(x),                      \tag{6}
\]
where \(r_k\) is uniformly bounded in \(L^2\cap L^\infty\), while its one
fast derivative is \(O(k)\). Consequently, the combination \(k^{-1}r_k\)
satisfies the more useful bounds
\[
 \|u_{0,k}-av(kz)\|_2=O(k^{-1}),\qquad
 \|\nabla(u_{0,k}-av(kz))\|_2=O(1).                  \tag{7}
\]

The leading fast derivative of \(av(kz)\) is \(akv'(kz)e_z\), which is
pointwise orthogonal to \(av(kz)\). Hence it changes direction but not
speed. We use the following comparison lemma. If \(a\ge0\) is smooth and
compactly supported, \(q\) is periodic with \(\inf|q|>0\), and
\(V(x)=a(x)q(kz)\), then every \(e\in H^1\) satisfies
\[
\|\nabla|V+e|-\nabla|V|\|_2
\le \|\nabla e\|_2+Ck\|e\|_2+C\|\nabla a\|_2.         \tag{8}
\]
Indeed, writing \(\widehat f=f/|f|\) away from its zero set (and using the
standard almost-everywhere formula for \(\nabla|f|\)), the difference is
bounded by \(|\nabla e|+|\widehat{V+e}-\widehat V|\,|\nabla V|\). The unit
directions differ by at most
\(C\min(1,|e|/(a|q|))\). Its product with the fast part \(akq'(kz)\) is at
most \(Ck|e|\), including where \(a=0\) by continuity. Its product with the
slow part \((\nabla a)q(kz)\) is at most \(C|\nabla a|\). This proves (8)
without dividing by the envelope. For the unit vector \(q=v\),
\(\nabla|V|=\nabla a\).

Applying (8) to (7) gives
\[
 \|\nabla|u_{0,k}|\|_2=O(1).                          \tag{9}
\]
Periodic averaging gives
\[
 k^{-2}\|\nabla u_{0,k}\|_2^2
\longrightarrow
\left(\int_{\mathbb R^3}a^2dx\right)
\left\langle|v'|^2\right\rangle>0.                   \tag{10}
\]
Therefore
\[
 \delta_k(0):=
 {\|\nabla|u_{0,k}|\|_2\over\|\nabla u_{0,k}\|_2}
\longrightarrow0.                                    \tag{11}
\]
The \(L^\infty\), \(L^2\), and \(L^3\) norms of the data are bounded
uniformly in \(k\).

## 3. Uniform short-time nonlinear control

Let \(u_k\) be the true unforced Navier--Stokes solution with viscosity
\(\nu>0\) and datum \(u_{0,k}\). The mild formula is
\[
 u_k(t)=e^{\nu t\Delta}u_{0,k}
-\int_0^t e^{\nu(t-s)\Delta}\mathbb P
             \operatorname{div}(u_k\otimes u_k)(s)\,ds.          \tag{12}
\]
The heat--Leray kernel estimate
\[
 \|e^{\nu t\Delta}\mathbb P\operatorname{div}\|_{L^1\to L^1
 \ {\rm kernel}}\le C(\nu t)^{-1/2}
\]
and the uniform initial \(L^\infty\) bound give a common mild
\(L^\infty\) lifespan \(T_0>0\), independent of \(k\), with
\[
 \sup_{0<t<T_0}\|u_k(t)\|_\infty\le C.                \tag{13}
\]
Energy also gives \(\sup_t\|u_k(t)\|_2\le C\).

Put \(U_k(t)=e^{\nu t\Delta}u_{0,k}\) and \(e_k=u_k-U_k\). From (12),
\[
 \|e_k(t)\|_2
\le C\int_0^t(\nu(t-s))^{-1/2}
          \|u_k(s)\otimes u_k(s)\|_2ds
\le C\sqrt t.                                         \tag{14}
\]
The \(H^1\) energy estimate gives
\[
 \sup_{0<t\le c k^{-2}}\|\nabla u_k(t)\|_2\le Ck.     \tag{15}
\]
In fact, on the common interval from (13), integration by parts and Young's
inequality give
\[
 {1\over2}{d\over dt}\|\nabla u_k\|_2^2
 +{\nu\over2}\|\Delta u_k\|_2^2
 \le {C\over\nu}\|u_k\|_\infty^2\|\nabla u_k\|_2^2.
\]
Since \(\|\nabla u_{0,k}\|_2=O(k)\), Gronwall proves (15), indeed on every
fixed subinterval of the common lifespan.
Commuting one derivative onto \(u_k\otimes u_k\), while retaining one
heat-kernel derivative, yields
\[
\begin{aligned}
 \|\nabla e_k(t)\|_2
 &\le C\int_0^t(\nu(t-s))^{-1/2}
       \|\nabla(u_k\otimes u_k)(s)\|_2ds\\
 &\le Ck\sqrt t.                                      \tag{16}
\end{aligned}
\]
Here
\(\|\nabla(u_k\otimes u_k)\|_2
\le2\|u_k\|_\infty\|\nabla u_k\|_2\).

At
\[
 t_k={s_0\over\nu k^2},                               \tag{17}
\]
equations (14)--(16) give
\[
 \|e_k(t_k)\|_2=O(k^{-1}),\qquad
 \|\nabla e_k(t_k)\|_2=O(1).                          \tag{18}
\]
All constants may depend on the fixed
\((a,v,s_0,\nu)\), but not on \(k\).

## 4. Heat localization and the limiting ratio

Heat evolution of the slowly modulated oscillation in (6), with
\(\nu k^2t_k=s_0\), gives
\[
 U_k(t_k)=a(x)w_{s_0}(kz)+\rho_k,\qquad
 \|\rho_k\|_2=O(k^{-1}),\quad
 \|\nabla\rho_k\|_2=O(1).                             \tag{19}
\]
This follows either from the Fourier representation or from the commutator
between the heat semigroup and multiplication by \(a\); each derivative
falling on the slow envelope gains one factor \(k^{-1}\) on the time scale
\(k^{-2}\). More explicitly, for every nonzero Fourier mode \(n\),
\[
 e^{\nu t_k\Delta}\bigl(a(x)e^{inkz}\bigr)
 =e^{inkz}e^{(s_0/k^2)\Delta+(2ins_0/k)\partial_z-s_0n^2}a.
\]
Taylor's formula in \(L^2\) and \(H^1\), followed by summation using the
rapid decay of the smooth periodic Fourier coefficients of \(v,A_1,A_2\),
proves (19). The \(k^{-1}r_k\) term in (6) contributes \(O(k^{-1})\) in
\(L^2\) and \(O(1)\) after one derivative.

Because \(w_{s_0}\) is bounded away from zero, the speed-gradient comparison
behind (8), now with \(q=w_{s_0}/|w_{s_0}|\), combines (18)--(19) to give
\[
\begin{aligned}
 k^{-1}\|\nabla u_k(t_k)\|_2
 &\longrightarrow
 \left[
 \left(\int a^2\right)\langle|w_{s_0}'|^2\rangle
 \right]^{1/2},\\
 k^{-1}\|\nabla|u_k(t_k)|\|_2
 &\longrightarrow
 \left[
 \left(\int a^2\right)
 \langle|\partial_z|w_{s_0}||^2\rangle
 \right]^{1/2}.                                      \tag{20}
\end{aligned}
\]
For the nonlinear error, the potentially dangerous fast derivative is
bounded by \(k\|e_k(t_k)\|_2=O(1)\), and the remaining contribution by
\(\|\nabla e_k(t_k)\|_2=O(1)\). Slow envelope derivatives are also \(O(1)\),
including near zeros of \(a\). Thus they vanish after division by \(k\).

It follows from (4) and (20) that
\[
 \delta_k(t_k)\longrightarrow
\left(
 {\langle|\partial_z|w_{s_0}||^2\rangle
  \over\langle|w_{s_0}'|^2\rangle}
\right)^{1/2}>0.                                     \tag{21}
\]

## Exact conclusion

The ratio
\(\|\nabla|u|\|_2/\|\nabla u\|_2\) can start arbitrarily small for uniformly
bounded compactly supported smooth R3 data and become order one after time
\(O(k^{-2})\), while every solution remains regular on a common much longer
time interval. Thus small speed-gradient ratio is not automatically
propagated on the active parabolic scale by incompressibility, viscosity, or
energy.

This is a direct test of the proposed short-heat-defect mechanism: diffusion
itself converts directional oscillation into magnitude oscillation when the
angular speed \(\vartheta'\) is nonconstant. Any propagation theorem must
control this transfer, impose extra geometry, or allow a defect of order one
on the parabolic scale.

## Frontier record

**MODE / RESULT:** FALSIFY. Automatic propagation of a small
speed-gradient ratio fails on the natural high-frequency time scale.

**FIRST GAP:** none for the short-time diagnostic. A useful replacement would
need a dynamically stable quantity that includes the heat-generated term
\(\partial_z(\vartheta'^2)\), rather than \(\nabla|u|\) alone.

**NON-CLAIMS:** the construction is regular, has uniformly bounded initial
\(L^3\), and says nothing about finite-time blow-up or failure of the signed
HF hypothesis. It does not turn a local regime test into global control.
