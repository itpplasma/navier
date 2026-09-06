# Terminal closure tests: critical Lyapunov obstruction and an exact two-balance countermodel

Date: 2026-09-06.
Status: complete author derivations; independent mathematical audit pending.
Terminal theorem: not proved. Terminal obstruction: unchanged.

Frozen research input: `f95bd7c9edf18d45059c4b8b024444ac625bf96b`.
This is research evidence, not a manuscript theorem or a promoted graph node.
There is no novelty claim. The construction below is NOT an unforced
Navier--Stokes solution; a nonzero curl residual is proved explicitly.

## 1. Terminal edge, admissible architectures, and the new exclusion

The target remains NS-R3: for every positive viscosity and every solenoidal
Schwartz datum on R3, the original unforced equation has a global smooth
solution with bounded kinetic energy. LOCAL, ENERGY and CONTINUATION in
`docs/proof-graph.yaml` supply the suffix once an arbitrary-data bound

$$
 \sup_{t<\min(H,T_*)}\|u(t)\|_3<\infty
$$

has actually been proved from the fixed inputs. Naming that supremum is not
a producer. None of the results here proves this bound for actual NS.

Three different mechanisms were tested against that suffix.

**Critical Lyapunov closure.** If a universal scale-invariant function of
energy and enstrophy were coercive in their product and nonincreasing on
all classical NS solutions, the interpolation inequality in Section 3
would give the required L3 bound directly. There would be no additional
unknown quantity. Section 3 rules out this entire C1 two-scalar class,
using actual local NS solutions from compactly supported data.

**Exact-balance dynamical closure.** A bound derived solely from the two
exact global NS balances, including the actual spatial vortex-stretching
integral rather than an upper estimate, would apply to every solenoidal
curve satisfying those premises. Section 4 constructs such a curve whose
L3 norm diverges. The residual is invisible to BOTH global tests, not just
the energy test. Thus replacing the old enstrophy inequality by its exact
identity is not, by itself, an escape from the scalar-budget obstruction.

**Strong-energy-compactness closure.** Even granting a strong L2 endpoint
and uniform spatial tightness, an argument still has to produce control at
the critical spatial scale. The same countermodel is strongly continuous
in L2 through its finite endpoint, with uniformly compact spatial support
and no loss in the global energy equality there. Nevertheless its L3 norm
and critical local energy concentration diverge. Section 5 gives the
explicit missing spatial rate. This is a falsification of that inference,
not a claim that actual NS has this endpoint behavior.

The active intrinsic-record proposal was also checked against the progress
gate. A theorem selecting a tangent with nonzero centred nonlinear
generator would not yet exclude nonlinear ancient NS/Euler profiles. The
current PLAN and the extraction note already acknowledge that missing
classification. Such selection alone is therefore not a terminal main
task under the owner's current instructions. The extraction is preserved;
neither it nor the fixed-input selection question is disproved here.

### Relation to the previous falsifiers

The new result must not be confused with the earlier records:

- `terminal-reset/05-countermodel.md`, Section 6.3, explicitly does NOT
  satisfy the exact NS enstrophy identity.
- `hf28-review-countermodel-spectral.md`, Section 3(e), explicitly leaves
  exact enstrophy and vector-equation premises outside its excluded class.
- The present construction DOES satisfy the exact enstrophy identity with
  the stretching of its own velocity, as well as the exact energy identity.
  Its strong L2 endpoint also prevents an explanation based merely on an
  energy atom or loss of global kinetic energy.

This is not a blanket strengthening of every earlier countermodel: it is
not band-limited, not a family of Galerkin solutions, not defined smoothly
past its endpoint, and not subject to the local NS energy equation. Those
premises must not be silently imported. The mathematical delta is the
specific extension of the excluded premise class just stated.

## 2. Two compactly supported solenoidal profiles

For a smooth compactly supported solenoidal field w, write

$$
 E(w)=\int|w|^2,\quad Y(w)=\int|\nabla w|^2,\quad
 Z(w)=\int|\Delta w|^2,\quad
 S(w)=\int\omega_w\cdot((\omega_w\cdot\nabla)w),
 \qquad \omega_w=\nabla\times w.
$$

All integrals in this note are over R3 unless otherwise specified. The
convention is squared norms, without factors of one half. For classical NS,

$$
 E'=-2\nu Y,\qquad Y'=2S-2\nu Z.                         \tag{1}
$$

### 2.1 A compact profile W with strictly positive total stretching

Start with the periodic field and a bounded periodic vector potential

