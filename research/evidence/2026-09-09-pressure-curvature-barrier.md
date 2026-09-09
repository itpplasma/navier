# Positive pressure curvature blocks a fixed-viscosity Euler-history transfer

Date: 2026-09-09. Frozen research input:
`68cf0c6cea4aab2689ad8be1219f14a1764938ff`.
AUTHOR PROOFS; independent mathematical audit PENDING; novelty undetermined.
The complete proofs are immediately integrated in
`paper/sections/viscous_history.tex`, subsection `pc:section`.
No canonical graph or formal theorem is promoted.

## 1. Consumer first: a whole construction class, not another ray calculation

The current Euler-history route proposes retaining a global upper pressure-
Hessian bound while generating diverging gradients with summable initial
increments. The theorem below shows that these requirements are INCOMPATIBLE
for exact unforced R3 NS at any fixed positive viscosity. The proof includes
all modes, the entire exterior and the canonical pressure; it has no carrier,
packet-width, symmetry, separation or overlap assumption. This removes the
whole budget-preserving transfer, rather than just the unchanged ray scales.
It does not exclude a redesigned history with unbounded positive curvature.

The independent positive consumer is precise. Let

    M(t)=||u(t)||infinity,
    K(t)=max(0, sup_x lambda_max(Hess p(t,x))),
    A(t)=integral_0^t sqrt(K(s)) ds.

For an absolute finite C, the actual equation gives

    M(t) <= M(0) exp(C A(t)).                            (1)

Consequently finiteness at a putative finite endpoint T of

    integral_0^T exp(2 C A(t)) dt                       (2)

bounds integral M^2 and hence enstrophy. LOCAL's H1 alternative excludes T.
In the easier case A(T)<infinity, (1) plus ENERGY gives bounded L3 by
||u||3^3<=M||d||2^2, and the existing CONTINUATION/LOCAL/ENERGY chain completes
regularity, including normalized pressure. No RF-family replacement is made.
For arbitrary data neither A(T) nor (2) has been bounded from the input.

## 2. Complete theorem and constants

For f in C2(R3) with D2f<=k I globally, k>=0, define the ball BMO seminorm
B=sup_Q average_Q |f-average_Q f|. The proved elementary interpolation is

    ||grad f||infinity <= 48 sqrt(2 k B).                (3)

Only the UPPER Hessian is bounded. Subtracting f from k|x-x0|^2/2 gives a
convex function. On a radius-r ball its central value is at least its average
minus 16 times its mean oscillation; its values on the half-ball are at most
the average plus 8 oscillations. The supporting plane therefore bounds its
central gradient by 48 oscillations/r. The quadratic correction contributes
at most kr^2/2. Optimizing r proves (3), including k=0 and B=0 by limits.

For the canonical p=sum R_i R_j(u_i u_j),

    [p]_BMO <= C_p M^2.                                 (4)

The manuscript provides the usual full proof: near/far splitting of the
stress, the L2 multiplier bound for the near part, and the actual derivative
of the Newtonian pressure kernel for the far oscillation. No false L-infinity
boundedness of a Riesz transform, extra harmonic pressure, or local pressure
closure is used. Equations (3)--(4) give (1) with C=48 sqrt(2 C_p) by the
regularized-speed maximum principle. C is not claimed sharp.

The stronger necessary condition for blowup is divergence of (2), not only
A(T)=infinity. In particular, a terminal bound K(t)<=c/(T-t)^2 with
2 C sqrt(c)<1 excludes blowup. A finite singular endpoint therefore requires

    limsup_(t->T) (T-t)^2 K(t) >= 1/(4 C^2).             (5)

No bound for the absolute value of a negative pressure eigenvalue occurs.
Under NS scaling, K_lambda(t)=lambda^4 K(lambda^2 t), and A is invariant.

## 3. Quantitative no-transfer theorem for an exact family

Fix nu>0 and H<infinity. Let u_j be ANY exact canonical unforced solutions
through times t_j<=H, with real solenoidal Schwartz data d_j and

    sup_j ||d_j||H3 <= B3,
    sup_j ||d_j||infinity <= Binf,
    sup_j integral_0^t_j sqrt(K_j(t)) dt <= B.

Then

    ||grad u_j(t_j)||infinity
      <= c_s B3 exp[(c_3/(2nu)) Binf^2 H exp(2 C B)]      (6)

uniformly in j. The proof is a complete viscous H3 energy bound using
||D^k(u tensor u)||2<=c M||D^k u||2 for 0<=k<=3. The intermediate derivative
interpolation inequalities are proved by integration by parts in the
manuscript. Thus no assumed endpoint convergence or unknown future Sobolev
norm is hidden in (6).

In particular a fixed-viscosity clone of the Euler construction cannot have
ALL of: bounded times, summable initial increments in H3, a single global
Hess p_j<=K_plus I with K_plus independent of j, and unbounded final gradients.
The initial-increment hypothesis in every Hm is stronger than required.
This includes freely prepared, overlapping, analytic-leakage architectures
and arbitrary full-vector exteriors. The obstruction is not an instantaneous
sign assertion at a chosen point.

