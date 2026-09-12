# The six-mode half-grade bridge persists on a full finite-time reference lattice

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@d4e0194fa5bebceb1d5a922cc6809b360e752d91`.

**Status: author theorem for the complete frozen source-reference infinite lattice on every fixed finite horizon in the small-data regime, with exact quadratic/Duhamel control. Independent mathematical audit and novelty assessment pending.** This upgrades the rank-four instantaneous six-mode bridge to the full nonlinear reference evolution with every generated sideband retained. It does not supply the six input ancestors from a common physical history and it is not a finite-`L` whole-space theorem.

## 1. Prediction before the test

The algebraic packet proves that six growing half-grade ancestors

    14, -13, 5, -4, 2, -1

have four independent quadratic edges into the next `z=1` source-parent keys

    5, -4, 2, -1.

A local symbol could nevertheless disappear after finite-time propagation if another quadratic decomposition canceled it or if a parent/target growth mismatch produced a zero Duhamel factor.

Prediction: neither happens. Each target has exactly one nonzero positive-half-grade pair; its only other positive decomposition is a self pair, which vanishes identically by incompressibility. The four causal growth mismatches are positive. Hence the quadratic finite-time target map is the same rank-four monomial map multiplied by four nonzero scalar Duhamel factors. Analytic dependence of the full parabolic flow then permits exact nonlinear retuning by the real implicit-function theorem.

## 2. Full reference lattice and analytic evolution

Let `Lambda` be the rank-two source-reference lattice from the spectral-cage theorem and let

    Lambda_(1/2)=(1/2) Lambda.

This is again a closed rank-two lattice. Work with real, zero-mean, divergence-free three-component fields on its dual two-torus. The frozen reference equation is

    partial_t u = L u + N(u),
    L=A(D)+(3/5) Delta,
    N(u)=-P[(u.grad)u],

with the same bounded source connection multiplier `A(D)` used by the full-lattice unstable-manifold theorem.

For `r>2`, the heat part is sectorial, `A(D)` is bounded, and the usual product estimate maps `H^r x H^r` to `H^(r-1)`. Heat smoothing therefore gives, for every fixed `T>0`, a neighborhood of zero in `H^r` on which the complete mild solution exists on `[0,T]` and depends real-analytically on the initial Fourier amplitudes. No Fourier truncation is imposed.

## 3. The six-mode initial family

At `t=0`, put only the six positive half-grade growing eigenmodes

    h_x=(x/20,0,1/2),
    x in {14,-13,5,-4,2,-1},

and their reality partners into the initial field. Write their complex positive-frequency amplitudes as

    epsilon x_14, epsilon x_-13, epsilon x_5,
    epsilon x_-4, epsilon x_2, epsilon x_-1.

Set all other lattice coefficients to zero initially. The full evolution immediately generates infinitely many sidebands; all remain part of the solution.

Let `Y_K(epsilon,x,T)` be the growing source-eigenbranch coordinate at the positive next-parent vector

    p_K=(K/10,0,1),
    K in {5,-4,2,-1}.

Because these four target modes are absent initially,

    Y_K=epsilon^2 Q_K(x,T)+O(epsilon^3)

uniformly for `x` in a fixed compact neighborhood and fixed `T`.

## 4. Exact quadratic finite-time coefficients

For each target the complete positive-half-grade decomposition list consists of one cross pair and one self pair:

    K= 5:  (14,-4) and (5,5),
    K=-4:  (-13,5) and (-4,-4),
    K= 2:  (5,-1) and (2,2),
    K=-1:  (-4,2) and (-1,-1).

For every transverse vector `a` at wavevector `k`,

    C(k,a;k,a)=0

because `a.k=0`. Thus all self-pair competitors vanish identically, even after their linear polarization evolves within the same transverse plane.

The selected ancestors start in positive eigenbranches, so at quadratic order their amplitudes evolve as scalar exponentials. Let `lambda_a,lambda_b` be the two half-grade positive rates and `lambda_K` the next-parent positive rate. The target growing coordinate is

    Q_K(x,T)
      =(-i) c_K x_a x_b e^(lambda_K T)
         [exp(D_K T)-1]/D_K,

where `c_K` is the nonzero exact Leray coefficient from the six-mode bridge and

    D_K=lambda_a+lambda_b-lambda_K.

The exact checker proves all four mismatches are strictly positive. In radical form,

    D_5 = 33/250
      +(-4292 sqrt(5)+725 sqrt(74)+1850 sqrt(29))/10730 >0,

    D_-4 = 21/200
      +(-6725 sqrt(29)+1450 sqrt(269)+15602 sqrt(5))/39005 >0,

    D_2 = 57/200
      +(-2525 sqrt(26)+5252 sqrt(5)+1300 sqrt(101))/13130 >0,

    D_-1 = 69/250
      +(-7540 sqrt(101)+13130 sqrt(29)+14645 sqrt(26))/76154 >0.

Therefore

    [exp(D_K T)-1]/D_K >0

for every fixed `T>0`. No finite positive horizon creates a quadratic cancellation.

## 5. Rank four survives finite time

Absorb the nonzero `T`-dependent scalar factors into coefficients `d_K(T)`. Then

    Q_5   =d_5(T)   x_14  x_-4,
    Q_-4  =d_-4(T)  x_-13 x_5,
    Q_2   =d_2(T)   x_5   x_-1,
    Q_-1  =d_-1(T)  x_-4  x_2.

Fix nonzero shared amplitudes `x_5,x_-4`. The complex Jacobian in the four controls

    (x_14,x_-13,x_-1,x_2)

has determinant

    d_5 d_-4 d_2 d_-1 x_-4^2 x_5^2 !=0.

Viewed over real and imaginary parts, multiplication by a nonzero complex number is an invertible real two-by-two map. Hence the corresponding eight-by-eight real Jacobian is invertible.

## 6. Exact nonlinear retuning

Choose any nonzero base six-mode vector `x^0`. Define the normalized endpoint map

    G(epsilon,x)=epsilon^(-2)
       (Y_5,Y_-4,Y_2,Y_-1).

Analyticity of the full mild flow and the absence of linear target terms make `G` extend real-analytically to `epsilon=0`, with

    G(0,x)=Q(x,T).

At `x^0` the derivative in the four control amplitudes above is invertible. The ordinary real implicit-function theorem therefore gives, for every sufficiently small `epsilon`, small retunings of those four complex ancestor amplitudes which hold any prescribed nearby normalized target quartet fixed **exactly** under the complete nonlinear infinite-lattice evolution.

Equivalently, any chosen nonzero leading target quartet in the local range can be realized as

    (Y_5,Y_-4,Y_2,Y_-1)=epsilon^2 y_*

with every stable and unstable sideband generated by the equation retained. This is not a finite Fourier-jet closure.

## 7. Recomputed frontier

The local late-regeneration module is now closed at frozen-reference finite-horizon scope: conditional on six small half-grade ancestors being available near a future source window, a full nonlinear lattice history can be retuned to produce a four-component next-parent trace with no hard/easy leading-order loss.

This is the second serious checkpoint on the same local six-mode bridge (instantaneous rank and then finite-time full-lattice persistence). Per the diversification rule, the next attack must move backward to **causal late supply of the six ancestors from one history**, not add another local Fourier refinement. Passive reuse of the old four is already super-amplifying. The open constructive options are therefore depletion/cancellation followed by late regeneration, or a genuinely different source-background parametric mechanism. The nonprincipal localized full-history adjoint remains the alternative route.

No finite-`L` physical lift, common Schwartz trace, nonlinear de-forcing solution, singularity preservation, or `NS-R3` conclusion is claimed.

Companion checker: `research/check_half_grade_finite_time_bridge.py`.
