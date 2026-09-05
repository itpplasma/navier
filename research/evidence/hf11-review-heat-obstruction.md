# Independent audit of the HF11 heat obstruction

**VERDICT: REPAIR.**  The fixed-positive-regularizer heat counterexample is
valid after one quantitative correction.  The averaging limit (14) only
implies a lower bound with, for example, \(Q/2\) for all sufficiently large
\(N\); it does not by itself imply the \(O(aN)\) averaging remainder asserted
in (17).  Replacing the leading \(Q\) there by \(Q/2\) and adjusting the
fractions completes the proof.

## Reviewed scope

I reviewed “research/evidence/hf11-heat-obstruction.md” at SHA-256
“526669db40d221e24e6bcb4f69bc8b820c8dfa19d7819314ad5c8b171048567d”,
relative to base commit
“f3e7605b8247a3e4b6a22739663cf4d7c97750df”.  The scope is the existence of
fixed \(\epsilon,\delta>0\) and smooth compactly supported solenoidal
\(u_N\) for which
\(D\mathcal K_{\epsilon,\delta}(u_N)[\Delta u_N]>0\).
No Euler evolution, unregularized limit, or trajectory conclusion is under
review.

## Reconstruction

### 1. The background pressure is strictly negative

For the convention
\[
 \widehat{R_iR_jh}(\xi)=-{\xi_i\xi_j\over|\xi|^2}\widehat h(\xi),
\]
the off-support kernel is
\[
 K_{ij}(x)={3x_ix_j-\delta_{ij}|x|^2\over4\pi|x|^5}. \tag{A1}
\]
The azimuthal background satisfies \(y\cdot U(y)=0\).  Contracting (A1)
with \(U_iU_j\), and using evenness of the kernel, gives exactly
\[
 p_U(0)=-\int {|U(y)|^2\over4\pi|y|^3}\,dy<0.         \tag{A2}
\]
The cylindrical support condition \(1<r<2\) puts the support outside the
Euclidean unit ball.  Thus \(p_U\) is smooth there, and continuity supplies
the ball \(B\) and constant \(c>0\) in (6).  There is no missing principal
value or pressure-gauge term in this off-support calculation.

### 2. Frequency and support algebra

The curl construction makes \(w_N\) smooth, compactly supported in \(B\),
and exactly divergence free.  Direct differentiation of (8) gives
\[
 \|w_N\|_q=O(1),\quad \|\Delta w_N\|_q=O(N^2),\quad
 w_N\cdot\Delta w_N
 =-N^2\chi^2\cos^2(Nx_1)+O_{L^q}(N),                 \tag{A3}
\]
including \(q=\infty\).

Because the supports of \(U\) and \(w_N\), together with all their
derivatives, are disjoint, the pointwise cross products in both quadratic
pressure sources vanish before applying the nonlocal Riesz transforms.
Hence both decompositions in (11) are exact.  Nonlocality does not recreate a
cross source after its input has vanished.

On \(B\), \(u_N=aw_N\) and
\(r_{a\epsilon _0}=a(\epsilon _0^2+|w_N|^2)^{1/2}\).  Therefore the
\(p_U/r_\epsilon\) part of the first line of (12) has exactly the factor \(a\)
in (13), with no lost amplitude.  Equation (A3), the explicit expansion
\[
 w_N=-\chi\cos(Nx_1)e_2+O_{C^0}(N^{-1}),
\]
and periodic averaging give
\[
 {T_N\over aN^2}\longrightarrow Q,                   \tag{A4}
\]
where \(Q>0\) because \(p_U\le-c\), the averaged integrand is nonnegative,
and \(\chi\) is nonzero.

### 3. All remaining nonlocal pairings

Calderón--Zygmund boundedness and (A3) give
\[
 \|p_{w_N}\|_{3/2}=O(1),\qquad
 \|R_iR_j(w_{N,i}\Delta w_{N,j})\|_{3/2}=O(N^2).
                                                               \tag{A5}
\]
These bounds account for the nonlocal tails outside \(B\).

On \(B\), the cubic-speed term is \(O(a^3N^2)\).  The
\(a^2p_{w_N}\) pressure-speed term is also \(O(a^3N^2)\), since
\[
 {a^2|p_{w_N}|\over
  a(\epsilon _0^2+|w_N|^2)^{1/2}}\,
 |aw_N\cdot a\Delta w_N|
 \lesssim_{\epsilon _0}a^3|p_{w_N}||w_N||\Delta w_N|,
\]
and Hölder uses (A3)--(A5).

