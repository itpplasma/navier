# HF14 independent audit: high-output evolution

Frozen input: base commit
`f297efc46756f5acd229e4a8aaa5284655ec6903`, with review input
`research/evidence/hf14-high-output-evolution.md` at SHA-256
`d7b91e1fdc2df4f56fc7bc52c1cfba4b6026f5135565dbdcd0ae9cb12f6900d3`.

## Verdict

**VERDICT: REPAIR.**  The generic chain-rule identities (6)--(13) are correct
when imposed coefficient and integrability hypotheses make every pairing
finite.  The unregularized away-from-cusp Euler algebra (14)--(18) is also
correct and retains the full pressure gradient and high-output pressure
source.  Three scope bridges need repair:

1. a generic \(C^2\) approximation with the two normalizations and unspecified
   “same cubic growth” does not by itself ensure that the functional,
   derivatives, Hessian coefficients, or nonlocal pairings are integrable;
2. (19) is not one exact fixed-regularizer remainder, because its first three
   terms use unregularized Euler coefficients while its heat term is said to
   use a fixed smooth regularization;
3. bounding this already combined remainder above by a positive strict
   fraction of dissipation does not bound \(\mathcal J_{k,J}\).  A dissipative
   term must first remain on the left side of the balance.

These are exact scope repairs.  No high-output producer follows from the
candidate.

## 1. Generic identity and its hypotheses

For a genuinely smooth radial density \(f(r,z)\), put
\(\beta=f_r/r\), with a smooth extension at \(r=0\).  Differentiating the
fixed Riesz representative gives (6), and
\[
 2R_iR_j(u_i\Delta u_j)=\Delta p-2R_iR_j(\partial_\ell u_i\partial_\ell u_j)
\]
gives (7)--(8), including the signs and factor two.  Integration by parts in
the velocity variables gives
\[
 \int\beta u\cdot\Delta u
 =-\int\beta|\nabla u|^2
  -\int(f_{rr}-f_r/r)|\nabla r|^2
  -\int f_{rz}\nabla r\cdot\nabla z,
\]
and integration by parts in \(z\) supplies the second mixed term and the
\(f_{zz}\) term.  Thus (9)--(13) contain all chain-rule terms.

The assertion becomes classical only after adding hypotheses that ensure,
for the chosen fixed regularizer and the actual solution class, that
\[
 f(r,z),\quad \beta|\nabla u|^2,quad
 (f_{rr}-\beta)|\nabla r|^2,quad
 f_{rz}\nabla r\cdot\nabla z,quad f_{zz}|\nabla z|^2,
\]
and
\[
 f_zQ_JR_iR_j(G_{ij}),\qquad
 \beta u\cdot V,qquad f_zQ_JR_iR_j(u_iV_j)
\]
are integrable, with sufficient time domination to differentiate under the
integral.  The scalar conditions (4) plus “same cubic growth” do not state
these derivative bounds.  A repaired trajectory scope can take
\(u\in C([0,T];H^m)\), \(u_t\in C([0,T];H^{m-2})\), \(m\ge4\), and require
the displayed coefficient-weighted integrability uniformly on that compact
interval for each fixed regularizer.  Rapid decrease at one time is not a
replacement for this compact-interval hypothesis.

## 2. Unregularized Euler algebra

Away from \(r=0\) and \(p_H=0\), (14)--(17) are algebraically correct.  The
cubic Euler contribution is
\[
 \int r u\cdot V=\int p\,u\cdot\nabla r.
\]
The advective part of the coupling cancels its \(p_H>0\) component.  On
\(p_H<0\), it leaves
\(p_H(1-r/s_H)u\cdot\nabla r\), while \(p_Lu\cdot\nabla r=L_J\) remains.
The pressure part of \(V=-N-\nabla p\) gives the third term of (17) with the
gradient of the full pressure.  Differentiating \(p_H=Q_Jp\) gives the last
term, including \(Q_J\), the double Riesz transform, and the factor two.
No low-pressure component or pressure-variation output is silently dropped.

This verification is only the stated away-from-cusps algebra.  It does not
supply differentiability of the unregularized functional or a passage from a
fixed scalar regularization.

## 3. One rigorous fixed-regularizer remainder

