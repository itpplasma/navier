# Review of HF26 §9: the controller resolution of open item 7.1 (Li's Theorem 7.2)

Independent adversarial audit, 2026-09-06 (Europe/Vienna).  Lens: re-fetch the
primary source myself, re-derive every geometric fact from scratch (by hand and
numerically), and attempt explicit refutations of each link in the controller's
chain — including the links that, if broken, would *strengthen* the programme's
position rather than weaken it.

## Freeze

| object | identity |
|---|---|
| research HEAD at audit time | `7b7b1ee90676778c7aa2e4215f60c124b46113fc` |
| target file | `research/evidence/hf26-prior-art-projection-differentiability.md`, 1551 lines, sha256 `1f955a5f3c4ef8dca812a23fa9eacdf4ae950dd874ee1fd8aa3fe6f7c76096dd` |
| audited section | §9 "CONTROLLER RESOLUTION of item 7.1 (2026-09-06)", lines 1494–1551 |
| primary source re-fetched | `arXiv:2303.16265v1` (28 Mar 2023), 30 pp., read with a PDF reader, then **deleted**; no copy retained anywhere |
| published text | J. Optim. Theory Appl. **200** (2024) 923–950, DOI `10.1007/s10957-023-02329-7` — **closed access, not obtained** (Springer returns a 303 to an authentication endpoint; Semantic Scholar reports `openAccessPdf.status = "CLOSED"`) |

## Scope

- **In scope:** §9 only — the verbatim rendering of Li's Definition 7.1, the
  claim about the proof's convergence factor, Finding 1 (power types of `L^3`),
  Finding 2 (vacuity by Nordlander), the Pisier attribution, the scope
  paragraph, and the verdict.
- **Read for context, not audited:** §§0–8 of the same file, and the reference
  they make to `research/evidence/hf26-temporal-continuation.tex` §3.
- **Not in scope:** the correctness of the candidate's Theorem 3.4/3.5, the
  correctness of Li's other sections, and any novelty judgement of any kind.
- **Constraints honoured:** third-party PDF downloaded to a scratch directory,
  read, and deleted (verified absent by `find`); no contact with any person; no
  self-managed polling.

---

## VERDICT: **CONFIRMED WITH CORRECTION**

Both findings stand *as statements about the arXiv preprint*.  The quotation of
Definition 7.1 is exact.  The claim about the proof's convergence factor is
exact.  Finding 1 is correct and in fact robust in a way the controller did not
state.  Finding 2's **conclusion** (the hypothesis class is empty, the theorem
vacuous) is correct, and I give a shorter and stronger proof of it; but Finding
2's **argument as written** is not valid in full generality, because
Nordlander's theorem requires `dim X >= 2` and the controller asserts it "for
every Banach space".  The corrections are C1–C7 below.

One genuine over-conclusion is present, and it is in the framing rather than in
either finding: the verdict sentence and the declaration that item 7.1 is "no
longer blocking" are stated **without the preprint qualifier**, while the branch
"published version repaired the ordering *and* the proof" is not excluded by
anything established here (correction C5).  §7.1 and the §8 NEXT DISTINCT ACTION
of the same file were left unamended and now contradict §9 (correction C7).

There is **no** over-conclusion in the novelty direction.  §9's sentence "The
programme still may not claim novelty for the linearization — every other ground
in section 6 stands untouched" is accurate and is the correct posture.

---

## Q1. Definition 7.1 as quoted — **CONFIRMED, exact**

I re-fetched `arXiv:2303.16265v1` and read §7 with a PDF reader.  The passage
preceding Definition 7.1 reads, verbatim (PDF text layer; superscripts on `ε`
and `t` are flattened by the extractor but are unambiguous from the surrounding
sentence "This positive number p > 1 describes the 'level' of convexity"):

> "The Pisier renorming theorem states that a super-reflexive uniformly convex
> and uniformly smooth Banach space X admits an equivalent uniformly convex and
> uniformly smooth norm for which the modulus of convexity and the modulus of
> smoothness 𝛿 and 𝜌 satisfy the following conditions: there are positive
> numbers a, b with a ≥ 1, b ≥ 1 and p, q with 1 < p < q such that
>
>    (c) δ(ε) ≥ 𝑎ε^𝑝 , for ε ∈ (0, 2];
>    (d) 𝜌(t) ≤ b𝑡^𝑞 , for t > 0."

and then

