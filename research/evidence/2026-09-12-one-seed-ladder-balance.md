# One odd seed populates the ladder but does not inherit the free bridge controls

Date: 2026-09-12. Input: `itpplasma/navier@db2f4c1e861424060cb7006c0a55508b8f4772e4`.

**Author proof and exact rational coefficient certificates. Independent audit
pending.** This wave tests the causal composition, not another independently
prepared six-mode bridge. The proposed dynamically generated ladder survives
all shortest-time trees. However, a conserved Fourier charge forces seed orders
`1,1,3,3,9,9` in its six ancestors and `6,6,2,2` in the next-parent quartet.
The latter's outer/inner pair-product ratio is `O(|A|^8)` at a fixed sufficiently
short positive time. It cannot satisfy the existing four-parent consumer's
fixed nonzero pair-product ratio as the single seed tends to zero.

This excludes substituting one small seed for the six *independently tunable*
ancestors in the proved bridge. It does not exclude a large/nonperturbative
one-seed transition, a seed-dependent long horizon, a different consumer for
all returned modes, or additional independent charge sectors.

## Working packet and prediction

TERMINAL CLAIM: original unforced incompressible NS on `R3`, fixed `nu>0`,
divergence-free Schwartz data; either arbitrary-data global classical
regularity or one datum with a finite classical endpoint.

ESTABLISHED: the finite-time six-input frozen bridge has a rank-four quadratic
target map; even source pumping cannot create the first odd seed; passive
interstage storage and the direct fixed-label adapter are not valid suppliers.

FIRST GAP: causally generate the six ancestors with the freedom and amplitude
balance actually needed by that bridge, without resetting them.

PREDICTION: the dynamic shear ladder may survive the complete convolution, but
its outputs from one seed will have dependent phases and unequal seed orders.
A nonzero output at each key will not imply a rank-four accessible target map.

FALSIFIER: an outer next-parent term of seed degree below six; cancellation of
all shortest-time ladder coefficients; or a nonvanishing fixed outer/inner
pair-product ratio at arbitrarily small seed with fixed pump and short horizon.

FORBIDDEN INFERENCES: selected tree = full coefficient; finite coefficient =
turnover; nonzero outputs = independent controls; frozen lattice = physical NS;
independent entry traces = one common Schwartz initial datum.

CHECK: exact charge, complete shortest-time recurrence, rational radical
bounds, and analytic small-seed dependence at fixed finite horizon.

## 1. Model and two independent amplitude phases

Use the complete frozen source-reference equation on the rank-two torus:

    u_t = L u - P[(u.grad)u],
    L_k = -P_k K_0 - mu |k|^2 I,
    K_0 = [[0,1,0],[1,0,0],[0,0,0]],   mu=3/5.

All Fourier outputs and both transverse components are retained. Let

    h=(1/10,0,1/2),      d=(1/20,0,1),
    a=(1,-sqrt(26)/5,-1/5),
    b=(1,+sqrt(401)/20,-1/20).

Initialize only

    u_h=A a,  u_-h=conj(A) a,
    u_d=B b,  u_-d=conj(B) b.                         (1)

Here `B!=0` is fixed independently of the seed `A`. The pump is the decaying
source branch. At `A=0` it is an exact single-wave solution: its self-convection
vanishes and its amplitude is `B exp(lambda_d,- t)`. Standard mild contraction
in `H^r`, `r>2`, gives real-analytic dependence on `A,conj(A)` near this smooth
pump on each sufficiently short fixed interval. The constants may depend on
`B`, the interval, the fixed torus and Sobolev index. There is no uniform
physical/interstage or large-pump claim.

In integer keys, write `k=(x/20,0,z/2)`. Every reachable key uniquely equals
`n h+p d`, where

    n=(2x-z)/3,       p=(2z-x)/3.                     (2)

The quantity `I=2x-z=3n` is additive under *every* convolution. The pump has
`I=0`, the seed `I=3`, and its reality partner `I=-3`. The source linear
multiplier preserves each key. Thus a monomial of seed degree `j+l` in
`A^j conj(A)^l` at key `k` must obey

    j-l=n,      j+l>=|n|.                            (3)

