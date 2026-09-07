# Audit record for smooth-block transport repair

Date: 2026-09-07. Base ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df.
Actual independent mathematical review by audit_lorentz, followed by
rechecking the requested repairs and affected consumers. This record
certifies a scoped transport-estimate repair, not a critical producer.

## Inputs and verdicts

The original author input SHA256 was
`d2ffdb4e5dd5e78bbd63ae8b2193e996db3babb2276a27d25d482e42d9c08325`.
The substantive estimates (1)--(12) passed. Two downstream scope claims
required correction: the multiplier is smooth away from the origin, and
exact fixed-grid scale invariance applies to dyadic dilations. The audit
supplies a counterexample to unqualified smoothness at the origin.

The repaired proof SHA256 was
`45a3ca695e702b94710c9af94a275b6f490fef8070f29f4dee0c2ef8e6aa9f7f`;
its exact new-file patch SHA256 was
`a58697a5d472a7132006d6eba14815545f5e3ed493f4f14839e92c7821dfc21e`.
The complete repair recheck returned PASS. It verified that both corrections
are present, all equations (1)--(12) are unchanged, and the consumers remain
valid. The comparable-scale signed production estimate remains unproved.

Full reports below are retained verbatim. Their SHA256 digests are
`42a26d0b9b8f041ddec62c42f85372087d3a1c92b80cf913523ee4199180af43`
and `4194c856a9105861ca1a51f6be3f2b015a9f3debb38c5f3f5a598b0728dacd6a`,
respectively. This is an actual repair recheck, not a fresh audit of unchanged
mathematics falsely attributed to a new reviewer.

## Original independent review

# Independent audit: smooth-block transport repair

VERDICT: REPAIR for two non-load-bearing scope assertions.
The substantive cutoff-uniform energy estimate and conditional one-flow
analysis PASS. No first invalid bridge was found in equations (1)--(12).

REVIEWED SCOPE: the complete frozen
.git/navier-wave-20260907/smooth-block-repair.md, SHA256
d2ffdb4e5dd5e78bbd63ae8b2193e996db3babb2276a27d25d482e42d9c08325,
over declared base ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df.
This fresh, bounded Codex mathematical audit is authorized by the current
owner delegation override relayed by the controller. The projected R3
family and its energy identity are accepted inputs. The kernel identities,
frequency geometry, summation estimates, pressure/cutoff pairing, and
sixth-power differentiation were checked directly. This audit does not
certify a producer, a continuation theorem, or terminal regularity.

FIRST BAD BRIDGE: section 5's unqualified description of m_U as a smooth
symbol, if it claims C-infinity smoothness also at xi=0. The sum is locally
finite and smooth away from zero; global smoothness at zero is not implied
and can fail even for admissible Schwartz initial data. The proof only uses
the valid annular smoothness. A second precision error is section 6's
unqualified exact scale invariance for a fixed dyadic reference grid.
Both are downstream descriptions, not failed bridges in equations (1)--(12).

EVIDENCE FOR THE SUBSTANTIVE PASS:

1. Overlap, multiplier square, and sixth-power differentiation.

The telescoping identity sum_(j<=m)Delta_j=S_m is correct, and the full
partition recovers every L2 field away from the measure-zero origin.
For each k,

    (1/6) d(lambda_k^3 ||Delta_k U||2^6)/dt
       = lambda_k^3 L_k^4 <Delta_k U_t,Delta_k U>
       = <U_t,gamma_k Delta_k^2 U>.

Thus A_U must contain Delta_k^2. The identity has no gamma derivative
because it differentiates the sixth-power functional, not a quadratic
functional with prescribed moving coefficients. At L_k=0 the sixth-power
Hilbert norm is differentiable and all displayed terms vanish.
Annular support gives D_exact >= D/4 (with an even stronger constant under
the exp(-2pi i x.xi) convention). At finite N the upper index tail is finite;
the lower tail is dominated by geometric lambda_k powers and bounded L2
norms of U and U_t. High Sobolev bounds justify the continuum summation
on compact classical intervals.

2. The full cutoff and pressure correction.

Delta_k commutes with Q_N. Expanding Delta_k(U.grad U) gives
V_k.grad u_k+C_k+R_k exactly, hence

    (d_t-nu Delta)u_k+V_k.grad u_k
      = -Q_N(C_k+R_k)+(I-Q_N)(V_k.grad u_k).