> "**Definition 7.1.** Let X be a uniformly convex and uniformly smooth Banach
> space. If there are positive numbers a, b with a ≥ 1, b ≥ 1 and p, q with
> 1 < p < q such that 𝛿 and 𝜌 satisfy the above conditions (c) and (d), then X
> is called a p-q uniformly convex and uniformly smooth Banach space."

> "**Theorems 7.2.** Let X be a p-q uniformly convex and uniformly smooth Banach
> space and C a nonempty closed and convex subset of X. Then 𝑃𝐶 is directionally
> differentiable on X."

(The "Theorems 7.2" plural is the preprint's own typo.)

The proof's final display and closing step, verbatim:

> "≤ 𝑘(6𝑎⁻¹𝑏(2‖𝑣‖)^𝑞)^{1/𝑝} 𝑡^{𝑞/𝑝−1} + 𝑘(6𝑎⁻¹𝑏(2‖𝑣‖)^𝑞)^{1/𝑝} 𝑠^{𝑞/𝑝−1}, for any
> s, t with 0 < s < t < 𝜆.
>
> Notice that 𝑞/𝑝 − 1 > 0 and for this arbitrarily given v ∈ 𝑋 with v ≠ θ,
> 𝑘(6𝑎⁻¹𝑏(2‖𝑣‖)^𝑞)^{1/𝑝} is a constant, which is independent from 1 > 𝜆 > 0 and
> s, t with 0 < s < t < 𝜆 < 1. This implies that … can be arbitrarily small as
> what one desires …"

**Every element of the controller's quotation checks out**: `a, b >= 1`;
`1 < p < q`; `delta(eps) >= a eps^p` on `eps in (0,2]`; `rho(t) <= b t^q` for
`t > 0`; convergence factor `t^(q/p - 1)`; closing step `q/p - 1 > 0`.  **No
misquotation.**  The controller's own hedge ("verbatim in substance") is if
anything too modest.

Two further facts I established that §9 does not record, both favourable to it:

- The proof is otherwise **internally valid**.  The chain
  `delta^{-1}(a u^p) <= u` is legitimate given (c) and `delta^{-1}` monotone,
  the restriction `u < 2` needed because (c) is only asserted on `(0,2]` is
  exactly what the auxiliary choice (7.3) secures, and the resulting estimate is
  a genuine Cauchy criterion in a complete space.  The theorem is therefore not
  *wrong*; it is **vacuous**.  §9's phrase "could not subsume anything as the
  hypothesis is stated" is the right characterisation.
- The proof's engine is Alber's global Björnestål estimate
  `‖P_C x − P_C y‖ ≤ k δ^{-1}(6ρ(2‖x−y‖))`, cited as "(5.4) in [1]", where [1] is
  an unpublished 1993 SIAM-meeting presentation of Ya. Alber.

## Q2. Finding 1, the `L^3` power types — **CONFIRMED, and robust beyond what is claimed**

The controller's arithmetic and its conclusion are correct.  I verified the
power types from scratch rather than by citation.

**Convexity.**  Hanner (1956) gives, for `r >= 2`,
`delta_{L^r}(eps) = 1 − (1 − (eps/2)^r)^{1/r}` exactly.  For `r = 3` this is
`eps^3/24 + O(eps^5)`; numerically `delta/eps^3 -> 0.0416667 = 1/24`
(`eps = 10^-3` gives `4.16666701e-11`), and `delta_{L^3}(2) = 1`.  So the
convexity power type of scalar `L^3` is exactly `3`, i.e. `max(3,2)`.

**The space is vector-valued, and the controller does not say so.**  The
programme's space is `L^3(R^3;R^3)` — a Lebesgue–Bochner space over a Hilbert
fibre, not scalar `L^3(R^3)`, which is what §9 writes.  The transfer is true but
is *not* automatic, so I proved it:

> For `a, b` in a Hilbert space `H` and `p >= 2`,
> `|(a+b)/2|^p + |(a−b)/2|^p <= (|a|^p + |b|^p)/2`.
> *Proof.*  With `s = |(a+b)/2|`, `t = |(a−b)/2|`, the parallelogram law gives
> `s^2 + t^2 = (|a|^2+|b|^2)/2`.  Since `u -> u^{p/2}` is convex for `p >= 2`,
> `s^p + t^p = (s^2)^{p/2} + (t^2)^{p/2}` is maximised over the segment
> `{s^2 + t^2 = const, s^2,t^2 >= 0}` at an endpoint, giving
> `((|a|^2+|b|^2)/2)^{p/2}`, which is `<= (|a|^p+|b|^p)/2` by the power-mean
> inequality `M_2 <= M_p`. ∎

Integrating over `R^3` gives Clarkson's inequality with constant 1 in
`L^3(R^3;R^3)`, hence `delta(eps) >= 1 − (1 − (eps/2)^3)^{1/3}`; and since scalar
`L^3(R^3)` embeds isometrically (`v = f e_1`) and moduli of convexity only
increase on subspaces, that bound is an equality.  Numerical check over 4·10^5
random pairs in `H = R^3`, `p = 3`: maximum violation `−4.2e−09`, i.e. none.
**Vector-valued convexity power type = 3, confirmed.**

**Smoothness.**  `rho_{L^3}(t)` computed from Lindenstrauss duality
`rho_{X*}(t) = sup_{0<=eps<=2}{eps t/2 − delta_X(eps)}` with
`delta_{L^{3/2}}` from the implicit Hanner equation:
`rho_{L^3}(t)/t^2 -> 1 = (p−1)/2` (values `0.9999` at `t = 0.01`).  Power type
exactly `2 = min(3,2)`.  For the vector-valued space I need only the *lower*
bound `rho >= rho_Hilbert ≍ t^2/2`, which holds in every Banach space of
dimension `>= 2`; the matching upper bound (2-uniform smoothness of `L^p(mu;H)`
for `p >= 2`) is the standard Figiel–Pisier fact, taken on citation and **not
load-bearing** for anything below.

**The conclusion about the convergence factor is correct, and stronger than
stated.**  For `X = L^3(R^3;R^3)`, *every* admissible exponent pair has `p >= 3`
(because `delta ≍ eps^3` caps it) and `q <= 2` (because `rho >= rho_Hilbert`
caps it).  Hence `q/p <= 2/3 < 1` for **every** admissible pair, not merely for
the sharp pair `(3,2)`, and the factor `t^{q/p−1}` diverges as `t` decreases to
zero in every case.  §9's "`p = 3` and `q = 2`" reads as though the exponents
were uniquely determined, which they are not; the conclusion survives that
correction with room to spare (C2).

## Q3. Finding 2, vacuity — **CONCLUSION CONFIRMED; ARGUMENT NEEDS REPAIR**

### (a) Is Nordlander correctly stated and applied?

Bibliographic identity confirmed: G. Nordlander, "The modulus of convexity in
normed linear spaces", Ark. Mat. **4** (1960) 15–17, DOI `10.1007/BF02591317`.
The full text is behind Project Euclid registration and I did **not** read it;
the statement is taken on citation and verified numerically (below).

The inequalities as used —
`delta_X(eps) <= delta_H(eps) = 1 − sqrt(1 − eps^2/4)` and
`rho_X(t) >= rho_H(t) = sqrt(1+t^2) − 1` — are the standard pair, and the
asymptotics the controller quotes (`~ eps^2/8`, `~ t^2/2`) are correct.
Independent numerical check on 12 random two-dimensional polygonal norms
(random symmetric polytope unit balls, 1200-point sphere discretisation):
`delta_X − delta_H <= −0.0078` at every tested `eps`, `rho_X − rho_H >= +0.023`
at every tested `t`; **zero violations**.  For `L^3` specifically, `delta_{L^3}
<= delta_H` was verified on a 2000-point grid of `(0,2]`.

**But the statement is applied with the wrong quantifier.**  §9 says "every
Banach space".  Nordlander's inequality requires `dim X >= 2`.  In a
one-dimensional space the unit sphere is `{±e}`, so `‖x−y‖ >= eps > 0` forces
`y = −x` and `delta(eps) = 1` on all of `(0,2]` — which *exceeds* `delta_H`, so
Nordlander fails there.  Dually `rho(t) = max(0, t−1)`, which is *below*
`rho_H(t)` for small `t`.  The controller's chain therefore does not cover
`dim X <= 1` (C1).

### (b) Does (c) with `a >= 1` force `p > 2`?  Endpoint vs. small `eps`

- **Small `eps`, `dim >= 2`:** `a eps^p <= eps^2/8 + O(eps^4)`.  If `p < 2` the
  ratio `8a·eps^{p−2}` diverges; if `p = 2` one needs `a <= 1/8`.  With `a >= 1`
  both are excluded, so `p > 2`.  **The controller is right.**
- **Endpoint `eps = 2` — and this is the decisive case the controller did not
  use.**  By definition `delta` maps `[0,2]` into `[0,1]`, so `delta(2) <= 1` in
  *every* normed space, with no dimension hypothesis and no appeal to
  Nordlander.  Condition (c) at `eps = 2` demands `delta(2) >= a·2^p >= 2^p > 2`,
  since `a >= 1` and `p > 1`.  Contradiction, immediately.

  So **Definition 7.1's class contains no space whose unit sphere is nonempty**,
  by a two-line argument.  The controller's Nordlander route reaches the same
  conclusion by a longer path that additionally needs `dim >= 2` (C3).

  Note that this is exactly where `a >= 1` earns its keep: with `a > 0`
  unconstrained, a one-dimensional space *does* satisfy (c) (take `a = 2^{−p}`,
  since `delta ≡ 1`) and also (d) (`ρ(t) = max(0,t−1) <= t^q` for `t > 1`,
  `q > 1`), for *any* `1 < p < q`.  The controller's own quoted `a >= 1` is what
  removes the one-dimensional loophole; §9 does not notice this, and Finding 2
  as written would have a counterexample without it.

### (c) Is "the class is empty" airtight?  Loopholes

**Airtight except for `X = {0}`.**  Enumerating:

| space | in the class? | why |
|---|---|---|
| `dim X = 0` (`X = {0}`) | vacuously yes | `S_X = ∅`, so `delta = inf ∅ = +∞` and `rho = sup ∅ = −∞`; (c) and (d) hold trivially |
| `dim X = 1` | **no** | `delta(2) = 1 < 2^p <= a·2^p` |
| `dim X >= 2` | **no** | same endpoint argument; independently, Nordlander gives `p >= 2 >= q`, contradicting `p < q` |

For `X = {0}` the metric projection onto the only nonempty closed convex subset
is the identity on a point and Theorem 7.2 is true and empty of content, so the
loophole changes nothing.  There is **no** "restricted range" escape: (c) is
demanded on all of `(0,2]` and (d) on all of `(0,∞)`, and it is the `eps = 2`
endpoint of (c) that does the killing, so weakening the small-`eps` behaviour
cannot help.  There is no renorming escape either (R12 below).

**Robustness the controller does not claim, and should.**  Dropping `a, b >= 1`
to `a, b > 0` — i.e. supposing the `>= 1` were a transcription slip in the
preprint — the class is *still* empty for every `dim X >= 2`: Nordlander forces
`p >= 2` and `q <= 2`, hence `q <= 2 <= p`, which contradicts the **strict**
`p < q`.  Finding 2's conclusion therefore does not hinge on the `a >= 1`
detail at all (C4).

**The strongest true statement, which unifies both findings and which §9
misses.**  For every Banach space of dimension `>= 2` and every `a, b > 0`
satisfying (c) and (d), one has `q <= 2 <= p`, hence

    q/p − 1 <= 0,   with equality only when p = q = 2.

So the closing step of Li's proof, `q/p − 1 > 0`, is **unattainable in every
Banach space**, not merely in `L^3`.  Finding 1's "it runs backwards there" is
not a peculiarity of `L^3`; it is the general situation, and `L^3` merely makes
the failure strict rather than borderline (C6).

### (d) "Verified numerically against the Hilbert moduli"

Emptiness of a hypothesis class is a theorem, not a numerical fact.  Numerics
can confirm the Hilbert-modulus formulas and sample individual spaces — which is
what I did, and what the controller presumably did — but the sentence as written
invites the reading that the vacuity itself was numerically established.  It was
not, and does not need to be (C7).

## Q4. The Pisier attribution — **CONFIRMED, and the controller understates it**

§9 says "the preprint attributes (c) and (d) to the Pisier renorming theorem,
which gives the **opposite** ordering, convexity of power type at least two and
smoothness of power type at most two."

- **The attribution is really made.**  Verbatim from the preprint, immediately
  before Definition 7.1: *"The Pisier renorming theorem states that a
  super-reflexive uniformly convex and uniformly smooth Banach space X admits an
  equivalent uniformly convex and uniformly smooth norm for which … there are
  positive numbers a, b with a ≥ 1, b ≥ 1 and p, q with 1 < p < q such that (c)
  … (d) …"*
- **What Pisier actually gives.**  Pisier, "Martingales with values in uniformly
  convex spaces", Israel J. Math. **20** (1975) 326–350: a super-reflexive space
  admits an equivalent norm whose modulus of smoothness satisfies
  `rho(t) <= C t^q` for some `q > 1`, and dually an equivalent norm whose
  modulus of convexity satisfies `delta(eps) >= c eps^p` for some `p < ∞`.
  Independent confirmation of the smoothness half, verbatim from the Wikipedia
  article *Uniformly smooth space*: *"A super-reflexive space X admits an
  equivalent uniformly smooth norm for which the modulus of smoothness ρ_X
  satisfies, for some constant C and some p > 1: ρ_X(t) ≤ C·t^p, t > 0."*
  Combined with `rho >= rho_Hilbert ≍ t^2/2`, the exponent produced is
  necessarily `<= 2`; dually the convexity exponent is necessarily `>= 2`.  So
  Pisier's exponents obey **convexity exponent `>= 2 >=` smoothness exponent** —
  the reverse of `1 < p < q`.  **The controller's characterisation is correct.**
- **Additional fact, in the controller's favour.**  The preprint gives **no
  citation at all** for the Pisier renorming theorem.  Its 24-item reference
  list (Alber ×4, Aronszajn, Berdyshev, Björnestål, Borwein–Noll,
  Fitzpatrick–Phelps, Haraux, Holmes, Khan–Li, Malanowski ×2, Mignot, Noll ×2,
  Petryshyn, Shapiro ×3, Takahashi, Tapia, Zarantonello) **contains no Pisier
  entry**.  The "well-known properties" (a) and (b) *are* cited, to [3,17,22,23];
  the conditions (c),(d) are not.  This makes the misstatement of the ordering
  substantially more likely to be an authorial slip carried into Definition 7.1
  than a deliberate non-standard convention.

## Q5. Scope honesty — **ACCURATE BUT INSUFFICIENT**

§9's scope paragraph is accurate on three counts: the resolution does read the
preprint and not the published JOTA text; Finding 2 is flagged as being about
the preprint only; and the note flags itself as an unaudited controller
derivation.  I independently confirmed that the published version is closed
access (Springer 303 to authentication; Semantic Scholar `"status": "CLOSED"`),
so the controller could not have read it, and that the published abstract —
which I re-fetched independently from Semantic Scholar — indeed omits the `p-q`
result that the arXiv v1 abstract announces ("Finally, we define the concept of
p-q uniformly convex and uniformly smooth Banach spaces.  We will prove that if
X is a p-q uniformly convex and uniformly smooth Banach space, then for any
nonempty closed and convex subset C of X, Pc is directionally differentiable on
the whole space X").

**It is insufficient in one place.**  §9 asserts "Finding 1 is independent of
that", then immediately qualifies it with "unless the proof were changed as
well".  The qualifier is not a footnote; it is the whole question.  There are
three branches for the published text:

1. **Published = preprint.**  Class empty, theorem vacuous, does not reach
   `L^3`.  Findings 1 and 2 both apply.
2. **Ordering corrected to `1 < q <= 2 <= p`, proof unchanged.**  Then `L^3` *is*
   in the class (3-uniformly convex, 2-uniformly smooth), so the *hypothesis no
   longer fails* — Finding 1's first half is void — and the only remaining
   objection is that the printed proof's closing step `q/p − 1 > 0` is false.
   That is a **defect finding against a refereed paper**, a far heavier claim
   than "the theorem does not apply", and the programme would have to say so in
   those words.
3. **Ordering corrected *and* proof repaired.**  Nothing established here
   excludes this.  In that branch Theorem 7.2 would apply to
   `X = L^3(R^3;R^3)`, `C = G_3`.

Branch 3 is the one that matters and it is open.  A referee who noticed the
ordering would have been looking straight at the step the ordering supports, so
"ordering fixed, proof untouched" is arguably the *least* likely of the three.
Consequently **item 7.1 is not fully closed**, and §9's flat "It is no longer
blocking" is defensible only in the weaker operational sense that no programme
claim depends on the answer (C5).

**One thing that makes branch 3 much less dangerous than §7.1 assumed, and which
I record because it bears on the bottom line.**  Even in branch 3, Theorem 7.2
would **not** subsume the candidate's Theorem 3.4.  Li's Definition 4.1, read
verbatim in the preprint, is one-sided:

> "**Definition 4.1.** For x ∈ X and v ∈ X with v ≠ θ, if the following limit
> exists (that is a point in X), lim_{t↓0} [P_C(x+tv) − P_C(x)]/t, then, P_C is
> said to be (Gâteaux) directionally differentiable at point x along direction
> v …"

and Theorem 7.2 asserts existence only, with no representation of the limit.
The candidate's T3.4 asserts a **two-sided** limit (`ε → 0`, `ε ≠ 0`) and
**identifies** it as the linear operator `L_U = I − P_{E_U}`.  Existence of both
one-sided limits does not give a two-sided limit unless the derivative is odd,
which Li does not assert (the preprint's §4 gives positive homogeneity only).
Conversely, in the mode of convergence Li's conclusion would be stronger for the
one-sided limit: `L^3` norm convergence implies `H_U` convergence, since
`M_U = ρI + U⊗U/ρ` has eigenvalues `ρ, ρ, 2ρ` and hence
`‖a‖_U^2 <= 2∫|U||a|^2 <= 2‖U‖_3‖a‖_3^2` by Hölder.  So the two statements are
**not nested in either direction**.  This makes §1.3's and §7.1's earlier phrase
"strictly more than T3.4 asserts" imprecise — an observation about §§1.3/7.1,
outside my audit scope, recorded for whoever amends them.

## Q6. The bottom line — **FOLLOWS, with the qualifier restored; no novelty over-conclusion**

> "Li's Theorem 7.2 **does not subsume** the candidate's weighted linearization,
> and could not subsume anything as the hypothesis is stated. The programme
> still may not claim novelty for the linearization — every other ground in
> section 6 stands untouched, and those grounds are what matter — but this
> particular paper is not the reason."

- "does not subsume … as the hypothesis is stated" — **established**, for the
  preprint, twice over (Finding 1 and Finding 2), and additionally by the
  one-sided/two-sided mismatch above which holds in every branch.
- "could not subsume anything as the hypothesis is stated" — **established**,
  and by a shorter argument than the one given.
- "this particular paper is not the reason" — this is broader than Theorem 7.2,
  since the same paper's §6 is the subject of the file's own open item §7.2.  I
  read §6 in full to test it: it contains only Theorem 6.1 (base point `y ∈ C`,
  direction `v ∈ C^⊥\{θ}`, derivative `θ`), Example 6.2 (`(R^3,‖·‖_3)` and its
  duality maps), Proposition 6.3 (pre-images of the positive cone) and
  Proposition 6.4 (the positive cone's directional derivatives).  §5 is balls,
  §4 is general properties, §8 is Hilbert space.  **No result of the preprint
  touches `P_{G_3}` at a base point outside `G_3`.**  The clause is therefore
  correct for the preprint — and, incidentally, the file's own open item §7.2 is
  now answered for the preprint.
- **No novelty over-conclusion.**  §9 explicitly re-states that the programme
  may not claim novelty and that §6's fifteen non-claims stand untouched.  That
  is the correct reading and it is stated plainly.  Nothing in §9 can be read as
  clearing the way for a novelty claim, and I found no sentence that drifts in
  that direction.
- **The one over-reach** is the missing "in the preprint" qualifier on the
  verdict sentence and on "It is no longer blocking" (C5, C7).

---

## Numbered corrections

**C1.**  §9, Finding 2: "By Nordlander's theorem every Banach space satisfies
`delta_X <= delta_Hilbert` … and `rho_X >= rho_Hilbert` …".  Insert the
dimension hypothesis: Nordlander's inequality holds for `dim X >= 2`.  In a
one-dimensional space `delta ≡ 1` on `(0,2]` and `rho(t) = max(0,t−1)`, and both
inequalities fail.  Suggested replacement: "By Nordlander's theorem, every
Banach space of dimension at least two satisfies …".

**C2.**  §9, Finding 1: "so in Li's notation `p = 3` and `q = 2`" should not
suggest uniqueness.  The admissible sets are `p ∈ [3,∞)` and `q ∈ (1,2]`;
`(3,2)` is the sharp pair.  Suggested replacement: "…so every admissible pair
has `p >= 3` and `q <= 2`, the sharp pair being `p = 3`, `q = 2`.  The
hypothesis `p < q` therefore fails for every admissible pair, and the proof's
convergence factor `t^{q/p−1}` has `q/p <= 2/3 < 1` in every case."

**C3.**  §9, Finding 2: add the elementary endpoint argument, which is shorter
than the Nordlander route, needs no dimension hypothesis, and covers the case
C1 exposes.  Suggested insertion: "More simply: `delta` takes values in `[0,1]`
by definition, so (c) at `eps = 2` requires `1 >= delta(2) >= a·2^p >= 2^p > 2`,
which is false for every `a >= 1`, `p > 1`.  The class therefore contains no
space with a nonempty unit sphere; only the zero space escapes, vacuously."

**C4.**  §9, Finding 2: record that the emptiness does **not** depend on the
`a >= 1` normalisation.  With `a, b > 0` unconstrained the class is still empty
for `dim X >= 2`, because Nordlander forces `q <= 2 <= p` and `p < q` is strict.
(`a >= 1` is exactly what additionally excludes the one-dimensional space, which
*does* satisfy (c) and (d) when `a` may be small.)

**C5.**  §9, Verdict and the opening "It is no longer blocking": restore the
preprint qualifier.  Suggested replacement for the verdict's first sentence:
"**In the March 2023 preprint**, Li's Theorem 7.2 does not subsume the
candidate's weighted linearization, and could not subsume anything, as the
hypothesis is stated."  And for the opening: "It is no longer blocking *for any
programme claim*, since no claim depends on the answer; the printed JOTA text is
still required before the comparison can be written down as settled."

**C6.**  §9, Finding 1: state the general fact, which is stronger and shorter
than the `L^3`-specific one.  In every Banach space of dimension `>= 2`, any
exponents satisfying (c) and (d) obey `q/p − 1 <= 0`, with equality only in the
Hilbert-modulus case `p = q = 2`.  Li's closing step `q/p − 1 > 0` is therefore
unavailable in every Banach space, and `L^3` is merely a case where the failure
is strict.

**C7.**  Two housekeeping items in the same file, both now inconsistent with §9:
(i) §7 item 1 still reads "**This must be resolved from the printed JOTA article
before any statement about the novelty of T3.4 is made anywhere**" and §8's NEXT
DISTINCT ACTION still lists obtaining the printed JOTA article as step (1); §9
neither amends nor cross-references them.  (ii) §9's "Verified numerically
against the Hilbert moduli" overstates what numerics can contribute — the
vacuity is a two-line proof, and numerics only confirm the Hilbert-modulus
formulas.  Also worth folding in: the preprint's §6 contains no statement about
a subspace at a general base point, which answers §7 item 2 for the preprint.

---

## Refutation attempts and outcomes

**R1 — "The controller misquoted Definition 7.1 (constants, exponent ordering,
or the ranges of `eps` and `t`)."**  *Failed.*  Re-fetched the preprint and read
§7 with a PDF reader.  Every element matches verbatim: `a, b >= 1`, `1 < p < q`,
`eps ∈ (0,2]`, `t > 0`.

**R2 — "The proof's convergence factor is not `t^{q/p−1}`, or the closing step
is not `q/p − 1 > 0`; the controller reverse-engineered it."**  *Failed.*  Both
appear verbatim in the displayed estimate and in the sentence "Notice that
q/p − 1 > 0 …".

**R3 — "Finding 2's emptiness argument is not valid for every Banach space."**
*Succeeded, against the argument only.*  Nordlander requires `dim X >= 2`; the
one-dimensional space satisfies neither Nordlander inequality.  The
**conclusion** survives via `delta(2) <= 1 < a·2^p`.  → C1, C3.

**R4 — "The emptiness is an artefact of the `a, b >= 1` normalisation; relax it
to `a, b > 0` and the class is populated, so Finding 2 is fragile."**  *Failed,
and the attempt strengthened the controller.*  With `a, b > 0` the class is
still empty for `dim X >= 2` because `p < q` is strict while `q <= 2 <= p`.
Only `dim X <= 1` is rescued, and there Theorem 7.2 is trivial.  → C4.

**R5 — "`p = 3, q = 2` is not well defined; some other admissible pair for `L^3`
could satisfy `p < q` or make the factor converge."**  *Failed.*  `delta_{L^3} ≍
eps^3` caps `p >= 3` and `rho >= rho_Hilbert` caps `q <= 2`, so `q/p <= 2/3` for
every admissible pair.  The phrasing still needs repair.  → C2.

**R6 — "The space is `L^3(R^3;R^3)`, a Bochner space over a Hilbert fibre; the
scalar Hanner power types do not transfer, so Finding 1 is about the wrong
space."**  *Failed.*  Proved the pointwise Clarkson inequality in a Hilbert
fibre for `p >= 2` (parallelogram + convexity of `u^{p/2}` + power-mean), giving
3-uniform convexity with the scalar Hanner modulus; sharpness from the isometric
scalar subspace; numerically verified over 4·10^5 random pairs, zero violations.
The step is true but unstated in §9.

**R7 — "Some other result of the same preprint subsumes T3.4, so 'this
particular paper is not the reason' is false."**  *Failed.*  Read §6 in full:
Theorem 6.1 is confined to `y ∈ C`, `v ∈ C^⊥`; the rest of §6 is the positive
cone of `(R^3,‖·‖_3)`; §5 is balls; §8 is Hilbert space.  Nothing addresses
`P_{G_3}` at a base point outside `G_3`.

**R8 — "The verdict over-concludes relative to the published JOTA text."**
*Succeeded, partially.*  Branch 3 (ordering corrected *and* proof repaired) is
not excluded by anything established, and is the branch a competent referee
would most plausibly produce.  The verdict is stated without the preprint
qualifier.  → C5.  Mitigated by the independent one-sided/two-sided mismatch,
which blocks subsumption in every branch.

**R9 — "'Verified numerically against the Hilbert moduli' is not a thing one can
verify numerically."**  *Succeeded, minor.*  → C7(ii).

**R10 — "The Pisier characterisation is wrong; Pisier's theorem might give
`p < q` under some convention."**  *Failed.*  Pisier's renorming produces
`rho <= C t^q` with `q > 1`, hence necessarily `q <= 2` since `rho >=
rho_Hilbert`; dually `delta >= c eps^p` with `p >= 2`.  Ordering is
`q <= 2 <= p`, the reverse of `1 < p < q`.  The attempt turned up a fact
favourable to the controller: the preprint cites **no** Pisier reference at all.

**R11 — "The vacuity is an artefact of the text-extraction of the PDF; the real
Definition 7.1 might read `delta(eps) >= a eps^p` only for small `eps`, or
`1 < p <= q`."**  *Failed.*  Read through a PDF reader, not a text proxy; the
range `(0,2]` is printed explicitly and `1 < p < q` appears **three times** in
§7 (the Pisier paragraph, Definition 7.1, and the proof's opening sentence "there
are 4 positive numbers a, b with a ≥ 1, b ≥ 1 and p, q with 1 < p < q").  A
uniform typo across three occurrences plus a proof that *uses* `q/p − 1 > 0` is
not credible.

**R12 — "Definition 7.1 is implicitly about an equivalent renorming (as the
Pisier sentence before it is), so the class is large after all."**  *Failed,
three ways.*  (i) Definition 7.1 as printed refers to `delta` and `rho` of `X`,
fixed at the head of §7 as "the modulus of convexity and modulus of smoothness
of X".  (ii) Even under a renorming, `delta <= 1` still kills (c) at `eps = 2`
with `a >= 1`, and Nordlander still kills `p < q`; renorming cannot evade a
bound that holds for every norm.  (iii) The metric projection is norm-dependent,
so a conclusion proved for a renormed space would not transfer to `P_{G_3}` in
the original `L^3` norm — the very object T3.4 is about.

---

## What I did NOT check

- **The published JOTA text**, DOI `10.1007/s10957-023-02329-7`.  Closed access;
  Springer redirects to authentication and Semantic Scholar reports no open PDF.
  Whether §7 survives, and in what form, remains genuinely open.  This is the
  single load-bearing gap and it is the same gap §7.1 named.
- **Nordlander's original 1960 text.**  Bibliographic identity verified on
  Project Euclid (Ark. Mat. 4 (1960) 15–17, DOI `10.1007/BF02591317`); full text
  behind registration.  The inequalities are taken on citation and verified
  numerically on random two-dimensional norms and on `L^3`.  The audit's
  conclusions do not depend on the attribution, because the endpoint argument
  (C3) replaces it.
- **Pisier's original 1975 text.**  Taken on citation plus one independent
  encyclopaedic restatement of the smoothness half.  Not read.
- **Li's §§1–5 and §8**, and Lemma 4.6 in particular.  I verified Definition 4.1
  verbatim (one-sided, norm limit) and read §§6–7 in full; the claim that Lemma
  4.6 gives only positive homogeneity is the file's §1.3 claim and I did not
  re-verify it.  My one-sided/two-sided remark rests on Definition 4.1 and on
  Theorem 7.2 asserting existence without representation, both of which I read.
- **2-uniform smoothness of `L^p(mu;H)` for `p >= 2`** (Figiel–Pisier).  Taken on
  citation; not load-bearing, since only the *lower* bound `rho >= rho_Hilbert`
  is used.
- **Any mathematical claim of the programme.**  I did not read, re-derive, or
  judge `hf26-temporal-continuation.tex` §3.  Nothing here promotes, discharges,
  or weakens any claim-graph node.
- **The other 14 non-claims in §6 and the remaining open items in §7.**  Item
  7.2 is answered for the preprint as a by-product (R7); items 7.3–7.8 were not
  touched.

---

**Non-claims.**  This review establishes no novelty, no priority, and no
mathematical result of the programme.  It makes no judgement on the correctness
of any other part of Li's paper, and it does not assert that the published JOTA
version contains the defect found in the preprint.  Corrections C1–C7 are
corrections to `hf26-prior-art-projection-differentiability.md` §9 and were
**not** applied; no file other than this one was edited.
