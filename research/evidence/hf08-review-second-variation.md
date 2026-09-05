# Independent audit of the finite-band square-energy second variation

VERDICT: **REPAIR**

REVIEWED SCOPE: `research/evidence/hf08-square-second-variation.md` at
frozen commit `f0196f75b2c8dd92e2ea32199baf608753e23aa5`.  The historical
identifier `88c0b2e4e9cb1fce9eb58f8a0b2e2ea8caee13e9` cited by the preceding
HF07 audit resolves, through `docs/history-signing/2026-09-05-map.json`, to
the signed replacement `809dae22012d9f6a45d6cd8bea7541ea308893ea`; the
history-signing README states that the source tree was preserved.

FIRST BAD BRIDGE: The note calls (11), (16), and (18)--(20) exact in a
"stated" finite-band setting, but it never states the spatial domain or the
function/operator class.  Finiteness of (1), integration by parts in (14) and
(18), self-adjointness of the Leray projector, and the pairings involving
`M_s` are consequently being used without hypotheses.  This is a scope gap,
not an algebraic error in the displayed second variation.

EVIDENCE:

1. Pointwise, for \(f(y)=\frac13((\epsilon^2+|y|^2)^{3/2}-
   \epsilon^3)\), direct differentiation gives (4)--(6).  Because
   \(s_u\geq\epsilon>0\), no denominator is singular.  Applying the chain
   rule to \(\mathcal R_\epsilon(u)=DF_\epsilon(u)[V(u)]\), using
   \(DV(U)[v]=V_{\rm lin}(U,v)\) and
   \(D^2V(U)[v,v]=2V(v)\), gives exactly
   \[
   [h^2]\mathcal R_\epsilon(U+hv)
    =DF_\epsilon(U)[V(v)]
     +D^2F_\epsilon(U)[v,V_{\rm lin}(U,v)]
     +\tfrac12D^3F_\epsilon(U)[v,v,V(U)].
   \]
   Thus the coefficients in (10) are correct.

2. Under the explicit pointwise orthogonality assumption
   \(WU\mathbin\cdot Wv=0\), (5) reduces in the middle term to
   \(\int s_U(Wv)\cdot WV_{\rm lin}\), and (6) reduces in the last term to
   \(\int (WU\cdot WV(U))|Wv|^2/s_U\).  This proves (11), including its
   factor \(1/2\).  The same Taylor expansion of \(F_\epsilon\) proves (12).
   The phrase "occupy dyadic components disjoint" should be read as the
   stated assumption (7); ordinary separation of overlapping Littlewood--
   Paley Fourier supports by itself does not automatically imply pointwise
   shell-array orthogonality.

3. For divergence-free fields with legitimate integration by parts,
   \[
   \langle U,V(v)\rangle=\int v_i v_j\partial_jU_i,
   \qquad
   \langle v,V_{\rm lin}(U,v)\rangle
      =-\int v_i v_j\partial_jU_i.
   \]
   Hence (13)--(14) are correct.  If \(W^*W=I\) and \(s_U=c\) is spatially
   constant, the first two lines of (11) equal \(c\) times this cancellation.
   The third line vanishes only with the separately stated condition
   \(WU\cdot WV(U)=0\), equivalently frozen Euler variation of this weight;
   spatial constancy of \(s_U\) alone does not imply it.  The candidate does
   state the extra condition and therefore does not make that inference.

4. With the convention
   \([\mathbb P,s]=\mathbb P M_s-M_s\mathbb P\), self-adjointness gives
   \[
   \langle sU,-\mathbb PN_{vv}\rangle
    =-\langle sU,N_{vv}\rangle
     -\langle[\mathbb P,s]U,N_{vv}\rangle,
   \]
   and the analogous identity for \(v,N_{Uv}\).  Integrating the two
   unprojected terms by parts cancels the two copies of
   \(s v_i v_j\partial_jU_i\) and leaves
   \[
     \int(U\cdot v)(v\cdot\nabla s)
      +\tfrac12\int |v|^2U\cdot\nabla s.
   \]
   This verifies every sign and coefficient in (18).  In particular, the
   frozen strain is not a surviving term in the complete scalar-weight
   calculation.

