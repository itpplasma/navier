# CP02-2 REVIEW: audit of `research/evidence/cp02-continuation.md` (round 2)

MODE: REVIEW with the proof-audit discipline. Date: 2026-09-05. Owner: audit
lane for CP02-2, round 2. File written: this one only. Nothing in the audited
file, in `main.tex`, or in any other evidence file was edited.

## 0. Frozen candidate

| item | value |
|---|---|
| audited file | `/home/ert/proj/navier/research/evidence/cp02-continuation.md` |
| sha256 | `c6c2717e4f2751863095531a768d70981933134cdd1f088347a3bd5503167a54` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `fc1ee2bcc7afbbef43bb41a9c5070009034e603f` |
| candidate length | 1262 lines; LaTeX block extracted to 933 lines |
| manuscript compared against | `/home/ert/proj/navier-paper/main.tex`, 562 lines, read in full |
| records read in full | `cp01-manuscript-obligations.md`, `cp01-literature-statements.md`, `cp02-review-continuation.md` (round 1) |
| interfaces read | `cp02-local-theory.md` (`prop:localtheory`(i)–(vi), `cor:Lq`, `lem:sup-esssup`, `lem:global-smooth`, `lem:nu-scaling`, `eq:nu-map`), `cp02-energy-enstrophy.md` (`def:sobolev-constant`, `lem:sobolev`), `references.bib` |

The author's own summary was treated as untrusted. Every step below was
reconstructed from the LaTeX block itself; every constant and exponent was
recomputed from scratch, independently of round 1.

Primary sources opened **in this round** (not taken from the candidate, from
round 1, or from the CP01 records):

* Escauriaza–Seregin–Šverák, *Russian Math. Surveys* **58**:2 (2003) 211–250,
  English translation PDF, 10-page free portion (pp. 211–220), retrieved from
  mathnet.ru. Note for reproducibility: the documented URL
  `getFT.phtml?jrnid=rm&paperid=609&what=fullteng` now answers **302** to
  `/links/<hash>/rm609_eng.pdf` and the redirect must be followed **with the
  session cookie set by the 302**; a bare fetch of either URL returns
  mathnet's "page not found" HTML (this is why round 1's recipe no longer
  works verbatim). Pages **211, 212, 213, 214** read; p. 212 additionally
  **rendered as a page image at 144 dpi** — see §4.1, this is load-bearing.
* Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, in
  *The Millennium Prize Problems*, Clay 2006, **pp. 57–58** (the edition the
  manuscript's `references.bib` entry `Fefferman2000` actually points at,
  `MPPc.pdf`), and the standalone official-statement PDF
  `claymath.org/wp-content/uploads/2022/06/navierstokes.pdf`, **pp. 1–2**.
  Both read.

Not opened by this round (unchanged [MO] or accepted from round 1):
Rudin RCA 3rd ed. pp. 80–81 (round 1 [DI]), Lieb–Loss pp. 64–70 and TOC
(round 1 [DI]/TOC), Lieb–Loss Theorem 8.3 text, Nirenberg 1959 p. 125
(numdam's item URL for `ASNSP_1959_3_13__115_0` returned 404 in this round),
Stein–Weiss Ch. I, Folland, Galdi Ch. III.

---

## 1. VERDICT

**PASS.**

The single bad bridge of round 1 — the Sobolev inequality imported for the
class $D^1(\R^3)$ and applied to $H^1(\R^3)$ across an inclusion that *is*
the Sobolev embedding — is genuinely repaired, and the repair is correct as
written. (F3) is now stated only for real $g\in C_c^1(\R^3)$ with $C_S$ taken
from the energy lane's `def:sobolev-constant`; the inclusion $H^1\subset D^1$
is explicitly disclaimed; the extension actually used is proved as
`lem:sobolev-h1` (smooth representative from the $L^1$-Fourier bound,
truncation by $\chi_R$, Fatou), whose three steps I verified line by line and
which uses only $f\in H^3$ of its hypothesis $f\in\bigcap_kH^k$. The one
place it is invoked (`lem:serrin-enstrophy` Step 2, on the components
$g_{ij}=\partial_ju_i$) supplies exactly that hypothesis from (R1). Nothing
downstream moved: $C_*=\tfrac{256}{3125}C_S^3$ and the power $\nu^{-4}$ are
unchanged and both recompute correctly.

**No new bad bridge was found.** I re-derived every nontrivial implication of
the block (§4.2), re-read the printed ESS pages that the imported theorem and
its hypothesis class depend on (§4.1, including a page image, because the
decisive symbol $\overline{Q}_T$ is invisible to text extraction), re-read
Fefferman's clauses in the edition the bibliography cites, and ran seven
refutation attempts (§4.3); all seven failed.

There are **fourteen editorial issues** (§10), two of which are not cosmetic
and must be fixed before the block is spliced:

* **(E-1)** `\cite[p.~2]{Fefferman2000}` points at the wrong page. In the
  edition the manuscript's `references.bib` names (*The Millennium Prize
  Problems*, Clay 2006, pp. 57–67) Fefferman's condition (4) is on **p. 57**
  and (6), (7), alternative (A) are on **p. 58**. Verified this round.
* **(E-2)** (F3) simultaneously defines $C_S$ as "the constant of
  Definition~\ref{def:sobolev-constant}" — which fixes *some* admissible
  constant, Nirenberg's — and then asserts "The sharp value is
  $C_S=S_3^{-1/2}$". Those two sentences cannot both be true of one symbol.
  One-line fix in §5.

Both are D5-compliance defects (a primary-source pointer that does not
support the statement at the cited place; an internally inconsistent
definition of a named constant), not gaps in the mathematics, which is why
the verdict is PASS rather than REPAIR.

## 2. REVIEWED SCOPE

Reconstructed from its first nontrivial implication and checked in full:

* Conventions paragraph (Fourier convention, $R_iR_j=-\Delta^{-1}\partial_i\partial_j$,
  $\norm f_{H^1}^2=\norm f_2^2+(2\pi)^{-2}\norm{\nabla f}_2^2$, matrix-norm
  conventions) and the standard-fact list (F1)–(F6);
* the (R1)–(R4) abbreviation against `prop:localtheory`(iii),(iv),(v) and
  `cor:Lq` — this is the item round 1 asked round 2 to re-check;
* `lem:nu-normalisation` (i)–(vi) and the closing (vi)-of-`prop:localtheory`
  identification;
* `lem:hardy`; `lem:solenoidal-density` Steps 1–3; `lem:leray-hopf` Steps 0–6
  against the **printed** ESS (1.3)–(1.7);
* `thm:ess` and `rem:ess-norm` transcription fidelity, re-verified against the
  printed pages;
