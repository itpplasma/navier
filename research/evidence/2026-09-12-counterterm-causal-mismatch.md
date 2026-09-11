# The stable-preload repair is off the four-parent backward-eternal unstable manifold

Date: 2026-09-12. Repository input: `itpplasma/navier@1d648a48973f8415cdfabaaa848d076f7f37cd4d`.

**Status: exact scoped source-reference obstruction; author proof with exact checker, independent mathematical audit and novelty assessment pending.** This does not retract the stable-preload repair. It proves that its two free stable counterterms cannot be supplied by the same four-coordinate backward-eternal unstable manifold of the autonomous frozen reference system. Additional inherited state or genuinely nonautonomous/global dynamics is necessary.

## 1. Exact scalar reduction for the easy targets

At either easy doubled target, the quadratic forcing has one nonzero cross-pair channel after the self-pair incompressibility cancellation. Write its nonzero complex forcing amplitude as `F`. If the two parent linear rates sum to `lambda_p` and the target positive-branch rate is the stable number `sigma<0`, define

    D=lambda_p-sigma.                                     (1.1)

For both easy targets the exact caged rates give `D>0`.

At quadratic order the stable coordinate solves

    y'=sigma y + F exp(lambda_p t).                       (1.2)

No approximation is used in the following comparison.

## 2. The backward-eternal causal value

The unique solution of (1.2) which decays toward the remote past is

    y_u(t)= F exp(lambda_p t)/D.                          (2.1)

Hence at a chosen stage left edge `t=0`, the quadratic stable coordinate on the four-parent local unstable manifold is

    y_u(0)=F/D.                                           (2.2)

This is exactly the Lyapunov--Perron denominator already used by the repository's full-lattice unstable-manifold theorem.

## 3. The future-canceling value has the opposite sign

Instead ask for the initial stable coordinate which makes the easy target vanish after a positive stage duration `T`. Solving (1.2) forward gives

    y(T)=exp(sigma T)
      [ y(0) + F (exp(DT)-1)/D ].                         (3.1)

Thus the unique future-canceling value is

    y_c(0)= -F (exp(DT)-1)/D.                             (3.2)

Comparing (3.2) with (2.2),

    y_c(0)/y_u(0)=1-exp(DT)<0,       T>0.                 (3.3)

Equivalently

    y_c(0)-y_u(0)= -F exp(DT)/D !=0.                      (3.4)

The mismatch is independent of the complex phase and magnitude of `F`: both values carry exactly the same forcing factor. The dual pair products are nonzero, every parent amplitude is therefore nonzero, and the two easy Leray coefficients are nonzero, so `F!=0` in both channels.

The same leading value is required if the endpoint target is merely reduced from `O(epsilon^2)` to `O(epsilon^4)`: the `epsilon^2` coefficient must still be canceled, so (3.2) is unchanged at leading order.

## 4. Consequence for the cascade route

The stable-preload theorem remains a valid **free-left-edge** local repair. The present identity proves that the required left-edge values are not the stable coordinates selected by the four-parent backward-eternal causal graph. Since the local unstable manifold contains every sufficiently small reference trajectory tending to zero as `t->-infinity`, no such four-coordinate autonomous history can realize the balanced stage.

A surviving constructive route must therefore use a genuinely new state-supply mechanism:

1. inherit additional modes from earlier physical stages so the local state is not constrained to the four-coordinate unstable manifold;
2. exploit the source's nonautonomous scale change to transport/create the required stable coordinates;
3. use sparse exterior/nonlocal entry; or
4. abandon construction and close a full physical adjoint obstruction.

This is the second serious return to stable-counterterm supply. Under the repository diversification rule, the next active attack must switch away from the autonomous frozen-stage graph.

## 5. Exact check and scope

`research/check_counterterm_causal_mismatch.py` verifies nonzero easy interaction coefficients, strict stability and `D>0` for both easy targets, and the exact algebra (2.2)--(3.4).

No statement is made about a scale-changing physical history with inherited modes, because such a history need not approach zero in the frozen stage coordinates. No physical interstage propagator, common Schwartz trace, nonlinear de-forcing solution, singularity preservation, or `NS-R3` theorem is proved.
