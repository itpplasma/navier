# Co-located second-generation ancestry wall for the clean dyadic circuit

Date: 2026-09-11. This packet tests whether the contamination-free first gate
can simply be iterated in place under the full original quadratic dynamics.

**Status: exact author Fourier Taylor-tree proof; independent audit and novelty
undetermined.** It is a no-go for the co-located selected-circuit interpretation,
not for spatial routing, auxiliary modes, or a different nonlinear return class.

## 1. Why time order matters

For the clean three-parent datum, the first selected children are born at
Taylor order one and are quadratic in the initial amplitudes.  A collision of
two such children is therefore quartic in the initial amplitudes and first
appears at Taylor order three: two first-generation amplitudes are `O(t)`,
their quadratic forcing is `O(t^2)`, and one more time integration gives
`O(t^3)`.

Thus the nominal second selected gate is not controlled by the first
nonlinear derivative.  One must inspect the complete top homogeneous
coefficient at order `t^3`.

## 2. One second-generation target has unique initial leaves

In lattice coordinates relative to `(k1,k2,k3)`, the first selected children
are

    g1=(-1,-1,0),       g2=(1,0,-1),       g3=(1,0,1).    (2.1)

The nominal second-generation target

    h=g1-g3=(-2,-1,-1)                                  (2.2)

is particularly rigid.  Its `l1` norm is four.  Any quartic Taylor tree for
`h` therefore has exactly the initial leaf multiset

    {-e1,-e1,-e2,-e3}.                                   (2.3)

There is no spare cancelling pair.  Consequently every degree-four
contribution to `h` carries the same scalar amplitude monomial

    d1^2 d2 d3.                                           (2.4)

Initial amplitude magnitudes and phases cannot alter the relative
polarizations of the different tree topologies contributing at this order.
This includes the calibrated common-phase amplitudes used to tune the selected
three-gate symbol gain.

The target is absent at Taylor orders one and two, so order three is its first
appearance in the top homogeneous dynamics.

## 3. Intended selected tree versus inherited-parent trees

Suppress the common scalar monomial (2.4).  The contribution coming from the
intended collision of the two first-generation selected children is

    V_sel(z)=
    (-2 i z (z^3+2z-4)/(3(z^2-4z+6)),

     -2 i z (z^4-8z^3+14z^2-16z+8)
       /(3(z^2-4z+6)(z^2-2z+2)),

     -2 i z (z^6-4z^5+7z^4-8z^3+14z^2-16z+8)
       /(3(z^2-4z+6)(z^2-2z+2))).                         (3.1)

The complete Taylor recurrence also contains trees in which an inherited
parent collides with a second-jet mode before reaching the same target.  Their
sum is a second vector `V_old(z)`, frozen explicitly in the companion checker.
It is of the **same amplitude degree and the same time order** as (3.1); it is
not a lower-order perturbation that disappears in the large-amplitude
`t=beta/A` scaling.

The cross product has a component

    [V_sel x V_old]_2
      = - z P(z) /
        [9 (z^2-4z+5)(z^2-4z+6)
           (z^2-2z+2)^2 (z^2-2z+3)],                     (3.2)

where

    P(z)=3z^12-26z^11+141z^10-530z^9+1481z^8
         -3066z^7+4547z^6-4418z^5+2024z^4
         +896z^3-1908z^2+1048z-160.                      (3.3)

The clean projective-return parameter satisfies

    Q(z)=z^10-z^9+4z^8+2z^6-2z^5
         -8z^3-32z^2+40z-16=0.                           (3.4)

Exact polynomial arithmetic gives

    gcd(Q,P)=1,       gcd(Q,z)=1.                         (3.5)

All real denominators in (3.2) are positive.  Hence at **every** projective
return root of `Q`,

    V_sel(z) x V_old(z) != 0.                             (3.6)

The old-parent contribution is not parallel to the intended selected
polarization.

## 4. Consequence: the exact symbol circuit is not the co-located leading NS orbit

The actual quartic/order-three coefficient at `h` is

    V_full(z)=V_sel(z)+V_old(z).                          (4.1)

By (3.6), `V_full` is not projectively equal to `V_sel` at any clean circuit
root.  Therefore even after solving the entire first-generation sibling
problem, the co-located original Navier--Stokes Taylor expansion does **not**
follow the selected three-mode gate at the first possible second-generation
order.

This is stronger than the inherited-parent ladder wall.  The ladder showed
that new frequencies appear before the desired replacement is complete.  The
present result shows that inherited ancestry also contaminates the **desired
second-generation frequency itself**, changing its polarization at leading
nonlinear order.

There is no rescue by choosing the special gain-tuning amplitudes: the unique
leaf multiset (2.3) forces both (3.1) and the contaminating term to carry the
same scalar monomial.

## 5. What this rules out and what survives

This closes the simplest interpretation of the new exact dyadic identity:

    put the three clean parent packets in one interaction region,
    let the first selected children appear,
    let those children collide again in the same region,
    and read off the next selected gate.                          (5.1)

At gate two, (5.1) is already wrong at the top homogeneous Taylor coefficient.
The exact identity `T^3=2I` remains valuable carrier algebra, but it is not a
closed asymptotic orbit of the co-located NS vector field.

A successful use of the circuit must instead change the spacetime ancestry:

1. **spatial routing:** newborn children must be separated from inherited
   parents before the next collision, then paired in new interaction regions;
2. **mode-specific purification:** an auxiliary background may alter the
   unwanted polarization before the next selected gate, provided the complete
   multi-mode geometry survives;
3. **augmented nonlinear state:** retain and deliberately use the old-parent
   trees rather than asking them to vanish.

The concurrent mode-specific affine purifier is relevant to item 2 at one
frequency, but its extension to all three channels and finite-energy
localization is still a separate load-bearing problem.

## 6. Reproducibility

`research/check_clean_gate_second_generation_wall.py` freezes `V_sel`, the
complete inherited-parent vector `V_old` for target (2.2), the cross-product
obstruction polynomial (3.3), the coprimality checks (3.5), and the unique
quartic leaf multiset.

No finite-time packet routing theorem, finite-energy background, manuscript or
formal change, or terminal NS-R3 claim is made here.
