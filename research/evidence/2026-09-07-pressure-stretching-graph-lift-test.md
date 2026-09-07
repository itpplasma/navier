# Pressure--stretching graph lift: the finite-contact implementation fails

Date: 2026-09-07.
Inspected remote base: `a55d0e9cba1d6b31cc297f2b10312777d0317bc4`.
Status: author derivation; no independent mathematical audit or novelty claim.
NS-R3 is NOT PROVED. No strict singularity reduction is claimed.
Outcome: a rigorous obstruction to the specific deterministic graph-lift
implementation tested here, NOT to every geometric or metriplectic approach.
This file is a standalone working result, not a promoted proof-graph node.

## 1. The attempted decisive step and its boundary

The proposed producer was to turn the pressure--stretching formulation into
an exact positive transport/diffusion lift, and then exclude its undamped
concentration support by finite Hamiltonian contact. The contemplated terminal
chain was:

    hypothetical finite NS singularity
      -> nonzero critically normalized defect
      -> transported defect supported in an undamped set
      -> finite-contact exclusion of that support
      -> contradiction.

The last implication is elementary once its hypotheses are true. The second
and third arrows are not supplied by calling a lift symplectic. This attempt
tests an explicit candidate: the graph of finitely many actual NS observables,
starting with Z=(omega, grad(u) omega), and a positive local diffusion on the
lifted space. Its central finite-contact property is proved IMPOSSIBLE below.

The limitation is important. A genuine concentration defect, after removing
the singularities introduced merely by representing a smooth function as a
Dirac graph, is not covered by the obstruction. No propagation/annihilation
law for such a genuine critical defect was obtained in this attempt.

Keep the original unforced equation on R3, one fixed nu>0, and the selected
classical mild branch of a divergence-free Schwartz datum. All calculations
below are on compact subintervals of its smooth lifespan. No force, averaged
model, modified viscosity, independent pressure Hessian, or prescribed strain
trajectory is inserted. LOCAL and the canonical pressure convention are as
recorded in the inspected repository.

## 2. The exact pressure--stretching system

Set G_ij=partial_j u_i, omega=curl u, sigma=G omega, P=Hess p, and

    L=partial_t+u.grad_x-nu Delta_x.

Differentiating the actual equation and taking its curl give

    LG=-G^2-P,       L omega=G omega=sigma.

The second-order product rule gives

    L sigma=(LG)omega+G(L omega)
                         -2nu sum_k (partial_k G)(partial_k omega).

The G^2 omega terms cancel. Thus, writing

    C=sum_k (partial_k G)(partial_k omega),
    A(P)=[[0,I],[-P,0]],       R=(0,-2nu C),

one obtains exactly

    LZ=A(P)Z+R,              Z=(omega,sigma).                  (2.1)

P is the actual canonical Hessian, with

    -Delta p=tr(G^2),   p=sum_ij R_i R_j(u_i u_j).

Symmetry of P makes A(P)^T J+J A(P)=0 for J=[[0,I],[-I,0]]. The inviscid
block has Hamiltonian (|sigma|^2+omega.P omega)/2. The inviscid identity is
established background [S1, equations (3)--(6)], not a new regularity theorem.
Neither this Hamiltonian nor its time-dependent pressure potential has been
shown positive or bounded. The viscous term R is NOT optional.

Under the same-viscosity NS change of scale

    u^(r)(y,s)=r u(x0+r y,t0+r^2 s),

G and omega acquire factor r^2, sigma and P factor r^4, and C factor r^6.
Both L sigma and P omega acquire factor r^6 as well. Hence the omitted viscous
correlation would be of LEADING order at the critical scaling, not a smaller
error justified merely by approaching a singularity.

## 3. The exact distributional lift has a negative value-space term

Define the local distribution

    rho(t,x,z)=delta(z-Z(t,x)),    z in R^6,
    B_ab(t,x)=sum_k partial_k Z_a partial_k Z_b.

