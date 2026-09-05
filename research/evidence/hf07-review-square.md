# Audit of the dyadic square-energy mechanism

VERDICT: **FAIL WITH SCOPE**

REVIEWED SCOPE: `hf07-square-energy.md` at verified SHA-256
`50f41a410784e997414c458a847428d0943931a393472a5302824401c8e0ac85`,
on full base commit `88c0b2e4e9cb1fce9eb58f8a0b2e2ea8caee13e9`.

FIRST BAD BRIDGE: Equation (11) is an exact computation only for the
unweighted divergence-free L2 pairing of the linearized operator \(L_U\).
The assertion immediately following it that the commutators created by the
cubic square-function weight “do not negate (11)” is not derived. Those
commutators are themselves of order \(\nabla U\), so an indefinite symmetric
part in the toy pairing does not establish a nonzero or indefinite symmetric
part of the complete trilinearization of (6). Consequently (11) is not yet an
exact obstruction to the proposed nonlinear cubic mechanism.

REPLACEMENT ARGUMENT: Keep (11) as an oracle locating the coefficient that
must be tested, and replace the claimed failure by the following conditional
statement: the square-cubic route fails to have a sign if the full low--high
principal form obtained by linearizing (6), including the variation of
\(s_{I,\epsilon}\) and the commutator of the Leray projection with
multiplication by that weight, has a nonzero indefinite symmetric part. To
turn this into a proof, compute that full principal form on an explicit
low-frequency strain and high-frequency divergence-free wave packet, then
show that its leading cubic integral changes sign under an admissible change
of data. No such computation appears in the frozen note. Merely estimating
the omitted terms by their absolute values cannot rule out exact cancellation.

EVIDENCE:

1. For finite \(I\) and \(\epsilon>0\), differentiation gives
   \[
    \mathcal F_{I,\epsilon}'
      =\sum_{j\in I}\int s_{I,\epsilon}u_j\cdot\partial_tu_j.
   \]
   Integration by parts in diffusion yields exactly
   \[
    -\nu\int s_{I,\epsilon}\sum_j|\nabla u_j|^2
    -\nu\int s_{I,\epsilon}|\nabla s_{I,\epsilon}|^2.
   \]
   Thus (4)--(5) have the correct coefficients and positive diffusion.

2. The common transport cancels because
   \[
    \sum_j s,u_j\cdot(u\cdot\nabla u_j)
      =s^2u\cdot\nabla s=\tfrac13u\cdot\nabla(s^3).
   \]
   The pressure contribution is
   \(\sum_j\int p_j u_j\cdot\nabla s\). The comma in the displayed
   integrand of (6), `p_j,u_j`, is a typographical error; with multiplication
   in its place, (6) is exact. The commutator symbol (8) and pressure symbol
   (9) have the stated signs and multipliers.

3. Formula (6) retains interactions with frequencies outside the finite
   band because \(C_j\) contains the full velocity in both nonlinear inputs.
   No band-boundary term is silently dropped at the finite-band level.

4. In the unweighted toy pairing, self-adjointness of \(\mathbb P\),
   \(\mathbb Pq=q\), and \(\nabla\cdot U=0\) give
   \[
    \langle q,L_Uq\rangle
      =\int q_aq_b\,\partial_bU_a.
   \]
   This correctly identifies low-frequency strain and is sign-indefinite as
   a quadratic L2 form. It does not include the derivative of the cubic
   weight or the weighted pressure projection, which are exactly the terms
   needed for the claimed nonlinear conclusion.

5. The displayed low--high bound (12) is at most a schematic sufficient
   upper bound until a paraproduct derivation includes every weighted Leray
   commutator, balanced interaction, and band-boundary term. Even if (12) is
   established, an uncontrolled absolute upper bound proves lack of closure
   by that estimate; it proves neither a sign-changing exact remainder nor
   impossibility of another grouping.

6. The phrase “a sharper Carleson version” does not specify a measure,
   square function, tents, norm, quantifiers, or a derived inequality. It
   cannot serve as a criterion or hypothesis. A valid replacement must state
   the actual spacetime quantity and prove that it bounds the complete
   remainder before invoking it in (15).

7. For fixed finite \(I\), the \(\epsilon\downarrow0\) passage is valid.
   The subtraction in (2) makes the regularized energy finite, and (16)
   controls the second diffusion term by the first. Smooth finite-band bounds
   dominate the remainder terms. The convention on \(\{S_I=0\}\) agrees
   with the Sobolev chain rule.

8. At a fixed Schwartz regular time, the energy limit in (3) is the standard
   homogeneous Littlewood--Paley square-function equivalence for
   \(1<p<\infty\), applied at \(p=3\). It establishes only
   \(\mathcal F(u)\simeq\|u\|_3^3\). The stronger assertion that the complete
   differentiated identity (2)--(6) passes through both infinite band edges
   needs explicit summable bounds for its commutator and pressure remainder;
   “standard homogeneous low-frequency estimates” alone is not a displayed
   proof of that assertion. In any case, fixed-time convergence supplies no
   uniform control near a terminal time.

CONDITIONAL SUFFIX THAT SURVIVES: The exact finite-band identity provides a
legitimate framework. If the full cubic low--high principal form is computed
and shown to leave a one-sided strain term, and if all-band convergence is
proved with uniform summable estimates, then a precisely stated input-only
spacetime bound for that full remainder of the form (15) would feed the
critical L3 continuation route.

UNNECESSARY DEPENDENCIES: The finite-band identity and its positive diffusion
need no Littlewood--Paley norm equivalence. The L2 strain oracle needs neither
the all-band limit nor a named Carleson framework.

NON-CLAIMS: This audit does not assert cancellation of the cubic low--high
form. It finds that the note has not computed it. Neither the L2 toy model nor
an uncontrolled absolute paraproduct bound proves a universal obstruction,
failure of HF, blow-up, or regularity.

REOPENING CONDITION: Supply (i) the complete low--high principal symbol or an
explicit wave-packet evaluation for the actual weighted cubic remainder, and
(ii) explicit summable estimates justifying the all-band differentiated
identity. If a Carleson-type repair is proposed, define its precise spacetime
quantity and prove the required remainder bound.
