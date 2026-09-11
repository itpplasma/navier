# Target-safe coexistence of the two purifier channels in Wiener algebra

Date: 2026-09-11. Repository input:
`itpplasma/navier@b527f6d0ef611cefc0a5c509f1fb3ea13cdc1127`.

**Status: author proof in the absolutely summable almost-periodic Fourier
algebra; finite-energy localization of the combined two-channel object is not
yet included in this packet. Independent mathematical audit and novelty are
undetermined.**

This packet closes the first nonlinear coexistence problem for the two minimal
purifier channels at the level that matters for the target strain. The global
cross-family velocity can be much larger than the tiny low velocity of either
rescaled channel, but its first generation is spectrally high. Returning to a
desired low carrier requires one additional interaction. That extra interaction
changes the target **strain** error from order one to `O(lambda)`.

No clean-dyadic-gate composition, recursive turnover, singular solution, or
`NS-R3` claim is made.

## 1. Algebra and the two exact channels

Let `W` denote the absolutely summable almost-periodic Fourier algebra of vector
fields

    u(x)=sum_(xi in S) uhat(xi) exp(i xi.x),
    ||u||_W=sum_xi |uhat(xi)|<infinity.                   (1.1)

The frequency set `S` may be countable. `W` is a Banach algebra, heat is a
contraction, Leray is a bounded coefficientwise multiplier, and

    || exp(nu s Delta) P div F ||_W
      <= C (nu s)^(-1/2)||F||_W.                          (1.2)

Take the two transverse pairs `(kappa_i,d_i)`, `i=1,2`, from
`2026-09-11-two-shear-purifier-reduction.md`, so

    2 d_1 tensor kappa_1+2 d_2 tensor kappa_2=G,
    sym G=H.                                               (1.3)

Their high pump directions are

    r_i=kappa_i cross d_i,
    rho_i=r_i/|r_i|.                                       (1.4)

For the explicit repository decomposition,

    rho_1 and rho_2 are not parallel,                     (1.5)

and

    kappa_1 and kappa_2 are not parallel.                 (1.6)

Both facts are exact algebraic statements over the quadratic field of the
rank-two reduction; the companion checker freezes them.

Use the gradient-preserving rescaling

    lambda=N^(-alpha),       0<alpha<1,                   (1.7)

    d_(i,lambda)=lambda d_i,
    kappa_(i,lambda)=kappa_i/lambda.                       (1.8)

For each `i`, let `U_i` be the complete exact three-layer 2D3C channel with
high shear centers `m N rho_i`, `m=1,2,3`, and the rescaled low pair (1.8).
Each `U_i` is by itself an exact Navier--Stokes solution in its 2D3C class.
On a fixed scaled horizon `0<=t<=T/N^2`,

    ||U_i(t)||_W <= C lambda N.                            (1.9)

Its intended low velocity is `O(lambda)` and its intended low gradient is
`O(1)`.

## 2. Frequency form of one channel

Every scalar-ladder frequency of channel `i` has the form

    s kappa_i/lambda+n N rho_i,                            (2.1)

with `s in {+1,-1}` and `n in Z`; the shear frequencies have the same form
with `s=0` and `n in {+/-1,+/-2,+/-3}`. Reality supplies the negative
frequencies automatically.

Thus every quadratic cross-family output has the form

    xi=s_1 kappa_1/lambda+s_2 kappa_2/lambda
       +N(n_1 rho_1+n_2 rho_2),                           (2.2)

with one nonzero mode drawn from each family.

Because `rho_1,rho_2` are linearly independent, there is a fixed `sigma>0`
such that

    |n_1 rho_1+n_2 rho_2|
      >= sigma sqrt(n_1^2+n_2^2)                          (2.3)

for all integers `n_1,n_2`. Numerically for the exact repository pair, the
smallest singular value of `[rho_1 rho_2]` is about `0.284`.

## 3. First cross-family forcing misses both target carriers

Let the four target frequencies be

    K_*={+/-kappa_1/lambda,+/-kappa_2/lambda}.             (3.1)

Suppose a cross output (2.2) equalled one element of `K_*`.

If `(n_1,n_2)!=(0,0)`, then by (2.3) its high part has magnitude at least
`sigma N`, while every low term has magnitude `O(lambda^-1)=O(N^alpha)`.
Since `alpha<1`, equality is impossible for all sufficiently large `N`.

If `n_1=n_2=0`, both input modes are low scalar modes and (2.2) reduces to

    s_1 kappa_1/lambda+s_2 kappa_2/lambda.                 (3.2)

Because `kappa_1,kappa_2` are nonparallel and `s_1,s_2` are both nonzero, this
cannot equal `+/-kappa_i/lambda`.

