# Nested anisotropic finite-energy localization of the exact 2D3C channel

Date: 2026-09-11. Repository input:
`itpplasma/navier@303ec66343aa067f6cbdf08c90d4aaf3d7f709ed`.

**Status: scoped author construction and raw-residual theorem; independent
mathematical audit and novelty undetermined.** This packet advances the
finite-energy localization problem for the exact clocked 2D3C purifier channel.
It does not prove a localized Navier--Stokes shadowing theorem, recursive
turnover, finite-time singularity, or `NS-R3`.

The new point is structural. A single common cutoff of the full 2D3C field has
an order-`N^2` nonlinear transition error which does not improve when the
cutoff radius grows. That is avoidable. The shear and passive-scalar pieces can
instead be localized by **nested anisotropic divergence-free curls**. The
scalar is tapered only where the shear is still exactly unmodified; the shear
is tapered only after the scalar has already vanished. In this geometry the
unsuppressed cross mismatch disappears and every raw transition term gains at
least one cutoff derivative:

    ||R_(N,L)||_infinity <= C_(nu,T,K) N^2/L               (0.1)

on the clock `0<=t<=T/N^2`, where

    R_(N,L)=partial_t U_(N,L)-nu Delta U_(N,L)
              +(U_(N,L).grad)U_(N,L).                     (0.2)

The field `U_(N,L)` is smooth, compactly supported and exactly divergence
free. The remaining analytic gate is to control the Helmholtz/Leray projection
and then shadow this approximate path by the actual unforced finite-energy
solution. Those steps are not claimed here.

## 1. Exact channel normal form

Use the rigidly rotated normal form of
`2026-09-11-exact-2d3c-clocked-channel.md`:

    U_N(t,x,y,z)=(v_N(t,y),0,w_N(t,x,y)),                  (1.1)

with

    partial_t v_N-nu partial_y^2 v_N=0,                   (1.2)

    partial_t w_N-nu( partial_x^2+partial_y^2 )w_N
        +v_N partial_x w_N=0.                              (1.3)

The `x` frequency of `w_N` is the fixed nonzero low carrier `K`; the shear
frequencies are `mN`, `m=1,2,3`. The canonical pressure is constant.

Choose potentials `psi_N,q_N` by

    partial_y psi_N=v_N,                                  (1.4)
    partial_x q_N=w_N.                                    (1.5)

The zero mean of the shear fixes `psi_N`; the fixed nonzero `x` frequency fixes
`q_N` without an integration constant. They satisfy the exact equations

    partial_t psi_N-nu partial_y^2 psi_N=0,                (1.6)

    partial_t q_N-nu( partial_x^2+partial_y^2 )q_N
        +v_N partial_x q_N=0.                              (1.7)

## 2. Uniform channel bounds on the viscous clock

For each fixed `T`, the exact channel gives, uniformly for
`0<=t<=T/N^2`,

    ||v_N||_infinity             <= C N,
    ||partial_y v_N||_infinity   <= C N^2,
    ||psi_N||_infinity           <= C,                    (2.1)

and

    ||q_N||_infinity
      +||partial_x q_N||_infinity <= C N,

    ||partial_y q_N||_infinity
      +||partial_x partial_y q_N||_infinity <= C N^2.      (2.2)

Here and below `C=C(nu,T,K)` also depends on the fixed three-layer pulse
weights, but not on `N` or `L`.

For completeness, (2.2) follows directly from the exact scalar ladder. If
`z_n(t)` is the coefficient at `(K,nN,0)`, the shift equation has

    ||A(t)||_(ell1->ell1)
      <= 2 sum_(m=1)^3 |beta_m(t)|.                        (2.3)

The strong clock has `|beta_m(0)|=O(N)` and

    integral_0^(T/N^2) sum_m |beta_m(t)| dt = O(1/N).      (2.4)

Hence both

    sum_n |z_n(t)| <= C N,                                (2.5)

and the first lattice moment

    sum_n (1+|n|)|z_n(t)| <= C N                          (2.6)