Q_N=P_N P_Leray is an orthogonal projection and Q_N u_k=u_k.
Consequently its output correction is orthogonal to u_k, even when the
block crosses |xi|=N. Solenoidality gives
<V_k.grad u_k,u_k>=0 by integration by parts. Both (1) and (3) follow
without removing projections from the untested block equation.
No distance from the cutoff boundary is used anywhere in this argument.

3. Localization and the smooth low-strain commutator.

The support of V_k lies below lambda_k/32. For the first commutator
term, an input frequency must therefore lie in
[15lambda_k/32,65lambda_k/32]. The multiplier

    sum_(|j-k|<=4) phi(xi/lambda_j)
       = chi(xi/lambda_(k+4))-chi(xi/lambda_(k-5))

equals one on the larger interval
[lambda_k/16,16lambda_k]. It also equals one on the support of Delta_k.
Thus the stated localization of C_k is exact, not merely approximate.

Integration by parts using div V_k=0 gives the displayed identity

    [Delta_k,V_k.grad]f(x)
      = integral grad K_k(y).(V_k(x-y)-V_k(x)) f(x-y) dy.

The mean-value bound and
integral |y||grad K_k(y)|dy = constant
give (4) by Young's inequality in L2. For Delta_k(H_k.grad V_k),
the same input annulus is selected. In that enlargement Delta_j H_k
equals Delta_j U: its frequencies are above the support of S_(k-6),
including the harmless boundary where the smooth cutoff vanishes.
This proves (5). Multiplying by gamma_k L_k and using the fixed adjacent
frequency ratios gives exactly (6). The coefficient is low strain,
without a leftover lambda_k ||V_k||infinity term.

4. High-pair geometry and output gain.

Both indices in H_k=sum_(j>k-6)u_j exceed k-6.
If two such indices differ by more than 12, the larger input frequency
minus the smaller exceeds 2lambda_k, so their product cannot meet the
output block. The generously enlarged index set in (7) is valid.
This restriction is on the difference of the input indices, not on
their distance above the output; genuine high-high-to-low terms remain.

Since div H_k=0, the output derivative falls on the kernel.
Its L1-to-L2 norm is ||grad K_k||2=C lambda_k^(5/2).
The product L1 bound is L_i L_j. Multiplication by gamma_k L_k converts
this to (8); for |i-j|<=12, the factor
(lambda_i lambda_j)^(-1/2) is at most a fixed constant times lambda_j^(-1).
The resulting factor lambda_k/lambda_j=2^(k-j) is therefore correct.
No projection norm in Lp or pressure estimate is silently used.

5. Low and high summation.

Bernstein gives ||grad V_k||infinity <= C sum_(l<=k-6)lambda_l^2 a_l.
Apply a_k^5 a_j <= (5/6)a_k^6+(1/6)a_j^6 in (6) and reindex the finitely
many neighboring j. This gives (9), with the allowed enlargement of the
upper l index and fixed constants. The low-frequency factor is indeed
2^(2(l-k)); a crude transport bound lambda_k||V_k||infinity would have
only 2^(l-k).

For (8), bound a_j by A and apply the same Young inequality to a_k^5 a_i.
The first resulting term is bounded by C A D since
sum_(j>=k-C0)2^(k-j) is uniformly finite. For the second, reverse summation:
for each i and |j-i|<=C0,

    sum_(k<=j+C0)lambda_k^2 2^(k-j) <= C lambda_j^2
                                            <= C lambda_i^2.

This proves (10), including high-high-to-low output. Zero blocks cause
no singular factors. Neither (9) nor (10) supplies smallness for arbitrary
amplitude.

6. Signed identity and the energy clock.

At each fixed state, A_U is self-adjoint, while U.grad is skew-adjoint
in the relevant pairing. Therefore

    <U,[A_U,U.grad]U> = 2 b(U,U,A_U U),

which proves (11), without differentiating the state-dependent weights.
Its symbol is smooth away from zero, with the local smoothness needed for
the low-frequency mean-value bound. Its coefficients are not forced to
be equal or to have a favorable sign.

