# Shear feedback: doubled-parent birth, exact transmission, and the growth gap

Date: 2026-09-10. Input: `itpplasma/navier@115d0f6fc7c6366cd08b85a51bfa53189ab8f635`.

**AUTHOR PROOFS; independent mathematical audit and novelty undetermined.**
This packet does not construct an unforced singular solution, a completed
regeneration cell, or an arbitrary-data continuation bound. The principal
source reference is extended to an explicitly specified nonlinear local
system below. That system is not identified with the complete physical
OpenAI solution, nor with a finite-energy whole-space background.

## 0. What was tested

The preceding phase-closure note found that the sum daughter does not wind
into a new source parent under the old frozen shear. Here we retain the
nonlinear feedback of the generated shear rather than just tracing that
one phase. Three concrete results replace the simplest phase-only picture:

1. The dominant difference shear does not directly advect the exactly
   symmetric daughter's phase. This is a directional cancellation, not
   an absence of all shear feedback.
2. In the full nonlinear reference system, the first shear and its further
   interactions generate both doubled parent wavevectors at order t^3.
   The coefficient is explicit, quartic in the original amplitudes, and
   persists at exact mirror tilt. Unequal parent magnitudes also generate
   the central daughter at this order.
3. Linearization about an exact diffusively decaying shear gives an
   infinite coupled lattice with a positive comparison structure. It
   transfers a central perturbation into the doubled-parent directions
   with an explicit finite-time lower bound, without dropping higher
   lattice modes from the mathematical equation.

These statements do not compose into a self-sustaining cascade. Under the
source's old normalization, isolated doubled parents have negative net
linear growth. Also, the same quartic birth is present in a globally smooth
original-NS control. A source-specific nonlinear amplification and common
physical history remain essential.

The terminal correction problem is unchanged:

    L_U w + P div(w tensor w) = -P F,
    u=U+w, u(0) in S_sigma(R3), viscosity fixed and positive,

with a preserved singular observation and the complete final force F. No
local Fourier calculation removes that total force.

## 1. The difference shear is directionally inefficient for direct steering

Use the preceding reference notation, in the orthonormal frame (e_x,N,e_z):

    p=b(u+c,0,1), q=b(-u+c,0,1), Delta=2u,
    k_d=p+q=2b(c,0,1), k_s=p-q=b Delta e_x,
    d=(0,c_0[Q_++Q_-],-2c), Q_+/-=sqrt(1+(+/-u+c)^2).

Apart from its scalar Fourier factor, the difference output is b Delta d.
Although its N component is order one when c is small,

    k_d . d = -4bc.                                      (1.1)

In particular the strongest shear direction is orthogonal to the daughter
wavevector at c=0. For the prescribed transverse shear

    W(t,x)=sigma(t) d sin(k_s.x),

the flow map is exactly

    Phi_t(x)=x+I(t)d sin(k_s.x), I(t)=integral_0^t sigma(s) ds,

because k_s.d=0. The passive phase initially k_d.x becomes

    phi(t,x)=k_d.x-I(t)(k_d.d)sin(k_s.x),
    grad phi=k_d-I(t)(k_d.d)k_s cos(k_s.x).                (1.2)

The normalized radial tilt changes by at most
2b|Delta I(t)| |c|. For sigma(t)=sigma_0 exp(-nu|k_s|^2 t),
this is at most 2|sigma_0| |c|/(nu b|Delta|).
Thus a bounded integrated shear of this form cannot turn c tending to zero
into an order-one tilt by direct advection alone.

This calculation is kinematic. It is NOT a geometric-optics approximation
for waves and shears of comparable wavelength. In particular it omits the
amplitude term (w.grad)W and the pressure response. The following sections
retain these terms instead of using (1.2) as a universal obstruction.

## 2. A nonlinear local system with the source reference matrix

Fix lambda>0, c_0<0, nu>0. Write v=(r,theta,zeta), independent of the
N-coordinate, periodic in x,z, and satisfying partial_x r+partial_z zeta=0.
Set

    K_ref = [[0,-lambda/c_0,-omega],
             [-lambda*c_0,0,0], [omega,0,0]],
    v_t + P[K_ref v] + P[(r partial_x+zeta partial_z)v] = nu Delta v. (2.1)

