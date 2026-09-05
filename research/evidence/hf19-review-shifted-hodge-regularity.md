# HF19 review: audit of `hf19-shifted-hodge-regularity.md`

MODE: REVIEW (proof-audit discipline), 2026-09-05. Independent audit of the
wave-HF19 lane "shifted-hodge-regularity" of the Track B frontier packet.

## 0. Freeze

| Item | Value |
| --- | --- |
| Audit target | `research/evidence/hf19-shifted-hodge-regularity.md` |
| SHA-256 of target | **undefined — the file does not exist** |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `5aefa82b99ac194c9f979ec96834042ae5a201d3` |
| Working tree at audit time | clean except three untracked HF19 lane notes (below) |
| Author summary supplied to this audit | `null` |

The freeze required by the packet cannot be completed as specified: there is no
byte string to hash. The commit hash is recorded above and is the one against
which the absence is certified. Note that the commit named in this session's
initial repository snapshot (`523d592`) is an ancestor state; the repository has
since advanced to `5aefa82`, and the target is absent at both.

## 1. Certification that the target is absent

The following searches were run at `5aefa82` and all returned empty for a
shifted-Hodge-regularity candidate:

1. `ls research/evidence/ | grep -i hf19` → exactly three files:
   `hf19-difference-functional.md`, `hf19-temporal-normal-form.md`,
   `hf19-second-order-falsifier.md`.
2. `find /home/ert/proj/navier -iname '*hf19*' -not -path '*/.git/*'` → the same
   three files.
3. `find /home/ert -maxdepth 6 -iname '*shifted*hodge*'` → empty.
4. `git log --oneline --all -- 'research/evidence/*hf19*'` → empty (no HF19 file
   has ever been committed on any ref).
5. `git ls-files | grep -i hf19` → empty.
6. `git branch -a` → `main` and `origin/main` only; `git stash list` → empty;
   `git worktree list` → one worktree.
7. `git status --porcelain --untracked-files=all` → the three files above and
   nothing else.
8. Session scratchpad tree searched for `*hodge*` → empty.

**The object under audit does not exist.** No candidate text, no draft, no
deleted-and-recoverable blob.

## 2. Disambiguation: is an existing file the target under another name?

Checked, because an audit must not declare a target missing when it has merely
been renamed. It has not been. The three HF19 notes are distinct lanes, each
self-labelled, and none contains a shifted-Hodge-regularity argument:

| File | Self-label | Subject | Bears on (H1)? |
| --- | --- | --- | --- |
| `hf19-difference-functional.md` | HF19-D, DISCOVER | \(\Delta=X/3-\mathcal Q\), its exact evolution, sign structure of \(D_3(u)-D_3(w)\) | No. Line 440 explicitly works "without (H1)-type regularity of the minimiser"; line 593 records "(H1) remains a" non-claim. |
| `hf19-temporal-normal-form.md` | HF19-A, DISCOVER | temporal normal forms \(K=\frac{d}{dt}B+R\); equivalence to a coercive critical Lyapunov functional | No. No occurrence of (H1), `W^{1,1}`, Sibner or Otway. |
| `hf19-second-order-falsifier.md` | HF19-B, FALSIFY | second-order behaviour of \(K\) on \(\mathcal M=\{{\rm div}(|u|u)=0\}\) | No. Uses a *linearised* nonlinear-Hodge problem at a point of \(\mathcal M\) (where \(q=0\)); this is a different object from regularity of the nonlinear minimizer, and the note claims no \(w\)-regularity. |

Section headers of all three were enumerated; none is about regularity of \(w\),
\(q\) or \(\phi\). `PLAN.md` (`active_task: HF19-track-b-running`, line 116) names no
HF19 lanes at all, so the plan file cannot adjudicate the intended name either.
Conclusion: the lane was commissioned and its output was never written to disk.

## 3. What the lane was to establish (audit-readiness record)

This section states obligations, not results. Nothing here is claimed as proved.

The lane name is fixed by the parent record. `hf18-review-hodge-regularity.md`
(VERDICT PASS) closes with REOPENING CONDITION (3)(b): hypothesis **(H1)**
should be attacked through the nonlinear Hodge literature for the *shifted*
system. The precise object is `hf18-hodge-regularity.md` §1.3 (1.5) and §3.2:

> **(1.5)** \(\operatorname{div}(|w|w)=0\), \(\operatorname{curl}w=\operatorname{curl}u\)
> (smooth, nonzero), for \(w=u+\nabla\phi\), \(\nabla\phi\in L^3(\mathbb R^3)\).
>
> **(H1)** \(w\in W^{1,1}_{\rm loc}(\mathbb R^3)\), equivalently
> \(q\in W^{1,1}_{\rm loc}\), equivalently \(\phi\in W^{2,1}_{\rm loc}\).

