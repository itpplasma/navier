# Independent audit of the pressure-entropy mechanism

VERDICT: **REPAIR**

REVIEWED SCOPE: `research/evidence/hf11-pressure-entropy.md` at SHA-256
`56c6e9e2de0521125be1e6d06a18457a09343d58d518c09632ac7b0bd5946356`,
on full base commit `f546d2538b90dda56469b5f5bb490b5be477bd7d`.
This audit checks static coercivity, the scalar regularization, every sign in
the fixed-regularizer evolution, finiteness of its terms, and applicability to
an actual compact classical Navier--Stokes interval.  It does not test a heat
sign on a special field and does not promote the mechanism.

FIRST BAD BRIDGE: There is no algebraic error through (16).  The first
applicability gap is the assumption in Section 3 that the solution remains
smooth and rapidly decreasing throughout the time interval.  Persistence of
Schwartz decay is neither supplied nor part of the available classical
trajectory hypothesis.  If “along smooth Navier--Stokes flow” in the opening
claim is meant to include the actual maximal classical trajectory, the stated
proof is therefore too narrow.  This is repairable without a decay theorem:
for every \(0<T<T_*\), the identities hold under
\[
 u\in C([0,T];H^m),\qquad u_t\in C([0,T];H^{m-2}),\qquad m\ge4,       \tag{R1}
\]
with the Riesz-transform pressure gauge.  The exact repair is given below.

EVIDENCE:

1. The pointwise coercivity is correct.  On \(p<0\), putting
   \(z=\sqrt{-p}\), maximization in \(r\ge0\) gives
   \[
   rz^2-{r^3\over6}\le {2\sqrt2\over3}z^3,
   \]
   with equality at \(r=\sqrt2z\).  Since
   \(1-2\sqrt2/3>0\), (3)--(4) follow.  On \(p\ge0\) the integrand is at
   least \(r^3/3\).  The upper bound follows from the
   \(L^{3/2}\)-boundedness of the double Riesz transform and Hölder.  Thus
   \[
   {1\over6}\|u\|_3^3\le\mathcal K(u)\le C\|u\|_3^3
   \]
   is valid.  In fact the lower pointwise argument uses no solenoidality or
   pressure equation; those enter only in identifying the chosen \(p\).

