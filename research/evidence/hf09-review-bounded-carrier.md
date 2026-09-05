# Independent audit of the bounded-carrier variable-weight diagnostic

VERDICT: **PASS**

REVIEWED SCOPE: `research/evidence/hf09-bounded-carrier.md`, frozen as an
untracked file on base commit
`f0196f75b2c8dd92e2ea32199baf608753e23aa5` with SHA-256
`a5a7f7e3719e60cf987c31421ba6fe083c7289212b9d7a8bf19f025a45384b0c`.

FIRST BAD BRIDGE: none.

EVIDENCE:

1. The fixed frame (1)--(4) exists as stated.  Since
   \(a=\log_2(8/5)\in(0,1)\), the support of \(r\) is contained in
   \([a-1,1]\), an interval shorter than two.  The constant endpoint
   neighborhoods of \(\alpha\) make all four joins in (1) smooth.  On a
   translate of \([0,a]\), one term equals one and all others vanish; on a
   translate of \([a,1]\), the only terms are
   \(\cos\alpha(t)\) and \(\sin\alpha(t)\).  Thus translation gives
   \(\sum_jr(t-j)^2=1\) everywhere.  Composing with \(\log_2|\xi|\) gives
   smooth real radial annular multipliers away from zero, and the construction
   is independent of \(N\).

2. The polarizations satisfy
   \(k\cdot a_0=N-N=0\) and
   \(\ell\cdot b_0=-N(1-N^{-1})-(1-N)=0\).  Orthogonality of the distinct
   trigonometric modes and normalized torus integration give
   \[
   \|v_N\|_2^2={|a_0|^2+|b_0|^2\over2}
    ={3+(1-N^{-1})^2\over2}\le2.
   \]
   This is a uniform upper bound, unlike the preceding growing-carrier
   example.

3. Multiplying a carrier by either frequency of \(U\) changes its
   \(z\)-frequency by one.  The resulting linearized frequencies have
   \(x\)-frequency of magnitude \(N\) and \(z\)-frequency among those in
   (8), up to simultaneous signs and repetitions.  Their smallest length is
   at least \(N\).  Their largest possible length is
   \(\sqrt{N^2+(N+1)^2}\), and for \(N\ge8\),
   \[
      1+(1+N^{-1})^2\le 1+(9/8)^2< (8/5)^2.
   \]
   Thus every carrier and linearized mode lies in the single fixed high
   plateau.  The low and high shells are disjoint, proving (9) and the
   pointwise orthogonality required by the exact second-variation formula.

4. The first pairing in (10) does not require the high plateau to contain all
   high--high outputs.  Opposite carrier \(x\)-frequencies give the only
   \(x\)-independent nonzero beat that can pair with \(sU\), at
   \((0,0,\pm1)\), where \(m_0=1\).  Outputs with nonzero \(x\)-frequency
   pair to zero with \(sU\).  Self-adjointness therefore reduces the first
   finite-band pairing exactly.  The high plateau contains every mode of
   \(V_{\rm lin}(U,v_N)\), so the second pairing reduces exactly as well.
   Since \((U\cdot\nabla)U=0\), the background-weight term vanishes.  This
   proves (10) without an implicit complete-frame assumption on \(V(v_N)\).

5. Direct multiplication gives
   \[
   (v_N)_1(v_N)_3=-\cos^2(k\cdot x)
    -(2-N^{-1})\cos(k\cdot x)\sin(\ell\cdot x)
    -(1-N^{-1})\sin^2(\ell\cdot x).
   \]
   The normalized \(x\)-averages of the square terms are \(1/2\), and
   \(k+\ell=(0,0,1)\) gives the cross average \(\frac12\sin z\).  This proves
   (13).  Since \(s'U=-A^3\cos^2z\sin z/s\), its product with the constant
   part of (13) is odd in \(z\), while the \(\sin z\) part yields exactly
   (14).  Hence \(L_N>0\) and
   \(L_N\to A^3I_{A,\epsilon}>0\).

6. Taking divergence of the linearized equation gives (12), with no omitted
   pressure term.  Every right-hand-side mode has \(|\xi_x|=N\), so the
   inverse Laplacian has multiplier magnitude at most \(N^{-2}\).  Also
   \((v_N)_3=-\cos(k\cdot x)-\sin(\ell\cdot x)\), whence orthogonality gives
   \(\|(v_N)_3\|_2=1\) and
   \(\|\partial_x(v_N)_3\|_2=N\).  Therefore
   \[
   \|p_N\|_2\le {2A\over N},\qquad
   |\langle s'(v_N)_3p_N\rangle|
     \le {A^2\over2\epsilon}\,{2A\over N}
     ={A^3\over\epsilon N}.
   \]
   All constants and normalized torus norms in (15)--(18) are correct.

7. Since \((2-N^{-1})/2\to1\), the lower bound (20) follows from (18) for
   sufficiently large dyadic \(N\), with \(A,\epsilon\) fixed.  Flipping the
   sign of the second carrier leaves each same-carrier quadratic term
   unchanged and reverses every cross-carrier term.  Same-carrier convective
   terms are constant after \(x\)-averaging and pair to zero with the odd
   factor \(s'U\); same-carrier pressure terms have odd \(z\)-frequency and
   pair to zero with \(s'\), whose nonzero Fourier frequencies are even.
   Thus the surviving complete coefficient reverses sign exactly.

8. If (21) held for this fixed frame with finite \(C(U,\epsilon)\) independent
   of \(N\), its right side would be at most
   \(2C(U,\epsilon)N^{-\gamma}\to0\), whereas (20) bounds the left side away
   from zero.  The contradiction proves precisely the claimed absence of a
   universal positive-power high--low gain for this normalized periodic
   family.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: The full candidate survives.  For one fixed
smooth radial tight frame and fixed \(A,\epsilon>0\), there is a dyadic
sequence of smooth periodic divergence-free perturbations with uniformly
bounded \(L^2\) mass whose exact finite-band variable-weight second variation
is bounded away from zero and takes either sign under a phase flip.  This
falsifies estimates of the exact form (21) in that setting.

UNNECESSARY DEPENDENCIES: No exact formula for \(p_N\) is needed; its Fourier
support and the inverse-Laplacian bound suffice.  No completeness of the
finite band on all outputs of \(V(v_N)\), infinite-band equivalence, viscosity,
or evolution equation is used.

NON-CLAIMS: The obstruction concerns one fixed periodic plateau frame and an
instantaneous finite-band second variation.  It does not exclude estimates
with other normalization, additional structure, time integration, or
viscous terms.  It supplies no localization to \(\mathbb R^3\), no statement
about arbitrary frames, no HIGH-PRESSURE implication, and no regularity or
global conclusion.

REOPENING CONDITION: A whole-space or spacetime obstruction requires a
separate localized construction with uniform control of Leray and multiplier
errors, followed by comparison with the exact proposed normalized estimate.