**Already proved upstream, hence not re-sellable by any candidate** (HF18-A,
audited PASS, at every fixed time of a classical \(H^m\) solution, \(m\ge4\),
divergence-free on \(\mathbb R^3\), no smallness, no decay beyond \(u\in H^m\)):
\(V=|w|^{1/2}w\in H^1(\mathbb R^3)\); \(A=|w|w\in W^{1,3/2}(\mathbb R^3)\) with
\(\operatorname{div}A=0\) a.e.; \(w\in L^3\cap L^9\cap B^{2/3}_{3,\infty}\); and on
\(\{V\ne0\}\) the *approximate* gradient
\(\nabla w=D\Psi(V)\nabla V\) with \(|\nabla w|\le|w|^{-1/2}|\nabla V|\).

**The exact analytic obstacle**, restated from HF18-A §1.6(e). On a compact
\(E\subset\mathbb R^3\), Cauchy–Schwarz gives only
\[
 \int_E|\nabla w|\ \le\ \int_E|w|^{-1/2}|\nabla V|
 \ \le\ \|\nabla V\|_{L^2}\Big(\int_E|w|^{-1}\Big)^{1/2},
\]
and \(|w|^{-1}\) need not be locally integrable; the degeneracy set \(\{w=0\}\) is
exactly where the shifted ellipticity (HF18-A (1.3)) vanishes. A candidate must
either bound \(\int_E|\nabla w|\) without passing through \(\int_E|w|^{-1}\), or
control \(|\{|w|<\varepsilon\}\cap E|\) quantitatively. A proof on \(\{|w|>\varepsilon\}\)
followed by \(\varepsilon\to0\) is not a proof: it needs a bound on
\(\int_{E\cap\{|w|<\varepsilon\}}|\nabla w|\) uniform in \(\varepsilon\), which is the
whole statement.

**Pre-registered checks** (the audit these would have received, recorded so the
lane can be re-run against a fixed standard):

- **C1 Circularity in the divergence identity.** HF18-B's established fact
  \(\operatorname{div}w=-\hat w\cdot\nabla|w|\) a.e. on \(\{w\ne0\}\) holds *in the
  approximate-gradient sense*. Using it as a distributional identity assumes
  (H1). Any candidate that does so is circular and fails at that line.
- **C2 Structure-hypothesis check against the shifted system.** Every imported
  theorem must be checked at \(\{w=0\}\), not at \(\{\nabla\phi=0\}\). The
  \(C^{1,\alpha}\) family (Uraltseva, Uhlenbeck, Evans, DiBenedetto, Lewis,
  Tolksdorf, Lieberman) is already excluded by HF18-A §1.3: its lower bound
  \(D_\xi a\,\eta\cdot\eta\ge\gamma(\kappa+|\xi|)^{p-2}|\eta|^2\) fails for every
  \(\gamma>0,\kappa\ge0\) at any \(x\) with \(u(x)\ne0\), \(\xi=-u(x)\). Re-importing
  any member of that family is the packet's "p-Laplace theorem applied outside
  its structure hypotheses" falsifier.
- **C3 Manfredi–Weitsman route.** \(W^{2,2}_{\rm loc}\) for \(p\)-harmonic functions,
  \(1<p<3+2/(n-2)\), is *unshifted*; the shifted extension is HF18-A's own
  "plausible but unproved". A candidate invoking it must prove the shifted
  version, and the source is metadata-only in this programme (Comm. PDE 13
  (1988) 651–668), so it cannot be load-bearing on a citation.
- **C4 Nonlinear Hodge route, degenerate boundary case.** See §4: the literature
  family that matches (1.5) structurally excludes exactly our parameter point.
  A candidate must close the degenerate case \(k=0\), not cite past it.
- **C5 Scaling.** Under \(\mathcal S_\lambda: u\mapsto\lambda u(\lambda\cdot)\) one
  has \(\mathcal Q\mapsto\mathcal Q\), \(\|\nabla V\|_2\mapsto\lambda\|\nabla V\|_2\),
  \(D_3\mapsto\lambda^2D_3\), while \(\|\nabla w\|_{L^1(\mathbb R^3)}\mapsto
  \lambda^{-1}\|\nabla w\|_{L^1}\) and \(\|\nabla w\|_{L^1(B_R)}\) rescales to
  \(\lambda^{-1}\|\nabla w\|_{L^1(B_{\lambda R})}\). Any claimed local estimate must
  carry the ball radius through this law; a radius-free constant is a scaling
  error.