5. Equation (16) follows from \(\mathcal M_s=W^*M_sW\) and adjunction.  Add
   and subtract multiplication by \(s_U\) in its two pairings, and add and
   subtract
   \(\frac12\int (U\cdot V(U))|v|^2/s_U\) in the last line of (11).  The
   residual is exactly (20).  Thus (20) is an algebraic remainder, with no
   smallness, derivative gain, or sign built into it.  This also confirms
   that the candidate does not silently discard finite-band or Leray terms.

6. The final scale discussion is only heuristic.  A commutator bound may
   trade a derivative on a high input for a derivative of the low weight,
   but this statement supplies neither a summable gain nor a nonzero signed
   value of the full expression.  The candidate properly declines both
   conclusions.  Nothing here passes to infinitely many bands,
   \(\epsilon=0\), an endpoint in time, HIGH-PRESSURE, or regularity.

REPLACEMENT ARGUMENT: Add the following standing hypothesis before (1):

> Work on \(\mathbb R^3\).  Let \(U,v\in\mathcal S(\mathbb R^3;\mathbb
> R^3)\) be divergence-free.  Let each \(\Delta_j\), for finite \(I\), be a
> real self-adjoint smooth Fourier multiplier mapping Schwartz functions to
> Schwartz functions, and let \(W=(\Delta_j)_{j\in I}\).  Let \(\mathbb P\)
> be the orthogonal Leray projector on \(L^2(\mathbb R^3)\), and fix
> \(\epsilon>0\).  Assume explicitly that \(WU\cdot Wv=0\) pointwise.

For this class, \(s_U-\epsilon\) and all differentiated factors have adequate
decay; \(s_U\) is bounded below by \(\epsilon\); every displayed integral is
finite; the Leray pairings are valid; and boundary terms vanish.  One can
justify (4)--(6) by pointwise differentiation and dominated convergence,
then derive (10)--(20) by the computations in Evidence 1--5.  This repairs
the first bad bridge without changing any formula or conclusion.  The same
calculation works on \(\mathbb T^3\) with smooth mean-zero fields and the
periodic Leray projector, but that is a separate declared setting and gives
no automatic whole-space conclusion.

CONDITIONAL SUFFIX THAT SURVIVES: With the replacement hypotheses, the entire
finite-band positive-\(\epsilon\) calculation (4)--(20) is exact.  It repairs
the HF07 omission by restoring low-mode feedback, weight variation, weighted
Leray commutators, and the explicit multiplier remainder.  It establishes
that the unweighted frozen-strain oracle alone is not an obstruction.  The
sign or cancellation of the complete expression still requires an explicit
field or wave-packet evaluation.

UNNECESSARY DEPENDENCIES: No Littlewood--Paley norm equivalence, infinite-band
limit, Navier--Stokes viscosity, continuation criterion, or historical HF
claim is used in this finite-dimensional differentiation.  Tight-frame
completeness is needed only for the special constant-weight cancellation
statement, not for (10)--(20).

NON-CLAIMS: This audit finds no derivative gain, small band-separation factor,
nonzero remainder, sign obstruction, pressure absorption, all-band identity,
endpoint estimate, or global regularity result.  An absolute bound on any
term would not establish that the full signed sum is nonzero.

REOPENING CONDITION: To advance beyond this repaired finite-band identity,
evaluate the complete sum (18)--(20) on explicitly admissible scale-separated
divergence-free data, including every commutator and multiplier defect, or
prove a signed estimate for the complete sum.  Any all-band or
\(\epsilon\downarrow0\) claim additionally needs uniform summable estimates
in a declared function class.

## Separate audit: exact periodic constant-weight diagnostic

VERDICT: **PASS**

REVIEWED SCOPE: `research/evidence/hf08-controller-constant-weight.md`, frozen
as an untracked file on base commit
`f0196f75b2c8dd92e2ea32199baf608753e23aa5` with SHA-256
`836c3f8c5492ef540bd7f9702e55a454d99b9a3fd495953b1984fbab997c5334`.