* `lem:l3-to-l5`;
* **`lem:sobolev-h1` Steps 1–3** (the round-2 focus);
* `lem:serrin-enstrophy` Steps 1–4;
* `thm:continuation` and its $\sup/\operatorname{ess\,sup}$ clause;
* `thm:conditional` Steps 0–5 against Fefferman (1)–(7) and alternative (A);
* `rem:gkp`;
* LaTeX self-containedness: every `\ref` target, every `\cite` key, the
  `\newtheorem` requirement, label collisions across all three lane files,
  and the retained-verbatim paragraphs against `main.tex`.

Out of scope (untouched by the candidate, not audited here): `prop:energy`,
`prop:scaling`, `prop:enstrophy`, `prop:ode`, `prop:pressure`,
`prop:lowpressure`, `hyp:highpressure`, `hyp:absorption`, `sec:compactness`,
`sec:quotient`, the X-1 paragraph, and `prop:localtheory` itself (its
*statement* was read for interface purposes; its proof was not audited).

## 3. FIRST BAD BRIDGE

**None.** The round-1 bridge is repaired and no other step fails.

For the record, the repaired bridge and why it is now sound. (F3) as it
now stands asserts $\norm g_6\le C_S\norm{\nabla g}_2$ only for real
$g\in C_c^1(\R^3)$, with the existence of $C_S$ delegated to the energy
lane's `def:sobolev-constant` (Nirenberg 1959 p. 125 (2.2) at
$n=3,j=0,m=1,r=q=2,a=1,p=6$; Mathlib
`eLpNorm_le_eLpNorm_fderiv_of_eq`). I checked that `def:sobolev-constant`
does state exactly the $C_c^1$ form the block quotes, including
$\norm{\nabla f}_2=\norm{\,|\nabla f|\,}_2$, so the interface is exact. The
parenthetical remark that Lieb–Loss's class $D^1(\R^3)$ contains
$C_c^\infty(\R^3)$ is now harmless: unlike $H^1\subset D^1$, the inclusion
$C_c^\infty\subset D^1$ is immediate under either candidate definition of
$D^1$ (a compactly supported bounded function is in $L^6$ and its gradient in
$L^2$; and $C_c^\infty$ is contained in any completion of itself). And the
inequality is no longer used through Lieb–Loss at all — `lem:sobolev-h1`
carries it from $C_c^\infty$ to $\bigcap_kH^k$ by a proof, not by a citation.

The nearest thing to a bridge failure I could construct is item (E-2) of §1:
if a reader takes "$C_S$ = the sharp value $S_3^{-1/2}$" literally, then
$C_S$ is no longer the constant `def:sobolev-constant` supplies, and (F3)
becomes an [MO] claim about Lieb–Loss Theorem 8.3 rather than a [DI]/[MO]
claim about Nirenberg. The block's own following clause ("only the existence
of $C_S$ is used below, not its value") shows the intent, and every use is
consistent with the weaker reading, so this is a wording defect, not a gap.

## 4. EVIDENCE

### 4.1 Source verification

**ESS (E1–E4): confirmed, and the one contested symbol confirmed by page
image.** The text layer of p. 212 reads "we mean a vector field
`v : QT → R3`" — i.e. **text extraction drops the overline**, because
`\overline{}` is drawn as a rule, not a character. Anyone re-checking this
from extracted text would wrongly "confirm" the CP01 record and wrongly
convict the candidate. I therefore rendered p. 212 at 144 dpi and read it:
the printed line is

> By a *Leray–Hopf weak solution* of the Cauchy problem (1.1), (1.2) in $Q_T$
> we mean a vector field $v\colon\overline{Q}_T\to\R^3$ such that

so the closure **is** printed (as $\overline{Q}_T$, bar over $Q$ only; the
block writes $\overline{Q_T}$ — immaterial). Round 1's finding stands, the
candidate is right, and `cp01-literature-statements` §3.1 (line 395,
"`v : Q_T → R^3`") is **wrong** and must be corrected by the literature lane.
Also confirmed verbatim from the same page: the definitions of
$\dot C_0^\infty$, $\mathring J$, $\mathring J{}^1_2$ (closures in $L_2$ and
$W^1_2$), $Q_T=\R^3\times{]0,T[}$; (1.3), (1.4) with "continuous on $[0,T]$",
(1.5) with $v\otimes v:\nabla w$ and test class $\dot C_0^\infty(Q_T)$, (1.6)
with "$\forall\,t_0\in[0,T]$", (1.7); the sentence "The definition still makes
sense for $T=+\infty$ …"; Theorem 1.1 with (1.8) $a\in\mathring J$. The block
reproduces all of these sign for sign. **New this round:** p. 212 also
carries, immediately after the closures, the parenthesis "(We use the standard
notation for the Lebesgue and Sobolev spaces.)" — this is ESS's own licence
for the block's identification $W^1_2=H^1(\R^3)^3$, and the block should quote
it (§10, item 5).

p. 213: the mixed-norm display is exactly the block's `eq:ess-norm`, including
$\operatorname*{ess\,sup}_{t\in]0,T[}\norm{f(\cdot,t)}_s$ for $l=+\infty$ and
"If $s=l$, then we briefly write $\norm f_{s,Q_T}$ instead of
$\norm f_{s,s,Q_T}$"; (1.13) is $v\in L_{3,\infty}(Q_T)$; Theorem 1.2 carries
(1.10) $\tfrac3s+\tfrac2l=1$, $s\in{]3,+\infty]}$ (so `rem:gkp`'s "$s=l=5$"
does satisfy it: $\tfrac35+\tfrac25=1$, $5\in{]3,\infty]}$). Theorem 1.2 *does*
assume (1.8); Theorem 1.3 *does not* — the block's remark about this is
correct.

p. 214, Theorem 1.3, printed: "Suppose that $v$ is a weak Leray–Hopf solution
of the Cauchy problem (1.1), (1.2) in $Q_T$ and $v$ satisfies the additional
condition (1.13). Then $v\in L_5(Q_T)$, (1.14) and hence it is smooth and
unique on $Q_T$." The block's `thm:ess` is **verbatim**. The unnumbered
classical-form prose before it is also quoted verbatim in `rem:ess-norm`.

p. 211, (1.1)–(1.2), printed:
$\partial_tv+\operatorname{div}v\otimes v-\Delta v=-\nabla p$,
$\operatorname{div}v=0$, $v(x,0)=a(x)$, unit viscosity. Exactly as the block
states. Note the definition of a Leray–Hopf weak solution never mentions $p$,
so the block need not (and does not) match ESS's pressure normalisation —
this is why `lem:leray-hopf` has nothing to check about $q$ beyond
$\int\nabla q\cdot w=0$.