Therefore the direct quadratic cross residual has exactly zero coefficient at
all four target frequencies for sufficiently large `N`:

    Pi_* P div(U_1 tensor U_2+U_2 tensor U_1)=0,           (3.3)

where `Pi_*` is coefficient projection onto `K_*`.

This is the decisive spectral moat. The first cross-family error is real, but
it is not a direct target-strain error.

## 4. Global cross-family correction

Put

    U=U_1+U_2.                                             (4.1)

Since each channel is individually exact, the only residual is the cross
stress. Seek an exact solution

    u=U+r,       r(0)=0.                                   (4.2)

The mild equation is

    r=-B(U_1,U_2)-B(U_2,U_1)
      -B(U,r)-B(r,U)-B(r,r),                              (4.3)

where

    B(a,b)(t)=integral_0^t
      exp(nu(t-s)Delta)P div(a tensor b)(s) ds.            (4.4)

By (1.2), (1.9), and `t<=T/N^2`,

    ||B(U_1,U_2)||_W+||B(U_2,U_1)||_W
      <= C lambda^2 N.                                    (4.5)

The linearized map around `U` has norm

    C sqrt(t)||U||_W
      <= C lambda,                                        (4.6)

and the quadratic Lipschitz constant on a ball of radius
`C lambda^2 N` is `O(lambda^2)`. Thus, for all sufficiently large `N`, the
mild map is a contraction on the whole scaled interval and produces a unique
solution satisfying

    sup_(0<=t<=T/N^2)||r(t)||_W
      <= C_T lambda^2 N.                                  (4.7)

If `alpha>1/2`, this global correction itself tends to zero. That stronger
condition is convenient but is not needed for the target estimate below.

## 5. One additional interaction gives the target gain

Project (4.3) onto `K_*`. By (3.3), the direct cross seed disappears:

    Pi_* r
      =-Pi_*[B(U,r)+B(r,U)+B(r,r)].                       (5.1)

On an output frequency in `K_*`, the derivative multiplier has size only

    |xi|=O(lambda^-1),                                     (5.2)

rather than the generic high size `O(N)`. Heat has norm at most one. Therefore

    ||Pi_* r(t)||_W
      <= C (lambda^-1)t
           [ ||U||_W ||r||_W+||r||_W^2 ].                 (5.3)

Using `t<=T/N^2`, (1.9), and (4.7),

    (lambda^-1) N^-2
      (lambda N)(lambda^2 N)=lambda^2,                    (5.4)

while the quadratic term is `O(lambda^3)`. Hence

    sup_t ||Pi_* r(t)||_W <= C_T lambda^2.                (5.5)

Multiplying once more by the target wave number gives the strain error

    sup_t ||grad Pi_* r(t)||_infinity
      <= C_T lambda.                                      (5.6)

Thus the exact two-channel Navier--Stokes solution retains the intended target
strain with an error tending to zero.

## 6. The full purifier tensor survives

The low output of channel `i` is `lambda` times the original low velocity but
has wavevector `kappa_i/lambda`. Therefore its leading local gradient is
unchanged:

    2(lambda d_i) tensor (kappa_i/lambda)
      =2d_i tensor kappa_i.                               (6.1)

The two synchronized channels have the same `1:4:9` pulse clock, so their
leading gradients sum at every matched pulse time to the same scalar pulse
profile times

    G=2d_1 tensor kappa_1+2d_2 tensor kappa_2.             (6.2)

Its symmetric part is exactly the required purifier matrix `H`; the
antisymmetric rotation from the rank-two reduction is retained rather than
discarded.

Combining the individual `O(1/N)` low-gradient ladder errors with (5.6), the
complete target-gradient error is

    O(1/N)+O(lambda).                                      (6.3)

For every `0<alpha<1`, this tends to zero as `N->infinity`.

## 7. What remains for a finite-energy purifier module

This packet proves the **nonlinear two-channel coexistence mechanism** in the
almost-periodic Wiener algebra. The remaining step is no longer cross-family
algebra; it is to combine this theorem with the nested finite-energy
localization from

* `2026-09-11-nested-2d3c-localization.md`, and
* `2026-09-11-wiener-2d3c-shadowing.md`.

The rescaled low frequency `|kappa_i|/lambda=O(N^alpha)` changes the one-channel
localization bookkeeping, but it remains below the pump scale `N`. One must
choose the localization radius `L(N)` so that cutoff leakage into the four
target bands is smaller than the `O(lambda)` strain error and verify the
rescaled self-residual bound. Those are quantitative estimates, not a new
coexistence mechanism.

After that combination, the live blocker becomes the actual clean-gate plus
purifier stage map.

No PLAN, canonical proof graph, manuscript, or formal status is promoted here.
Independent mathematical audit is pending. `NS-R3` remains unresolved.