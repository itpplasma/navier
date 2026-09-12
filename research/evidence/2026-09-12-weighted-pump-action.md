# Weighted pump action and the impossibility of exact angular-gap resets

Date: 2026-09-12. Input: `itpplasma/navier@7f00e36856362b5afc2b2ff92094ccf267e170ea`.

**Author analytic proof; independent audit pending.** The full-chain gain is
real, but its availability at the source's actual pulse scales needs a separate
estimate. This wave proves a whole-space weighted-pressure estimate and applies
it to a phase-coherent, angular-gap pump family. It retains every spatial and
angular sideband in that class. For a source-normalized primary pulse the extra
energy-growth exponent is `O(L^(3/4))`, rather than `O(L)` or an estimate inferred
from a two-mode projection. The construction handles all spatial copies of a
rectangle; it does not interchange a spatial supremum and a time integral.

The angular-gap hypothesis is essential. The source's complete collection of
labels is not asserted to share this gap. Nor is the actual nonlinear even
background assumed equal to the prescribed source. These two missing inputs
remain explicit at the end. A separate whole-space backward-uniqueness
argument proves that an unforced classical solution cannot acquire a new exact
rotational symmetry at a positive time. Thus a single history cannot obtain a
rising invariant gap by deleting the old symmetry-breaking sector at handoffs.

## Working packet

TERMINAL CLAIM: the unchanged original unforced NS problem on `R3`, fixed
positive viscosity, divergence-free Schwartz data and its classical branch.

ESTABLISHED: the one-seed ladder has correlated high-order outputs; the complete
pump chain has certified finite-time gain. A source pulse has a Gaussian
envelope and covariance-determined, not freely chosen, amplitude.

FIRST GAP: quantify the pump action available in a source-scale physical band,
including canonical pressure and the distinction between one rectangle copy
and the entire spatial field.

PREDICTION: covariance normalization gives peak nonlinear amplitude `L^(1/4)`
and width `sqrt(L)`, suggesting action `L^(3/4)`. Directly inserting a single-copy
integral into a whole-space energy inequality is invalid. A weight following
the pulse clock may recover that saving, but only if its pressure commutator is
controlled uniformly in the carrier scale.

FALSIFIER: a pressure term losing an uncontrolled derivative or exponential
weight ratio; a weight that fails to descend across rectangle boundaries; or
loss of the assumed angular gap under the actual coefficient field.

CHECK: an exact whole-space angular Poincare/weighted elliptic estimate, a
compact clock primitive, physical scaling, and the full nonlinear parity
identity. No finite-section or selected-ray propagator is substituted.

## 1. A weighted pressure lemma on all of R3

Let `r=(x_1^2+x_2^2)^(1/2)`. Let `phi(t,r,x_3)` be real, axisymmetric, smooth,
bounded, with bounded derivatives, constant outside a compact spatial set.
Let a scalar pressure `p` have only angular Fourier indices of magnitude at
least the positive integer `N`. The axisymmetry of the weight gives the exact
angular inequality

    ||e^(-phi) p/r||_2 <= N^(-1) ||e^(-phi) grad p||_2.   (1)

This is Fourier Poincare on each circle, followed by integration in `r,x_3`.
No finite axial interval, pressure localization, or boundary condition on an
artificial cylinder is introduced.

Suppose `-Delta p=div F` and `F` is in weighted `L2`. Write

    delta = ||r grad phi||_infinity / N < 1/2,
    c_delta = (1+2delta)/(1-2delta).

Testing with `e^(-2phi) p` and using (1) on *both* derivative-of-weight terms
proves

    ||e^(-phi) grad p||_2 <= c_delta ||e^(-phi) F||_2.    (2)

Indeed the left side of the integration-by-parts identity is at least
`(1-2delta)||e^(-phi) grad p||_2^2`; the absolute right side is at most
`(1+2delta)||e^(-phi)F||_2 ||e^(-phi)grad p||_2`.
Smooth approximation and spatial cutoffs justify the test in the homogeneous
energy class. The bounded weight is harmless for this justification. Crucially,
its *amplitude* does not enter the constant in (2); only its logarithmic
spatial derivative divided by the angular gap does.

## 2. Full pressure-retaining velocity energy inequality

Let `U,w` be smooth solenoidal fields and let `w` solve

    w_t+(U.grad)w+(w.grad)U-nu Delta w+grad p=0.           (3)

Assume the canonical pressure in (3) has the gap in (1). This holds, for
example, if all cylindrical-component Fourier indices are multiples of `N`,
`U` has only even multiples and `w` only odd multiples. These are rotational
vector sectors, not fixed Cartesian-component Fourier conventions. Ordinary
viscosity, divergence, Leray projection and (3) preserve those sectors.