- **C6 Boundary terms at infinity.** HF18-A's global identity (1.10) is
  cutoff-free because it pairs \(A\in L^{3/2}\) with \(D_hq\), \(q\in L^3\). Any new
  argument reintroducing a cutoff \(\eta_R\) must display the remainder and its
  \(R\to\infty\) limit; \(\nabla w\) has no a-priori global class.
- **C7 Scope ceiling.** Even granted in full, (H1) promotes exactly HF18-A
  Proposition 3' — the two forms \(K=-\int q\cdot((A\cdot\nabla)w)=\int u\cdot((A\cdot\nabla)w)\)
  — and gives \(\nabla w\) as a genuine object. It supplies **no** time-integrated
  absorption and does **not** touch the first gap. A candidate claiming HIGH-STRAIN
  or HIGH-PRESSURE progress from (H1) alone is refuted by HF18-A §4: no size
  bound in \(\mathcal Q\) and \(D_3\) can close, by scaling.

## 4. Independent source verification for the reopening condition

The parent audit's item 7 pointed the lane at nonlinear Hodge theory. Because
this review's reopening condition rests on that pointer, it was re-verified here
rather than inherited.

**[DI]** T. H. Otway, *An elliptic inequality for nonlinear Hodge fields*,
arXiv `math-ph/9806007` (abstract page and full text fetched this session). The
equation studied is \(\delta(\rho(Q)\omega)=0\) with the *weakened*
irrotationality condition \(d\omega=u\wedge\omega\). The structure condition is
\[
 K^{-1}(Q+k)^q\ \le\ \rho(Q)+2Q\rho'(Q)\ \le\ K(Q+k)^q,
\]
\(K>0\), \(k\ge0\), \(q\ge0\); the paper states that \(L_\omega\) "is a
divergence-form operator which is **uniformly elliptic for \(k>0\)**", and
Theorem 1 asserts \(L_\omega(Q)+C(Q+k)^q(|\nabla u|+|u|^2)Q\ge0\) with \(L_\omega\)
uniformly elliptic in that regime.

