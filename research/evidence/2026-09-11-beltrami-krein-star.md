# Beltrami Krein structure removes the `exp(c rho)` first-star wall

Date: 2026-09-11. Repository input:
`itpplasma/navier@3e67b4d51c23ea067ed2726bd1d6571819b2be6f`.

**Status: exact linearized identity plus exact two-sector consequence.** The
thin-shell checkpoint left open whether the raw `o(1)` Beltrami localization
defect is destroyed by a generic Gronwall factor `exp(C rho)`, where
`rho=P/(nu N)->infinity`. For the first slow/near-shell sideband star the answer
is no: the Beltrami linearization is skew with respect to the quadratic form
`curl-Lambda`, which forces an `R^-1` asymmetry between forward and reverse
couplings. At the useful Raman scaling `rho^2/R=O(1)`, the spectral rate stays
`O(1)`. The physical Euclidean norm can have an `O(sqrt(R))` nonnormal factor,
but the preceding shell width can beat that factor.

The exact two-sector ledger is frozen by
`research/check_beltrami_krein_star.py`.

This theorem does not control off-shell perturbation frequencies reached after
multiple high-background translations.

## 1. Exact Beltrami form of the linearization

Let `U(t)` be any divergence-free field satisfying at each time

    curl U=Lambda U,                                      (1.1)

with fixed `Lambda>0`; its scalar amplitude may depend on time. Let `v` be a
divergence-free perturbation. The vector identity

    grad(U.v)
      =(U.grad)v+(v.grad)U+U cross curl v+v cross curl U   (1.2)

and (1.1) give

    P[(U.grad)v+(v.grad)U]
      =-P[U cross (curl-Lambda)v].                         (1.3)

Set

    D=curl-Lambda.                                        (1.4)

The linearized Navier--Stokes equation is therefore

    v_t=nu Delta v+P[U cross Dv].                          (1.5)

The large background enters only after the Beltrami defect `D` of the
perturbation.

## 2. The `D`-quadratic form is amplitude-blind

Because `D` is self-adjoint on divergence-free fields and commutes with
`Delta`,

    d/dt <v,Dv>
      =2 nu <Delta v,Dv>
       +2 <P(U cross Dv),Dv>
      =2 nu <Delta v,Dv>,                                 (2.1)

since `Dv` is divergence free and `(U cross Dv).Dv=0` pointwise. In particular,
the inviscid part preserves

    Q_D(v)=<v,Dv>                                         (2.2)

for arbitrary amplitude of `U`.

Equivalently, if

    A_U v=P[U cross Dv],                                  (2.3)

then

    A_U^* D+D A_U=0.                                      (2.4)

This is a Krein-skew identity. It is the exact replacement for the useless
positive-norm Gronwall estimate based on `||grad U||_infinity`.

## 3. Slow to near-shell coupling is necessarily asymmetric

In a helicity Fourier basis, `D` has scalar eigenvalue

    d_sigma(k)=sigma |k|-Lambda,    sigma in {+1,-1}.      (3.1)

For a clean slow frequency `|k|=O(b)` with `Lambda~N=Rb`, every helicity has

    |d_s|~N.                                               (3.2)

If one common-sphere background carrier translates it to a first sideband
`k+q` with `|q|=Lambda`, then

    ||k+q|-Lambda|=O(b),                                  (3.3)

so its positive-helicity Beltrami defect satisfies

    |d_h|=O(b).                                            (3.4)

Take one scalar slow/sideband channel and write the inviscid coupling matrix as

    A=[[0,a],[b_*,0]],                                    (3.5)

where `b_*` is slow -> sideband. From (2.4),

    d_s a+d_h conjugate(b_*)=0.                           (3.6)

Thus if the forward entry has the nominal normalized size

    |b_*|=O(rho),                                         (3.7)

then automatically

    |a|=O(rho/R).                                         (3.8)

No separate cancellation estimate is required.

## 4. Exact two-sector spectral scale

Normalize the `D` weights to

    d_s=-R,
    d_h=+/- d,       d>0,                                 (4.1)

and take `b_*=rho`. The Krein relation gives

    a=-d rho/R        for d_h=-d,
    a=+d rho/R        for d_h=+d.                         (4.2)

Hence the characteristic polynomials are exactly

    lambda^2+d rho^2/R       (same Krein sign),           (4.3)
    lambda^2-d rho^2/R       (opposite Krein sign).       (4.4)

The same-sign channel is elliptic. The opposite-sign channel can be
hyperbolic, but its rate is only

    O(rho/sqrt(R)).                                       (4.5)

At the required Raman scaling

    rho^2/R=O(1),                                         (4.6)

there is therefore no `exp(c rho)` first-star instability. Hyperbolic action,
when present, occurs on the same order-one effective scale as the intended
Raman filter.

The balancing map that makes both off-diagonal entries comparable rescales the
near-shell variable by `sqrt(R)`. Thus the Euclidean propagator may carry a
condition-number loss

    O(sqrt(R)),                                           (4.7)

which is the nonnormal sideband excursion seen in finite-star calculations.

## 5. The thin shell still wins this loss

For the explicit compatible sequence from the preceding checkpoint,

    Re=sigma^12,
    R=sigma^4,
    rho=sigma^2,
    delta/b=sigma^-1,                                     (5.1)

the raw shell-residual correction relative to a high parent is `sigma^-3`.
The worst first-star balancing loss is

    sqrt(R)=sigma^2.                                      (5.2)

Their product is

    sigma^-1=delta/b ->0.                                 (5.3)

So first-star nonnormality does not obstruct finite-energy shell localization.

## 6. Recomputed frontier: off-shell multi-step Krein channels

The remaining danger is now specific. Repeated translation by the Beltrami
background reaches frequencies whose distance from the Beltrami sphere is
`O(N)`, not `O(b)`. On those sectors `|D|=O(N)`, and (2.4) alone permits
`O(rho)` couplings in both directions. Opposite Krein signatures could then
produce a genuine `O(rho)` instability.

The next exact discriminator is therefore not another first-star estimate. It
is the complete **fast-coordinate Fourier lattice** of the five-module
Beltrami background. In the `N/b->infinity` limit its background directions are
coordinate-sphere positive-helicity modes, while perturbations are a Bloch
lattice generated from the slow quasi-momentum. One must determine whether the
specific filter-synthesizing amplitude/phase choices admit an off-shell Krein
collision with positive real growth `c rho`, or whether the lattice has a
bounded symmetrizer/normal form after the slow-shell sectors are weighted by
`sqrt(R)`.

A finite Galerkin computation can discriminate candidate phases but is not a
proof. Any surviving stability claim must be analytic/exact; any explicit
finite invariant unstable subblock with exact positive growth would refute the
current Beltrami realization.

No PLAN/canonical proof-graph promotion, recursive turnover, singular solution,
or `NS-R3` claim is made here.
