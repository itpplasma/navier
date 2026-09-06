## 6. A divergence-free countermodel with exact energy balance, slow records, and unbounded deformation

This construction tests proposed *intermediate inferences*. It is not claimed to solve NS, satisfy the local energy inequality with the NS pressure, or satisfy the exact enstrophy identity. Its vector-equation residual is computed explicitly.

### 6.1 A compactly supported profile with a prescribed linear core

Let

\[
A_0=\begin{pmatrix}2&-1&0\\1&-2&0\\0&0&0\end{pmatrix}.
\]

It has trace zero, eigenvalues `sqrt(3), -sqrt(3), 0`, satisfies `A_0 e_3=0`, and

\[
\nabla\times(A_0x)=2e_3.
\]

Choose a smooth cutoff `chi` equal to one on `B_1` and zero outside `B_2`. Define

\[
W_0(x)=\nabla\times\left[-\tfrac13\chi(x)\,x\times(A_0x)\right]. \tag{6.1}
\]

Then `W_0` is smooth, compactly supported, and divergence free. The identity

\[
\nabla\times\bigl(x\times(A_0x)\bigr)=-3A_0x
\]

shows that `W_0=A_0x` near zero. Put

\[
e_0=\|W_0\|_2^2>0,\quad
y_0=\|\nabla W_0\|_2^2>0,\quad
z_0=\|\Delta W_0\|_2^2>0.
\]

Choose

\[
\tfrac12\le\alpha<\tfrac34,\qquad
m=\tfrac32-2\alpha\in(0,\tfrac12],\qquad
L^2=\frac{2y_0}{m e_0}.
\]

For an amplitude `a>0`, define

\[
W(x)=aL W_0(x/L).
\]

Its norms are

\[
e=a^2L^5e_0,\quad y=a^2L^3y_0,\quad z=a^2Lz_0,
\qquad me=2y. \tag{6.2}
\]

Near zero, `W(x)=a A_0x`.

### Theorem 6.1: exact energy and the enstrophy upper inequality do not exclude slow critical growth

For any prescribed `C>0`, choose `a` sufficiently large that

\[
(1-m)y+z\le C y^3.
\]

This is possible because the left side is proportional to `a^2` and the right side to `a^6`. For `0<=t<1`, put `tau=1-t` and

\[
b(x,t)=\tau^{-\alpha}W(x/\sqrt\tau). \tag{6.3}
\]

Every time slice is smooth, compactly supported, and divergence free, with a Schwartz initial datum. Direct changes of variables give

\[
E_b=e\tau^m,\qquad
Y_b=y\tau^{m-1},\qquad
Z_b=z\tau^{m-2},
\]

where `E_b=||b||_2^2`, `Y_b=||grad b||_2^2`, and `Z_b=||Delta b||_2^2`. Consequently

\[
E_b'+2Y_b=0,
\qquad
E_b(t)+2\int_0^tY_b(s)\,ds=E_b(0), \tag{6.4}
\]

and

