# A weighted Hessian pressure bound replaces even Lipschitz action by critical form smallness

Date: 2026-09-12. Input: `itpplasma/navier@c7feb2cabf2329fcd5cff69165cb110d7c289903`.

**Author analytic proof; independent audit pending.** This wave changes the
estimate rather than trying to bound a quantity that the preceding actual-NS
packet control shows can be arbitrarily large. A high-angular weighted
Hessian/Laplacian estimate gives a zero-order pressure bound with no
exponential weight-amplitude loss. It permits the even-feedback term to be
absorbed by viscosity under a *critical velocity* smallness hypothesis,
without any estimate on its gradient or its accumulated Lipschitz action.

The proof is whole-space and retains the low sectors through explicit defects.
It supplies a new conditional physical-band consumer, not the missing
one-history producer of the critical smallness and approximate purity.

## Working packet

TERMINAL CLAIM: original unforced incompressible NS on R3, nu>0, solenoidal
Schwartz data, its classical branch and a terminal regularity or singularity
conclusion at exactly that scope.

ESTABLISHED: the approximate-gap pressure note retains all low sectors. The
unforced even-feedback packet theorem invalidates norm-only control of B_Z,
even along one material particle. Large B_Z alone is not singularity evidence.

FIRST GAP: estimate the actual action of Z on an odd wave without paying
||grad Z||_infinity.

PREDICTION BEFORE TEST: the weighted identity relating Hessian and Laplacian
norms loses only ||r grad phi||_infinity/(N-1), not the amplitude of phi.
Duality then estimates pressure from the stress Z tensor w, rather than from
(grad Z)w. Small ||Z||_3 can be absorbed into viscous dissipation.

FALSIFIER: a missing spin-one shift in angular Poincare, an uncontrolled
second derivative of the weight, an unretained low pressure mode, or a
constant depending exponentially on phi in the *high* sector.

CHECK: a full weighted integration identity, rotational Fourier Poincare,
whole-space duality, form estimates, source normalization, and a compact
solenoidal swirl showing the low-sector loss is still genuinely attainable.

## 1. Weighted Hessian/Laplacian estimate with the spin-one shift

Let phi be smooth, bounded, real and axisymmetric, with compactly supported
spatial gradient. Put W=exp(-phi). Suppose a smooth scalar q has only angular
indices |m|>=N, where the integer N>=2. Define

    g_r=||r grad phi||_infinity,
    d_1=g_r/(N-1)<1/2,      C_1=1/(1-2d_1).

The estimate is

    ||W Hess q||_2 <= C_1 ||W Delta q||_2.               (1)

It extends to the associated homogeneous second-derivative class by density.
No bound on Hess phi or on osc(phi) occurs in C_1.

To prove it first note the exact angular inequality

    ||W grad q/r||_2 <= (N-1)^(-1)||W Hess q||_2.        (2)

The first Cartesian derivatives of a scalar angular index m have indices
m,m+1,m-1. Thus every Cartesian component of grad q has angular gap at least
N-1. Apply circle Poincare to these components, integrate with the axisymmetric
weight, and use |partial_theta grad q|<=r|Hess q|. This is why N rather than
N-1 would not be justified for the vector gradient.

For real q the pointwise identity is

    div[Hess q grad q-(Delta q)grad q]
                                  =|Hess q|^2-|Delta q|^2.

Multiply by W^2 and integrate. With X=||W Hess q||_2 and Y=||W Delta q||_2,

    X^2-Y^2
      =2 int W^2 grad phi . [Hess q grad q-(Delta q)grad q]
      <=2g_r ||W grad q/r||_2 (X+Y)
      <=2d_1 X(X+Y).

Cancel X+Y when nonzero. This gives (1-2d_1)X<=Y and proves (1); the zero
case is immediate. For complex q take real parts with the conjugate gradient.
Spatial cutoffs and approximation justify the same formula; no derivative
of phi beyond its first derivative was introduced.

## 2. Zero-order pressure from a stress, including all angular sectors

Let S be a tensor and let p be its canonical pressure,

    -Delta p=partial_i partial_j S_ij.

Use the tensor rotation action, including rotation of both tensor indices,
and write subscripts h,l for total rotational indices |m|>=N and |m|<N.
Rotational projections intertwine double divergence and commute with W.
Then

    ||W p_h||_2 <= C_1 ||W S_h||_2,
    ||W p_l||_2 <= exp(A)||W S_l||_2,
    A=osc(phi).                                        (3)

The high estimate follows by duality. For a high scalar test h of unit L2
norm, set q=(-Delta)^(-1)(W h). Then

    <W p_h,h>=<S_h,Hess q>
              <=||W S_h||_2 ||W^(-1)Hess q||_2.

Apply (1) with weight W^(-1) to q. Its constant is the same and
||W^(-1)Delta q||_2=||h||_2. Supremizing gives the first inequality in (3).
One can start with compact high tests: the inverse Laplacian is smooth and
has sufficient decay, so all integrations are legitimate, then take L2 limits.

