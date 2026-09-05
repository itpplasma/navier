# HF17 independent audit: cubic quotient functional

Frozen input: base commit
`0918b9ab403fcbc878ee20b62d887f6405123337`, with review input
`research/evidence/hf17-quotient-functional.md` at SHA-256
`a57fd95e847bfda0a597c75322cafad42827c559f33420b369f2a5897f8c0ce7`.

## Verdict

**VERDICT: PASS.**  The metric representative exists and is unique, the
functional is quantitatively coercive on solenoidal fields and invariant
under the critical scaling, heat preserves the closed gradient space and
contracts the quotient functional, and the derivative is exactly the
annihilating norm functional in (15).  For the actual compact \(H^m\)
trajectory class, \(m\ge4\), the fixed Riesz pressure satisfies
\(\nabla p\in\mathcal G_3\), so the pressure cancellation is applicable.
The generator inequality requires \(\Delta u\in L^3\), as stated.  No control
of the remaining transport flux follows.

## Minimizer and Euler condition

The set \(\mathcal G_3\) is a closed linear subspace of the reflexive space
\(L^3\), hence weakly closed.  If \(q_n\) is minimizing, boundedness of
\(u+q_n\) implies boundedness of \(q_n\).  Weak compactness and lower
semicontinuity produce a minimizer.  Strict convexity of
\(w\mapsto\|w\|_3^3\) makes the representative \(w=u+q(u)\), and therefore
also \(q(u)\), unique.  This proves (3)--(4).

Varying the minimizer along any real multiple of
\(q\in\mathcal G_3\) gives
\[
 \int |w|w\cdot q=0.
\]
No regularity of \(w\) beyond \(L^3\) is used.  Taking compactly supported
gradient variations is exactly the distributional statement
\(\operatorname{div}(|w|w)=0\).

## Coercivity, homogeneity, and scaling

The Leray projection is bounded on \(L^3\), fixes every distributionally
solenoidal \(L^3\) field, and annihilates the \(L^3\)-closure of compact
gradients.  Thus \(u=\mathbb Pw\), proving the lower bound in (8); \(q=0\)
proves the upper bound.  Both constants and the factor \(1/3\) are correct.

Linearity of \(\mathcal G_3\) proves cubic amplitude homogeneity.  Moreover
\[
 \lambda(\nabla\phi)(\lambda x)
 =\nabla[\phi(\lambda\,\cdot)](x),
\]
and the inverse scaling has the same property.  Hence the critical spatial
scaling maps \(\mathcal G_3\) bijectively to itself and preserves the
\(L^3\) quotient norm, proving (10).

## Heat invariance

For a generating gradient,
\(G_t\nabla\phi=\nabla G_t\phi\).  The heat-evolved potential is smooth with
rapid decay.  If \(\chi_R\) is a standard cutoff, then
\[
 \nabla(\chi_RG_t\phi)
 =\chi_R\nabla G_t\phi+(G_t\phi)\nabla\chi_R
 \longrightarrow\nabla G_t\phi
 \quad\hbox{in }L^3.
\]
Mollification if needed keeps these approximants in the generating class.
The \(L^3\)-bounded heat semigroup extends this invariance to the closure.
Applying heat to the minimizing representative then gives both inequalities
in (12).  This proof does not differentiate or regularize \(w\).

## Direct derivative proof

The differentiability assertion need not rest on an unverified abstract
quotient theorem.  Let \(w_h=w(u+h)\).  Quotient contraction gives
\[
 |\|w_h\|_3-\|w\|_3|\le\|h\|_3.                       \tag{R1}
\]
Any weakly convergent subsequence of \(w_h\) as \(h\to0\) has the correct
quotient class and, by lower semicontinuity and (R1), is the unique minimizer
\(w\).  Its norms also converge; uniform convexity of \(L^3\) then gives
\(w_h\to w\) strongly.  Consequently
\(|w_h|w_h\to|w|w\) in \(L^{3/2}\).

The upper competitor \(w+h\) gives
\[
 \mathcal Q(u+h)-\mathcal Q(u)
 \le \langle |w|w,h\rangle+o(\|h\|_3).
\]
Using \(w_h-h\) as a competitor for \(u\), and the strong convergence just
proved, gives the reverse inequality with the same linear term.  The standard
uniform remainder for the \(L^3\) cubic on bounded sets makes this Frechet,
not merely directional, differentiation.  Therefore
\[
 D\mathcal Q(u)[h]=\int|w|w\cdot h.
\]
At the zero quotient class, the cubic bound
\(0\le\mathcal Q(h)\le\|h\|_3^3/3\) gives derivative zero directly.
Equation (5) then proves (16)--(17).

## Pressure gradients in the actual trajectory class

For \(u\in H^m(\mathbb R^3)\), \(m\ge4\), Sobolev multiplication and Riesz
boundedness give the fixed representative
\(p=R_iR_j(u_i u_j)\) with \(p,\nabla p\in L^3\).  For example,
\(u_i u_j\in W^{1,3}\) because \(u,\nabla u\) have more than the required
Sobolev integrability; equivalently one may combine the available \(L^2\)
and \(L^\infty\) Sobolev bounds.  Thus \(p\in W^{1,3}\).

Choose cutoffs \(\chi_R\).  Then
\[
 \nabla(\chi_Rp)-\nabla p
 = (\chi_R-1)\nabla p+p\nabla\chi_R\longrightarrow0
 \quad\hbox{in }L^3,
\]
because the first term is an \(L^3\) tail and the second is bounded by
\(R^{-1}\|p\|_{L^3(\{R\lesssim|x|\lesssim2R\})}\).  Mollifying
\(\chi_Rp\) produces compactly supported smooth potentials with gradients
converging in \(L^3\).  Hence \(\nabla p\in\mathcal G_3\) for every time on
the actual compact classical interval, without assuming preserved Schwartz
decay or relying on formal integration by parts.

## Heat generator and evolution scope

If \(u,\Delta u\in L^3\), then \(u\) lies in the \(L^3\) generator domain of
the heat semigroup and
\[
 {G_tu-u\over t}\to\Delta u\quad\hbox{in }L^3.
\]
Frechet differentiability and (12) therefore prove (19).  Under the stated
regularity ensuring all directions lie in \(L^3\), the chain rule and the
gradient cancellation give (18).  The transport pairing is finite, but the
variational construction supplies neither a sign nor a bound for it.  Since
\(w\) is only an \(L^3\) metric representative, no integration by parts in
(20) is justified.

## Audit record

**REVIEWED SCOPE:** minimizer existence and uniqueness; quotient norm and
Frechet derivative; Leray coercivity; amplitude and spatial scaling; heat
invariance of \(\mathcal G_3\); actual \(H^m\) pressure-gradient membership;
and the heat generator inequality.

**FIRST BAD BRIDGE:** none.

**REPLACEMENT ARGUMENT:** none.  The direct envelope argument above can replace
the abstract uniform-smoothness sentence if an entirely internal proof is
preferred.

**CONDITIONAL SUFFIX THAT SURVIVES:** any independently proved one-sided
input-only spacetime bound for the transport flux, at the strength needed to
combine with heat monotonicity, would control the coercive quotient
functional.

**UNNECESSARY DEPENDENCIES:** smoothness or differentiability of \(w(u)\), a
weighted heat identity, and preserved rapid decay of the Navier--Stokes
solution are unnecessary.

**NON-CLAIMS:** no transport-flux estimate or sign, pressure estimate,
HIGH-PRESSURE theorem, critical continuation bound, or regularity result is
established.

**REOPENING CONDITION:** none for the functional properties; the next gap is
the transport flux (20).
