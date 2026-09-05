# HF11: planar swirl heat diagnostic for the pressure entropy

MODE / RESULT: **DISCOVER, restricted nonpositive example.**  The complete
heat derivative of the coercive pressure--speed functional has an exact
one-dimensional form for smooth planar azimuthal swirls.  On the
heat-invariant Gaussian swirl family it is strictly negative.  This family
therefore supplies no positive heat derivative, but it gives a reusable exact
test of every term, including the pressure entropy.

## 1. Planar swirl reduction

Work on \(\mathbb R^2\), and let

\[
 u(x)=w(r)e_\theta,\qquad r=|x|,                       \tag{1}
\]

where \(w\ge0\) is smooth, rapidly decreasing, and \(w(r)=O(r)\) at the
origin with the usual compatibility conditions making \(u\) smooth.  This is
divergence free.  The nonlinear acceleration and the pressure in the
representative vanishing at infinity are

\[
 (u\cdot\nabla)u=-{w^2\over r}e_r,\qquad
 p(r)=-q(r),\qquad
 q(r):=\int_r^\infty {w(s)^2\over s}\,ds.             \tag{2}
\]

Indeed \(p'=w^2/r\), so
\(\Delta p=2ww'/r=-\operatorname{div}((u\cdot\nabla)u)\).
In particular \(p\le0\) and \(p_-=q\).

For this field the two-dimensional analogue of the HF11 functional is

\[
 K[w]=2\pi\int_0^\infty r
 \left({w^3\over3}-qw+q^{3/2}\right)\,dr.             \tag{3}
\]

The planar vector heat equation preserves the swirl class and gives

\[
 w_t=Lw:=w''+{w'\over r}-{w\over r^2}.                \tag{4}
\]

Differentiating (2) along (4) gives the full pressure evolution

\[
 q_t(r)=2\int_r^\infty {w(s)Lw(s)\over s}\,ds.         \tag{5}
\]

Consequently direct differentiation of all three terms in (3) yields

\[
\boxed{\;
 {1\over2\pi}{dK\over dt}
 =\int_0^\infty r(w^2-q)Lw\,dr
  +\int_0^\infty r\left(-w+{3\over2}\sqrt q\right)
       \left(2\int_r^\infty {w(s)Lw(s)\over s}\,ds\right)dr .
\;}                                                    \tag{6}
\]

The second line is the complete derivative of the pressure--speed and
pressure-entropy terms; it must not be omitted.  Equivalently, Fubini gives
the single radial pairing

\[
 {1\over2\pi}{dK\over dt}
 =\int_0^\infty
 \left[
 r(w^2-q)+{2w(r)\over r}
 \int_0^r \sigma\left(-w(\sigma)+{3\over2}\sqrt{q(\sigma)}\right)d\sigma
 \right]Lw(r)\,dr.                                    \tag{7}
\]

Rapid decay and \(w=O(r)\) justify differentiation and Fubini.  Formula
(6), rather than the signs of selected summands, is the exact restricted
sign object.

## 2. An exactly heat-invariant Gaussian family

Fix \(a,\beta>0\) and take

\[
 w_{a,\beta}(r)=a r e^{-\beta r^2}.                   \tag{8}
\]

It is the smooth vector field
\(u=a e^{-\beta r^2}(-y,x)\).  Its pressure is elementary:

\[
 q(r)=\int_r^\infty a^2s e^{-2\beta s^2}\,ds
 ={a^2\over4\beta}e^{-2\beta r^2}.                    \tag{9}
\]

Substitution of (8)--(9) into all three terms of (3) gives

\[
\begin{aligned}
 2\pi\int_0^\infty r\,{w^3\over3}\,dr
 &= { \pi^{3/2}a^3\over4\,3^{5/2}\beta^{5/2}},\\
 -2\pi\int_0^\infty rqw\,dr
 &=-{ \pi^{3/2}a^3\over8\,3^{3/2}\beta^{5/2}},\\
 2\pi\int_0^\infty rq^{3/2}\,dr
 &= {\pi a^3\over24\beta^{5/2}}.                     \tag{10}
\end{aligned}
\]

Thus

\[
 K[w_{a,\beta}]
 =C_*a^3\beta^{-5/2},\qquad
 C_*={\pi\over24}
 \left(1-{\sqrt\pi\over3\sqrt3}\right)>0,             \tag{11}
\]

where positivity follows, for example, from \(\pi<27\).

The planar heat semigroup acts exactly on this vector Gaussian.  With
\(d(t)=1+4\beta t\),

\[
 e^{t\Delta}\!\left[a e^{-\beta r^2}(-y,x)\right]
 ={a\over d(t)^2}
   e^{-\beta r^2/d(t)}(-y,x).                         \tag{12}
\]

Hence the evolved swirl remains (8), with

\[
 a(t)={a\over d(t)^2},\qquad
 \beta(t)={\beta\over d(t)}.                          \tag{13}
\]

Using (11),

\[
 K(t)=C_*a^3\beta^{-5/2}d(t)^{-7/2},
\]

and therefore

\[
\boxed{\quad
 {dK\over dt}(0)=-14\beta K[w_{a,\beta}]<0.
\quad}                                                \tag{14}
\]

More generally \(K'(t)=-14\beta(t)K(t)<0\) for every \(t\ge0\).
Equations (9)--(14) evaluate the pressure--speed and \(p_-^{3/2}\) pieces
exactly, so (14) is an analytic sign certificate rather than a numerical
sign test.

## 3. Scope

CLAIM AND SCOPE: Equations (6)--(7) hold for the stated smooth,
nonnegative, rapidly decreasing planar swirls.  Equation (14) proves strict
heat decrease on the two-parameter Gaussian subclass.  It does not prove
that (6) is nonpositive for every swirl.

EVIDENCE: The pressure formula (2), radial heat equation (4), pressure
derivative (5), and exact Gaussian integrals (9)--(13) account for the full
functional.  The entropy term is responsible for the last term of (10) and
the \(3\sqrt q/2\) contribution in (6)--(7).

FIRST GAP: Decide the sign of (6) for general smooth swirls, or construct a
different analytic family for which the complete expression is positive.
The Gaussian family itself is strictly decreasing and cannot serve as a heat
monotonicity counterexample.

SURVIVING CONDITIONAL SUFFIX: The pressure entropy remains statically
coercive, and the Gaussian swirl is compatible with heat dissipation.  This
does not control the full three-dimensional heat contribution.

NON-CLAIMS: A planar swirl extended constantly in the third coordinate has
infinite three-dimensional energy.  Cutting it off in a long cylinder changes
divergence, introduces axial heat terms, and changes the nonlocal Riesz
pressure.  No \(\mathbb R^3\) lift, limiting cylinder argument, universal heat
sign, Navier--Stokes estimate, pressure absorption, or regularity conclusion
is asserted.

NEXT DISTINCT ACTION: A reusable \(\mathbb R^3\) diagnostic would require
either a genuinely three-dimensional axisymmetric field with exactly
tractable pressure or a long-cylinder construction with quantitative
divergence correction, heat, and Riesz-pressure errors.
