# BDNK transfer screen: a nonlinear core obstruction and the causal shear barrier

2026-10-07. Base: `itpplasma/navier@9b1a66486e3d6d5e49fadcb40b95eea49315b0b7`.
Status: **AUTHOR PROOF; independent mathematical reconstruction pending**.
This packet changes no accepted NS-R3 claim and claims neither BDNK global
regularity nor an exact BDNK singular solution. No novelty priority is claimed.

## 1. Question, source scope, and a fixed physical model

BEFORE: the proposed direct relativistic lift of the NS shrinking core had
not been tested against the full stress tensor or the pulse-damping mechanism.
AFTER: the slow-shrinking, weighted-C2, noncooling proper-velocity lift is
excluded by the energy equation; a uniform heat-damping transfer is refuted
by the exact shear spectrum. Other BDNK singularity mechanisms remain open.

Use signature (-,+,+,+), c=1, one neutral conformal BDNK fluid on Minkowski
spacetime. Write u=(gamma,w), gamma=sqrt(1+|w|^2), physical velocity v=w/gamma,
Delta^{mu nu}=g^{mu nu}+u^mu u^nu, D=u^alpha partial_alpha, theta=partial_alpha u^alpha.
Set epsilon=Theta^4, P=epsilon/3 (the constant in the temperature law is absorbed
in units), eta=eta0 Theta^3, chi=chi0 Theta^3, lambda=lambda0 Theta^3. Fix

    eta0>0, chi0=a1 eta0, a1>=4,
    lambda0>=3 eta0 a1/(a1-1).

The concrete strictly causal frame A is chi0=25 eta0/2, lambda0=25 eta0/3.
The complete constitutive law, with no Euler substitution in its time derivatives, is

    A = chi (3 D log Theta + theta),
    Q^mu = lambda (D u^mu + Delta^{mu alpha} partial_alpha log Theta),
    sigma^{mu nu} = (partial^mu u^nu + partial^nu u^mu
                    + u^mu D u^nu + u^nu D u^mu)/2 - theta Delta^{mu nu}/3,
    T^{mu nu} = (epsilon+A)(u^mu u^nu+Delta^{mu nu}/3)
               +u^mu Q^nu+Q^mu u^nu-2 eta sigma^{mu nu},
    partial_mu T^{mu nu}=S^nu.

S is zero or extends smoothly through the proposed singular point. A bounded
source is enough for the exclusion below; a residual divergent there is not
an admissible smooth forcing.

Primary sources actually read:
- Pandya--Pretorius, arXiv:2104.00804v2, printed p.6, equations (13)--(16),
  including the page image: https://arxiv.org/pdf/2104.00804v2 . This supplies
  precisely the tensor, powers of epsilon, causal inequalities, and frame A.
- OpenAI, *Finite time blowup for Navier--Stokes*, Theorem 1.1 and sections
  2--3, with printed pp.4 and 7 inspected as images:
  https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf .
  The read source gives radial scale tau^(1/2), axial scale tau^(1/2-h),
  tangential speed tau^(-1/2-h), 0<h<1/100, and smooth forcing.
- Clarisse et al., arXiv:2510.16603v1, equations (3)--(6), (10)--(19):
  https://arxiv.org/html/2510.16603v1 . Used to cross-check the full energy
  equation and the extra derivative data, not as a regularity theorem.

The proposed adapter is w=U_classical (or a fixed constant multiple), NOT
v=U_classical. It normalizes u exactly but is not a proved hydrodynamic limit.
A conformal neutral fluid has no massive conserved rest-density variable;
its equilibrium shear limit is not a full incompressible c-to-infinity theorem.
The temperature and BDNK derivative initial data are additional unknowns.

## 2. Exact nonlinear energy component

