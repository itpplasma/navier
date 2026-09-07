# Audit record for whole-space cubic refinement

Date: 2026-09-07. Controller record of actual fresh-context mathematical
reviews. Base `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`; initial worktree
patch SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Model-agnostic delegation was explicitly authorized by the owner for this run.
Review verdicts do not promote a terminal claim or recertify older literature.

## Component scopes

The following independent workers received the complete respective frozen
proof candidates in fresh contexts. They did not author those candidates.
Hashes identify the exact scratch revisions; the integrated durable proof is
`2026-09-07-whole-space-cubic-refinement.md` and receives its own review.

| Reviewer task | Scope | Candidate SHA256 | Verdict |
| --- | --- | --- | --- |
| audit_construction | Whole-space bandlimited Hilbert ODE, Bernstein, energy, full interlevel equation | `1d321fea6097ae55abb4f2603453d4259c57291299f398ef1631007abcd4970e` | PASS in Section 2 scope |
| audit_identification | Compact-classical L2 comparison and conditional endpoint consumer | `dbae75accbc6753fc7b9e7cce38788773066af98e40e1b6048bad2290e02e229` | PASS |
| audit_cubic | Sharp-shell synthesis, overlap, time quantifiers and cubic production | `6b773fd21eca3871269863a803ba3b9ec97d0bc1e9421945c3ba2b1c9dfb099a` | Spatial PASS; generic time statement REPAIR |
| audit_construction, separate subsequent scope | Actual separated-scale stress and scalar compensation test | `702724e83cf2138b2fb7128e1e4493dbe7ac74c5ee499bfb29d78c551c75000a` | PASS in Sections 3--4 scope |

## Required repair and surviving conclusions

The original generic cubic-family statement omitted strong time measurability.
Scalar norm control cannot imply it: take a nonmeasurable sign s(t), a fixed
nonzero bandlimited phi, u_0=0, and u_M=s(t)phi for M>=1. RF-CUBE holds as
a pointwise scalar bound, but the resulting L3 path is not measurable.
The corrected generic theorem explicitly assumes strongly measurable L2
paths and finite H. At fixed bandlimit the map L2 -> L3 is continuous by
Fourier inversion/interpolation, so the resulting paths are L3 measurable.
Countability removes a common null set; pointwise cubic tails and dominated
convergence give every finite L^q_t L3_x convergence. Actual smooth projected
ODE paths already satisfy the added measurability hypothesis. The durable
proof includes this repair and does not silently enlarge its generic scope.

The audit also supplies the uniform L2 tail by geometric Holder, with
constant (1-2^(-3/4))^(-2/3), and confirms that uniform-in-time L3 convergence
is unnecessary and does not follow from the weaker certificate. Disjoint
moving-time packets give the counterexample. A future integrated producer
must hold at every upper time t<=H, not solely at endpoint H.

The construction audit found no finite-dimensional or Poincare-gap premise;
real solenoidal L2 data suffice for fixed cutoff. The local identification
audit checked the H3-to-gradient-L-infinity bound, spectral H2 tail, zero-norm
Gronwall and every-finite-horizon quantifiers. Its local classical constants
are never used as the missing input-only critical constant. The paired audit
checked the support condition K<=N/2 and both high-parent dissipation costs;
its near-diagonal growth is a limitation of the bound, not an optimality claim.

## Final integration review

PASS: actual fresh-context `audit_integration` checked Sections 1--6.
The complete report is [the independent integration review](2026-09-07-cubic-refinement-integration-review.md).
It found no invalid implication in the stated component and conditional
claims. Frozen original integrated proof SHA256:
`2f0a91378b48f15ca28120b62b8a5fef5f3038b36b6ca77147cd2f14a30ca347`.
Its exact uncommitted new-file patch SHA256:
`c71c04638be94796b48170c54e50df74a5be5b4cb67918b90ddfb168c3bd3061`.
This is a reproducible immutable review input over the stated base commit;
being uncommitted does not make it unreproducible. The integration review
checked the complete durable proof, uniform Fourier convention, repaired
measurability, consumer composition and scope, rather than voting on the
component reviewers' conclusions.


A subsequent independent wording-delta review passed. Final proof SHA256:
`5e985a4587264d20650a6038132e0dd415ef223c3f2409f027f7b1a02481b31b`.
Delta-review SHA256:
`b3802f1ebf5823af31c0dabc4499ad2e6a7bccf2a29f389eb93af0846d330835`.
It confirmed exactly four changes: audit status, explicit coarse support,
an explicit sharpness annulus, and removal of the inaccurate adjective
"datum-independent" from a local classical spectral-tail comparison.
No equation or producer/consumer quantifier changed. The generic time
component's original REPAIR verdict is preserved as review history.

For reproducibility, reversing this complete delta reconstructs the original
frozen proof from the final tracked proof, including its exact digest:

This is a zero-context unified delta (apply with `--unidiff-zero`).

```diff
--- original-reviewed-proof
+++ final-reviewed-proof
@@ -4,2 +4,2 @@
-Status: integrated author proof; component audits completed, final integration
-audit pending. No NS-R3 proof, new singularity restriction, or novelty claim.
+Status: integrated author proof; independent component and final integration
+audits passed in their recorded scopes. No NS-R3 proof, new singularity restriction, or novelty claim.
@@ -160,2 +160,2 @@
-strongly measurable L2 paths, almost-everywhere stated supports, a bounded
-coarse L-infinity L2 norm and the essential-time certificate. Norm control
+strongly measurable L2 paths, almost-everywhere stated increment supports,
+coarse support in the radius-N0 ball, a bounded coarse L-infinity L2 norm and the essential-time certificate. Norm control
@@ -181,2 +181,2 @@
-Take a nonzero real solenoidal Schwartz phi supported in a strict Fourier
-annulus and f_j(x)=N_j phi(N_j(x-x_j)). Then c_j=||phi||2 and
+Take a nonzero real solenoidal Schwartz phi supported in the Fourier
+annulus {1/2<|xi|<1} and f_j(x)=N_j phi(N_j(x-x_j)). Then c_j=||phi||2 and
@@ -226 +226 @@
-Together with the datum-independent spectral tail of u on this interval,
+Together with the spectral tail of u on this interval,
```

## Verification scope

No new computational checker is used to certify the universal synthesis or
PDE implication. Their evidence is the displayed proof and independent
mathematical review. Research schema checks and the existing finite exact
regressions are separate structural/regression checks. No Lean verification,
independent reaudit of LOCAL/CONTINUATION/ENERGY literature, terminal proof,
or exhaustive novelty search is claimed.
