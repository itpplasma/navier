# HF10: the coefficient-one pressure--speed functional is not coercive

MODE / RESULT: **FALSIFY.**  There exists
\(u\in C_c^\infty(\mathbb R^3;\mathbb R^3)\) with
\(\nabla\cdot u=0\) such that, for the fixed Riesz-transform pressure
\(p(u)=R_iR_j(u_i u_j)\),
\[
 \mathcal C(u):={1\over3}\int_{\mathbb R^3}|u|^3
                 +\int_{\mathbb R^3}p(u)|u|<0.       \tag{1}
\]
Consequently this coefficient-one functional is neither nonnegative nor a
coercive lower control of \(\|u\|_3^3\) on smooth compactly supported
solenoidal fields.

CLAIM AND SCOPE: The construction is on \(\mathbb R^3\), uses the standard
Fourier convention in which \(R_iR_j\) has multiplier
\(-\xi_i\xi_j/|\xi|^2\), and produces one smooth compactly supported real
divergence-free field.  It concerns only the static functional (1).

EVIDENCE:

## 1. Exact two-dimensional negative model

In polar coordinates on \(\mathbb R^2\), let
\[
 v_0(r,\vartheta)=e_\vartheta\,\mathbf 1_{0<r<1}.
\]
This bounded compactly supported field is divergence-free distributionally:
its normal component vanishes at the unit circle, and the apparent point at
the origin has measure zero.  For an azimuthal field \(v=f(r)e_\vartheta\),
\((v\cdot\nabla)v=-f(r)^2e_r/r\).  Thus the pressure with gauge zero at
infinity is
\[
 p_f(r)=-\int_r^\infty {f(\rho)^2\over\rho}\,d\rho. \tag{2}
\]
For \(f=\mathbf1_{(0,1)}\), this is
\[
 p_0(r)=\begin{cases}\log r,&0<r<1,\\0,&r\ge1.
 \end{cases}                                         \tag{3}
\]
The pair \((v_0,p_0)\) satisfies the stationary Euler balance
\((v_0\cdot\nabla)v_0+\nabla p_0=0\) distributionally.  Taking divergence
shows that (3) is exactly the decaying two-dimensional Riesz pressure
\(R_\alpha^{(2)}R_\beta^{(2)}(v_{0,\alpha}v_{0,\beta})\); no additive gauge
constant remains.  Since \(p_0\in L^{3/2}(\mathbb R^2)\), all following
pairings are finite.  Direct integration gives
\[
 {1\over3}\int_{\mathbb R^2}|v_0|^3={\pi\over3},
 \qquad
 \int_{\mathbb R^2}p_0|v_0|
   =2\pi\int_0^1r\log r\,dr=-{\pi\over2},            \tag{4}
\]
and hence
\[
 \mathcal C_2(v_0):={1\over3}\int|v_0|^3+
                         \int p_0|v_0|=-{\pi\over6}. \tag{5}
\]

For comparison, the formal profile \(f(r)=r^q\mathbf1_{r<1}\), \(q>0\),
has
\[
 p_q(r)={r^{2q}-1\over2q}\quad(r<1),
 \qquad
 \mathcal C_2(v_q)=
 {2\pi(q-1)\over3(3q+2)(q+2)}.                      \tag{6}
\]
This confirms the negative sign for \(0<q<1\), but (6) is only a diagnostic:
such a profile need not be smooth at the origin or rim.

## 2. Smooth compactly supported planar swirl

