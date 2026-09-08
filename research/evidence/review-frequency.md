# Frozen independent audit of the frequency reduction

**VERDICT: REPAIR.**  The low-frequency pressure estimate and the signed
high-tail sufficient lemma are mathematically valid.  Two localized repairs
are required before integration: state the real-even/self-adjoint multiplier
conventions used in the projector pairing, and make the scaled-snapshot
falsifier explicitly conditional because the note does not construct a
divergence-free Schwartz profile with nonzero pressure work.  Neither repair
changes the low/high reduction or its conditional suffix.

## Reviewed scope and frozen input

The immutable candidate is repository `../navier`, exact commit
`6c68c7ae07c1fb385b8068f83d2fc7aae957668c`, file
`research/evidence/frequency.md`.  I also checked the repaired opening of
`research/evidence/enstrophy.md` at the same commit.  No pressure-control
claim from my earlier architecture note is reviewed as established here.

The audit covers the truncated Riesz kernel, all displayed scaling and
Hölder exponents, the signed high-frequency sufficient statement, the Leray
and Littlewood--Paley projector pairings, and the precise logical strength of
the snapshot discussion.

## Low-frequency kernel: PASS

Choose a homogeneous Littlewood--Paley partition with real, even, smooth
annular multiplier \(\varphi\), and let
\(S_J=\sum_{j\leq J}\Delta_j\).  Away from the origin its symbol is a bounded
low-pass function \(\chi(2^{-J}\xi)\).  For the \(ij\) pressure component,
the symbol of \(S_JR_iR_j\) is

\[
 m_{J,ij}(\xi)=
 \chi(2^{-J}\xi)\frac{-\xi_i\xi_j}{|\xi|^2},
 \qquad \xi\ne0.
\]

The directional discontinuity at \(\xi=0\) is harmless for this estimate:
\(|m_{J,ij}|\leq \mathbf 1_{|\xi|\lesssim2^J}\), so

\[
 \|m_{J,ij}\|_{L^1_\xi}\leq C2^{3J}.
\]

If \(K_{J,ij}=\mathcal F^{-1}m_{J,ij}\), Fourier inversion gives
\(\|K_{J,ij}\|_\infty\leq C\|m_{J,ij}\|_1\leq C2^{3J}\).  Young's endpoint
convolution estimate therefore yields

\[
 \|S_JR_iR_j f\|_\infty
 \leq C2^{3J}\|f\|_1.                                \tag{A}
\]

This uses a bounded frequency-truncated kernel.  It neither asserts that the
kernel is \(L^1_x\) nor that an untruncated Riesz transform maps
\(L^1_x\) to itself.  Taking \(f=u_i u_j\) proves candidate equation (3):

\[
 \|p_{\leq J}\|_\infty
 \leq C2^{3J}\|u\otimes u\|_1
 \leq C2^{3J}\|u_0\|_2^2.
\]

Next,
\(\|u\cdot\nabla|u|\|_1\leq\|u\|_2\|\nabla u\|_2\), because
\(|\nabla|u||\leq|\nabla u|\) almost everywhere.  Thus

\[
 |L_J(t)|\leq C2^{3J}\|u_0\|_2^3\|\nabla u(t)\|_2.
\]

Cauchy--Schwarz in time and
\(\int_0^\tau\|\nabla u\|_2^2dt\leq\|u_0\|_2^2/(2\nu)\) give

\[
 \left|\int_0^\tau L_Jdt\right|
 \leq C2^{3J}\|u_0\|_2^4(H/(2\nu))^{1/2},             \tag{B}
\]

uniformly for \(\tau<\min\{H,T_*\}\).  Every exponent and datum power in
candidate equations (3)--(5) is correct.

## Exact signed high-tail consumer: PASS

For a finite integer \(J=J(\nu,u_0,H)\) chosen from input data before viewing
the trajectory, assume there are \(0\leq\theta<1\) and finite
\(A_{\rm high}(\nu,u_0,H,J)\), independent of \(\tau,T_*\) and all unknown
solution norms, such that

\[
 \int_0^\tau H_Jdt
 \leq\theta\nu\int_0^\tau D_3dt+A_{\rm high}          \tag{HF}
\]

for every \(0<\tau<\min\{H,T_*\}\).  Since
\(P_3=L_J+H_J\), estimate (B) gives