$$
 U=(0,-\cos x,\sin y+\cos(x+y)),\qquad
 A=(\cos y,\sin(x+y),\sin x),\qquad \nabla\times A=U.
$$

Its vorticity is

$$
 \omega_U=(\cos y-\sin(x+y),\sin(x+y),\sin x).
$$

Consequently its stretching density is

$$
 \omega_U\cdot((\omega_U\cdot\nabla)U)
 =\sin x\sin(x+y)\cos y-\sin x\sin^2(x+y),
$$

whose mean over a periodic cell is 1/4.

Choose a nonnegative C-infinity cutoff chi, equal to one on B1 and zero
outside B2. For L large set

$$
 W_L=\nabla\times(\chi(x/L)A(x)).
$$

Then W_L is compactly supported and solenoidal. Uniformly on its support,

$$
 W_L=\chi(x/L)U+O(L^{-1}),\qquad
 \nabla W_L=\chi(x/L)\nabla U+O(L^{-1}).
$$

The support has volume O(L3), so the error in its stretching integral is
O(L2). The leading integrand is chi(x/L)^3 times the periodic stretching
density. Every nonzero Fourier mode has integral O(L2), by one integration
by parts against the cutoff. The constant mode therefore gives

$$
 S(W_L)=\tfrac14 L^3\int\chi^3+O(L^2)>0
$$

for all sufficiently large L. This is a whole-space compact-profile
construction, not an inference transferring a periodic PDE theorem.

Zero helicity can be imposed without losing this sign. Take two disjoint
translated copies of W_L, reflect one by an orthogonal matrix Q with
determinant -1, and sum them. Under w(x) -> Qw(Q^T x), energy, enstrophy,
Z and S are invariant, while the helicity integral changes sign. Disjoint
supports remove all cross terms. Fix the resulting field W and constants

$$
 e=E(W)>0,\quad y=Y(W)>0,\quad z=Z(W)>0,\quad \sigma=S(W)>0.
                                                               \tag{2}
$$

Then W is smooth, compactly supported, solenoidal, and has zero helicity.
The reflection is optional for the two main proofs, but makes the scope
of helicity-only repairs explicit.

### 2.2 A compact reservoir V with zero stretching

Let rho be a smooth function of one real variable, equal to one near zero
and zero for arguments at least one. In coordinates xi define

$$
 V_0(\xi)=\rho(|\xi|^2)(-\xi_2,\xi_1,0).
$$

This field is solenoidal. Its vorticity lies in the meridional plane,
whereas (omega dot grad)V_0 is azimuthal. Hence pointwise

$$
 V_0\cdot\omega_{V_0}=0,\qquad
 \omega_{V_0}\cdot((\omega_{V_0}\cdot\nabla)V_0)=0.
$$

For a direct Cartesian check, write V_0=f(-xi2,xi1,0). Then
omega_h=-(xi1,xi2) f_{xi3}; its inner product with both
(-xi2,xi1) and (-omega2,omega1) vanishes. This proves both assertions.

Translate V_0 to the ball of radius one about x_V=(3,0,0), and call it V.
Near x_V it is exactly (-xi2,xi1,0), with constant vorticity 2 e3. Define

$$
 e_V=E(V)>0,\quad y_V=Y(V)>0,\quad z_V=Z(V)>0,
 \qquad c=y_V/e_V,\qquad \kappa=(z_V-cy_V)/e_V\ge0.             \tag{3}
$$

The last inequality follows from Y(V)^2 <= E(V) Z(V), by integration by
parts and Cauchy--Schwarz. No unknown solution norm enters these constants.

## 3. No coercive scale-invariant two-scalar Lyapunov function

### Theorem A

Fix nu>0. There is no C1 function F:(0,infinity)^2 -> R satisfying all of:

1. F(E/lambda,lambda Y)=F(E,Y) for every lambda>0;
2. writing F(E,Y)=Phi(EY), one has Phi(q)->infinity as q->infinity;
3. F(E(u(t)),Y(u(t))) is nonincreasing along every classical whole-space
   NS solution from solenoidal Schwartz data, even just on its initial
   local existence interval.

Viscosity-dependent choices F_nu are also excluded, for each fixed nu.

**Why this candidate would close NS-R3.** Sobolev interpolation gives

$$
 \|u\|_3\le\|u\|_2^{1/2}\|u\|_6^{1/2},\qquad
 \|u\|_3^4\le C E(u)Y(u).                                  \tag{4}
$$

