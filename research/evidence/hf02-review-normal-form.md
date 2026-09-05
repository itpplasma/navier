# Audit of the corrected high-pressure heat normal form

VERDICT: **REPAIR**

REVIEWED SCOPE: Section 3 onward of research/evidence/hf01-controller.md,
frozen at repository base
169ec50daa9295e0a713236bf969c2f42a507f51 with complete new-file SHA-256
d05a7450d61cdfdc4651588e707dfc27121d486742b4f0eac30ac60658f30142.
Both identifiers were reproduced before review. I checked the high-pressure
functional, Fréchet derivative, heat inverse, chain-rule signs, transport
estimates, powers of \(\nu s\) and \(2^J\), time integration, and remaining
HF obligation.

FIRST BAD BRIDGE: The superseded proposal identified
\[
 \mathcal H_J(u)=-\langle\mathbb P Q_Jw,N\rangle,
 \qquad w=|u|u,\quad N=(u\cdot\nabla)u.                \tag{A}
\]
This is false for a finite cutoff. The full cancellation
\(\langle w,N\rangle=0\) does not imply
\(\langle Q_Jw,N\rangle=0\). Formula (A) drops this truncated transport term.

EVIDENCE:

1. Since \(Q_J=I-S_J\), \(\mathbb P\), and \(I-\mathbb P\) are commuting
   self-adjoint multipliers, while \(\nabla p=-(I-\mathbb P)N\),
   \[
   \begin{aligned}
    \int (p-S_Jp)\,u\cdot\nabla|u|
      &=\int Q_Jp\,\operatorname{div}w\\
      &=-\langle Q_J\nabla p,w\rangle\\
      &=\langle Q_Jw,(I-\mathbb P)N\rangle.            \tag{1}
   \end{aligned}
   \]
   Moreover,
   \[
    \langle Q_Jw,(I-\mathbb P)N\rangle
     =\langle Q_Jw,N\rangle-\langle\mathbb P Q_Jw,N\rangle.
                                                               \tag{2}
   \]
   The first term on the right is the term omitted from (A).

2. Define \(G_s=e^{\nu s\Delta}\),
   \(a=\nu^{-1}2^{-2J}\), and
   \[
    \mathcal B_J(u)=-\int_a^\infty\mathcal H_J(G_su)\,ds.
                                                               \tag{3}
   \]
   The bound
   \[
    |\mathcal H_J(v)|\le C\|v\|_6^3\|\nabla v\|_2
   \]
   and the heat estimates
   \(\|G_su\|_6+\|\nabla G_su\|_2
      \le C(\nu s)^{-1/2}\|u\|_2\)
   give
   \[
    |\mathcal H_J(G_su)|\le C(\nu s)^{-2}\|u\|_2^4
   \]
   and hence
   \[
    |\mathcal B_J(u)|
      \le C\nu^{-2}a^{-1}\|u\|_2^4
      =C\nu^{-1}2^{2J}\|u\|_2^4.                     \tag{4}
   \]

3. The map \(w(v)=|v|v\) is continuously Fréchet differentiable. For
   \(v\ne0\),
   \[
    Dw(v)[h]=|v|h+\frac{v\cdot h}{|v|}v,
   \]
   while \(Dw(0)[h]=0\), and always
   \(|Dw(v)[h]|\le2|v||h|\). Differentiation of (1) gives
   \[
   \begin{aligned}
    D\mathcal H_J(v)[h]
     ={}&\langle Q_JDw(v)[h],(I-\mathbb P)N(v)\rangle\\
       &+\langle Q_Jw(v),(I-\mathbb P)
          ((h\cdot\nabla)v+(v\cdot\nabla)h)\rangle.    \tag{5}
   \end{aligned}
   \]
   Hölder and multiplier bounds yield
   \[
    |D\mathcal H_J(v)[h]|
     \le C\left(\|v\|_6^2\|h\|_6\|\nabla v\|_2
       +\|v\|_6^3\|\nabla h\|_2\right).               \tag{6}
   \]
   Thus, for \(v=G_su,h=G_sz\),
   \[
    |D\mathcal H_J(G_su)[G_sz]|
      \le C(\nu s)^{-2}\|u\|_2^3\|z\|_2.              \tag{7}
   \]
   Integration on \([a,\infty)\) is locally uniform in \(u\), so (3) is
   \(C^1\) on \(L^2\), and the chain rule is valid along compact strong
   intervals.

4. Since \(\partial_sG_su=G_s(\nu\Delta u)\), the minus sign in (3) gives
   \[
    D\mathcal B_J(u)[\nu\Delta u]
      =-\int_a^\infty\frac d{ds}\mathcal H_J(G_su)\,ds
      =\mathcal H_J(G_au).                            \tag{8}
   \]
   With \(u_t=\nu\Delta u-\mathbb PN(u)\), this becomes
   \[
    \mathcal H_J(u)=\frac d{dt}\mathcal B_J(u)
      +[\mathcal H_J(u)-\mathcal H_J(G_au)]
      +D\mathcal B_J(u)[\mathbb PN(u)].               \tag{9}
   \]
   Every sign in the corrected normal form is therefore right.