\[
 \int_0^\tau P_3dt
 \leq\theta\nu\int_0^\tau D_3dt
      +A_{\rm low}+A_{\rm high}.
\]

Integration of the exact \(L^3\) balance then yields

\[
 \|u(\tau)\|_3^3+3(1-\theta)\nu\int_0^\tau D_3dt
 \leq\|u_0\|_3^3+3(A_{\rm low}+A_{\rm high}).         \tag{C}
\]

This proves both candidate equation (6) and the claimed weighted-dissipation
bound.  The high tail must remain the single signed quantity \(H_J\); a sum
of absolute shell contributions would be a strictly stronger, unsupported
Besov-type demand.

Candidate equation (7) is sufficient only with its stated extra uniform
selection information.  A bare finite limsup, if its threshold in \(J\)
could depend on the unknown trajectory, would not produce an input-chosen
cutoff.  An integration-ready version should directly quantify a modulus:
there is an input-computable \(J_0(\nu,u_0,H,\varepsilon)\) such that every
\(J\geq J_0\) satisfies the bracketed bound by
\(A_{\rm tail}+\varepsilon\), uniformly in \(\tau\).  Then choosing, for
example, \(\varepsilon=1\) produces (HF).

## Projector pairing: REPAIR

Let \(N=(u\cdot\nabla)u\), \(w=|u|u\), and let \(\mathbb P\) be the
whole-space Leray projector.  On compact subintervals of the maximal strong
solution, Sobolev regularity gives \(w,N\in L^2\), so the following are
legitimate \(L^2\) pairings.  The pressure equation gives

\[
 \nabla p=-(I-\mathbb P)N.
\]

Moreover,

\[
 \int w\cdot N
 =\frac13\int u\cdot\nabla|u|^3=0.
\]

Since \(\mathbb P\) is the orthogonal Fourier projector on \(L^2\), it is
self-adjoint, and hence

\[
 P_3=\int w\cdot(I-\mathbb P)N
     =-\int \mathbb Pw\cdot N.                        \tag{D}
\]

This verifies candidate equation (2), including its signs.

For the high-frequency identity, one additionally needs \(S_J\), and hence
\(P_{>J}=I-S_J\), to be self-adjoint.  This holds for the real, even dyadic
multipliers fixed above.  Fourier multipliers commute, so

\[
 \begin{aligned}
 H_J
 &=-\int w\cdot\nabla p_{>J}
   =\int w\cdot(I-\mathbb P)P_{>J}N\\
 &=\int P_{>J}w\cdot(I-\mathbb P)N.                  \tag{E}
 \end{aligned}
\]

Likewise, self-adjointness and annular Fourier support justify replacing
\(N\) in \(\int\Delta_jw\cdot(I-\mathbb P)N\) by a fixed enlargement
\(\widetilde\Delta_jN\).  The candidate should state these multiplier choices
before invoking “orthogonality.”  With that sentence added, the pairing and
neighboring-output-shell reduction are correct.  Almost orthogonality alone
does not produce a sign, a small factor, or a telescoping boundary functional;
the candidate correctly stops before claiming any of these.

## Absolute estimates and scaling: PASS

The absolute pressure estimate uses

\[
 \|p\|_3\lesssim\|u\otimes u\|_3=\|u\|_6^2,
 \qquad
 |P_3|\leq\|p\|_3\|u\|_6\|\nabla u\|_2,
\]

where \(1/3+1/6+1/2=1\).  Sobolev turns its right side into
\(C\|\nabla u\|_2^4\), which energy does not integrate.  These exponents are
correct.

For \(u_N(x)=N\phi(Nx)\), direct changes of variables give

\[
 \|u_N\|_3=\|\phi\|_3,\quad
 \|u_N\|_2^2=N^{-1}\|\phi\|_2^2,\quad
 D_3[u_N]=N^2D_3[\phi],\quad P_3[u_N]=N^2P_3[\phi].
\]

Also \(\|u_N\|_2^3\|\nabla u_N\|_2=O(N^{-1})\), so fixed-\(J\)
low-frequency work is \(O(N^{-1})\).  Conditional on
\(P_3[\phi]\ne0\), candidate equation (9a) follows exactly.

## Snapshot conclusion: REPAIR