Coercivity and monotonicity would bound EY from its initial value through
Phi's sublevel set. Equation (4) and CONTINUATION would then exclude a finite
maximal time; LOCAL and ENERGY give the rest of the terminal theorem.

**Proof of the obstruction.** Scale invariance forces
F(E,Y)=F(1,EY)=Phi(EY). For u(0)=B W, LOCAL gives an actual classical NS
solution, and (1) at time zero gives, with Q=EY,

$$
 Q(0)=B^4ey,\qquad
 Q'(0)=2B^5e\sigma-2\nu B^4(ez+y^2).                        \tag{5}
$$

This derivative is positive for every

$$
 B>\nu(ez+y^2)/(e\sigma).
$$

As B varies above that threshold, Q(0) ranges over an entire positive
half-line. Monotonicity would therefore imply Phi'(q)<=0 at every q on
that half-line. Phi is then nonincreasing on a tail, contradicting its
coercivity. This proves Theorem A.

This uses actual NS solutions, not the comparison curve below. It does
not exclude nonmonotone a priori estimates, time-dependent functionals,
functionals involving additional spatial information, or small-data
monotonicity. In particular it is not a no-go theorem for all Lyapunov
approaches. It rules out the complete precisely stated two-scalar class.

## 4. Exact energy AND exact enstrophy with a strong L2 endpoint

### Theorem B

For every fixed nu>0 there exist a finite T>0 and a single curve
b in C-infinity(R3 x [0,T)) such that:

- Each slice is compactly supported and solenoidal; all supports lie in
  one fixed compact set, and b(0) is one fixed Schwartz datum.
- With E=E(b), Y=Y(b), Z=Z(b), S=S(b), BOTH equations (1) hold exactly.
  The stretching S is that of b itself, not a prescribed independent scalar.
- b extends strongly continuously in L2 to time T; its endpoint is a
  smooth compactly supported nonzero field. The global energy equality
  holds at T as well, and the total viscous dissipation is finite.
- Nevertheless ||b(t)||_3 -> infinity and Y(t) -> infinity as t increases
  to T. The total helicity is zero at every time.
- With the canonical NS pressure, its vector residual is divergence free,
  orthogonal in L2 to both b and -Delta b, and nonzero. Thus b is NOT a
  solution of the original unforced NS equation, for any pressure choice.

### 4.1 Ansatz and the two exact scalar equations

Introduce a positive scalar D, to be sent to infinity, and set

$$
 r(D)=D^{-2/3},\qquad d(D)=y-ceD^{-4/3},
$$

$$
 a(D)^2=\frac{D^{5/3}}{d(D)},\qquad
 P(D)=e a(D)^2r(D)^3=\frac{eD^{-1/3}}{d(D)}.                 \tag{6}
$$

Here P denotes the pulse's kinetic energy, NOT its pressure. Take D0 so
large that d(D)>y/2 for all D>=D0 and the support of W(x/r(D)) lies in B1.
It is then disjoint from V. Let E be a second scalar variable, and set

$$
 B(D,E)^2=\frac{E-P(D)}{e_V},\qquad
 b(x,t)=a(D(t))W(x/r(D(t)))+B(D(t),E(t))V(x).                \tag{7}
$$

In the region E>P(D), take the positive square roots. Disjointness and
changes of variables give the exact reconstructions

$$
 E(b)=E,\qquad Y(b)=D+cE,
$$

$$
 Z(b)=\frac{zD^{7/3}}{d(D)}+z_V B^2,\qquad
 S(b)=\frac{\sigma D^{5/2}}{d(D)^{3/2}}.                    \tag{8}
$$

For example, the pulse contribution to Y-cE is

$$
 a^2(yr-ce r^3)=a^2 r d(D)=D.
$$

The reservoir contributes zero stretching. Evolving D,E by

$$
 E'=-2\nu(D+cE),                                           \tag{9}
$$

$$
 D'=\frac{2\sigma D^{5/2}}{d(D)^{3/2}}
 -2\nu\left\{\frac{zD^{7/3}-cyD}{d(D)}
                  +\kappa(E-P(D))\right\}                 \tag{10}
$$

therefore makes (1) hold identically. Indeed, (10) is precisely
D'=2S-2nu(Z-cY), and Y'=D'+cE'=2S-2nuZ. This derivation also
checks the sign of the cY term; it is not an upper inequality.

### 4.2 Finite-time escape and a nonvanishing reservoir

Use initial conditions D(0)=D0 and E(0)=1. Put K=sigma/y^(3/2)>0.
Uniformly for E in [1/2,1], as D tends to infinity, the right side of (10)
is