Specialisation to (1.5), recomputed here: \(\rho(Q)=Q^{1/2}\) reproduces
\(\rho(Q)\omega=|w|w\), and
\(\rho+2Q\rho'=Q^{1/2}+2Q\cdot\tfrac12Q^{-1/2}=2Q^{1/2}\), i.e. \(q=1/2\) and
\(k=0\). The two-sided bound then holds with \(K=2\), but the uniform-ellipticity
proviso \(k>0\) fails. Independently, our curl condition is not of Otway's
multiplicative form: if \(\operatorname{curl}u=\alpha\wedge w\) for some 1-form
\(\alpha\), then at any \(x_0\) with \(w(x_0)=0\) the right side vanishes while
\(\operatorname{curl}u(x_0)\ne0\) generically — and \(\{w=0\}\) is precisely the
degeneracy set. Both of the parent audit's obstructions are therefore confirmed
independently, at the parameter point that matters.

This is a verified *obstruction to the cited route*, not an impossibility proof
for (H1).

## 5. Refutation attempts

An audit must try to refute the candidate's new facts. There are none to
refute: no statement was produced. The only refutable objects reachable from
this lane's name are the two already-audited upstream statements (H1)-free
results of HF18-A, which are outside this review's scope and carry a standing
PASS. No new counterexample family is proposed here, because proposing one
would be lane work, not audit work.

## Audit record

**VERDICT: INVALID.** There is no object under audit. The audit could not be
performed for the reason that the artifact
`research/evidence/hf19-shifted-hodge-regularity.md` does not exist at
`5aefa82`, has never existed on any ref, and is not present under any other
name in the repository, the user's home tree, or the session scratchpad. This
is not a mathematical verdict on the shifted-Hodge-regularity question, and it
is not a FAIL: nothing was asserted, so nothing is wrong.

**REVIEWED SCOPE:** the absence itself (§1), certified by eight independent
searches; the disambiguation against the three existing HF19 notes (§2); the
parent statements that define the lane's obligations, read in full —
`hf18-hodge-regularity.md` (§0 imports, §1 including (1.1)–(1.5), Lemma V,
Theorem 1, Corollary 1, §2 Theorem 2, §3 Propositions 3 and 3′, §4 Theorem 4
and Corollary 4, §5 self-check, §7 sources) and
`hf18-review-hodge-regularity.md` (refutation attempts 1–7 and full audit
record); `hf18-divergence-speed-link.md` and its two reviews and
`hf17-quotient-functional.md`, `hf17-quotient-evolution.md` as summarised in
PLAN.md "HF16–HF17" and "HF18"; `PLAN.md` "Beyond the checkpoint", "Frontier
packet", "HF16–HF17", "HF18". No upstream result was re-audited; all carry
standing PASS verdicts.

**FIRST BAD BRIDGE:** none, vacuously. There is no first nontrivial implication
to reconstruct, because there is no chain of implications. The first *process*
failure is upstream of the mathematics: the HF19 lane "shifted-hodge-regularity"
produced no output file while the other three HF19 lanes did.

**EVIDENCE:** the eight searches of §1, run at `5aefa82` and reproduced there
verbatim; section-header enumeration and `(H1)`/`W^{1,1}`/`Sibner`/`Otway`
greps across the three existing HF19 notes (§2), which show each of them
explicitly *leaving* (H1) open rather than addressing it; the (H1) statement and
the \(|w|^{-1}\notin L^1_{\rm loc}\) obstacle read directly from
`hf18-hodge-regularity.md` §1.6(e) and §3.2; the ellipticity-failure argument of
§1.3 read directly; the \(\mathcal S_\lambda\) exponents of C5 recomputed here
from \(u_\lambda(x)=\lambda u(\lambda x)\); and the primary source of §4 fetched
and its parameter specialisation \(q=1/2\), \(k=0\) recomputed.

**REPLACEMENT ARGUMENT:** none is possible and none is offered. A REPAIR verdict
requires a replacement lemma for a broken step; there is no step. Supplying the
missing lane's mathematics here would make this file the candidate rather than
its audit, and would leave the candidate unaudited — the failure mode this
review exists to prevent. §3 records the obligations and pre-registered checks
so that a re-run is auditable against a fixed standard, and §4 verifies the one
literature pointer the reopening condition depends on.

**CONDITIONAL SUFFIX THAT SURVIVES:** nothing new, and nothing lost. The HF18
suffix is untouched by this audit and stands exactly as recorded: at every fixed
time of a classical \(H^m\) solution, \(m\ge4\), divergence-free on
\(\mathbb R^3\), with no smallness and no decay beyond \(u\in H^m\) —
\(V=|w|^{1/2}w\in H^1\), \(A=|w|w\in W^{1,3/2}\),
\(w\in L^3\cap L^9\cap B^{2/3}_{3,\infty}\),
\(D_{\mathcal Q}(u)=D_3(w)=\int(|\nabla V|^2-\tfrac19|\nabla|V||^2)\ge c\|u\|_9^3\),
the transport forms (F2), (F5), (F6), (F7), and on every compact classical
interval \(\mathcal Q'+\nu D_3(w)=K\) with \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\);
(F3)–(F4) under (H1) only. Hence, if the first gap is ever closed with
\(\theta\le1\) and input-only \(A_{\rm input}\), then
\(\mathcal Q(\tau)+(1-\theta)\nu\int_0^\tau D_3\,dt\le\mathcal Q(0)+A_{\rm input}\),
giving \(\sup_t\|u\|_3\) and \(u\in L^3_tL^9_x\) up to \(\min(H,T_*)\), hence
continuation by the imported ESS node. This review adds no term to that suffix
and removes none.

**UNNECESSARY DEPENDENCIES:** none identified, there being no argument. Recorded
for the re-run: (H1) is *not* a dependency of any HF18-A result outside
Proposition 3′, nor of any HF19-A/B/D result, so the lane is not blocking.

**NON-CLAIMS:** this file establishes no regularity of \(w\), \(q\) or \(\phi\);
does not prove, disprove, or make progress on (H1); does not show (H1) is
unprovable — §4 obstructs one cited route at one parameter point and nothing
more; establishes no bound on \(K\), no time-integrated absorption, no
HIGH-STRAIN and no HIGH-PRESSURE result, no continuation theorem for arbitrary
data, and no Millennium claim. It passes no judgement on the mathematical
content of the three existing HF19 notes, which are outside its scope and
require their own audits. The verdict INVALID is about artifact availability
only and must not be reported as a negative finding against the lane's
mathematics.

**REOPENING CONDITION:** (1) The lane produces
`research/evidence/hf19-shifted-hodge-regularity.md`; this audit is then re-run
against it with a real SHA-256 freeze and the checks C1–C7 of §3 applied in
order. (2) If the lane is not re-run, `PLAN.md` should record HF19 as having
three lanes (A, B, D) rather than four, so the absence is a decision on the
record instead of a silent hole. (3) Independently of (1) and (2): the parent
reopening condition of `hf18-review-hodge-regularity.md` (3)(b) stands, with §4
above narrowing it — the Sibner–Sibner / Otway nonlinear Hodge family is the
right structural home for (1.5), our parameter point is exactly its excluded
degenerate boundary case \(k=0\) with \(q=1/2\), and our prescribed curl
\(\operatorname{curl}w=\operatorname{curl}u\) is provably not of the
multiplicative form \(u\wedge\omega\) near \(\{w=0\}\); so closing that degenerate
case, or proving it cannot be closed, is the decisive step and no citation can
substitute for it.

---

## Frontier record

**MODE / RESULT:** REVIEW; result INVALID — the audit target does not exist, at
`5aefa82` or on any ref, and is not present under another name. Certified by
eight searches and a disambiguation against the three HF19 notes that do exist.
One by-product: the parent audit's literature pointer was re-verified from the
primary source, and the excluded parameter point of the matching nonlinear
Hodge theory was recomputed independently.

**CLAIM AND SCOPE:** exactly two claims. (i) `research/evidence/hf19-shifted-hodge-regularity.md`
is absent at commit `5aefa82`, with the search record of §1; scope: this
repository, this home tree, this session's scratchpad, at that commit. (ii) In
Otway `math-ph/9806007` the structure condition
\(K^{-1}(Q+k)^q\le\rho+2Q\rho'\le K(Q+k)^q\) with uniform ellipticity stated for
\(k>0\) specialises, at \(\rho(Q)=Q^{1/2}\), to \(q=1/2\), \(k=0\); and
\(\operatorname{curl}u=\alpha\wedge w\) is impossible at points where \(w=0\) and
\(\operatorname{curl}u\ne0\). Scope: a statement about that paper's hypotheses
and about (1.5)'s parameters — not a statement about (H1)'s truth.

**EVIDENCE:** as recorded under EVIDENCE above.

**FIRST GAP:** unchanged by this review. An input-only spacetime bound
\(\int_0^\tau K\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+A_{\rm input}\), uniform for
\(\tau<\min(H,T_*)\), \(\theta\le1\), \(A_{\rm input}\) depending only on
\(u_0,\nu,H\) — or the pressure-route analogue. (H1) is not this gap and, by C7,
would not close it.

**SURVIVING CONDITIONAL SUFFIX:** as recorded under CONDITIONAL SUFFIX THAT
SURVIVES above; the HF18 suffix, unchanged.

**NON-CLAIMS:** as recorded under NON-CLAIMS above. In particular no progress on
(H1), no progress on the first gap, and no Millennium claim.

**NEXT DISTINCT ACTION:** re-run the shifted-Hodge-regularity lane with the
target fixed as (H1) for the system (1.5), attacking the degenerate case
\(k=0\), \(q=1/2\) of the nonlinear Hodge structure condition directly, and with
the scope ceiling C7 stated in the lane's own header so it cannot drift into a
gap claim; then re-run this audit against the produced file with a real freeze.

## Sources

Directly inspected [DI] this session:
- T. H. Otway, *An elliptic inequality for nonlinear Hodge fields*,
  arXiv `math-ph/9806007`: title, author, abstract; equation
  \(\delta(\rho(Q)\omega)=0\) with \(d\omega=u\wedge\omega\); the structure
  condition \(K^{-1}(Q+k)^q\le\rho+2Q\rho'\le K(Q+k)^q\); the sentence that
  \(L_\omega\) is uniformly elliptic for \(k>0\); Theorem 1
  \(L_\omega(Q)+C(Q+k)^q(|\nabla u|+|u|^2)Q\ge0\).
- Repository files at `5aefa82`: `PLAN.md`; `research/evidence/hf18-hodge-regularity.md`;
  `research/evidence/hf18-review-hodge-regularity.md`;
  `research/evidence/hf19-difference-functional.md`,
  `hf19-temporal-normal-form.md`, `hf19-second-order-falsifier.md` (headers,
  summaries, and targeted greps).

Metadata-only [MO], not load-bearing anywhere in this audit: L. M. and R. J.
Sibner (nonlinear Hodge theory); Manfredi–Weitsman, Comm. PDE 13 (1988)
651–668; Uraltseva, Uhlenbeck, Evans, DiBenedetto, Lewis, Tolksdorf, Lieberman;
Bojarski–Iwaniec. Lindqvist, *Notes on the p-Laplace equation*, was directly
inspected in the parent audit and is not re-cited as load-bearing here.
