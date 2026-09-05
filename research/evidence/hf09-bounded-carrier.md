# HF09: bounded-carrier variable-weight obstruction on the torus

Status: bounded periodic mechanism test.  This note strengthens the
variable-weight calculation by keeping the perturbation uniformly bounded in
\(L^2\) as its carrier frequency tends to infinity.  It is not an
\(\mathbb R^3\) result and has no direct HIGH-PRESSURE or continuation
consequence.

## 1. One admissible tight frame with the required plateau

Work on \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), with normalized integral
\(\langle h\rangle=(2\pi)^{-3}\int h\).  The plateau used below can be built
into a single smooth radial tight Littlewood--Paley frame as follows.

Put \(a=\log_2(8/5)\).  Choose a smooth nondecreasing function
\(\alpha:[a,1]\to[0,\pi/2]\), equal to zero near \(a\) and to \(\pi/2\) near
\(1\).  Define a smooth function \(r\) on the logarithmic radial variable by

\[
 r(t)=
 \begin{cases}
  \sin\alpha(t+1),&a-1\le t\le0,\\
  1,&0\le t\le a,\\
  \cos\alpha(t),&a\le t\le1,\\
  0,&\text{otherwise}.
 \end{cases}                                         \tag{1}
\]

The constant neighborhoods in the definition of \(\alpha\) make all joins
smooth.  For \(t\in[0,a]\), only \(r(t)\) among the integer translates is
nonzero and equals one.  For \(t\in[a,1]\), the only nonzero terms are
\(r(t)=\cos\alpha(t)\) and
\(r(t-1)=\sin\alpha(t)\).  Translation therefore proves exactly that

\[
 \sum_{j\in\mathbb Z}r(t-j)^2=1.                     \tag{2}
\]

Set

\[
 m_j(\xi)=r(\log_2|\xi|-j),\qquad \Delta_j=m_j(D).   \tag{3}
\]

These are smooth, real, radial, self-adjoint annular multipliers away from the
zero mode, (2) is the tight-frame identity, and

\[
 m_j(\xi)=1\quad\text{for}\quad
 2^j\le|\xi|\le {8\over5}2^j.                        \tag{4}
\]

Thus the plateau is a proved property of the one fixed frame (3), rather than
an assumption changed with the carrier.

## 2. Uniformly bounded carrier

Fix \(A>0\), \(\epsilon>0\), and

\[
 U=(A\cos z,0,0),\qquad
 s=(\epsilon^2+A^2\cos^2z)^{1/2}.                    \tag{5}
\]

For \(N=2^J\ge8\), let

\[
 \begin{aligned}
 k&=(N,0,N),&a_0&=(1,0,-1),\\
 \ell&=(-N,0,1-N),&b_0&=(1-N^{-1},0,-1),             \tag{6}\\
 v_N(x,z)&=a_0\cos(k\cdot(x,y,z))+b_0\sin(\ell\cdot(x,y,z)).
 \end{aligned}
\]

Both polarizations are solenoidal because \(k\cdot a_0=0\) and
\(\ell\cdot b_0=0\).  Orthogonality of distinct Fourier modes gives

\[
 \|v_N\|_2^2={3+(1-N^{-1})^2\over2}\le2.             \tag{7}
\]

Take the finite band \(W=(\Delta_0,\Delta_J)\).  The background frequency has
length one.  The two carrier frequencies and every frequency produced by
linearizing about \(U\) have the form

\[
 (\pm N,0,q),\qquad q\in\{N-1,N,N+1,2-N,1-N,-N\},   \tag{8}
\]

up to signs and repetitions.  For \(N\ge8\), all their lengths lie in
\([N,(8/5)N]\).  Hence (4) gives exactly

\[
 WU=(U,0),\qquad Wv_N=(0,v_N),\qquad
 \Delta_JV_{\rm lin}(U,v_N)=V_{\rm lin}(U,v_N).      \tag{9}
\]

The only low nonzero beat of \(V(v_N)\) that can pair with the
\(x\)-independent field \(sU\) has frequency \((0,0,\pm1)\), where
\(m_0=1\).  All remaining outputs either have nonzero \(x\)-frequency or are
orthogonal to \(sU\).  Consequently the first two lines of the exact
finite-band second variation reduce without a multiplier approximation to

\[
 \mathcal C_2(U,v_N)
 =\langle sU,V(v_N)\rangle
  +\langle sv_N,V_{\rm lin}(U,v_N)\rangle.            \tag{10}
\]

The background-weight evolution term is exactly zero because \(V(U)=0\).

## 3. Positive limiting coefficient with exact Leray projection

As in the complete weighted calculation, write

\[
 V_{\rm lin}(U,v_N)=-(U\cdot\nabla)v_N
 -(v_N\cdot\nabla)U-\nabla p_N.
\]