**Fefferman (E7): confirmed, with a page correction.** Read in both editions.
(4) $|\partial_x^\alpha u^\circ(x)|\le C_{\alpha K}(1+|x|)^{-K}$ on $\R^n$,
for any $\alpha$ and $K$; (6) $p,u\in C^\infty(\R^n\times[0,\infty))$;
(7) $\int_{\R^n}|u(x,t)|^2dx<C$ for all $t\ge0$; and (A) "Take $\nu>0$ and
$n=3$. Let $u^\circ(x)$ be any smooth, divergence-free vector field satisfying
(4). Take $f(x,t)$ to be identically zero. Then there exist smooth functions
$p(x,t)$, $u_i(x,t)$ on $\R^3\times[0,\infty)$ that satisfy (1), (2), (3),
(6), (7)." So the block's clause list is exactly (A)'s list, and its statement
that (5) is "vacuous" is right — (5) does not even appear in (A). **But** in
the `MPPc.pdf` edition that `references.bib` cites (pp. 57–67), (4) is on
**p. 57**, not p. 2; p. 2 is the standalone official-statement PDF's
pagination (where (4) sits on p. 1, not p. 2, either). See §10 item 1.

**Interfaces (not external, but checked).** `prop:localtheory`(iii) gives
$u,p\in C^j([0,T];H^k)$ for all $j,k$ with all derivatives bounded on
$[0,T]\times\R^3$; `cor:Lq` gives precisely the six fields
$u,\nabla u,\Delta u,\partial_tu,p,\nabla p$ in $C([0,T];L^q)$, $2\le
q\le\infty$; (iv) gives the pointwise equation, $\nabla\cdot u=0$,
$u(0)=u_0$, $p=R_iR_j(u_iu_j)$; (v) gives
$\lim_{t\uparrow T_*}\norm{u(t)}_{H^1}=+\infty$; (vi) gives exactly the
scaling identification and $T_*(\nu,u_0)=\nu^{-1}T_*(1,\nu^{-1}u_0)$, whence
$T_*(1,a)=\nu T_*=S_*$ as the block asserts. `def:sobolev-constant` is the
$C_c^1$ form. `lem:global-smooth` and `lem:sup-esssup` say what the block
attributes to them. **The (R1)–(R4) mapping is therefore correct**, including
the point round 1 flagged: (R1) bundles the $L^q$ statement, and the block now
attributes that half to `cor:Lq` explicitly.

**Label and reference hygiene (checked mechanically).** All 13 external
`\ref`/`\eqref` targets in the block (`prop:localtheory`, `cor:Lq`,
`lem:nu-scaling`, `lem:global-smooth`, `lem:sup-esssup`, `def:sobolev-constant`,
`prop:energy`, `def:target`, `eq:NS`, `eq:nu-map`, `eq:pressure-consequence`,
`hyp:absorption`, `hyp:highpressure`) exist in `main.tex` or in the two other
lane files. All five `\cite` keys (`Tao2013`, `ESS2003`, `GKP2013`,
`Fefferman2000`, `Kato1984`) exist in `references.bib`. None of the block's
sixteen new labels collides with a label in `cp02-local-theory.md` or
`cp02-energy-enstrophy.md` — the round-1 collision `eq:enstrophy-identity` is
gone. The retained-verbatim `hyp:critical` and the two following paragraphs
are byte-identical in substance to `main.tex` lines 469–500. A grep for
"standard / well known / easy to see / clearly / obvious / straightforward /
routine" in the block returns two hits, both benign (the heading "Standard
facts used" and "as is standard" describing a *notational* reading).

### 4.2 Independent recomputation (this round, from scratch)

**`lem:sobolev-h1` (the round-2 focus).** Step 1: with the weight
$w=(1+|\xi|^2)^{-2}$, Cauchy–Schwarz gives
$\int|\xi|^m|\hat f|\le(\int w)^{1/2}(\int w^{-1}|\xi|^{2m}|\hat f|^2)^{1/2}$;
$\int_{\R^3}w=4\pi\int_0^\infty r^2(1+r^2)^{-2}dr=4\pi\cdot\tfrac\pi4=\pi^2$,
so the prefactor is $\pi$; and
$w^{-1}|\xi|^{2m}=(1+|\xi|^2)^2|\xi|^{2m}\le(1+|\xi|^2)^{m+2}$, giving
$\int|\xi|^m|\hat f|\le\pi\norm f_{H^{m+2}}$ — exactly as printed. Hence
$(2\pi i\xi)^\alpha\hat f\in L^1\cap L^2$ for every $\alpha$, so $F$ is
$C^\infty$ with $\partial^\alpha F=\mathcal F^{-1}[(2\pi i\xi)^\alpha\hat f]$
bounded by $\norm{(2\pi\xi)^\alpha\hat f}_1$; $F=f$ and $\partial_jF=\partial_jf$
a.e. by (F1)(c),(d); $F$ real by $\hat f(-\xi)=\overline{\hat f(\xi)}$.
Step 2: $\chi_RF\in C_c^\infty$ is real, so (F3) applies, and
$\norm{\nabla(\chi_RF)}_2\le\norm{\chi_R\nabla F}_2+\norm{F\nabla\chi_R}_2
\le\norm{\nabla f}_2+R^{-1}\norm{\nabla\chi}_\infty\norm f_2$. Step 3: Fatou
on $|\chi_RF|^6$ (pointwise $\chi_RF\to F$ since $\chi_R(x)=1$ once
$R\ge|x|$) gives $\norm F_6\le\liminf_R\norm{\chi_RF}_6\le C_S\norm{\nabla f}_2$.
Correct. Only $f\in H^3$ is used (I checked: $m=0$ needs $H^2$, $m=1$ needs
$H^3$); stating it for $\bigcap_kH^k$ is a harmless over-hypothesis matching
the use site.