This remains true through arbitrary pump insertions, all generated means,
shears, and all non-selected sidebands.

Equivalently, choose translations fixing `d.x` but varying `h.x` by `theta`.
Translation covariance sends `A` to `A exp(i theta)` and the output at `k` to
`exp(i n theta)u_k`. Analyticity therefore gives the all-orders form

    u_k(A)=A^n F_k(|A|^2;B,T),             n>=0,
    u_k(A)=conj(A)^(-n) F_k(|A|^2;B,T),    n<0.       (4)

Both statements concern the full lattice, not a six-mode truncation.

## 2. Complete shortest-time calculation

For a key `n h+p d`, at least `|n|+|p|` initial leaves are necessary.
A binary convolution tree on that many leaves has `|n|+|p|-1` vertices.
At this *shortest possible time order*, no source-linear/viscous vertex and
no opposite-sign leaf pair can occur. Every leaf has the sign of `n` or `p`.
Consequently the exact shortest-time coefficient is obtained by summing all
ordered partitions inside that signed two-generator cone.

Strip the common factor `(-i)^(a+b-1)` and the initial amplitude monomial.
With `W_10=a`, `W_01=b`, the complete recurrence is

    (a+b-1) W_ab
      = sum_(0<=i<=a,0<=j<=b)
          P_(k_ab)[(W_ij.k_(a-i,b-j)) W_(a-i,b-j)]. (5)

Zero-degree factors are absent. Terms with zero total wavevector vanish.
Pure self pairs vanish by transversality. Formula (5) includes *all*
shortest-time trees, whether or not they can be described as a shear ladder.

At these orders the planar components are rational. The transverse component
is a rational linear combination of `sqrt(26)` and `sqrt(401)` because the
nonlinear advection has no transverse derivative. The checker therefore uses
only `fractions.Fraction`, followed by integer-square-root enclosures for the
growing coordinate

    c_+(v,k)=(v_x-v_y/sqrt(1+(k_x/k_z)^2))/2.          (6)

The following signs are certified; decimal sizes are orientation only.
Time orders are measured from (1), not from a separately prescribed shear.

| Output | `(n,p)` | First time order | Stripped growing coefficient, approximately |
|---|---:|---:|---:|
| half key `-1` | `(-1,1)` | 1 | `-7.3604e-2` |
| half key `5` | `(3,-1)` | 3 | `+2.3099e-5` |
| half key `-4` | `(-3,2)` | 4 | `+6.1201e-5` |
| half key `8` | `(5,-2)` | 6 | `+4.0230e-7` |
| half key `-7` | `(-5,3)` | 7 | `-1.2188e-7` |
| half key `11` | `(7,-3)` | 9 | `+6.5786e-10` |
| half key `-10` | `(-7,4)` | 10 | `+2.1002e-10` |
| half key `14` | `(9,-4)` | 12 | `+1.1710e-12` |
| half key `-13` | `(-9,5)` | 13 | `-3.7680e-13` |
| next parent `+5` | `(6,-2)` | 7 | `+2.1860e-8` |
| next parent `-4` | `(-6,4)` | 9 | `-2.2030e-9` |
| next parent `+2` | `(2,0)` | 3 | `+1.4053e-3` |
| next parent `-1` | `(-2,2)` | 3 | `-2.7836e-4` |

The existing half key `2` is the initial seed. Thus every required half-grade
ancestor is genuinely populated. Its lowest nonzero seed degree is respectively
`1,1,3,3,9,9` for `2,-1,5,-4,14,-13`.

The exception to the naive shortest-leaf time is the next `+2` parent, `2h`.
Its two-leaf term is a self pair and is exactly zero, including any linear
polarization changes. There is no three-leaf representation. At four leaves,
the possible all-seed tree is again collinear and zero. The surviving monomial
is `A^2 |B|^2`; the complete unrestricted cubic-time Euler recurrence with both
signs of both inputs gives the strictly positive coefficient in the table.
Linear vertices cannot change these conclusions because they add no frequency.
The unrestricted low-order recurrence also checks transversality, reality and
agreement with the cone extraction where both apply.

