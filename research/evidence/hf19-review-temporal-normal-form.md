# Audit of HF19-A: temporal normal forms for the transport term on the quotient route

VERDICT: **REPAIR**

## REVIEWED SCOPE

Candidate `research/evidence/hf19-temporal-normal-form.md`, frozen at SHA-256
`17730f1b39509bd25a61625f8eaf6bbbe35b8c3c3bab1642a3aa4ac4c20e9197`
(593 lines), repository `../navier` at
`git rev-parse HEAD = 1014e7e3c33af4a341a5f46156a22b808170257b`.
Manuscript `../navier-paper/main.tex` at `39ccb66` (verified by
`git log --oneline -1`), section `sec:quotient`.

Everything in the note was reconstructed from its first nontrivial
implication: Lemma 0.1, Proposition 0.2, Theorem 1, Corollary 1.1,
Remarks 1.2–1.3, Lemma 2.1, Propositions 2.2–2.3, Theorem 2(i)–(iii),
Corollary 2.4(a)–(b), Lemma 3.1, Theorem 3, Section 4(a)–(c), the numerical
table of Section 5, and the frontier record of Section 6.  Every exponent,
every scaling pair, and every constant chain was recomputed independently.
Imported facts were checked against their sources, not against the note's
summary of them:

- `def:D3P3` (`eq:D3-def`, `eq:P3-def`), `prop:pressure`(i)–(iv),
  `lem:quotient-coercive` (`eq:cp-coercive`), `lem:quotient-scaling`,
  `lem:quotient-heat`, `lem:quotient-stability`, `lem:quotient-chainrule`
  (Steps 1–4), `lem:qe-heat-continuity`, `def:qe-dissipation`,
  `lem:quotient-heatsign`, `lem:quotient-transport` (Steps 4–5),
  `prop:quotient-evolution`, `lem:quotient-lowstrain` (`eq:qe-lowstrain`),
  `lem:qe-gronwall`, `hyp:highpressure`, `hyp:absorption`,
  `lem:absorption-split`, `hyp:highstrain`, `prop:quotient-conditional`,
  `rem:highstrain-scope` — all read directly in `main.tex` at `39ccb66`.
- `hf18-hodge-regularity.md` §0 (0.1)–(0.2), (E1)–(E5), (1.9), (1.11),
  (1.12), Theorem 2 with (2.1)–(2.3), Proposition 3 (F1),(F2),(F5),(F6),(F7),
  Proposition 3' (conditional on (H1), NOT used by the note), Theorem 4
  (4.1)–(4.2), Corollary 4; `hf18-review-hodge-regularity.md` R5–R7.
- `hf18-divergence-speed-link.md` §0 exponent lattice, Prop. 1.4, §3.1
  (`\nabla\Pi_L=-(I-\mathbb P)[(u^{hi}\cdot\nabla)A]`).
- `hf04-review-saturation.md` (the REPAIR-form characteristic argument that
  Theorem 2(i) imports).

No primary web source was needed: every load-bearing external statement is a
manuscript lemma or an audited note in this repository, and each was
inspected directly.

## FIRST BAD BRIDGE

Two, in reading order; the second is the substantive one.

**(B1) Lemma 0.1(a), the displayed input constant.**  The lemma concludes
"(G) holds with `A_input = a_input + |B(u_0)| + \int_0^H r` and the same
`\theta`, `M`".  Integrating (NF) gives

    \int_0^\tau K \le (1-c)\mathcal Q(\tau) + a_input + |B(u_0)|
                      + \theta\nu\int_0^\tau D_3(w) + M\int_0^\tau \mathcal Q
                      + \int_0^\tau r ,

so the stated `A_input` is achieved only if the term `(1-c)\mathcal Q(\tau)`
is absent, i.e. only if `c=1`.  For `c<1` the constant is not proved by the
displayed argument; `\mathcal Q(\tau)` is exactly the quantity the lemma is
trying to bound, so writing it into `A_input` unrepaired would be circular.
The lemma's own Gronwall step supplies the missing bound, so this is a
one-line repair (R1 below) and nothing downstream depends on the wrong
constant: the only instantiation of Lemma 0.1(a) in the note is Theorem 1,
where `c=1` and the statement is correct as written.

**(B2) Corollary 1.1(a), the boundary-term estimate.**  The proof asserts

    -[\mathcal Q - X/3]_0^\tau \le X(0)/3
    "because \mathcal Q(\tau)\le X(\tau)/3 and \mathcal Q(0)\ge0".

Write `Y := X/3 - \mathcal Q \ge 0` (this is (Q4)).  Then
`-[\mathcal Q - X/3]_0^\tau = [X/3-\mathcal Q]_0^\tau = Y(\tau)-Y(0)`.
The two cited facts give `Y(\tau)\ge0` and `Y(0)\le X(0)/3`, hence
`Y(\tau)-Y(0) \ge -X(0)/3`: they establish a **lower** bound and are used as
an **upper** bound.  The asserted inequality is false in general.
Counterexample to the step (all values admissible for a pair
`(\mathcal Q, X)` obeying (Q4) with `C_{\mathbb P}^3 \ge 3`):
`X(\tau)=90, \mathcal Q(\tau)=10, X(0)=3, \mathcal Q(0)=1` give
`-[\mathcal Q-X/3]_0^\tau = 20`, while `X(0)/3 = 1`.
The genuinely unbounded object is `Y(\tau) \le X(\tau)/3`, a quantity of the
same criticality as the conclusion.

The mirror step in Corollary 1.1(b) is **correct**: there the boundary term is
`-[X/3-\mathcal Q]_0^\tau = Y(0)-Y(\tau) \le Y(0) \le X(0)/3`, because
`Y(\tau)\ge0`.  The failure is genuinely one-sided; the note's word
"symmetric" hides an asymmetry.

Corollary 1.1(a) is repairable (R2 below), but only through the Gronwall
closure of (G), which costs the corollary the property the note advertises:
the transfer strain ⇒ pressure is not instantaneous and its constant is not
`A + X(0)/3` but `A + C_{\mathbb P}^3(\mathcal Q(0)+A)e^{MH}`.

Everything else in the note that I checked is either correct as stated or
correctly scoped; the detailed ledger is under EVIDENCE.

## REPLACEMENT ARGUMENT