**`lem:serrin-enstrophy`.** $Y'=2\langle\nabla u,\nabla\partial_tu\rangle$
from the $C^1$-curve identity; Plancherel gives
$\sum_j\int4\pi^2\xi_j^2\hat u_i\overline{(\partial_tu)^\wedge_i}
=-\int(-4\pi^2|\xi|^2\hat u_i)\overline{(\partial_tu)^\wedge_i}$, i.e.
$\langle\nabla u,\nabla\partial_tu\rangle=-\langle\Delta u,\partial_tu\rangle$.
Pressure term: $\overline{2\pi i\xi_i\hat p}=-2\pi i\xi_i\overline{\hat p}$,
so $\langle\Delta u,\nabla p\rangle=\int4\pi^2|\xi|^2\overline{\hat p}
\sum_i2\pi i\xi_i\hat u_i=\int4\pi^2|\xi|^2\overline{\hat p}\,
(\nabla\cdot u)^\wedge=0$; the sign works out. Substituting
$\partial_tu=\nu\Delta u-(u\cdot\nabla)u-\nabla p$ gives
$\tfrac12Y'+\nu\norm{\Delta u}_2^2=\langle(u\cdot\nabla)u,\Delta u\rangle$.
Hölder: $\tfrac15+\tfrac3{10}+\tfrac12=\tfrac2{10}+\tfrac3{10}+\tfrac5{10}=1$.
Interpolation: $\int f^{10/3}=\int f^{4/3}f^2\le(\int f^2)^{2/3}(\int f^6)^{1/3}$
by Hölder at $(\tfrac32,3)$, so
$\norm f_{10/3}\le\norm f_2^{2/5}\norm f_6^{3/5}$ ($\tfrac43\cdot\tfrac3{10}=\tfrac25$,
$2\cdot\tfrac3{10}=\tfrac35$). Componentwise Sobolev:
$\norm{\nabla u}_6^2=\norm{\sum g_{ij}^2}_3\le\sum\norm{g_{ij}}_6^2
\le C_S^2\sum\norm{\nabla g_{ij}}_2^2=C_S^2\norm{\nabla^2u}_2^2$.
Plancherel: $\sum_{i,j,k}(2\pi\xi_j)^2(2\pi\xi_k)^2|\hat u_i|^2
=\sum_i(4\pi^2|\xi|^2)^2|\hat u_i|^2$, so
$\norm{\nabla^2u}_2=\norm{\Delta u}_2$. Product:
$|\langle(u\cdot\nabla)u,\Delta u\rangle|\le C_S^{3/5}\norm u_5Y^{1/5}
\norm{\Delta u}_2^{8/5}$ ($\tfrac35+1=\tfrac85$). Young at $(\tfrac54,5)$
with $a=(\tfrac{5\nu}4)^{4/5}\norm{\Delta u}_2^{8/5}$,
$b=(\tfrac{5\nu}4)^{-4/5}C_S^{3/5}\norm u_5Y^{1/5}$:
$\tfrac45a^{5/4}=\nu\norm{\Delta u}_2^2$ and
$\tfrac15b^5=\tfrac15(\tfrac4{5\nu})^4C_S^3\norm u_5^5Y
=\tfrac15\cdot\tfrac{256}{625}\nu^{-4}C_S^3\norm u_5^5Y
=\tfrac{256}{3125}C_S^3\nu^{-4}\norm u_5^5Y$, so $C_*=\tfrac{256}{3125}C_S^3$
exactly. Gronwall: $Y'\le2C_*\nu^{-4}\norm u_5^5Y$, $(Ye^{-G})'\le0$,
$Y\le Y(0)e^{G_T}$, and the square root halves the exponent to
$C_*\nu^{-4}\int_0^T\norm u_5^5$ — `eq:serrin-bound` as printed.

**`lem:nu-normalisation`.** $\partial_sv=\nu^{-2}(\partial_tu)$,
$(v\cdot\nabla)v=\nu^{-2}(u\cdot\nabla)u$, $\nabla q=\nu^{-2}\nabla p$,
$\Delta v=\nu^{-2}(\nu\Delta u)$; the unit-viscosity equation follows, and
$\partial_s^jv=\nu^{-1-j}\partial_t^ju$ matches `lem:nu-scaling`(a). Energy:
$\nu\int_0^{s/\nu}\norm{\nabla u}_2^2d\tau
=\nu\cdot\nu^{-1}\int_0^s\norm{\nabla u(\sigma/\nu)}_2^2d\sigma
=\nu^2\int_0^s\norm{\nabla v}_2^2d\sigma$; dividing the identity by $\nu^2$
gives (v). $\int_0^{S_*}\norm{v}_5^5ds=\nu\cdot\nu^{-5}\int_0^{T_*}\norm u_5^5dt
=\nu^{-4}\int_0^{T_*}\norm u_5^5dt$ — the $\nu^{-4}$ is right.

**`lem:hardy`.** $\tfrac{d}{dr}(rF^2)=F^2-2rFg$ gives
$\int_\alpha^RF^2=[rF^2]_\alpha^R+2\int_\alpha^RrFg$;
$F(R)\le R^{-1/2}(\int_R^\infty s^2g^2)^{1/2}$ so
$RF(R)^2\le\varepsilon_R\to0$; Cauchy–Schwarz on $\int rFg$ gives
$X^2\le\varepsilon_R+2M_\omega X$, so
$X\le M_\omega+\sqrt{M_\omega^2+\varepsilon_R}\to2M_\omega$. Constant $2$ is
the sharp $2/(n-2)$ at $n=3$. $|(\omega\cdot\nabla)A|\le|\nabla A|$
(Cauchy–Schwarz componentwise, $|\omega|=1$), and polar coordinates convert
$\int_0^\infty|A(r\omega)|^2dr$ into $\int|A|^2/|x|^2dx$ because the $r^{-2}$
cancels the Jacobian $r^2$. Correct.

**`lem:solenoidal-density`.**
$2\pi i\,\xi\times\hat A=-\xi\times(\xi\times\hat v)/|\xi|^2
=-(\xi(\xi\cdot\hat v)-|\xi|^2\hat v)/|\xi|^2=\hat v$ a.e. under
$\xi\cdot\hat v=0$. $\int_{|\xi|<1}|\xi|^{-2}d\xi=4\pi$, giving
$\norm{\hat A}_1\le(2\pi)^{-1}((4\pi)^{1/2}\norm v_2+\pi\norm v_{H^2})$.
$\norm{\nabla A}_2^2\le\sum_j\int\xi_j^2|\hat v|^2/|\xi|^2=\norm v_2^2$.
Note (and this is right) the block never claims $A\in L^2$: $\hat A$ can fail
to be square-integrable near $\xi=0$ (take $\hat v\sim|\xi|^{-1/2}$, which is
in $L^1\cap L^2$ while $|\hat v|^2|\xi|^{-2}\sim|\xi|^{-3}$ is not
integrable), and the block only ever uses $\partial^\alpha A$, $|\alpha|\ge1$,
whose symbols are in $L^1\cap L^2$. Cutoff errors: $|A|\le2R|A|/|x|$ on the
annulus gives $\norm A_{L^2(\text{ann})}\le2R\eta(R)$ with
$\eta(R)=\norm{A/|x|}_{L^2(|x|\ge R)}\le2\norm v_2$, so the four gradient
terms are $o(1)$, $O(R^{-1})$, $O(R^{-1})$, $O(R^{-1})$ as printed, and the
Hardy detour is indispensable (a bare $\norm A_\infty$ bound gives
$R^{-1}\cdot R^{3/2}\to\infty$). $\mathring J{}^1_2\subset\mathring J$ because
$W^1_2$-convergence implies $L_2$-convergence.

**`lem:leray-hopf`.** Testing the equation against $\varphi\in\dot C_0^\infty$
gives $\langle v,\Delta\varphi\rangle+\int v_iv_j\partial_j\varphi_i$ with the
pressure term killed by $\nabla\cdot\varphi=0$, hence
$L_\varphi=\norm a_2\norm{\Delta\varphi}_2+\norm a_2^2\norm{\nabla\varphi}_\infty$
(using $|v\otimes v:\nabla\varphi|\le|v|^2|\nabla\varphi|$). Lipschitz +
$\varepsilon$-density in $\mathring J$ + $\Pi$ gives $\ell$ bounded, Riesz
gives $v_*$, $(\mathring J^\perp)^\perp=\mathring J$ gives
$v_*\in\mathring J$, and $\norm{v_*}_2^2=\lim\langle v(s),v_*\rangle$ gives
$\norm{v_*}_2\le\liminf\norm{v(s)}_2$. (1.5): the printed identity is
reproduced term by term, with
$\int v_j(\partial_jv_i)w_i=-\int v_iv_j\partial_jw_i$ (valid because
$\partial_jv_j=0$) and $-\int\Delta v\cdot w=\int\nabla v:\nabla w$; the test
function's support in $K\times[t_1,t_2]$ with $0<t_1<t_2<T\le S_*$ keeps
everything inside the region where $v,q$ are $C^\infty$. (1.6) at $t_0=S_*$
follows from the liminf plus the monotone limit of the energy identity. The
endpoint value enters only (1.4) and (1.6), both of which the block verifies,
and is irrelevant to (1.3) and (1.5) (a null set / the open cylinder).

