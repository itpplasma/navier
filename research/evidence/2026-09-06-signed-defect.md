# Signed defect cancellation and one-sided form clock (2026-09-06)

## Frozen inputs and scope

Research baseline: `itpplasma/navier` at
`4e0893e1ee3e3a2ab6684ef8590dcdcd661cf521`.
Manuscript baseline: `itpplasma/navier-paper` at
`aa9f9c4056bc718b1e83058861159b4382bed2a4`.
New source: `itpplasma/navier-paper`, commit
`a14114b8527630a469e7afdea1d2ec53bacfe8f5`,
`sections/signed_defect.tex`, SHA-256
`2e0a101a00a9a9170b0d750a41876a8f556af747184d509dc22a6b5eda1b6a27`.

Status: full author-checked component derivations; independent mathematical
audit pending. No Lean result or open claim is promoted. The equation,
domain, viscosity and branch are the original unforced three-dimensional
Navier--Stokes equation on R3, nu>0, with the selected Schwartz-data
classical branch. The snapshot cancellation needs solenoidal H^m data,
m>=4. No spatial moment assumption is needed.

Project inputs are the accepted quotient regularity/evolution and weighted
dissipation results. The final direct continuation implication additionally
uses the review-pending `de:quotient-clock` component. This dependency is
explicit; the present author check is not a new independent audit of it.

## 1. Exact signed cancellation

With rho=|w|, V=rho^(1/2)w, A=rho w, sigma=-div w,
B_ij=R_i R_j sigma=partial_i q_j, and B0=B+sigma I/3, the new source proves

    integral sigma rho^3 = 0,
    K = -integral V^T S(u) V = integral V^T B V = integral V^T B0 V.

The cutoff proof is important. w belongs to L3 and L6, hence to L4;
rho^3 grad w belongs to L1. Thus F=rho^3 w belongs to W^(1,1) and L1,
div F=2 sigma rho^3, and a standard cutoff gives integral div F=0.
There is no assumption that the representative is smooth or in L2, and
no division by rho at its zero set. The velocity term removed by div A=0
has separately justified integrability and vanishing cutoff errors.

Plancherel gives ||B0||2=sqrt(2/3)||sigma||2. The trace-free part of
z tensor z has Frobenius norm sqrt(2/3)|z|^2. These two factors give

    |K| <= (2/3) ||sigma||2 ||w||6^3.

This avoids the old mixed pairing with u=P w and hence its Leray constant.
The exact Young coefficient in the quotient inequality is now

    Q' + (nu/2) D <= a0^3/(2 nu^3) ||sigma||2^4 Q,
    a0 = 9 C_S^2/8.

The earlier audited coefficient (81/32) C6^4 a0^3 is not deleted or silently
relabelled as audited. The improvement is a separately frozen component.
The exponent four has not improved.

## 2. A signed quadratic-form alternative

Define b_nu(M) as the positive part of the supremum, over nonzero smooth
compactly supported vector fields psi, of

    [integral psi^T M psi - (4 nu/9) integral |grad psi|^2]
    / integral |psi|^2.

This is a variational definition, not an asserted eigenvalue theorem.
The source proves extension to H1 by density, finiteness, countable-test
measurability and local boundedness on the branch. For M=B0,

    0 <= 3 b_nu <= a0^3 ||sigma||2^4/(2 nu^3),
    Q' + (nu/2) D <= 3 b_nu Q,
    Q(t) + (nu/2) integral_0^t D <= Q0 exp(3 integral_0^t b_nu).

The form controls only signed amplification after subtraction of a fixed
viscous form. A finite input-only bound on its accumulated value would
suffice; estimating the full defect fourth power first is unnecessary.
With E0=||u0||2^2, Y0=||grad u0||2^2 and
Astar=8 C_S^3 C9^3 Q0/(3 nu^3), the original requested integral has the
fully explicit conditional bound

    integral_0^t ||sigma||2^4
    <= E0 Y0/(32 nu) exp(Astar exp(3 integral_0^t b_nu)).

This last step uses the pending quotient clock plus the accepted energy
identity and ||sigma||2^4<=Y^2/16. In particular its right-hand side is NOT
yet input-only: no arbitrary-data bound on the form clock is proved.

## 3. Critical amplitude-tail certificate

Let f=lambda_max(B0)>=0 and delta=4 nu/(9 C_S^2). The source defines
kappa_nu(f) as the infimum of positive rational k with
||(f-k)_+||_(3/2)<=delta. It proves Borel measurability and

    0 <= b_nu <= kappa_nu <= a0^3 ||sigma||2^4/(6 nu^3).

The exact scalar estimate is

    (x-k)_+^(3/2) <= (3 sqrt(3)/16) k^(-1/2) x^2,

