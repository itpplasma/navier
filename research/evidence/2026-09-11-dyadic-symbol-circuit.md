# Exact three-pulse dyadic Leray-symbol circuit

Date: 2026-09-11. Repository input:
`itpplasma/navier@647e25be018a17af75b62194140a35c4a4591247`.

**Status: exact author algebra at the original Leray quadratic symbol; independent
mathematical audit and novelty undetermined.** No Navier--Stokes trajectory,
localized turnover, common Schwartz datum, unforced singularity, or arbitrary-
data regularity theorem is constructed. This packet does not promote PLAN,
the manuscript, the canonical proof graph, or formal status.

The purpose is to attack the missing turnover operation in
`2026-09-11-supercritical-turnover-contract.md` at the first place where the
previous source-specific route had failed: reproduce a genuinely
three-dimensional parent geometry at a smaller scale rather than merely
create another Fourier carrier. The result is positive at the exact
principal-symbol level. It is also accompanied by an exact contamination
audit showing why it is not yet a closed Fourier subsystem.

## 1. Original Leray pair and notation

For nonzero Fourier wavevectors `p,q` and real transverse polarizations
`a,b`, write

    B((p,a),(q,b))
      = P_(p+q)[(a.q)b+(b.p)a],                         (1.1)

where `P_k=I-k tensor k/|k|^2`. In the Fourier equation for real
incompressible Navier--Stokes, the common coefficient is `-i` times (1.1).
Thus (1.1) is not an averaged or modified nonlinearity: it is the exact
symmetric pair contribution of the original convective term after Leray
projection, with only the common Fourier phase suppressed.

Negative wavevectors of a real field carry the conjugate scalar coefficient
and the same real polarization. All calculations below retain this convention.

## 2. A scoped two-parent wall

There is a useful reason to look beyond the simplest two-parent relay.
Consider, after rotation and scaling,

    p=(1,0,0),
    q=R(cos theta,sin theta,0),

and transverse polarizations

    a=(0,1,z),
    b=(-sin theta,cos theta,w).

Let `e` and `f` be the sum- and difference-frequency children from
`p,q`, and ask that their next collisions reproduce polarizations parallel
to `a` at `2p` and `b` at `2q`. Put `t=tan(theta/2)`. Exact factorization of
the two orientation residuals contains, away from nonzero geometric factors,

    (1+t^2) w + (t^2-1) z,                               (2.1)
    (t^2-1) w + (1+t^2) z.                               (2.2)

Their determinant is exactly

    4 t^2.                                                (2.3)

Hence for a noncollinear pair `t != 0` and unequal lengths `R != 1`, exact
projective recurrence in this particular `p+/-q -> 2p,2q` architecture
forces

    z=w=0.                                                (2.4)

The polarizations are then planar. When `R=1`, both second-generation
interactions vanish identically. This is **not** a theorem that every
two-parent NS cascade is planar; it excludes this concrete Hadamard-style
two-parent recurrence and motivates the three-parent search below.

## 3. An exact rational three-parent circuit

Take the three wavevectors

    k1=(1,0,0),
    k2=(1,1,0),
    k3=(1,0,1),                                           (3.1)

and the real divergence-free polarizations

    a1=(0,1,1/2),
    a2=(1,-1,-2/3),
    a3=(1,0,-1).                                          (3.2)

The wavevectors span R3. Define one generation by the signed collision rule

    k1'=-k1-k2,
    k2'= k1-k3,
    k3'= k1+k3,                                           (3.3)

and let each new polarization be the exact Leray pair (1.1) with the same
sign choices. On wavevectors, (3.3) is the integer matrix

    T=[[-1,-1, 0],
       [ 1, 0,-1],
       [ 1, 0, 1]].                                      (3.4)

It satisfies the exact identity

    T^3=2 I.                                              (3.5)

The stronger fact is that the polarizations close projectively as well.
The three exact generations are

**Generation 1**

    (-2,-1,0) : (-1/5,  2/5,  1/6),
    ( 0, 0,-1): (-1/2,  1,    0),
    ( 2, 0, 1): ( 1/10, 1,   -1/5).                      (3.6)

**Generation 2**

    ( 2, 1, 1): (-1/12,  1/6,   0),
    (-4,-1,-1): ( 5/36, -5/18, -5/18),
    ( 0,-1, 1): (13/60,-13/30,-13/30).                   (3.7)

**Generation 3**

    2 k1 : (5/54) a1,
    2 k2 : (13/120) a2,
    2 k3 : -(13/360) a3.                                 (3.8)

Every displayed polarization is exactly transverse to its displayed
wavevector. Thus after three selected nonlinear generations the entire
three-dimensional wavevector geometry is doubled and each polarization
returns to its original projective line. No floating-point search or
approximate alignment is used in (3.5)--(3.8).

This is the first exact recursive polarization geometry in the present
programme that survives the genuinely three-dimensional Leray projection.
It is a circuit identity, not yet a claim about a solution following only
these selected collisions.

## 4. Exact phase closure and a supercritical selected-circuit gain

Restore the common Fourier factor `-i`. If `z_j` is the scalar coefficient
multiplying the current real polarization, the selected gate has scalar map

    z1'=-i conjugate(z1) conjugate(z2),
    z2'=-i z1 conjugate(z3),
    z3'=-i z1 z3.                                        (4.1)

Let

    d1=5/54,   d2=13/120,   d3=13/360