**`thm:conditional` Step 0.** Both directions of "(4) for all $\alpha,K$
$\iff$ $u_0\in\mathcal S$" check out, including the use of
$(1+|x|)^{-\lceil K\rceil}\le(1+|x|)^{-K}$ for real $K\ge0$.

**Pressure identification.** $R_iR_j$ has multiplier
$(-i\xi_i/|\xi|)(-i\xi_j/|\xi|)=-\xi_i\xi_j/|\xi|^2$;
$-\Delta^{-1}\partial_i\partial_j$ has
$-(-(4\pi^2|\xi|^2)^{-1})(-4\pi^2\xi_i\xi_j)=-\xi_i\xi_j/|\xi|^2$. Identical,
as (D1) requires. $\norm f_{H^1}^2=\norm f_2^2+(2\pi)^{-2}\norm{\nabla f}_2^2$
is the exact identity for the block's weight convention.

**Sharp-constant algebra (for E-2 only).** $S_3=\tfrac{n(n-2)}4|\mathbb S^n|^{2/n}$
at $n=3$ with $|\mathbb S^3|=2\pi^2$ is $\tfrac34(2\pi^2)^{2/3}
=3\cdot2^{-4/3}\pi^{4/3}=3(\pi/2)^{4/3}=5.4785\ldots$, so
$S_3^{-1/2}=0.4273\ldots$; the block's algebra is right, its *attribution* is
the problem (§1 E-2).

### 4.3 Refutation attempts (seven; all failed)

1. **Kill `lem:sobolev-h1` by a counterexample.** Any real
   $f\in\bigcap_kH^k$ with $\norm f_6>C_S\norm{\nabla f}_2$ would do. None
   exists (the inequality is true on $H^1$), and more usefully: the proof
   never needs it to be true — it derives it. Tried instead to break Step 2 by
   making $\norm{F\nabla\chi_R}_2$ non-vanishing: it is bounded by
   $R^{-1}\norm{\nabla\chi}_\infty\norm f_2$ with $\norm f_2<\infty$ from
   $f\in H^0$, so no. Tried to break Step 3 by choosing $f\notin L^6$ a
   priori: Fatou is applied to $|\chi_RF|^6$, whose integrals are finite by
   Step 2, and yields finiteness of $\norm F_6$ as a *conclusion*; no
   circularity. Failed.
2. **Hidden circularity through Lieb–Loss.** Traced every use of (F3): the
   only one is Step 2 of `lem:serrin-enstrophy`, via `lem:sobolev-h1`, on
   $C_c^\infty$ inputs. The $D^1$ sentence is inert. Failed.
3. **Wider ESS test class.** If $\dot C_0^\infty(Q_T)$ did *not* require
   $x$-solenoidality, (1.5) as printed (no pressure term) would be false for
   the block's $v$, and the verification would collapse. But ESS's own
   $\dot C_0^\infty$ on $\R^3$ is defined as solenoidal (page image, §4.1), so
   the dotted notation carries solenoidality; no wider reading is available.
   Failed — though the block's justification ("any narrower test class is
   contained in it") argues the wrong direction; see §10 item 4.
4. **Endpoint of `lem:leray-hopf` unnecessary.** Argued that ESS's class lives
   on the open cylinder so Step 1 is decoration. Refuted by the page image:
   $v\colon\overline{Q}_T\to\R^3$, and (1.4), (1.6) quantify over
   $t_0\in[0,T]$. Step 1 is required. Failed.
5. **Preserved Schwartz decay in time (forbidden by D2).** Traced every appeal
   to decay: `lem:hardy` and `lem:solenoidal-density` are applied to
   $v(s)\in\bigcap_kH^k$ and to the potential $A$ built from it (whose decay
   is *proved*, via the $L^1$-density argument, not assumed);
   $\mathcal S$ occurs only at $t=0$ (`lem:nu-normalisation`(i),
   `thm:conditional` Step 0) and in the throwaway last sentence of
   `lem:solenoidal-density`. No violation. Failed.
6. **Uniqueness smuggled in.** ESS Theorem 1.3 is applied to the transported
   classical branch *itself*, which the block proves to be a Leray–Hopf weak
   solution; the return path to $H^1$ is the manuscript-owned
   `lem:serrin-enstrophy`. The "smooth and unique on $Q_T$" clause of
   Theorem 1.3 is explicitly not used. `prop:localtheory`(vi) is recorded and
   declared unused. Failed — the (D3) route is clean.
7. **$\nu$-power or constant wrong.** Recomputed $\nu^{-4}$ twice (once from
   the norm transport, once from the Young step) and $C_*$ once; both agree
   with the block. Failed.

## 5. REPLACEMENT ARGUMENT

Not applicable: the verdict is PASS, so there is no replacement text for the
manuscript. For completeness, the two mandatory fixes of §1 are one-line
LaTeX edits inside the candidate's own block (they change no mathematics and
no constant):

```latex
% (E-1)  In thm:conditional, Step 0: replace
%   \cite[p.~2]{Fefferman2000}
% by
%   \cite[p.~57]{Fefferman2000}
% (condition (4) sits on p.~57 of the Millennium Prize Problems volume, the
%  edition the bibliography entry names; (6), (7) and alternative~(A) are on
%  p.~58, so the citation in Steps~2--4 -- if one is added -- is p.~58.)

% (E-2)  In (F3): replace the sentence
%   The sharp value is $C_S=S_3^{-1/2}$ with
%   $S_3=\tfrac34(2\pi^2)^{2/3}=3(\pi/2)^{4/3}$ (Lieb--Loss, ...
% by
%   The least admissible constant in this inequality is $S_3^{-1/2}$ with
%   $S_3=\tfrac34(2\pi^2)^{2/3}=3(\pi/2)^{4/3}$ (Lieb--Loss, \emph{Analysis},
%   2nd ed., Theorem~8.3, ``Sobolev's inequality for gradients'', p.~202,
%   stated there for the class $D^1(\R^3)$ of \S8.2, p.~201, which contains
%   $C_c^\infty(\R^3)$ because a compactly supported bounded function lies in
%   $L^6$ and its gradient in $L^2$); we do not use this value, only the
%   existence of the constant $C_S$ fixed by
%   Definition~\ref{def:sobolev-constant}, and $C_*$ below is expressed
%   through that $C_S$.
```