All identities are tested locally in (t,x,z); no finite total mass of dx is
assumed. B is positive semidefinite. Write F(t,x,z)=A(P(t,x))z+R(t,x), so
F(t,x,Z)=LZ. Direct differentiation of the Dirac graph yields

    L rho+div_z(F rho)=-nu sum_ab partial_(z_a)partial_(z_b)(B_ab rho).
                                                                  (3.1)

For example,

    Delta_x rho=-(Delta_x Z_a)partial_(z_a)rho
                        +B_ab partial_(z_a)partial_(z_b)rho.

This proves the sign in (3.1). Equivalently, for every smooth value test psi,

    L[psi(Z)]=Dpsi(Z).F(t,x,Z)-nu D2psi(Z):B.                 (3.2)

The right side of (3.1) is not a positive Fokker--Planck diffusion in z.
This does not contradict physical spatial diffusion: diffusion smooths a
field, while the distribution of its values can concentrate.

**Proposition 1.** Wherever grad_x Z is nonzero, rho cannot satisfy a forward
Fokker--Planck equation with the SAME spatial drift u and spatial diffusion
nu Delta_x, no mixed x/z diffusion, any smooth value drift beta, and an
additional positive semidefinite value-diffusion matrix D:

    L rho+div_z(beta rho)=sum_ab partial_(z_a)partial_(z_b)(D_ab rho).
                                                                  (3.3)

Proof. At a point (t0,x0), take psi equal to |z-Z(t0,x0)|^2/2 near the graph
value, with a compact cutoff outside that neighborhood. Its gradient at the
value is zero and its Hessian is I. Equation (3.2) gives

    L[psi(Z)](t0,x0)=-nu |grad Z(t0,x0)|^2<0.

The moment equation of (3.3) instead gives tr D(t0,x0,Z)>=0. The drift cannot
repair this because Dpsi=0 at that point. Contradiction. Localizing in x
makes the same argument an ordinary distributional test. QED.

This proposition excludes only the stated block-diffusion lift. Mixed
spatial/value diffusion is allowed in the next section and explicitly tested;
its absence is not silently imposed on every possible positive lift.

### An actual compact-data NS calibration

Let v2(x,y,z)=(y^2,0,xy), a homogeneous divergence-free quadratic field, and
let chi be compact smooth and equal to one near the origin. Define

    u0=curl[-(1/4)chi(x) x cross v2(x)].

The identity curl[-x cross v2/4]=v2 shows that u0=v2 near zero; u0 is compact,
smooth, and solenoidal. LOCAL gives its actual unforced solution at every
fixed nu>0. Near zero at its initial time,

    G=[[0,2y,0],[0,0,0],[y,x,0]],
    omega=(x,-y,-2y),      sigma=(-2y^2,0,0),
    C=(-2,0,0),            |grad omega|^2=6.

At the origin, omega=sigma=G=0, but L sigma=(4nu,0,0). The canonical
pressure is the one produced by u0; its contribution P omega vanishes there
without choosing P. In particular, with psi(z)=|z_omega|^2/2 near zero,

    L[psi(Z)](0,0)=-6nu.

This is an actual local NS calculation, not an affine infinite-energy
solution or a force prescription. Nonzero grad omega persists for a short
positive interval, so Proposition 1 also applies strictly after the initial
time, by centering the test at the value at any such point. The example is
not a singular solution and does not refute any NS continuation theorem.

## 4. A positive mixed-diffusion repair exists, but its graph is trapped

The sign problem can be repaired. On the lifted space use

    Y_i=partial_(x_i)+(partial_i Z).grad_z,
    D0=partial_t+u.grad_x+(D_t Z).grad_z,
    D_t Z=partial_t Z+u.grad_x Z=A(P)Z+R+nu Delta_x Z.        (4.1)

Extend the displayed coefficients independently of z. For the defining
functions q_a(t,x,z)=z_a-Z_a(t,x), one has IDENTICALLY

    Y_i q_a=0,              D0 q_a=0.                       (4.2)

Moreover Y_i rho=0 and D0 rho=0 distributionally. Since div_x u=0 and the
vertical coefficients in (4.1) do not depend on z, these vector fields have
zero spatial/value divergence. Thus

    D0 rho=nu sum_i Y_i^2 rho                              (4.3)