Choose smooth radial amplitudes \(f_n\) satisfying
\[
 0\le f_n\le1,
 \quad f_n(r)=c_nr\ \hbox{ near }0,
 \quad f_n(r)=1\ \hbox{ on }[2/n,1-2/n],
 \quad f_n(r)=0\ \hbox{ for }r\ge1,
\]
with smooth transitions in the two omitted annuli.  They can be chosen so
that \(v_n=f_n(r)e_\vartheta\) lies in
\(C_c^\infty(\mathbb R^2;\mathbb R^2)\); the exact linear behavior near the
origin makes \(f_ne_\vartheta=c_n(-y,x)\) there.  The fields are solenoidal,
and dominated convergence gives
\[
 v_n\longrightarrow v_0\quad\hbox{strongly in }L^3(\mathbb R^2). \tag{7}
\]
Therefore \(v_n\otimes v_n\to v_0\otimes v_0\) in \(L^{3/2}\).  Boundedness
of the two-dimensional Riesz transforms on \(L^{3/2}\) gives
\[
 p(v_n)\longrightarrow p_0\quad\hbox{strongly in }L^{3/2}.       \tag{8}
\]
Using (7)--(8), Hölder's inequality, and
\(\big||v_n|-|v_0|\big|\le|v_n-v_0|\), both terms of \(\mathcal C_2\) are
continuous in this limit.  Hence
\[
 \mathcal C_2(v_n)\longrightarrow-\pi/6.             \tag{9}
\]
Fix one sufficiently large \(n\), and write its smooth compactly supported
swirl as \(v\); then \(\mathcal C_2(v)<0\).

## 3. Long compact three-dimensional lift

Fix a nonzero \(\eta\in C_c^\infty(\mathbb R)\) with \(\eta\ge0\), and for
\(L>0\) define
\[
 u_L(x_1,x_2,z)=\eta(z/L)(v_1(x_1,x_2),v_2(x_1,x_2),0).          \tag{10}
\]
Then \(u_L\in C_c^\infty(\mathbb R^3)\) and
\(\nabla\cdot u_L=\eta(z/L)\nabla_h\cdot v=0\).

Put \(\zeta=z/L\), and let \(T_L\) act on functions of
\((x_h,\zeta)\) by the Fourier multiplier
\[
 -{\xi_\alpha\xi_\beta\over
       |\xi_h|^2+L^{-2}\xi_\zeta^2},
 \qquad \alpha,\beta\in\{1,2\}.                    \tag{11}
\]
After the change of variables, the three-dimensional pressure satisfies
\[
 p(u_L)(x_h,L\zeta)
   =T_L\bigl(\eta(\zeta)^2v_\alpha v_\beta\bigr)(x_h,\zeta).   \tag{12}
\]
The operators \(T_L\) are anisotropic dilation conjugates of ordinary
three-dimensional double Riesz transforms.  Their \(L^r\) operator norms are
therefore bounded independently of \(L\), for every \(1<r<\infty\).

For the fixed smooth compactly supported input
\(g_{\alpha\beta}=\eta^2v_\alpha v_\beta\), the multipliers in (11) converge
almost everywhere to
\(-\xi_\alpha\xi_\beta/|\xi_h|^2\), with value zero assigned on the
measure-zero axis \(\xi_h=0\).  Dominated convergence in Fourier space gives
strong \(L^2\) convergence.  Uniform \(L^r\) bounds for some
\(1<r<3/2\), also valid for the slicewise two-dimensional limiting Riesz
operator, bound the difference in \(L^r\).  Interpolation yields
\[
 T_Lg_{\alpha\beta}\longrightarrow
 \eta(\zeta)^2R_\alpha^{(2)}R_\beta^{(2)}
       (v_\alpha v_\beta)
 \quad\hbox{strongly in }L^{3/2}(\mathbb R^2\times\mathbb R_\zeta). \tag{13}
\]

The cubic term scales exactly, while (13) and Hölder give the pressure-term
limit:
\[
 {\mathcal C(u_L)\over L}
 \longrightarrow
 \left(\int_{\mathbb R}\eta(\zeta)^3\,d\zeta\right)
 \left\{{1\over3}\int_{\mathbb R^2}|v|^3+
                  \int_{\mathbb R^2}p(v)|v|\right\}
 =\left(\int\eta^3\right)\mathcal C_2(v)<0.          \tag{14}
\]
Thus \(\mathcal C(u_L)<0\) for every sufficiently large finite \(L\), and
any one such \(u_L\) is the required smooth compactly supported solenoidal
counterexample.