For fixed nonzero `B`, finite differentiability in time of the amplitude
variations turns these nonzero finite jets into nonzero leading seed
coefficients for every sufficiently small positive `T`. No convergent Taylor
series in time, long-time propagation or singularity is inferred.

## 3. Causal composition restores an exact amplitude obstruction

Let `Y_5,Y_-4,Y_2,Y_-1` be the *complete nonlinear* next-parent growing
coordinates at one fixed sufficiently short time `T>0`. Formula (4) and the
nonzero coefficients just proved imply

    Y_5   = A^6       [f_5(B,T)+O(|A|^2)],
    Y_-4  = conj(A)^6 [f_-4(B,T)+O(|A|^2)],
    Y_2   = A^2       [f_2(B,T)+O(|A|^2)],
    Y_-1  = conj(A)^2 [f_-1(B,T)+O(|A|^2)],           (7)

with all four `f` nonzero. Their leading small-`T` monomials are

    f_5  ~ (-i)^7 c_5 conj(B)^2 T^7,
    f_-4 ~ (-i)^9 c_-4 B^4 T^9,
    f_2  ~ (-i)^3 c_2 |B|^2 T^3,
    f_-1 ~ (-i)^3 c_-1 B^2 T^3.                     (8)

The four constants `c` have the signs in the table. In particular

    (Y_5 Y_-4)/(Y_2 Y_-1)
       = |A|^8 [R(B,T)+O(|A|^2)] -> 0.             (9)

As `T->0`, `R(B,T)` has a nonzero coefficient times `|B|^2 T^10`.
All error constants are for the fixed pump and fixed short interval.

The two-decomposition source consumer requires the ratio of these pair
products to be a fixed nonzero number (or in a compact set bounded away from
zero), with its causal growth-mismatch retuning included. Equation (9) rules
this out in the one-small-seed regime. Adjusting the seed phase does not help:
it cancels *exactly* in both pair products. At fixed pump/horizon the accessible
quartet depends on only one complex seed, not four independent complex controls.
The rank-four theorem for freely prescribed six ancestors cannot be composed
with this supplier by treating its correlated outputs as free variables.

This is not a proof that no full returned-state consumer works. Other generated
modes could participate in a different cancellation architecture, and the
normal-form functions in (7) are not controlled on a seed-dependent long
interval. Those are new missing hypotheses, not consequences of rank four.

## 4. Necessary correction to the single-pump block wording

A pump Fourier mode shifts a perturbation by `+d` and `-d`. The six displayed
half-grade modes are therefore **not** a closed linearization: modes such as
`h+d` at axial grade `3/2` also occur. The previously computed two-directional
coefficients and their negative products are correct projected symbols, not
a proof of stability of the entire infinite pump-coupled system.

What is invariant linearly is `n` in (2). With reality, the three complementary
pairs occupy the distinct classes `|n|=1,3,9`, each accompanied by infinitely
many pump shifts. A completely zero class stays zero under the single-pump
linearization. The earlier need for nonlinear cross-class generation survives;
its explanation must use these charge classes, not a six-mode block truncation.
The parity evidence/checker wording is corrected accordingly in this wave.

## 5. Recomputed frontier and scope

The cheapest one-seed ladder test is now resolved in both directions: complete
shortest-time birth succeeds, but the attempted free-bridge composition fails
at small seed by (9). More shortest-time ladder coefficients would not address
the first gap.

The next distinct constructive test is to use the **full pump-coupled linear
chains** and ask whether growing/decaying polarization feedback provides a
nonperturbative amplification mechanism missed by the projected two-mode
symbols. Such a mechanism must still supply independent charge classes or a
new full-state consumer and control its nonlinear saturation. A strong enough
physical history would have to feed UE1, then UE2 (full correction), UE3 (one
Schwartz trace) and UE4 (singular observation/classical-branch identification).
No part of that remaining whole-space chain is promoted here.

Companion: `research/check_one_seed_ladder.py`. The directly relevant retained
pump and finite-time bridge checkers were replayed. Structural verification is
not mathematical or formal certification. No external theorem is newly
imported; no independent review or novelty claim is made.
