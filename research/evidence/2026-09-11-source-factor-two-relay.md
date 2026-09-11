# Full-jet factor-two relay of the four source parent frequencies

Date: 2026-09-11. Repository input:
`itpplasma/navier@5a51ba2745c7afc0ce5af97a4243b63e0dd25687`.

**Status: exact frozen source-reference Taylor theorem through cubic time / quartic amplitude order.** After correcting the Leray interaction helper used by three earlier source checkers, the four-parent synthesis mechanism survives. The same two decompositions that can synthesize a pure decaying common daughter can be dual-tuned to synthesize a pure growing common daughter. Together with the pair-difference shears, the complete source-reference Fourier evolution through order `t^3` generates **all four factor-two parent frequencies with nonzero growing-branch coordinates**. Every ordered convolution contributing through that order is included; the result is not a selected-tree calculation.

The exact computation is frozen by
`research/check_source_factor_two_relay.py`. The checker uses the corrected Leray bilinear form and exact rational enclosures for the radical coefficients.

This is not yet a regenerative turnover. In the same frozen spectral cage the doubled frequencies lie in the stable `|z|=2` sector. A physical relay needs the source similarity scale to evolve so that these frequencies become the next normalized `|z|=1` parent sites before their amplitudes are lost, or else needs continued late nonlinear feeding. Localization, finite-`L` variation, one-data interstage transport, and full source exactification remain open.

## 1. Corrected four-parent cage algebra

Use the caged reference geometry

    c=1/20,
    d_A=9/20,
    d_B=3/20,                                             (1.1)

with four growing parent tilts

    s_1= 1/2,
    s_2=-2/5,
    s_3= 1/5,
    s_4=-1/10.                                            (1.2)

Their wavevectors and growing eigenpolarizations are

    p_j=(s_j,0,1),
    a_+(s)=(1,-sqrt(1+s^2),-s).                           (1.3)

The correct unordered Leray coefficient is

    C(p,a;q,b)
      =P_(p+q)[(a.q)b+(b.p)a].                            (1.4)

A code audit found that three source checkers had accidentally assigned the arguments in the order `p,q,a,b` inside this helper. The proof coefficients in the accompanying evidence notes came from the correct algebra; the checkers are repaired in the same research period. In particular the pair outputs are now explicitly checked to be transverse to their common daughter.

The two designated pair sums coincide:

    k=p_1+p_2=p_3+p_4=(1/10,0,2).                         (1.5)

Write the two pair outputs in the daughter eigenbasis as

    F_A=beta_(A,+) a_+(c)+beta_(A,-) a_-(c),
    F_B=beta_(B,+) a_+(c)+beta_(B,-) a_-(c).              (1.6)

The previously proved strict ratio inequality

    beta_(A,-)/beta_(A,+)
      > beta_(B,-)/beta_(B,+)                             (1.7)

implies two dual interference choices.

The old choice

    w_A=beta_(B,+),
    w_B=-beta_(A,+)                                       (1.8)

cancels the growing coordinate and retains a pure decaying daughter.

The **dual choice**

    w_A=beta_(B,-),
    w_B=-beta_(A,-)                                       (1.9)

instead gives

    w_A F_A+w_B F_B = gamma_* a_+(c),
    gamma_*!=0.                                           (1.10)

Indeed the decaying coordinate cancels identically and the surviving growing coefficient is the negative of the old nonzero decaying determinant. Thus four growing parents can also seed a pure growing common daughter at quadratic order.

## 2. Exact factor-two frequency geometry

Each designated pair also generates its nonzero difference shear. For pair `A`,

    s_A=p_1-p_2=(9/10,0,0),                               (2.1)

and for pair `B`,

    s_B=p_3-p_4=(3/10,0,0).                               (2.2)

The reflected differences `-s_A,-s_B` are present by reality.

The common daughter plus these four shears lands exactly at

    k+s_A = 2 p_1,
    k-s_A = 2 p_2,
    k+s_B = 2 p_3,
    k-s_B = 2 p_4.                                       (2.3)

Thus the cage has an exact factor-two relay in frequency space. Dividing the doubled wavevectors by two reproduces the original four tilts.

