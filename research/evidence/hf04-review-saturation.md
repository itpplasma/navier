# Audit of saturation and exact full-heat cancellation

VERDICT: **REPAIR**

REVIEWED SCOPE: hf04-saturated-normal-form.md at verified SHA-256
df06cfda285357d176c545b56b366fb850c423b3fae027681a84243f5c9e3c23,
on full base commit 06cbc0fa7a3b6d7dcea36950ab43259a89132baa.

FIRST BAD BRIDGE: The sentence following the chain rule says that exact
algebraic cancellation “for all states requires”
\[
 F_X+F_{\mathcal B}=0.                                \tag{A}
\]
This necessity does not follow merely from cancellation along realized
Navier--Stokes states. Such a conclusion would require an unproved
independence or richness statement for the realized values of
\((X,\mathcal B,P_3,D_3,D\mathcal B[\mathbb PN])\).

REPLACEMENT ARGUMENT: State the premise coefficientwise on the ambient scalar
domain
\[
 \Omega=(0,\infty)\times\mathbb R
\]
with coordinates \((X,\mathcal B)\): an “exact algebraic pressure
cancellation” means by definition that the coefficient of \(P_3\) in the
formal chain rule vanishes at every point of \(\Omega\). Under this precise
premise, (A) is immediate. The characteristics of
\(\partial_XF+\partial_{\mathcal B}F=0\) are the connected lines
\[
 X-\mathcal B=y,\qquad X>0.
\]
Each such fiber is connected, parametrized by \(X\in(0,\infty)\), so every
\(C^1\) solution on connected \(\Omega\) has exactly the form
\[
 F(X,\mathcal B)=f(X-\mathcal B).
\]
This repairs the scope without assuming anything about independence of
realized PDE quantities.

EVIDENCE:

1. The weighted pressure estimate is correct. Calderón--Zygmund,
   \(L^3\)-\(L^9\) interpolation, and Hölder give
   \[
    \|p\|_{9/4}\le C\|u\|_3\|u\|_9,\qquad
    \|u\cdot\nabla|u|\|_{9/5}
      \le \|u\|_9^{1/2}D_3^{1/2}.
   \]
   Since \(\|u\|_9^3\le CD_3\),
   \[
    |P_3(u)|\le C\|u\|_3D_3(u).                       \tag{1}
   \]

2. For \(X=\|u\|_3^3/3\), the heat equation obeys exactly
   \(dX(G_su)/ds=-\nu D_3(G_su)\), and \(X(G_su)\to0\).
   Therefore
   \[
   \begin{aligned}
    |\mathcal B(u)|
      &\le C\int_0^\infty(3X(G_su))^{1/3}D_3(G_su)\,ds\\
      &\le \frac{C}{\nu}\int_0^{X(u)}(3x)^{1/3}dx
       =\frac{C}{4\nu}\|u\|_3^4,                     \tag{2}
   \end{aligned}
   \]
   after absorbing the universal constant from (1).

3. The saturated functional
   \[
    \mathcal F_\delta=X-\delta\mathcal B/(1+\|u\|_3/\nu)
   \]
   satisfies
   \[
    |\mathcal F_\delta-X|\le C\delta\|u\|_3^3
      =3C\delta X.
   \]
   Thus it is coercive for sufficiently small fixed \(\delta>0\).

4. On a sufficiently high Sobolev class, writing
   \(P_3=-\int\nabla p\cdot|u|u\) avoids differentiating \(|u|\) alone.
   The map \(u\mapsto|u|u\) is \(C^1\), pressure is quadratic, and the
   differentiated heat integral has a locally bounded integrand near zero
   and an integrable heat-kernel majorant at infinity. Hence
   \[
    D\mathcal B(u)[h]
      =-\int_0^\infty DP_3(G_su)[G_sh]\,ds
   \]
   and integration in heat time gives
   \[
    D\mathcal B(u)[\nu\Delta u]=P_3(u).               \tag{3}
   \]
   Along a strong solution,
   \[
    X'=P_3-\nu D_3,\qquad
    \mathcal B'=P_3-D\mathcal B(u)[\mathbb PN(u)].    \tag{4}
   \]

