# Independent audit of the variable-weight square-energy diagnostic

VERDICT: **REPAIR**

REVIEWED SCOPE: `research/evidence/hf08-variable-weight.md`, frozen as an
untracked file on base commit
`f0196f75b2c8dd92e2ea32199baf608753e23aa5` with SHA-256
`06777115804e38e7eeaad7ae7c0c5990d7785ff8cef80267b8b57e038ed78d15`.

FIRST BAD BRIDGE: The existence paragraph for the smooth tight dyadic frame
only says to "arrange" that squared translates sum to one.  That operation is
the substantive compatibility condition between a unit plateau, smoothness,
support shorter than two logarithmic units, and tightness.  A concrete
construction is needed.  In addition, the reduction of the first term in
(9) cannot be justified by commuting the low multiplier through the variable
weight: \(sU\) has infinitely many \(z\)-harmonics.  The claimed reduction is
nevertheless valid by the support-local argument supplied below.

EVIDENCE:

1. Let \(a=\log_2(1+\delta)\in(0,1)\).  Choose a smooth function
   \(\theta:[a,1]\to[0,\pi/2]\), equal to zero to infinite order at \(a\)
   and to \(\pi/2\) to infinite order at \(1\).  Define a smooth logarithmic
   profile \(q\) by
   \[
   q(t)=\begin{cases}
   \sin\theta(t+1),&a-1<t<0,\\
   1,&0\leq t\leq a,\\
   \cos\theta(t),&a<t<1,\\
   0,&\text{otherwise}.
   \end{cases}
   \]
   The flat endpoints make \(q\in C^\infty(\mathbb R)\), its support has
   length \(2-a<2\), and for every \(t\), exactly a plateau term or the two
   adjacent transition terms contribute, with squared sum
   \(\cos^2\theta+\sin^2\theta=1\).  Thus
   \(m_0(r)=q(\log_2r)\) for \(r>0\), extended by zero at the origin, and
   \(m_j(\xi)=m_0(2^{-j}|\xi|)\) give a smooth real radial annular frame away
   from the origin satisfying (1)--(2).  This completes the construction
   asserted tersely in the candidate.

2. The frequencies of \(U\) have length one.  Those of \(v\) are
   \((\pm K,0,\pm1)\) with correlated signs and \((\pm K,0,0)\).  Condition
   (3) places them in the high plateau, and large \(J\) separates the active
   low and high shell indices.  Hence \(WU=(U,0)\), \(Wv=(0,v)\), and
   \(WU\cdot Wv=0\).  Also \(U\) depends only on \(z\) while pointing in the
   \(x\)-direction, so \((U\cdot\nabla)U=0\) and \(V(U)=0\).

3. For the first term of the exact coefficient, the \(x\)-average of the
   quadratic field \(V(v)\) can only use opposite \(x\)-frequencies from the
   two modes of \(v\).  Its nonzero \(z\)-frequencies are therefore only
   \(\pm1\); all other quadratic outputs have nonzero \(x\)-frequency or
   zero \(z\)-frequency.  Since \(sU\) is independent of \(x\), only these
   \(x\)-zero, frequency-one outputs enter its pairing with \(V(v)\), and
   \(\Delta_0\) is exactly one there.  Consequently
   \[
      \langle sWU,WV(v)\rangle=\langle sU,V(v)\rangle.
   \]
   This does not require \(\Delta_0(sU)=sU\), which is false in general, or
   any plateau property at the high--high output frequencies.

4. Every Fourier mode of \(V_{\rm lin}(U,v)\) has \(x\)-frequency \(\pm K\)
   and \(z\)-frequency of absolute value at most two.  Equations
   (3)--(4) put all of them in the high plateau.  Therefore the second exact
   pairing is \(\langle sv,V_{\rm lin}(U,v)\rangle\).  The third term is zero
   by \(V(U)=0\).  This proves (9) with all relevant finite-band multipliers
   retained; it is not a scalar-multiplier approximation.

5. Directly differentiating (6) gives
   \[
   v_x=-\sin(Kx+z),\qquad
   v_z=K\sin(Kx+z)-K\cos(Kx).
   \]
   Taking divergence of the linearized Euler equation yields (10).  One
   explicit zero-mean solution is
   \[
   p_{\rm lin}=-{AK^2\over K^2+4}\sin(Kx+2z)+A\sin(Kx)
    -{AK^2\over K^2+1}\cos(Kx-z)
    +{AK^2\over K^2+1}\cos(Kx+z).
   \]
   This verifies the inversion of every nonzero Fourier mode and fixes the
   pressure convention up to an irrelevant constant.

6. Integration by parts in (9) cancels the unweighted strain and transport
   terms.  Also \(\operatorname{div}(sU)=\partial_x(sA\cos z)=0\), so the
   nonlinear pressure in \(V(v)\) has zero pairing with \(sU\).  The
   remainder is exactly (11).  Substitution of the displayed pressure gives
   the \(\sin2z\) coefficient
   \[
   {AK\over4}-{3AK^3\over2(K^2+1)(K^2+4)},
   \]
   whose positive-frequency complex Fourier coefficient is precisely
   \[
   -{iAK(K^4-K^2+4)\over8(K^2+1)(K^2+4)}.
   \]
   Thus (12)--(13), including the Leray correction and its sign, are correct.

7. Since
   \(s'=-A^2\sin(2z)/(2s)\), integration by parts gives (14).  Pairing the
   conjugate \(\pm2\) modes then gives exactly (8).  Its prefactor is
   negative because \(A,K>0\), \(K^4-K^2+4>0\), and the displayed integral
   is strictly positive.  Replacing \(\sin(Kx)\) by \(-\sin(Kx)\) reverses
   every cross interaction that produces the \(x\)-average at frequency
   \(2\), while same-mode terms cannot pair with \(s'\); hence the full
   coefficient changes sign.

REPLACEMENT ARGUMENT: Replace the informal frame-construction sentence by
the explicit \(q,\theta\) construction in Evidence 1, and insert the
support-local arguments of Evidence 3--4 in place of the bare assertion that
the plateau identities imply (9).  These changes prove the claimed frame
exists and justify (9) without falsely commuting a Fourier multiplier with
the variable weight.  Equations (10)--(14) then prove the proposition exactly.

CONDITIONAL SUFFIX THAT SURVIVES: After this repair, (8) is a rigorous exact
finite-band, positive-\(\epsilon\), periodic example in which the full
variable-weight second variation is nonzero and takes either sign under a
phase reversal.  It rules out an additional universal algebraic cancellation
identity in this setting.

UNNECESSARY DEPENDENCIES: No multiplier values are needed at high--high
outputs outside the pairings identified above.  No all-band square-function
equivalence, limiting argument, viscosity, or Navier--Stokes trajectory is
used.

NON-CLAIMS: The norm of the displayed perturbation grows with \(K\), since
\(v_z\) has amplitude of order \(K\).  The nonzero coefficient therefore
does not refute a normalized high--low gain or prove a scale-uniform lower
bound.  It gives no \(\mathbb R^3\) transfer, time-integrated pressure
estimate, failure of HIGH-PRESSURE, derivative gain, regularity result, or
global conclusion.

REOPENING CONDITION: To obtain a normalized scale obstruction, exhibit a
family with controlled declared norms and compare the complete coefficient
to the proposed gain.  Any whole-space use additionally requires localized
wave packets with quantitative Leray and multiplier-error control.