The candidate does not exhibit or prove existence of a divergence-free
Schwartz field \(\phi\) with \(P_3[\phi]\ne0\).  Therefore equation (9a) is a
correct conditional calculation, but it cannot by itself establish that a
nonzero critical pressure-work profile exists.  There is a second logical
limit: these snapshots are not shown to be points on Navier--Stokes
trajectories with uniformly controlled initial data, so they cannot refute
the spacetime statement (HF) or candidate equation (10).  The candidate says
the latter explicitly, but the preceding “therefore no estimate of the form
(10)” sentence is broader than the evidence.

The minimal repair is to replace that conclusion by:

> If one supplies a divergence-free Schwartz profile \(\phi\) with
> \(P_3[\phi]\ne0\), equations (9)--(9a) show that energy size and a fixed
> output cutoff alone cannot yield a decaying pointwise high-tail factor.
> No such profile is constructed here.  Snapshot scaling does not refute any
> spacetime trajectory estimate, including (HF) or (10).

Alternatively, the author may retain the stronger instantaneous-mechanism
falsifier after giving an explicit \(\phi\) and verifying
\(P_3[\phi]\ne0\).  Even then, equation (10), as written with a time integral,
must remain outside the scope of the snapshot counterexample.

## Enstrophy-opening repair: PASS with one editorial residue

At the frozen commit, `enstrophy.md` now formulates the calculation for the
strong Sobolev solution, inserts cutoffs, explains why cutoff errors vanish,
uses regularization for nonlinear tests, and explicitly says that no
Schwartz-decay persistence is assumed.  This fully repairs the mathematical
issue in the prior audit.  The later phrase “incompressibility and decay give”
should be changed editorially to “incompressibility and the cutoff limit
give” for consistency, but the preceding paragraph already supplies the
valid argument, so this residue is not a bad bridge.

## Conditional suffix that survives

After the two localized frequency-note repairs, the following chain is valid:

1. The energy identity alone gives the explicit uniform low-output estimate
   (B) for every input-chosen finite \(J\).
2. The signed high-tail lemma (HF), if proved with its stated non-circular
   quantifiers, combines with (B) to give (C).
3. Equation (C) supplies finite-horizon \(L^\infty_tL^3_x\) control and an
   additional weighted \(D_3\) integral.

The note does not prove (HF), a temporal shell cancellation, or a nonzero
snapshot pressure-work profile.  It does rigorously isolate high output
frequencies as the only part not already bounded by energy at a fixed cutoff.

## Integration-ready lemma

The following statement can be added to the manuscript and dependency graph
without importing any unproved high-frequency assertion.

**Lemma (energy control of low-output pressure work).**  Fix \(\nu,H>0\), an
integer \(J\), and a divergence-free datum \(u_0\in H^m(\mathbb R^3)\cap
L^2(\mathbb R^3)\) with \(m>5/2\).  Let \(u\) be its maximal strong solution
on \([0,T_*)\), and normalize pressure by
\(p=R_iR_j(u_i u_j)\).  Choose the low-pass multiplier \(S_J\) from a real,
even homogeneous Littlewood--Paley partition and set

\[
 L_J(t)=\int_{\mathbb R^3}S_Jp\,u\cdot\nabla|u|\,dx.
\]

Then there is a universal constant \(C\), depending only on the fixed cutoff
profile and Fourier convention, such that every
\(0<\tau<\min\{H,T_*\}\) satisfies

\[
 \left|\int_0^\tau L_J(t)dt\right|
 \leq C2^{3J}\|u_0\|_2^4\left(\frac{H}{2\nu}\right)^{1/2}.             \tag{LF}
\]

**Proof.**  Estimate (A) applied to \(u_i u_j\), followed by
\(|\nabla|u||\leq|\nabla u|\), gives the pointwise estimate preceding (B).
Cauchy--Schwarz in time and the energy identity give (LF).  Strong Sobolev
regularity and spatial cutoffs justify all pairings.  No critical norm,
terminal-time regularity, or high-frequency estimate is used.

## Non-claims and reopening condition

This audit does not prove the high-tail lemma, pressure absorption, or global
regularity.  It does not source-audit external Littlewood--Paley, local
existence, or endpoint-continuation theorems.  It does not turn arbitrary
snapshots into solution trajectories.

The full frequency route can be reopened when either (i) a signed trajectory
estimate proves (HF), or (ii) a genuine telescoping law is supplied with an
explicit boundary functional and summable errors.  The stronger snapshot
falsifier can be promoted only after constructing and checking a profile with
nonzero \(P_3\).
