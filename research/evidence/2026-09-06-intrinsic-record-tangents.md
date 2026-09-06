# Intrinsic record tangents without an assumed critical bound

Date: 2026-09-06.
Status: complete author derivation; independent mathematical audit pending.
Scope: a blow-up extraction bridge, not a proof of NS-R3, not an endpoint
estimate, and not a manuscript theorem. No novelty or priority claim.

Input research revision: `c2c5f793d1e447a82dd99c7e434c76fc989ec316`.
Input manuscript revision: `81f0cd1524e8a625e6ee46970d69e40e5a2e50bf`.
The retained project inputs are LOCAL and ENERGY. In particular, LOCAL
supplies the smooth maximal branch, bounded spatial derivatives on compact
classical intervals, decay at spatial infinity, and the H1 blow-up
alternative. None of the quotient, defect, pressure-work, shell, or material
response hypotheses is used.

## 1. Why change the object?

The existing `compactness.md` correctly observes that a velocity-record
blow-up produces a nonzero bounded ancient mild solution, but that its limit
can be spatially constant. Original finite energy does not become a uniform
finite-energy bound after magnification. Adding an unproved critical norm to
repair that loss would repeat the old endpoint problem.

Here the normalized object is a velocity **increment**, in a frame moving
with a local spatial mean. Its global Holder seminorm is bounded by the
record selection itself, not by an a priori estimate. Nonconstancy therefore
survives compactness. The price is a possibly vanishing effective viscosity.
That price must not be hidden: the Euler branch is genuine and the companion
`2026-09-06-viscous-mixing-falsifier.md` rules out several tempting rigidity
claims about it.

This moving-frame subtraction is not the project's cubic gradient quotient.
It removes spatially constant velocities. Its acceleration is retained
explicitly in the equation.

## 2. Bridge theorem

Fix $0<\alpha<1/2$, a viscosity $\nu>0$, and a smooth, nonnegative, radial
function $\phi$ supported in $B_1$, with $\int\phi=1$. Write

$$
 [f]_\alpha=\sup_{x\ne y}\frac{|f(y)-f(x)|}{|y-x|^\alpha},
 \qquad \langle f\rangle_\phi=\int\phi(y)f(y)\,dy.
$$

Suppose the selected Schwartz-data classical branch has $T_*<\infty$.
Then there are record times $t_n\uparrow T_*$, pairs $(x_n,y_n)$, and
positive numbers

$$
 h_n=[u(t_n)]_\alpha,\quad r_n=|y_n-x_n|,\quad
 A_n=|u(y_n,t_n)-u(x_n,t_n)|=h_nr_n^\alpha,
 \quad e_n=(y_n-x_n)/r_n
$$

with the following properties.

1. $h_n\to\infty$, $r_n\to0$, and
   $[u(t)]_\alpha\le h_n$ for $0\le t\le t_n$.
2. For all sufficiently large $n$,

   $$
   \mathcal R_n=\frac{A_nr_n}{\nu}\ge c_\alpha>0.
   $$

   The constant depends only on $\alpha$, $\phi$, and the dimension, not on
   an unknown endpoint norm. In particular, $A_n\to\infty$.
3. Define $X_n$ backwards from $X_n(t_n)=x_n$ by

   $$
   \dot X_n(t)=c_n(t)
       :=\int\phi(z)u(X_n(t)+r_nz,t)\,dz.
   $$

   Set

   $$
   v_n(y,s)=\frac{u(X_n(t)+r_ny,t)-c_n(t)}{A_n},\qquad
   t=t_n+\frac{r_n}{A_n}s,
   \quad \mu_n=\frac{\nu}{A_nr_n},\quad S_n=\frac{t_nA_n}{r_n}.
   $$

   On $[-S_n,0]$, these fields satisfy

   $$
   \langle v_n\rangle_\phi=0,\qquad [v_n(s)]_\alpha\le1,
   \qquad |v_n(e_n,0)-v_n(0,0)|=1,
   $$

   and

   $$
   |v_n(y,s)|\le C_\phi(1+|y|^\alpha).
   $$

   Both backward domain lengths diverge:

   $$
   S_n\longrightarrow\infty,\qquad
   \mu_n S_n=\frac{\nu t_n}{r_n^2}\longrightarrow\infty.
   $$

   Also $[v_n(-S_n)]_\alpha=[u_0]_\alpha/h_n\to0$.
