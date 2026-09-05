# HF02: a compactly supported R3 profile with nonzero pressure work

Status: static algebraic construction for the unforced Navier--Stokes pressure
operator on \(\mathbb R^3\).  It supplies a smooth compactly supported
divergence-free field \(u\) for which

\[
 P_3[u]=\int_{\mathbb R^3}p[u]\,u\cdot\nabla|u|\,dx>0,
 \qquad p[u]=R_iR_j(u_i u_j).
\]

This closes the previously conditional snapshot-profile test.  The field is
not asserted to be a blow-up profile or a Navier--Stokes trajectory segment,
and the construction does not refute the time-integrated high-pressure lemma.

## 1. The periodic cell and its sign

On \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\), put

\[
 \psi(X,Y)=\sin X+\sin Y-\cos(X+Y),
 \qquad v=(\partial_Y\psi,-\partial_X\psi,0).           \tag{1}
\]

Thus \(v\) is divergence free and

\[
 v_1=\cos Y+\sin(X+Y),\qquad
 \partial_Xv_1=\cos(X+Y).                             \tag{2}
\]

Let \(p_v\) be the zero-mean periodic pressure determined by

\[
 -\Delta p_v=\partial_i\partial_j(v_i v_j)
             =-2\det D^2\psi.                         \tag{3}
\]

The sign in (3) follows directly from
\(\partial_i\partial_j(v_i v_j)=\partial_i v_j\partial_jv_i\)
and, for \(v=(\psi_Y,-\psi_X)\),

\[
 \partial_i v_j\partial_jv_i
 =2(\psi_{XY}^2-\psi_{XX}\psi_{YY})=-2\det D^2\psi.
\]

Writing \(Z=X+Y\),

\[
 \psi_{XX}=-\sin X+\cos Z,\quad
 \psi_{YY}=-\sin Y+\cos Z,\quad
 \psi_{XY}=\cos Z,
\]

so

\[
 -2\det D^2\psi
 =-2\sin X\sin Y+2\cos Z(\sin X+\sin Y).              \tag{4}
\]

Since \(-2\sin X\sin Y=\cos(X+Y)-\cos(X-Y)\), the coefficient
of \(\cos Z\) on the right of (3) is \(+1\).  Because
\(-\Delta\cos Z=2\cos Z\), the \(\cos Z\) coefficient of \(p_v\) is
\(+1/2\).  All other Fourier modes are orthogonal to \(\cos Z\).  With
\(\langle\cdot\rangle\) denoting normalized cell average,

\[
 \boxed{\langle p_v\,\partial_Xv_1\rangle
 =\frac12\langle\cos^2Z\rangle=\frac14.}              \tag{5}
\]

For the periodic field \(e_1+\varepsilon v\), the constant part creates no
pressure and the constant--\(v\) cross pressure vanishes by
\(\nabla\cdot v=0\).  Hence the pressure is \(\varepsilon^2p_v\).  Uniformly
for small \(\varepsilon\), Taylor expansion away from zero gives

\[
 (e_1+\varepsilon v)\cdot
 \nabla|e_1+\varepsilon v|
 =\varepsilon\partial_Xv_1+O(\varepsilon^2),           \tag{6}
\]

and (5) yields cell-average pressure work
\(\varepsilon^3/4+O(\varepsilon^4)>0\) for sufficiently small positive
\(\varepsilon\).

## 2. Compact divergence-free localization

Choose a nonnegative, nonzero
\(a\in C_c^\infty(\mathbb R^3)\).  Choose
\(\chi\in C_c^\infty(\mathbb R^3)\) equal to one on a neighborhood of
\(\operatorname{supp}a\), and define

\[
 B=\nabla\times(0,0,\chi(x)y).                         \tag{7}
\]

Then \(B\in C_c^\infty\), \(\nabla\cdot B=0\), and
\(B=e_1\) on a neighborhood of \(\operatorname{supp}a\).

For integers \(n\ge1\), set

\[
 \Psi_n(x,y,z)={a(x,y,z)\over n}\psi(nx,ny),
 \qquad V_n=\nabla\times(0,0,\Psi_n).                  \tag{8}
\]

Then \(V_n\in C_c^\infty(\mathbb R^3;\mathbb R^3)\),
\(\nabla\cdot V_n=0\), and

