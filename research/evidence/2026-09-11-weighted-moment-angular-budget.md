# Input-only weighted moment and Fourier angular-concentration budget

Date: 2026-09-11. Repository input:
`itpplasma/navier@37376b61cd0a40b66a8ac2925a6d579ae6705257`.

**Status: author theorem on every compact classical interval of the original
whole-space unforced Navier--Stokes branch.** A finite first spatial moment of
the initial datum yields an input-only finite-horizon bound for both
`||x u(t)||_2` and the spacetime weighted dissipation `||x grad u||_2`. In
Fourier variables this supplies a cutoff-independent spacetime budget for
angular derivatives of every smooth dyadic block. A one-dimensional slab
inequality then gives a scale-summed `O(eta)` budget for concentration inside
any fixed relative-width resonance slab.

This is a new positive-route input for the signed comparable-frequency problem.
It does **not** yet control the full triad production, because the resonant slab
orientation depends on the companion frequency and the nonresonant normal form
creates higher-order feedback terms.

No terminal regularity claim is made.

## 1. Whole-space weighted moment identity

Let `u` be the canonical classical solution on `[0,T]`, `T<=H`, of

    u_t-nu Delta u+(u.grad)u+grad p=0,
    div u=0,                                                (1.1)

with Schwartz initial datum `d`. Put

    E_0=||d||_2^2,
    G(t)=||grad u(t)||_2^2,
    M(t)=|| |x|u(t)||_2.                                   (1.2)

The ordinary energy identity gives

    ||u(t)||_2^2+2nu integral_0^t G(s) ds=E_0.             (1.3)

Multiply (1.1) by `|x|^2 u` and integrate. A standard cutoff approximation to
`|x|^2` justifies every integration by parts before the moment is known finite.
The diffusion term satisfies

    integral |x|^2 u.Delta u
      =-integral |x|^2 |grad u|^2+3||u||_2^2.              (1.4)

Using `div u=0`,

    -integral |x|^2 u.(u.grad u)
      = integral (x.u)|u|^2,                               (1.5)

and

    -integral |x|^2 u.grad p
      =2 integral p(x.u).                                  (1.6)

Hence

    (1/2)(M^2)'
      +nu || |x| grad u||_2^2
      =3nu||u||_2^2
       +integral (x.u)|u|^2
       +2 integral p(x.u).                                 (1.7)

The canonical pressure is

    p=R_i R_j(u_i u_j).                                    (1.8)

Riesz boundedness on `L^2`, Holder, Sobolev and interpolation give

    ||p||_2 <= C ||u||_4^2,                                (1.9)

    ||u||_4^2
      <=C ||u||_2^(1/2)||grad u||_2^(3/2)
      <=C E_0^(1/4) G^(3/4).                              (1.10)

Therefore

    (M^2)'
      +2nu || |x|grad u||_2^2
      <=6nu E_0+C M E_0^(1/4)G^(3/4).                     (1.11)

No `L^infinity`, critical norm, future strain, or continuation assumption
enters this estimate.

## 2. Input-only finite-horizon moment bound

Let

    M_H=sup_(0<=t<=min(H,T)) M(t).                          (2.1)

Integrating (1.11), dropping its nonnegative weighted-dissipation term, and
using (1.3) yields

    M_H^2
      <= M(0)^2+6nu E_0 H+C M_H B_H,                      (2.2)

where

    B_H=E_0^(1/4) integral_0^min(H,T) G^(3/4) dt
       <=C E_0 H^(1/4) nu^(-3/4).                         (2.3)

The last step is Holder in time together with
`integral G<=E_0/(2nu)`.

Solving the scalar quadratic inequality gives the explicit schematic bound

    M_H
      <= sqrt(M(0)^2+6nu E_0 H)
         +C E_0 H^(1/4)nu^(-3/4).                         (2.4)

The constant is universal up to the fixed Fourier normalization. In
particular, it is independent of the maximal smooth time `T`, every Fourier
cutoff, and all future critical norms.

Returning to (1.11) now gives

    nu integral_0^min(H,T) || |x|grad u||_2^2 dt
       <= C(d,nu,H).                                       (2.5)

Thus both the first moment and its weighted dissipative derivative have an
input-only finite-horizon budget.

## 3. Fourier derivative budget for smooth blocks

Use the audited smooth dyadic partition from
`2026-09-07-smooth-block-repair.md` and put

    u_k=Delta_k u,
    L_k=||u_k||_2,
    lambda_k=2^k lambda_0.                                 (3.1)