4. After a subsequence, $\mu_n\to\mu\in[0,c_\alpha^{-1}]$,
   $e_n\to e\in S^2$, and $v_n\to v$ locally uniformly on
   $\mathbb R^3\times(-\infty,0]$. Convergence is also uniform in time in
   local spatial $C^\beta$ for every $0<\beta<\alpha$. The limit satisfies

   $$
   \langle v(s)\rangle_\phi=0,\quad [v(s)]_\alpha\le1,
   \quad |v(e,0)-v(0,0)|=1.
   $$

   With the canonical pressure modulo constants specified below, it solves

   $$
   \partial_s v=F_\mu(v)-\langle F_\mu(v)\rangle_\phi,
   \quad F_\mu(v)=\mu\Delta v-\nabla\!\cdot(v\otimes v)
                          -\nabla\mathcal P[v],\quad \nabla\cdot v=0.
   $$

   Thus the alternative is a nonconstant ancient positive-viscosity
   centred Navier--Stokes solution, or a nonconstant ancient centred Euler
   solution. The first is not automatically in the globally bounded mild
   class of the classical KNSS theorem.
5. If $1/3<\alpha<1/2$ and $\mu=0$, the Euler limit obeys local energy
   conservation, with the frame acceleration included. Moreover,

   $$
   \mu_n|\nabla v_n|^2\,dy\,ds\ \longrightarrow\ 0
   $$

   against compactly supported test functions in
   $\mathbb R^3\times(-\infty,0)$. This is a local assertion, not a claim
   of global finite energy or global energy conservation for $v$.

The interval $(1/3,1/2)$, for example $\alpha=2/5$, combines an integrable
pressure/Stokes tail with the local energy-conservation commutator estimate.
No bound on the original Holder seminorm is asserted.

## 3. Records, shrinking scales, and the two backward domains

Put $E_0=\|u_0\|_2^2$. A standard ball argument, included here, gives

$$
 \|u(t)\|_\infty
 \le C_\alpha E_0^{\alpha/(2\alpha+3)}
                  [u(t)]_\alpha^{3/(2\alpha+3)}.                 \tag{1}
$$

Indeed, near a point of speed $M=\|u(t)\|_\infty$, the speed is at least
$M/2$ on a ball of radius comparable to $(M/[u(t)]_\alpha)^{1/\alpha}$.
Integrating its square and using ENERGY proves (1), also by approximation
if a maximum is not attained. The zero-seminorm case follows from finite
energy: a spatial constant in $L^2(\mathbb R^3)$ is zero.

If $[u(t)]_\alpha$ were bounded on $[0,T_*)$, (1) would bound
$\|u(t)\|_\infty$. With $Y=\|\nabla u\|_2^2$ and
$Z=\|\Delta u\|_2^2$, direct enstrophy testing gives

$$
 Y'+\nu Z\le\nu^{-1}\|u\|_\infty^2Y.
$$

Gronwall would contradict LOCAL's finite-time H1 blow-up alternative.
Thus the seminorm is unbounded. It is continuous on every compact
classical interval: uniform $C^1$ continuity and
$[f]_\alpha\le C\|f\|_\infty^{1-\alpha}\|\nabla f\|_\infty^\alpha$
suffice. Choose first hitting times of levels tending to infinity.

At each such time, the Holder quotient attains its positive supremum.
For separations tending to zero this follows from the bounded gradient;
for separations tending to infinity it follows from bounded velocity.
For bounded, nonzero separations with both points escaping to infinity,
velocity decay makes the quotient tend to zero. A maximizing sequence
therefore has a convergent subsequence with distinct endpoints.