follow by the same Gronwall argument, since shifts by `m=1,2,3` change
`1+|n|` by only a fixed factor. Equations (1.5), (2.5), and (2.6) give (2.2).

## 3. Why a common cutoff has a genuine order-`N^2` wall

Let `chi_L` be a scalar cutoff and form, schematically, `chi_L U_N`. Ignore the
divergence correction for this diagnostic. Even if all derivative commutators
are `O(L^-1)`, the convective term contains

    (chi_L U_N.grad)(chi_L U_N)
      =chi_L^2 (U_N.grad)U_N
        +chi_L (U_N.grad chi_L) U_N.                       (3.1)

The time/heat part contains only

    chi_L [partial_t U_N-nu Delta U_N]
      =-chi_L (U_N.grad)U_N.                               (3.2)

Therefore the transition residual contains

    (chi_L^2-chi_L)(U_N.grad)U_N.                          (3.3)

For the strong channel the passive-scalar interaction
`v_N partial_x w_N` is `O(N^2)`. On every nontrivial transition where
`chi_L` stays away from `0,1`, (3.3) is therefore `O(N^2)` independently of
`L`. This is the hidden wall in a one-cutoff localization. Merely moving the
edge farther away does not make the edge dynamics perturbative.

## 4. Nested divergence-free localization

Take smooth one-dimensional inner cutoffs

    d_L(x), e_L(y), f_L(z)                                (4.1)

and outer cutoffs

    a_L(x), b_L(y), c_L(z),                               (4.2)

all compactly supported, with the standard derivative bounds

    |partial^r a_L|+...+|partial^r f_L| <= C_r L^(-r)      (4.3)

for `r=1,2,3`. Require the strict nesting condition

    a_L=b_L=c_L=1                                         (4.4)

on an open neighborhood of

    supp(d_L e_L f_L).                                    (4.5)

Thus every outer derivative also vanishes on the complete inner support and
its transition region.

Define the outer shear streamfunction and inner scalar potential

    Phi_L=a_L(x)b_L(y)c_L(z) psi_N(y,t),                   (4.6)

    Theta_L=d_L(x)e_L(y)f_L(z) q_N(x,y,t).                 (4.7)

Set

    V_L=curl(0,0,Phi_L),                                  (4.8)

    W_L=curl(0,Theta_L,0),                                (4.9)

    U_(N,L)=V_L+W_L.                                      (4.10)

Then `U_(N,L)` is smooth, compactly supported, and exactly divergence free.
Explicitly,

    V_L=(partial_y Phi_L,-partial_x Phi_L,0),              (4.11)

    W_L=(-partial_z Theta_L,0,partial_x Theta_L).          (4.12)

On the complete support of `W_L`, nesting gives

    V_L=(v_N,0,0).                                        (4.13)

Conversely, wherever an outer cutoff varies, `W_L=0`.

This is the load-bearing separation. The passive scalar is never multiplied by
a partially switched shear, and the shear is never switched while the scalar
is present.

## 5. Exact cancellation of the dangerous cross term

On `supp W_L`, (4.13) and the coordinate dependence imply identically

    (W_L.grad)V_L=0.                                      (5.1)

Indeed `V_L=(v_N(y),0,0)` and `W_L` has only `e_1,e_3` components, so it never
differentiates in `y`.

The other cross term is exactly

    (V_L.grad)W_L=v_N partial_x W_L.                       (5.2)

Thus it belongs to the same scalar transport operator already present in the
exact channel; there is no second cutoff multiplier. This is precisely what
fails in (3.1)--(3.3).

## 6. Inner scalar residual

Write

    chi_i=d_L e_L f_L.                                    (6.1)

Because `v_N=v_N(y)` and curl of an `e_2` potential uses only `x,z`
derivatives, the transport-diffusion operator commutes with that curl:

    (partial_t-nu Delta+v_N partial_x)W_L
      =curl(0,E_i,0),                                     (6.2)

where, using (1.7),

    E_i=-nu[2 grad chi_i.grad q_N+q_N Delta chi_i]
          +v_N (partial_x chi_i)q_N.                       (6.3)

