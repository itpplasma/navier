# Audit of the radial and angular dynamics calculation

VERDICT: **REPAIR**

REVIEWED SCOPE: hf05-radial-dynamics.md at verified SHA-256
80e948a5f03be59ec722ace9ebe96df7cb5f586ffae7fc214d7818acac6a6b97,
on full base commit 62201652bafd1efa02d6789a341ab97a179f436d.

FIRST BAD BRIDGE: The statement that the nonnegative zero-set defect in
\(Z_\varepsilon\) is “needed to justify limiting inequalities” is too strong
without a uniform-integrability estimate. Pointwise convergence
\[
 Z_\varepsilon\to r|\nabla n|^2
\]
holds only on \(\{r>0\}\). At a zero of \(u\),
\(Z_\varepsilon=|\nabla u|^2/\varepsilon\), so neither \(Z_\varepsilon\) nor
the signed product
\(\Psi_\varepsilon\Delta\rho_\varepsilon\) has a supplied integrable
majorant. Positivity alone does not justify passage to the unregularized
evolution identity.

REPLACEMENT ARGUMENT: Retain equations (9), (13), (15), and (20) only as
exact identities for each fixed \(\varepsilon>0\). The scalar energy itself
does converge:
\[
 A_\varepsilon
 =\int\frac{r^2}{r_\varepsilon}|\nabla r|^2
 \longrightarrow\int r|\nabla r|^2=A,
\]
because \(0\le r^2/r_\varepsilon\le r\). Formula (11) and the angular
expansion (16) should be labeled pointwise/formal on \(\{r>0\}\). A genuine
\(\varepsilon\downarrow0\) evolution theorem requires separate uniform
bounds for the \(Z_\varepsilon\), Hessian, and signed product terms. With
this scope correction, the rest of the calculation is valid.

EVIDENCE:

1. Away from \(u=0\), \(u=rn\) gives
   \[
    |\nabla u|^2=|\nabla r|^2+r^2|\nabla n|^2.
   \]
   Hence the cubic dissipation is
   \[
    D_3=\int r|\nabla u|^2+\int r|\nabla r|^2=2A+B.
   \]
   The sum \(A+B=\int r|\nabla u|^2\) is weighted and is not the classical
   enstrophy \(\int|\nabla u|^2\).

2. The pressure exponents are correct:
   \[
    \|p\|_{9/4}\le C\|u\|_{9/2}^2
      \le C\|u\|_3\|u\|_9,
   \]
   \[
    \|r\nabla r\|_{9/5}
      \le\|r^{1/2}\|_{18}\|r^{1/2}\nabla r\|_2,
   \]
   and
   \(\|r\|_9^{3/2}\le(3/2)C A^{1/2}\). Thus
   \[
    |P_3|\le C\|u\|_3A.
   \]
   This proves absorption only under the displayed angular-dominance
   condition; it does not produce that condition dynamically.

3. With
   \(r_\varepsilon=(|u|^2+\varepsilon^2)^{1/2}\) and
   \(h_\varepsilon=u/r_\varepsilon\), direct differentiation gives
   \[
    \partial_t r_\varepsilon+u\cdot\nabla r_\varepsilon
      +h_\varepsilon\cdot\nabla p
     =\nu\Delta r_\varepsilon-\nu Z_\varepsilon,
   \]
   \[
    Z_\varepsilon
     =\frac{r_\varepsilon^2|\nabla u|^2
       -\sum_j|u\cdot\partial_ju|^2}{r_\varepsilon^3}\ge0.
   \]
   Cauchy--Schwarz proves the sign. On \(\{r>0\}\), the limit is exactly
   \(r|\nabla n|^2\).

4. For \(\rho_\varepsilon=r_\varepsilon^{3/2}\), the chain rule yields
   \[
    \rho_t+u\cdot\nabla\rho
      =\nu\Delta\rho-\Phi_\varepsilon-\Psi_\varepsilon-\Pi_\varepsilon
   \]
   with prefactors \(3\nu/4\), \(3\nu/2\), and \(3/2\), respectively.
   Since \(A_\varepsilon=(4/9)\|\nabla\rho_\varepsilon\|_2^2\), pairing with
   \(-\Delta\rho_\varepsilon\) gives the factor \(9/8\) in front of
   \(A_\varepsilon'\). Integration of transport gives
   \[
    -\int\partial_i u_j\,\partial_i\rho_\varepsilon
                         \partial_j\rho_\varepsilon,
   \]
   with the sign stated in (15).

5. Formally on \(\{r>0\}\),
   \(\Psi=(3\nu/2)r^{3/2}|\nabla n|^2\). Integration by parts gives exactly
   \[
    -\frac{27\nu}{8}\int r|\nabla r|^2|\nabla n|^2
    -\frac{9\nu}{4}\int r^2\nabla(|\nabla n|^2)\cdot\nabla r.
   \]
   The first term is favorable and the second has no fixed sign. The Young
   estimate at fixed \(\varepsilon\) introduces
   \(C\nu\|r_\varepsilon^{1/2}Z_\varepsilon\|_2^2\), whose formal limit is
   \(C\nu\int r^3|\nabla n|^4\), beyond \(B\).

6. Writing \(b_\varepsilon=u/r_\varepsilon^{1/2}\), integration by parts in
   the pressure term gives both
   \((\partial_i b_{\varepsilon,k})(\partial_kp)\) and
   \(b_{\varepsilon,k}\partial_i\partial_kp\), with the coefficient
   \(-3/2\). The alternative Young bound introduces a weighted
   pressure-gradient norm. These identities expose uncontrolled terms; their
   available upper bounds alone prove no sign theorem or general no-go result.

7. The simpler \(K_\varepsilon=\|\nabla r_\varepsilon\|_2^2\) identity has
   the same transport and pressure-Hessian signs. Since it is unweighted, it
   does not control \(A\) without a speed bound.

8. The periodic shear is an independent behavioral oracle. For
   \(u_0=(\cos\varphi(z),\sin\varphi(z),0)\), convection vanishes and the
   exact solution is componentwise heat flow. Direct Taylor expansion gives
   \[
    r_t(0)=-\nu(\varphi')^2,\qquad
    \partial_zr(t)=-2\nu t\varphi'\varphi''+O(t^2),
   \]
   and therefore
   \[
    A(t)=4\nu^2t^2\int_{\mathbb T^3}
             (\varphi'\varphi'')^2+o(t^2).
   \]
   This disproves propagation of the naive condition \(A=0\) in the
   periodic class. It is not an R3 concentration example.

CONDITIONAL SUFFIX THAT SURVIVES: If a new coupled radial-angular functional
cancels the signed transfer and controls the pressure-Hessian and strain
terms uniformly through \(\varepsilon\downarrow0\), it could feed the
angular-dominance absorption condition. No such functional is constructed.

UNNECESSARY DEPENDENCIES: The periodic oracle is not needed to derive the
regularized identities; it independently tests the proposed propagation
mechanism.

NON-CLAIMS: The audit proves no angular dominance, pressure absorption,
high-frequency estimate, general impossibility theorem, or regularity result.
Uncontrolled absolute bounds do not determine the sign of the angular
transfer.

REOPENING CONDITION: Supply a coupled weighted evolution with uniform
zero-set control and input-only bounds for its signed direction,
pressure-Hessian, and strain terms.