### R1 (replaces Lemma 0.1(a))

**Lemma 0.1(a)'.**  Let (NF) hold in integrated form on `[0,\tau]` for every
`0<\tau<\min(H,T_*)`, with `\theta\le1`, `M\ge0`, `r\ge0` input-integrable,
and let (C) hold at `u(\tau)` for every such `\tau`, with `c\in(0,1]`,
`a_input<\infty`.  Put `A_0 := a_input + |B(u_0)| + \int_0^H r`.  Then

    c\,\mathcal Q(\tau) + (1-\theta)\nu\int_0^\tau D_3(w)\,dt
        \le \mathcal Q(0) + A_0 + M\int_0^\tau \mathcal Q\,dt ,          (R1.1)

hence, dropping the nonnegative dissipation term (`\theta\le1`,
`D_3(w)\ge0` by `lem:quotient-heatsign`) and applying `lem:qe-gronwall` to
the continuous `y=\mathcal Q\circ u` on each `[0,\tau_1]\subset[0,\min(H,T_*))`,

    \mathcal Q(\tau) \le \mathcal Q_{\max}
        := c^{-1}\bigl(\mathcal Q(0)+A_0\bigr)e^{(M/c)H}
        \qquad \text{for all } 0\le\tau<\min(H,T_*),                    (R1.2)

and (G) holds with the same `\theta`, the same `M`, and

    A_input := A_0 + (1-c)\,\mathcal Q_{\max}.                          (R1.3)

*Proof.*  Integrating (Q1), `\mathcal Q(\tau)+\nu\int_0^\tau D_3(w)
=\mathcal Q(0)+\int_0^\tau K`; integrating (NF) and inserting (C) at
`u(\tau)` gives
`\int_0^\tau K \le (1-c)\mathcal Q(\tau)+A_0+\theta\nu\int_0^\tau D_3(w)+M\int_0^\tau\mathcal Q`.
Subtracting yields (R1.1).  Gronwall gives (R1.2).  Feeding (R1.2) back into
the same bound on `\int_0^\tau K` gives (G) with (R1.3).  For `c=1`,
(R1.3) reduces to the note's constant. `\square`

Nothing else in the note changes: its only use of Lemma 0.1(a) is at `c=1`.

### R2 (replaces Corollary 1.1(a))

**Corollary 1.1(a)'.**  Fix `\nu,u_0,H` and assume (G) for `K` with
`\theta_s\le1`, `M\ge0`, `A<\infty`, for all `0<\tau<\min(H,T_*)`.  Put

    \mathcal Q_{\max} := \bigl(\mathcal Q(0)+A\bigr)e^{MH},
    A' := A + C_{\mathbb P}^3\,\mathcal Q_{\max}.

Then for every `0<\tau<\min(H,T_*)`

    \int_0^\tau P_3\,dt
      \le \nu\int_0^\tau D_3(u)\,dt-(1-\theta_s)\nu\int_0^\tau D_3(w)\,dt
          + M\int_0^\tau \tfrac{X}{3}\,dt + A'
      \le \nu\int_0^\tau D_3(u)\,dt + M\int_0^\tau \tfrac{X}{3}\,dt + A' ,

and with `prop:pressure`(ii) and `lem:qe-gronwall` this gives
`hyp:critical`:
`\sup_{0\le\tau<\min(H,T_*)}\|u(\tau)\|_3^3 \le (\|u_0\|_3^3+3A')e^{MH}`.

*Proof.*  Integrate (Q1) on `[0,\tau]`, insert (G), and drop
`(1-\theta_s)\nu\int_0^\tau D_3(w)\ge0` (`\theta_s\le1`, `D_3(w)\ge0`):
`\mathcal Q(\tau)\le\mathcal Q(0)+A+M\int_0^\tau\mathcal Q`, so
`\mathcal Q(\tau)\le\mathcal Q_{\max}` by `lem:qe-gronwall`; by (Q4),
`Y(\tau)=X(\tau)/3-\mathcal Q(\tau)\le X(\tau)/3\le C_{\mathbb P}^3\mathcal Q_{\max}`.
Now (1.1) at `s=0` reads
`\int_0^\tau P_3 = \int_0^\tau K + \bigl(Y(\tau)-Y(0)\bigr)
+\nu\int_0^\tau\bigl(D_3(u)-D_3(w)\bigr)`;
bound `\int_0^\tau K` by (G), drop `-Y(0)\le0`, bound `Y(\tau)` as above, and
use `\mathcal Q\le X/3` in the Gronwall term.  The last sentence is
`prop:pressure`(ii) plus `lem:qe-gronwall` on `X/3`. `\square`

