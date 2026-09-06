# A viscous mixing falsifier for record-tangent rigidity

Date: 2026-09-06.
Status: complete author derivation; independent mathematical audit pending.
This is a counterexample to an overbroad proposed rigidity mechanism, NOT
a counterexample to global regularity of the target Navier--Stokes problem.

Companion bridge: `2026-09-06-intrinsic-record-tangents.md`.
Frozen project inputs: research `c2c5f793d1e447a82dd99c7e434c76fc989ec316`,
manuscript `81f0cd1524e8a625e6ee46970d69e40e5a2e50bf`.

## 1. The claim this construction falsifies

A nonconstant ancient Euler limit cannot be excluded merely by saying that
it arose from smooth viscous flows with the following normalized properties:

$$
 [v_n(s)]_\alpha\le1,\quad \langle v_n(s)\rangle_\phi=0,\quad
 |v_n(e_n,0)-v_n(0,0)|=1,
$$

$$
 \mu_n\to0,\quad S_n\to\infty,\quad \mu_n S_n\to\infty,
 \qquad [v_n(-S_n)]_\alpha\to0.
                                                               \tag{1}
$$

In particular, retaining both convective and diffusive backward domain
lengths, rather than only an ancient limit in convective time, does not make
such a rigidity claim true. The construction below has all of (1), actual
first-record selection, smooth globally regular unforced Navier--Stokes
parents, one common smooth periodic initial velocity, and a uniform kinetic
energy bound per periodic cell. Its locally uniform limit is a bounded,
nonconstant, stationary Euler shear. For $\alpha>1/3$, the local viscous
dissipation measures also converge to zero, as in the companion bridge.

The parents have viscosities tending to zero and record times tending to
infinity. They are periodic, not finite-energy fields on the whole space.
These distinctions are essential. The construction does not assert that
this shear is attainable from a singular branch with one fixed whole-space
Schwartz datum, one fixed viscosity, and a finite positive terminal time.

## 2. An exact globally regular Navier--Stokes family

Use coordinates $(x,y,z)$ on the $2\pi$-periodic three-torus. Define

$$
 b(x,y)=(\sin x\cos y,-\cos x\sin y),\qquad
 p_b(x,y)=\tfrac14(\cos2x+\cos2y).
$$

Direct differentiation gives

$$
 \nabla\cdot b=0,\quad \Delta b=-2b,\quad
 (b\cdot\nabla)b+\nabla p_b=0.                                \tag{2}
$$

For every $\varepsilon>0$, set

$$
 B^\varepsilon(x,y,t)=e^{-2\varepsilon t}b(x,y),\qquad
 p^\varepsilon(x,y,t)=e^{-4\varepsilon t}p_b(x,y).
$$

Let $W^\varepsilon$ solve the scalar linear equation

$$
 \partial_tW^\varepsilon+B^\varepsilon\cdot\nabla W^\varepsilon
 =\varepsilon\Delta W^\varepsilon,\qquad W^\varepsilon(0,x,y)=\sin y.
                                                               \tag{3}
$$

Then

$$
 U^\varepsilon=(B^\varepsilon_1,B^\varepsilon_2,W^\varepsilon)
                                                               \tag{4}
$$

with the displayed pressure is an exact unforced three-dimensional
Navier--Stokes solution of viscosity $\varepsilon$. All fields are
independent of $z$. The third velocity component has no feedback into the
two horizontal equations; its equation is precisely (3). The pressure has
no $z$ derivative. The horizontal equations follow from (2).

Equation (3) is uniformly parabolic for each fixed $\varepsilon>0$, with
smooth globally defined periodic coefficients. It has a global smooth
solution; differentiating (3) and using finite-time Gronwall bounds gives
all spatial derivatives on every finite interval. The maximum principle
bounds $|W^\varepsilon|$ by one. Thus these are globally regular solutions,
not hypothetical singular solutions or approximate solutions.

Every member has the same initial velocity

$$
 U_0=(\sin x\cos y,-\cos x\sin y,\sin y).
$$