Finite overlap gives sum lambda_k^2 L_k^2 <= C G.
Since 0<=phi<=1, ||Delta_k^2 U||2<=L_k. Bernstein and the triangle
inequality in L3 then give

    ||A_U U||3 <= C sum lambda_k a_k^5
                <= C A^3 sum lambda_k a_k^2
                <= C A^3 G.

Vector Sobolev and Holder imply
|b(U,U,A_U U)|<=C A^3 G^2<=C sqrt(W)G^2.
Combining this with (1) and differentiating sqrt(W+epsilon) proves (12)
after epsilon decreases to zero. Thus the packet correctly retains the
uncontrolled integral of G^2; it does not replace it by the energy
integral of G.

REPLACEMENT ARGUMENT FOR THE SYMBOL SENTENCE:

Every compact subset of R3 minus the origin meets only finitely many block
supports. Hence m_U is C-infinity there, and its scale-local derivative
and kernel estimates are exactly those used in section 3. No assertion of
global C-infinity smoothness is needed.

Global smoothness can fail already at t=0. For example take the real
solenoidal Schwartz datum with Fourier transform

    d_hat(xi)=i (xi cross e) exp(-|xi|^2),

where e is a fixed nonzero real vector. The low blocks of P_N d agree with
those of d. A change of variables gives L_k^2=c lambda_k^5+O(lambda_k^7)
as k tends to minus infinity, with c>0. Thus
gamma_k=c^2 lambda_k^13+O(lambda_k^15). Finite overlap and the nonnegative
partition imply m_U(xi) is bounded above and below by positive constants
times |xi|^13 near zero. It is radial and even. If it were C^13 at zero,
its restriction to an axis would be an even C^13 function, with Taylor
coefficients through order 12 vanishing by the O(|xi|^13) bound and its
order-13 coefficient vanishing by evenness. It would be o(|xi|^13), a
contradiction. Thus global C-infinity smoothness is genuinely unavailable.

Replace the description with:

"Its instantaneous multiplier is smooth on R3 minus the origin, with the
uniform annular kernel bounds proved in section 3."

REPLACEMENT ARGUMENT FOR THE SCALING SENTENCE:

Write W_lambda0 to show dependence on the grid. For
U_r(x)=r U(r x), direct Fourier scaling gives

    Delta_(lambda_k) U_r(x)
      = r [Delta_(lambda_k/r) U](r x),

and its L2 norm is r^(-1/2) times the original block norm. Therefore

    W_lambda0(U_r) = W_(lambda0/r)(U).

If r=2^m, shifting the integer block index proves exact invariance.
Equivalently, rescaling the reference grid simultaneously gives

    W_(r lambda0)(U_r) = W_lambda0(U).

The same calculation gives D_(r lambda0)(U_r)=r^2 D_lambda0(U),
and the nonlinear production scales by r^2 as well. For arbitrary r
and a fixed grid, finite overlap between the two shifted dyadic
partitions gives equivalent norms, but not generally equality.
In particular, the smooth transition profile is not constrained to make
the sixth powers of the two overlapping blocks continuously scale invariant.

Replace the sentence with:

"Under dyadic NS rescaling, or simultaneous rescaling of the dyadic
reference grid, W is invariant and D and the nonlinear production scale
quadratically. Arbitrary rescalings at a fixed reference grid give
equivalent critical norms."

This exact qualification leaves every energy estimate and its constants
unchanged. It neither adds a hypothesis to the PDE theorem nor repairs
any missing producer.

CONDITIONAL SUFFIX THAT SURVIVES: the actual projected R3 solution,
including cutoff-crossing blocks, obeys (1)--(12). The smooth commutator
removes the specific low-transport boundary loss and gains one power of
low/output separation. The comparable-frequency and high-pair signed
spacetime control remains open at arbitrary amplitude.

UNNECESSARY DEPENDENCIES: no cutoff-interior adapter, sharp Lp projection
bound, weak-solution limit, continuation theorem, or external-advector
model is needed for these estimates. The estimates do not use independent
block orthogonality; only finite frequency overlap, L2 contraction of the
smooth block, and orthogonality of the actual tested Q_N are used.

