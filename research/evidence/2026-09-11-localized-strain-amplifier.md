# Finite-energy short-time localized strain amplifier

Date: 2026-09-11. Repository input before this note:
`itpplasma/navier@a254453e988a4120ef7bdf1637586b51f3f25aab`.

**Status: author proof from the exact relative-energy identity and standard local
smooth Navier--Stokes theory; independent mathematical audit and novelty
undetermined.** This proves a finite-energy, fixed-viscosity, short-time
amplification mechanism at every spatial scale. It does **not** prove a
frequency-pure mode purifier, spatial routing/recombination, a regenerative
turnover, or blowup. No canonical/manuscript/formal status is promoted.

The preceding mode-specific affine purifier is exact for finite time but has
infinite energy. The point here is to remove that particular objection without
pretending that the full gate--route--purify chain is complete.

## 1. Exact compact realization of an affine strain germ

Let `S` be any real trace-free `3 x 3` matrix and put

    L(x)=Sx.

The homogeneous vector identity

    curl[-x cross L(x)/3]=L(x)                             (1.1)

holds whenever `tr S=0`. Choose a real cutoff `chi_R` which is one on
`B_(3R)` and supported in `B_(4R)`, and define

    B_0(x)=c curl[-chi_R(x) x cross (Sx)/3].               (1.2)

Then `B_0` is real, compactly supported, smooth and solenoidal, and

    B_0(x)=c Sx,      grad B_0=cS       on B_(3R).         (1.3)

Thus every affine trace-free strain can occur as the **exact local germ of an
admissible Schwartz datum**. No harmonic pressure has been chosen; the pressure
will be the canonical whole-space pressure of the actual solution.

For the purifier normal form take an orthonormal frame `(e,f,n)` and

    S=-e tensor e+f tensor f,                              (1.4)

so `S e=-e`, `S f=f`, `S n=0`.

## 2. Compact desired and rejected packet directions

Fix a nonzero carrier number `K`; for the clean doubled-mode application one
may take `K=2`. Choose a smooth radial cutoff `chi_L`, equal to one on `B_L`
and supported in `B_(2L)`, and put

    phi_L(x)=K^(-1) chi_L(x) sin(K n.x).                   (2.1)

Define the exact compact solenoidal packets

    w_e=curl(phi_L f),
    w_f=curl(phi_L e).                                    (2.2)

The signs are irrelevant. As `L` tends to infinity,

    w_e = -chi_L cos(K n.x)e + O((KL)^(-1)),
    w_f =  chi_L cos(K n.x)f + O((KL)^(-1))               (2.3)

in the normalized `L2` sense, while their gradient Rayleigh quotients converge
to `K^2`. Consequently

    <w_e,S w_e>/||w_e||_2^2 -> -1,
    <w_f,S w_f>/||w_f||_2^2 -> +1,                        (2.4)

    ||grad w_e||_2^2/||w_e||_2^2 -> K^2,
    ||grad w_f||_2^2/||w_f||_2^2 -> K^2.                  (2.5)

These limits follow directly from (2.2): the derivative of the oscillatory
factor gives the displayed leading term, whereas differentiating the scaled
cutoff costs `O(L^(-1))`; oscillatory averages of `sin^2` and `cos^2` have the
same leading volume. Equivalently one can rescale to the unit ball and use the
Riemann--Lebesgue lemma.

For `K=2`, take `L` sufficiently large that, for example,

    <w_e,S w_e>/||w_e||^2 < -19/20,
    ||grad w_e||^2/||w_e||^2 < 17/4,                      (2.6)

and

    <w_f,S w_f>/||w_f||^2 > 19/20.                        (2.7)

Choose the base-strain strength

    c=5.                                                   (2.8)

The support of both packets lies in `B_(2L)`, where (1.3) is exact after
choosing `R>L`.

## 3. The full nonlinear relative-energy identity

Let `B(t)` be the classical unforced viscosity-one Navier--Stokes solution from
`B_0`. Let `U(t)` be the classical solution from `B_0+w_0`, where `w_0` is one
of the packets above, or a fixed sufficiently small scalar multiple of it.
On their common local lifespan put

    w=U-B.

Subtracting the two original equations gives

    w_t-Delta w+P div(B tensor w+w tensor B+w tensor w)=0. (3.1)

Taking the global `L2` pairing with `w` gives the **exact nonlinear identity**

    (1/2) d/dt ||w||_2^2 + ||grad w||_2^2
       = - integral w^T (grad B) w dx.                    (3.2)

The transport by `B` cancels by incompressibility, the complete self-term
`w.grad w` cancels in energy, and pressure is removed only by the exact
solenoidal pairing. Thus no linearization assumption is needed for (3.2).