$$
 D'=2K D^{5/2}(1+o(1)).                                    \tag{11}
$$

The viscous leading term has order D^(7/3), strictly smaller than
D^(5/2); d(D)->y, and the reservoir term is bounded. Increase D0 so that

$$
 K D^{5/2}\le D'\le 3K D^{5/2}                             \tag{12}
$$

throughout D>=D0, E in [1/2,1], and so that P(D0)<1/4. P is decreasing:

$$
 P'(D)=e\left[-\frac{D^{-4/3}}{3d(D)}
              -\frac{D^{-1/3}d'(D)}{d(D)^2}\right]<0,
 \qquad d'(D)=\frac43ceD^{-7/3}>0.                         \tag{13}
$$

While E>=1/2, (9), (12), and E<=1 give the total possible energy loss
before D reaches infinity as at most

$$
 \frac{2\nu}{K}\int_{D_0}^{\infty}(D+c)D^{-5/2}\,dD
 =\frac{4\nu}{K}D_0^{-1/2}
   +\frac{4\nu c}{3K}D_0^{-3/2}.                           \tag{14}
$$

Choose D0 still larger so this is less than 1/4. By a first-exit argument
E can never reach 3/4, much less 1/2. Hence E>P(D), B is bounded above and
away from zero, and the ODE cannot leave its smooth domain at finite D.
Inequality (12) forces D to infinity at a finite time T, with

$$
 T\le\frac{2}{3K}D_0^{-3/2},\qquad
 D(t)\asymp(T-t)^{-2/3},\qquad E(t)\longrightarrow E_*\ge3/4.
                                                               \tag{15}
$$

The two-sided rate follows by integrating 1/D' from D(t) to infinity.
Every constant is fixed by the chosen profiles and nu; no endpoint
solution norm is used to define the construction.

### 4.3 Critical divergence without any loss of L2 energy

Equations (6), (15) yield

$$
 a\asymp D^{5/6},\quad r=D^{-2/3},\quad
 P(D)\asymp D^{-1/3}\longrightarrow0.
$$

The pulse tends to zero in L2, and the reservoir tends to
B_*V, where B_*=(E_*/e_V)^(1/2). Therefore

$$
 b(t)\longrightarrow B_*V\quad\hbox{strongly in }L^2.       \tag{16}
$$

This gives a continuous L2 curve on the compact interval [0,T], so its
image is L2-precompact. The energy densities also converge strongly in L1;
there is no concentrated energy atom at the endpoint. Passing to T in the
integrated form of (9) gives

$$
 E_*+2\nu\int_0^T Y(b(t))\,dt=1.                          \tag{17}
$$

On the other hand, disjoint supports give

$$
 \|b(t)\|_3^3
 =(ar)^3\|W\|_3^3+B^3\|V\|_3^3,
 \qquad ar=\frac{D^{1/6}}{\sqrt{d(D)}}.
$$

Consequently

$$
 \|b(t)\|_3\asymp D^{1/6}\asymp(T-t)^{-1/9}\to\infty,
 \qquad Y(b(t))\asymp D\to\infty.                         \tag{18}
$$

In particular integral_0^T Y is finite whereas integral_0^T Y^2 is
infinite. Unlike the earlier power-law countermodel, these behaviors now
coexist with the EXACT spatial stretching identity in (1).

Helicity vanishes because the two profiles have zero helicity, scaling
preserves zero, and disjoint support eliminates cross terms.

### 4.4 The vector residual and why no pressure repairs it

Let p_b=sum_ij R_i R_j(b_i b_j) be the usual decaying pressure and define

$$
 f=b_t+(b\cdot\nabla)b+\nabla p_b-\nu\Delta b.             \tag{19}
$$

This is a smooth divergence-free residual on each compact time interval.
The pressure definition makes its divergence zero. Compact support of b
and the usual pressure decay justify the global integrations below.
Equations (1) give exactly

$$
 \langle f,b\rangle=\tfrac12 E'+\nu Y=0,
$$

$$
 \langle f,-\Delta b\rangle
       =\tfrac12 Y'+\nu Z-S=0.                            \tag{20}
$$

Nevertheless f is nonzero. Since B^2=(E-P(D))/e_V,

$$
 e_V(B^2)'=-2\nu(D+cE)-P'(D)D'.                           \tag{21}
$$

Using (11), (13),

$$
 -P'(D)D'=\frac{2eK}{3y}D^{7/6}(1+o(1)).                 \tag{22}
$$

This eventually dominates the order-D negative term in (21). Thus B'>0
near T. At the centre x_V of the reservoir, and throughout a fixed small
neighborhood of it,

$$
 b=B(t)(-\xi_2,\xi_1,0),\qquad \omega_b=2B(t)e_3.
$$

There the vorticity has no spatial derivatives, and
(omega_b dot grad)b=0. The curl of (19) at x_V is therefore

$$
 (\nabla\times f)(x_V,t)=2B'(t)e_3\ne0                    \tag{23}
$$

near T. A pressure gradient has zero curl, so no different pressure can
make b an unforced NS solution. This conclusion is independent of any
unproved regularity or uniqueness theorem. It completes Theorem B.

## 5. The exact compactness inference that fails

Let R_W contain the support of W and take R_W r(D)<1. The reservoir is
outside the ball B_(R_W r(D))(0). Its pulse energy in that ball is P(D).
Consequently

$$
 \int_{B_{R_W r(D)}}|b|^2=P(D)\asymp r(D)^{1/2}\to0,
$$

but

$$
 \frac{1}{R_W r(D)}\int_{B_{R_W r(D)}}|b|^2
 \asymp r(D)^{-1/2}\longrightarrow\infty.                  \tag{24}
$$

Thus strong L2 convergence, even to a smooth endpoint with no energy
loss and with fixed compact spatial support, does not supply the rate
needed to make critical local energy small. Qualitative uniform
integrability is not a critical Morrey bound. This statement does not
claim that a single local energy bound is by itself a complete NS
regularity criterion; it falsifies the attempted rate conversion before
such a criterion can even be applied.

## 6. Disposition and what must not be claimed

Retire the universal coercive C1 scale-invariant F(E,Y) monotonicity route.
Retire scalar closure arguments using only the two exact global balances,
solenoidality, the associated spatial identities, fixed positive viscosity,
one fixed smooth input, finite physical time and energy-level compactness.
Those premises admit the countermodel in Theorem B. Merely adding the exact
integrated vortex-stretching identity or strong L2 continuity cannot repair
that inference.

Do NOT retire pointwise strain/vorticity evolution, the full momentum
equation, local energy transport, or genuinely spatial mechanisms on this
basis. Theorem B fails the original vector equation and has no established
local NS energy inequality. It supplies no information ruling out a
successful argument using those additional premises. It also does not
falsify any actual fixed-input intrinsic-tangent selection theorem.

A future closure proposal must identify the specific spatial evolution
consequence it proves and why that consequence reaches the terminal
suffix. Saying only that the equation residual vanishes is the original
problem, not a smaller remaining theorem. Likewise, introducing another
uncontrolled strain, flux, or compactness norm is not a reduction.

No terminal estimate, strictly weaker terminal obligation, independent
audit, formal result, or manuscript integration is claimed. These are
architectural falsifications, not a solution of NS-R3.

## 7. Attribution and author checks

The periodic positive-stretching snapshot is already in the frozen PLAN,
Section 5. Its vector-potential cutoff, reflection, the whole-space
Lyapunov obstruction, and the two-component ODE construction are derived
above. Concentration ansatzes have a long history; no priority claim is
made for the use of a rescaled profile. This is not a solution of a Leray
self-similar profile equation.

Relevant primary-source context, not imported proofs of these statements:

- E. Miller, *Finite-time blowup for a Navier--Stokes model equation for
  the self-amplification of strain*, arXiv:1910.05415; Analysis & PDE 16
  (2023), no. 4. Its abstract records finite-time blowup of a different
  strain model sharing the NS enstrophy identity and strain constraint
  space. This note does not claim to discover that enstrophy identity
  alone is insufficient.
- T. Tao, *Finite time blowup for an averaged three-dimensional
  Navier--Stokes equation*, arXiv:1402.0290. The averaged equation is not
  the original NS equation or the comparison curve constructed here.
- G. Koch, N. Nadirashvili, G. Seregin and V. Sverak, *Liouville theorems
  for the Navier--Stokes equations and applications*, arXiv:0709.3599.
  Ancient extraction does not by itself supply arbitrary-data rigidity.

The exact profile mean 1/4 and the algebraic energy/enstrophy
reconstructions were checked symbolically. The proof of blowup of the
comparison ODE uses the displayed analytic inequalities, not a numerical
integration. No PDE simulation or independent reviewer was used.

An independent audit should reconstruct the cutoff error, reflection
parities, the sign in (10), positivity of the reservoir throughout the
bootstrap, the exact exponent comparison in (11) and (22), and the curl
residual in (23). Structural repository checks are not mathematical audits.