P is the full three-component Leray projector on this invariant Fourier
plane. No finite lattice is used in (2.1). The omega part is a pressure
gradient on mean-zero two-dimensional divergence-free fields: its planar
curl is omega times the planar divergence. It can therefore be removed
from the displayed component system without deleting a dynamical mode.
The component equations are

    (partial_t+r partial_x+zeta partial_z)r
            = (lambda/c_0)theta - partial_x p + nu Delta r,
    (partial_t+r partial_x+zeta partial_z)theta
            = lambda c_0 r + nu Delta theta,
    (partial_t+r partial_x+zeta partial_z)zeta
            = -partial_z p + nu Delta zeta.              (2.2)

This is a viscous two-dimensional velocity/scalar system with both linear
couplings retained, not a closed three-mode ansatz. On a fixed torus it has
a unique smooth solution for a short interval for every smooth datum.
For completeness, heat variation of constants in H^s, s>2, uses the
bounded zero-order linear map and the product bound from H^s to H^(s-1).
The heat gain of one derivative has kernel O((t-s)^(-1/2)), giving a
contraction on a short interval; higher spatial regularity and the equation
give the time derivatives used below. Nothing here asserts uniformity on a
concentrating sequence.

### What background this represents

Put kappa=-lambda/c_0>0, G=-lambda c_0>0, and g=kappa+G.
In a uniformly rotating Cartesian frame with Coriolis matrix

    C=[[0,kappa,0],[-kappa,0,0],[0,0,0]],

the affine field U_B=g x N solves rotating NS with pressure
p_B=-kappa g x^2/2. Its convective term and Laplacian vanish and
C U_B+grad p_B=0. Linearizing about it gives precisely K_ref with omega=0;
independence of N removes only the background advection g x partial_N.
A further skew planar term omega is absorbed into pressure as above.

This supplies an exact local background interpretation. It is not a
finite-energy R3 datum: the affine background is unbounded and the waves
are periodic. Cutting it off produces a new matching problem. The source's
finite-L normal has a small N component and its slow/transverse derivatives
are also absent from (2.1). No uniform transfer to those physical errors is
claimed here.

The matrix and growing polarizations are those recorded in the preceding
source-derived note. The inspected primary source, (7.5)--(7.10), explicitly
separates its principal equation from slow transport and other residuals.
Those residuals are not silently declared zero in this extension.

## 3. Exact nonlinear birth of the doubled parents

Let b,u>0, Q=sqrt(1+u^2), and set

    p=b(u,0,1), q=b(-u,0,1),
    a_p=(1,c_0 Q,-u), a_q=(1,c_0 Q,u).

The real initial field has Fourier coefficients

    v_p(0)=A a_p, v_q(0)=B a_q,
    v_-p(0)=A a_p, v_-q(0)=B a_q,                       (3.1)

where A,B are real. Arbitrary phases of the two nonparallel parents can
be moved to real phases by a spatial translation; the formulas below use
that convention. A Fourier coefficient here multiplies exp(i k.x), with
no implicit cosine factor of one half.

### Theorem 1: fourth-degree feedback at the third time order

For the full smooth solution of (2.1), as t decreases to zero,

    v_(2p)(t) = (16i/3)c_0 Q (bu)^3 A^2 B^2 t^3 N + O(t^4),
    v_(2q)(t) =-(16i/3)c_0 Q (bu)^3 A^2 B^2 t^3 N + O(t^4),
    v_(p+q)(t)=-(8i/3)c_0 Q (bu)^3 AB(A^2-B^2)t^3 N + O(t^4). (3.2)

All the displayed targets have zero coefficients at time orders zero,
one and two. The remainder is for fixed data, fixed b,u,lambda,c_0,nu
in any fixed spatial Sobolev class. No bound uniform in L or b is implied.
The leading coefficients are independent of lambda and nu. They are not
asserted to dominate at a full turnover time.