Let L=partial_t log Theta, dgamma=partial_t gamma, divw=sum_i partial_i w_i,
wg=w dot grad gamma, and wL=w dot grad log Theta. Direct tensor expansion gives

    T00 = epsilon(4 gamma^2-1)/3 + Cg dgamma + CL L + spatial,
    Cg = chi(4 gamma^2-1)/3 +2 lambda gamma^2 -4 eta(gamma^2-1)/3,
    CL = chi gamma(4 gamma^2-1)+2 lambda gamma(gamma^2-1),
    spatial = [chi(4 gamma^2-1)/3+2 eta(gamma^2-1)/3] divw
              +2(lambda-eta)gamma wg
              +[chi(4 gamma^2-1)+2 lambda gamma^2]wL.                 (1)

This retains the heat flux, shear, and frame energy correction, including the
negative shear contribution. The coefficient used below is not obtained by
throwing away terms of an unknown sign. Define

    C = 4 chi0/3 +2 lambda0 -4 eta0/3 >0,
    B = 4 chi0 +2 lambda0 >0,  kappa=B/C>1.                           (2)

In frame A, C=32 eta0 and kappa=25/12. These signs hold throughout the
stated conformal causal family, not only in this frame.

## 3. Nonlinear no-go theorem for a specified similarity class

Let tau=t_star-t and xi_i=x_i/tau^beta_i, with a>0 and 0<beta_i<1. Let D0
be a bounded neighborhood of xi=0 invariant under contraction
xi_i -> r^beta_i xi_i for 0<r<=1. Suppose a smooth solution on this shrinking
neighborhood has profiles

    tau^a gamma(t,tau^beta xi) -> G(xi),
    tau^a w(t,tau^beta xi) -> W(xi),
    tau^b Theta(t,tau^beta xi) -> H(xi),                              (3)

where G>=0 is not identically zero, H>0, and G^2=|W|^2. The convergence is
weighted C2: on every compact contraction-invariant subdomain, all xi and
tau partial_tau derivatives of total order at most two converge to the
corresponding profile derivatives; derivatives containing tau partial_tau
converge to zero. Profiles extend with bounded derivatives to xi=0, and H
is bounded away from zero there. These explicit hypotheses exclude unresolved
finer oscillations or uncontrolled time derivatives of the remainder.

**Theorem.** Under (1)--(3) and bounded S, no such solution exists when

    b > -a/kappa.                                                   (4)

In particular, b>=0 (temperature constant in scale or heating) is excluded.
No finite-energy assumption, energy condition, or global continuation
criterion is needed for this local similarity exclusion.

**Proof.** Put L_beta=sum_i beta_i xi_i partial_i. The material derivatives
are kept inside the full tensor before asymptotic expansion. Its exact identity
for sigma in section 1 shows that derivative stresses contain at most three
powers of gamma: the apparent extra projectors cancel by u dot partial u=0.
With the weighted C2 hypotheses, the stress and its differentiated remainders
therefore have the following upper orders:

| Contribution | T^{mu nu} order | Largest spatial-divergence order |
|---|---|---|
| Ideal | tau^(-4b-2a) | tau^(-4b-2a-beta_max) |
| Time-derivative constitutive terms | tau^(-3b-3a-1) | tau^(-3b-3a-1-beta_max) |
| Space-derivative constitutive terms | O(tau^(-3b-3a-beta_max)) | O(tau^(-3b-3a-2beta_max)) |

The time derivative of the dominant energy has one additional tau^(-1).
Since beta_max<1, all spatial contributions are lower order. This is a
comparison of differentiated expansions, not an assumption that the PDE
is homogeneous or that spatial gradients vanish.

If b<a+1, the time-derivative stress dominates the ideal part. Equation (1) gives

    T00 = tau^(-s)[F(xi)+o(1)],  s=3a+3b+1,
    F = H^3 G^2 { C(aG+L_beta G)
                   +B G[b+L_beta log H] }.                          (5)

Its energy equation, multiplied by tau^(s+1), implies

    (s+L_beta)F=0.                                                  (6)