whose constant is attained at x=4k. This is an amplitude cutoff, not a
Littlewood--Paley frequency cutoff. Any measurable integrable k(t)>=0
satisfying the displayed tail-smallness condition a.e. is a sufficient
certificate. Actual Navier--Stokes scaling sends b_nu and kappa_nu to
lambda^2 times their original values, so their time integrals are critical.

## 4. Where the attempt to close the missing bound stops

The available inequality bounds b_nu and kappa_nu ABOVE by a constant
times ||sigma||2^4. It does not bound that unknown integral by initial
data. Combining it with the new conditional bound gives only a circular
inequality. Neither a smaller coefficient, a locally finite Rayleigh rate,
nor a finite clock on each compact classical interval is an estimate
uniform at a putative finite maximal time.

A budget-level diagnostic makes the restriction precise. Choose a nonzero
real Schwartz scalar s and M=(R_i R_j s)+s I/3. The matrix is a nonzero
trace-free L2 field. There exists a smooth compactly supported vector test
psi with integral psi^T M psi>0: otherwise the matrix would be negative
semidefinite a.e., and its zero trace would force M=0, contrary to
||M||2=sqrt(2/3)||s||2. Multiply s by a sufficiently large fixed positive
amplitude so that b_nu(M)>0. Set lambda(t)=(T-t)^(-1/2) and
s_t(x)=lambda(t)^2 s(lambda(t)x). The Hessian-multiplier relation and
scaling give b_nu(M_t)=lambda(t)^2 b_nu(M), whose time integral diverges.
But ||s_t||2^2=lambda(t)||s||2^2 is time integrable,
||s_t||_(3/2)^2 is constant, and || |x|s_t||2^2 scales as lambda(t)^(-1).
Thus those three bare functional budgets cannot control the form clock.
This is a scalar-field diagnostic, NOT a Navier--Stokes solution, NOT an
assertion that s_t is the minimizing representative's actual defect, and
NOT a no-go theorem against using the vector equation. In particular the
older non-solution curve with divergent defect fourth power does not by
itself prove divergence of b_nu; the sign argument above is needed for this
separate budget-level diagnostic.

The next positive target is an input-only estimate

    sup_{t<min(H,Tstar)} integral_0^t b_nu(B0(s)) ds
    <= C(nu,u0,H) < infinity,

or an explicit integrable amplitude certificate, obtained from vector
Navier--Stokes evolution rather than the listed scalar budgets. The new
component proves its consumer, not its producer. HIGH-PRESSURE,
HIGH-STRAIN, DEFECT-L4 and NS-R3 remain open. No strict separation of
finiteness conditions on actual selected finite-horizon branches is claimed:
the continuation consumer excludes such a separation.

## 5. Primary-source comparison

Directly inspected 2026-09-06: Evan Miller, "Navier--Stokes regularity
criteria in sum spaces", arXiv:2007.02023v1, Theorem 1.2 and the mixed
sum-space decomposition arguments. Metadata verified at
https://arxiv.org/abs/2007.02023; full text inspected at
https://arxiv.org/html/2007.02023v1. Published as Pure and Applied Analysis
3 (2021), 527--566, DOI 10.2140/paa.2021.3.527.

That theorem concerns the positive middle eigenvalue of the velocity
strain, with critical Lp_t Lq_x plus L1_t Linfinity_x decomposition.
Our matrix B0 is the trace-free Hessian of the cubic representative's
gradient correction. Miller's theorem is not applied to it. The comparison
is contextual, with no novelty claim for one-sided form estimates,
amplitude decompositions or the general sum-space mechanism. No third-party
PDF or text is vendored. All current derivations are in the new source.

## 6. Integration, tests and independent-review obligations

The paper source is included in main.tex and the abstract/proof boundary,
README, Makefile, bibliography and generated map are synchronized.
The research PLAN, dossier, README and candidate metadata are synchronized.
Every existing graph node, its class, formal phase and privacy flag stays
unchanged. The old phrase that a classical-gradient producer is "unusable"
is repaired: such a bound would establish continuation and is a legitimate
research target, but cannot be assumed as already available. The associated
Serrin statement is an implication, not equality of conditions.

`tools/check_signed_defect.py` contains exact rational constant checks,
2000 finite algebra probes and source/label checks. These are author
regressions, not an independent review, not tests on PDE trajectories and
not Lean formalization. Guarded integration scripts check frozen source
hashes, preserve nonoverlapping edits, reject mismatched generated maps,
and are replayed idempotently. The research verifier and the document
build cover structure only; the recorded workflow result must be checked
before reporting a successful remote build.

Independent review must reconstruct the W^(1,1) flux including the zero
set, the signed Hessian and strain representations, both trace-free
factors, each exact Young maximum, countable-test measurability, the
amplitude-infimum endpoint, and the direct quotient-clock dependency.
The first unsupported positive implication remains the uniform
arbitrary-data form-clock (or fourth-power defect) bound.