and start with the common phase

    z_j=i alpha d_j,       alpha>0.                       (4.2)

Three iterations of (4.1) give, before the projective factors in (3.8),

    (z1''',z2''',z3''')=(i C alpha^8,
                          i C alpha^8,
                         -i C alpha^8),                   (4.3)

where

    C=d1^4 d2^2 d3^2
     =28561/25389989167104.                               (4.4)

The minus sign in the third scalar component is canceled by the minus
projective multiplier in (3.8). Relative to the initial physical
coefficients, **all three outputs have the same exact gain**

    g_circuit = C alpha^7.                                (4.5)

Therefore any prescribed positive projective gain can be represented
algebraically. In particular the canonical half-scale target from the
supercritical turnover contract,

    s=2,       g=5/2,                                    (4.6)

is obtained by the exact condition

    alpha^7=63474972917760/28561.                         (4.7)

Numerically `alpha` is about 21.6402015904. The corresponding magnitudes of
the three initial scalar coefficients are approximately

    alpha d1 = 2.00372,
    alpha d2 = 2.34436,
    alpha d3 = 0.781452.                                  (4.8)

The selected circuit therefore hits the **correct formal turnover window**:
`g=5/2>2`, while the half-scale same-shape localized energy ratio would be

    g^2/2^3=25/32<1,                                     (4.9)

and the critical/Reynolds ratio would grow by `g/2=5/4`.

Equations (4.5)--(4.9) do **not** prove energy growth in an NS solution.
On a fixed-volume Fourier field, interpreting the selected circuit as a
literal same-time replacement would violate the fixed-volume energy wall
already proved in the turnover-contract packet. Physical localization and
actual time evolution are load-bearing.

## 5. Full first-generation audit: the global Fourier subsystem is not closed

For a real initial field containing all six modes `+/-k1,+/-k2,+/-k3`,
the exact first quadratic generation has twelve nonzero output wavevectors:

    (-2,-1,-1), (-2,-1,0), (-2,0,-1),
    ( 0,-1, 0), ( 0,-1,1), (0,0,-1),
    ( 0, 0, 1), ( 0, 1,-1), (0,1,0),
    ( 2, 0, 1), ( 2, 1, 0), (2,1,1).                    (5.1)

The companion checker freezes every corresponding rational polarization.
In particular:

* the `k1,k3` pair is favorable: its sum and difference outputs are both
  selected circuit children (up to conjugation);
* the `k1,k2` pair produces the selected `-k1-k2` child **and** the nonzero
  sibling `k1-k2=(0,-1,0)`, with polarization `(-1,0,7/6)`;
* the unused `k2,k3` collision produces additional nonzero children, e.g.
  `(2,1,1)` with polarization `(10/9,-10/9,-10/9)`.

Thus the three selected modes are **not** an invariant finite Fourier
subsystem. This packet does not delete the sibling modes and does not call
(3.3) an exact NS orbit.

The contamination pattern does, however, suggest a concrete localized
implementation test. The `k1,k3` packets can collide in one interaction
region, because both sign outputs are useful. A `k1,k2` collision can occur
in a second region, with its unwanted sibling routed away. The `k2,k3`
packets should not overlap at leading order. Such routing is meaningful only
for localized packets and must retain the nonlocal Leray/pressure tail.
No such routed gate is proved here.

## 6. Relation to de-forcing and the surviving route

The new result fits both active negative architectures:

1. **Supercritical turnover route.** The exact symbol has a genuine
   three-dimensional recursive geometry with scale factor two, and its
   selected amplitude algebra can be tuned to the interior target `g=5/2`.
   What remains is to realize one routed, localized, unforced physical gate
   satisfying the six acceptance items in
   `2026-09-11-supercritical-turnover-contract.md`.

2. **OpenAI pulse de-forcing route.** The angular-heat packet has just
   excluded passive storage/import of all future high-angular seeds.
   A nonlinear near-activation birth mechanism is one of the explicitly
   surviving alternatives. The circuit above gives an exact polarization
   and wavevector recurrence that could generate such seeds from a finite
   starter set. Because the source needs exponentially small entry seeds,
   a weak-overlap implementation can in principle operate in a perturbative
   amplitude regime; proving this with the full source propagator remains
   separate work.

The next positive theorem should therefore not be another carrier-creation
identity. It should be a **localized routed-gate lemma**: a finite-time
original-NS packet interaction in which the desired selected child has a
quantitative lower bound, all siblings/pressure tails have controlled
destinations or norms, viscosity is retained, and the output is admissible
for the next gate without resetting the inherited state.

## 7. Reproducible validation

`research/check_dyadic_symbol_circuit.py` was executed before upload and
passed **72 exact symbolic assertions**. It checks:

* all input/generation transversality identities;
* `T^3=2I`;
* every rational wavevector and polarization in (3.6)--(3.8);
* the projective constants and exact circuit constant (4.4);
* the complex phase recurrence (4.1)--(4.5);
* the exact rational `g=5/2` calibration and turnover-window ratios;
* all twelve first-generation real-field outputs and their transversality;
* the two-parent orientation-factor equations and determinant (2.3).

The frozen JSON output records these values. SymPy exact arithmetic is used;
there is no numerical PDE trajectory in this checker. No full checkout,
repository-wide verifier, manuscript build, Lean build, or independent
mathematical audit was performed for this additive packet.