5. The chain rule following from (4) is
   \[
    \frac d{dt}F=(F_X+F_{\mathcal B})P_3
      -\nu F_XD_3
      -F_{\mathcal B}D\mathcal B(u)[\mathbb PN(u)].
                                                               \tag{5}
   \]
   For the saturated choice, its pressure coefficient can be bounded more
   sharply than the candidate states. With \(U=(3X)^{1/3}\),
   \[
    q(X)=\frac{\nu}{\nu+U},\qquad
    q'(X)=-\frac{\nu}{U^2(\nu+U)^2}.
   \]
   If (2) is written \(|\mathcal B|\le C_B U^4/\nu\), then
   \[
    |q'(X)\mathcal B|
      \le C_B\frac{U^2}{(\nu+U)^2}\le C_B.
   \]
   Hence
   \[
    \left|(F_X+F_{\mathcal B})-1\right|
      \le\delta(1+C_B).
   \]
   For \(\delta\le[2(1+C_B)]^{-1}\), the residual pressure coefficient is
   uniformly at least \(1/2\), rather than merely being generically of order
   one. Saturation repairs static coercivity but leaves a uniformly nonzero
   multiple of the original pressure work.

6. The noncoercivity of every ambient exactly cancelling scalar functional is
   valid. The audited positive-pressure profile implies
   \(\mathcal B(\phi)\ne0\) for some Schwartz \(\phi\); parity permits
   \(\mathcal B(\phi)>0\). If \(\chi\) is linearly independent of \(\phi\),
   \[
    \psi_s=\cos(\pi s)\phi+\sin(\pi s)\chi
   \]
   never vanishes. Hence \(X(\psi_s)\) has a positive minimum on
   \([0,1]\). The continuous function
   \(h_a(s)=a\mathcal B(\psi_s)-X(\psi_s)\) is positive at \(s=0\) for
   large \(a\) and negative at \(s=1\). Its zero \(s_a\) gives
   \[
    X(a\psi_{s_a})-\mathcal B(a\psi_{s_a})=0,\qquad
    X(a\psi_{s_a})\to\infty.                          \tag{6}
   \]

7. Exact energy \(E>0\) is imposed by
   \[
    N_a=a^2\|\psi_{s_a}\|_2^2/E,\qquad
    u_a(x)=aN_a\psi_{s_a}(N_ax).
   \]
   Then \(\|u_a\|_2^2=E\), while both \(X\) and the full heat inverse
   \(\mathcal B\) are invariant under \(u(x)\mapsto Nu(Nx)\).
   Thus (6) persists on the exact fixed-energy shell. Every ambient solution
   \(F=f(X-\mathcal B)\) takes the constant value \(f(0)\) on this sequence
   while \(X\to\infty\), so it cannot control the critical norm.

CONDITIONAL SUFFIX THAT SURVIVES: With “exact cancellation” defined
coefficientwise on \(\Omega\), all conclusions of the note survive. The same
fixed-energy sequence also rules out coercivity of
\(F(X,\mathcal B,E)\), or a functional with fixed \(\nu\) or fixed time as
additional passive parameters: on each fixed parameter slice the PDE still
gives \(F=f(X-\mathcal B,E)\). This does not extend to extra geometric or
frequency variables or to a trajectory-restricted state domain.

UNNECESSARY DEPENDENCIES: No independence of realized pressure, dissipation,
and normal-form remainder is needed after adopting the ambient
coefficientwise definition.

NON-CLAIMS: The result excludes only scalar functions of
\((X,\mathcal B)\) that demand exact ambient algebraic cancellation. It does
not exclude approximate cancellation, extra active state variables,
frequency-dependent or time-nonlocal corrections, direct remainder control,
HF, or global regularity.

REOPENING CONDITION: No reopening is needed for the repaired ambient theorem.
Any claim of necessity on the realized PDE state set requires a separate
richness theorem for that set.