Since \(\operatorname{div}(sU)=0\), integration by parts in (10), including
the nonlinear-pressure term, gives the exact scalar identity

\[
 \mathcal C_2(U,v_N)
 =\left\langle s'(z)(v_N)_3
       \bigl(U(v_N)_1+p_N\bigr)\right\rangle,         \tag{11}
\]

where the linearized pressure, and hence the full Leray correction, is
retained through

\[
 \Delta p_N=-2U'(z)\partial_x(v_N)_3.                 \tag{12}
\]

Averaging the first product in the fast variable \(x\) is elementary:

\[
 \left\langle(v_N)_1(v_N)_3\right\rangle_x
 =-{2-N^{-1}\over2}(1+\sin z).                       \tag{13}
\]

Because \(s'U=-A^3\cos^2z\sin z/s\), the part odd in \(z\) integrates to
zero and (13) yields

\[
 L_N:={2-N^{-1}\over2}A^3
 \left\langle{\cos^2z\sin^2z\over s}\right\rangle_z>0. \tag{14}
\]

It remains to bound the pressure without discarding it.  Every Fourier mode
on the right of (12) has \(|\xi_x|=N\), so inversion of \(\Delta\) and
Parseval give

\[
 \|p_N\|_2
 \le {2\over N^2}\|U'\partial_x(v_N)_3\|_2
 \le {2A\over N^2}\|\partial_x(v_N)_3\|_2
 ={2A\over N}.                                      \tag{15}
\]

Here the last equality follows because the two Fourier waves in
\((v_N)_3=-\cos(k\cdot x)-\sin(\ell\cdot x)\) are orthogonal.  Also
\(\|(v_N)_3\|_2=1\) and

\[
 \|s'\|_\infty
 =\left\|{-A^2\cos z\sin z\over s}\right\|_\infty
 \le {A^2\over2\epsilon}.                            \tag{16}
\]

Therefore the exact pressure remainder

\[
 R_N:=\langle s'(v_N)_3p_N\rangle
\]

satisfies

\[
 |R_N|\le {A^3\over\epsilon N}.                      \tag{17}
\]

Combining (11), (14), and (17) proves

\[
 \boxed{\quad \mathcal C_2(U,v_N)=L_N+R_N,\qquad
 |R_N|\le {A^3\over\epsilon N}.\quad}                \tag{18}
\]

If

\[
 I_{A,\epsilon}:=
 \left\langle{\cos^2z\sin^2z\over
 (\epsilon^2+A^2\cos^2z)^{1/2}}\right\rangle_z>0,   \tag{19}
\]

then \(L_N\to A^3I_{A,\epsilon}\).  In particular, for every sufficiently
large dyadic \(N\),

\[
 \mathcal C_2(U,v_N)\ge {1\over2}A^3I_{A,\epsilon}>0. \tag{20}
\]

Replacing the second summand in (6) by \(-b_0\sin(\ell\cdot x)\) reverses
the sign of the complete coefficient.  Indeed, the terms quadratic in either
single carrier have only odd \(z\)-frequency after the \(U'\) shift and pair
to zero with \(s'\), whose Fourier frequencies are nonzero even integers.
Only the cross-carrier terms survive, and all of them change sign.

## 4. Exact obstruction and scope

**MODE / RESULT:** FALSIFY.  For the single admissible tight frame (1)--(4),
the normalized high carrier has bounded quadratic mass while its complete
variable-weight second variation stays bounded away from zero with either
sign.

More precisely, (7), (18), and (20) rule out any universal estimate for this
family of the form

\[
 |\mathcal C_2(U,v_N)|
 \le C(U,\epsilon)N^{-\gamma}\|v_N\|_2^2,
 \qquad \gamma>0,                                    \tag{21}
\]

with a constant independent of \(N\).  Thus scale separation alone supplies
no positive power gain for the normalized instantaneous coefficient.  The
weighted Leray term is present and is quantitatively smaller here; every
finite-band multiplier is exact on the active pairings by (4), (8), and (9).

**FIRST GAP:** (21) is only an obstruction to a proposed instantaneous
high--low gain for this square-functional coefficient.  It is not an
\(\mathbb R^3\) counterexample and does not address time integration,
viscous absorption, arbitrary trajectories, or the universal signed HF
statement.

**NON-CLAIMS:** no localization of these plane waves to \(\mathbb R^3\),
infinite-band or \(\epsilon\downarrow0\) passage, Navier--Stokes solution
construction, critical estimate, regularity theorem, or Clay conclusion is
asserted.

**NEXT DISTINCT ACTION:** transferring this obstruction to the whole-space
mechanism would require a localized wave packet with proved uniform errors
for the nonlocal Leray projection and the fixed frame multipliers.  A periodic
instantaneous obstruction alone does not provide that transfer.
