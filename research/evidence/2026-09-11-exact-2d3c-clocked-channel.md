# Exact nonlinear 2D3C clocked purifier channel

Date: 2026-09-11. Repository input:
`itpplasma/navier@f07dd8d0ededef7ec4e1d1bca7d02325f44801b6`.

**Status: exact invariant-subsystem theorem with a quantitative full-nonlinear
pulse estimate; independent audit and novelty undetermined.** For one prescribed
transverse purifier child, the three-layer clocked pump can be arranged so
that its complete nonlinear Navier--Stokes self-dynamics is not a generic
high-frequency cascade at all. It is an exact 2D3C shear/passive-scalar system:
the in-plane pump evolves by heat, and the perpendicular component solves a
linear advection-diffusion equation.

This upgrades the preceding three-layer pulse from a second-Picard mechanism
to a controlled **full nonlinear channel** in the translation-invariant 2D3C
class. At the advective-strength scaling, the intended low pulse remains order
one while all higher scalar-ladder corrections are `O(1/N)` as the pump
frequency `N` tends to infinity.

The exact carrier identities are frozen by
`research/check_2d3c_clocked_channel.py` (33 symbolic assertions).

The theorem is not yet an `R3` finite-energy construction: exact invariance
uses independence of the third coordinate. Localizing this channel and then
coupling the two purifier channels from the preceding reduction are the live
steps.

## 1. Normal form

By a rigid rotation, every prescribed transverse pair `(kappa,d)` can be put
in the form

    kappa=K e1,       d parallel e3,       K!=0.           (1.1)

It is enough to prove the unit-`d` algebra; its magnitude is absorbed into the
scalar parent coefficient. Put

    a=e3,
    b=e1/K.                                                 (1.2)

For a large frequency `N>0` and layers `m=1,2,3`, choose

    q_m=m N e2,
    p_m=kappa-q_m=(K,-mN,0).                              (1.3)

Then

    a.p_m=a.q_m=0,
    b.q_m=0,
    b.p_m=1.                                               (1.4)

Therefore the exact original Leray pair is

    C(p_m,a;q_m,b)=a                                      (1.5)

for all three layers. Their heat-decay gaps are exactly

    D_m=|p_m|^2+|q_m|^2-|kappa|^2
       =2m^2N^2.                                          (1.6)

Thus the required `1:4:9` pulse clock survives exactly.

The wrong-sign sibling also remains in the same scalar polarization:

    C(p_m,a;-q_m,b)=a.                                    (1.7)

It is not discarded; it belongs to the invariant scalar ladder below.

## 2. The three shear layers have zero mutual nonlinearity

All `q_m` are collinear and all use the same polarization `b`, with

    b.q_m=0.                                               (2.1)

Hence for every `m,n in {1,2,3}`,

    C(q_m,b;q_n,b)=0.                                     (2.2)

The real in-plane velocity therefore has the exact form

    V(t,x)=b sum_(m=1)^3
       [ beta_m exp(-nu m^2N^2 t) exp(i m N x_2)
        +conjugate ],                                      (2.3)

and satisfies

    V_t-nu Delta V+(V.grad)V=0,
    (V.grad)V=0                                           (2.4)

identically. In physical coordinates this is simply an `e1`-directed shear
whose amplitude depends only on `x_2`.

No approximation, averaging, or smallness is used in (2.4).

## 3. The perpendicular component is an exact passive scalar

Let

    u=V+w e3,                                              (3.1)

with `w=w(t,x_1,x_2)` independent of `x_3`. Then `div u=0`, and because all
spatial derivatives in the `e3` direction vanish,

    (w e3.grad)V=0,
    (w e3.grad)(w e3)=0.                                  (3.2)

The remaining cross term is

    (V.grad)(w e3)=(V.grad w)e3.                          (3.3)

It is already divergence free. Consequently the complete original
Navier--Stokes system reduces exactly to

    V_t-nu Delta V=0,                                     (3.4)

    w_t-nu Delta w+V.grad w=0.                            (3.5)

The canonical pressure is constant for this subsystem. The `e3` component
cannot feed back on the shear.

This is a genuine invariant 2D3C class of the original equation, not a
linearization.

## 4. Exact Fourier ladder

Focus on the positive `K` sector of the real scalar field. Its frequencies are

    k_n=(K,nN,0),       n in Z.                            (4.1)

Let `z_n(t)` be the corresponding scalar Fourier coefficients. Since

    b.k_n=1                                                (4.2)

for every integer `n`, each shear harmonic shifts the scalar ladder with the
same exact coupling coefficient. Equation (3.5) is equivalent to

    z_n' + nu(K^2+n^2N^2) z_n
      = -i sum_(m=1)^3
          [ beta_m(t) z_(n-m)
           +conjugate(beta_m(t)) z_(n+m) ],               (4.3)

where

    beta_m(t)=beta_m(0) exp(-nu m^2N^2 t).                (4.4)

The companion checker verifies the underlying Leray identities directly:
all scalar--scalar quadratic interactions vanish, while both `+q_m` and
`-q_m` shift every scalar mode with coefficient exactly one.