\[
 V_n=a(x)v(nx,ny)+n^{-1}r_n(x),                        \tag{9}
\]

where \(r_n=((\partial_ya)\psi(nx,ny),
-(\partial_xa)\psi(nx,ny),0)\) is uniformly bounded in every unscaled
\(L^q\) norm, while \(\|\nabla V_n\|_q=O(n)\).

Finally take

\[
 u_{n,\varepsilon}=B+\varepsilon V_n.                 \tag{10}
\]

This is a real, compactly supported, smooth divergence-free field.  On the
support of \(V_n\), it equals \(e_1+\varepsilon V_n\), so it is bounded away
from zero there for \(0<\varepsilon\leq\varepsilon_0(a,\psi)\).

## 3. The cross pressure vanishes exactly

Because \(B=e_1\) wherever \(V_n\ne0\), the cross tensor in
\(u_{n,\varepsilon}\otimes u_{n,\varepsilon}\) is globally

\[
 B\otimes V_n+V_n\otimes B=e_1\otimes V_n+V_n\otimes e_1.
\]

Its double divergence is

\[
 \partial_i\partial_j
 (\delta_{i1}(V_n)_j+(V_n)_i\delta_{j1})
 =2\partial_1\operatorname{div}V_n=0.                 \tag{11}
\]

Thus its Riesz pressure is zero (up to an irrelevant constant), and

\[
 p[u_{n,\varepsilon}]=p_B+\varepsilon^2p_{V_n}.        \tag{12}
\]

This exact cancellation is the reason for placing the entire oscillatory
support inside the constant plateau of \(B\).

## 4. A finite-mode Riesz localization lemma

The needed whole-space approximation is elementary because the periodic
profile has finitely many Fourier modes.

**Lemma.**  Let \(T=m(D)\) be a degree-zero Fourier multiplier whose symbol is
smooth away from the origin.  Let
\(f(X,Y)=\sum_{k\in K}f_ke^{ik\cdot(X,Y)}\), where
\(K\subset\mathbb Z^2\setminus\{0\}\) is finite, and let
\(c\in C_c^\infty(\mathbb R^3)\).  Then

\[
 T[c(x)f(nx,ny)]
 =c(x)\sum_{k\in K}m(k_1,k_2,0)f_ke^{ink\cdot(x,y)}+E_n,           \tag{13}
\]

with \(\|E_n\|_2\leq C_{m,c,f}n^{-1}\).

**Proof.**  For one mode, the Fourier transform of the left side is
\(m(nk+\eta)\widehat c(\eta)\), with \(k\) embedded as \((k_1,k_2,0)\).
On \(|\eta|\leq n|k|/2\), the mean-value theorem and the order-zero symbol
bound \(|\nabla m(\xi)|\leq C|\xi|^{-1}\) give

\[
 |m(nk+\eta)-m(nk)|\leq C_k n^{-1}|\eta|.
\]

Plancherel bounds this portion by \(C_kn^{-1}\|c\|_{H^1}\).  On the
complement, boundedness of \(m\) and rapid decay of \(\widehat c\) give
\(O(n^{-M})\) for any fixed \(M\).  Sum over the finite set \(K\).  Homogeneity
gives \(m(nk)=m(k)\), proving (13).

Apply the lemma componentwise to \(R_iR_j\) and the nonzero Fourier modes of
\(v_i v_j\).  The zero mode must be kept separately.  From (9), \(L^2\)
boundedness of the Riesz transforms, and the lemma,

\[
 p_{V_n}=a^2p_v(nx,ny)+q_0+e_n,\qquad
 \|e_n\|_2\leq C_an^{-1},                              \tag{14}
\]

where, if \(M_{ij}=\langle v_i v_j\rangle\),

\[
 q_0=R_iR_j(M_{ij}a^2)                                 \tag{15}
\]

is a fixed smooth nonoscillatory term, not a band-limited term. Formula (14) also absorbs all terms
containing the \(n^{-1}r_n\) correction in (9).  The constants are independent
of \(n\).

## 5. Pressure-work asymptotics

On \(\operatorname{supp}V_n\), Taylor expansion of the smooth map
\(z\mapsto|z|\) around \(e_1\), using (9), gives in every finite \(L^q\)

\[
 u_{n,\varepsilon}\cdot\nabla|u_{n,\varepsilon}|
 =\varepsilon n a(x)\partial_Xv_1(nx,ny)
  +O_a(\varepsilon)+O_a(n\varepsilon^2),               \tag{16}
\]

