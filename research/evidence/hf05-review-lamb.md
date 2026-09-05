# Independent audit of the HF05 Lamb-commutator note

VERDICT: **REPAIR**

REVIEWED SCOPE: `hf05-lamb-commutator.md`, frozen at base commit
`3d5642a9f48e2666a7cdbf848a5494978fe38cca` and new-file SHA-256
`dd5cab232ccdb619a2a4daaee14720de0ed1af0802274d4fd08e11cb388cb0dd`.
The digest was reproduced before review.  This audit checks the algebraic
identities, signs, multiplier bounds, energy remainder, and scaling.  It does
not assess publication priority or promote the argument.

FIRST BAD BRIDGE: no mathematical bridge through (25) fails.  The first
unsupported claim is the heading “**New exact reduction**” in Section 6.
The note derives the identity, but it supplies no literature audit capable of
establishing novelty or published priority.  Moreover its norm estimate is
explicitly the same Hölder--Calderón--Zygmund estimate as (10a), so it must
not be advertised as a new commutator estimate.  Replace “New exact
reduction” by “Derived exact reduction” (or simply “Exact reduction”).

EVIDENCE:

1. With \(L=u\times\omega\) and \(q=p+|u|^2/2\),
   \((u\cdot\nabla)u=\nabla(|u|^2/2)-L\).  Since
   \(\nabla p=-(I-\mathbb P)(u\cdot\nabla u)\), this gives
   \(\nabla q=(I-\mathbb P)L\) with the stated sign.

2. For \(w=|u|u\),
   \(\operatorname{div}w=u\cdot\nabla|u|\).  The kinetic contribution
   vanishes because
   \[
      \int \frac{|u|^2}{2}u\cdot\nabla|u|
       =\frac16\int u\cdot\nabla |u|^3=0.
   \]
   Integration by parts, \(w\cdot L=0\), and self-adjointness of
   \(\mathbb P\) therefore give
   \[
      P_3=-\langle w,(I-\mathbb P)L\rangle
          =\langle \mathbb Pw,L\rangle
          =\langle[\mathbb P,|u|]u,L\rangle.
   \]
   Thus (3)--(6) have the correct signs.  The commas in (4)--(5) should be
   ordinary multiplication/spacing, not punctuation inside the formula.

3. The principal-value increment representation (7) is correct up to the
   declared fixed kernel sign convention.  The bound (8) follows directly
   from \(L^3\) boundedness of the smooth Leray multiplier, Hölder, and
   homogeneous Sobolev:
   \[
      \|[\mathbb P,a]b\|_3
       \le C\|ab\|_3+\|a\|_6\|\mathbb Pb\|_6
       \le C\|\nabla a\|_2\|b\|_6.
   \]
   With \(a=|u|\), \(b=u\),
   \(\|u\times\omega\|_{3/2}\le\|u\|_6\|\omega\|_2\), and the classical
   a.e. inequality \(|\nabla|u||\le|\nabla u|\), equation (10) follows.
   The same estimate follows from (10a), exactly as the note acknowledges.

4. The high-cutoff correction has the correct sign.  For a real-even smooth
   multiplier \(Q_J\), self-adjointness and commutation with \(\mathbb P\)
   give
   \[
   \begin{aligned}
      H_J&=-\langle Q_Jw,\nabla p\rangle\\
         &=\langle Q_J[\mathbb P,|u|]u,L\rangle
           +\langle Q_Jw,\nabla k\rangle.
   \end{aligned}
   \]
   Since \(\langle w,\nabla k\rangle=0\) and \(S_J=I-Q_J\), the last term is
   \(-\langle S_Jw,\nabla k\rangle\), as in (16).  Reusing the unfiltered
   cancellation without this term would indeed be wrong.

5. At fixed \(J\), Bernstein and energy give
   \(\|S_Jw\|_\infty\lesssim2^{3J}\|u\|_2^2\) and
   \(\|\nabla k\|_1\le\|u\|_2\|\nabla u\|_2\).  Hence
   \[
      \int_0^\tau|\langle S_Jw,\nabla k\rangle|dt
       \lesssim 2^{3J}\|u_0\|_2^4(H/(2\nu))^{1/2}.
   \]
   The fourth power of the \(L^2\) norm and the \(H^{1/2}\nu^{-1/2}\)
   dependence in (19) are correct.  “Energy-controlled” here means this
   finite-horizon, fixed-cutoff bound; it does not control the new critical
   trajectory norm (22).

6. If \(Y=\|\nabla u\|_2^2\), then under Navier--Stokes scaling
   \(Y_\lambda(t)=\lambda Y(\lambda^2t)\), while
   \(\delta_{\rm sp}\) is invariant.  Thus
   \(\int\delta_{\rm sp}Y^2dt\) is scale invariant.  Energy controls only
   \(\int Ydt\).  The warning after (23) is correct: two \(L^1_t\) factors
   do not have an integrable product.  The \(L^\infty_t\) input (24) is
   sufficient but is substantial and scales by \(\lambda\).

7. The amplitude-reversal check is an algebraic snapshot test, not a claim
   that \(u\mapsto-u\) is a Navier--Stokes solution symmetry.  Read that way,
   its signs are correct: the quadratic pressure and \(L=u\times\omega\)
   stay fixed, while both \(P_3\) and the commutator factor change sign.

REPLACEMENT ARGUMENT: retain (3)--(25), describe (6) and (16) as identities
derived in this note, and state only that they expose Lamb-vector geometry.
The analytic estimate remains the standard direct pressure/Hölder bound in a
different factorization.  Replace the Section 6 heading by “Derived exact
reduction.”  Also repair the malformed TeX in the frozen file:

- `H_J=langle` in (16) must be `H_J=\langle`;
- both occurrences of `quad\hbox` in (23)--(24) must be
  `\qquad\hbox` (or equivalent spacing);
- formulas (4)--(5) should remove the stray commas after \(k\) and \(p\).

CONDITIONAL SUFFIX THAT SURVIVES: the exact global and high-cutoff
commutator identities, the speed-sensitive classical estimate, the
fixed-\(J\) energy bound for the low kinetic correction, and the reduction to
the critical norm \(\mathcal G_H\) all survive.  They identify a possible
depletion variable but supply no estimate of it from energy.

UNNECESSARY DEPENDENCIES: the increment kernel (7) is not needed to prove
(8)--(10), and the commutator identity is not needed to obtain the numerical
bound (10a).  Claims based on the external profile and trajectory notes are
not needed for the exact reduction and were not independently audited here.

NON-CLAIMS: this audit establishes neither novelty nor priority for the
identity.  It does not establish an input-only bound on \(\mathcal G_H\), a
frequency gain, a sign, pressure absorption, HF, or global regularity.  In
particular, the energy inequality controls \(\int Y\), not (22).

REOPENING CONDITION: reopen the analytic route upon a proved input-only
bound for \(\mathcal G_H\), or a signed/frequency-sensitive commutator
estimate strictly stronger than the direct pressure Hölder estimate.  Any
novelty claim requires a separate documented literature search.