Solenoidality gives

    -Delta p=div F,    F_j=2 sum_i (partial_i U_j) w_i.   (4)

Set `v=e^(-phi) w` and `K(t)=||grad U||_infinity`, with the matrix norm chosen
so `|F|<=2K|w|`. Weighted integration of the pressure term, followed by (1)--(2),
gives

    |int e^(-2phi) w.grad p|
      <= 4delta c_delta K ||v||_2^2.                    (5)

There is no derivative of `w` on the right. In particular no inverse viscosity
or unproved critical norm was used to absorb this term.

The diffusion and transport identities are exact:

    nu int e^(-2phi) w.Delta w
       =-nu ||grad v||_2^2+nu int |grad phi|^2 |v|^2,

    int e^(-2phi) w.(U.grad)w
       =int (U.grad phi)|v|^2.

Consequently, with `S(U)=sym grad U`,

    (1/2) d_t ||v||_2^2 + nu ||grad v||_2^2
       <= [ess sup_x {-lambda_min(S(U))-phi_t-U.grad phi
                                      +nu |grad phi|^2}
                        +4delta c_delta K] ||v||_2^2.    (6)

Formula (6) is an all-mode whole-space estimate. In particular it is not a
localization of the adjoint with an omitted cutoff residual.

## 3. Why one-copy Gaussian integration was not sufficient

For any nonzero smooth bump `g>=0`, supported in `(-1/2,1/2)` with maximum one,
consider the periodic moving profile

    f_L(x,t)=L^(1/4) sum_(j in Z) g((t-x-jL)/sqrt(L)),
    x in R/LZ,  0<=t<=L,  L>1.

For every `t`, a spatial point attains the maximum `L^(1/4)`. On the other hand,
for every fixed `x`, its integral over one period is `L^(3/4) int g`. Thus

    int_0^L sup_x f_L = L^(5/4),
    sup_x int_0^L f_L = L^(3/4) int g.                    (7)

This exact counter-control forbids commuting the two operations. It is not
asserted to be the source field. The physical source has multiple lifted
rectangle copies, so the analogous norm-order issue cannot be skipped.

## 4. A compact clock weight that works across every copy

Consider a single physical band and the source-style auxiliary rectangles.
Use fast time `t_*`, local pulse coordinate `v in [0,L]`, and a transverse
coordinate `xi`. The leading clock derivative satisfies `t_* v=1` at fixed
slow variables. The normalized spatial derivative of `v` is zero on each
lift. Assume `L` is comparable to the band parameter `S` and bounded overlap
of slow/auxiliary supports as in the source geometry.

Choose a nonnegative compactly supported envelope `g_L` which majorizes the
pulse on its cutoff support and obeys

    g_L(v)<=C exp[-c(v-L/2)^2/L],
    I_L=int_0^L g_L(v)dv <= C sqrt(L).

All derivatives vanish near the endpoints. Let `a(x_slow,xi)>=0` be a smooth
amplitude majorant with `a<=C L^(1/4)`, containing the slow and transverse
cutoffs. Fix `b in C_c^infinity(0,1)`, `b>=0`, `int_0^1 b=1`. Define

    f=a g_L(v),
    R=a I_L L^(-1) b(v/L),
    phi=a int_0^v [g_L(s)-I_L L^(-1)b(s/L)] ds.          (8)

The two integrals in brackets have the same total. Thus `phi` is identically
zero near *both* endpoints; its transverse cutoff has the same property at the
other rectangle edges. It descends smoothly to the auxiliary torus and then to
the physical phase map. Sum (8) over a bounded-overlap family if needed.
Every copy is included, not separately initialized. The exact clock identity
and estimates are

    partial_v phi=f-R,
    ||phi||_infinity<=C L^(3/4),
    ||R||_infinity<=C L^(-1/4).                          (9)

The remaining slow derivative/transport terms are estimated explicitly below.
The compensating broad term `R` is retained in the energy inequality; dropping
it would create precisely the kind of false cutoff certificate already ruled
out in this repository.

## 5. Source normalization and uniform band estimate

The primary source inputs inspected for this wave are (6.1), (6.6), (6.11)--
(6.12), (7.16), (7.21), (7.24), and (7.27)--(7.29) of the cited PDF. They give
`epsilon=Q^h`, `S=ell^2`, `L~S`, primary normalized velocity
`sqrt(epsilon) a_sigma t_sigma^h`, carrier size `k~epsilon^(-1/2)`, Gaussian
`|t_sigma^h|<=CP`, and `a_sigma^2~sqrt(S)|T_0,*|`. The normalized radial
auxiliary derivative costs at most `epsilon^(-kappa_s)` times a polynomial in
`S`, where `kappa_s=10^-5`. These are source inputs, not new PDE conclusions.