At least one of the maximizing endpoints has speed at least $A_n/2$.
On a ball of radius $4^{-1/\alpha}r_n$ about it, the record bound makes
the speed at least $A_n/4$. Consequently

$$
 E_0\ge c_\alpha A_n^2r_n^3
          =c_\alpha h_n^2r_n^{2\alpha+3}.                       \tag{2}
$$

It follows that $r_n\to0$. Before proving Reynolds noncollapse, one
already has

$$
 A_n/r_n=h_nr_n^{\alpha-1}\longrightarrow\infty.
$$

Since $t_n\to T_*>0$, this proves both $S_n\to\infty$ and
$\nu t_n/r_n^2\to\infty$. The ODE for $X_n$ exists on the whole compact
interval $[0,t_n]$: its vector field is smooth and bounded there.

Subtracting its defining mean proves

$$
 v_n(y,s)=\int\phi(z)
   \frac{u(X_n(t)+r_ny,t)-u(X_n(t)+r_nz,t)}{A_n}\,dz.
$$

The record inequality now gives the claimed uniform growth bound and
mean normalization. Subtracting two values gives the seminorm bound and
preserves the terminal unit increment.

Under Navier--Stokes scaling, $h$ scales by $\lambda^{1+\alpha}$,
$A$ by $\lambda$, $r$ by $\lambda^{-1}$, and time by
$\lambda^{-2}$. In particular $\mathcal R$, $S$, $\mu S$, and the
normalized assertions above are invariant. The two diverging backward
lengths are proved domain properties, not assumed bounds on a new clock.

## 4. Canonical pressure and the acceleration term

Let $\chi_R$ be a smooth radial cutoff equal to one on $B_R$, supported
in $B_{2R}$. For a solenoidal $v$ with the displayed growth and Holder
bounds, define

$$
 \mathcal P_R[v](y)
 =\sum_{i,j}R_iR_j(\chi_Rv_iv_j)(y)
  -\sum_{i,j}R_iR_j(\chi_Rv_iv_j)(0).
                                                               \tag{3}
$$

Here $R_iR_j$ is the full double-Riesz operator, including its local
term; no local term of its kernel is dropped. Near a point, the usual
principal value is defined by the positive Holder exponent. If $y$ is
in a fixed ball and $z$ is far from that ball, the difference between
the two kernels in (3) is bounded by $C|y||z|^{-4}$. Hence the omitted
far tail is bounded by

$$
 C|y|\int_R^\infty \rho^{-4}(1+\rho^{2\alpha})\rho^2d\rho
 \le C|y|(R^{-1}+R^{2\alpha-1})\longrightarrow0.                \tag{4}
$$

Thus (3) converges locally to a canonical pressure $\mathcal P[v]$ with
$\mathcal P[v](0)=0$. The same decomposition, with a cutoff fixed around
any prescribed compact ball, gives uniform local $C^\beta$ pressure
bounds for $0<\beta<\alpha$. The near part is the ordinary
Calderon--Zygmund Holder estimate; the far part is uniformly Lipschitz
by (4). It also proves local continuity of this pressure construction
under locally uniform convergence and uniform Holder/growth bounds:
first fix the far cutoff, use strong local $C^\beta$ convergence with a
slightly larger exponent, and then send the cutoff to infinity.

For each prelimit field this is the physical normalized pressure,
modulo a spatial constant. Subtracting a constant velocity changes
$v_iv_j$ only by constant and cross terms. The double divergence of the
cross terms is zero because the unshifted velocity is solenoidal; in
the original decaying finite-energy class this can also be checked by
Fourier transformation. Their pressure gradient is zero. Formula (4)
fixes the extension to the centred field. An arbitrary harmonic
quadratic pressure is not available as an extra degree of freedom.

A direct chain rule in the moving frame gives

$$
 \partial_s v_n+v_n\cdot\nabla v_n+\nabla\mathcal P[v_n]
 =\mu_n\Delta v_n-\frac{r_n}{A_n^2}\dot c_n(t).                 \tag{5}