For the low estimate the unweighted stress-to-pressure multiplier
-k_i k_j/|k|^2 has norm at most one from Frobenius tensor L2 to scalar L2.
The two weighted/unweighted norm comparisons cost exp(A). These estimates
retain all axial frequencies and introduce no artificial spatial boundary.

## 3. Feedback form estimate without derivatives of Z

Let B,Z,w be smooth solenoidal fields satisfying the complete linearized
velocity equation

    w_t+((B+Z).grad)w+(w.grad)(B+Z)-nu Delta w+grad p=0. (4)

The exact odd equation of an unforced even/odd decomposition is one case of
(4). Write p=p_B+p_Z, where

    -Delta p_B=div[2(w.grad)B],
    -Delta p_Z=div div(Z tensor w+w tensor Z).

Set v=Ww, Y=||v||_2^2, D=||grad v||_2, G=||grad phi||_infinity, and
z_3=||Z||_3. Fix a whole-space Sobolev constant C_S with

    ||v||_6 <= C_S D,    ||v||_3^2 <= C_S sqrt(Y)D.

Solenoidality of w gives div v=-v.grad phi. Integrating the Z stretching
term once, rather than taking a supremum of grad Z, yields

    -int v_i v_j partial_i Z_j
       =int Z.(v.grad)v-int(Z.v)(v.grad phi).

Combining it with the Z transport term gives the bound

    |Z stretching and transport contributions|
                      <= C_S z_3 D^2+2C_S G z_3 sqrt(Y)D. (5)

No assumption on ||grad Z|| is present.

Put S_Z=Z tensor w+w tensor Z, and define

    theta=||v_l||_2/sqrt(Y),
    xi_Z=||W(S_Z)_l||_2/(2z_3||v||_6),                 (6)

using zero if a denominator is zero. Both ratios lie in [0,1]. They describe
actual low velocity and actual low stress, not a presumed invariant sector.
From (3), integration of pressure onto the weight, and rotational orthogonality,

    |int W^2 w.grad p_Z|
      <=2G[||v_h||_2||W(p_Z)_h||_2
                             +||v_l||_2||W(p_Z)_l||_2]
      <=4C_S G z_3(C_1+exp(A)theta xi_Z)sqrt(Y)D.       (7)

In particular a high pressure/stress sector is treated with the constant C_1,
not exp(A). No derivative of Z is hidden in xi_Z.

Combining (5)--(7), put

    b=C_S G z_3[2+4C_1+4exp(A)theta xi_Z].

If

    z_3 <= nu/(4C_S),                                  (8)

then the total Z contribution is at most

    (nu/2)D^2+(b^2/nu)Y.                               (9)

Indeed the first term of (5) costs at most nu D^2/4, and
b sqrt(Y)D<=nu D^2/4+b^2Y/nu. This is viscous form absorption, not an estimate
of the Lipschitz action B_Z. The earlier packet counterexample shows why
that distinction is substantive.

## 4. All-mode energy consumer with the new feedback budget

For the known B part retain the first-order approximate-gap pressure estimate.
Let

    d_0=g_r/N,   c_0=(1+2d_0)/(1-2d_0),
    K_B=||grad B||_infinity,
    eta_B=||W[2(w.grad)B]_l||_2/(2K_B sqrt(Y)),

again with the zero-denominator convention. The base-pressure contribution is
at most [4d_0 c_0 K_B+2K_B exp(A)theta eta_B]Y. Together with (9), the exact
weighted energy identities give

    (1/2)Y'+(nu/2)D^2
       <=[M_phi(B)+4d_0 c_0 K_B
                       +2K_B exp(A)theta eta_B+b^2/nu]Y, (10)

    M_phi(B)=ess sup[-lambda_min S(B)-phi_t-B.grad phi
                                             +nu|grad phi|^2].

Thus the two defects are now

    J_gap,B=2 int K_B exp(A)theta eta_B,

    J_form,Z=(C_S^2/nu) int G^2 z_3^2
                       [2+4C_1+4exp(A)theta xi_Z]^2.   (11)

The derivative-based B_Z does not appear. In particular neither
||S(Z)||_infinity nor ||grad Z||_infinity is required in this consumer.
All modes remain in the equation. N is only an instantaneous estimate cutoff;
choosing different N on different bands does not reset a physical state.

## 5. The source-normalized form action is small under physical critical smallness

Use the same primary-band hypotheses and notation as
`2026-09-12-weighted-pump-action.md`: length sqrt(Q), time Q^(1+h), velocity
Q^(-1/2-h), epsilon=Q^h, L comparable to ell^2, and kappa_s=10^(-5).
Write stars for normalized quantities. Exactly,

    nu_*=nu epsilon,
    ||Z_*||_3=epsilon ||Z_physical||_3.                 (12)

Consequently (8) is the scale-invariant physical condition

    ||Z_physical||_3 <= nu/(4C_S).                      (13)

It is not the much stronger assumption that the physical Lipschitz action
is small. Suppose additionally

    G_*<=C epsilon^(-kappa_s)L^M,
    C_1<=C,
    exp(A)theta xi_Z<=C,
    T_*<=C_T L.