2. The entropy regularizer has the asserted properties.  The function
   \(q\mapsto q_-^{3/2}\) is convex, and its derivative is globally
   Hölder continuous with exponent \(1/2\).  Convolution preserves convexity
   and that seminorm.  Subtracting the tangent at zero therefore gives
   \(\Phi_\delta(0)=\Phi_\delta'(0)=0\),
   \(\Phi_\delta''\ge0\), and
   \[
   |\Phi_\delta'(q)|\le C|q|^{1/2},\qquad
   |\Phi_\delta(q)|\le C|q|^{3/2},                              \tag{R2}
   \]
   uniformly in \(\delta\).  For fixed \(\delta\), smoothness and the
   vanished tangent also give \(O_\delta(q^2)\) at zero.  Hence the entropy
   is integrable when \(p\in L^2\cap L^{3/2}\), without assuming
   \(p\in L^1\).  Pointwise convergence and the second bound in (R2) justify
   \(\Phi_\delta(p)\to p_-^{3/2}\) in \(L^1\).  The subtracted linear term
   causes no \(L^1\) problem because domination is applied to the complete
   \(\Phi_\delta(p)\), not to that term separately.

3. Differentiation of the fixed Riesz representative gives
   \[
   p_t=2R_iR_j(u_i u_{j,t}).
   \]
   Substitution of \(u_t=\nu\Delta u+V\), commutation with \(\Delta\), and
   \[
   \Delta(u_i u_j)=u_i\Delta u_j+u_j\Delta u_i
                   +2\partial_k u_i\partial_k u_j
   \]
   yield exactly (12), including the minus sign in
   \(-2\nu R_iR_j(G_{ij})\).

4. The nonlinear part (15) is exact.  The velocity derivative of
   \((r_\epsilon^3-\epsilon^3)/3+p\rho_\epsilon\) is
   \((r_\epsilon+p/r_\epsilon)u\), while the total coefficient of \(p_t\)
   is \(w_{\epsilon,\delta}=\rho_\epsilon+\Phi_\delta'(p)\).
   Inserting the \(V\)-part of \(p_t\) gives the factor two in its Riesz
   term.  Since \(\epsilon>0\), there is no zero-set differentiation issue.

5. The heat signs and coefficients in (16) are correct.  Direct integration
   by parts gives
   \[
   \begin{split}
   \int(r_\epsilon+p/r_\epsilon)u\cdot\Delta u
   ={}&-\int r_\epsilon(|\nabla u|^2+|\nabla r_\epsilon|^2)\\
     &-\int {p\over r_\epsilon}
       (|\nabla u|^2-|\nabla r_\epsilon|^2)
       -\int\nabla p\cdot\nabla r_\epsilon.
   \end{split}
   \]
   The \(\Delta p\) term contributes a second copy of the mixed gradient
   and \(-\int\Phi_\delta''(p)|\nabla p|^2\).  The pressure-source term is
   \(-2\int w_{\epsilon,\delta}R_iR_j(G_{ij})\).  These are precisely the
   five groups in (16).

6. The local Hessian information \(\Phi_\delta''\ge0\) controls only
   \(-\int\Phi_\delta''(p)|\nabla p|^2\).  It gives no sign to
   \(R_iR_j(G_{ij})\): this scalar is nonlocal and depends on the same
   velocity that determines \(p\) and \(w_{\epsilon,\delta}\).  The mixed
   term and the coefficient \(p/r_\epsilon\) are also indefinite.  Thus the
   candidate correctly declines to infer either
   \(\mathcal H_{\epsilon,\delta}\le0\) or the existence of a field with
   positive heat contribution from the displayed local terms alone.

7. The first unsupported estimate needed for closure is exactly a one-sided
   bound for the complete sum (16), together with control of the nonlinear
   contribution (15).  Static coercivity supplies neither.  All explicit
   bounds already used in the note—(2), (5), and (9)—are valid; there is no
   earlier failed numerical inequality.

8. Equation (7) has the typographical string
   `\rho_\epsilon=r_\epsilon-\epsilon,qquad`; it should read
   `\rho_\epsilon=r_\epsilon-\epsilon,\qquad`.  This does not affect any
   formula or inference.

REPLACEMENT ARGUMENT: Assume (R1) on a compact interval and fix
\(\epsilon,\delta>0\).  Sobolev multiplication in dimension three gives
\[
 p\in C H^m,\quad V\in C H^{m-1},\quad
 p_t\in C H^{m-2},\quad G_{ij}\in C H^{m-1},                    \tag{R3}
\]
where all spaces are over \(\mathbb R^3\).  In particular \(u,p,\nabla u\)
are bounded, while all quantities needed below are in \(L^2\).  For fixed
regularizers,
\[
 \rho_\epsilon\in H^1\cap L^2,\qquad
 \Phi_\delta'(p)\in H^1\cap L^2,                               \tag{R4}
\]
because \(0\le\rho_\epsilon\le|u|\),
\(|\nabla\rho_\epsilon|\le|\nabla u|\), and
\(\Phi_\delta'(0)=0\) with bounded fixed-\(\delta\) second derivative on
the bounded range of \(p\).  Therefore
\(w_{\epsilon,\delta}\in H^1\cap L^2\).

The terms in (15) are finite by, for example,
\[
 \|r_\epsilon u\cdot V\|_1
 \le\epsilon\|u\|_2\|V\|_2+\|u\|_4^2\|V\|_2,
 \qquad
 \|p n_\epsilon\cdot V\|_1\le\|p\|_2\|V\|_2,
\]
and
\[
 \left|\int w_{\epsilon,\delta}R_iR_j(u_iV_j)\right|
 \le C\|w_{\epsilon,\delta}\|_2
       \|u\|_\infty\|V\|_2.                                  \tag{R5}
\]
The terms in (16) are finite because \(r_\epsilon\le\epsilon+|u|\),
\(r_\epsilon^{-1}\le\epsilon^{-1}\), \(p\in L^\infty\),
\(\nabla p,\nabla u\in L^2\), and
\[
 \|R_iR_j(G_{ij})\|_2\le C\|G\|_2
 \le C\|\nabla u\|_\infty\|\nabla u\|_2.                      \tag{R6}
\]
Approximate the fields in these Sobolev spaces by compactly supported smooth
fields, apply the classical chain rule and integration by parts there, and
pass to the limit using (R3)--(R6).  Equivalently, use the Sobolev chain rule
directly.  Time continuity makes every term integrable on \([0,T]\), so
(14)--(16) hold pointwise in time where the strong derivative is evaluated
and in integrated form on every subinterval.  This proves the fixed-
regularizer identity for the actual classical trajectory without any
Schwartz-persistence premise.

The repair does not justify an unregularized derivative.  The candidate is
correct that the speed map has a zero-set directional-derivative obstruction.
Only convergence of the functional values has been proved as
\(\epsilon,\delta\downarrow0\); an unregularized integrated balance would
still require separate domination of every term.

CONDITIONAL SUFFIX THAT SURVIVES: Static two-sided cubic control and the exact
fixed-regularizer evolution survive.  With the Sobolev repair they apply on
each compact interval strictly before \(T_*\).  Any modified-energy estimate
remains conditional on a one-sided bound for the full heat and nonlinear
remainders and, if regularizers are removed, on the missing domination
argument.

UNNECESSARY DEPENDENCIES: Schwartz decay is unnecessary.  Solenoidality is
unnecessary for the pointwise static lower bound.  No conclusion about the
heat sign follows from analyzing the local Hessian of the entropy alone.

NON-CLAIMS: This audit proves no sign for (16), no unregularized Frechet
derivative, no passage of the differentiated identity to
\(\epsilon=\delta=0\), no pressure absorption estimate, and no regularity or
global-existence result.

REOPENING CONDITION: Supply either a one-sided estimate for the complete
right-hand side of (14), uniform enough to remove the regularizers and
approach \(T_*\), or an exact smooth-field evaluation that determines the
sign of the full nonlocal heat expression.