NON-CLAIMS: no sign of the remaining commutator production, no temporal
critical producer, no inference of small critical amplitude from large N,
no terminal NS-R3 theorem, no source inspection, and no formal verification.
This review does not independently certify the earlier sharp-block
counterexample; the new smooth low-strain estimate was checked directly.

REOPENING CONDITION: after qualifying the symbol and scaling sentences, the audited
repair is mathematically passing in the stated scope. Any promotion to
a terminal route still requires the missing signed spacetime estimate and
its complete consumer, with their own frozen reviews.

## Repair recheck

# Recheck of the smooth-block scope repairs

VERDICT: PASS in the previously audited mathematical scope.

REVIEWED INPUTS:
- Base: ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df.
- Durable candidate: research/evidence/2026-09-07-smooth-block-repair.md.
- Candidate SHA256: 45a3ca695e702b94710c9af94a275b6f490fef8070f29f4dee0c2ef8e6aa9f7f.
- Exact new-file patch: .git/navier-wave-20260907/smooth-final.patch.
- Patch SHA256: a58697a5d472a7132006d6eba14815545f5e3ed493f4f14839e92c7821dfc21e.
- Prior full mathematical audit: .git/navier-wave-20260907/audit-smooth-block.md,
  SHA256 42a26d0b9b8f041ddec62c42f85372087d3a1c92b80cf913523ee4199180af43.

FIRST BAD BRIDGE: none remains in the repaired candidate's audited scope.

EVIDENCE:

Both supplied hashes match the files inspected. I read the complete frozen
new-file patch and the complete diff against the previously audited packet.
The changes consist of provenance and non-claim text plus the two requested
scope corrections. Equations (1)--(12), their hypotheses, and their proofs
are unchanged.

The multiplier is now asserted to be smooth only on R3 minus the origin.
This follows from local finiteness of the annular sum. The commutator
estimates use the individual smooth annular kernels and their uniform
scaled bounds; they require no global C-infinity extension of m_U through
zero. The earlier counterexample to global smoothness therefore no longer
contradicts any claim, and the cutoff-boundary energy pairing is unaffected.

The scaling paragraph now restricts exact invariance to dyadic dilation
or simultaneous dilation of the reference grid, states equivalence for
arbitrary dilation with a fixed grid, and includes the correct formula

    W_(lambda_0)(U_r) = W_(lambda_0/r)(U),  U_r(x)=r U(r x).

This follows directly from
Delta_(lambda_k)U_r(x)=r[Delta_(lambda_k/r)U](r x).
An integer shift of k proves dyadic invariance; simultaneous grid
rescaling gives the same result. The analogous direct calculation gives
quadratic scaling of D and the nonlinear production. Finite overlap
between shifted dyadic partitions supplies the stated norm equivalence
for a fixed grid. No proof consumer used the rejected unqualified equality.

REPLACEMENT ARGUMENT: the two exact replacements requested by the original
audit are now present and correct; no further replacement is required.

CONDITIONAL SUFFIX THAT SURVIVES: the actual full R3 projected NS family
obeys the cutoff-uniform smooth-block estimates, including blocks that
cross the cutoff boundary. The smooth commutator supplies the additional
low/output separation power. The signed production identity, absolute
C A D bound, and squared-enstrophy comparison remain valid in their stated
scope, as established in the prior full audit.

REMAINING GAP: input-only spacetime control of the signed comparable-scale
production and its high-pair tail at arbitrary critical amplitude.
Neither the repaired symbol description nor the corrected scaling statement
supplies that control.

NON-CLAIMS: no critical producer, no terminal NS-R3 conclusion, no source
audit of an imported continuation theorem, no formal verification, and no
canonical promotion by this worker. This is a repair recheck composed with
the identified prior full audit, not a second independent full review.


## Final heading correction

The prose checker required one heading rename after mathematical review.
The controller changed only that heading, not mathematical text. Reversing
the following complete delta reconstructs the exact repaired review input.

This is a zero-context unified delta (apply with `--unidiff-zero`).

```diff
--- reviewed-smooth-proof
+++ final-smooth-proof
@@ -168 +168 @@
-## 5. What improved, and what did not
+## 5. Smooth transport and comparable-scale production
```

Final proof SHA256:
`acb555a98b27f54f7fc4183ed2f99a3469d3c61f8f3d1d35516e1a4af31d7920`.
