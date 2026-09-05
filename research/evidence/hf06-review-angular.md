# Independent audit of the HF06 angular-pressure note

VERDICT: **REPAIR**

REVIEWED SCOPE: `hf06-angular-pressure.md`, frozen at base commit
`bd2ae2d1253d31c580ad07211cad02379758c000` and new-file SHA-256
`8859f50257533f4428122abb12f0a811b34dbbf2bb8f3b51df235a4106f07170`.
The digest was reproduced before review. This audit checks the two-mode
symbol, reality convention, angular and low-output bounds, localized
multiplier endpoints, shell ledger, and dissipation comparison.

FIRST BAD BRIDGE: the heading and conclusion that the derivative restores
“exactly one” low-output factor overstate an upper bound. Equations
(10)--(11) prove that the interaction is at most \(C|q||a||b|\) in the
specified high-high-to-low geometry. They do not prove a matching lower
bound, exclude polarization cancellation, or show that every interaction
contains no additional smallness. The valid conclusion is that the available
uniform symbol bound recovers **at least the displayed \(O(|q|)\) upper-bound
gain relative to an \(O(K)\) estimate**, and no stronger uniform gain has
been proved.

EVIDENCE:

1. The factor two and sign in (3) are correct. At \(q=k+l\), the ordered
   cross terms are \(a_i b_j+b_i a_j\), so
   \[
      \widehat p_{k,l}(q)
       =-2\frac{(q\cdot a)(q\cdot b)}{|q|^2}
       =-2\frac{(l\cdot a)(k\cdot b)}{|q|^2}.
   \]
   An unordered symmetrized bilinear convention can absorb the two, as the
   note says. For a real field, conjugate sum outputs and the corresponding
   difference outputs must be added. This restores reality without changing
   the coefficient of an individual ordered cross interaction.

2. The null cases are correct. Parallel inputs make both transverse
   contractions vanish; (q=0) has zero pressure gradient and must be kept
   outside the (|q|^{-2}) formula. These are pressure-symbol statements,
   not conclusions about the full quartic pressure pairing.

3. For comparable inputs, solenoidality yields
   \(|l\cdot a|\le |l|\sin\alpha |a|\) and its symmetric counterpart.
   Thus the near-parallel pressure coefficient has the asserted quadratic
   angular upper bound. Near antiparallel inputs satisfy
   \(K\beta\lesssim |q|\), including when radial mismatch dominates, so
   the inverse Laplacian can consume the quadratic angular factor and leave
   only an order-zero pressure upper bound.

4. A useful global strengthening follows directly from (10), without
   comparable-frequency assumptions:
   \[
   \boxed{
      |\widehat{\nabla p}_{k,l}(k+l)|
       \le 2\min\{|k|,|l|\}\sin\alpha\,|a|\,|b|.}
   \]
   Indeed, bound one contraction by
   \(|q\cdot a|\le|q||a|\) and the other by
   \(|q\cdot b|=|k\cdot b|\le|k|\sin\alpha|b|\), then interchange
   (k,l). This is a universal angular upper bound. It does not imply that a
   broad angular sector is small, because (sin\alpha) is then order one,
   and it supplies no angular equidistribution.

5. The low-output and angular statements must remain distinct. The general
   output-localized Calderón--Zygmund estimate
   \[
      \|\Delta_j\nabla p\|_s
       \lesssim 2^j\|\widetilde\Delta_j(u\otimes u)\|_s
   \]
   is simply the order-one derivative at output frequency (2^j). For
   antiparallel comparable inputs, geometry also gives
   (K\beta\lesssim|q|\), so the angular bound is consistent with it. Neither
   fact converts the other into a sector-counting gain.

6. The localized multiplier estimate (14) holds for every
   (1\le s\le\infty), provided the Littlewood--Paley cutoffs are smooth.
   After output localization, the multiplier kernel has (L^1) norm
   (O(2^j)), so both endpoints follow from convolution; no endpoint
   boundedness of an unlocalized Riesz transform is invoked. The frozen note
   explicitly explains (s=1), but (s=\infty) is valid for the same
   reason. If “all (L^p)” is claimed, smooth cutoff conventions must remain
   part of the statement.

7. The shell pairing (15) follows from output matching and Hölder, but it is
   an **upper-bound ledger**, not an identity despite the phrase “exact
   absolute shell ledger.” At (s=1), finite overlap in (k') and
   Cauchy--Schwarz give
   \[
      \sum_{|k-k'|\le C}\|u_k\|_2\|u_{k'}\|_2
       \lesssim \sum_k\|u_k\|_2^2.
   \]
   What remains is precisely the asserted
   \(\ell^1_j\) sum
   \(\sum_{j>J}2^j\|\widetilde\Delta_jw\|_\infty\).
   At (s=3/2), (18) likewise still contains the double shell sum. No
   interchange or Cauchy--Schwarz step displayed in the note removes that
   summability requirement. Energy alone supplies neither (ell^1) bound.

8. The dissipation estimate is correct:
   \[
      \|\nabla(|u|u)\|_{3/2}
       \le 2\||u|^{1/2}\|_6
              \||u|^{1/2}\nabla u\|_2
       \lesssim \|u\|_3^{1/2}D_3^{1/2}.
   \]
   It consumes the uncontrolled critical (L^3) norm and is an aggregate
   Sobolev estimate, not the required (ell^1) frequency distribution.
   The scaling check is also correct: both the fixed-time pressure work and
   (D_3) scale by (lambda^2), while angles and (|q|/K) are invariant.

REPLACEMENT ARGUMENT: retain the symbol and sector calculations, replace
“restores exactly one” by “yields an \(O(|q|)\) output-frequency bound,” and
state that this is the strongest uniform gain established by the calculation,
without a sharpness or lower-bound claim. Add the universal gradient-symbol
bound above as a clean separation of angular transversality from output
localization. Replace “exact absolute shell ledger” by “absolute shell upper
bound,” and keep the (ell^1) sums as explicit missing inputs.

The frozen source also contains malformed TeX tokens (`quad` in (1) and
(14), and commas in place of multiplication spacing in (4), (6), and (11));
these should be repaired before reuse.

CONDITIONAL SUFFIX THAT SURVIVES: the exact cross coefficient, reality and
null-case analysis, near-parallel quadratic angular bound, antiparallel
order-zero pressure bound, (O(2^j)) output-localized gradient estimate at
all (L^p) endpoints, and shell upper bounds (15)--(18) survive. They expose
the uncontrolled Besov/critical-shell summation and do not close HF.

UNNECESSARY DEPENDENCIES: the external real-profile and periodic-shear notes
are not needed for the symbol or shell estimates and were not audited here.
The universal gradient-symbol bound needs no dyadic decomposition.

NON-CLAIMS: the audit proves no lower bound, sharp asymptotic, absence of
cancellation, angular equidistribution, broad-sector smallness, signed
pressure estimate, or regularity result. It makes no novelty claim.

REOPENING CONDITION: reopen the route with a proved trajectory estimate that
summably controls the antipodal high-high shell pairs or their signed pairing
with (Q_J(|u|u)), without assuming the critical continuation norm the route
is intended to produce.