Plancherel identifies multiplication by `x_j` with differentiation in
`xi_j`. On the annular support of block `k`,

    lambda_k ||grad_xi uhat_k||_2
      <= C_phi(
           ||Delta_k^* (x grad u)||_2
           +||Delta_k^* u||_2),                            (3.2)

where `Delta_k^*` is one fixed finite enlargement of the block. The second
term includes the derivative of the smooth cutoff; the first follows from

    partial_(xi_j)(xi_l uhat)
       =delta_(jl) uhat+xi_l partial_(xi_j) uhat.           (3.3)

Finite overlap, (1.3) and (2.5) therefore imply

    integral_0^min(H,T)
      sum_k lambda_k^2 ||grad_xi uhat_k||_2^2 dt
      <= C_phi(d,nu,H).                                    (3.4)

This bound is uniform over Fourier-ball Galerkin cutoffs as well: the tested
moment calculation is performed before the orthogonal cutoff, and finite block
overlap does not depend on the upper resolution.

## 4. Exact slab inequality

Let `f in H^1(R^3)`, let `n` be any unit vector, `c in R`, and `delta>0`.
Slice `xi=y+s n` with `y perpendicular n`. For almost every `y`, the
one-dimensional Sobolev estimate gives

    sup_s |f(y+s n)|^2
      <=2 ||f_y||_(L2_s)||partial_s f_y||_(L2_s).          (4.1)

Integrating over an interval of length `2delta` and then over `y`, followed by
Cauchy--Schwarz, yields

    ||1_(|xi.n-c|<=delta) f||_2^2
      <=4 delta ||f||_2 ||partial_n f||_2
      <=4 delta ||f||_2 ||grad_xi f||_2.                   (4.2)

The constant is independent of the slab orientation and center.

For a comparable-frequency heat-resonance condition with `|p|~lambda_k`,

    |p.q| <= eta lambda_k^2,                               (4.3)

`q` lies in a slab of absolute thickness `C eta lambda_k` perpendicular to
`p`. Applying (4.2) to a block gives, uniformly in the companion frequency
`p`,

    ||1_res uhat_k||_2^2
      <= C_phi eta lambda_k L_k
                     ||grad_xi uhat_k||_2.                 (4.4)

## 5. Scale-summed spacetime resonance budget

For any choice of one such relative-width slab in each block, possibly with
arbitrary orientations and centers fixed for that application, sum (4.4) and
integrate in time. Cauchy--Schwarz in `(k,t)` gives

    integral_0^min(H,T) sum_k ||1_res uhat_k||_2^2 dt
      <= C_phi eta
        [integral_0^min(H,T) sum_k L_k^2 dt]^(1/2)
        [integral_0^min(H,T)
             sum_k lambda_k^2||grad_xi uhat_k||_2^2 dt]^(1/2)

      <= C_phi(d,nu,H) eta.                               (5.1)

Here finite overlap gives `sum_k L_k^2<=C||u||_2^2<=C E_0`.

Thus the solution cannot spend arbitrary spacetime `L^2` mass in a prescribed
family of increasingly thin comparable-frequency resonance slabs: relative
angular width `eta` costs `O(eta)` from input data alone.

This is qualitatively different from a snapshot angular-measure heuristic.
Concentration of Fourier mass in a thin slab would force a large Fourier
derivative, and (3.4) pays for that derivative through the physical weighted
viscous dissipation.

## 6. Exact scope and next discriminator

The heat homological denominator for a triad `p+q=k` is

    nu(|p|^2+|q|^2-|k|^2)=-2nu p.q.                       (6.1)

The existing static-normal-form no-go shows that the exact resonant set
`p.q=0` carries nonzero NS interactions, so it cannot be deleted. Equation
(5.1) supplies a new way to split it instead:

* a near-resonant slab `|p.q|<=eta lambda^2`, paid by the input-only angular
  budget; and
* a nonresonant region with denominator at least
  `2nu eta lambda^2`, where time integration by parts is available.

The first unresolved calculation is now sharp: perform this split on the
**signed smooth-block comparable-frequency production**, retaining the
state-dependent multiplier differences and all vector polarizations. The test
must show whether the `O(eta)` resonant budget and the
`1/(eta lambda^2)` nonresonant normal-form gain can be optimized without
reintroducing `sup_k a_k`, `integral G^2`, or an uncontrolled time derivative
of the multiplier weights `gamma_k`.

A failure at the last item would isolate a new exact blocker: the functional's
state-dependent weights, not Fourier angular concentration itself.

NON-CLAIMS: (5.1) is not an RF-q producer, does not bound the complete triad
integral, and does not imply NS-R3. Independent mathematical audit and novelty
assessment are pending.