## 4. Sharp coefficient threshold within radial swirls

There is also a sharp restricted-class bound explaining how much of the
pressure correction a nonnegative planar swirl can tolerate.  For
\(v=w(r)e_\vartheta\), \(w\ge0\), put
\[
 M=\int_{\mathbb R^2}|v|^3,
 \qquad B=\int_{\mathbb R^2}p(v)|v|,
 \qquad a(t)=e^{2t/3}w(e^t).
\]
Formula (2), followed by \(r=e^t\) and \(\rho=e^{t+h}\), gives exactly
\[
 M=2\pi\int_{\mathbb R}a(t)^3\,dt,
 \qquad
 -B=2\pi\int_0^\infty e^{-4h/3}
       \int_{\mathbb R}a(t)a(t+h)^2\,dt\,dh.         \tag{15}
\]
Hölder and translation invariance imply
\[
 \int a(t)a(t+h)^2dt
 \le \|a\|_3\|a(\cdot+h)^2\|_{3/2}
 =\int a^3,
\]
and therefore
\[
 -B\le {3\over4}M.                                  \tag{16}
\]
The constant is sharp: take nonnegative smooth \(a_T\) equal to one on a
logarithmic interval of length \(T\), with transition regions of fixed
length.  For every fixed \(h\), the correlation in (15), divided by
\(\int a_T^3\), tends to one as \(T\to\infty\); domination by Hölder and the
integrable kernel \(e^{-4h/3}\) then gives \((-B_T)/M_T\to3/4\).  Translating
the logarithmic support away from \(r=0\) makes
\(w_T(r)=r^{-2/3}a_T(\log r)\) a smooth compactly supported swirl amplitude,
so this sharpness occurs inside the admissible smooth class.

Consequently, for \(\kappa\ge0\), within nonnegative smooth compactly
supported planar swirls,
\[
 {1\over3}M+\kappa B
 \ge \left({1\over3}-{3\kappa\over4}\right)M.        \tag{17}
\]
For \(\kappa<0\), the valid lower bound is instead \(M/3\), since
\(B\le0\). Thus it has a uniform positive lower bound in terms of \(M\)
exactly when
\(\kappa<4/9\); at \(\kappa=4/9\) it is nonnegative but has no uniform
positive coercivity; and for \(\kappa>4/9\), the smooth log-plateau sequence
makes it negative.  Equivalently, the power diagnostic (6), extended to
\(q>-2/3\), has \(B/(M/3)=-3/(q+2)\to-9/4\) as
\(q\downarrow-2/3\); smooth core and rim cutoffs preserve this limit by the
same \(L^3\)-to-\(L^{3/2}\) pressure continuity used in (7)--(9).

This threshold is only a sharp statement for the declared two-dimensional
radial-swirl class.  It does not assert the optimal coefficient for arbitrary
two- or three-dimensional fields.  In particular, it supplements rather than
replaces the three-dimensional transfer in Section 3.

FIRST GAP: none for the static coefficient-one coercivity claim.

SURVIVING CONDITIONAL SUFFIX: Any modified-energy argument using exactly
\(\frac13\int|u|^3+\int p(u)|u|\) cannot obtain critical-norm control from a
universal nonnegative or positive-coercive lower bound on that functional.
This does not assess its Euler derivative identity or other possible boundary
functional estimates.

NON-CLAIMS: Negativity of (1) is not a Navier--Stokes trajectory, a pressure
absorption failure, a blow-up construction, or evidence against global
regularity.  It does not rule out adding other correction terms, changing
the pressure coefficient, controlling the functional together with another
quantity, or exploiting time-dependent cancellation.

NEXT DISTINCT ACTION: Independently audit the Euler derivative identity for
this functional.  If that identity passes, any use as a modified energy must
pair it with a separate coercive quantity or alter the correction, because
the coefficient-one functional alone has the counterexample above.
