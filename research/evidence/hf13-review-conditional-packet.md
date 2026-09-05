# HF13 independent audit: conditional homogeneous packet

Frozen input: base commit
`7afbff88ef95b44beb2157fe5a4b43eaf3a796c0`, with review input
`research/evidence/hf13-conditional-packet.md` at SHA-256
`9d8a4c7b4804ee90cee38c88ba00723f5632088cd49e0db1bea82bc456d4a487`.

## Verdict

**VERDICT: PASS, CONDITIONAL ON (5)--(6).**  For a fixed \(k>0\), the stated
background premise implies a compactly supported smooth solenoidal field on
which \(\mathcal J_k\) increases over a finite linear heat step.  The proof
does not construct or otherwise promote the background premise.

## Pressure derivative and global Taylor estimate

For \(p\ge0\), \(H_k(r,p)=pr\), so \(a_k(r,p)=r\).  For \(p=-q<0\), writing
\(s=(r^2+kq)^{1/2}\) gives
\[
 a_k(r,-q)
 =s+{kq\over2s}-{3\over2}\sqrt{kq}
   -{3\over2}\sqrt q.                                  \tag{R1}
\]
This tends to \(r\) as \(q\downarrow0\), and at \(r=0\) it equals
\(-3\sqrt q/2\).  The square-root terms in (R1), including
\(q/(r^2+kq)^{1/2}\), are uniformly one-half Holder in \(q\), independently
of \(r\ge0\).  This proves (11), including across \(p=0\).  Integrating the
derivative along the pressure segment proves
\[
 |H_k(r,p+\zeta)-H_k(r,p)-a_k(r,p)\zeta|
 \le C_k|\zeta|^{3/2}
\]
with a constant uniform in \(r,p\).  For
\(\zeta=\alpha^2b^2p_{w_N}\), integration gives exactly the uniform
\(O(b^3)\) remainder in (13), since
\(\sup_N\|p_{w_N}\|_{3/2}<\infty\).  This estimate includes the sets where
the perturbed pressure crosses zero.

On the packet ball, \(p_U\le-c\).  Uniformly there,
\[
 g_k(r,p_U)=-{\sqrt{(p_U)_-}\over2\sqrt k}r^2+O_{k,c}(r^4).
                                                               \tag{R2}
\]
The pressure perturbation does not spoil this expansion.  One direct check is
to apply the preceding Taylor estimate at both \(r\) and zero.  The two
remainders total \(O(b^3)\); because \(p_U\le-c\),
\(a_k(r,p_U)-a_k(0,p_U)=O_{k,c}(r^2)\), whose pairing with
\(b^2p_{w_N}\) is \(O(b^4)\).  Thus (R2), the global pressure Taylor term,
and the cubic packet give (15)--(16), uniformly in \(N\) and
\(\alpha\in[0,1]\).  This supplies the asserted crossing-set justification
without any \(L^\infty\) bound on \(p_{w_N}\).

## Riesz transfer and packet averaging

The growth estimate (4) gives
\(a_k(|U|,p_U)\in L^3\), because \(U\in L^3\) and
\(p_U\in L^{3/2}\).  The double Riesz multiplier is real and even, hence
self-adjoint under the legitimate \(L^3\)-\(L^{3/2}\) pairing.  Therefore
\[
 \int a_k(|U|,p_U)p_{w_N}
 =\int R_iR_j[a_k(|U|,p_U)](w_N)_i(w_N)_j.
\]
The curl packet has
\(w_N=\chi\cos(N\xi\cdot x)e+O_{L^s}(N^{-1})\) for every required
\(s\).  Weak periodic averaging of its quadratic tensor gives
\[
 (w_N)_i(w_N)_j\rightharpoonup {1\over2}\chi^2e_ie_j,
\]
while \(|w_N|^2\rightharpoonup\chi^2/2\).  These limits prove (18).  Its
first term is strictly negative by \(p_U\le-c\) and \(\chi\ne0\); its second
is strictly negative under (6), or under the stated weaker weighted-integral
premise.  Hence \(C_*<0\).

## Continuity and finite heat step

The modulated-envelope heat calculation gives (20)--(21).  The functional is
locally Lipschitz on \(L^3\): the quadratic pressure map obeys (22), changing
the speed at fixed pressure is controlled by
\(|\partial_rg_k|\le|p|\), and changing pressure at fixed speed is controlled
by \(|a_k(r,p)|\le C_k(r+\sqrt{|p|})\).  Holder pairs these coefficients in
\(L^3\) with pressure increments in \(L^{3/2}\).  The scalar cusps are covered
by the absolutely continuous line-segment argument and the same integrable
bounds.  Thus (24) follows from (21).

The quantifier order is valid: first fix \(k\), a background satisfying the
premise, its packet data, and \(\sigma\).  Then choose \(b\) so both uniform
\(O(b^3)\) errors are below a fixed fraction of
\((1-\lambda^2)|C_*|b^2\).  Finally choose \(N\) so \(C_N\le C_*/2<0\) and
the heat-transfer error is below the remaining margin.  Equation (25) is then
strictly positive.

## Audit record

**REVIEWED SCOPE:** conditional implication from (5)--(6); scalar derivative
and its uniform half-Holder bound; global Taylor remainder; pressure-sign
crossings; local velocity expansion; self-adjoint Riesz transfer; packet
tensor averaging; local \(L^3\) continuity; and parameter order.

**FIRST BAD BRIDGE:** none, conditional on the explicit background premise.

**REPLACEMENT ARGUMENT:** none.

**CONDITIONAL SUFFIX THAT SURVIVES:** any background satisfying (5)--(6), or
the stated weaker negative weighted integral, yields a finite heat-step
counterexample for that fixed \(k\).

**UNNECESSARY DEPENDENCIES:** no pointwise or \(L^\infty\) control of the
packet pressure and no differentiated heat identity are needed.

**NON-CLAIMS:** this audit does not establish existence of the background,
the premise for every \(k\), an Euler estimate, a Navier--Stokes trajectory
estimate, HIGH-PRESSURE, continuation, or global regularity.

**REOPENING CONDITION:** construct or refute a compact solenoidal background
satisfying the directional sign premise.