## 6. CONDITIONAL SUFFIX THAT SURVIVES

Given

* `prop:localtheory` delivering clauses (R1)–(R4) of (D2) — concretely
  (iii)+`cor:Lq`, the preamble+(iv), (iv), (v) — and `lem:global-smooth`
  (local-theory lane);
* `prop:energy` and `def:sobolev-constant` (energy lane);

the block proves, for the unforced system on $\R^3$ with arbitrary $\nu>0$
and divergence-free Schwartz datum, on the classical branch:

1. the $\nu$-normalised branch $v$ is a Leray–Hopf weak solution in the exact
   printed ESS sense (1.3)–(1.7) on every $Q_T$ with $T\le S_*=\nu T_*<\infty$,
   endpoint included, with datum $a=\nu^{-1}u_0\in\mathring J{}^1_2$;
2. $T_*<\infty$ and $\sup_{t<T_*}\norm{u(t)}_3<\infty$ imply
   $u\in L^5(\R^3\times(0,T_*))$, via ESS Theorem 1.3 — the only imported
   theorem, its hypothesis class verified clause by clause against the printed
   definition, with no imported uniqueness theorem;
3. every real $f\in\bigcap_kH^k(\R^3)$ satisfies
   $\norm f_6\le C_S\norm{\nabla f}_2$ (`lem:sobolev-h1`);
4. $\int_0^T\norm u_5^5<\infty$ implies
   $\sup_{t<T}\norm{\nabla u(t)}_2\le\norm{\nabla u_0}_2
   \exp\bigl(\tfrac{256}{3125}C_S^3\nu^{-4}\int_0^T\norm u_5^5\bigr)$
   and hence $\sup_{t<T}\norm{u(t)}_{H^1}<\infty$;
5. hence `thm:continuation` in the C-0 shape
   "$T_*<\infty\Rightarrow\sup_{0<t<T_*}\norm{u(t)}_3=\infty$", with
   $\sup=\operatorname{ess\,sup}=\sup_{[0,T_*)}$ justified from
   $u\in C([0,T];L^3)$;
6. hence `hyp:critical` $\Rightarrow$ `def:target`, with Fefferman's (1), (2),
   (3), (6), (7) each checked, (5) vacuous under (A), and the datum class (4)
   identified with $\mathcal S(\R^3)^3$ in both directions.

`hyp:critical` remains an unproved hypothesis. Nothing above bears on
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION or NS-R3.

## 7. UNNECESSARY DEPENDENCIES

* **`lem:sup-esssup` (local-theory lane).** Cited as "cf." at the end of
  `thm:continuation`, but the block's own proof of the
  $\sup/\operatorname{ess\,sup}$ clause is complete. The cross-reference can
  stay as a pointer or be dropped; it carries no weight.
* **`prop:localtheory`(vi) / `lem:nu-scaling`.** The block itself says
  `lem:nu-normalisation`'s final assertion "is not used below", and (i)–(iv)
  duplicate `lem:nu-scaling`(a)–(d). Only (v) and (vi) are load-bearing. The
  integrator's deduplication is therefore free of mathematical risk. One
  caution: if the integrator drops `eq:nu-map` in favour of
  `eq:nu-normalization`, the block's sentence "The substitution
  \eqref{eq:nu-normalization} below is the map \eqref{eq:nu-map} of the
  local-theory section" must go too, or the reference dangles.
* **`lem:sobolev-h1` vs the energy lane's `lem:sobolev`.** Genuinely
  redundant: `lem:sobolev` proves the inequality on all of $H^1(\R^3)^m$.
  Keeping `lem:sobolev-h1` makes the section self-contained; replacing its
  single use by `lem:sobolev` with $m=1$ leaves $C_*$ unchanged. Either is
  sound. (Do not do both — two lemmas with the same content in one paper.)
* **`rem:gkp`, `\cite{Kato1984}`, and the Lieb–Loss sharp-constant
  parenthetical** are decorative by design.
* **(F4) (Riesz representation).** Used only in `lem:leray-hopf` Step 1. It
  could be replaced by weak-$*$ sequential compactness, but not more cheaply,
  and the current route avoids a subsequence.
* Nothing else can be removed without cost. `lem:hardy` in particular is
  load-bearing (refutation attempt 2 of round 1, re-confirmed here).

## 8. NON-CLAIMS (of this audit)

No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result is
asserted, approached, or judged closer. `hyp:critical`, `hyp:absorption`,
`hyp:highpressure` and `eq:quotient-gap` remain unproved and untouched. This
audit does **not** verify `prop:localtheory` (only its statement, as an
interface), `prop:energy`, `prop:pressure`, `prop:lowpressure`,
`prop:enstrophy`, `prop:scaling`, `prop:ode`, `sec:compactness`,
`sec:quotient`, or the X-1 paragraph. No claim is made that the audited block
solves any part of the Millennium problem; it is a conditional continuation
section resting on one imported literature theorem. Sources **not** read in
their primary text by this round: Lieb–Loss (any page), Rudin, Nirenberg 1959,
Stein–Weiss Ch. I, Folland, Galdi, Tao 2013, GKP 2013 — for these I rely on
round 1's [DI] findings (Rudin pp. 80–81, Lieb–Loss pp. 64–70 and TOC) and on
the CP01 record (Tao, GKP), and I inherit their [MO] tags unchanged. The
sharp-constant algebra in §4.2 is my own computation, not a reading of
Lieb–Loss Theorem 8.3.

## 9. REOPENING CONDITION

Reopen if any of the following changes:

1. `prop:localtheory` is written with a package weaker than (R1)–(R4) — in
   particular if the normalised pressure leaves the $C^j_tH^k$ statement (used
   in `lem:nu-normalisation`(ii), `lem:leray-hopf` Steps 1 and 4,
   `lem:serrin-enstrophy` Step 1), if `cor:Lq` drops any of the six fields or
   narrows $2\le q\le\infty$ (the block needs $q=3,5,\infty$), or if the
   blow-up alternative is stated in a norm not equivalent to $H^1$;
2. the local-theory lane renumbers or re-splits clauses (iii)–(vi), or drops
   `lem:global-smooth`;
3. the energy lane changes `def:sobolev-constant`'s class away from
   $C_c^1(\R^3)$ real-valued, or its $\norm{\nabla f}_2$ convention — the
   first would break `lem:sobolev-h1` Step 2, the second changes $C_*$
   numerically (never the $\nu^{-4}$);
4. the pressure lane changes `eq:pressure-consequence` away from the
   integrated P-3 form used by the retained paragraph after `hyp:critical`;
5. the `Fefferman2000` bibliography entry is changed from the *Millennium
   Prize Problems* chapter (pp. 57–67) to the standalone official-statement
   PDF, in which case the page pointer of §5 (E-1) must become p. 1;