At time zero, (1.3) and the support property yield

    (1/2) E_e'(0)
       = -5 <w_e,S w_e>-||grad w_e||^2 > (1/2)||w_e||^2,  (3.3)

using (2.6), whereas

    (1/2) E_f'(0)
       = -5 <w_f,S w_f>-||grad w_f||^2 <0.                (3.4)

The numerical constants in (3.3) are only a convenient strict interior
choice. Any strict production/dissipation margins suffice.

Smooth local theory gives `B,U` and continuity of the quantities in (3.2).
Therefore there are numbers

    delta>0,       eta_+>0,       eta_->0                 (3.5)

(depending only on the two fixed dimensionless initial data) such that

    ||U_e(delta)-B(delta)||_2^2
       >= (1+eta_+) ||w_e||_2^2,                          (3.6)

    ||U_f(delta)-B(delta)||_2^2
       <= (1-eta_-) ||w_f||_2^2.                          (3.7)

After reducing the initial perturbation amplitudes if desired, the two
solutions can be placed in one fixed bounded set of smooth initial data and a
common positive `delta` can be chosen. Equations (3.6)--(3.7) are genuine
finite-time statements for finite-energy original Navier--Stokes solutions,
not affine reference rates.

They do **not** say that an arbitrary mixture is decomposed and purified by one
finite-energy flow. The theorem certifies finite-energy directional
amplification/attenuation, which is a necessary component of the routed
architecture.

## 4. Exact scaling to every physical frequency at fixed viscosity

Let `V(s,y)` be either of the viscosity-one solutions above. For arbitrary
fixed physical viscosity `nu>0` and frequency scale `b>0`, define

    V_b(t,x)=nu b V(nu b^2 t,bx).                          (4.1)

A direct change of variables shows that (4.1) solves the original equation
with viscosity `nu`. The physical time corresponding to the fixed
`dimensionless` interval `delta` is

    Delta t_b=delta/(nu b^2).                              (4.2)

Thus the localized finite-energy amplifier operates on the same parabolic
clock as the exact affine purifier.

The initial spatial radius is `O(b^(-1))`; the velocity and gradient scales
are

    |V_b| ~ nu b,
    |grad V_b| ~ nu b^2.                                  (4.3)

Most importantly,

    ||V_b(0)||_2^2 = (nu^2/b) ||V(0)||_2^2,               (4.4)

while

    ||V_b(0)||_3^3 = nu^3 ||V(0)||_3^3.                   (4.5)

So the local `L2` energy cost of this strain gadget decreases as the carrier
frequency rises. There is no fixed-viscosity energy scaling obstruction to
using such a gadget at small scales. Higher Sobolev norms do grow with `b`, so
preloading infinitely many gadgets into one Schwartz datum is **not** justified
by (4.4); a successful autonomous cascade must generate or transport the
strain dynamically.

The amplification and attenuation factors in (3.6)--(3.7) are unchanged by
(4.1), because both numerator and denominator of each relative energy ratio
carry the same factor `nu^2/b`.

## 5. Relation to the clean dyadic route

The current algebra has established:

* an exact clean first dyadic source;
* unavoidable inherited-parent ancestry at later gates;
* nonzero intended projections at all contaminated second-generation targets;
* exact mode-specific affine purification of any nonzero intended projection;
* the present finite-energy short-time realization of a strict strain
  amplifier/attenuator on the correct parabolic clock.

This removes the statement "the purifier only exists at infinite energy" as a
fatal objection. It does **not** yet implement the purifier on three separated
clean-gate target packets, because the actual compact background in this note
is designed together with one local packet. The remaining operation is an
autonomous **router/recombiner** inside one forward history:

    target birth
      -> physical separation from inherited parents
      -> local finite-energy strain discrimination
      -> recombination into the next clean pairing graph.          (5.1)

No heat dispersion provides the separation in (5.1), and independent copies of
this theorem cannot simply be reset at successive times. This is now the first
unproved operation on the negative route.

## 6. Reproducibility and audit boundary

`research/check_localized_strain_amplifier.py` verifies the generic curl
extension identity (1.1), the purifier normal form, strict rational production
margins, and all fixed-viscosity scaling relations (4.1)--(4.5). The finite-time
persistence in Section 3 uses ordinary smooth local NS theory and continuity;
the checker is not a PDE solver.

No repository-wide verifier, manuscript build, Lean build, independent audit,
router/recombiner, recursive turnover, common Schwartz cascade datum, or
terminal NS-R3 result is supplied here. NS-R3 remains unresolved.