For each fixed admissible \(f^\eta\), the exact balance is
\[
 {d\over dt}\mathcal J^\eta(t)
 =L_J(t)+\mathfrak R^\eta_{k,J}(t),
 \qquad
 \mathfrak R^\eta_{k,J}:=mathcal E_{f^\eta}
                         +\mathcal H_{f^\eta}-L_J.       \tag{R1}
\]
Here both \(\mathcal E_{f^\eta}\) and \(\mathcal H_{f^\eta}\) use the same
regularized density and its derivatives.  Formula (R1) is exact, and the
known low-output estimate can be applied to \(L_J\).  It does not identify
\(\mathfrak R^\eta_{k,J}\) with the displayed unregularized expression (19).

Alternatively, (19) may be retained only as a formal target assembled from
the away-from-cusp limit.  To turn it into a balance one must prove convergence
of the regularized functional values and every integrated Euler and heat term,
with domination across both \(r=0\) and \(p_H=0\).  The candidate explicitly
does not prove this, so its “understood through a fixed smooth scalar
regularization” phrase cannot make (19) exact.

## 4. Correct closure form

From (R1), a bound
\[
 \int_0^t\mathfrak R^\eta_{k,J}
 \le \theta\nu\int_0^tD+ A,qquad 0<\theta<1,            \tag{R2}
\]
does not control \(\mathcal J^\eta(t)\) unless the integral of \(D\) is
already known.  The reason is that \(\mathfrak R^\eta_{k,J}\) already
contains the complete heat contribution; there is no negative copy of
\(\nu D\) left on the left side to absorb the right side of (R2).

A sufficient formulation must first extract an actual nonnegative
dissipation from the heat identity:
\[
 \mathcal H_{f^\eta}=-\nu D^\eta+\mathcal H_{\rm rem}^\eta,
 \qquad D^\eta\ge0.                                    \tag{R3}
\]
If one then proves
\[
 \int_0^t(\mathcal E_{f^\eta}-L_J
                 +\mathcal H_{\rm rem}^\eta)
 \le\theta\nu\int_0^tD^\eta+A,                         \tag{R4}
\]
the exact balance yields
\[
 \mathcal J^\eta(t)+(1-\theta)\nu\int_0^tD^\eta
 \le \mathcal J^\eta(0)+\int_0^tL_J+A.                \tag{R5}
\]
Only a statement of this form, together with uniform coercivity, a uniform
low-output bound, and a justified regularization limit, can feed a critical
bound.  The candidate proves neither (R3) with useful \(D^\eta\) nor (R4).
A direct input-only upper bound on the entire integral in (R1) would also
bound the functional, but calling a positive multiple of an uncontrolled
dissipation an input-only remainder would not.

## Audit record

**REVIEWED SCOPE:** pressure differentiation; generic radial Hessian heat
identity; full-pressure Euler decomposition at fixed cutoff; regularity and
integrability scope; consistency of regularized terms; and the claimed
conditional continuation use.

**FIRST BAD BRIDGE:** lines 30--39 assert applicability to any \(C^2\) scalar
approximation satisfying only (4) and unspecified cubic growth.  Those
conditions do not control the first and second derivative coefficients in
(9)--(13) or justify their spacetime pairings.

**REPLACEMENT ARGUMENT:** impose the explicit coefficient-weighted
integrability above, use the coherent fixed-regularizer balance (R1), and use
the dissipative closure structure (R3)--(R5).  Keep (17) as unregularized
away-from-cusp algebra until a domination argument proves its integrated
regularization limit.

**CONDITIONAL SUFFIX THAT SURVIVES:** the exact generic formulas under the
repaired hypotheses, the away-from-cusp algebra (17), and the known separate
low-output estimate for \(L_J\).

**UNNECESSARY DEPENDENCIES:** rapid spatial decay is unnecessary for the
generic identity when compact-interval \(H^m\) regularity and the displayed
integrability hypotheses are available.

**NON-CLAIMS:** no sign for the heat Hessian, high-output spacetime estimate,
regularization limit, pressure absorption, HIGH-PRESSURE theorem, critical
bound, continuation, or global regularity is established.

**REOPENING CONDITION:** a producer claim requires one coherent regularized
or limiting balance and an estimate with a genuine dissipative term retained
on the left as in (R3)--(R5).