The source's original inviscid result is not contradicted. Bound (1) also
controls Euler velocity in this class, but the H3/enstrophy implication uses
strictly positive viscosity. The constants in (6) deteriorate as nu decreases
to zero; this is an exact distinction, not a silent uniform inviscid limit.

## 4. Primary-source and originality ledger

Sources revisited on 2026-09-09:

* OpenAI, *Finite Time Blowup for the Euler Equation*,
  https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf .
  Main theorem, sequence of exact Euler solutions, summable Hm initial
  increments, global upper pressure-Hessian bound, and its displacement
  coercivity role directly inspected. The rendered printed page 3 explicitly
  displays the one-sided bound and the gradient/increment requirements.
  Parsed and rendered pagination still differ, so no mixed equation-number
  attribution or newly recomputed file fingerprint is claimed. Our theorem
  is stated and proved independently of those pagination details.
* Connected GitHub revision read:
  openai/NavierStokesAndEuler/main at
  `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`.
  This is a current revision check, NOT an Euler Lean build, independent source
  proof audit, or revalidation of the inherited PDF hash.
* OpenAI, *Finite Time Blowup for Navier--Stokes*,
  https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf .
  Main statement rechecked: smooth forcing and zero initial datum. Retain the
  owner's acceptance and prior forced-kernel record. No unforced consequence
  or current kernel replication is inferred.
* Seregin--Sverak, *Navier-Stokes equations with lower bounds on the pressure*,
  Archive for Rational Mechanics and Analysis 163 (2002), 65--86,
  DOI 10.1007/s002050200199, MiS preprint 92/2001.
  Primary institutional abstract/metadata inspected:
  https://www.mis.mpg.de/de/publications/preprint-repository/article/2001/issue-92 .
  Its full-preprint endpoint was rejected for an octet-stream content type;
  the publisher PDF endpoint redirected to metadata. Exact theorem hypotheses
  were NOT inspected and no theorem from it is imported. Pressure criteria,
  including one-sided pressure criteria, are prior art.
* Chae--Constantin, *Remarks on type I blow up for the 3D Euler equations and
  the 2D Boussinesq equations*, arXiv:2103.10672v1,
  https://arxiv.org/pdf/2103.10672 .
  Theorem 1.1, Remark 1.1 and the kinematic formulas on printed pp2--4 inspected.
  The criteria involve signed directional Hessian/strain combinations, not
  the positive largest-eigenvalue clock used here. They concern Euler, not a
  fixed-positive-viscosity transfer. No optimality comparison is asserted.
* Palasek, arXiv:2605.13827v1,
  https://arxiv.org/html/2605.13827v1 .
  The existing ledger records pre-activation damping as prior art for a model.
  This source was revisited; it is not an unforced original-NS embedding.
  The new obstruction here is independent of a chosen frequency history.

Targeted searches for pressure semiconcavity, positive Hessian eigenvalues,
BMO and regularity did not locate an exact predecessor for the full combination.
That is NOT a novelty certificate. The semiconcavity estimate, classical
L-infinity-to-BMO argument, speed maximum principle and viscous continuation
all require ordinary mathematical scrutiny. No priority is claimed.
Caltech and other previously logged sources retain their existing hypothesis
and audit gates; no new completed stability certificate was obtained here.

## 5. Adversarial checks and exact boundary

The proof retains the whole-space pressure and all velocity components.
A bound on one material curve or one core is insufficient for (3) at arbitrary
x,r. A merely local pressure may contain harmonic terms not controlled by (4).
A forced field has an extra speed source and a different pressure equation.
The sharp Fourier-ball projected RF flows do not obey the same pointwise speed
equation, so (1) is NOT asserted for that family. The theorem instead uses the
original-branch L3/enstrophy continuation consumer directly.

Negative curvature alone is not dangerous in (3), but no sign of the actual
pressure work is assumed. A nonzero affine pressure has infinite global BMO;
it is not a counterexample. Pure-gradient perturbations of pressure do not
change the fixed canonical representative. The zero velocity is handled
without division. Compact classical intervals justify all maximum principles
and integrations by parts; endpoint estimates are uniform precisely when the
displayed clocks are finite.

`research/check_pressure_curvature.py` checks finite identities in the proof,
not the universal BMO lemma, PDE maximum principle, all functions, independent
correctness, or the cited Euler construction. No independent reviewer or
formal proof is claimed. Canonical graphs stay unchanged.

## 6. Consequence for the live attack

Retire the requirement that a successful unforced viscous transfer preserve
the Euler source's global upper pressure-Hessian budget. That requirement now
contradicts the desired outcome, independently of a repair of packet damping.
The remaining construction must realize one common datum with a genuinely
unbounded positive-curvature history and a DIFFERENT, actually viscous history
inverse that tolerates it. A local/directional action bound is logically
weaker and has not been ruled out by this theorem. Alternatively an input-only
bound for (2) would prove the positive terminal result, but it has not been
produced and is not claimed to be easier than the original problem.