Under (4), s>0, because kappa>1. A bounded profile satisfying (6) is zero:
F(r^beta xi)=r^(-s)F(xi), and boundedness as r goes to zero gives F(xi)=0.
This dilation argument includes profiles vanishing at the spatial origin.

Set Z=H^(3 kappa) G^3, a nonnegative bounded C1 function. No division by G
is needed at its zeros. Direct differentiation rewrites (5) as

    F=(C/3)H^(3-3 kappa)
        [L_beta Z+3(a+kappa b)Z].                                  (7)

Since a+kappa b>0, the same dilation argument gives Z=0, hence G=0,
contradicting (3).

If b>a+1, the ideal part dominates. Its leading energy is
F_ideal=4 H^4 G^2/3 with s_ideal=4b+2a>0. Again the energy equation implies
(s_ideal+L_beta)F_ideal=0, contradicting its bounded nonzero profile.

At b=a+1, both contributions have the same positive exponent. The argument
first gives F+4 H^4 G^2/3=0. Equation (7) then yields

    L_beta Z+3(a+kappa b)Z=-(4/C)H^(1+3 kappa)G^2 <=0.

Along a contracting ray, r^[3(a+kappa b)]Z(r^beta xi) has nonpositive
derivative and limit zero at r=0. Thus Z<=0. With Z>=0 this again forces
G=0. This proves the theorem in all three cases. QED.

**Source application and exact scope.** The proposed normalized leading NS
core has a=1/2+h, beta=(1/2,1/2,1/2-h); its radial proper component is lower
order after multiplication by tau^a. Whenever the lifted full core, its
corrections, and a thermal completion satisfy (3), (4) excludes it. In frame A
any survivor in this class would need b<=-12a/25, i.e. temperature tending
toward zero at least at that power, or would have to violate another hypothesis.
This is a necessary condition, not a constructed cooling solution.

We do NOT assert that every possible relativistic adaptation, every original
oscillatory correction, or every thermal completion satisfies (3). A leading
balance in a core with finer spatial/time scales requires a different argument.
The excluded class is nonempty as an ansatz class (constant nonzero W and
constant positive H already give normalized timelike test fields); it is not
claimed to contain a previously known BDNK solution.

## 4. The independent causal-shear obstruction

Linearize the same complete tensor at rest with epsilon0=Theta0^4, and take
an infinitesimal transverse perturbation v_y(t,x), delta Theta=0. Writing
h0=epsilon0+P0, one obtains

    T^{0y}=h0 v_y+lambda partial_t v_y,
    T^{xy}=-eta partial_x v_y,
    lambda partial_tt v_y+h0 partial_t v_y-eta partial_xx v_y=0.       (8)

Coefficients here are evaluated at equilibrium. Define tau_Q=lambda/h0,
D_s=eta/h0. A Fourier mode has exact exponents

    s_+-=(-1 +- sqrt(1-4 tau_Q D_s k^2))/(2 tau_Q).                   (9)

The slow root is -D_s k^2+O(k^4) at small k. Above
k_c=1/(2 sqrt(tau_Q D_s)), both roots have real part -1/(2 tau_Q),
independent of k. The high-frequency characteristic speed is sqrt(eta/lambda).
An oscillatory eigenmode gives a direct counterexample to a uniform-in-k
heat multiplier estimate exp(-c D_s k^2 t), even at one fixed positive time:
normalize the complete mode state (v,v_t/k), not only the initial velocity.
Its norm stays comparable to exp[-t/(2 tau_Q)] as k increases.
This is an exact linear obstruction, not proof of nonlinear blow-up.

The NS pulse mechanism increases the wavenumber until viscous k^2 damping
beats amplification (source section 2.2). Equation (9) means that this heat
argument cannot simply be imported into causal BDNK. It does not exclude a
new nonlinear pulse mechanism with a different damping estimate.