For the estimate below, retain only a **phase-coherent band family** whose
background/pump and perturbation have the parity/gap required in Section 2.
This is a hypothesis on the physical fields. The original infinite source
collection is not asserted to meet it.

Use isotropic space units `sqrt(Q)`, time units `Q^(1+h)`, and velocity units
`Q^(-1/2-h)`. The resulting viscosity is `nu epsilon` with fixed `nu>0`.
The physical strain-time scale cancels exactly:

    Q^(1+h) Q^(-1/2-h) Q^(-1/2)=1.                     (10)

On a regular annulus the leading pump strain is at most `f` of (8), with all
slow/amplitude/curl derivative contributions bounded by
`epsilon^(1/2-2kappa_s) L^M` for some fixed finite `M`. Increasing `M` absorbs
fixed derivatives and bounded overlap; constants depend on the fixed source
profiles and the chosen regular band patch, not on the band index.

The weight satisfies

    ||grad phi||_infinity+||r grad phi||_infinity
                        <= C epsilon^(-kappa_s) L^M.

Take an invariant gap `N>=c epsilon^(-1/2)` (or more generally
`N>=c epsilon^(-alpha)` for fixed `alpha>kappa_s`). The exact lemma gives

    delta<=C epsilon^(alpha-kappa_s) L^M ->0.             (11)

The base has normalized radial velocity `O(epsilon)` and axial action on slow
coefficients costs `epsilon`; its angular transport annihilates `phi`. Slow
time also costs `epsilon`. The pump velocity is `O(sqrt(epsilon)L^(1/4))`.
Thus the uncanceled transport terms in (6), the viscosity weight term, and the
pressure term are bounded by a finite sum of

    epsilon^(1-kappa_s)L^M,
    epsilon^(1/2-kappa_s)L^M,
    epsilon^(1-2kappa_s)L^M,
    epsilon^(alpha-kappa_s)L^M.                          (12)

Assume explicitly that the normalized base gradient is uniformly bounded and
that the complete pump gradient satisfies the above envelope/remainder bounds;
then `K<=C(1+L^(1/4))+o(1)`. These bounds hold for the stated primary band
coefficients, not for an arbitrary nonlinear correction added to them.
All powers of epsilon in (12) are positive, and `epsilon=2^(-h ell)`, `L~ell^2`.
Their time integrals on any interval `0<=t_*<=C_T L` therefore tend to zero.

Let `M_base(t_*)=||S(U_base)||_infinity` in these units. Using (9) in (6), and
converting between weighted and unweighted norms only at the endpoints, yields

    ||w(T)||_2
      <= exp[int_0^T M_base(s)ds + C L^(3/4)+o(1)]
                                                      ||w(0)||_2,
    0<=T<=C_T L.                                        (13)

No exponential-in-weight constant occurs in the pressure estimate. The only
such conversion is the explicitly retained endpoint factor, already of order
`exp(C L^(3/4))`. The estimate is uniform over all physical copies and all
angular sidebands satisfying the gap. It does not claim closeness of the full
propagator to a frozen finite-dimensional system over this interval.

In particular, the primary wave pump cannot supply an extra `exp(eta L)`
amplification **above this base-strain budget** for any fixed `eta>0` as
`L->infinity`. This is not a comparison to an unknown exact base propagator,
and it does not assert that base amplification itself is inadequate.

## 6. Exact nonlinear meaning and the first remaining term

The angular-gap estimate also identifies rather than discards the nonlinear
feedback. In an `N`-fold rotationally equivariant NS solution, decompose the
velocity into even and odd multiples of `N`, `u=E+O`. With even forcing only,
the odd equation is exactly

    O_t+(E.grad)O+(O.grad)E-nu Delta O+grad p_odd=0.       (14)

Odd--odd products belong to the even equation; they do not vanish from the
system. Write `E=U_base+W_primary+Z`. Applying (6) to (14) adds the explicit
budget

    B_Z(T)=int_0^T [||S(Z)||_infinity
                     +||Z.grad phi||_infinity
                     +4delta c_delta ||grad Z||_infinity] ds. (15)

Consequently (13) has the further exponent `B_Z(T)`. No smallness of `O` was
needed for this identity. What is not proved is an input-only or source-scale
bound on the actual even feedback `Z`, which is driven in part by `O tensor O`.
If a proposed one-seed repair needs an extra `exp(eta L)` above the base-strain
budget, it must violate `B_Z=o(L)`, lose the angular gap, or use a different
consumer (for example cancellation in the previously chosen denominator).