The intended low child is `k_0=kappa`. The three initial scalar parents are

    p_m=k_(-m).                                            (4.5)

## 5. Full nonlinear control by a small integrated shear parameter

Let `S(t)` denote the diagonal heat semigroup in (4.3). It is an `l2`
contraction. The time-dependent shift operator on the right-hand side has
operator norm bounded by

    ||A(t)||_(l2->l2)
      <= 2 sum_(m=1)^3 |beta_m(t)|.                        (5.1)

Define

    Lambda(t)=integral_0^t ||A(s)|| ds.                   (5.2)

Then

    Lambda(infinity)
      <= 2 sum_(m=1)^3
          |beta_m(0)|/(nu m^2N^2).                        (5.3)

The Duhamel series for (4.3), using only heat contraction and (5.1), gives the
standard absolute bound

    ||z(t)-z^(0)(t)-z^(1)(t)||_2
      <= ||z(0)||_2 [exp(Lambda)-1-Lambda],               (5.4)

where `z^(0)` is pure heat and `z^(1)` is the first shear interaction. This is
a bound for the **exact full nonlinear NS solution inside the invariant
class**, because (4.3) is the exact equation.

## 6. Strong clocked pulse with vanishing nonlinear remainder

Use the same temporal weights as before,

    w_1=5,       w_2=-32,       w_3=27.                   (6.1)

Choose parent products

    x_m beta_m(0)=c0 w_m,                                 (6.2)

where `x_m=z_(-m)(0)` is the scalar-parent coefficient. Set

    c0=-2 nu N^2.                                         (6.3)

Then the first-interaction coefficient at the low child `n=0` is exactly

    z_0^(1)(t)
      = -i exp(-nu K^2 t)
          [5 exp(-x)-8 exp(-4x)+3 exp(-9x)],               (6.4)

up to the fixed real polarization/phase convention, with

    x=2 nu N^2 t.                                         (6.5)

Thus the full order-one positive pulse from the preceding packet is recovered,
including quadratic onset and cancellation of the slow low heat tail.

Balance the two parent factors in each product, for example so that

    |x_m|=|beta_m(0)|=sqrt(|c0 w_m|).                     (6.6)

For fixed `nu>0`, these coefficients are `O(N)`. Nevertheless (5.3) gives

    Lambda(infinity) <= C_nu/N.                           (6.7)

Also

    ||z(0)||_2=O_nu(N).                                   (6.8)

Therefore (5.4) yields

    ||z-z^(0)-z^(1)||_2 = O_nu(1/N)                       (6.9)

uniformly for all time. In particular, at the low child,

    z_0(t)=z_0^(1)(t)+O_nu(1/N).                          (6.10)

This is the key point: the pump amplitudes may be of order `N`, so the low
pulse is order one on its viscous clock `t comparable to N^(-2)`, yet the
**complete nonlinear correction to that pulse tends to zero**. The special
transverse/shear geometry removes the generic `PN` nonlinear rate from the
relevant ladder; the integrated coupling is only `O(1/N)`.

Thus the isolated clocked purifier channel is not merely a Picard heuristic.
It has an exact full nonlinear asymptotic regime.

## 7. Coordinate-free interpretation

For a general transverse child `(kappa,d)`, put

    r=kappa cross d.                                      (7.1)

Choose the three shear parents parallel to `r`,

    q_m=m N r_hat,                                        (7.2)

and the scalar parents

    p_m=kappa-q_m.                                        (7.3)

Take

    a parallel d,
    b=kappa/|kappa|^2.                                    (7.4)

Then `b.q_m=0`, `b.p_m=1`, and the entire construction above is obtained by a
rigid rotation and harmless scalar normalization. All three shear harmonics
remain collinear, so their exact zero-nonlinearity property is preserved.

Each of the two transverse children obtained in the preceding two-shear
reduction can therefore be equipped with its own exact clocked 2D3C channel.

## 8. Remaining R3 and two-channel blockers

The exact invariant class is constant in the `d` direction and is therefore
not finite-energy on all of `R3`. It is a mechanism theorem, not yet an
admissible Clay datum. Two nontrivial steps remain:

1. **finite-energy localization:** replace the translation-invariant channel by
   a broad Schwartz packet/cylinder and prove that the `O(1/N)` pulse accuracy
   survives the divergence correction, pressure tail, and edge region on the
   required time `O(N^(-2))`;
2. **two-channel coexistence:** superpose the two minimal purifier channels and
   control their mutual cross interactions. Each channel is individually
   linearizable exactly, but their planes/polarizations differ and the union is
   not itself 2D3C.

These are much narrower than the previous ten-family nonlinear pump problem.
The next useful theorem should attack localization first: on the very short
`N^(-2)` clock, a transverse localization radius growing as a positive power
of `N` should make edge and nonlocal-pressure errors quantitatively small. That
scaling must be proved, not assumed.

No finite-energy R3 pulse, regenerative turnover, or singular solution is
claimed here. `NS-R3` remains unresolved.