For each of the four interactions in (2.3), the stripped Leray coefficient has a nonzero projection onto the growing eigenbranch at the doubled frequency. This already identifies the correct polarization path, but by itself would be vulnerable to omitted-tree cancellation. The next section removes that ambiguity.

## 3. Complete `t^3` source-reference jet

Use the full frozen source-reference Fourier ODE with

    K_0=[[0,1,0],[1,0,0],[0,0,0]],
    mu=3/5,                                                (3.1)

so for each nonzero wavevector `q`

    L_q a
      =[-K_0+q(q^T K_0)/|q|^2-mu|q|^2 I]a.               (3.2)

Initialize all four positive-frequency parents with pair products satisfying (1.9), together with their reality partners. Expand

    u(t)=U_0+tU_1+t^2U_2+t^3U_3+...                       (3.3)

using the exact recurrence from the full quadratic convolution:

    (j+1)U_(j+1)
      =L U_j + sum_(ell=0)^j B(U_ell,U_(j-ell)).           (3.4)

No Fourier output is truncated at the represented orders. The exact numbers of nonzero modes are

    8, 28, 60, 104                                        (3.5)

at orders zero through three. Every coefficient is checked for divergence-freeness and for its reality partner.

Let `Pi_+^(2p_j)` denote the growing source-eigenbranch coordinate at the doubled parent frequency. The checker proves

    Pi_+^(2p_j) U_3 !=0,       j=1,2,3,4.                 (3.6)

The coefficients are imaginary under the chosen Fourier convention; after multiplication by `-i` their real values are enclosed by exact rational intervals obtained from integer square-root bounds. Numerically only for orientation, their approximate values are

    2p_1: -2.25e-4,
    2p_2: +1.68e-8,
    2p_3: -3.49e-3,
    2p_4: +8.86e-5.                                      (3.7)

The smallest interval remains strictly separated from zero. Therefore the attractive central-daughter/shear subtree is **not canceled** by the other quartic trees, the source linear matrix, viscosity, or reality partners at this first relay order.

## 4. Relation to the older doubled-parent birth theorem

The September 10 shear-feedback theorem already found doubled-parent wavevectors at order `t^3` for a symmetric two-parent input. That result was insufficient for a cascade because the output was mainly an `N`-directed polarization, the copied mode was linearly damped in the same stage, and a globally smooth periodic control had the same early birth.

The present result is sharper in two ways:

1. the four-parent dual tuning first creates a **pure growing common daughter** rather than an uncontrolled mixed daughter; and
2. after summing the complete cubic-time jet, each of the four factor-two parent frequencies has an explicitly nonzero **growing source-eigenbranch coordinate**.

It still does not solve the interstage damping problem. The growing coordinate in (3.6) refers to the inviscid/source eigenpolarization at that frequency; the frozen caged viscous rate for every `|z|=2` mode is negative.

## 5. First unresolved relay step

A recursive source-prehistory mechanism would need the factor-two output of one stage to become the four growing `|z|=1` parents of a later normalized stage. There are two possible realizations:

1. **passive interstage carry:** generate the doubled parents, then transport them until the source similarity scale has contracted by the corresponding factor; or
2. **continuous late relay:** keep lower harmonics present so that they feed the doubled sector close to the later time when that sector becomes linearly amplifying.

The first mechanism is threatened by the strong viscous cost accumulated while a doubled copy is over-damped. The second is a genuine nonlinear frequency cascade problem and must be analyzed with the full returned state, not by concatenating Taylor jets.

The next discriminating calculation is the physical interstage exponent: compare the actual source normalized growth/diffusion accumulated by a doubled parent between its birth window and the time it becomes a next-stage parent with the quasi-polynomial local entry amplitude required by the pulse consumer. If passive carry loses by a super-quasi-polynomial factor, only continuous late nonlinear feeding remains.

## 6. Scope

No finite-duration gain, localized turnover, finite-`L` physical relay, common Schwartz trace, full nonlinear de-forcing solution, singularity preservation, or `NS-R3` conclusion is claimed. The theorem is an exact frozen-reference Taylor coefficient and frequency/polarization closure result pending independent audit.