\[
\frac{Y_b'+Z_b}{Y_b^3}
 =\frac{(1-m)y+z}{y^3}\,\tau^{1-2m}\le C, \tag{6.5}
\]

because `1-2m=4alpha-2>=0` and `0<tau<=1`. Thus `Y_b'+Z_b<=C Y_b^3`, a stronger version, after adjustment of constants, of the enstrophy upper inequality used in the graph. Moreover,

\[
\int_0^1Y_b(t)\,dt=y/m<\infty.
\]

For `alpha>1/2`, however,

\[
\|b(t)\|_3=\tau^{1/2-\alpha}\|W\|_3\longrightarrow\infty,
\qquad
\int_0^1Y_b(t)^2\,dt=\infty. \tag{6.6}
\]

Let `K=||W||_infinity`. The velocity maximum is exactly `K tau^(-alpha)`. Taking levels `M_n=2^nK` yields first record times `t_n=1-2^(-n/alpha)` and

\[
M_n^2(t_n-t_{n-1})
 =K^2(2^{1/\alpha}-1)\,2^{n(2-1/\alpha)}\longrightarrow\infty
\quad(\alpha>1/2). \tag{6.7}
\]

Hence the slow-record alternative in Section 5 cannot be excluded using only exact global energy balance, the enstrophy upper inequality, smooth divergence-free time slices, and the corresponding integral budgets.

The spatial moments also remain finite: `integral |x|^2 |b|^2` is a constant times `tau^(m+1)`, and `integral |x|^2 |grad b|^2` is a constant times `tau^m`. This statement is about those finite quantities, not a claim that the curve satisfies every identity or every fixed constant in the project's moment derivation.

### Theorem 6.2: volume preservation plus those budgets does not bound deformation

Let `X(t,xi)` be the ordinary flow of `b` on any interval ending before `1`. Since `b(0,t)=0`, its central trajectory remains at zero. Set

\[
J(t)=D_\xi X(t,0),\qquad \gamma=\alpha+\tfrac12.
\]

The variational equation is

\[
J'=a(1-t)^{-\gamma}A_0J,\qquad J(0)=I.
\]

Thus

\[
J(t)=\exp(aA_0 I_\gamma(t)),\qquad
I_\gamma(t)=
\begin{cases}
-\log\tau,&\gamma=1,\\
(\tau^{1-\gamma}-1)/(\gamma-1),&\gamma>1.
\end{cases} \tag{6.8}
\]

Since `tr A_0=0`, `det J(t)=1`. Since `A_0` has the positive eigenvalue `sqrt(3)`,

\[
\|J(t)\|\ge\exp(a\sqrt3\,I_\gamma(t))\longrightarrow\infty. \tag{6.9}
\]

This is an exact incompressible-flow obstruction, not merely the observation that arbitrary determinant-one matrices can have large norms. It includes the genuine global energy identity and the enstrophy upper inequality along a single fixed initial field.

It does not directly falsify an averaged stochastic pullback estimate for actual NS solutions. It falsifies the proposed derivation of deformation control from volume preservation and those scalar budgets alone.

### 6.3 The explicit vector residual prevents an NS overclaim

At the central trajectory the vorticity is

\[
\omega_b(0,t)=2a\tau^{-\gamma}e_3,
\qquad
\partial_t\omega_b(0,t)=2a\gamma\tau^{-\gamma-1}e_3\ne0.
\]

Near zero the velocity is exactly linear and the vorticity spatially constant. Therefore

\[
(b\cdot\nabla)\omega_b=0,\quad
\Delta\omega_b=0,\quad
(\omega_b\cdot\nabla)b
 =2a^2\tau^{-2\gamma}A_0e_3=0
\quad\text{at }x=0.
\]

The unit-viscosity NS vorticity equation would require the displayed nonzero time derivative to vanish. No pressure choice can repair a nonzero curl residual. This proves directly that (6.3) is not an unforced NS solution.

For `alpha>1/2`, the exact global enstrophy identity is also not supplied: its viscous/time-derivative side scales as `tau^(-1/2-2alpha)`, whereas its stretching integral scales as `tau^(-3alpha)`. Their positive left coefficient and unequal exponents preclude equality for the entire interval. The upper inequality must not be substituted for that identity.

### 6.4 Relation to prior comparison profiles

At `alpha=1/2`, (6.3) is precisely the backward self-similar velocity scaling underlying the Leray-profile literature [NRS, TSAI] and several earlier project countermodels. For `alpha>1/2`, it uses a distinct amplitude exponent and realizes slow record transitions. The construction is presented as a directly checkable falsifier for the two proposed bridges, not as discovery of the self-similar ansatz or a new solution of the Leray profile equation. Neither exact self-similar rigidity nor its citations are imported as a theorem excluding the marked ancient class.