is a genuine positive mixed-diffusion forward equation satisfied by the
graph density. A finite-mass version uses rho=m(t,x)delta(z-Z), where m>0
solves the ordinary scalar advection--diffusion equation with drift u.
No stochastic force is added to NS; this is an auxiliary representation.

But (4.2) also says that diffusion and transport preserve EVERY level set
z-Z(t,x)=constant. All their iterated Lie brackets annihilate the q_a.
This construction works for any prescribed smooth Z; it carries no new
regularity restriction merely by being an exact positive lift. It also uses
the full D_t Z, including the viscous and spatial derivative terms, rather
than just the six-dimensional Hamiltonian block.

## 5. General theorem: positivity and an exact graph force tangency

The preceding trapping is not a poor choice of the mixed coefficients.

**Theorem 2 (graph-preserving diffusion obstruction).** Let Z be any smooth
map of (t,x) into R^m, m>=1, and let rho=w(t,x)delta(z-Z(t,x)), with smooth
positive w on the open base region. Suppose rho solves a smooth forward
sum-of-squares diffusion equation whose test generator is

    D=partial_t+X0+nu sum_(j=1)^q X_j^2,

where X0 and X_j are spatial/value vector fields and nu>0. Then X_j and
the extended drift partial_t+X0 are tangent to the space-time graph

    S={(t,x,z): z=Z(t,x)}.

Every iterated Lie bracket of those fields is tangent to S as well.

Proof. For each q_a=z_a-Z_a(t,x), test the forward equation with chi q_a^2,
where chi>=0 is any compact smooth test. On the graph every first-order
term vanishes, as do the cutoff cross terms. The remaining integrand is

    2nu chi sum_j (X_j q_a)^2.

The weak equation makes its integral against rho zero. Positivity of w and
continuity imply X_j q_a=0 at every graph point. Hence each diffusion field
is tangent. Test next with chi q_a. Cross terms again vanish. Since X_j q_a
vanishes on S and X_j is tangent, X_j^2 q_a also vanishes there. It follows
that (partial_t+X0)q_a=0 on S. Finally, the commutator of vector fields
preserving the ideal of functions vanishing on a submanifold preserves that
ideal. Induction proves tangency of every iterated bracket. QED.

This is a smooth local statement. It asserts nothing about singular
coefficients at an NS endpoint or a nongraph kinetic family. It applies to
any finite enlargement by pressure variables, derivatives, or other smooth
observables, provided that the lift still has this deterministic graph form.
No assumption that such observables form a coherent D-module is used.

## 6. The finite-contact lower bound vanishes to every order

There are TWO distinct Hamiltonian constructions in this attempt. The matrix
A(P) generates a Hamiltonian on the value fiber (omega,sigma). A finite-type
symbol test for a lifted differential operator instead uses the cotangent
Hamiltonian of its transport vector field. They cannot be identified without
an adapter. Here the latter, faithful to the positive lift, can be computed.

For the explicit fields (4.1), let (tau,xi,zeta) be cotangent coordinates and
set

    ell_i=xi_i+partial_i Z.zeta,
    h=tau+u.xi+D_t Z.zeta,
    a=nu sum_i ell_i^2.                                    (6.1)

At every point of S and every nonzero zeta, the covector

    (tau,xi,zeta)=(-partial_t Z.zeta,-(D_x Z)^T zeta,zeta)    (6.2)

is nonzero and conormal to S. At (6.2), ell_i=0 and h=0.
For linear cotangent symbols the Poisson bracket corresponds, up to the
irrelevant convention-dependent sign, to the commutator of the base vector
fields. By (4.2), or by Theorem 2, every such commutator is tangent. It follows
that H_h^j ell_i vanishes on N*S for every j. Leibniz's rule therefore gives

    H_h^j a=0 on N*S for ALL j>=0.                         (6.3)

In particular no finite N and positive c can satisfy the proposed bound

    sum_(j=0)^N |H_h^j a|^2>=c