5. Put \(h_s=G_s\mathbb P\operatorname{div}(u\otimes u)\). The Fourier
   bound \(\|\widehat{u\otimes u}\|_\infty\le\|u\|_2^2\) and Plancherel give
   \[
    \|\nabla h_s\|_2^2
      \le C\|u\|_2^4
        \int_{\mathbb R^3}|\xi|^4e^{-2\nu s|\xi|^2}d\xi
      \le C(\nu s)^{-7/2}\|u\|_2^4.
   \]
   Sobolev then gives
   \[
    \|\nabla h_s\|_2+\|h_s\|_6
      \le C(\nu s)^{-7/4}\|u\|_2^2.                  \tag{10}
   \]
   The two terms in (6) have powers
   \[
    (\nu s)^{-1}(\nu s)^{-7/4}(\nu s)^{-1/2}
     =(\nu s)^{-13/4}
   \]
   and
   \((\nu s)^{-3/2}(\nu s)^{-7/4}=(\nu s)^{-13/4}\).
   Consequently
   \[
    |D\mathcal H_J(G_su)[h_s]|
      \le C(\nu s)^{-13/4}\|u\|_2^5.                 \tag{11}
   \]
   Integration gives exactly
   \[
   \begin{aligned}
    |D\mathcal B_J(u)[\mathbb PN(u)]|
      &\le C\|u\|_2^5\int_a^\infty(\nu s)^{-13/4}ds\\
      &\le C\nu^{-1}(\nu a)^{-9/4}\|u\|_2^5\\
      &=C\nu^{-1}2^{9J/2}\|u\|_2^5.                  \tag{12}
   \end{aligned}
   \]
   Energy bounds its time integral by
   \[
    CH\nu^{-1}2^{9J/2}E_0^{5/2}.                     \tag{13}
   \]
   The calculation never estimates the unsmoothed nonlinearity in \(L^2\).

6. At \(s=a\),
   \[
    |\mathcal H_J(G_au)|
      \le C(\nu a)^{-2}\|u\|_2^4
      =C2^{4J}\|u\|_2^4.                              \tag{14}
   \]
   Its time integral is at most \(CH2^{4J}E_0^2\). The boundary functional
   also obeys
   \[
    |\mathcal B_J(u(\tau))-\mathcal B_J(u_0)|
      \le C\nu^{-1}2^{2J}E_0^2.                       \tag{15}
   \]

REPLACEMENT ARGUMENT: Replace (A) by (1). Equations (3)--(9) then give the
correct heat normal form without discarding cutoff transport. Equations
(10)--(13) prove that its nonlinear transport derivative is an admissible
energy-only finite-horizon remainder. This completely repairs both named
defects in the original normal form.

CONDITIONAL SUFFIX THAT SURVIVES: Define
\[
 R_J(u)=\mathcal H_J(u)-\mathcal H_J(G_au).            \tag{16}
\]
For fixed finite \(J\), equations (9), (12), and (15) show that
\[
 \int_0^\tau R_J(u(t))dt
 \le\theta\nu\int_0^\tau D_3(t)dt
   +A_R(\nu,u_0,H,J)                                  \tag{17}
\]
with universal \(\theta<1\), finite input-only \(A_R\), and uniformity for
\(\tau<\min\{H,T_*\}\), implies HF. Conversely, (14) shows directly that HF
implies (17), after adding \(CH2^{4J}E_0^2\) to the remainder. Therefore
short-heat absorption (17) and HF are equivalent modulo explicit
energy-controlled remainders. The defect retains the uncontrolled active
scales and is not estimated by the normal form.

FIRST REMAINING UNSUPPORTED BRIDGE: Prove (17) for arbitrary large Schwartz
data without the unknown critical supremum or a higher continuation norm.
Starting (3) at \(a=0\) removes \(R_J\) formally, but the energy estimates in
(4) and (7) are nonintegrable at zero. Smooth-snapshot finiteness does not
make them uniform toward a putative endpoint.

UNNECESSARY DEPENDENCIES: The normal form is not needed merely to establish
the equivalence of HF and (17), because (14) already controls their
difference. Its new content is the energy-only transport estimate (12),
which rules out that term as the obstruction in this heat-inverse approach.

NON-CLAIMS: The repair proves no sign, monotonicity, HF estimate, critical
bound, or global regularity theorem. The factor \(2^{9J/2}\) is admissible
only because HF permits a fixed finite input-selected \(J\); it supplies no
decay as \(J\to\infty\).

REOPENING CONDITION: Supply a signed short-time heat estimate proving (17),
or a different functional whose energy-controlled inverse reaches \(s=0\).
The estimate must be uniform in \(\tau<\min\{H,T_*\}\), with remainder
depending only on \(\nu,u_0,H,J\), not an unknown trajectory supremum.