**Remark (what the repair costs).**  In (a)' the input constant `A'` is
produced only *after* the Gronwall closure of (G).  That closure is already
`prop:quotient-conditional`, i.e. already `hyp:critical`.  Hence direction (a)
of Corollary 1.1 is a corollary of the conclusion, not an independent
instantaneous transfer.  Only direction (b) — pressure ⇒ strain — is an
unconditional instantaneous transfer through the identity (1.1), with the
exact constant `X(0)/3`.  The abstract's "the HIGH-STRAIN and HIGH-PRESSURE
gaps are equivalent at `\theta\le1`" must therefore be restated as:

- (b) `hyp:absorption` with `\theta_p\le1` ⇒ (G) for `K` with `\theta_s=1`,
  `M=0`, `A_{\rm input}=A+X(0)/3`.  Unconditional, one line from (1.1).
- (a)' (G) for `K` with `\theta_s\le1` ⇒ the *Gronwall-form* pressure bound
  above with `\theta_p=1` and constant degraded by
  `C_{\mathbb P}^3e^{MH}` — after, and only after, the Gronwall closure.

**Terminology correction, required.**  What (a)' delivers is **not**
`hyp:absorption` as the manuscript states it: `hyp:absorption` (line 3652 of
`main.tex`) requires a *fixed* `\theta\in[0,1)` and carries **no** Gronwall
term.  `\theta_p=1` plus `M\int X/3` is a strictly different, weaker statement.
The note's sentence "the pressure absorption `hyp:absorption` holds with
`\theta_p=1` and a Gronwall term" must not be read as instantiating the
manuscript hypothesis.  (Direction (b) is unaffected: it *assumes*
`hyp:absorption` with `\theta_p\le1`, which is implied by the manuscript's
`\theta_p<1`.)

### R3 (scope tightening, required, not a repair of a false claim)

**The quantifier on (C).**  (C) is written as a property of the functional
`B`, with the quantifier over `u` left implicit.  Lemma 0.1(a) and R1 use it
**only at the trajectory points** `u(\tau)`, `0<\tau<\min(H,T_*)`, with
`a_input` permitted to depend on `(\nu,u_0,H)`.  Theorem 2(ii) and Theorem 3
refute (C) under the **universal** reading (over all solenoidal Schwartz
fields, resp. over a fixed energy shell).  These are different statements, and
the note conflates them in two places:

- Theorem 2(ii): "no `f(\mathcal Q-B_h)` is coercive in `\mathcal Q`, even on
  a fixed energy shell";
- Theorem 3: "`B=\mathcal Q-\Phi_m` violates (C) for every `c`, `a_input`".

Both are correct for the universal quantifier and **unproved** for the
trajectory-local one.  The fixed-energy-shell construction in Theorem 2(ii)
narrows but does not close the gap: energy is an input, but a trajectory
issuing from one fixed `u_0` need not visit the fields `u_a`.  Every
statement of Theorems 2–3 and every route-level sentence resting on them must
carry the phrase "for the universal reading of (C)".  With that phrase the
theorems are correct as proved; without it they claim more than the
constructions give.

### R4 (Theorem 3, missing hypothesis in the abstract)

Theorem 3's hypothesis "no atom at `0`" is **necessary**, not cosmetic: for
`m=\beta\delta_0+m'` one has `\Phi_m\ge\beta\mathcal Q`, so (C) holds with
`c=\beta`.  The theorem statement carries the hypothesis; the note's abstract
("Every heat-smoothed modified energy ... is non-coercive") drops it and must
be corrected.  This matters because the atom-carrying mixtures
`\Phi=\beta\mathcal Q+(1-\beta)\mathcal Q(G_a u)` are exactly the class that
has both a rigorous derivative (Lemma 3.1) and coercivity; they fail for the
*other* reason, the one in Corollary 2.4(a): with `B=\mathcal Q-\Phi`,
`R = K-B' = \beta K + (1-\beta)K_a + \nu(1-\beta)\bigl(D_3(w)-D_3(w(G_au))\bigr)`,
so a fraction `\beta>0` of the unsmoothed `K` always survives.  Section 3
should record this one-line computation; otherwise the note leaves the reader
with a coercive, rigorously differentiable class that its three theorems do
not visibly cover.

## EVIDENCE

Independent verification, item by item.  "✓" = reconstructed and confirmed.

**Section 0.**
1. ✓ (Q1)–(Q5), (P1)–(P2) are faithful transcriptions.  `D_{\mathcal Q}(u)=D_3(w)`
   is HF18-A (2.2) under (0.1) only — every field the note evaluates it at
   (`u(t)`, `G_su`, `G_su(t)`) is solenoidal and in `H^m`, `m\ge4`, so the
   import is inside its audited scope.  Likewise (Q3) = HF18-A (4.2), whose
   proof uses only (1.11), Hölder `(3,6,2)`, Corollary 1(a) — all static
   under (0.1).
2. ✓ (Q2)'s four forms are HF18-A (F1),(F2),(F6) plus the definition; these
   hold under (0.1) alone.  The note correctly does **not** use (F3)–(F4),
   which HF18-A §3.2 quarantines behind (H1) `w\in W^{1,1}_{loc}`.  Checked
   explicitly, because using (F3)/(F4) would have been an out-of-scope import.
3. ✓ (P1)'s identification `|(\nabla u)^{\mathsf T}u|^2/|u| = |u||\nabla|u||^2`:
   `((\nabla u)^{\mathsf T}u)_j = u_i\partial_ju_i = |u|\partial_j|u|`.
4. ✓ `\nu`-rescaling of the manuscript's `G_s`: `k_{\nu s}=k_r` with `r=\nu s`,
   so `lem:quotient-heat`, `lem:qe-heat-continuity`, `lem:heat-generator`
   transfer verbatim.
5. ✓ Scaling bookkeeping against HF18-B §0's exponent lattice:
   `\mathcal Q,X\sim(a^3,\lambda^0)`, `D_3\sim(a^3,\lambda^2)`,
   `K,P_3\sim(a^4,\lambda^2)`, `E\sim(a^2,\lambda^{-1})`.
6. ✗ Lemma 0.1(a) constant — bad bridge (B1), repaired by R1.
7. ✓ Lemma 0.1(b): `B=\mathcal Q` gives `R=\nu D_3(w)`, (NF) at `\theta=1`,
   `|B|\le\mathcal Q`, and the integrated form is the tautology
   `\int K=\mathcal Q(\tau)-\mathcal Q(0)+\nu\int D_3(w)`.  Correct, and the
   right reason to insist on (C) rather than `|B|\le C\mathcal Q`.
8. ✓ **Proposition 0.2 is correct — and is a change of variables, not a
   theorem.**  Since `R` is *defined* as `K-B'` and `\mathcal Q'=K-\nu D_3(w)`
   is (Q1), `R=\Phi'+\nu D_3(w)` is an identity, and (NF) ⟺ (L) is
   substitution.  The equivalence is neither vacuous nor circular: it assumes
   nothing it concludes.  But it carries no mathematical content beyond
   notation, and should be demoted to a Remark.  Two quantifier points:
   (i) the hypothesis "`B\circ u` absolutely continuous on compact classical
   intervals" is essential and is *dropped* in the note's abstract ("for every
   functional `B` whatsoever") and in the PLAN summary — restore it;
   (ii) the equivalence is at the level of a.e. pointwise inequalities, while
   (G) is time-integrated.  Theorem 1 supplies (NF) only in the integrated
   sense (correctly flagged in (1.2)), so (NF) should be *defined* in
   integrated form; Lemma 0.1 only ever integrates, so nothing breaks.