FIRST BAD BRIDGE: none.

EVIDENCE:

1. On \((\mathbb R/2\pi\mathbb Z)^3\),
   \(k\cdot a=N-N=0\), while
   \(l\cdot b=-N(1-1/N)-(1-N)=0\).  Thus \(U\) and \(v\) are real smooth
   divergence-free fields.  Since \(U\) depends only on \(z\) and \(U_3=0\),
   \((U\cdot\nabla)U=0\), hence \(V(U)=0\).

2. Radiality makes every component of the frequency-one field \(U\) acquire
   the same real multiplier \(m_j(0,0,1)\).  The tight-frame identity at that
   frequency gives
   \(|WU|^2=\sum_jm_j(0,0,1)^2|U|^2=1\).  Consequently
   \(s_U=\sqrt{\epsilon^2+1}\) is constant.  For sufficiently large \(N\),
   compactly supported dyadic multipliers place the frequency-one background
   and the two size-\(N\) perturbation frequencies in disjoint shell-index
   sets, so \(WU\cdot Wv=0\) pointwise.

3. The audited formula (11) applies.  Its third term is zero because
   \(V(U)=0\).  For \(f=U\) or \(f=v\), Parseval and self-adjointness give
   \[
      \langle Wf,Wg\rangle
       =\sum_{\xi\in\operatorname{supp}\widehat f}
          \widehat f(\xi)^*\widehat g(\xi)
          \sum_{j\in I}m_j(\xi)^2
       =\langle f,g\rangle.
   \]
   Only the tight-frame identity on the Fourier support of the first pairing
   argument \(f\) is used.  Therefore the first two terms reduce to
   \(c\{\langle U,V(v)\rangle+
   \langle v,V_{\rm lin}(U,v)\rangle\}=0\) by (13).  There is no requirement
   that \(W^*W V(v)=V(v)\), or that the finite interval cover frequencies
   produced by the high--high nonlinearity: components of \(V(v)\) outside
   the support of \(U\) have zero Fourier pairing with \(U\), and the same
   support-local argument applies to \(v\) and \(V_{\rm lin}\).

4. Writing \(K=Nx+Nz\) and \(L=-Nx+(1-N)z\), direct multiplication gives
   \[
   v_1v_3=-\cos^2K-(2-1/N)\cos K\sin L
           -(1-1/N)\sin^2L.
   \]
   Because \(\partial_zU_1=-\sin z\) and \(v_2=0\), the strain pairing is
   \(\langle-v_1v_3\sin z\rangle\).  The square terms have zero normalized
   mean against \(\sin z\), while
   \(\cos K\sin L=\frac12\{\sin z+\sin(L-K)\}\), and \(L-K\) has nonzero
   \(x\)-frequency.  Hence
   \[
      \langle v_iv_j\partial_jU_i\rangle
       ={2-1/N\over2}\langle\sin^2z\rangle
       ={2-1/N\over4}>0.
   \]
   Thus this example has a strictly positive frozen-strain oracle and an
   exactly zero complete second-order coefficient for every \(\epsilon>0\).

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: The diagnostic is an exact analytic
counterexample to the implication from a nonzero frozen-strain coefficient
to a nonzero complete square-energy second variation in the stated periodic,
finite-band, constant-weight setting.

UNNECESSARY DEPENDENCIES: A global tight-frame identity on every possible
output of \(V(v)\) is unnecessary.  The identity on the supports of \(U\)
and \(v\) suffices.  No variable-weight estimate or all-band limit is used.

NON-CLAIMS: The example does not show that the complete rate vanishes beyond
order \(h^2\), that a variable-weight remainder has either sign, that the
square-function route fails, or that a periodic trigonometric construction
transfers to Schwartz data on \(\mathbb R^3\).  It has no implication for HF
or global regularity.

REOPENING CONDITION: none for this diagnostic.  A stronger obstruction still
requires evaluation of the full variable/evolving-weight expression on an
admissible field family.