The mean of $|U_0|^2$ on the three-torus is one. The ordinary periodic
energy identity gives

$$
 \int_{\mathbb T^3}|U^\varepsilon(t)|^2
 \le (2\pi)^3                                                     \tag{5}
$$

uniformly in $\varepsilon$ and $t$. As fields on $\mathbb R^3$, their
periodic lifts do not have finite total kinetic energy.

## 3. Uniform control of the inviscid transport approximation

The matrix $\nabla b$ has the form

$$
 \begin{pmatrix}a&-d\\ d&-a\end{pmatrix},\qquad
 a=\cos x\cos y,\quad d=\sin x\sin y.
$$

Its singular values are $|a+d|$ and $|a-d|$, both at most one.
Consequently $\|\nabla B^\varepsilon(t)\|_{\mathrm{op}}\le1$.
Let $\Phi_\tau$ be the flow of $b$ and put

$$
 q_\varepsilon(t)=\int_0^t e^{-2\varepsilon s}ds
       =\frac{1-e^{-2\varepsilon t}}{2\varepsilon},
 \qquad
 \widetilde W^\varepsilon(t)=W_0\circ\Phi_{-q_\varepsilon(t)}.
$$

This solves (3) with its diffusion term removed. Its spatial derivatives
obey, for $j=1,2,3$,

$$
 \|\nabla^j\widetilde W^\varepsilon(t)\|_\infty\le C_j e^{jt}.   \tag{6}
$$

For completeness, the first derivative of the forward or backward flow is
bounded by $e^{|\tau|}$ using $\|\nabla b\|\le1$. The ODE for the
second derivative has a homogeneous coefficient of norm at most one and a
forcing bounded by $C e^{2|\tau|}$; its integral is bounded by
$C e^{2|\tau|}$. The third-derivative ODE is treated similarly with
forcing bounded by $C e^{3|\tau|}$. Composing with the fixed smooth $W_0$
and using $q_\varepsilon(t)\le t$ proves (6), with constants independent
of $\varepsilon$.

Write $D^\varepsilon=W^\varepsilon-\widetilde W^\varepsilon$.
It has zero initial data and satisfies

$$
 (\partial_t+B^\varepsilon\cdot\nabla-\varepsilon\Delta)D^\varepsilon
 =\varepsilon\Delta\widetilde W^\varepsilon.
$$

The maximum principle and (6) yield

$$
 \|D^\varepsilon(t)\|_\infty\le C\varepsilon e^{2t}.            \tag{7}
$$

After differentiating, the extra matrix coefficient has norm at most one.
Applying the corresponding scalar inequality to the gradient magnitude,
or first to a regularized magnitude, gives

$$
 \|\nabla D^\varepsilon(t)\|_\infty
 \le\int_0^t e^{t-s}C\varepsilon e^{3s}ds
 \le C\varepsilon e^{3t}.                                      \tag{8}
$$

These bounds are for actual solutions of (3), not a numerical
approximation. They suffice below without any uniform-in-time inviscid
limit theorem.

## 4. Exponentially growing increments before diffusion dominates

On the invariant line $x=0$, the flow of $b$ solves

$$
 \dot y=-\sin y,\qquad
 \tan(y(\tau)/2)=e^{-\tau}\tan(y(0)/2).
$$

Thus at the two points

$$
 P_\pm(t)=\bigl(0,\ \pm2\arctan(e^{-q_\varepsilon(t)})\bigr)
$$

the transported scalar has values
$\widetilde W^\varepsilon(t,P_\pm(t))=\pm1$. Their separation is
$4\arctan(e^{-q_\varepsilon(t)})$.

Fix $0<\alpha<1/2$, and for integers $n$ tending to infinity choose

$$
 \varepsilon_n=n^{-1/2}e^{-2n}.                                \tag{9}
$$

The elementary inequality
$0\le t-q_\varepsilon(t)\le\varepsilon t^2$ shows
$q_{\varepsilon_n}(n)=n+o(1)$. By (7), the actual scalar increment at
$P_\pm(n)$ is at least $2-Cn^{-1/2}$. Consequently