9. ✓/⚠ The framing paragraph "global continuation gives (G) with `\theta=0`,
   i.e. `\Phi=\mathcal Q` itself satisfies (L) with `\theta=0`" silently
   promotes the integrated (G) to the pointwise (L).  It is repairable and
   the conclusion stands: under `T_*=\infty`, `K` is continuous on `[0,H]`
   (`prop:quotient-evolution`), so (L) holds pointwise with `\Phi=\mathcal Q`,
   `\theta=0`, `M=0`, `r=K^+\in L^\infty(0,H)` — the same device as
   `rem:highstrain-scope`'s converse (`L=0`, `A_{\rm input}=\int_0^H|K_0|`).
   The meta-conclusion — no obstruction theorem for the general class is
   provable without deciding NS-R3 — is sound and is the most valuable
   sentence in the note.

**Section 1.**
10. ✓ **Theorem 1, identity (1.1), is correct.**  Integrate (Q1):
    `[\mathcal Q]_s^t+\nu\int D_3(w)=\int K`; subtract `prop:pressure`(ii)
    `[X/3]_s^t+\nu\int D_3(u)=\int P_3`.  Finiteness of every term checked
    against `prop:pressure`(i) (`P_3, D_3(u)` bounded measurable, `X\in C`)
    and `prop:quotient-evolution` (`K, D_3(w)` continuous).
11. ✓ (1.2): `R=K-B'=\nu D_3(w)+X'/3=P_3+\nu(D_3(w)-D_3(u))`;
    `B=\mathcal Q-X/3\le0` by (Q4) and `\ge-(C_{\mathbb P}^3-1)\mathcal Q`
    from `X/3\le C_{\mathbb P}^3\mathcal Q`; (C) with `c=1`, `a_{\rm input}=0`.
    `X` is Lipschitz on compacts by `prop:pressure`(ii) with bounded
    integrands, so `B\circ u` is absolutely continuous as (NF) requires. ✓
12. ✗ Corollary 1.1(a) — bad bridge (B2), repaired by R2.
13. ✓ Corollary 1.1(b) and (c).  (b)'s boundary bound is correct as shown
    above; (c) is read off the displayed middle terms correctly.
14. ✓ Remark 1.2: with `\theta=1` the budget `\nu D_3(w)` in `R` is exactly
    consumed, leaving `P_3-\nu D_3(u)`, whose low-output part is `prop:lowpressure`
    and whose remainder is `\int(P_3)_{>J}`, scaling `(a^4,\lambda^2)` —
    `hyp:highpressure` verbatim.  The gap is not moved; the note says so.
15. ✓ Remark 1.3 is an accurate statement of what is and is not known about
    `\mathrm{sgn}(D_3(u)-D_3(w))`; the reduction to a static question on
    `\mathcal M` with the test class of HF18-B Prop. 1.4 is legitimate.

**Section 2.**
16. ✓ Lemma 2.1(a)–(d).  (b): `s\mapsto G_su` is `C^1` into `H^{m-2}\subset L^3`
    (`m\ge4`), so Step 2 of `lem:quotient-chainrule` — which uses only
    `prop:quotient-derivative` with its quantified remainder and `L^3`
    differentiability of the curve — applies; the note's restriction to
    `(0,\infty)` is conservative and harmless.  Limit:
    `\mathcal Q(G_su)\le\frac13\|G_su\|_3^3\le C(\nu s)^{-3/4}\|u\|_2^3`
    from `\|k_t\|_{6/5}\sim t^{-1/4}` (Young, `1/3=1/2+5/6-1`). ✓
    (d) recomputed: `A(av)=a|a|A(v)`, `(av)\times\mathrm{curl}(av)=a^2 v\times\mathrm{curl}\,v`,
    so `K(av)=a^3|a|K(v)`; under `\mathcal D_\lambda`, `A\mapsto\lambda^2A(\lambda\cdot)`,
    `v\times\mathrm{curl}\,v\mapsto\lambda^3(\cdot)(\lambda\cdot)`, `dx\mapsto\lambda^{-3}dy`,
    giving `\lambda^2`. ✓  `w(\alpha u)=\alpha w(u)` for all real `\alpha` is
    `lem:quotient-scaling`, so oddness is legitimate.
17. ✓ **Proposition 2.2 (2.2) is correct.**
    `\int_0^\infty|K(G_su)|ds \le (C_*/\nu)\int_0^\infty \mathcal Q_s^{1/3}(-d\mathcal Q_s/ds)ds
    = (C_*/\nu)\,[-\tfrac34\mathcal Q_s^{4/3}]_0^\infty = \tfrac{3C_*}{4\nu}\mathcal Q(u)^{4/3}`,
    the antiderivative argument needing only `\mathcal Q_s\in C^1` and
    `\mathcal Q_s\to0`, not monotonicity.  Dilation invariance recomputed via
    `G_s\mathcal D_\lambda=\mathcal D_\lambda G_{\lambda^2s}` and `s\mapsto\lambda^2s`. ✓
    `\nu`-dependence checked: `B_h=\nu^{-1}\int_0^\infty K(e^{\sigma\Delta}u)d\sigma`,
    consistent with `B_h\sim(a^4/\nu,\lambda^0)` against `\mathcal Q\sim(a^3,\lambda^0)`.
    The quartic-vs-cubic mismatch is real and is the engine of Theorem 2(ii).
18. ✓ The (C)-from-(2.2) reading: `B_h\le\frac{3C_*}{4\nu}\mathcal Q^{1/3}\cdot\mathcal Q`,
    so (2.2) supplies (C) only under `\frac{3C_*}{4\nu}\mathcal Q^{1/3}\le1-c`,
    i.e. `\|u\|_3\lesssim\nu` — HF18-A Corollary 4's threshold.  The note is
    careful to say this is what *(2.2)* supplies, not that (C) fails; correct,
    since `B_h\le0` would give (C) with `c=1` for free.  (Section 5 reports
    `B_h>0` on all four sampled fields.)
19. ✓ Proposition 2.3: `B_h(G_tu)=-\int_t^\infty K(G_su)ds` by `G_sG_t=G_{s+t}`,
    and FTC with a continuous integrand gives `\frac{d}{dt}B_h(G_tu)=K(G_tu)`.
20. ✓ The note's own falsifier is correctly raised and not evaded: the
    transport-direction chain rule for `B_h` requires differentiability of
    `u\mapsto w(u)`, and `lem:quotient-stability` gives only the Hölder-`1/2`
    modulus `\|w'-w\|_3\le2(\|w\|_3+\|h\|_3)^{1/2}\|h\|_3^{1/2}`.  (2.4) is
    therefore **formal**, and the note labels it so.  Verified that no
    rigorous conclusion of the note depends on (2.4): Theorem 2's content is
    the coercivity failure of `\mathcal Q-B_h`, which is proved by static
    scaling and needs no chain rule at all.