$$

Differentiate $\langle v_n\rangle_\phi=0$ in (5). If

$$
 a_n(s)=\langle F_{\mu_n}(v_n)\rangle_\phi,
$$

then $r_n\dot c_n/A_n^2=a_n$. Thus (5) is exactly

$$
 \partial_s v_n=F_{\mu_n}(v_n)-a_n.
                                                               \tag{6}
$$

Equivalently the total pressure is $\mathcal P[v_n]+a_n(s)\cdot y$.
This linear pressure records the known frame acceleration; it is not
silently discarded or used to choose an arbitrary new solution.

## 5. Reynolds noncollapse: an input-independent bridge

Use the same moving spatial frame but the diffusive time coordinate
$t=t_n+(r_n^2/\nu)\tau$. Denote the resulting field by $w_n$. Then

$$
 \partial_\tau w_n-\Delta w_n
 =-\mathcal R_n\mathbb P\nabla\cdot(w_n\otimes w_n)-b_n(\tau), \tag{7}
$$

where $b_n$ is spatially constant. Every term is smooth on the compact
prelimit interval. The same mean, growth, seminorm, and terminal
increment bounds hold. No estimate on $b_n$ is needed in this step.

The Stokes derivative kernel in dimension three satisfies

$$
 |K_{ijk}(z,\tau)|\le C(|z|^2+\tau)^{-2},\qquad \tau>0.         \tag{8}
$$

This is the kernel estimate in KNSS, equation (3.7); its representation
formula is their (3.5). The weighted extension needed here follows
directly from (8): changing variables $z=\sqrt\tau\,\zeta$ yields

$$
 \int |K(z,\tau)|(1+|z|^{2\alpha})dz
 \le C_\alpha(\tau^{-1/2}+\tau^{\alpha-1/2}).                  \tag{9}
$$

The moment integral at infinity is finite exactly for the range
$2\alpha<1$ used here. Thus all the convolutions below converge
absolutely under the uniform growth bound, even though that bound is
not an unweighted global $L^\infty$ bound for the limiting class.
For each fixed $n$, the original smooth bounded velocity and the
spatial constant subtraction also justify the usual Duhamel formula.

Apply (7) on $[-L,0]$ and take the difference of its values at $e_n$
and $0$. The integral of $b_n$ cancels exactly. The linear term obeys

$$
 |(e^{L\Delta}w_n(-L))(e_n)-(e^{L\Delta}w_n(-L))(0)|
 \le C_\alpha L^{(\alpha-1)/2}.                               \tag{10}
$$

To check (10), subtract a constant inside the convolution with
$\nabla G_L$ and integrate $|z|^\alpha|\nabla G_L(z)|$.
For the nonlinear term, use $|w_n(z,\tau)|^2\le C(1+|z|^{2\alpha})$
at each of the two bounded observation points, followed by (9).
This gives the concrete inequality

$$
 1\le C_\alpha L^{(\alpha-1)/2}
       +C_\alpha\mathcal R_n
            (L^{1/2}+L^{\alpha+1/2}).                         \tag{11}
$$

First choose one fixed $L=L_\alpha\ge1$ so that the first term is at
most $1/2$. This interval is available for every sufficiently large
$n$, because its full diffusive backward length is
$\nu t_n/r_n^2\to\infty$. Now (11) yields

$$
 \mathcal R_n\ge
 \frac{1}{2C_\alpha(L_\alpha^{1/2}+L_\alpha^{\alpha+1/2})}
 =c_\alpha>0.                                                  \tag{12}
$$

This is not an assumed upper bound on a critical norm. It rules out
collapse to a purely caloric normalization at the selected increment
scale. It gives no upper bound on $\mathcal R_n$ and must not be read
as one. Combining (12) with $r_n\to0$ gives $A_n\to\infty$.

## 6. Compactness with no hidden harmonic pressure