$$
 [U^{\varepsilon_n}(n)]_\alpha\ge c_\alpha e^{\alpha n}.       \tag{10}
$$

All seminorms here are those of the periodic lift on $\mathbb R^3$.
They are finite for bounded smooth periodic functions. The amplitude
bound, (6), and (8) imply for $0\le t\le n$

$$
 \|U^{\varepsilon_n}(t)\|_\infty\le C,\qquad
 \|\nabla U^{\varepsilon_n}(t)\|_\infty\le C e^t,
 \qquad [U^{\varepsilon_n}(t)]_\alpha\le C_\alpha e^{\alpha t}.
                                                               \tag{11}
$$

The last inequality follows by interpolating the uniform amplitude and
Lipschitz bounds. The constants do not depend on $n$.

Choose a fixed sufficiently small $c>0$ and let $t_n$ be the first time
at which

$$
 [U^{\varepsilon_n}(t_n)]_\alpha=H_n:=c e^{\alpha n}.
$$

Equations (10)--(11) ensure, after discarding finitely many indices,

$$
 n-C_\alpha\le t_n\le n,\qquad
 [U^{\varepsilon_n}(t)]_\alpha\le H_n\quad(0\le t\le t_n).     \tag{12}
$$

Continuity in time gives the first hitting time. The Holder quotient
attains its maximum: periodicity makes the location compact modulo a
period, bounded amplitude removes arbitrarily large separations, and a
bounded gradient removes separations tending to zero.

Let $r_n$ be the maximizing separation and $A_n=H_nr_n^\alpha$ its
increment. By (11), $A_n\le C$ and $A_n\le C e^n r_n$. These two
inequalities, together with $H_n=c e^{\alpha n}$, give both sides of

$$
 c_1e^{-n}\le r_n\le c_2e^{-n},\qquad
 c_3\le A_n\le c_4.                                           \tag{13}
$$

This step uses the actual maximizing pair, not an arbitrarily prescribed
pair on the invariant line.

## 5. Both backward domains diverge

Use exactly the local-mean moving frame and convective normalization in
the companion note, with parent velocity $U^{\varepsilon_n}$ and parent
viscosity $\varepsilon_n$. Then, by (9), (12), and (13),

$$
 \mu_n=\frac{\varepsilon_n}{A_nr_n}\asymp n^{-1/2}e^{-n}\to0,
 \qquad
 S_n=\frac{t_nA_n}{r_n}\asymp n e^n\to\infty,
$$

$$
 \mu_n S_n=\frac{\varepsilon_nt_n}{r_n^2}\asymp\sqrt n
 \longrightarrow\infty.                                      \tag{14}
$$

In particular the construction does not rely on a bounded, or vanishing,
diffusive backward domain. A simpler linearly mixing example would fail
this test; the exponentially stretching cellular flow is needed here.

Since the initial datum is common to all members,

$$
 [v_n(-S_n)]_\alpha=[U_0]_\alpha/H_n\longrightarrow0.           \tag{15}
$$

Record selection and centring give all the other conditions in (1),
including the exact unit terminal increment. In this example the
normalized velocities are even uniformly bounded on all of space-time,
because the original amplitudes are bounded and $A_n$ is bounded below.

## 6. The limit is a nonconstant stationary Euler shear

The compactness argument of Sections 4 and 6 of the companion note uses
only the normalized Holder/growth bound, a bounded effective viscosity,
and the canonical pressure. It therefore applies here. For a smooth
periodic field, the canonical whole-space pressure gradient agrees with
the usual periodic Fourier pressure gradient: this is checked first on
Fourier modes, where the zero mode contributes no gradient, and then by
smooth periodic approximation and the integrable far-gradient kernel.

There is also a direct check in this example. The physical pressure is
$p^{\varepsilon_n}$ from Section 2. Its spatial gradient is bounded
independently of $n$. After dividing pressure by $A_n^2$, its oscillation
on any normalized compact ball is at most $C r_n/A_n^2$, which tends to
zero. The canonical pressure gauge is therefore zero in the limit.

