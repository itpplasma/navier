# Dissipation-budget continuation and the full nonendpoint defect line

Date: 2026-09-06. **Status: complete component derivations, author self-check
only; independent mathematical audit pending. No terminal or gap promotion.**
`PLAN.md` remains the sole live programme status. This file is a frozen review
input, not a new task ledger or a replacement for the manuscript.

## Scope and source freeze

The user explicitly requested paper-proof work and commits in `navier` and
`navier-paper`, including unsigned commits. This task therefore adds a
standalone review supplement to the paper repository despite the earlier
read-only direction. It does not pause the ongoing formalization, change the
phase declarations, rewrite agent rules, or claim independent review.

Initial input pins:

- Research: `9c5def29be04e0d0e723677feae0437a0ea61300`.
- Manuscript: `065a962d6c6672dcf4bed2db17eb004081014a68`.

The argument is in the companion manuscript file
`dissipation_budget_continuation.tex`, SHA-256
`99ba06d12e59ed612aa588010c896e7b39484abb620560b748083272d8fd9977`.
The manuscript publication commit is
`dbd44acbf703539bb4bc9a05bc2ecd792d506c24`.
It is an independently buildable supplement, not included by `main.tex`.
The complete local and quotient packages are explicitly imported project
inputs; they are not represented as new proofs or published literature.
The new sufficiency lemmas and exponent calculations are proved in full.

The refresh during preparation found research main advanced to
`3dc52dc6e955a22931ae0b7a6ff62a3e0962135b`. Its three intervening commits
change the plan, the map generator/output, and add HF29 corridor evidence.
They do not change the mathematical inputs used here or the paths edited by
this continuation. The actual commit parent, not the initial read pin,
records the final refresh used for publication.

## 1. A useful dependency removal for the original pressure route

Let `E=||u||_2^2`, `Y=||grad u||_2^2`, `Z=||Delta u||_2^2`, and let `S` be
the homogeneous Sobolev constant. The direct enstrophy test gives

\[
 Y'+\nu Z\le (27S^2/16)\nu^{-3}\|u\|_6^4Y.
\]

The physical cubic dissipation satisfies

\[
 \|u\|_6^4\le (9S^2/8)\|u\|_3D_3.
\]

If the existing signed pressure hypothesis supplies, uniformly below
`min(H,Tstar)`,

\[
 \int_0^tP_3\le\theta\nu\int_0^tD_3+A,\qquad 0\le\theta<1,
\]

write `delta=1-theta` and `R=||u0||_3^3+3A`. Subtracting from the cubic
balance and retaining both terms proves

\[
 \|u(t)\|_3^3+3\delta\nu\int_0^tD_3\le R,
 \qquad
 \int_0^t\|u\|_6^4\le\frac{3S^2R^{4/3}}{8\delta\nu},
\]

and therefore

\[
 Y(t)+\nu\int_0^t Z
 \le Y_0\exp\!\left(\frac{81S^4R^{4/3}}{128\delta\nu^4}\right).
\]

The LOCAL blow-up alternative gives `Tstar>H` directly. Combining the
existing low-frequency bound with HIGH-PRESSURE supplies exactly this
hypothesis, with no new smallness or quantifier change. Hence the original
strict-pressure sufficiency path can avoid ESS, Leray-Hopf endpoint
membership, and backward uniqueness. This is a dependency reduction, not a
producer for HIGH-PRESSURE.

**Important non-deletions.** The standalone assertion that a bare uniform
`L3` bound forces continuation still retains its endpoint theorem. A
HIGH-STRAIN formulation allowing `theta=1` must not be silently changed to
strict absorption: at coefficient one the dissipation budget disappears.
The supplement gives a scalar counterexample to that inference, explicitly
not a Navier-Stokes field.

HF28 already used retained dissipation to remove ESS from the comparison-field
route. This continuation applies the same classical principle directly to the
original strict-pressure route. It makes no novelty claim.

## 2. The whole finite-exponent nonendpoint defect family

Use the existing cubic minimizer `w`, `q=w-u`, `Q=||w||_3^3/3`,
`Aw=|w|w`, `sigma=-div w`, and the quotient dissipation `D`. The imported
unweighted div-curl lemma includes global weak derivatives across zero sets,
`||grad q||_2^2=||sigma||_2^2<=Y/4`, and `w,q in L6`; it does **not** assert
`w,q in L2`. The existing weighted estimate is `||w||_9^3<=a0 D`,
where `a0=9S^2/8`.

The exact mixed identity is reconstructed with its sign and integrability:

\[
 Q'+\nu D=\int (R_iR_j\sigma)(A_w)_i u_j.
\]

It is already an `L2` pairing. Consistency of Riesz extensions on
`L2 intersect Ls` permits the additional Holder estimate without another
integration by parts in an unproved class.

For every finite `s>3/2`, define

\[
 \alpha=\frac{3}{2s},\qquad p_s=\frac{2s}{2s-3},\qquad
 r_s=\frac{3s}{s-1},\qquad \frac2{p_s}+\frac3s=2.
\]

With explicit unweighted Riesz/Leray constants the proof gives

\[
 |Q'+\nu D|\le b_s\|\sigma\|_s Q^{1-\alpha}D^\alpha,
 \qquad
 Q'+\frac\nu2D\le
 c_s\nu^{-3/(2s-3)}\|\sigma\|_s^{p_s}Q.
\]