By (12), $\mu_n$ is bounded. Fix a compact spatial ball and a finite
backward time interval. The growth and Holder bounds give uniform
local bounds on $v_n$ and $p_n=\mathcal P[v_n]$. Pairing (6) with
$\phi$ and integrating derivatives onto $\phi$ bounds $a_n$ uniformly:
its three terms involve $\mu_nv_n\Delta\phi$,
$(v_n\otimes v_n)\nabla\phi$, and $p_n\nabla\phi$.

Let $\eta_\varepsilon$ be a spatial mollifier. On a slightly smaller
ball, the equation gives

$$
 \|\partial_s(v_n*\eta_\varepsilon)\|_\infty
       \le C\varepsilon^{-2},\qquad
 \|v_n-v_n*\eta_\varepsilon\|_\infty\le C\varepsilon^\alpha.
$$

Consequently a time increment $d$ is bounded by
$C(\varepsilon^\alpha+|d|\varepsilon^{-2})$.
Taking $\varepsilon=|d|^{1/(\alpha+2)}$ proves a uniform time modulus.
Arzela--Ascoli and diagonal extraction give locally uniform convergence
on all finite cylinders, including the one-sided terminal trace $s=0$.
Spatial interpolation gives the claimed local $C^\beta$ convergence.

The pressure construction in Section 4 now gives $p_n\to p$ locally
uniformly. Pairing with $\phi$ also gives $a_n\to a$ on compact time
intervals, since the derivative terms have already been transferred to
$\phi$. Passing to distributions in (6) proves the centred limiting
equation. Strong convergence passes the nonlinear product; no Reynolds
stress is inserted without justification. The convergence $e_n\to e$
and the spatial modulus preserve the unit increment at $s=0$.

Neither global finite energy nor a global critical norm of $v$ has
been obtained. In particular, (2) is a lower bound on original energy
needed for the selected increment, not a uniform upper bound on the
energy of the normalized fields.

## 7. The inviscid limit has no local anomalous energy defect

Now choose $1/3<\alpha<1/2$ and suppose $\mu=0$. Write
$p=\mathcal P[v]$ and $a=\langle F_0(v)\rangle_\phi$.
The standard spatial-mollification argument is local here. For

$$
 \tau_\ell=(v\otimes v)_\ell-v_\ell\otimes v_\ell
$$

one has on compact cylinders

$$
 |\tau_\ell|\le C\ell^{2\alpha},\qquad
 |\nabla v_\ell|\le C\ell^{\alpha-1}.
$$

Testing the mollified Euler equation by $v_\ell$, the possible energy
flux defect is bounded by $C\ell^{3\alpha-1}\to0$. The other
commutator fluxes tend to zero locally as well. The acceleration is
spatially constant and contributes $-a\cdot v$. This proves

$$
 \partial_s\frac{|v|^2}{2}
 +\nabla\cdot\left[\left(\frac{|v|^2}{2}+p\right)v\right]
 =-a\cdot v.                                                   \tag{13}
$$

This is the Constantin--E--Titi commutator mechanism, applied locally;
no global integrability of $v$ is assumed.

Each smooth prelimit obeys, with $e_n=|v_n|^2/2$,

$$
 \partial_s e_n+\nabla\cdot[(e_n+p_n)v_n]
 =\mu_n\Delta e_n-\mu_n|\nabla v_n|^2-a_n\cdot v_n.
$$

For a smooth compactly supported scalar test function $\zeta$ in the
open ancient domain, integration by parts gives

$$
 \int\mu_n|\nabla v_n|^2\zeta
 =\int\left[e_n\partial_s\zeta
 +(e_n+p_n)v_n\cdot\nabla\zeta
 +\mu_ne_n\Delta\zeta-a_n\cdot v_n\zeta\right].               \tag{14}
$$

Every term on the right converges. By (13), its limit is zero.
The left sides are nonnegative measures for nonnegative tests, so
(14) proves the local vanishing assertion in the theorem. It does not
bound original dissipation on all rescaled space-time, or on intervals
whose lengths tend to infinity with $n$.

## 8. What the bridge does and does not buy