The form budget then obeys

    J_form,Z <= C(nu) epsilon^(1-2kappa_s)L^(2M+1)
                        sup ||Z_physical||_3^2 =o(1).  (14)

Every epsilon power is positive. This is the correct physical normalization;
one must not compare normalized critical size to the unscaled viscosity.

For example, sup theta<=exp(-cL), c>0, makes the purity condition above true
when A=O(L^(3/4)). It also makes J_gap,B=o(1) under the already-stated polynomial
K_B bound for the prescribed primary/base coefficients. Hence (10) recovers

    ||w(T)||_2 <= exp[int M_base+C L^(3/4)+o(1)]||w(0)||_2, (15)

without an exact angular gap and without any assumption B_Z=o(L), provided
(13) and that quantitative approximate purity are actually available.
The constants are independent of the band index and of derivatives of Z,
while depending on nu and the fixed profile/patch constants as before.

This closes the derivative-cost part of the feedback interface. It does not
construct one history satisfying (13) and the purity estimate. Neither the
unforced energy law nor the present calculation provides those hypotheses.

## 6. The low-sector pressure loss is attainable by a genuine NS stress

The first approximate-gap note used a general elliptic force. Here the same
exponential norm loss is realized by a compact, solenoidal, axisymmetric
velocity at its actual NS pressure equation.

Choose a nonzero smooth radial cutoff chi(rho), compactly supported and smooth
as a function of rho^2 at the origin. Let

    f(x)=chi(rho)(-x2,x1,0),      rho=|x|.

This is solenoidal and rotational index zero. With a=chi^2,

    (f.grad)f=-a(rho)(x1,x2,0),
    -Delta p=-2a(rho)-(rho^2-x3^2)a'(rho)/rho.          (16)

The pressure source has only spherical orders zero and two. Its order-zero
monopole vanishes by integration by parts. Put

    m=(4pi/3) int_0^infinity rho^4 a(rho) d rho >0.

Outside the support, the canonical pressure is exactly

    p(x)=-m partial_33 Gamma(x)
        =-m(3cos(theta)^2-1)/(4pi rho^3).               (17)

For instance the order-two source is (2/3)rho a'(rho)P_2(cos(theta)); its
exterior moment is (1/5)(2/3)int rho^5 a' =-(2/3)int rho^4 a, which gives
(17). Thus for an exterior radius R,

    ||p||_(L2(rho>R))^2=m^2/(15pi R^3).                (18)

Take phi_A=A psi, psi radial equal to one on supp f and zero for rho>=R.
Then ||exp(-phi_A)(f tensor f)||_2=exp(-A)||f tensor f||_2, whereas the
weighted pressure norm is bounded below by the positive square root in (18).
The low-sector stress-to-pressure norm is therefore at least c exp(A), even
on stresses of the form f tensor f with f smooth and solenoidal.

Multiplying f by any fixed sufficiently small amplitude makes it valid
small-data initial velocity for an original unforced global solution; the
ratio is unchanged because both stress and pressure scale quadratically.
Taking B=w=f similarly realizes this pressure, up to factor two, in the exact
linearized initial pressure equation. No external force or arbitrary stress
realizability assertion is involved.

This remains a pressure-*norm* control, not a necessary lower bound on the
signed weighted pressure work of the particular source. It forbids deleting
the low-sector term from (3) solely by appealing to incompressibility or the
quadratic NS stress structure. Dynamical/spatial cancellations in a given
history remain possible and must be proved rather than assumed.

## 7. Recomputed first dependency

The new route is not to prove a false generic estimate on B_Z. It is to
produce, for the *same inherited physical history*, sufficiently small even
critical velocity together with sufficiently small weighted low-sector
velocity/stress products. The exact consumer is (10)--(15).

In constructive terms the missing estimate can be stated as

    sup_band ||Z_physical||_3 <= nu/(4C_S),
    J_gap,B+J_form,Z=o(L),

with no independent handoff data, no low-mode deletion and the full nonlinear
coupling retained. The convenient exponential theta condition is sufficient,
not asserted necessary. Whether such a source-specific history exists is open.
A signed coupled even/odd or material estimate may be used to produce these
bounds; another finite ladder, eigenvalue calculation, norm-only Lipschitz
estimate or exact symmetry reset cannot.

The complete correction equation, one Schwartz trace, finite energy,
classical-branch identification and singular observation still have to be
supplied for a negative terminal result. The arbitrary-data positive producer
and nonprincipal full-history adjoint are not resolved by this wave.

## Verification and provenance

`research/check_feedback_form_bound.py` checks the exact Hessian flux identity,
spin-one cutoff arithmetic, Young completion, exterior quadrupole coefficient
and norm, and physical epsilon exponents. The full analytic proof is above;
finite arithmetic does not certify a terminal PDE claim.

The Sobolev inequality and canonical Fourier pressure multiplier are used in
their ordinary whole-space H1/L2 classes. No new external NS regularity theorem
is imported. The prior source-envelope bounds are retained as the same
conditional inputs as in the weighted-pump note; no new source-wide audit is
claimed. Canonical proof-graph and formal statuses are unchanged.
