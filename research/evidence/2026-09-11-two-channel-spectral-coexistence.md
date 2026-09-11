# Target-safe coexistence of the two purifier channels in Wiener algebra

Date: 2026-09-11. Original repository input:
`itpplasma/navier@b527f6d0ef611cefc0a5c509f1fb3ea13cdc1127`.
Corrected after the exact geometry checker at
`itpplasma/navier@ac13d4ad817e4909ed69e15189a19d02f681410c`.

**Status: author proof in the absolutely summable almost-periodic Fourier
algebra; finite-energy localization of the combined two-channel object is not
yet included in this packet. Independent mathematical audit and novelty are
undetermined.**

This packet closes the first nonlinear coexistence problem for the two minimal
purifier channels at the level that matters for the target strain. The global
cross-family velocity can be larger than the small low velocity of either
rescaled channel, but its first generation is spectrally high. Returning to a
desired low carrier requires one additional interaction. That extra interaction
makes the target strain error `O(lambda)`.

**Correction note.** The two channels have the same fast `1:4:9` pump clock,
but after `kappa_i -> kappa_i/lambda` their slow low-frequency heat factors are
`exp(-nu |kappa_i|^2 t/lambda^2)` and need not agree. On the operating interval
`t=O(N^-2)` they differ from one by `O(N^(2 alpha-2))` when
`lambda=N^-alpha`, `alpha<1`. The original version of Section 6 called their
leading scalar pulse profiles identical; the correct statement is asymptotic,
with this additional explicit error.

No clean-dyadic-gate composition, recursive turnover, singular solution, or
`NS-R3` claim is made.

## 1. Algebra and the two exact channels

Let `W` be the absolutely summable almost-periodic Fourier algebra

    u(x)=sum_(xi in S) uhat(xi) exp(i xi.x),
    ||u||_W=sum_xi |uhat(xi)|<infinity.                   (1.1)

It is a Banach algebra. Heat is contractive, Leray is a bounded coefficientwise
multiplier, and

    || exp(nu s Delta) P div F ||_W
      <= C (nu s)^(-1/2)||F||_W.                          (1.2)

Take the two transverse pairs `(kappa_i,d_i)`, `i=1,2`, from
`2026-09-11-two-shear-purifier-reduction.md`, so

    2 d_1 tensor kappa_1+2 d_2 tensor kappa_2=G,
    sym G=H.                                               (1.3)

Put

    r_i=kappa_i cross d_i,
    rho_i=r_i/|r_i|.                                       (1.4)

The exact checker `research/check_two_channel_spectral_coexistence.py` proves
over the quadratic field of the rank-two reduction that

    rho_1 and rho_2 are not parallel,
    kappa_1 and kappa_2 are not parallel.                 (1.5)

Its positive-root numerical calibration gives

    rho_1.rho_2 approximately -0.919189522121,
    sigma_min([rho_1 rho_2]) approximately 0.284271838.    (1.6)

Use the gradient-preserving rescaling

    lambda=N^(-alpha),       0<alpha<1,                   (1.7)

    d_(i,lambda)=lambda d_i,
    kappa_(i,lambda)=kappa_i/lambda.                       (1.8)

For each `i`, let `U_i` be the complete exact three-layer 2D3C channel with
high shear centers `m N rho_i`, `m=1,2,3`, and low pair (1.8). Each `U_i` is
individually an exact Navier--Stokes solution in its translation-invariant
2D3C class. On every fixed scaled horizon `0<=t<=T/N^2`,

    ||U_i(t)||_W <= C lambda N.                            (1.9)

Its low velocity is `O(lambda)` and its low gradient is `O(1)`.

## 2. Frequency form and spectral moat

Every scalar-ladder frequency of channel `i` has the form

    s kappa_i/lambda+n N rho_i,                            (2.1)

with `s in {+1,-1}`, `n in Z`; the shear frequencies have `s=0` and
`n in {+/-1,+/-2,+/-3}`.

A quadratic cross-family output therefore has the form

    xi=s_1 kappa_1/lambda+s_2 kappa_2/lambda
       +N(n_1 rho_1+n_2 rho_2).                           (2.2)

Because the two `rho_i` are linearly independent, there is a fixed `sigma>0`
such that

    |n_1 rho_1+n_2 rho_2|
      >= sigma sqrt(n_1^2+n_2^2)                          (2.3)

for all integers `n_1,n_2`.

Let

    K_*={+/-kappa_1/lambda,+/-kappa_2/lambda}.             (2.4)

If `(n_1,n_2)!=(0,0)`, the high part of (2.2) is at least `sigma N` while the
low part is only `O(lambda^-1)=O(N^alpha)`. Since `alpha<1`, (2.2) cannot
belong to `K_*` for all sufficiently large `N`. If `n_1=n_2=0`, nonparallelism
of `kappa_1,kappa_2` excludes a low--low sum from equaling one target.
Therefore

    Pi_* P div(U_1 tensor U_2+U_2 tensor U_1)=0           (2.5)

exactly for sufficiently large `N`, where `Pi_*` is coefficient projection
onto `K_*`.

## 3. Global cross-family correction

Set

    U=U_1+U_2.                                             (3.1)

Since each channel is exact, the residual of `U` consists only of cross stress.
Seek an exact solution

    u=U+r,       r(0)=0.                                   (3.2)

Writing

    B(a,b)(t)=integral_0^t
      exp(nu(t-s)Delta)P div(a tensor b)(s) ds,            (3.3)