The horizontal velocity $B^{\varepsilon_n}$ is uniformly Lipschitz with
constant at most one. Its centred, normalized horizontal increment on a
fixed ball is bounded by $C r_n/A_n\to0$. The third component and the
moving mean are independent of the third spatial coordinate. Hence any
locally uniform subsequential limit has the form

$$
 v(y,s)=(0,0,F(y_1,y_2,s)).                                    \tag{16}
$$

It is bounded, has global Holder seminorm at most one, has zero
$\phi$-mean, and retains a unit terminal increment. In particular it
is not a spatial constant.

For a field of the form (16),
$\nabla\cdot(v\otimes v)=0$, since only its $(3,3)$ entry is nonzero
and that entry is independent of $y_3$. Its canonical pressure is zero.
The centred Euler equation thus says $\partial_s v=-a(s)$ with $a$
spatially constant. Differentiating the zero $\phi$-mean forces $a=0$.
Therefore $F$ is independent of $s$: the limit is a nonconstant
stationary Euler shear.

For $1/3<\alpha<1/2$, the local commutator and tested energy identity
in the companion note also give

$$
 \mu_n|\nabla v_n|^2\,dy\,ds\longrightarrow0
$$

on every compact subset of the open ancient domain. There is no positive
local anomalous dissipation that can be used to contradict this example.
No smoothness of the limiting scalar beyond the proved Holder class is
needed for the falsification.

## 7. Exact scope of the obstruction

This example disproves rigidity statements based only on the normalized
package (1), first records, and local convergence, even when these are
supplemented with a uniform energy bound per parent periodic cell. It also
exposes an invalid exchange of limits: (15) at the receding initial times
does not imply that the limiting ancient field tends to zero as
$s\to-\infty$. Here the limiting field is stationary and nonzero.

It does not disprove an appropriately stronger theorem about tangents of
one fixed finite-energy whole-space solution with a finite-time endpoint.
The fixed-input and fixed-viscosity restrictions cannot be erased merely
because the limiting equation is Euler. Nor can a uniform global energy
bound for the centred tangent be manufactured from the periodic bound (5)
or from the original whole-space bound in the companion theorem.

A proposed next rigidity lemma must therefore either retain and use a
specific additional fixed-input restriction, or choose a different
mathematical object. Defining a class as "exactly the tangents of a
singularity" and asserting that it is empty is just regularity renamed,
not a new lemma. Adding another unproved endpoint norm is likewise not a
repair. This note is a stop rule for those mechanisms, not an assertion
that all future blow-up or Lagrangian arguments must fail.

## 8. Verification and attribution

The identities (2), including the pressure sign and Laplacian eigenvalue,
were independently recomputed algebraically within the author check using
SymPy. The symbolic outputs were zero divergence, zero Euler residual,
and zero residual for $\Delta b+2b$. The singular-value calculation for
$\nabla b$ was checked symbolically as well. These are finite algebra
checks, not an independent mathematical audit of the compactness argument.

The analytic argument above explicitly proves the required transport
approximation estimates, scale bounds, both backward-domain limits, and
classification of the limiting vertical field. No numerical Navier--Stokes
simulation or formal proof is claimed. Independent review should focus on
(6)--(8), use of the actual first-record maximizer in (13), periodic versus
whole-space pressure normalization, and preservation of nonconstancy.

The 2.5-dimensional passive-scalar construction is a classical mechanism;
no priority claim is made for it or for exponential stretching near a
hyperbolic point. The present note uses its displayed formulas as a
self-contained falsifier of the precise proposed record-tangent package.
For the broader context of Euler limits from Navier--Stokes blow-up,
see G. Seregin, arXiv:2304.04045v1. For the local energy-conservation
mechanism used in Section 6, see Constantin--E--Titi (1994), DOI
10.1007/BF02099744, and the complete local calculation in the companion
note. No theorem from those sources is promoted to arbitrary-data
regularity here.