21. ✓ Theorem 2(i): the imported argument matches `hf04-review-saturation.md`
    verbatim in form (fibres `\{\mathcal Q-B=y,\ \mathcal Q>0\}` connected,
    `F` constant along each, `f(y):=F(Q_0,Q_0-y)` independent of `Q_0`,
    `f\in C^1` locally).  The premise is stated coefficientwise on the ambient
    `\Omega`, which is exactly the scope the HF04 audit demanded — the note
    does **not** repeat the refuted "cancellation along realized states"
    version.
22. ✓ Theorem 2(ii), fully recomputed.  Path `\psi_\sigma=\cos(\pi\sigma)\phi+\sin(\pi\sigma)\chi`
    never vanishes (linear independence, `(\cos,\sin)\ne(0,0)`), is continuous
    into every `H^k`, runs `\phi\to-\phi`.  Majorant:
    `|K(G_s\psi_\sigma)|\le 2C_*\|\psi_\sigma\|_3^2\|\nabla G_s\psi_\sigma\|_3^2
    \le C\min(1,(\nu s)^{-3/2})`, integrable on `(0,\infty)`, from (Q3),
    HF18-A (2.3) (`D_{\mathcal Q}\le2\|w\|_3\|\nabla u\|_3^2` with
    `\|w\|_3\le\|u\|_3` by admissibility of `q=0`), `\|\nabla G_sv\|_3\le\|\nabla v\|_3`
    and `\|\nabla G_sv\|_3\le C(\nu s)^{-3/4}\|v\|_2`.  IVT on
    `h_a(\sigma)=aB_h(\psi_\sigma)-\mathcal Q(\psi_\sigma)` with `h_a(0)>0`
    for `a>\mathcal Q(\phi)/B_h(\phi)` and `h_a(1)<0`.  Then
    `\mathcal Q(a\psi_{\sigma_a})-B_h(a\psi_{\sigma_a})=a^3(\mathcal Q-aB_h)(\psi_{\sigma_a})=0`
    and `\mathcal Q\ge a^3m_0\to\infty`.  Energy shell: with `N_a=a^2\|\psi_{\sigma_a}\|_2^2/E`
    and `u_a=aN_a\psi_{\sigma_a}(N_a\cdot)`, `\|u_a\|_2^2=a^2N_a^{-1}\|\psi\|_2^2=E`
    (recomputed: `\|\mathcal D_\lambda v\|_2^2=\lambda^{-1}\|v\|_2^2`), and both
    relations survive by dilation invariance of `\mathcal Q` and `B_h`. ✓
    **Robustness note (in the note's favour):** (ii) does not actually need
    (i)'s global characterisation.  The attainable set is contained in
    `\{|B|\le\frac{3C_*}{4\nu}\mathcal Q^{4/3}\}\subsetneq\Omega`, on which a
    fibre `\{\mathcal Q-B=y\}` with `y>0` need not be connected; but the fibre
    used by (ii) is `y=0`, whose trace on that set is `\{\mathcal Q\ge c^{-3}\}`,
    connected.  So (ii) survives even if (i) is restricted to attainable pairs.
23. ✓ Theorem 2(iii): the equivalence `B_h\equiv0 \iff K\equiv0` on Schwartz
    fields (Prop. 2.3 applied to the Schwartz orbit `G_t\phi`, plus continuity
    at `t=0`), the density transfer to `H^m`, and the dichotomy "if `K\equiv0`
    then (G) holds with `\theta=M=A=0`" are all correct.  The dichotomy is the
    right way to state the theorem, since `K\not\equiv0` is supported only by
    the periodic numerics of Section 5 and is not proved anywhere.  Checked
    that `(G)` for `K` with an `M`-term does drive `prop:quotient-conditional`:
    `\int K_L=\int K-\int K_{\rm low}` and `|K_{\rm low}|\le M_L\mathcal Q`
    (`eq:qe-lowstrain`), so the Gronwall of `prop:quotient-conditional` runs
    unchanged with `M+M_L`.
24. ✓ Corollary 2.4(a), recomputed.  `g(x)=(1+x^{1/3}/\nu)^{-1}`,
    `|F_\delta-\mathcal Q|=\delta g(\mathcal Q)|B_h|\le\frac{3C_*}{4}\delta\mathcal Q`;
    `K`-coefficient `1-\delta g(\mathcal Q)-\delta g'(\mathcal Q)B_h`;
    `|g'(x)|=\frac{\nu}{3}x^{-2/3}(\nu+x^{1/3})^{-2}`, so
    `|g'(\mathcal Q)B_h|\le\frac{C_*}{4}\frac{\mathcal Q^{2/3}}{(\nu+\mathcal Q^{1/3})^2}\le\frac{C_*}{4}`;
    coefficient `\ge1-\delta(1+C_*/4)\ge\frac12` for `\delta\le\frac{1}{2(1+C_*/4)}`.
    (The note's inline display of the `g'B_h` bound is typographically garbled
    but its value `C_*/4` is right.)  Conclusion — saturation buys coercivity
    at the price of leaving `\ge\frac12 K` uncancelled, bounded only by (Q3) —
    is correct and is HF04 (15) transferred.
25. ✓ Corollary 2.4(b) bounds, recomputed.
    `|K(G_su)|\le C_*\mathcal Q_s^{1/3}\cdot2\|G_su\|_3\|\nabla G_su\|_3^2
    \le C\|G_su\|_3^2\|\nabla G_su\|_3^2\le C(\nu s)^{-1/2}(\nu s)^{-3/2}\|u\|_2^4
    = C(\nu s)^{-2}\|u\|_2^4`; `|B_a|\le C\|u\|_2^4/(\nu^2a)=C2^{2L}\|u_0\|_2^4/\nu`
    at `a=\nu^{-1}2^{-2L}` — matches (2.5).  Energy monotonicity from
    `prop:energy`.  (C) with `c=1` follows.  The formal normal form is right:
    `DB_a[\nu\Delta u]=\frac{d}{dt}\big|_{0}B_a(G_tu)=K(G_au)`, so
    `K(u)=\frac{d}{dt}B_a(u)+[K(u)-K(G_au)]+\rho_a`.
    `\rho` scaling recomputed: `DB_h\sim(a^3/\nu)`, `\mathbb P(u\cdot\nabla)u\sim(a^2,\lambda^2\text{-covariant})`,
    `\rho\sim(a^5/\nu,\lambda^2)` against `\nu D_3\sim(\nu a^3,\lambda^2)`,
    ratio `(a/\nu)^2\sim(\mathcal Q^{1/3}/\nu)^2`. ✓ Two powers supercritical.
26. ⚠ Corollary 2.4(b)'s hedge about `K(G_au)` is unnecessary — see
    UNNECESSARY DEPENDENCIES 1.

**Section 3.**
27. ✓ Lemma 3.1.  `G_su\in C^1([0,T];H^2)\subset C^1([0,T];L^3)`; chain-rule
    Step 2 gives `\frac{d}{dt}\mathcal Q(G_su)=\langle A(G_su),G_su_t\rangle`;
    `G_s\nabla p\in\mathcal G_3` by `lem:quotient-pressure` + `lem:quotient-heat`(c)
    and is annihilated by `lem:quotient-minimizer`(c) **at the field `G_su`**
    (checked: the Euler–Lagrange condition is applied at the right base point);
    `\langle A(G_su),\nu\Delta G_su\rangle=-\nu D_3(w(G_su))` by HF18-A Thm 2
    at `G_su`.  Bounds are (Q5) and the `L^2\to L^3` heat bound. ✓
28. ✓ Theorem 3, recomputed.  `\mathcal Q(G_su_{\alpha,\lambda})=\alpha^3\mathcal Q(G_{\lambda^2s}u_0)
    \le\alpha^3C(\nu\lambda^2s)^{-3/4}\|u_0\|_2^3\to0` for each `s>0`,
    dominated by the `m`-integrable constant `\alpha^3\mathcal Q(u_0)`; then
    choose `\alpha` with `c\alpha^3\mathcal Q(u_0)>2\sup_{[0,1]}a`, then
    `\lambda` with `\|u_{\alpha,\lambda}\|_2^2\le1` and
    `\Phi_m<\frac12c\alpha^3\mathcal Q(u_0)`, giving
    `\Phi_m<\frac12c\mathcal Q\le c\mathcal Q-a(\|u\|_2^2)`. ✓
    The mechanism (a heat-smoothed critical functional sees only
    energy-controlled scales) is correctly identified.
29. ⚠ Abstract drops the "no atom at `0`" hypothesis — see R4.

**Section 4.**
30. ✓ 4(b) is correct: `lem:quotient-transport` Step 4 gives
    `\mathcal Q(u_s)=\mathcal Q(u)-s\langle A,(u\cdot\nabla)u\rangle+o(|s|)
    =\mathcal Q(u)+sK+o(|s|)` — `K` *is* the Lagrangian derivative of
    `\mathcal Q` along its own velocity.  The obstruction identified (the
    pulled-back pressure gradient is no longer annihilated after composition
    with `\Phi^u_{-s}`) is the right one.
31. ⚠ 4(a)'s envelope transfer ("the proof of `prop:quotient-derivative`
    transfers") is asserted, not carried out, for `\Psi\ne F`.  Nothing in the
    note depends on it: by Proposition 0.2 every such `B` is subject to the
    same Lyapunov reformulation regardless.  Non-blocking, but it should be
    labelled a sketch.
32. ⚠ 4's framing sentence "has a justified time derivative ... only through
    one of two mechanisms" and the closing "Consequently the classes (a)–(c)
    contain no candidate beyond Sections 1–3" are exhaustiveness assertions
    with no proof.  The CLAIM AND SCOPE block already demotes Section 4 to "a
    classification of which functionals admit a justified derivative, not a
    theorem about all functionals"; the body text must be brought into line
    with that demotion.  4(c) is a statement about the current state of
    knowledge (`t\mapsto w(u(t))` known only `1/2`-Hölder into `L^3`;
    `V` only bounded in `H^1` by HF18-A (1.9)), which is accurate.

**Section 5 (numerics).**
33. ✓ The table is internally consistent: I recomputed every derived column.
    `K/(\mathcal Q^{1/3}D_3)`: `-1.098/(4.594\cdot789.0)=-3.03\times10^{-4}`;
    `-0.0616/(4.653\cdot829.5)=-1.60\times10^{-5}`;
    `-1.338/(4.619\cdot765.9)=-3.78\times10^{-4}`;
    `-0.1490/(4.548\cdot791.9)=-4.14\times10^{-5}`.
    `B_h/\mathcal Q^{4/3}`: `0.159/445.5=3.57\times10^{-4}`;
    `0.0667/468.8=1.42\times10^{-4}`; `0.227/455.4=4.98\times10^{-4}`;
    `0.0392/427.9=9.16\times10^{-5}`.  All match the printed values.
    `\mathcal Q\le X/3` holds in all four rows, as (Q4) requires.
    `K<0\Rightarrow B_h=-\int K>0` is consistent.
34. ✓ The `48^3` cross-reference is accurate: `hf18-review-hodge-regularity.md`
    R6 reports `T=-0.04216589`, `F1=-0.04216580`, ..., i.e. `K=-0.0422` with
    `\|q\|_3/\|w\|_3=0.167`.  Independent support for `K\not\equiv0`.
35. ⚠ Reproducibility defect: `hf19_probe.py` is declared "session scratchpad,
    ephemeral; not part of the record" and does not exist in the repository
    (`find . -name 'hf19*'` returns only the four notes).  The numbers that
    support the hypothesis of Theorem 2(ii)–(iii) are therefore not
    reproducible from this repository.  The HF18 audit's independent `48^3`
    computation is the only reproducible support, and it is itself recorded
    only as printed output.
36. ⚠ Reading 3's "the family of Theorem 2(ii) can be started at `\phi=u`
    directly" transfers a `2\pi`-periodic field to the `\mathbb R^3` Schwartz
    hypothesis of Theorem 2(ii).  That transfer is not made.  Since the note
    declares the periodic problem a proxy for the variational problem only,
    this sentence should say "supports", not "can be started at".

**Refutation attempts made (none succeeded against the surviving items).**
- Tried to break (1.1) by a sign convention mismatch between
  `prop:pressure`(ii) and (Q1): checked `eq:P3-def` and `def:qe-dissipation`
  directly; signs agree.
- Tried to break Prop. 2.2 by an `s\downarrow0` or `s\to\infty` endpoint
  failure and by non-strict monotonicity of `\mathcal Q_s`: the antiderivative
  form of the substitution needs neither.
- Tried to break Theorem 2(ii) with a family on which `B_h` changes sign
  discontinuously, or with a vanishing `\psi_\sigma`: excluded by linear
  independence and by the dominated-convergence continuity of `B_h` along the
  path, both of which I re-derived.
- Tried to break Theorem 2(ii) by restricting `F` to attainable `(\mathcal Q,B_h)`
  pairs (where `\Omega`'s fibres can disconnect): the `y=0` fibre stays
  connected, so the obstruction survives (item 22).
- Tried to break Theorem 3 with an atom at `0`: this *does* break it, which is
  why the hypothesis is necessary (R4) — and the resulting class fails for a
  different, computable reason, which the note should record.
- Tried to break Prop. 0.2 by exhibiting a `B` for which `R` is not
  well-defined or the equivalence reverses: none exists; the statement is an
  identity, with the AC hypothesis doing the only work.
- Tried to find hidden circularity (use of the norm to be controlled):
  found exactly one instance, `Y(\tau)\le X(\tau)/3` in Corollary 1.1(a) —
  bad bridge (B2).  No other claim in the note uses `\|u\|_3`, `\mathcal Q`,
  or `X` at the endpoint to bound itself.
- Tried to find an instantaneous fact promoted to a time-integrated one:
  found one framing-level instance (item 9, the converse direction of the
  Prop. 0.2 consequence), repairable; and the reverse promotion in (1.2),
  which the note flags itself.

## CONDITIONAL SUFFIX THAT SURVIVES

With R1–R4 applied, the following stand:

1. **Lemma 0.1(b)** unconditionally: `|B|\le C\mathcal Q` is not a usable
   boundary condition; (C) is the right one.
2. **Proposition 0.2**, restated as a Remark with its absolute-continuity
   hypothesis restored and (NF) defined in integrated form.  Its real payload
   — that no obstruction theorem for the general class of correctors can be
   proved without deciding NS-R3 — survives, with item 9's repair.
3. **Theorem 1, identity (1.1)**, unconditionally on every compact classical
   interval, together with (1.2) and its bounds
   `-(C_{\mathbb P}^3-1)\mathcal Q\le B\le0`, `(C)` with `c=1`.
4. **Corollary 1.1(b)** unconditionally, with the exact constant `X(0)/3`; and
   **Corollary 1.1(a)'** (R2) with the degraded constant
   `A+C_{\mathbb P}^3(\mathcal Q(0)+A)e^{MH}`, understood as a post-Gronwall
   consequence rather than an instantaneous transfer, and understood as
   *not* delivering `hyp:absorption` in the manuscript's sense.
5. **Corollary 1.1(c)** and **Remark 1.3**: the strict transfer `\theta<1`
   needs a comparison between `D_3(u)` and `D_3(w)` in one direction or the
   other, and neither is proved.  The reduction to a static question on
   `\mathcal M` is well posed.
6. **Lemma 2.1, Proposition 2.2 (2.2), Proposition 2.3 (2.3)** for every
   solenoidal `u\in H^m(\mathbb R^3)`, `m\ge4`, `\nu>0` — all inside HF18-A's
   audited scope (0.1).
7. **Theorem 2(i)** on `\Omega` under the coefficientwise premise as defined
   in (2.4); **Theorem 2(ii)** conditionally on `B_h\not\equiv0` on solenoidal
   Schwartz fields, and **only for the universal reading of (C)** (R3);
   **Theorem 2(iii)**, the dichotomy, unconditionally.
8. **Corollary 2.4(a)** as an exact algebraic computation; **Corollary 2.4(b)**
   for the bounds (2.5) and (C) with `c=1`, formal for the chain rule, with
   the hedge of item 26 removed.
9. **Lemma 3.1** unconditionally; **Theorem 3** unconditionally for atomless
   `m`, and **only for the universal reading of (C)** (R3).
10. **Section 4(b)**: `K` is the Lagrangian derivative of `\mathcal Q` along
    its own velocity, and the pressure re-enters after composition with the
    flow.
11. **The first gap is unchanged.**  Confirmed: nothing in the note closes,
    weakens, or reformulates
    `\int_0^\tau K\le\theta\nu\int_0^\tau D_3(w)+M\int_0^\tau\mathcal Q+A_{\rm input}`
    at its quantifiers.

What does **not** survive as stated:

- The route-level conclusion "temporal normal forms are exhausted on the
  quotient route as they were on the pressure route".  This is an **informal
  induction from three computed failures**, not a theorem about a specified
  class, and it is in direct tension with the note's own Proposition 0.2 and
  its own NON-CLAIMS line ("no obstruction for the general class of
  functionals (Prop. 0.2 shows none is provable without deciding NS-R3)").
  What is proved is: *no candidate survived in the three classes computed —
  `B=\mathcal Q-X/3`; `F(\mathcal Q,B_h)` with coefficientwise cancellation on
  `\Omega`; `\Phi_m` with atomless `m` — under the universal reading of (C).*
  That is the sentence that may be recorded.  "Exhausted" may not.
- The abstract's "for every functional `B` whatsoever" (drop of the
  absolute-continuity hypothesis).
- The abstract's unqualified "Every heat-smoothed modified energy ... is
  non-coercive" (drop of the no-atom hypothesis).
- Corollary 1.1(a)'s identification of its conclusion with `hyp:absorption`.

## UNNECESSARY DEPENDENCIES

1. **Corollary 2.4(b) does not need heat monotonicity of `D_3(w)`, and neither
   does SURVIVING CONDITIONAL SUFFIX (iii).**  The note writes that
   `K(G_au)` "is absorbable into `\theta\nu D_3(w)` *if* the (open) heat
   monotonicity `D_3(w(G_au))\le CD_3(w(u))` held".  But (2.5) already gives
   `|K(G_au)|\le C(\nu a)^{-2}\|u_0\|_2^4` pointwise in `t`, hence
   `\int_0^\tau|K(G_au)|dt\le CH(\nu a)^{-2}\|u_0\|_2^4`, an input constant,
   for every input-selected `a>0`.  The heat defect's subtracted term is
   therefore unconditionally input-controlled and conditional-suffix item
   (iii) is redundant.  The conclusion of 2.4(b) — that only the unsmoothed
   `K(u)` remains — is unaffected and in fact cleaner.
2. **Theorem 2(i) is not needed for Theorem 2(ii)** (item 22).  Only
   constancy of `F` along the single fibre `\{\mathcal Q-B=0\}` is used.
   Stating (ii) that way makes it independent of whether the coefficientwise
   premise is imposed on all of `\Omega` or only on the attainable set.
3. **Lemma 2.1(b)'s restriction of `C^1` to `(0,\infty)`** is unnecessary
   (`s\mapsto G_su` is `C^1` into `H^{m-2}\subset L^3` on `[0,\infty)` for
   `m\ge4`), but nothing depends on it.
4. **HF18-B Prop. 1.4** is cited only in Remark 1.3 and the next-action list,
   as a source of a test class; it is not load-bearing for any claim.
5. Section 5's reading 2 (`K\ne0` robustly) is used only to motivate the
   hypothesis of Theorem 2(ii); Theorem 2(iii) makes the whole section
   dispensable for the logic, since the alternative to `K\not\equiv0` is
   NS-R3 itself.  This is a virtue of the note's design and should be kept.

## NON-CLAIMS

Confirmed as correctly disclaimed by the note, and re-asserted here:

- No sign of `K`, of `P_3`, or of `D_3(u)-D_3(w)` in general.
- No differentiability of `u\mapsto w(u)`; no rigorous transport-direction
  chain rule for `B_h`; (2.4) is formal throughout.
- No `hyp:highstrain`, `hyp:highpressure`, `hyp:critical`, continuation, or
  regularity result.  The first gap is unchanged at its quantifiers.
- No novelty for the heat-inverse device (HF01/HF04) or the characteristic
  argument (HF04 review).
- No statement about which minimizers `w` occur along trajectories.

Added by this audit:

- **Proposition 0.2 is not a theorem about normal forms.**  It is a change of
  variables `\Phi=\mathcal Q-B`, with `R:=K-B'` by definition.  It must not be
  reported as a positive by-product of the same weight as Theorem 1.
- **Theorems 2 and 3 do not exclude a corrector satisfying (C) only along the
  trajectories of a given datum.**  They exclude universal coercivity over
  solenoidal Schwartz fields (Theorem 3) and over a fixed energy shell
  (Theorem 2(ii)).  Since (C) is used in Lemma 0.1(a) only at `u(\tau)`, the
  obstruction is strictly weaker than the note's route-level reading of it.
- **Theorem 1 is a subtraction of two audited balances.**  It is correct and
  worth recording, but its proof is one line and it establishes no new
  estimate; its value is the exact location of the pressure/strain difference,
  not a new bound.
- **The numerics of Section 5 are not reproducible from this repository**
  (item 35).
- Nothing in this note is a Millennium result, and nothing in it changes the
  claim graph.

## REOPENING CONDITION

This verdict should be reopened if any of the following changes:

1. **A counterexample to R2 or a better constant.**  If the boundary term
   `Y(\tau)=X(\tau)/3-\mathcal Q(\tau)` in Corollary 1.1(a) can be bounded by
   input data *without* first closing (G) by Gronwall, then direction (a)
   becomes the instantaneous transfer the note claims and the "two gaps are
   one gap at `\theta\le1`" reading is restored at full strength.  I could not
   find such a bound, and (Q4) alone cannot give one, since `Y` and `X/3` have
   the same criticality `(a^3,\lambda^0)`.
2. **The quantifier on (C).**  If the programme decides that (C) is to be read
   trajectory-locally (over `\{u(\tau):0<\tau<\min(H,T_*)\}` for each
   `(\nu,u_0,H)`, `a_{\rm input}` datum-dependent), then Theorems 2(ii) and 3
   exclude nothing and the heat-inverse and heat-smoothed classes must be
   re-examined from scratch.  If (C) is fixed universally, the theorems stand
   as proved.  This choice is not made anywhere in the note or in `PLAN.md`
   and should be made explicitly.
3. **`K\equiv0` on solenoidal `H^m` fields.**  If ever proved, Theorem 2(iii)
   gives (G) with `\theta=M=A=0` and hence NS-R3 through
   `prop:quotient-conditional`; the whole note is then superseded.  If instead
   `B_h(\phi)\ne0` is proved on `\mathbb R^3` for one solenoidal Schwartz
   `\phi` (the HF20 candidate's swirl construction is the natural source, once
   audited), Theorem 2(ii) becomes unconditional and Section 5's numerics stop
   being load-bearing.
4. **Differentiability of `u\mapsto w(u)`.**  An `L^3` implicit-function
   theorem for HF18-A (1.1) would make (2.4) rigorous.  Theorem 2 shows this
   would not save `F(\mathcal Q,B_h)`, but it would open Section 4(c), which
   this audit has not examined for content beyond the differentiability
   obstruction.
5. **A measure with an atom at `0`.**  The mixture class
   `\Phi=\beta\mathcal Q+(1-\beta)\mathcal Q(G_au)` is coercive and rigorously
   differentiable; R4 shows it fails for the Corollary 2.4(a) reason, but that
   computation is not in the note and should be added before Section 3 is
   cited as covering "heat-smoothed" correctors.
6. **The Section 5 script.**  If `hf19_probe.py` is restored to the repository
   and its four runs reproduce, item 35 is discharged.

---

VERDICT: **REPAIR**.  Theorem 1's identity, Lemma 2.1, Propositions 2.2–2.3,
Theorem 2(i)–(iii), Corollary 2.4, Lemma 3.1 and Theorem 3 are correct within
the scopes stated above; Lemma 0.1(a) and Corollary 1.1(a) each require the
replacement given here; Proposition 0.2 must be demoted from proposition to
change of variables; the route-level "exhaustion" conclusion must be demoted
to "no candidate survived in the three computed classes, for the universal
reading of (C)".  The first gap is unchanged and NS-R3 remains OPEN.