on this nonzero conormal support. The same conclusion holds for every smooth
positive graph-preserving lift in Theorem 2, not just (4.1). It is unchanged
by a smooth change of the lifted coordinates.

For m=6 the space-time graph has dimension four inside a ten-dimensional
base, and its conormal has dimension ten in the twenty-dimensional cotangent
space. The canonical one-form restricts to zero there, so the conormal is
Lagrangian. It is not a geometrically forbidden characteristic support.
Most importantly, it is present for EVERY smooth solution because a Dirac
graph is already singular in its normal directions. Those singularities
are introduced by the representation, not evidence of NS blow-up.

Thus the exact positive graph lift cannot supply the proposed finite-contact
escape argument. The obstruction is exact tangency to all orders, not a
failed absolute-value estimate or a finite-resolution constant.

## 7. Why critical normalization does not repair this attempt

Tangency and (6.3) hold for each rescaled smooth graph as well. In addition,
(2.1) retains both the pressure term and the viscous correlation at critical
order. Passing to a limit does not justify replacing the full balance by
Hamiltonian invariance alone.

Nor does the energy budget imply zero critically normalized dissipation.
For a genuine smooth unforced solution V on a compact interval, the genuine
rescaled solutions u_r(x,t)=r^(-1)V(x/r,t/r^2) obey

    ||u_r(0)||_2^2=r ||V(0)||_2^2,
    nu integral |grad u_r|^2 dx dt=r nu integral |grad V|^2 dy ds.

These physical costs tend to zero while the resolved solution and its
normalized dissipation remain V and its nonzero dissipation. This family
has varying initial data and shrinking observation intervals; it is NOT a
singularity of one fixed datum. It checks precisely the normalization
inference and is consistent with the repository's earlier scaling ledger.

The actual open bridge is therefore still to construct a nontrivial critical
DEFECT, not a raw graph, and prove its NS-specific transport and dissipative
compatibility after removing artificial graph singularities. No theorem
proving that bridge, or a signed estimate that replaces it, was obtained.

The exact conormal obstruction does not falsify all possible Hamiltonian
finite-contact arguments, stochastic representations, metriplectic estimates,
or nonlocal space-time geometric approaches. No general theorem rules those
out here. It falsifies the concrete graph-lift implementation tested in this
attempt. No new continuation criterion or singularity subclass is promoted.

## 8. Sources, tests and repository status

[S1] L. Napper, I. Roulstone, V. Rubtsov, M. Wolf, Monge--Ampere Geometry and
Vortices, Nonlinearity 37 (2024), 045012. The primary HTML, equations (3)--(6)
and the distinction between the pressure diagnostic and dynamics, was checked:
https://arxiv.org/html/2302.11604v2 . No NS regularity result is imported from it.

[S2] G. Koch, N. Nadirashvili, G. Seregin, V. Sverak, Liouville theorems for
the Navier--Stokes equations and applications. The primary HTML's bounded
mild local theory and regularity were checked:
https://arxiv.org/html/0709.3599v1 . Only an actual smooth local lifespan is
used for the compact-data test; no general three-dimensional Liouville
conclusion is assumed.

[S3] K. Pravda-Starov, Subelliptic Estimates for Quadratic Differential
Operators, arXiv:0809.0186. Primary abstract checked for the scope of the
linear quadratic-operator singular-space mechanism:
https://arxiv.org/abs/0809.0186 . Its theorems are motivation only and are not
applied to the nonlinear NS equation or the graph lift.

The graph sign, positive-lift construction and conormal argument are derived
in full above; no novelty or exhaustive prior-art claim is made. Symbolic
self-checks verify the explicit compactification's uncut polynomial curl,
vorticity, stretching, correlation term, and second-order product rule.
They are not an independent proof audit or PDE simulation.

Remote main, PLAN, AGENTS, the LOCAL/ENERGY/SCALE part of the canonical graph,
the terminal-gap note, and focused repository searches were read. No remote
file or status was changed. The complete repository verifier and independent
mathematical review were not run. This working note records a failed attempt
at the decisive producer, not a proof of NS-R3 or a strict reduction of it.