In particular 2p and 2q appear when AB is nonzero, even at equal weights.
The central daughter is generated when the weights have unequal nonzero
magnitudes. Exact cancellation of the first quadratic sum is not an
all-orders prohibition of these later interactions.

Proof. Let B(f,h)=-P[(f.grad)h] denote the ordered NS bilinear map and
L=-P K_ref+nu Delta. Put V=v(0), S=B(V,V). The growing polarization identity
gives LV=rho V, rho=lambda/Q-nu b^2 Q^2. Direct whole-symbol multiplication
leaves only the shear pair, with

    S_(p-q)=-4i bu c_0 Q AB N,
    S_-(p-q)=conjugate(S_(p-q)).                         (3.3)

This shear is N-directed and independent of N. Hence
B(S,V)=B(S,S)=0, LS=-nu|p-q|^2 S. Put D=B(V,S). It is again purely
N-directed, with support at the parent carriers and at +/- (2p-q),
+/- (2q-p), and their corresponding conjugates. In integer labels
k=b(um,0,n), its eight possible nonzero coefficients are

    D_(3,1)=D_(-3,-1)=D_(-1,1)=D_(1,-1)
          =-8 c_0 Q (bu)^2 A^2 B N,
    D_(-3,1)=D_(3,-1)=D_(1,1)=D_(-1,-1)
          =-8 c_0 Q (bu)^2 AB^2 N.                     (3.4)

