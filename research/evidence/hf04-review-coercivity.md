# Audit of full-heat modified-energy coercivity

VERDICT: **PASS**

REVIEWED SCOPE: hf04-controller-coercivity.md at verified SHA-256
7a58cf78f64326bd4ded8657aa8969299c9c64ae24bafa90b711ecc0f016116a,
on full base commit 00b1fa3ff95785fe0232e60864498ab02ee90fd7. The
claim concerns the direct functional
\[
 F_J(u)=\frac13\|u\|_3^3-cB_J(u),\qquad
 B_J(u)=-\int_0^\infty H_J(G_su)\,ds,
\]
for fixed \(J\), \(\nu>0\), and \(c\ne0\).

FIRST BAD BRIDGE: none.

EVIDENCE:

1. For each solenoidal Schwartz field, the full-heat integrals defining
   \(B_J\) and \(B\) are finite. On \(0\le s\le1\), heat evolution preserves
   the needed Schwartz norms uniformly and
   \[
    |H_J(v)|+|P(v)|\le C\|v\|_6^3\|\nabla v\|_2.
   \]
   For \(s\ge1\), heat smoothing gives the integrable majorant
   \(C(\nu s)^{-2}\|u\|_2^4\), uniformly in the low-pass scale.

2. The semigroup sign is correct:
   \[
    B(G_tu)=-\int_t^\infty P(G_su)\,ds,\qquad
    \frac d{dt}B(G_tu)=P(G_tu).
   \]
   The independently audited compact profile has \(P(u)>0\), so continuity
   makes \(B(G_tu)\) nonconstant near \(t=0\). Some heat-evolved Schwartz
   field \(\phi\) therefore has \(B(\phi)\ne0\). Since pressure is even and
   \(u\cdot\nabla|u|\) is odd under \(u\mapsto-u\),
   \(B(-\phi)=-B(\phi)\); one may arrange \(cB(\phi)>0\).

3. For positive amplitude \(a\), heat linearity gives
   \(B_J(au)=a^4B_J(u)\) and \(B(au)=a^4B(u)\), while
   \(\|au\|_3^3=a^3\|u\|_3^3\).

4. Fix exact energy \(E>0\), set
   \[
    N=\frac{a^2\|\phi\|_2^2}{E},\qquad
    u_a(x)=aN\phi(Nx).
   \]
   Then
   \[
    \|u_a\|_2^2=a^2N^{-1}\|\phi\|_2^2=E
   \]
   exactly. Spatial scaling gives an \(N^2\) factor in pressure work, and
   the substitution \(r=N^2s\) cancels it in the heat-time integral:
   \[
    B_J(u_a)=a^4B_{\kappa_a}(\phi),\qquad
    \kappa_a=\frac{2^J}{N}\longrightarrow0.
   \]

5. For every fixed \(s\ge0\),
   \[
    \|S_{\kappa}p[G_s\phi]\|_3
      \le C\kappa^{1/2}\|p[G_s\phi]\|_2\longrightarrow0.
   \]
   This is the three-dimensional low-frequency Bernstein estimate from
   \(L^2\) to \(L^3\), combined with the \(L^2\) multiplier bound.
   Pairing with
   \(G_s\phi\cdot\nabla|G_s\phi|\in L^{3/2}\) proves
   \(H_\kappa(G_s\phi)\to P(G_s\phi)\).

6. Dominated convergence is valid on the entire heat interval. Near
   \(s=0\), the uniform Schwartz bound in item 1 dominates independently of
   \(\kappa\); near infinity, the same item supplies
   \(C(\nu s)^{-2}\|\phi\|_2^4\). Hence
   \[
    B_{\kappa_a}(\phi)\to B(\phi).
   \]
   Since \(\|u_a\|_3^3=a^3\|\phi\|_3^3\),
   \[
    F_J(u_a)
      =\frac{a^3}{3}\|\phi\|_3^3
       -ca^4(B(\phi)+o(1))\longrightarrow-\infty.
   \]
   Therefore no finite energy-only lower bound exists at any exact
   \(E>0\). For the full-pressure inverse the same conclusion follows
   directly from \(B(u_a)=a^4B(\phi)\).

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: Starting the heat inverse at zero removes
the short-heat defect for a fixed Schwartz snapshot, but the direct additive
modified energy loses coercivity even on an exact fixed-energy shell.

UNNECESSARY DEPENDENCIES: No Navier--Stokes trajectory, continuation theorem,
or finite-time singularity assumption is used after the audited existence of
a profile with nonzero pressure work.

NON-CLAIMS: This theorem obstructs only the direct linear correction
\(\|u\|_3^3/3-cB_J(u)\). It does not exclude nonlinear saturation, another
modified functional, additional trajectory information, the spacetime HF
hypothesis, or global regularity. The constructed fields are snapshots, not
one evolution.

REOPENING CONDITION: none for this coercivity obstruction. A proposed
replacement functional requires a separate chain-rule and coercivity audit.
