# Independent audit of the HF02 prior-art table

VERDICT: **REPAIR**

REVIEWED SCOPE: all four entries in `hf02-prior-art.md`, frozen at
SHA-256 `a7435b4a0887953c761d3d436548d2fdfeeb888e25de228cc77d5d3e958f11fb\).
The digest was reproduced before review. The audit checks only exact source
statements and their relation to HIGH-PRESSURE; it does not validate a source
merely because its theorem is stated.

FIRST BAD BRIDGE: the Zhou row merges the interior and endpoint
gradient-pressure cases into
\[
 \nabla p\in L^{\alpha,\gamma},\qquad
 \frac2\alpha+\frac3\gamma\leq3,\qquad1\leq\gamma\leq\infty,
\]
without the endpoint qualifications in Theorem 1.1. The primary theorem has
an interior range \(2/3<\alpha<\infty\), \(1<\gamma<\infty\), a separate
unconditional endpoint \(L_t^{2/3}L_x^\infty\), and a separate
\(L_t^\infty L_x^1\) endpoint that is assumed sufficiently small.

EVIDENCE:

## 1. Bradshaw--Grujić: pass

The source is arXiv:1501.01043v2, “Frequency localized regularity criteria
for the 3D Navier--Stokes equations.” It explicitly sets forcing to zero and
viscosity to one on \(\mathbb R^3\). Theorem 1 fixes
\(\epsilon\in(0,1)\), \(T>0\), and a Leray--Hopf weak solution
\[
 u\in C((0,T);\dot B_{\infty,\infty}^{-\epsilon})
\]
on \([0,T]\). It assumes a time \(t_0\in(0,T)\), finitely many later times
\(t_i\), the subdued finite-window condition (3), the displayed lower spacing
between successive times, and the displayed upper terminal gap. It concludes
that \(u\) extends smoothly beyond \(T\). The table's summary is accurate,
although the exact source writes \(C(0,T;\cdot)\), conventionally meaning the
open interval, rather than continuity at \(t=0\).

Theorem 2 has the same solution hypotheses and assumes exactly
\[
 \int_0^T\left(
 \sup_{J_{\rm low}(t)\leq j\leq J_{\rm high}(t)}
 2^{-\epsilon j}\|\dot\Delta_j u(t)\|_\infty
 \right)^{2/(1-\epsilon)}dt<\infty.
\]
It concludes regularity on \((0,T]\). Both cutoff definitions involve the
Besov norm, and \(J_{\rm low}\) also uses
\(\|u\|_{L^\infty_tL^2_x}\). Neither theorem contains a pressure projection
or estimates the signed HF functional. The table's comparison is supported
by the full primary text:
[Theorems 1--2](https://arxiv.org/html/1501.01043#S1.Thmtheorem1).

## 2. Zhou: repair the theorem statement and weak-solution hypotheses

The accessible author-uploaded full text identifies the exact result as
Theorem 1.1. It assumes
\[
 u_0\in L^2(\mathbb R^3)\cap L^q(\mathbb R^3),\qquad q\geq4,
\]
with distributional divergence zero, and \(u\) a Leray--Hopf weak solution
of the unforced, unit-viscosity Cauchy problem. The conclusion is that \(u\)
is regular on \([0,T]\) under any of:

1. \(\nabla p\in L^\alpha(0,T;L^\gamma)\),
   \(2/\alpha+3/\gamma\leq3\),
   \(2/3<\alpha<\infty\), and \(1<\gamma<\infty\);
2. \(\nabla p\in L^{2/3}(0,T;L^\infty)\);
3. \(\|\nabla p\|_{L^\infty(0,T;L^1)}\) is sufficiently small.

Thus \(\gamma=\infty\) occurs only at the specified
\(\alpha=2/3\) endpoint, while \(\gamma=1\) occurs only at
\(\alpha=\infty\) and carries smallness. The abstract's compressed phrase
\(1\leq\gamma\leq\infty\) cannot replace these theorem-level qualifications.
The notation is \(L^{\alpha,\gamma}=L^\alpha_tL^\gamma_x\).

The source contains two distinct calculations. In Section 2, the proof of
Theorem 1.1 multiplies by \(4u|u|^2\) and derives equations (2.1)--(2.6),
including the Calderón--Zygmund estimate
\(\|\nabla p\|_r\leq C\||u||\nabla u|\|_r\). In Section 3, for the pressure
criterion, it multiplies by \(s u|u|^{s-2}\) and obtains the general \(L^s\)
balance containing
\[
 2(s-2)\int |p|\,|u|^{s/2-1}|\nabla |u|^{s/2}|.
\]
Thus the prior-art table's generic \(L^s\) calculation is genuinely present,
but it belongs to the proof of the pressure criterion (Theorem 1.2 and its
Section 3 formulation), not to the gradient-pressure criterion in Theorem
1.1. Theorem 1.2 assumes the same initial-data and Leray--Hopf framework and,
in its interior range, requires
\[
 p\in L^\alpha(0,T;L^\gamma),\qquad
 \frac2\alpha+\frac3\gamma\leq2,\quad
 1<\alpha<\infty,\quad\frac32<\gamma<\infty.
\]
Its following remark attributes the endpoints \(L_t^1L_x^\infty\) and
sufficiently small \(L_t^\infty L_x^{3/2}\) to earlier work; those endpoints
should not be presented as additional cases proved by Theorem 1.2 itself.

The comparison with HF survives: every case assumes pressure-gradient
control and none gives a fixed-frequency signed pressure estimate.
Primary full text:
[author-uploaded Proceedings paper](https://www.researchgate.net/publication/226020355_On_regularity_criteria_in_terms_of_pressure_for_the_Navier-Stokes_equations_in_R3).

## 3. Taghizadeh: inaccessible, no mathematical verdict

The supplied bare link
\(https://www.researchgate.net/publication/400395309\) redirects to the
generic ResearchGate publications directory. Searches by the identifier and
author name did not recover a stable publication title, author list, theorem,
equation, abstract, or downloadable primary text. The available Taghizadeh
profile result concerns an unrelated mechanics researcher and cannot identify
the intended item.

Accordingly, “unavailable as a verified source” is the correct status for the
link in the frozen table. This is a source-access gap only. It is not evidence
that the intended paper lacks a matching estimate, and no claim about its
mathematical validity follows. If the user's longer title-bearing URL differs
from the bare identifier, that exact URL or the primary PDF is needed for a
theorem-level audit.

## 4. Cox Proposition D.5: statement verified, proof status overstated if called established

The full ResearchGate rendering states Proposition D.5 at Appendix D.2.1.
For dyadic \(j\), \(J\geq J_0\), a working slab \(Q\), and a caloric cutoff
\(\eta\) supported in \(Q\), it defines
\[
 \operatorname{Tail}_j(J)=
 \sum_{|k-j|>J}\|\Delta_k(\eta u\otimes u)\|_{L^2(Q)}
\]
and asserts
\[
 \operatorname{Tail}_j(J)\leq C_{\rm env}\gamma^J M(Q),\qquad
 M(Q)=\|u\|_{L^\infty_tL^3_x(Q)}^2+
      \|\nabla u\|_{L^2(Q)}^2+1.
\]
It says \(\gamma\in(0,1)\), \(J_0\in\mathbb N\) depend on the scale-free
Calibration Box constants and that the bound is uniform in \(j,Q\) subject
to Appendix D admissibility. The table accurately transcribes the
proposition.

The context matters. Appendix D says D.5 consumes the pressure-smart local
energy inequality and harmonic corrector of Appendix B, the “CPM split and
tail budget” of Appendix C, and the scale-free LP/CZ/\(A_2\) toolkit. The
printed proof is only a short assertion that CPM oscillation control, finite
annular overlap, a kernel moment, and the envelope budget yield geometric
decay. It does not display the paraproduct estimates or derive the constant
uniformity. Therefore the proposition is accurately reported as a
**candidate stated in the author preprint**, but this inspection does not
independently establish its proof. Its budget explicitly contains the local
critical norm and local dissipation, and its tail is a velocity-product Bony
tail rather than the project's signed pressure pairing. It is not an HF
premise.

## 5. Cox Theorem G.5: statement verified, proof has concrete defects

Theorem G.5 states that for any divergence-free
\(u_0\in L^3(\mathbb R^3)\), “the suitable solution” satisfies
\[
 \sup_{t\geq0}\|u(t)\|_3\leq M(\|u_0\|_3).
\]
The singular phrase “the suitable solution” does not specify selection or
uniqueness in a class where those issues matter. The proof then defines
\[
 M_*:=\inf\{M>0:\exists u\ {\rm suitable\ with}\
                 \sup_{t<T(u)}\|u(t)\|_3>M\}.          \tag{G.30}
\]
As written, this is not a positive minimal blowup threshold: any nonzero
suitable solution makes the property true for all sufficiently small
\(M>0\), so the infimum is \(0\). The next sentence nevertheless selects
solutions with suprema decreasing to \(M_*>0\). This is an invalid bridge,
independent of the unresolved internal references.

The alleged ancient-limit construction further asserts norm attainment and
nontriviality in (G.31), an APMS modulus from Proposition F.8, and an
iteration of the Type-I alternative G.28, but supplies only a summary. The
document also retains unresolved references in its closure ledger, including
“Absorption budget & parameters ??,??,??” and “Appendix G, Thm. ??” in
Appendix H.16. These facts prevent importing G.5. The source does expose
enough full text to identify the defective threshold above; this is stronger
than merely saying that its proof has placeholders, but it does not by itself
adjudicate every lemma in the 100-plus-page preprint.

Primary source:
[Cox full ResearchGate rendering](https://www.researchgate.net/publication/397174185_Resolving_Global_Regularity_for_the_3D_Navier-Stokes_Equations_at_the_Critical_Endpoint),
especially Proposition D.5 and Theorem G.5.

REPLACEMENT ARGUMENT:

Revise the table as follows.

1. Keep the Bradshaw--Grujić row, adding unit viscosity and the exact
   \(C((0,T);\dot B_{\infty,\infty}^{-\epsilon})\) convention if desired.
2. Replace the Zhou gradient-pressure criterion by the three exact cases
   above, add \(u_0\in L^2\cap L^q\), \(q\geq4\), and identify the weak
   solution as Leray--Hopf. Retain the general \(L^s\) calculation, but
   attribute it to Section 3 and Theorem 1.2's pressure criterion; distinguish
   it from the \(4u|u|^2\) gradient-pressure calculation for Theorem 1.1.
3. Retain Taghizadeh only as inaccessible metadata and make no statement
   about what the unavailable paper proves or fails to prove.
4. Keep Cox D.5 as a preprint-stated candidate with its full Appendix D
   dependencies; do not describe its terse proof as independently verified.
5. For G.5, record both the unresolved references and the defective
   definition (G.30); do not import the theorem.

CONDITIONAL SUFFIX THAT SURVIVES: Bradshaw--Grujić supplies a valid
frequency-localized velocity continuation criterion. Zhou supplies valid
conditional pressure-gradient criteria with the repaired endpoints. Cox
D.5 is a stated local tail candidate whose formula consumes the critical
norm. None of these statements yields the fixed-cutoff signed HF estimate.

UNNECESSARY DEPENDENCIES: the broad assertion that Cox's entire document is
invalid is unnecessary and is not made. Proposition D.5 can be compared with
HF from its own stated formula and context even though G.5 fails. Likewise,
failure to access Taghizadeh does not support any mathematical conclusion.

NON-CLAIMS: this audit does not establish Cox D.5, disprove every argument in
the Cox preprint, or infer anything about the inaccessible Taghizadeh item.
It does not prove HIGH-PRESSURE or global Navier--Stokes regularity.

REOPENING CONDITION: reopen Taghizadeh after receiving a stable title-bearing
URL or primary PDF. Reopen Cox D.5 as a usable premise only after its CPM,
envelope, and admissibility dependencies and the geometric tail derivation
are independently verified. G.5 requires at least a corrected nonzero
critical-threshold definition and a complete audited compactness/rigidity
chain without unresolved references.
