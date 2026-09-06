# Speed-shell cancellation and the effective defect (2026-09-06)

## Frozen inputs and status

Research baseline: `20db07ae50842a0e0bd7c72c6a8b4512cfd2735a`.
Paper baseline: `eb0c551f9bf38c899e019eaaa464fc24db429116`.
New proof: `itpplasma/navier-paper` commit
`5643f3e53ce837896fdd69247c3972ba4180ebfa`,
`sections/speed_shell.tex`, SHA-256
`6d4ed41005c59d2734a1befc41779ec63e0bd6805c3178dc42b54c9a0efae4da`.

Status: full author-checked component proofs; independent mathematical audit
pending. No graph node, formal phase, or terminal claim is promoted. The
original unforced equation on R3, every positive viscosity, and the selected
Schwartz-data branch remain the target. This is not a complete arbitrary-data
paper proof, because the temporal estimate identified below is not derived.

Project premises are accepted quotient regularity and evolution plus the
separately pending signed-work component. The final fourth-power consumer
also uses the separately pending quotient dissipation clock. This author
check does not independently audit either predecessor. Snapshot assumptions
are solenoidal H^m data, m>=4, and the resulting representative with w in
L3 intersect L6, grad w in L2, sigma=-div w in L2,
div(|w|w)=0, w dot grad|w|=|w|sigma, and sigma=0 a.e. on {w=0}.
No finite L2 norm of w, moment condition, smooth unit direction or second
spatial derivative of w is assumed.

## 1. A stronger exact cancellation

For every k>0, not merely almost every k,

    integral_{|w|>k} sigma = 0.

Set rho=|w| and F_k=(rho/k-1)_+ w. The weak chain rule gives
`div F_k = 1_{rho>k} sigma`. The right side is L1 because its support has
measure at most k^-3 ||w||3^3. The flux belongs to L^(3/2), bounded by
rho^2/k. Therefore its pairing with a large radial cutoff tends to zero:
`||grad chi_R||3` is uniformly bounded, while the L^(3/2) tail of F_k tends
to zero. This is the required endpoint cutoff estimate; assuming F_k in L1
would be unjustified. The zero-level and positive-level Sobolev identities
remove any surface-measure or division-at-zero issue.

Differences yield cancellation on every finite positive speed shell. If
H_rho is the closed L2 span of speed-shell indicators, sigma is orthogonal
to H_rho. Every square-integrable Borel function of positive speed, extended
by zero on the zero set, belongs to H_rho. This follows by finite-measure
pushforward approximation and exhaustion. In particular the old identity
`integral sigma rho^3=0` is one member of a full family, not the only one.

## 2. An exact residual, not an assumed depletion factor

Let V=rho^(1/2)w, F0=V tensor V-rho^3 I/3, and

    chi = sum R_i R_j F0_ij
        = sum R_i R_j(V_i V_j)+rho^3/3.

The signed-work identity and self-adjoint Riesz multipliers give
`K=<sigma,chi>`. The scalar chi is not the velocity pressure. Let P_rho
be L2 orthogonal projection onto H_rho, and define

    N_rho = ||(I-P_rho)chi||2,
    delta_rho = 3 N_rho/(2 ||rho^3||2),

with delta=0 for w=0. The trace-free Fourier contraction has norm sqrt(2/3),
and ||F0||2=sqrt(2/3)||rho^3||2. Hence

    0 <= delta_rho <= 1,
    K = <sigma,(I-P_rho)chi>,
    |K| <= (2/3) delta_rho ||sigma||2 ||w||6^3.

This removes all speed-only contributions before Cauchy--Schwarz. There is
no claim that delta is uniformly below one, small, or time integrable.
For disjoint finite speed shells E_j, omitting zero-volume terms,

    N_rho^2 <= ||chi||2^2 - sum_j (integral_Ej chi)^2/|E_j|.

Nested dyadic speed partitions exhausting (0,infinity) give monotone
convergence to the exact residual. The formula is an analytic certificate
when its integrals are exact, not a claim that sampled quadrature is rigorous.

Countable rational piecewise-linear profiles prove measurability without
differentiating P_rho. The proof uses strong L3 continuity of w, local L6
boundedness, weak L2 continuity of chi, and strong L2 continuity of each
fixed profile composition. The infimum defining the residual is Borel.

## 3. Two rates that do not exceed the previous ones