There is an important anisotropic gain here. Although
`partial_y q_N=O(N^2)`, the final curl in (6.2) differentiates `E_i` only in
`x` or `z`, never in `y`. From (2.1)--(2.2) and (4.3),

    ||curl(0,E_i,0)||_infinity <= C N^2/L.                 (6.4)

The inner field has the component sizes

    ||W_(L,3)||_infinity <= C N,
    ||W_(L,1)||_infinity <= C N/L.                         (6.5)

Since its advecting directions are only `x,z`, direct differentiation gives

    ||(W_L.grad)W_L||_infinity <= C N^2/L.                 (6.6)

Together with (5.1)--(5.2), the complete residual on the inner region is
therefore `O(N^2/L)`.

## 7. Outer shear residual

Write

    chi_o=a_L b_L c_L.                                    (7.1)

Using (1.6),

    (partial_t-nu Delta)Phi_L
      =-nu[2(partial_y chi_o)v_N+psi_N Delta chi_o]
      =:E_o.                                               (7.2)

Hence

    (partial_t-nu Delta)V_L=curl(0,0,E_o).                 (7.3)

The curl uses only `x,y` derivatives. Equations (2.1), (4.3), and the fact that
the only high derivative is the single `partial_y v_N=O(N^2)` give

    ||curl(0,0,E_o)||_infinity <= C N^2/L.                 (7.4)

The cutoff shear has

    ||V_(L,1)||_infinity <= C N,
    ||V_(L,2)||_infinity <= C/L.                           (7.5)

Therefore

    ||(V_L.grad)V_L||_infinity <= C N^2/L.                 (7.6)

On the outer transition `W_L=0` by nesting, so there are no additional cross
terms.

## 8. Raw-residual theorem

Combining Sections 5--7 proves:

**Theorem.** Fix `nu>0`, the low transverse carrier `K!=0`, the three-layer
clocked channel, and a scaled horizon `T<infinity`. For every sufficiently
large `N` and every `L>=1`, the nested field (4.10) is a real smooth compactly
supported divergence-free field satisfying

    sup_(0<=t<=T/N^2)
      || partial_t U_(N,L)-nu Delta U_(N,L)
          +(U_(N,L).grad)U_(N,L) ||_infinity
      <= C_(nu,T,K) N^2/L.                                (8.1)

The bound is global in space. In contrast, the one-cutoff ansatz has the
order-`N^2` transition term (3.3).

Thus the large nonlinear edge forcing is not intrinsic to finite-energy
localization of the exact 2D3C channel; it is an artifact of tapering both
pieces together.

## 9. What (8.1) does and does not close

On the operating clock `Delta t=O(N^-2)`, the raw forcing budget in (8.1) has
the favorable integrated size

    Delta t ||R_(N,L)||_infinity <= C/L.                   (9.1)

This is exactly the localization scale suggested by the initial pressure-tail
packet, now for the complete nonlinear differential residual of an explicit
compact path rather than only its initial acceleration.

However `R_(N,L)` is not known to be solenoidal. The true forced form relevant
to mild Navier--Stokes stability is

    P R_(N,L),                                             (9.2)

and the Leray projector is not bounded on `L^infinity`. Therefore (8.1) alone
must not be promoted to a shadowing theorem. The next exact analytic target is
one of the following equivalent useful estimates:

    ||P R_(N,L)||_(appropriate scale-invariant/local norm)
       <= C N^2 L^(-gamma),       gamma>0,                 (9.3)

or a direct Oseen-kernel estimate showing that the complete residual produces
`o(1)` error in a fixed inner core during `0<=t<=T/N^2`.

The nested geometry is designed to help that step: every pressure-producing
transition contains a cutoff derivative, while the order-`N^2` cross mismatch
has been removed exactly. A logarithmic Calderon--Zygmund loss would still be
acceptable by taking `L` to grow faster than that loss; an order-one loss in
`L` would be a genuine new obstruction.

No canonical proof graph, PLAN status, manuscript theorem, or formal phase is
promoted by this packet. `NS-R3` remains unresolved.