6. the ESS pagination used here (pp. 211–214 of the *Russian Math. Surveys*
   English translation) is replaced by the Russian original's numbering, in
   which case every `\cite[p.~…]{ESS2003}` must be re-pinned;
7. `lem:sobolev-h1` is deleted in favour of the energy lane's `lem:sobolev`
   — then the *statement* used at `lem:serrin-enstrophy` Step 2 must be
   checked to cover real scalar $f\in\bigcap_kH^k$ with the same $C_S$.

## 10. MINOR EDITORIAL ISSUES FOR THE INTEGRATOR

1. **(mandatory, E-1)** `\cite[p.~2]{Fefferman2000}` in `thm:conditional`
   Step 0 → **p. 57**. Verified against `MPPc.pdf` (the bibliography's URL):
   condition (4) is on p. 57, (6), (7) and alternative (A) on p. 58. The
   CP01 record's "PDF pp. 1–2" refers to a *different* edition than the bib
   entry; the literature lane should reconcile the two (either add a second
   bib entry for the standalone statement, or re-pin all Fefferman page
   references to 57–58).
2. **(mandatory, E-2)** (F3): "The sharp value is $C_S=S_3^{-1/2}$" contradicts
   "$C_S$ = the constant of Definition~\ref{def:sobolev-constant}". Use the
   §5 wording ("the least admissible constant in this inequality is
   $S_3^{-1/2}$ …; we use only the existence of the $C_S$ fixed by
   Definition~\ref{def:sobolev-constant}").
3. `lem:sobolev-h1` Step 3 applies Fatou along the continuous parameter
   $R\to\infty$. Add "along $R\in\mathbb N$" (or "$R_n\to\infty$"), since
   (F5)/Fatou is a statement about sequences.
4. `lem:leray-hopf`'s justification of the $\dot C_0^\infty(Q_T)$ reading
   argues in the wrong direction: "any narrower test class is contained in it"
   protects against a *narrower* intended class, whereas the risk is a
   *wider* one (without $x$-solenoidality, (1.5) would carry a pressure term
   and would be false as printed). Replace by the correct argument, which is
   available: ESS *define* $\dot C_0^\infty$ on $\R^3$ to consist of solenoidal
   fields (p. 212), so any reading of $\dot C_0^\infty(Q_T)$ inherits
   solenoidality in $x$; the only latitude is whether it is required for each
   $t$ or in a space-time sense, and the block verifies the former, which is
   the weaker requirement on $w$ and hence the stronger verification.
5. The block asserts "$W^1_2=H^1(\R^3)^3$ with the norm
   $\norm w_{W^1_2}=(\norm w_2^2+\norm{\nabla w}_2^2)^{1/2}$" without saying
   why it may. ESS licence this on the same page: quote their parenthesis
   "(We use the standard notation for the Lebesgue and Sobolev spaces.)"
   immediately after the closures sentence. (Also note in half a sentence that
   the closure $\mathring J{}^1_2$ is unchanged by passing to an equivalent
   $W^1_2$ norm, since the block's own $H^1$ weight convention differs from
   the $W^1_2$ one by the factor $(2\pi)^{-1}$ on the gradient term.)
6. `lem:solenoidal-density` Step 3 differentiates $(\chi_R-1)v$ with $v$ only
   known to be weakly differentiable. Either invoke the product rule for a
   $C^\infty$ multiplier with bounded derivatives against an $H^1$ function,
   or (cheaper, and already available) note that $v$ has a $C^\infty$
   representative by the argument of `lem:sobolev-h1` Step 1, so the product
   rule is classical.
7. `lem:nu-normalisation`(iii) is justified by "there is no change of the
   spatial variable, so every spatial norm of $v(s)$ is $\nu^{-1}$ times the
   same norm of $u(s/\nu)$". True, but the sentence as written speaks about
   norms *of $v$*, while the claim also covers $\norm{\nabla v(s)}_2$. Add
   "and likewise $\nabla v(\cdot,s)=\nu^{-1}(\nabla u)(\cdot,s/\nu)$".
8. §1 of the candidate says the block "replaces the whole of the manuscript's
   Section 5 … to the end of the proof of `thm:conditional`", but the block
   continues past that point with `rem:gkp`. Correct the description (the
   remark is new material appended after `thm:conditional`).
9. §1's cross-reference list names `prop:lowpressure`; the block never
   references it. Trim.
10. Conventions paragraph: "the memberships in (R1) and the divergence
    statement (R4) do not depend on the choice" — "divergence" here means
    "divergence to $+\infty$", one line after $\nabla\cdot u=0$ has been
    discussed. Reword to "the blow-up statement (R4)".
11. `thm:ess`'s environment is `theorem`, so it will print as e.g.
    "Theorem 5.7" beside the quoted "Theorem 1.3". The bracket
    "[…, Theorem~1.3 of \cite{ESS2003}; quoted, not proved here]" handles it;
    no change needed, recorded so a referee query is anticipated.
12. `rem:ess-norm` and the retained paragraph after `hyp:critical` both make
    the "not the weak Lorentz space" point once each in the integrated text —
    check after the splice that the deleted `main.tex` sentence is not
    reinstated a second time.
13. Preamble: only `\newtheorem{lemma}[theorem]{Lemma}` is required by this
    block (verified: no `definition`, `corollary`, or `example` environment
    is used, and `\R`, `\norm`, `\operatorname*`, `\mathring`, `\mathbb C`,
    `\qedhere` are all already available). The local-theory lane needs
    `corollary` and `definition` in addition; one shared block of
    `\newtheorem` lines suffices.
14. Carried forward from round 1 §10, still outstanding and **not** this
    lane's to fix: (a) `cp01-literature-statements` §3.1 line 395 must read
    $v\colon\overline{Q}_T\to\R^3$ (independently re-confirmed here from the
    page image); (b) `main.tex` lines 51–52 inside `premise:local`
    ("Persistence of higher Sobolev regularity and uniqueness identify this
    branch with the maximal mild solutions used in the continuation theorem
    below") is false as a description of the (D3) proof and must be replaced
    by the local-theory lane's §2.1 paragraph; (c) the "Proof boundary"
    section must name `lem:leray-hopf` and `lem:serrin-enstrophy` as
    manuscript-owned and load-bearing (the candidate supplies suitable
    wording); (d) `cp02-local-theory.md` and `cp02-energy-enstrophy.md` both
    define `\label{lem:duality}` — one must be renamed by those lanes.

---

## 11. Obligations status after this audit

Discharged by the candidate, verified here, no repair required:

* **C-0** — `thm:continuation` in the required shape; contrapositive as
  `eq:endpoint`; $\operatorname{ess\,sup}\to\sup$ justified from
  $u\in C([0,T];L^3)$ and proved in place (not merely delegated).
* **C-2** — replaced by the (D3) route and written in full: `lem:hardy`,
  `lem:solenoidal-density`, `lem:leray-hopf` (endpoint included),
  `thm:ess` quoted verbatim from the printed page, `lem:l3-to-l5`,
  `lem:serrin-enstrophy`. No uniqueness theorem for $L^3$ mild solutions is
  imported; the case $T^*(a)>\nu T_*$ does not arise.
* **C-3, assembly half** — Fefferman's clauses checked one by one against the
  printed (A); only the page pointer needs correcting (§10 item 1).
* **S-1, $H^1$-extension half** — `lem:sobolev-h1`, verified. This is the
  round-1 repair and it holds.
* **§8 item 3** of the literature note — ESS p. 213 quoted for
  $L_{3,\infty}=L^\infty_tL^3_x$; re-verified from the printed page.
* **N-1, partial** — `eq:serrin-enstrophy-identity` written out from exact
  memberships, with $\langle\Delta u,\nabla p\rangle=0$ and
  $\norm{\nabla^2u}_2=\norm{\Delta u}_2$; reusable by the enstrophy lane.

Still open (unchanged):

* **C-3, the smoothness lemma** (Tao 5.4(iv) $\Rightarrow$
  $u,p\in C^\infty([0,T]\times\R^3)$) — owned by the local-theory lane, cited
  as (R2)/`lem:global-smooth`, not proved in the audited block. I read that
  lane's *statement* only.
* **S-1, source half** — Nirenberg 1959 p. 125 (2.2) is [MO] for both the
  continuation lane and this audit (numdam returned 404 this round);
  Lieb–Loss Theorem 8.3's text and constant remain [MO] (my §4.2 algebra
  corroborates the value but is not a reading). Only the *existence* of $C_S$
  is load-bearing.
* **E8, E12** — Stein–Weiss Ch. I and Folland's theorem numbers remain [MO].
* **Galdi Ch. III** — unverified and uncited; `lem:solenoidal-density`
  replaces it, correctly restricted to $\bigcap_kH^k$.
* **P-3, X-1, `sec:quotient`** — untouched.

---

## 12. Frontier record

**MODE / RESULT.** REVIEW (proof audit), round 2, of
`research/evidence/cp02-continuation.md`
(sha256 `c6c2717e…`) at repository HEAD
`fc1ee2bcc7afbbef43bb41a9c5070009034e603f`. Result: **PASS** — the round-1 bad
bridge is genuinely repaired, no new bad bridge exists, and two
citation-level D5 defects require one-line fixes before splicing.

**CLAIM AND SCOPE.** This audit claims only that the audited block, with the
two one-line edits of §5, is a complete proof of the six statements of §6,
conditional on `prop:localtheory` (R1)–(R4), `lem:global-smooth`,
`prop:energy`, `def:sobolev-constant`, and the single imported theorem ESS
Theorem 1.3. It claims nothing about any other section of the manuscript, and
nothing about `hyp:critical` being provable.

**EVIDENCE.** ESS pp. 211–214 read this round from the mathnet English
translation (with the corrected 302-plus-cookie retrieval recipe), and p. 212
**rendered as a page image**, which is the only way to see the printed
$\overline{Q}_T$ — the PDF text layer silently drops the overline, so a
text-only check would have mis-convicted the candidate. All ESS
transcriptions in the block are verbatim, including (1.3)–(1.7),
"$\forall t_0\in[0,T]$", the mixed-norm two-case display, Theorem 1.2's LPS
range, Theorem 1.3, the unnumbered classical-form prose, and (1.1)–(1.2) with
unit viscosity. Fefferman read in both editions: (1)–(7) and (A) are used
exactly as printed, but (4) is on p. 57 (book) / p. 1 (standalone), not the
cited p. 2. Independent recomputation this round of: the $L^1$-Fourier bound
$\int|\xi|^m|\hat f|\le\pi\norm f_{H^{m+2}}$ with $\int(1+|\xi|^2)^{-2}=\pi^2$;
`lem:sobolev-h1`'s three steps; $\int_{|\xi|<1}|\xi|^{-2}=4\pi$;
$2\pi i\,\xi\times\hat A=\hat v$; $\norm{\nabla A}_2\le\norm v_2$ and the
observation that $A\notin L^2$ in general (so the block is right not to claim
it); Hardy's constant 2 and its boundary terms; every cutoff error in $W^1_2$;
the (1.5) test identity term by term; the enstrophy identity and
$\langle\Delta u,\nabla p\rangle=0$; $\tfrac15+\tfrac3{10}+\tfrac12=1$,
$\theta=\tfrac25$, $\norm{\nabla^2u}_2=\norm{\Delta u}_2$, Young at
$(\tfrac54,5)$ giving $C_*=\tfrac{256}{3125}C_S^3$, the Gronwall halving, and
$\nu^{-4}$ twice by two routes; the Schwartz$\iff$(4) equivalence;
$3(\pi/2)^{4/3}=\tfrac34(2\pi^2)^{2/3}=5.4785\ldots$. Mechanical checks: 13
external `\ref` targets all resolve, 5 `\cite` keys all exist, 16 new labels
collide with nothing in the other two lane files, D5 phrase grep clean.
Seven refutation attempts, all seven failed.

**FIRST GAP.** No logical gap inside the section. The first gap is
documentary: the compactly supported Sobolev inequality's primary text
(Nirenberg 1959 p. 125 (2.2), reached only through the energy lane and [MO]
here; Lieb–Loss Theorem 8.3 for the value, [MO]), and behind it E8
(Stein–Weiss) and E12 (Folland). The first structural dependency is clause
(R2) of `prop:localtheory` / `lem:global-smooth`, cited and not proved here.
The first *citation* defects are §1 (E-1) and (E-2).

**SURVIVING CONDITIONAL SUFFIX.** As §6: given (R1)–(R4),
`lem:global-smooth`, `prop:energy` and `def:sobolev-constant`,
`hyp:critical` $\Rightarrow$ `def:target`, through `lem:nu-normalisation`,
`lem:hardy`, `lem:solenoidal-density`, `lem:leray-hopf`, ESS Theorem 1.3,
`lem:l3-to-l5`, `lem:sobolev-h1`, `lem:serrin-enstrophy`, `thm:continuation`,
`thm:conditional`. One imported literature theorem, its hypothesis class
verified against the printed definition; no imported uniqueness theorem.

**NON-CLAIMS.** As §8.

**NEXT DISTINCT ACTION.** Hand the block to the integrator with the two §5
edits applied and §10's items 3–13 resolved; then splice in place of
Section 5, add `\newtheorem{lemma}[theorem]{Lemma}`, resolve the three
declared overlaps (`lem:nu-normalisation`/`lem:nu-scaling`,
`lem:sobolev-h1`/`lem:sobolev`, `eq:nu-normalization`/`eq:nu-map`), and run
the structural verifier. Separately: the literature lane corrects
`cp01-literature-statements` §3.1 ($Q_T\to\overline{Q}_T$) and reconciles the
`Fefferman2000` pagination, and should read Nirenberg p. 125 and Lieb–Loss
pp. 201–204 to close the source half of S-1. No further round of this audit
is needed on the continuation section unless a reopening condition of §9
fires.