Linearized MIS shear, h0 v_t+partial_x pi=0 and
 tau_pi pi_t+pi=-eta v_x, gives the same telegraph equation when
 tau_pi=lambda/h0. Thus this particular barrier is shared by matched
relaxation models; it does not establish nonlinear equivalence of the models.

## 5. The obvious nonlinear shear shortcut also fails

In the full 3+1 tensor, set u=(sqrt(1+p(t,x)^2),0,p(t,x),0) and Theta constant.
This is an EXACT normalized plane ansatz, not a linearization. With gamma=u0,

    T^{0x}=-eta partial_x gamma,
    T^{xx}=epsilon/3+(chi+2 eta)partial_t gamma/3,
    partial_t T^{0x}+partial_x T^{xx}
       =(chi-eta)partial_tx gamma/3.                               (10)

The causal parameter family has chi>eta. Generic time-dependent shear
therefore fails the longitudinal momentum equation. Keeping only (8) is
not a consistent nonlinear reduction. Any shock construction must retain
induced longitudinal flow, temperature evolution, and the derivative data.

## 6. Heating cannot rescue validity at finite energy on these scales

This is an additional conditional physical diagnostic, not used in the theorem.
Assume a core patch with G,H bounded below, nonnegative total energy density,
uniformly bounded integrated energy, and T00>=c epsilon gamma^2 on that patch,
as required by a quantitatively small constitutive correction. Set
V_beta=sum beta_i. Integration over that patch forces

    b <= (V_beta-2a)/4.                                            (11)

If G(0),H(0)>0 and b>=0, the exact frame energy correction has

    A/epsilon ~ chi0(3b+a)G(0)/H(0) * tau^(b-a-1).                  (12)

For the NS scales, (11) gives b<=1/8-3h/4, while boundedness of (12)
requires b>=3/2+h. The intervals are disjoint. Thus simply heating a
finite-energy normalized NS core cannot keep this first-order correction
small. Negative exterior energy cancelling the core or a cold-vacuum limit
would violate the diagnostic assumptions, not repair this conclusion.

## 7. Outcome, stopping point, and pivot

The direct noncooling normalized-core transfer is excluded in the stated
weighted-C2 class, including smooth forcing. This is not universal healing:
bounded-state shock formation (a=0), causal or finer scales (some beta_i>=1),
rapid oscillatory profiles, sufficiently cooling/vacuum regimes, and other
constitutive models are not covered. Even relativistic ideal-fluid energy
conservation excludes its analogous ideal-dominated similarity class; the
result must not be advertised as a universal viscous regularizing effect.

The next new producer is a faithful nonlinear characteristic-steepening
argument for the full coupled BDNK fields with bounded timelike velocity and
positive bounded temperature. Its coefficients and damping must come from
the actual constrained equations; (10) rejects the easiest scalar-shear
shortcut. Neither (8) nor the RVM signed-impulse theorem supplies that producer.
This packet does not know the sign/size of that full nonlinear steepening term
or construct the required Cauchy solution. Audit the exclusion first, then
attack this distinct producer rather than tune the already-excluded lift.

## 8. Executed verification and limits

`python3 research/check_bdnk_transfer.py` passed 121 exact algebraic checks
with SymPy 1.14.0; the actual stdout is recorded beside this file. The checker
constructs the four-tensor independently on twelve rational normalized jets,
checks all constraints and (1), verifies (2),(7), the shear polynomial/MIS
elimination, (10), and the exponent arithmetic. `py_compile` passed.
Those computations support the argument but do not prove its universal
asymptotic quantifiers, establish novelty, or constitute independent review.

A read-only full-repository snapshot download for repository-wide verification
failed because the execution container could not resolve codeload.github.com.
No `research/verify.py`, LaTeX build, Lean build, Comparator, or CI run is
claimed. Publication uses GitHub Git objects and a non-force leased ref update.
Only navier is changed; jc2, navier-formal, and vlasov-maxwell are left intact.