The constants `b_s,c_s` are displayed in the TeX source. Exact Young
maximization is proved, not hidden in a generic constant. Multiplying by
`(4/3) Q^(1/3)` is valid at zero and yields a weighted `Q^(4/3)` dissipation
budget, followed by a direct `L4_t L6_x` continuation bound. Thus finite
accumulated defect on the entire nonendpoint derivative-critical line is a
sufficient condition. The existing `s=2,p=4` constant reduces exactly to
`81 C6^4 a0^3/32`.

The endpoint `s=3/2` is handled separately under a **strict smallness**
assumption. No theorem for an arbitrarily large endpoint norm is claimed.
The proof does not cover `s=infinity` and uses no false endpoint Riesz bound.
The family is conditional; energy does not establish any of its needed
arbitrary-data critical budgets.

## 3. Reconstruction of the HF30 comparison, with the right logical scope

Set

\[
 \Gamma=\nu^{-3}\int_0^t\|\sigma\|_2^4,\qquad
 B=\nu^{-3}\int_0^tY^2,\qquad C_\sigma=81C_6^4a_0^3/32.
\]

The supplement reproduces HF30's implication, with its displayed `J0`:

\[
 \Gamma\le B/16,\qquad
 B\le\frac{E_0Y_0}{2\nu^4}
       \exp\!\left(kJ_0\exp(4C_\sigma\Gamma/3)\right),
 \quad k=27S^2/16.
\]

On any finite interval ending at or before `Tstar`, the two accumulated
quantities are finite together. At a hypothetical finite maximal time both
are infinite. This rules out, on the actual classical branch, finite
fourth-power defect with divergent squared-enstrophy integral. It does not
prove a reverse instantaneous spatial norm inequality.

At the initial graph pin, DEFECT-L4's review called that question
"unsettled in both directions". This reconstruction supports the scoped
repair already proposed by HF30. **Do not label this self-reconstruction an
independent audit of HF30.** The graph sentence should be repaired after the
separate integration review, not by promoting the unproved DEFECT-L4 node.

Also keep the direction of implication straight: `||sigma||2<=||grad u||2/2`
alone says that the full-gradient hypothesis implies the defect hypothesis;
it cannot prove the latter is not weaker. The finite-endpoint converse here
uses the equation and continuation. Energy still controls only
`integral ||sigma||2^2 <= E0/(8 nu)`, not its fourth power.

## 4. Adversarial review requested

A reviewer should reconstruct these specific implications, rather than merely
checking compilation or accepting the stated conclusions:

1. The pressure route's exact constants, preserved cutoff quantifiers,
   uniformity up to `Tstar=H`, and use of strict rather than coefficient-one
   absorption. Verify that no endpoint theorem enters the positive suffix.
2. The mixed identity's sign, global derivative identity, harmonic ambiguity,
   cutoff products, and consistency of the `L2` and `Ls` Riesz extensions.
3. All exponents for `3/2<s<infinity`, exact Young coefficient, measurability,
   zero-safe `Q^(4/3)` multiplication, and both excluded endpoints.
4. The defect/enstrophy comparison's actual-trajectory scope and both logical
   directions. No pointwise reverse norm bound or arbitrary-data upper bound
   is a conclusion.

The appropriate graph change, after a successful audit, is an additional
conditional strict-absorption sufficiency edge and the limited review-text
repair. Do not delete ESS from the separately stated bare-CRITICAL theorem,
and do not promote NS-R3, CRITICAL, HIGH-PRESSURE, HIGH-STRAIN, or DEFECT-L4.

## 5. Prior-art and verification record

The mechanism is attributed to classical nonendpoint Serrin-type testing;
Serrin, *On the interior regularity of weak solutions of the Navier-Stokes
equations*, Arch. Rational Mech. Anal. 9 (1962), 187-195,
DOI `10.1007/BF00253344`. Bibliographic metadata was checked against the
publisher; the required inequality is proved in the supplement rather than
inferred from an unseen source. Tao's primary record `arXiv:1108.1165` was
checked; the LOCAL package remains an explicitly imported manuscript proof.
The corresponding HF25, HF28, and HF30 project sources are cited by frozen
revision. No novelty, priority, or arbitrary-data regularity claim is made.

Checks executed on the frozen supplement:

```sh
cd ../navier-paper
make continuation
python3 ../navier/research/evidence/check_dissipation_budget_continuation.py \
  --tex dissipation_budget_continuation.tex
```

The regression output is:

```text
PASS: exact exponents/constants, 288 Young samples, boundary examples, 34 unique/resolved labels and bibliography.
Scope: arithmetic and source regression only; no PDE correctness, independent mathematical audit, or Lean proof is certified.
```

The supplement builds to seven pages, with no undefined references/citations,
no LaTeX warnings, and no overfull boxes. The rendered pages were inspected.
The included Python script uses only the standard library. It checks exact
rational exponent identities and constants, 288 deterministic Young samples,
the coefficient-one and square/fourth-power boundary examples, and internal
source references. Numerical samples are not a proof of the analytic lemmas.

The full pre-existing manuscript/map were not rebuilt; no Lean build or
`research/verify.py` run is claimed. The latter requires all three complete
local repositories, which were not available. Authoritative graph/status files
are unchanged. Generated PDFs and TeX auxiliaries are not committed.

The shell could not resolve `github.com`, so no successful literal `git pull`
is claimed. The connected GitHub API is used instead: refresh the remote head,
create an additive tree from that current commit, and move main only with
`force=false`. A concurrent head advance requires rebuilding on the new parent,
never overwriting remote work. Commit transport and build checks do not supply
independent mathematical review.
