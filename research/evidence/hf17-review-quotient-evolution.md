# Independent audit of the quotient evolution

VERDICT: **PASS**

REVIEWED SCOPE: research/evidence/hf17-quotient-evolution.md, frozen with
SHA-256
84f2dcbf7801c911eea2535b870a358b99cb2b5af06da97a7ec8689d4b09b670
on base commit 0918b9ab403fcbc878ee20b62d887f6405123337.
The quotient minimizer and directional-derivative lemma are treated as the
previously reviewed input named by the candidate.

FIRST BAD BRIDGE: none.

EVIDENCE:

1. Strict convexity of \(L^3\) gives uniqueness of the minimizing coset
   representative, and its first variation against the closed gradient
   subspace gives
   \(\int |w|w\cdot g=0\).  Thus \(A=|w|w\) is distributionally
   divergence-free.  Since the Leray projection is bounded on \(L^3\),
   annihilates the closed gradient space, and fixes solenoidal \(u\),
   \[
      u=\mathbb Pw,\qquad q=(I-\mathbb P)w.
   \]
   Boundedness of both projections proves (5), with
   \(\|A\|_{3/2}=\|w\|_3^2\) and
   \(\|w\|_3^3=3\mathcal Q(u)\).

2. On the declared compact classical \(H^m\) interval, \(m\ge4\),
   \(\Delta u\), \((u\cdot\nabla)u\), and \(u_t\) belong to \(L^3\).
   The Riesz pressure gradient also belongs to \(L^3\) and lies in the
   closed gradient subspace.  Applying the reviewed directional derivative
   therefore kills \(\nabla p\) through (3) and gives (6), with both signs
   correct.

3. The heat semigroup maps the closed gradient subspace into itself.  Using
   \(e^{s\Delta}q\) as a competitor and \(L^3\)-contractivity gives (7).
   Since
   \[
      {e^{s\Delta}u-u\over s}\longrightarrow\Delta u
      \quad\hbox{in }L^3
   \]
   for the classical field, the reviewed derivative formula identifies the
   right generator and proves
   \(\int A\cdot\Delta u\le0\).  This is generator nonpositivity only; it
   does not supply a coercive lower bound for
   \(-\int A\cdot\Delta u\).

4. Let \(\Phi_s\) be the flow of the frozen smooth divergence-free velocity.
   It is a volume-preserving proper \(C^1\) diffeomorphism for both signs of
   sufficiently small \(s\).  If \(q=\nabla\varphi\), then
   \[
      D\Phi_{-s}^T(q\circ\Phi_{-s})
      =\nabla(\varphi\circ\Phi_{-s}).
   \]
   Approximation by compactly supported smooth gradients and boundedness of
   pullback on \(L^3\) extend this to every \(q\in\mathcal G_3\), so \(q_s\)
   in (10) is an admissible competitor.

5. At \(x=\Phi_s(y)\), one has
   \[
      u_s(x)=u(y),\qquad
      q_s(x)=D\Phi_s(y)^{-T}q(y).
   \]
   Volume preservation therefore gives exactly the envelope (11).  The
   classical Sobolev assumptions imply
   \[
   {u\circ\Phi_{-s}-u\over s}\to-(u\cdot\nabla)u
   \quad\hbox{in }L^3,
   \qquad
   {D\Phi_s^{-T}-I\over s}\to-(\nabla u)^T
   \quad\hbox{uniformly}.
   \]
   Multiplication by \(q\in L^3\) supplies the required \(L^3\) domination
   for the competitor expansion.

6. Write the left and right sides of (11) as
   \(\mathcal Q(u)+sL+o(|s|)\) and
   \(\mathcal Q(u)+sR+o(|s|)\).  The inequality for \(s>0\) gives
   \(L\le R\), while division by \(s<0\) gives \(L\ge R\).  Hence their
   coefficients agree:
   \[
      -\int A\cdot((u\cdot\nabla)u)
      =-\int A_i(\partial_i u_j)q_j.
   \]
   The right contraction is
   \(-\int q\cdot((A\cdot\nabla)u)\), proving (9) without differentiating
   \(q\) or \(w\).  Substitution into (6) gives every sign in (13).

7. For \(v=S_Lu\),
   \[
   \begin{aligned}
   \left|\int q\cdot((A\cdot\nabla)v)\right|
   &\le\|\nabla v\|_\infty\|q\|_3\|A\|_{3/2}\\
   &\le C\|\nabla v\|_\infty\|w\|_3^3\\
   &\le C2^{5L/2}E_0^{1/2}\mathcal Q(u).
   \end{aligned}
   \]
   The last line uses three-dimensional Bernstein and the kinetic-energy
   inequality.  Thus (14) is an input-dependent Gronwall coefficient with
   the correct frequency and energy powers.

8. Splitting \(\nabla u=\nabla v+\nabla u^{hi}\) leaves exactly (15).
   The crude estimate
   \(\|\nabla u^{hi}\|_\infty\mathcal Q(u)\) introduces an uncontrolled
   high-frequency norm and supplies neither an input-only coefficient nor
   viscous absorption.  The candidate correctly stops there.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: The full candidate survives.  On every
compact classical interval, the quotient functional has the exact
pressure-free evolution (13); its heat generator is nonpositive, and its
low-strain Euler part obeys the input-dependent bound (14).

UNNECESSARY DEPENDENCIES: The heat sign uses only invariance of the closed
gradient space under the heat semigroup and \(L^3\) contraction.  The strain
rewrite needs no smoothness or spatial derivative of the nonlinear
minimizer.

NON-CLAIMS: Generator nonpositivity is not a quantitative viscous
dissipation estimate.  This audit proves no bound for (15), no HF estimate,
no continuation theorem, and no global regularity result.

REOPENING CONDITION: Bound the complete high-strain form (15) by a strict
fraction of the available heat dissipation plus an input-only remainder, or
exhibit another exact cancellation that removes it.