The old constant-tangent obstruction is removed, without assuming
$L^\infty_tL^3_x$, a Morrey upper bound, a strain clock, or an endpoint
compactness theorem. A second normalization failure, vanishing local
Reynolds number, is excluded by a complete kernel argument. This is a
necessary structural bridge from a putative singularity, not a new
conditional continuation criterion.

The following attempted suffixes fail.

- Finite-energy inheritance: before subtracting a mean, normalized total
  energy is bounded only by $E_0/(A_n^2r_n^3)$, which need not be bounded.
  After mean subtraction, the field need not even be globally in $L^2$.
- Positive local anomalous dissipation in the Euler branch: for the
  chosen exponent, Section 7 proves the opposite on every fixed compact
  cylinder. An unproved positive lower bound would itself require new
  structure; it cannot be supplied by the word "singularity".
- Universal intrinsic ancient rigidity: $v=(f(y_2),0,0)$ is a stationary
  Euler solution for any smooth bounded $f$. Subtract its $\phi$-mean
  and normalize a maximizing Holder increment. It satisfies the
  normalized mean, seminorm, nonconstancy, canonical-pressure, and
  local energy-conservation requirements simultaneously.

The companion mixing note goes further: even record normalization,
vanishing normalized initial seminorm, and both diverging backward
domain lengths can accompany such a steady Euler limit in a family of
smooth globally regular viscous flows. Therefore a new terminal
argument must retain information about **one fixed whole-space input
at one fixed positive viscosity and a finite physical endpoint**.
These conditions are not replaced here by a named unproved compactness
axiom. No such terminal reachability theorem has been proved in this run.

## 9. Author checks and required independent audit

The derivation was checked for the direction of the enstrophy implication,
the energy exponents in (1)--(2), attainment of the Holder quotient,
all space/time scaling factors, cancellation of the frame acceleration
only in increments, the pressure gauge and tail exponent, the order
of choosing $L$ in (11), the distinction between a lower and an upper
Reynolds bound, time compactness without assuming velocity derivatives,
and the sign in the tested energy identity (14).

An independent audit must in particular reconstruct the canonical
pressure/physical-pressure identification, the weighted Duhamel
formula in the accelerating frame, and passage to the local energy
identity. The note is not an independent audit of itself. No Lean
build, PDE numerical verification, or terminal graph-node promotion
is claimed.

## Sources and attribution

- Project LOCAL and ENERGY at the input research revision; see
  `docs/proof-graph.yaml`. The earlier velocity-record obstruction is
  in `research/evidence/compactness.md` at the same revision.
- G. Koch, N. Nadirashvili, G. Seregin, V. Sverak, *Liouville theorems
  for the Navier--Stokes equations and applications*, arXiv:0709.3599.
  Author PDF: https://www-users.cse.umn.edu/~sverak/publications/liouville.pdf .
  Equations (3.5), (3.7), and the discussion around Proposition 6.1
  were inspected, including the rendered kernel page. The weighted
  moment calculation and the present normalization are derived above.
- G. Seregin, *Remarks on Type II blowups of solutions to the
  Navier--Stokes equations*, arXiv:2304.04045v1. Its Euler-scaling
  construction requires additional hypotheses stated in Proposition
  1.2; that proposition is not imported as an arbitrary-data producer.
- P. Constantin, W. E, E. S. Titi, *Onsager's conjecture on the energy
  conservation for solutions of Euler's equation*, Commun. Math. Phys.
  165 (1994), 207--209, DOI 10.1007/BF02099744. Attribution for the
  commutator mechanism; the local estimate needed here is displayed.
- A. V. Gavrilov, *A steady Euler flow with compact support*,
  arXiv:1810.08020v1. In addition to the explicit shear above, this
  construction shows why simply asking for a finite-energy Euler
  representative cannot make a blanket Euler Liouville theorem true.

A focused source check is not an exhaustive novelty search. No
unverified recent claimed regularity or axisymmetry-reduction theorem
is used as a premise.