The second time derivative is
v''(0)=rho^2 V+(2rho-nu|p-q|^2)S+D. In the third derivative,
L v'' and the terms involving only V and S have no coefficients at
2p,2q,p+q; B(D,V)=0. Consequently at these targets

    v'''(0)=B(V,D)=B(V,B(V,B(V,V))).                    (3.5)

The ordered convolution gives (3.2) after division by 3!=6.
Every omitted term is excluded here by its exact support or direction,
not by a smallness assumption. Full untruncated time jets, including L
and ordinary viscosity, check the statement independently of this support
simplification at two positive viscosities through order eight. QED.

### The central cancellation has an exact symmetry at equal weights

For A=B, the initial field satisfies

    r(x,z)=-r(pi/(bu)-x,z),
    theta(x,z)=-theta(pi/(bu)-x,z),
    zeta(x,z)=zeta(pi/(bu)-x,z).                         (3.6)

The equations (2.2) are invariant under this transformation, including the
linear couplings, convection, pressure, and viscosity. Uniqueness preserves
it. Therefore the x averages of r and theta vanish. The x average of zeta
is constant in z by incompressibility and zero by conservation of its
spatial mean. All nonzero pure-z modes, including the central daughter,
vanish for the entire smooth lifespan, not just through a finite jet order.
The doubled carriers have nonzero x frequency and obey (3.6); they are not
excluded. Unequal A and B break this specific symmetry and (3.2) gives its
first central response.

### Growing coordinates are present, not only a new wavevector

A pure N vector at tilt u decomposes as

    N=[a_+(u)-a_-(u)]/(2c_0 Q).

Thus each nonzero coefficient at 2p or 2q includes a nonzero coordinate on
the corresponding growing INVISCID eigenbranch, and an equal opposite
coordinate on the decaying branch. It is not initially a pure growing
polarization. Whether it subsequently grows with viscosity is a separate
question answered negatively for an isolated exact copy in Section 5.

## 4. Keep the amplitude/pressure response to the generated shear

The following is a finite-time test beyond a Taylor coefficient. It uses a
prescribed initial shear, so it must not be conflated with a completed
nonlinear history starting from (3.1).

Use the same rotating frame and let

    U_s(t,x)=[g x+(H0/s)exp(-nu s^2 t)sin(sx)]N,
    p_s=-kappa g x^2/2+(kappa H0/s^2)exp(-nu s^2 t)cos(sx), (4.1)

where s>0, H0>=0, g=kappa+G and G>0. This background solves the full
rotating NS equations exactly: convection is zero, the sinusoid obeys
ordinary heat diffusion, and pressure cancels Coriolis. No time-dependent
force is used to maintain the sinusoid. The affine/infinite-energy scope
qualification of Section 2 still applies.

Linearize about U_s and take perturbations independent of N with z
frequency k>0. Write y for their radial velocity and a for minus their
N velocity. For radial Fourier label m in Z put

    K_m^2=k^2+m^2 s^2, delta_m=nu K_m^2, P_m=k^2/K_m^2.

The entire linearized PDE, including pressure, is exactly the infinite
lattice

    y_m'=-delta_m y_m+kappa P_m a_m,
    a_m'=-delta_m a_m+G y_m
                  +(H0/2)exp(-nu s^2 t)(y_(m-1)+y_(m+1)). (4.2)

The third component is fixed by incompressibility:
zeta_m=-(ms/k)y_m. No carrier is deleted from (4.2). All its off-diagonal
coefficients are nonnegative. This is a special linear comparison property;
the full NS Fourier nonlinearity has no such positivity property.

### Theorem 2: full-lattice finite-time transmission into both tilted copies

Suppose y_0(0)=Y>0, a_0(0)>=0, and all other initial coefficients vanish.
Then every component of (4.2) is nonnegative, and for each t>=0,

    a_(+/-1)(t) >= (H0 Y/2)t exp(-delta_1 t),
    y_(+/-1)(t) >= (kappa P_1 H0 Y/4)t^2 exp(-delta_1 t). (4.3)

For the source geometry k=2b, s=2bu, these are precisely the directions
(2bu,0,2b)=2p and (-2bu,0,2b)=2q.

Proof. The diagonal heat semigroup is positive on l2(Z) direct-sum l2(Z).
The remaining coefficient operator is bounded on every fixed time interval:
P_m<=1 and the shifts have bounded l2 norm. Its Duhamel series converges
in operator norm after factoring out the diagonal heat evolution on each
iterated time simplex. Every term preserves the nonnegative cone. This
constructs the full infinite-lattice solution and proves positivity. Smooth
finite-mode data stay spatially smooth on compact positive-time intervals
by the parabolic equation with smooth coefficients.

In particular y_0(t)>=Y exp(-delta_0 t). Retain just the positive path
from y_0 to a_1 in Duhamel. Since

    delta_1=delta_0+nu s^2,

its integral is exactly (H0 Y/2)t exp(-delta_1 t). One more positive path
from a_1 to y_1 gives the second inequality; reflection gives m=-1.
All other paths and all higher modes are retained in the equation and add
nonnegative contributions, so this is a lower bound for the untruncated
system, not an assertion that a two-mode truncation is exact. QED.

The transfer does not contradict (1.1). It proceeds through
(w.grad)U_s in the N momentum equation, followed by the rotation/pressure
coupling into radial velocity. Direct advection by an N-directed shear
vanishes for these perturbations. Treating phase steering as the only
possible response would miss this channel.

The sign H0>=0 can be arranged for a single sinusoid by shifting its radial
phase. That does not establish that the parent/daughter phases in a whole
nonlinear history simultaneously satisfy the positivity assumptions.

### Numerical calibration, not a PDE certificate

With lambda=kappa=G=b=1, u=12/5, nu=125/2197, and initial y_0=a_0=1,
the implicit Radau integration gives, at t=2,

    H0=1:  y_1 approximately 0.01551253,
    H0=16: y_1 approximately 0.26815161,
    H0=64: y_1 approximately 2.38777741.

The corresponding rigorous formula lower bounds are about 0.00681966,
0.10911453 and 0.43645811. These numbers are floating-point evaluations,
not interval certificates. Symmetric finite sections with 4,8,16,32 radial
harmonics per side agree in y_1 to about 1.2e-10 over the sampled interval.
The analytical finite-section comparison is valid here because of positivity;
agreement alone is not a certified tail estimate.

The H0=64 case shows amplification in this prepared linear reference test,
not that the preceding nonlinear parent evolution creates that shear and
those initial signs while retaining its other modes. No nonlinear handoff
between Section 3 and (4.1) has been proved.

### A full nonlinear reference pilot was also run

To avoid treating the two positive calculations as a composed trajectory,
`research/check_nonlinear_reference.py` evolves (2.2) directly in planar
vorticity and N velocity, with pressure reconstructed by the exact planar
Leray relation. It retains every convolution in the stated dealiased Fourier
band, ordinary viscosity, both linear source couplings, and all returned
modes inside that band. It is a finite-dimensional numerical approximation,
not an untruncated PDE certificate or a computation of the physical source.

For A=1, B=2, u=12/5, c_0=-1, lambda=1 and nu=125/2197, grids
48,64,96,128 were evolved to t=2. The last two use dt=0.0005; the first
two dt=0.001. At t=0.2, the summed energy of the four doubled carriers is
2.8455918, compared with total energy 114.7402406 and parent-carrier energy
78.1924676. The 64/96/128 results agree closely at this early time. This
is a resolved numerical birth observation in the local reference, not a
verified regenerated source pulse: most doubled energy is still N velocity,
and the radial growing structure is not a copy of the old parents.

The long-time pilot fails a 0.1 percent spatial-agreement check. At t=2,
total energies for grids 48/64/96/128 are approximately
48.17483 / 40.13757 / 37.41205 / 37.25642; doubled-carrier energies are
0.00056024 / 0.00019854 / 0.00167986 / 0.00183260. In particular the
96-to-128 doubled-energy difference is still about 8.3 percent relative
to the 128-grid value. Small final edge energy does not remove errors
accumulated at earlier times. No reliable full-turnover verdict is inferred
from the t=2 numbers. A further resolution sweep would be numerical work,
not a proof of nonlinear amplification or of impossibility.

The zero-matrix original-NS control was run on grid 64 with the same data.
Its planar velocity agrees with (5.2) at t=2 to relative error below 6e-15;
its doubled modes are passive N velocity. At t=0.2 its doubled-carrier energy
is 2.2804304, so substantial early doubled-mode production also occurs in
that rigorously globally smooth control. Each run checks the Fourier energy
identity against the computed RHS; this is a numerical consistency check,
not an integrated error certificate.

## 5. Two tests prevent calling this a regenerative cascade

### The copied parent is more strongly damped

Under the source reference normalization

    nu b^2=lambda/(1+u^2)^(3/2)=lambda/Q^3,

a parent at its pulse midpoint has net rate zero. A geometrically identical
copy with both wavevector components doubled has net rate

    gamma_(2p)=lambda/Q-4nu b^2 Q^2=-3lambda/Q<0.         (5.1)

The inviscid eigenbranch remains the same, but the dissipation is four times
larger. New frequencies and nonzero growing coordinates therefore do not
by themselves give a new amplifying source pulse. If only a homogeneous
background growth parameter were changed, it would need lambda_new>4lambda.
With fixed rotation kappa and lambda^2=kappa G, that would require G_new>16G.
This is an isolated/homogeneous comparison, not a necessary condition for
all nonnormal, spatially varying or nonlinear amplification mechanisms.
A sinusoidal shear does not uniformly change G; pointwise large shear is
not a substitute for solving its coupled perturbation problem.

### A globally smooth original-NS control has the same quartic births

Set the whole matrix K_ref to zero, keeping exactly (3.1) and nu>0 on a
three-dimensional periodic box, with independence of N. The planar velocity
(r,zeta) has a streamfunction whose two wavevectors have the same length.
Its vorticity is a fixed scalar multiple of that streamfunction. Therefore
its planar self-advection is a pressure gradient and

    (r,zeta)(t)=exp(-nu b^2 Q^2 t)(r,zeta)(0)              (5.2)

is the exact planar NS velocity. The N component solves a linear
advection-diffusion equation driven by this known smooth planar flow.
The maximum principle bounds its supremum by its initial supremum. Energy
estimates for its derivatives, with the explicitly smooth coefficients in
(5.2), give all Sobolev orders on every finite interval. Thus this is a
globally smooth original unforced periodic NS solution.

Its coefficients at the targets in (3.2) have the SAME t^3 leading terms.
Indeed the proof of (3.2) uses the linear matrix only for the scalar
relation LV=rho V and for the shear's scalar decay; those hold here with
rho=-nu b^2 Q^2. The new modes are passive N velocity in this control,
not a new poloidal cascade. The maximum principle precludes interpreting
their birth as increasing maximum speed without a separate mechanism.

Consequently the quartic coefficient alone is not evidence of a singularity.
The rotation/background coupling and an actual sustained nonlinear history
are load-bearing. This control is periodic, not the required R3 datum;
it is used only to falsify an overly broad interpretation of the seeding.

## 6. Exact remaining gap after this follow-through

There is now an explicit route from parent waves to doubled-parent
wavevectors, and an exact reference shear response that can populate those
directions with radial velocity despite the passive-phase cancellation.
The old statement 'the daughter cannot wind, therefore it cannot regenerate'
would be unjustified. But no self-reproducing unforced cascade follows.

The missing step is a full nonlinear transition in which the original
parents generate the needed shear and new polarizations, all returned modes
are included, and the new state has enough amplification at its increased
viscous cost. The two positive calculations above cannot be concatenated by
resetting the shear or deleting the old parents. The positivity of (4.2)
does not persist under arbitrary signed nonlinear mode feedback.

Even such a local transition would still need a fixed-viscosity physical
embedding with the source's finite-L phases, localization, slow drift,
canonical whole-space pressure, and ONE common Schwartz trace. No error
bound for that embedding or singularity-preserving correction was supplied.
Failure of the old homogeneous growth balance does not exclude all new
coupled backgrounds, nor does it imply arbitrary-data global regularity.

## 7. Validation and source provenance

`research/check_source_shear_feedback.py` passed 299 exact assertions and
12 labelled floating-point positive-lattice cases. Exact checks include
symbolic general-amplitude coefficients, full Fourier time jets through
order eight at two positive viscosities for both the source reference and
the original-NS control, every generated mode's transversality/reality,
reflection symmetry, exact diffusing-background pressure signs, the two
positive Duhamel paths, and the isolated doubled-mode growth rate.
The time jets have no spatial frequency truncation at their computed order.
Finite Taylor data do not certify a complete trajectory or radius of validity.

A preliminary explicit DOP853 lattice run failed the positivity guard in a
stiff high-mode tail (approximately -1.9e-7) and was discarded. The reported
cases use implicit Radau with relative tolerance 2e-10 and absolute tolerance
2e-12; the positive lower-bound and nested-section checks then passed.
No positivity theorem is inferred from either numerical solver.
The five nonlinear-reference/control runs are separately labelled and the
failed long-time convergence is retained, not counted as verification.
The preceding checkers were also rerun: 1049 exact adjoint assertions,
28 exact regeneration assertions plus nine principal-ODE cases, and six
exact phase-closure assertions passed. The source-pulse adjoint checker also passed its 12 exact symbolic and
102 numerical assertions. These were the uploaded prior checkers, not a
fresh checkout or all repository tests.

The source PDF was inspected through its primary public URL, including
rendered printed pages 74--75 for (7.2)--(7.10). No whole-source audit or
new Lean build occurred. The primary source is an input only at its forced
scope. The additional periodic control is derived directly above, not
imported as a theorem about the source or about R3.

Connected GitHub was read at the input SHA. Direct shell networking failed
DNS resolution, so no full repository checkout was available. The full
research verifier, all repository-wide checks, manuscript build, and Lean
were NOT run. Local code execution and whitespace/syntax checks are the
validation of this additive packet. No PLAN, manuscript, canonical proof
graph, or formal status is promoted by this evidence file.

Sources: preceding project notes `2026-09-10-source-phase-closure.md` and
`2026-09-10-source-prehistory-regeneration.md` at the input SHA; OpenAI,
*Finite Time Blowup for Navier--Stokes*, (7.2)--(7.10), inspected 2026-09-10,
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf .
For context, Singh--Sridhar, *Plane shearing waves of arbitrary form: exact
solutions of the Navier--Stokes equations*, arXiv:1101.5507, describes the
exact shear-wave cancellation background; its abstract was inspected, not
used as an unproved nonlinear or finite-energy embedding theorem.
All new derivations and code are original to this packet; no third-party
source code was copied. No literature novelty or publication claim is made.
