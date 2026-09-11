# Four growing source parents synthesize one pure decaying branch

Date: 2026-09-11. Repository input:
`itpplasma/navier@f0ec96db765a10f5522aa7e8367936def47cfc90`.

**Status: exact reference-principal theorem through first quadratic order.** The finite all-growing same-`b` cancellation attempt is obstructed by its unique extreme difference output. A genuinely different mechanism survives: use two different decompositions of the same daughter, still with four **growing** source eigenbranches, and choose the two pair products so that the daughter's growing eigencomponent cancels while its decaying eigencomponent remains.

For one explicit rational geometry and one explicit viscous strength, all four parents are linearly growing, the selected target is a pure decaying source eigenvector at quadratic order, and every other first quadratic output is linearly damped. Thus the source's decaying-branch escape is not intrinsically inaccessible from growing modes.

This is not yet a turnover: cubic feedback, finite-`L` corrections, physical localization, common initial trace and the full source mean/pressure remain open.

## 1. Reference system

Use the source reference eigenpolarizations with `lambda_0=1` and `c_0=-1`:

    a_+(s)=(1,-sqrt(1+s^2),-s),
    a_-(s)=(1,+sqrt(1+s^2),-s).                           (1.1)

For a Fourier mode

    p=b(s,0,1),                                            (1.2)

these are transverse. Include scalar viscous damping with

    mu=6/25.                                               (1.3)

The reference positive-branch rate is

    gamma_+(b,s)=1/sqrt(1+s^2)-mu b^2(1+s^2),             (1.4)

and the negative branch has the first term negated.

Take four parents, all with `b=1`, at tilts

    s_1=11/10,  s_2=-9/10,
    s_3= 7/20,  s_4=-3/20.                                (1.5)

The first pair has center `1/10` and half-separation `1`; the second has the same center and half-separation `1/4`. Both sums therefore land at

    k=p_1+p_2=p_3+p_4=(1/5,0,2),                          (1.6)

whose tilt is `c=1/10`.

## 2. Two decompositions have different chiral ratios

For any equal-`b` pair centered at `c` with half-separation `d>0`, write its sum-frequency Leray output in the daughter eigenbasis as

    C_sum = beta_+(d) a_+(c)+beta_-(d) a_-(c).            (2.1)

Let

    q(s)=sqrt(1+s^2),
    q_c=q(c),
    qbar_d=[q(c+d)+q(c-d)]/2.                              (2.2)

Direct substitution into the exact sum coefficient from the September 10 regeneration packet gives

    beta_-(d)/beta_+(d)
      =[qbar_d-q_c]/[qbar_d+q_c].                         (2.3)

For the present positive center and separations, `beta_+(d)>0`. Since `q` is strictly convex,

    d -> qbar_d

is strictly increasing for `d>0`: its derivative is
`[q'(c+d)-q'(c-d)]/2>0`. Therefore the ratio (2.3) is strictly larger for `d=1` than for `d=1/4`.

Let `(beta_{A,+},beta_{A,-})` denote the `d=1` pair and `(beta_{B,+},beta_{B,-})` the `d=1/4` pair. Weight their complex pair products by

    w_A=beta_{B,+},
    w_B=-beta_{A,+}.                                      (2.4)

Then the total growing coordinate is exactly zero, while the decaying coordinate is

    beta_{B,+} beta_{A,-}-beta_{A,+} beta_{B,-}
      =beta_{A,+} beta_{B,+}(R_A-R_B) >0,                 (2.5)

where `R=beta_-/beta_+`.

For reproducibility, the checker simplifies (2.5) to

    5[-2 sqrt(41309)-sqrt(22321)+sqrt(18281)+2 sqrt(45349)]/20402
      >0.                                                  (2.6)

Hence the combined target coefficient is a nonzero scalar multiple of

    a_-(1/10)=(1,sqrt(101)/10,-1/10),                     (2.7)

with **no** `a_+` component.

The signs in (2.4) are physically realizable by ordinary complex/real Fourier phases: only the pair products are prescribed.

## 3. All four parents grow

Among the four tilts in (1.5), the largest absolute value is `11/10`; (1.4) decreases with `q=sqrt(1+s^2)`. Therefore it suffices to check

    gamma_+(1,11/10)
      =10/sqrt(221)-663/1250 >0.                           (3.1)

The inequality is exact; squaring positive sides reduces it to an integer inequality. Hence every parent grows in the same reference background.

The target positive branch at `b=2,c=1/10` is also available:

    gamma_+(2,1/10)
      =10/sqrt(101)-606/625 >0.                            (3.2)

The quadratic synthesis nevertheless selects only the negative branch (2.7).

## 4. Every other first quadratic output is damped

A self-interaction of one transverse plane wave vanishes identically.

Every difference frequency of two parents in (1.5) has axial component zero because all parents have the same `b=1`. Thus its source reference undamped eigenvalues collapse to zero and viscosity makes every nonzero difference mode strictly damped.

The four non-designated sums all have axial component `2` and tilts

    29/40, 19/40, -11/40, -21/40.                         (4.1)

The largest positive-branch rate among them occurs at the smallest absolute tilt `11/40`. There

    gamma_+(2,11/40)
      =40/sqrt(1721)-5163/5000 <0.                        (4.2)

Again this is an exact radical inequality; after squaring positive sides it is an integer comparison. Consequently every other sum is damped in **both** eigenbranches.

Thus, through first quadratic order, the only undamped/growing-frequency output window is the designated target, and the chosen pair weights put that target entirely in its decaying eigenbranch.

## 5. Consequence and next discriminator

The previous statement that a decaying source branch necessarily has to be preloaded from the remote past is too strong. At the reference-symbol level it can be **generated instantaneously by four growing branches with all other first quadratic clutter linearly damped**.

This is a genuine mechanism change from finite same-`b` sideband cancellation. It uses interference at a common daughter, not cancellation of each parent-pair difference output.

The immediate next test must include the next nonlinear jet and time evolution. The decaying target is continually forced by the growing parents; interactions of that target and of the damped first sidebands with the parents may regenerate growing frequencies at cubic order. If such an unavoidable growing cubic output exists with the same source scale, this module is not a closed prehistory cell. If the cubic complement remains damped or triangular, the result supplies a serious candidate for dynamically producing the mixed-branch ingredient required by the September 10 sideband-cancellation escape.

Companion checker: `research/check_source_decaying_synthesis.py`.

NON-CLAIMS: no finite-`L` source theorem, no nonlinear invariant subsystem, no physical packet localization, no common Schwartz trace, no completed turnover and no `NS-R3` conclusion. Independent audit and novelty assessment remain pending.
