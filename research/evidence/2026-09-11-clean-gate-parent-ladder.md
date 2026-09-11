# All-orders inherited-parent ladder in the clean dyadic gate

Date: 2026-09-11. This packet continues
`2026-09-11-clean-dyadic-gate.md` and
`2026-09-11-clean-gate-second-jet-wall.md`.

**Status: exact author Fourier Taylor-tree proof; independent audit and novelty
undetermined.** This is a no-go result for exact finite carrier closure of the
three-parent clean datum, not a no-go theorem for localized packet routing,
augmented initial states, or Navier--Stokes blowup.

## 1. The ladder

Keep the clean family

    k1=(1,0,0),       a1=(0,1,z),
    k2=(0,1,0),       a2=(1,0,z),
    k3=(-z,0,1),      a3=(1,0,z),                         (1.1)

and independent negative-mode scalar coefficients `d1,d2,d3`.  Define lattice
frequencies

    r_n=-n k1-k2,       n>=1.                              (1.2)

The first clean child is

    B((-k1,a1),(-k2,a2))=-2 z e3,                         (1.3)

where `e3=(0,0,1)`.  More importantly, for every integer `n>=1`,

    B((-k1,a1),(r_n,e3))=-e3.                             (1.4)

Thus once the first child exists, every further collision with the inherited
`-k1` parent produces the next frequency on the same vertical polarization
line.

## 2. Unique minimal ancestry

At time derivative order `n`, the homogeneous piece of the quadratic flow has
degree `n+1` in the initial amplitudes.  Consider the coefficient at lattice
frequency `(-n,-1,0)`.  A monomial of degree `n+1` contributing to that
frequency must be represented by `n+1` initial leaves chosen from

    +/-e1, +/-e2, +/-e3.                                   (2.1)

The coordinate sum and leaf budget force exactly

    n copies of -e1 and one copy of -e2.                   (2.2)

Indeed the first coordinate already requires at least `n` negative `e1`
leaves and the second requires one negative `e2` leaf, exhausting all `n+1`
leaves.  There is no room for a positive `e1`, a positive `e2`, or a cancelling
`+/-e3` pair.

A subtree containing only copies of `-e1` vanishes because one divergence-free
plane wave has zero self-interaction.  Consequently every nonzero binary tree
with the leaf multiset (2.2) has the `-e2` leaf joined to a `-e1` leaf first,
and thereafter the remaining `-e1` leaves attach successively.  Up to the
usual symmetric ordering multiplicities, the ancestry is the ladder
(1.3)--(1.4); there is no competing carrier tree with a different
polarization that can cancel it.

## 3. Exact coefficient

Restore the common Fourier factor `-i` in the original projected
Navier--Stokes nonlinearity.  Equation (1.3) gives the first derivative
coefficient

    2 i z d1 d2 e3.                                       (3.1)

Each further ladder step (1.4) contributes one factor `i d1`.  Induction gives
for every `n>=1`

    [d1^n d2] u^(n)_(r_n)(0)
       = 2 i^n z e3,                                      (3.2)

or, including the amplitudes explicitly,

    u^(n)_(r_n)(0) contains
       2 i^n z d1^n d2 e3.                                (3.3)

No viscosity term enters this **minimal-ancestry coefficient**.  A linear
viscous operation preserves lattice frequency and does not merge initial
leaves.  To reach `r_n` from the initial support with only `n` differentiations
requires all `n` quadratic merges encoded above; replacing any one of them by
a linear viscous operation leaves too few merges to reach `(-n,-1,0)`.

## 4. Nonvanishing on the projective-return circuit

The clean three-gate projective return requires

    Q(z)=z^10-z^9+4z^8+2z^6-2z^5
         -8z^3-32z^2+40z-16=0.                            (4.1)

Since `Q(0)=-16`, equivalently `gcd(Q,z)=1`, every projective-return root has
`z!=0`.  Therefore for nonzero `d1,d2`, every ladder coefficient (3.3) is
nonzero.

This strengthens the second-jet observation into an all-orders statement:

> Starting from the three-parent clean datum alone, the exact Fourier Taylor
> tree generates infinitely many distinct frequencies `-n k1-k2`.  Hence the
> three selected carriers cannot be completed to a finite exact Fourier
> replacement history merely by tuning their initial phases or by exploiting
> viscosity.

The scope matters.  This does **not** exclude an augmented initial datum whose
additional modes contribute at the same frequencies, nor a localized
construction in which old parents and children cease to overlap before the
ladder becomes dynamically important.  It excludes the simplest finite
carrier closure of this clean three-parent datum.

## 5. Consequence for the live turnover route

The result separates two jobs that had been conflated:

1. **birth:** the clean family solves the first-source contamination problem;
2. **inheritance:** persistence of the parents creates an infinite Fourier
   ancestry unless a genuine transport/filter/localization mechanism acts.

Accordingly the next useful positive result must control inherited parents,
not discover another first-generation cancellation.  Two concrete tests are
now justified:

* construct a strain/filter window that amplifies the three selected children
  while damping the old parents and at least the first ladder mode; because
  `|r_n|` grows with `n`, damping `r_2` under a common strain can automatically
  dominate the higher ladder if the polarization remains `e3`;
* or prove a finite-time spatial routing lemma that separates the inherited
  parent packet from the newborn child on the same `O(ell/A)` turnover clock.

The affine-strain router already present in the repository makes the first
option directly testable, although its existing matrix was designed for the
older rational circuit and need not work for the clean family.

## 6. Reproducibility

`research/check_clean_gate_parent_ladder.py` verifies (1.3), the symbolic
identity (1.4), the unique degree-`n+1` leaf multiset through twelve exact
finite calibrations, and nonvanishing of `z` on projective-return roots.  The
all-`n` leaf-budget argument and induction are the proof; the finite loop is a
regression check, not the theorem.

No continuum packet estimate, numerical PDE orbit, manuscript/formal update,
or terminal claim promotion is made here.  NS-R3 remains unresolved.