This is the current first uncontrolled physical quantity for the phase-coherent
pump route: accumulated **even strain and clock relocation**, not the existence
of a nonzero local ladder coefficient. More finite-chain eigenvalues or more
shortest-time trees do not control (15).

The independent full-source issue is cross-label angular mixing: without an
invariant growing gap, (11) is unavailable. Arbitrary unforced data and the full
source collection are not restricted to our parity class. These are precise
scope limits, not proofs that those alternative mechanisms are impossible.

## 7. Exact angular-gap resets cannot occur in the original unforced flow

This obstruction does not assume a frozen source, a Fourier lattice or a small
correction. Let `u` be a smooth finite-energy unforced NS classical branch on
`[0,T]`, with enough Sobolev regularity that its velocity and gradient are
bounded there. Every compact pre-endpoint interval of the target Schwartz
branch has this property. Fix a rotation `R` around the distinguished axis and
write `u^R(x)=R u(R^(-1)x)` and `z=u-u^R`. Rotational covariance and the Leray
projection give the exact difference equation

    z_t+A z=F,
    A=-nu Delta,
    F=-P[(u.grad)z+(z.grad)u^R],
    ||F||_2<=M_0 ||grad z||_2+M_1 ||z||_2,               (16)

where `M_0=sup_[0,T]||u||_infinity` and
`M_1=sup_[0,T]||grad u^R||_infinity` are finite. No pressure term was omitted:
`P` is the orthogonal whole-space Leray projection and has norm one on `L2`.

Where `e=||z||_2^2>0`, let `q=<Az,z>/e`. Self-adjointness of `A` yields

    q'=-2||(A-q)z||_2^2/e+2<(A-q)z,F>/e
       <= (1/2)||F||_2^2/e
       <= (M_0^2/nu) q+M_1^2.                           (17)

Gronwall bounds `q` on every finite subinterval starting with `e>0`. Also

    (log e)' >= -2q-2(M_0/sqrt(nu))sqrt(q)-2M_1.         (18)

The right side has a finite lower integral. Therefore `e` cannot have a first
zero in this interval. The calculation can start at any time with `e>0`; smooth
regularity justifies the differentiations, or a spatial Fourier cutoff gives
the same limit on compact classical intervals.

Consequently

    u(T)=u^R(T)  implies  u(0)=u^R(0).                  (19)

The reverse implication is ordinary forward uniqueness. Hence the exact
rotational symmetry group is constant throughout the smooth lifespan.

In particular a state with nonzero odd sector relative to `N` cannot make that
**entire** sector identically zero at a finite regular handoff to a `2N`-fold
state. A hypothetical sequence of exact symmetry resets with `N_j->infinity`
would require the initial datum to be invariant under rotations through
`2pi/N_j`. Continuity then makes it axisymmetric: for any fixed angle choose
integer multiples of `2pi/N_j` converging to it. Such data never generate the
intended non-axisymmetric seeds.

This does not prevent an individual Fourier coefficient from crossing zero,
or prevent approximate depletion of a whole sector. The constants in (17)--
(18) are solution-dependent and are not bounded uniformly at a putative
singular endpoint. We therefore obtain no input-only lower bound on the size
of a surviving low angular sector. A genuinely quantitative *approximate-gap*
adapter must retain and estimate it; exact reset is not an available repair.

Together, (13), (15) and (19) leave a precise physical transition problem:
control the actual even feedback and the surviving low-sector pressure terms
from one common trace, or develop a full-state mechanism which uses them
instead of discarding them. The localized full-history adjoint and the
arbitrary-data positive producer remain separate unresolved alternatives.
Another exact finite ladder or freely prescribed entry state would not address
these missing estimates.

## Provenance and checks

Primary source: OpenAI, *Finite Time Blowup for Navier--Stokes*, Sections 6--7,
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf .
The current parsed primary statements were inspected on 2026-09-12 at printed
pages 63, 65, 81--83. Web PDF rendering was attempted and returned cache-miss
errors, so this is explicitly a parsed-statement inspection, not a fresh
rendered-page audit or a whole-source correctness claim. No PDF is committed.

`research/check_weighted_pump_action.py` freezes the pressure-constant algebra,
the exact norm-order counter-control, scale exponents, and the
Dirichlet-quotient sign in the no-reset argument. The analytic inequalities and clock construction
are proved above, not inferred from this finite check. The prior exact pump
certificate and one-seed controls are replayed for integration. No independent
mathematical audit, canonical graph promotion, new formal coverage or `NS-R3`
conclusion is claimed.