we have

    r=-B(U_1,U_2)-B(U_2,U_1)
      -B(U,r)-B(r,U)-B(r,r).                              (3.4)

By (1.2), (1.9), and `t<=T/N^2`,

    ||B(U_1,U_2)||_W+||B(U_2,U_1)||_W
      <= C lambda^2 N.                                    (3.5)

The linearized mild-map norm is

    C sqrt(t)||U||_W <= C lambda,                         (3.6)

and the quadratic Lipschitz constant on a ball of radius
`C lambda^2 N` is `O(lambda^2)`. Hence for sufficiently large `N` the full
scaled interval is contractive and

    sup_(0<=t<=T/N^2)||r(t)||_W
      <= C_T lambda^2 N.                                  (3.7)

For `alpha>1/2` this global correction itself tends to zero.

## 4. Target projection gains one interaction

By the exact moat (2.5), the direct cross seed disappears after `Pi_*`:

    Pi_* r=-Pi_*[B(U,r)+B(r,U)+B(r,r)].                   (4.1)

On an output frequency in `K_*`, the derivative multiplier is only

    |xi|=O(lambda^-1),                                     (4.2)

rather than `O(N)`. Heat is contractive, so

    ||Pi_* r(t)||_W
      <= C lambda^-1 t
        [||U||_W||r||_W+||r||_W^2].                       (4.3)

Using (1.9), (3.7), and `t<=T/N^2`,

    lambda^-1 N^-2
       (lambda N)(lambda^2 N)=lambda^2,                   (4.4)

and the quadratic term is smaller. Therefore

    sup_t ||Pi_* r(t)||_W <= C_T lambda^2,                (4.5)

and multiplying by the target wave number gives

    sup_t ||grad Pi_* r(t)||_infinity
      <= C_T lambda.                                      (4.6)

Thus cross-family dynamics perturb the desired target strain by `O(lambda)`.

## 5. Individual channel accuracy after rescaling

The rescaling preserves the rank-one gradient exactly:

    2(lambda d_i) tensor (kappa_i/lambda)
      =2 d_i tensor kappa_i.                              (5.1)

The scalar-ladder coupling and the fast decay gaps remain unchanged:

    D_m=2m^2N^2.                                           (5.2)

The exact one-channel full-nonlinear ladder remainder has scalar coefficient
`O(1/N)`. Its physical low velocity error is `O(lambda/N)`; multiplying by
`|kappa_i|/lambda` gives the low-gradient error

    O(1/N).                                                (5.3)

The additional low heat factor is

    h_i(t)=exp[-nu |kappa_i|^2 t/lambda^2].               (5.4)

On `0<=t<=T/N^2`,

    |1-h_i(t)|
      <= C_T /(lambda^2 N^2)
      =C_T N^(2 alpha-2).                                 (5.5)

Therefore the two leading low gradients share the same fast `1:4:9` pulse
profile only up to the explicit slow-heat mismatch (5.5).

## 6. Correct combined purifier estimate

Let `g_fast(t)` denote the common three-layer fast pulse profile, normalized as
in the exact 2D3C channel. The two leading low gradients are

    g_fast(t) h_1(t) [2d_1 tensor kappa_1],
    g_fast(t) h_2(t) [2d_2 tensor kappa_2].                (6.1)

Since

    G=2d_1 tensor kappa_1+2d_2 tensor kappa_2,
    sym G=H,                                               (6.2)

we obtain uniformly on the scaled interval

    grad Pi_* u(t)
      =g_fast(t) G
        +O_T(lambda)
        +O_T(1/N)
        +O_T(N^(2 alpha-2)).                               (6.3)

The symmetric part therefore obeys

    sym grad Pi_* u(t)
      =g_fast(t) H
        +O_T(lambda+N^-1+N^(2 alpha-2)).                  (6.4)

Every term tends to zero for `0<alpha<1`; if one also wants the global
cross-family correction (3.7) to vanish, choose

    1/2<alpha<1.                                           (6.5)

For example `alpha=3/4` gives target-strain errors

    O(N^-3/4)+O(N^-1)+O(N^-1/2)=O(N^-1/2).                (6.6)

The antisymmetric rotation in `G` is retained throughout; only the symmetric
part is used for the purifier energy discrimination.

## 7. Remaining finite-energy step

This packet proves nonlinear two-channel coexistence in the almost-periodic
Wiener algebra. To obtain a finite-energy purifier module, combine it with the
nested localization and Wiener shadowing packets. With rescaled low frequency
`O(N^alpha)`, the localization estimates must be tracked uniformly in `N`, and
the direct cross-family target moat becomes a rapidly decaying Fourier-tail
estimate rather than exact zero after spatial cutoff.

A sufficient target is a compact Schwartz approximate path whose projected
self residual is `O(lambda N^2/L)` in `F L1`, whose global cross correction is
`O(lambda^2 N)`, and whose target-strain error is

    O(lambda)+O(N^-1)+O(N^(2 alpha-2))+O(L^-1)
      + superalgebraic cutoff leakage.                    (7.1)

Taking, for example, `alpha=3/4` and `L=N` would make every displayed error
tend to zero. Establishing (7.1) for the rotated nested cutoffs is the next
finite-energy calculation.

No PLAN, canonical proof graph, manuscript, or formal status is promoted here.
Independent mathematical audit is pending. `NS-R3` remains unresolved.