uniformly for \(0<\varepsilon\leq\varepsilon_0\).  The error is supported in
one fixed compact set.

Periodic averaging, proved by integrating each nonzero Fourier mode against
the smooth compact amplitude, gives

\[
 \int_{\mathbb R^3}a^3(x)p_v(nx,ny)
              \partial_Xv_1(nx,ny)\,dx
 ={1\over4}\int_{\mathbb R^3}a^3(x)dx+O_a(n^{-1}).     \tag{17}
\]

Indeed, the product is a finite Fourier series whose mean is (5); every
nonzero mode has an oscillatory integral \(O(n^{-1})\), or \(O(n^{-M})\)
after repeated integration by parts.

Combining (12), (14), (16), and (17) gives

\[
 \boxed{\displaystyle
 P_3[u_{n,\varepsilon}]
 ={n\varepsilon^3\over4}\int_{\mathbb R^3}a^3dx
  +O_a(n\varepsilon^4)+O_{a,B,\varepsilon}(1).}        \tag{18}
\]

Here are the error bounds behind (18):

* \(\varepsilon^2a^2p_v(nx,ny)\) paired with the
  \(O(n\varepsilon^2)\) term in (16) is \(O(n\varepsilon^4)\).
* By (14), \(\varepsilon^2e_n\) paired with the leading term in (16) is
  \(O(\varepsilon^3)\) by Cauchy--Schwarz.
* The entire fixed-pressure contribution from \(q_0\) is \(O(1)\): use
  \(u\cdot\nabla|u|=\operatorname{div}(|u|u)\) and integrate the derivative
  onto the fixed smooth \(q_0\).  This avoids falsely estimating the
  second-order oscillatory derivative term by \(O(n)\).
* The entire \(p_B\) contribution is likewise \(O(1)\), since
  \(-\int\nabla p_B\cdot|u|u\) is uniformly bounded on the fixed compact
  support.  Outside \(\operatorname{supp}V_n\), the velocity is just \(B\);
  that part is independent of \(n\).

Choose \(\varepsilon>0\) so small that the absolute coefficient hidden in
\(O_a(n\varepsilon^4)\) is at most
\(\frac18\varepsilon^3\int a^3\).  Then choose \(n\) large enough that the
bounded remainder is smaller than
\(\frac18n\varepsilon^3\int a^3\).  Equation (18) yields

\[
 P_3[u_{n,\varepsilon}]>0.                             \tag{19}
\]

Thus an actual compactly supported divergence-free R3 profile with nonzero
pressure work exists.  Replacing it by its negative reverses \(P_3\), since
\(p[-u]=p[u]\) and \((-u)\cdot\nabla|-u|=-u\cdot\nabla|u|\).  Both signs
therefore occur among smooth compactly supported divergence-free snapshots.

## 6. Scaling consequence and exact scope

For any profile \(u\) obtained above and \(u_N(x)=Nu(Nx)\),

\[
 P_3[u_N]=N^2P_3[u],\qquad D_3[u_N]=N^2D_3[u],
 \qquad \|u_N\|_2^2=N^{-1}\|u\|_2^2.                 \tag{20}
\]

Consequently, at every fixed output cutoff \(J\), the high pressure work has
the nonzero critical asymptotic from `frequency.md`, while kinetic energy
tends to zero.  This rigorously falsifies a pointwise proof that would make
the high tail small relative to its critical scaling using only energy size
and a fixed Bernstein cutoff.

It does **not** falsify the signed spacetime estimate (HF).  The rescaled
profiles in (20) are snapshots, not a family of actual solution trajectories
with the required common input control.  Viscous evolution acts on the same
\(N^{-2}\) time scale on which \(P_3\) and \(D_3\) grow like \(N^2\), so a
temporal cancellation remains logically possible.

**Result:** the earlier condition “if a divergence-free Schwartz profile with
\(P_3\ne0\) exists” is discharged by (7)--(19).

**First remaining gap:** no argument here controls the signed time integral
of high-frequency pressure work along arbitrary large-data R3 trajectories.

**Non-claims:** this is not initial data for a demonstrated singularity, a
stationary solution, or evidence of blowup.  It proves an algebraic snapshot
falsifier and nothing beyond that scope.