For the pressure-evolution source, the uniform mollifier estimate gives
\[
 \|\Phi_\delta'(p_U+a^2p_{w_N})\|_3
 \lesssim\|p_U+a^2p_{w_N}\|_{3/2}^{1/2}=O(1).         \tag{A6}
\]
Pairing (A6) with the high source in (A5), including its prefactor \(a^2\),
is \(O(a^2N^2)\).  The \(\rho_\epsilon\) factor is \(O(a|w_N|)\) on \(B\),
giving \(O(a^3N^2)\); outside \(B\), its fixed \(L^3\) bound paired with the
nonlocal high source gives \(O(a^2N^2)\).

The background terms are uniformly \(O(1)\).  In particular, the potentially
singular factor in the change of the background pressure-speed term is
harmless:
\[
 \left|{U\cdot\Delta U\over
  (a^2\epsilon _0^2+|U|^2)^{1/2}}\right|
 \le|\Delta U|,                                      \tag{A7}
\]
uniformly for \(0<a\le1\).  Pairing (A7) with
\(a^2p_{w_N}\in L^{3/2}\) gives the claimed \(O(a^2)\) change.  The remaining
low-source terms are bounded by the same \(L^3\)-\(L^{3/2}\) pairings.
Thus every term outside \(T_N\) has the amplitude and frequency bounds used
in the proof; no nonlocal contribution has been omitted.

## First bad bridge and repair

The first unsupported implication is the passage from the qualitative limit
(14) to (17) with
\[
 T_N\ge aN^2Q-C_1aN.                                 \tag{A8}
\]
Dominated periodic averaging establishes (A4), but without an explicit
quantitative averaging lemma it does not establish the \(O(N^{-1})\) rate in
(A8).  The \(O(aN)\) envelope error from (A3) is separate from the convergence
rate of the leading oscillatory average.

No rate is needed.  Since \(a>0\) is a scalar prefactor and (A4) is independent
of \(a\), there exists \(N_0\), depending only on the already fixed
\(U,\chi,\epsilon _0\), such that
\[
 T_N\ge {aQ\over2}N^2\qquad(N\ge N_0).                \tag{A9}
\]
Combining (A9) with the audited bounds above gives
\[
 D\mathcal K_{a\epsilon _0,\delta}(u_N)[\Delta u_N]
 \ge {aQ\over2}N^2-C_2(a^2+a^3)N^2-C_3.             \tag{A10}
\]
The separate \(O(aN)\) envelope term may be retained on the right without
changing the argument.  Choose \(a\in(0,1]\) so that
\[
 C_2(a^2+a^3)\le {aQ\over8}.
\]
This fixes the positive regularizer \(\epsilon=a\epsilon _0\).  Then take a
single integer
\[
 N\ge N_0
\]
large enough that \(C_3\), and the optional \(C_1aN\) term if retained,
consume at most \(aQN^2/8\).  Equation (A10) is then at least
\(aQN^2/4>0\).  This is the required exact counterexample.

## Audit result

**FIRST BAD BRIDGE:** the unproved \(O(N^{-1})\) rate implicit in (17)'s use
of the exact leading coefficient \(Q\).

**EVIDENCE:** (A1)--(A2) verify the pressure kernel and strict sign.
(A3)--(A7) verify support separation, amplitude powers, the nonlinear
pressure source, and every nonlocal pairing.  Equations (A9)--(A10) repair the
only quantitative gap using the qualitative averaging limit actually proved.

**REPLACEMENT ARGUMENT:** replace the leading \(aN^2Q\) in (17) by
\(aN^2Q/2\) for \(N\ge N_0\), then use the choices following (A10).

**CONDITIONAL SUFFIX THAT SURVIVES:** for fixed positive
\(\epsilon=a\epsilon _0\) and fixed \(\delta>0\), a smooth compactly
supported solenoidal field with strictly positive full heat direction exists.
Therefore the regularized pressure entropy has no universal dissipative heat
sign.  Static coercivity is unaffected.

**UNNECESSARY DEPENDENCIES:** no explicit averaging rate is needed.  The
argument needs only convergence in (14), followed by selection of a
sufficiently large carrier.

**NON-CLAIMS:** no \(\epsilon,\delta\downarrow0\) limit, Euler compensation,
trajectory obstruction, HIGH-PRESSURE estimate, blow-up statement, or
regularity conclusion follows.

**REOPENING CONDITION:** none after the replacement argument.  Reinstating
the sharper original form of (17) would require an explicit quantitative
periodic-averaging estimate.