The exact Young coefficient gives

    Q' + nu D/2 <= a0^3/(2 nu^3) delta_rho^4 ||sigma||2^4 Q,
    a0=9 C_S^2/8.

For every bounded Borel profile h, the full shell cancellation gives
`integral h(rho) sigma rho^3=0`. Consequently the signed form is unchanged
by replacing B0 with `B0+h(rho)sigma I`. Taking the infimum of the old
nonnegative Rayleigh rate over a countable family of compactly supported
rational piecewise-linear profiles, including zero, defines beta_nu. Then

    0 <= beta_nu <= b_nu(B0),
    Q' + nu D/2 <= 3 beta_nu Q.

There is no optimizing-profile or measurable-selection assumption. Each
fixed-profile Rayleigh expression is measurable by weak--strong pairing,
and countable supremum/infimum operations preserve Borel measurability.
The matrix correction is in L2 even though it is not trace free.

With c_nu the minimum of the two displayed coefficients and L_c=integral c_nu,

    Q(t)+nu/2 integral_0^t D <= Q0 exp(L_c(t)),
    integral_0^t ||sigma||2^4
      <= E0 Y0/(32 nu) exp(Astar exp(L_c(t))),
    Astar=8 C_S^3 C9^3 Q0/(3 nu^3).

The final line is conditional on control of L_c and uses the prior pending
quotient clock. The first line is an inequality valid on each compact
classical interval without a new hypothesis. All integrands are Borel and
locally bounded. No strict separation of trajectory finiteness criteria is
asserted; continuation would preclude the relevant endpoint separation.

## 4. Attempt at the missing bound and exact stopping point

The new spatial cancellation does not by itself prove

    sup_{t<min(H,Tstar)} integral_0^t c_nu(s) ds <= C(nu,u0,H)<infinity.

Using delta<=1 and beta<=b merely bounds this rate from above by the
original fourth-power defect rate. Combining that inequality with its own
consumer is circular. The existing energy/moment budgets give lower time
exponents; no justified estimate upgrades them to this critical integral.

The exact residual retains critical scaling: under u_lambda=lambda u(lambda x),
sigma_lambda=lambda^2 sigma(lambda x), chi_lambda=lambda^3 chi(lambda x),
and delta_lambda=delta. Thus delta^4||sigma||2^4 scales by lambda^2, canceled
by time scaling. Cancellation has not silently gained a derivative or time
power. No time derivative of the moving shell projection or optimizing
profile has been proved. Differentiating either variational definition as
though it were smooth is the first unsupported proposed dynamical step.
The new rates identify cancellation that a temporal argument may exploit;
they are not that argument. HIGH-PRESSURE, HIGH-STRAIN, DEFECT-L4 and NS-R3
remain open for this precise reason, not because of any historical label.

## 5. Source comparison and checks

Primary-source comparison inspected 2026-09-06:
Evan Miller, "Navier--Stokes regularity criteria in sum spaces",
arXiv:2007.02023v1, full text https://arxiv.org/html/2007.02023v1;
metadata https://arxiv.org/abs/2007.02023. The stated velocity-strain and
critical sum-space conditions do not provide a bound for this scalar speed
residual or correction Hessian. The paper already cites its published
version, Pure and Applied Analysis 3 (2021), 527--566,
DOI 10.2140/paa.2021.3.527. This is contextual attribution, not an imported
closure theorem or an exhaustive novelty search. No third-party text or PDF
is vendored, and no priority claim is made.

`tools/check_speed_shell.py` in the paper repository checks the frozen source,
labels, exact flux/Young/clock constants, critical scaling and 400 finite
weighted projection examples. These are author regressions, not tests of
PDE trajectories, infinite-dimensional projection limits, independent
mathematical review, or Lean formalization. Existing component regressions
are retained. Local main-document compilation succeeded after configuring
the available bibtex.original executable; no repository workaround for the
local tool alias is needed. Remote build results must be inspected separately.

Independent audit must reconstruct: the L^(3/2) cutoff at every threshold;
positive-level and zero-set chain rules; density for the varying speed
subspace including atoms of its pushforward measure; the Riesz sign and both
trace-free factors; nested-shell limits; countable-profile measurability;
the absence of a required minimizer for beta; the Young coefficient and
minimum-of-rates integration; and the exact dependency on pending quotient
clock and signed-work proofs. No independent audit is claimed by this note.
