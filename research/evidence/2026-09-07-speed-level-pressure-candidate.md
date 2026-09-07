Controller-retained worker snapshot, 2026-09-07. Original worker file: level-set-pressure.md;
SHA256 `36214aaf2b33d16052cccd75d5021efdb7f211ad35bef9d07b6b5cb947f35d4f`.
Author derivation with independent mathematical audit PENDING. This
record is evidence for further research, not an established graph theorem.
The original worker text follows unchanged. PLAN alone allocates work.

# Second discovery period: pressure flux through speed levels

Date: 2026-09-07. Frozen repository base for provenance:
`ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
Worker evidence only. Author derivations below; independent audit pending.
No terminal theorem, singular solution, or canonical claim promotion.

## 1. Exact object, proposed gain, and prior-obstruction check

Before reading the applicable prior notes, the proposed object was the
excess-energy tail of the ORIGINAL velocity,

    rho=|u|,
    Omega_a={rho>a},
    E_a=(1/2) integral (rho^2-a^2)_+,       a>0.

The proposed gain was cancellation of pressure variation across nested
speed surfaces, strong enough to bound integral_0^infinity E_a da from
the inputs on every finite time interval. This integral is exactly

    X=(1/3)||u||_3^3.

Thus an input-only bound would feed the stipulated L-infinity_t L3
continuation consumer for every solenoidal Schwartz datum and fixed nu>0
on R3. The original local branch, normalized Riesz pressure, energy and
trace remain the consumer; no companion equation is substituted.

After the object was registered, the following were read:

* research/evidence/2026-09-06-speed-shell.md;
* research/evidence/2026-09-07-local-entropy-and-single-channel-transfer.md.

The first concerns the quotient representative and its signed defect,
including exact speed-shell orthogonality. The second excludes a fixed
local velocity entropy monotone for every datum. Neither is claimed anew.
The object pursued here was instead a domain-dependent harmonic projection
that exposes the pressure flux and its moving-domain derivative.

## 2. The original velocity tail balance

On a compact smooth time interval, at a positive regular speed value a,
let Sigma_a=boundary Omega_a and let n be its outward normal, so
n=-grad rho/|grad rho|. The speed-squared equation gives

    E_a' = J_a - nu D_a,                                  (2.1)
    J_a = -integral_Sigma_a p u.n
        = -integral_Omega_a u.grad p,
    D_a = integral_Omega_a |grad u|^2
          +a integral_Sigma_a |grad rho|.

The last term is the diffusion contribution from the kink in the positive
part. Formula (2.1) can also be obtained by smoothing the positive part;
the geometric formula here is used only at regular values.

Every closed boundary component has integral u.n=0 by solenoidality.
Consequently an arbitrary componentwise constant can be subtracted from
p inside J_a. This is a cancellation, not an estimate of the remaining
pressure oscillation. Integrating the uncorrected balance over a recovers
the ordinary cubic pressure work and cubic dissipation; doing that alone
does not improve the existing criterion.

## 3. A surface inverse without an assumed geometric constant

For each bounded regular Omega_a, let G_a be the closed subspace of L2
vector fields consisting of gradients of H1 functions. Project u|Omega_a
orthogonally onto G_a:

    g_a=grad phi_a,      w_a=u-g_a,
    K_a=||g_a||_(L2(Omega_a))^2.                           (3.1)

Equivalently phi_a is harmonic with Neumann data partial_n phi_a=u.n,
with a constant fixed separately on each connected component. The
variational definition is

    K_a = sup_psi [2 integral_Omega_a u.grad psi
                         -integral_Omega_a |grad psi|^2]. (3.2)

No uniform surface Poincare constant, topology bound, or pressure
oscillation estimate is inserted. Orthogonal projection gives

    0<=K_a<=integral_Omega_a rho^2,
    div w_a=0,       w_a.n=0.

For the static integrals over ALL a, define (3.2) using restrictions of
globally smooth compactly supported test functions and a fixed countable
family dense in their C1 topology on compact sets. This agrees with (3.1)
on bounded smooth domains by extension and density. At exceptional levels
it is the definition used here. Each variational expression is Borel in a,
so the supremum is measurable. No shape derivative at those levels follows
from this definition. The ambient test functions still incur energy cost
only inside Omega_a; this convention does not add exterior reconstruction.

If h_a is the harmonic function in Omega_a with boundary trace p, then

    J_a=-integral_Omega_a grad phi_a.grad h_a,
    |J_a| <= sqrt(K_a) sqrt(H_a),
    H_a=integral_Omega_a |grad h_a|^2
        <=integral_Omega_a |grad p|^2.                    (3.3)

Indeed gradient projection preserves pairing with grad p, and harmonicity
of phi_a removes the zero-boundary function p-h_a. Thus pressure flux
depends only on the harmonic extension of the boundary pressure. This is
the exact quantified cancellation available without geometric constants.

The first missing estimate in (3.3) is control of the harmonic pressure
energy H_a after integration over levels and time. Replacing it by the
displayed full pressure-gradient energy introduces an uncontrolled
acceleration quantity. Poisson's equation for the actual pressure has not
supplied an input-only bound for H_a.

## 4. Nonlocal correction and its regular-level shape derivative

There is a stronger reason to inspect K_a than applying Cauchy--Schwarz
to (3.3): its bulk pressure derivative is exactly 2J_a. Work on a time
interval where the chosen level is regular and its smooth domains can be
identified by a smooth deformation. Put q=rho^2/2. The outward speed of
the level boundary is

    V_n=q_t/|grad q|=u.n+W,
    W=(-u.grad p+nu Delta q-nu|grad u|^2)/|grad q|.         (4.1)

Envelope differentiation of (3.2), whose variation in phi_a vanishes,
gives

    K_a'=2 integral_Omega_a u_t.g_a
         +integral_Sigma_a V_n(2u.g_a-|g_a|^2).

Insert NS, split V_n as in (4.1), and integrate convection by parts.
Because w_a is divergence free and tangent to the boundary,
integral w_a.grad(|g_a|^2/2)=0. The result is

    K_a' = 2J_a
       +2 integral_Omega_a (w_a tensor w_a):D2 phi_a
       +2nu integral_Omega_a Delta u.g_a
       +integral_Sigma_a W(2u.g_a-|g_a|^2).               (4.2)

Therefore the bulk pressure term cancels in E_a-K_a/2, but two genuinely
uncontrolled structures remain: the Hessian in (4.2), and the pressure
part of the relative boundary motion W. In particular the level boundary
is not a material boundary, and treating it as one loses the final term.

The apparent reciprocal |grad q| cannot simply be bounded through a
critical value. On a compact regular band, coarea converts the pressure
part of the final term in the derivative of E_a-K_a/2 into

    (1/2) integral_{rho in band}
       [u.grad p/rho] [2u.g_rho-|g_rho|^2] dx.            (4.3)

This calculation is restricted to such regular bands. No differentiability
of integral K_a da through topology changes, or global bound for (4.3), has
been established. Coarea removes a displayed geometric denominator; it
does not control the new nonlocal boundary trace.

## 5. The natural integrated subtraction is not coercive

The candidate suggested by the bulk cancellation is

    F(u)=X(u)-(1/2) integral_0^infinity K_a(u) da.          (5.1)

There are compact smooth solenoidal fields for which

    integral K_a da / integral rho^3 dx -> 1.             (5.2)

Thus F/(integral rho^3) tends to -1/6. This defeats this particular
level-by-level subtraction, even though it is nonlocal.

Here is a short certificate of (5.2). In cylindrical coordinates (r,z),
choose smooth nonnegative functions a_delta,h,g with

    a_delta=1 on [0,1], support a_delta subset [0,1+delta],
    support h subset (1,2),  integral_0^infinity r h(r)dr=1,
    0<=g<=1, support g subset (-2,2), g=1 on [-1,1].

Let

    M_delta=integral r a_delta(r)dr,
    f(r)=a_delta(r)-M_delta R^(-2)h(r/R),
    F0(r)=integral_0^r s f(s)ds,
    u_z=f(r)g(z/L),
    u_r=-F0(r)g'(z/L)/(rL),       u_theta=0.              (5.3)

Take R>2(1+delta). Since integral r f(r)dr=0, F0 is compactly supported.
At the axis F0(r)=r^2/2, so the formula is smooth there. Direct cylindrical
differentiation gives div u=0. These are actual compact smooth R3 data.
The positive axial core is long; the negative return speed is O(R^-2),
and sup |u_r|=O(L^-1). Constants below can be chosen uniformly for
0<delta<1 and R>4, after L is made sufficiently large for the chosen R.

Fix eta>0. Choose R large and then L large so that rho<eta outside
r<1+delta. Thus all Omega_a with a>=eta lie in this core cylinder. On each
such domain use the SAME trial potential

    psi(z)=L G(z/L),     G'=g.

It has grad psi=g(z/L)e_z. On r<=1 the discrepancy u-grad psi is only the
O(L^-1) radial velocity; on 1<r<1+delta its squared integral is O(delta L).
Consequently projection optimality gives, uniformly over a>=eta,

    integral_Omega_a rho^2-K_a
        <= integral_Omega_a |u-grad psi|^2
        <= C delta L+C/L.

The maximal speed is bounded by 2, so integration in a yields

    integral_0^infinity K_a da
       >= integral rho^2(rho-eta)_+ dx-C delta L-C/L
       >= integral rho^3 dx-eta||u||_2^2-C delta L-C/L.    (5.4)

For these fields, ||u||_2^2<=CL and integral rho^3>=cL; the radial L2
contribution is O((log R)/L), which is absorbed by first fixing R and then
taking L large. The reverse bound integral K_a da<=integral rho^3 always
holds. Send eta,delta to zero, choosing R and L in the stated order, to
obtain (5.2). No NS trajectory with a persisting jet shape is asserted.

## 6. Exact scope and return to the existing global quotient

The degeneracy has a precise cause: each phi_a is an interior potential,
and its Neumann energy charges no exterior extension or reconstruction.
A nearly constant axial core can therefore be almost entirely removed.
This is not a rejection of all nonlocal pressure cancellation.

The controller identified the canonical QUOTIENT-FUNCTIONAL /
QUOTIENT-EVOLUTION repair during this calculation. A genuine global
nonlinear gradient quotient has a different coercivity mechanism:
for a globally admissible v=u+grad phi, Leray projection gives P v=u, so

    ||v||_3 >= ||u||_3/||P||_(L3->L3).

Taking the global infimum of integral |u+grad phi|^3 therefore preserves
critical coercivity. The independent interior subtractions in (5.1) do
not possess this global reconstruction inequality. Merely saying each
interior potential admits some global extension does not repair (5.1):
the exterior cost must actually enter its functional.

Replacing this failed subtraction by the global nonlinear quotient returns
to the already developed quotient architecture and its open signed defect
evolution estimate. The two functionals are not asserted equal. The
cross-lane identification is that the natural coercivity repair lands on
that existing mechanism; this period has not supplied its missing clock.

RESULT: exact tail flux, harmonic-pressure pairing, regular-level shape
identity, and a compact-data obstruction to one specific nonlocal
pressure-cancelling subtraction. The estimate needed to control harmonic
pressure flux in time remains open. The terminal consumer is intact but
has no new input producer.

STOPPING POINT: no further saturation or expansion of the jet example.
A new mechanism would need actual time cancellation of the pressure-driven
level motion or new control of the global quotient's signed defect, not a
free geometry constant or omission of exterior reconstruction costs.
