# HF04: saturation versus exact full-heat cancellation

Status: repair/no-go analysis, 2026-09-05. This note concerns scalar modified
energies built only from the critical cubic quantity and the full-pressure
heat inverse. It does not exclude nonscalar normal forms, frequency-dependent
functionals, or estimates using additional trajectory information.

Fix \(\nu>0\), write
\[
 U(u)=\|u\|_3,\qquad X(u)={1\over3}U(u)^3,
\]
and let \(G_s=e^{\nu s\Delta}\). Define on solenoidal Schwartz fields
\[
 \mathcal B(u)=-\int_0^\infty P_3(G_su)\,ds.           \tag{1}
\]

## 1. Coercive bound for the full heat inverse

The pointwise pressure estimate needed here is
\[
 |P_3(v)|\le C\|v\|_3D_3(v).                          \tag{2}
\]
To verify it, first
\[
 \|p[v]\|_{9/4}\le C\|v\|_{9/2}^2
 \le C\|v\|_3\|v\|_9.                                \tag{3}
\]
Also, writing one factor as a weighted gradient,
\[
 \|v\cdot\nabla|v|\|_{9/5}
 \le \||v|^{1/2}\|_{18}
      \||v|^{1/2}\nabla v\|_2
 \le \|v\|_9^{1/2}D_3(v)^{1/2}.                      \tag{4}
\]
Since \(\||v|^{3/2}\|_6^2=\|v\|_9^3\le CD_3(v)\),
Holder in (3)--(4) proves (2).

Along the heat flow,
\[
 {d\over ds}X(G_su)=-\nu D_3(G_su).                  \tag{5}
\]
Therefore (2) and the substitution \(dX=-\nu D_3ds\) give the exact
one-dimensional bound
\[
\begin{aligned}
 |\mathcal B(u)|
 &\le C\int_0^\infty U(G_su)D_3(G_su)\,ds\\
 &\le {C\over\nu}\int_0^{X(u)}(3x)^{1/3}\,dx
 ={C\over4\nu}U(u)^4.                                \tag{6}
\end{aligned}
\]
The constant in the last display can absorb the constant in (2).

Consequently the saturated correction
\[
 \mathcal F_\delta(u)
 =X(u)-\delta\,{\mathcal B(u)\over1+U(u)/\nu}          \tag{7}
\]
is coercive for a sufficiently small fixed \(\delta>0\):
\[
 |\mathcal F_\delta(u)-X(u)|
 \le C\delta\,U(u)^3=3C\delta X(u).                   \tag{8}
\]
Thus saturation genuinely repairs the static quartic-versus-cubic
coercivity failure of the unsaturated functional \(X-\mathcal B\).

## 2. Differentiating the heat inverse

For a sufficiently high-Sobolev smooth state, use
\[
 P_3(u)=-\int\nabla p[u]\cdot |u|u\,dx.
\]
The finite-dimensional map \(z\mapsto |z|z\) is \(C^1\), including at zero,
and \(p[u]\) is quadratic. Thus \(P_3\) is \(C^1\) on a sufficiently high
Sobolev class, without differentiating \(z\mapsto|z|\) by itself.
Differentiation under (1) gives
\[
 D\mathcal B(u)[h]
 =-\int_0^\infty DP_3(G_su)[G_sh]\,ds.                \tag{9}
\]
Near \(s=0\), this follows from local smoothness of the quartic pressure
functional on the relevant Sobolev bounded set. At large \(s\), heat kernel
estimates for \(G_su\) and \(G_sh\), together with the multilinear version of
(2), give an integrable majorant. For Schwartz \(u,h\), this directly
justifies (9); the same identity extends to a strong trajectory whenever its
displayed Sobolev and heat-tail bounds are finite.

The heat direction is exact. Since
\[
 {d\over ds}P_3(G_su)=DP_3(G_su)[\nu\Delta G_su],
\]
integration by parts in \(s\), using \(P_3(G_su)\to0\), yields
\[
 D\mathcal B(u)[\nu\Delta u]=P_3(u).                  \tag{10}
\]
For Navier--Stokes,
\[
 u_t=\nu\Delta u-\mathbb P N(u),\qquad N(u)=(u\cdot\nabla)u,
\]
and hence
\[
 X'=P_3-\nu D_3,\qquad
 \mathcal B'=P_3-D\mathcal B(u)[\mathbb PN(u)].       \tag{11}
\]
These formulas are rigorous on the strong class just described. The
algebraic conclusions below require only (11) at states where it is defined.

## 3. Exact chain rule and the saturation defect

Let \(F=F(X,\mathcal B)\) be \(C^1\). Along a strong trajectory, (11) gives
\[
\begin{aligned}
 {d\over dt}F(X,\mathcal B)
 &=(F_X+F_{\mathcal B})P_3
   -\nu F_XD_3
   -F_{\mathcal B}D\mathcal B(u)[\mathbb PN(u)].
                                                               \tag{12}
\end{aligned}
\]
Thus exact algebraic cancellation of the full pressure work for all states
requires
\[
 F_X+F_{\mathcal B}=0.                                \tag{13}
\]
On each connected component, the \(C^1\) solutions of (13) are precisely
\[
 F(X,\mathcal B)=f(X-\mathcal B).                     \tag{14}
\]

The saturated functional (7) does not satisfy (13). Put
\[
 q(X)=\left(1+{(3X)^{1/3}\over\nu}\right)^{-1}.
\]
Then
\[
 F_X+F_{\mathcal B}
 =1-\delta q(X)-\delta q'(X)\mathcal B.               \tag{15}
\]
For the small \(\delta\) required by coercivity, the coefficient in (15)
remains generically of order one, rather than becoming a universal small
factor. Applying the absolute estimate (2) produces
\[
 |P_3|\le CUD_3,
\]
whose coefficient grows without bound relative to \(\nu D_3\) as
\(U/\nu\to\infty\). The saturation therefore trades the static coercivity
defect for an uncontrolled chain-rule pressure term.

## 4. No exactly cancelling scalar functional controls \(X\)

The full heat inverse is not identically zero. Indeed,
\[
 \mathcal B(G_tu)=-\int_t^\infty P_3(G_su)\,ds,\qquad
 {d\over dt}\mathcal B(G_tu)=P_3(G_tu).               \tag{16}
\]
The audited compact profile with \(P_3(u)>0\) makes the right side positive
at \(t=0\). Hence \(\mathcal B(G_tu)\) is nonconstant near zero, so some
solenoidal Schwartz field \(\phi\) has \(\mathcal B(\phi)\ne0\).
Replacing \(\phi\) by \(-\phi\) reverses \(\mathcal B\); take
\(\mathcal B(\phi)>0\).

Choose any solenoidal Schwartz field \(\chi\) linearly independent of
\(\phi\), and define a continuous path
\[
 \psi_s=\cos(\pi s)\phi+\sin(\pi s)\chi,\qquad 0\le s\le1.       \tag{17}
\]
It joins \(\phi\) to \(-\phi\) and never vanishes. Compactness of the
parameter interval gives
\[
 \inf_{0\le s\le1}X(\psi_s)>0.                        \tag{18}
\]
Both \(X(\psi_s)\) and \(\mathcal B(\psi_s)\) are continuous.

Amplitude homogeneity gives
\[
 X(a\psi_s)=a^3X(\psi_s),\qquad
 \mathcal B(a\psi_s)=a^4\mathcal B(\psi_s).            \tag{19}
\]
For every sufficiently large \(a\), the continuous function
\[
 h_a(s)=a\mathcal B(\psi_s)-X(\psi_s)
\]
is positive at \(s=0\) and negative at \(s=1\). Choose
\(s_a\in(0,1)\) with \(h_a(s_a)=0\). Then
\[
 X(a\psi_{s_a})-\mathcal B(a\psi_{s_a})=0,\qquad
 X(a\psi_{s_a})\ge a^3\inf_sX(\psi_s)\longrightarrow\infty.
                                                               \tag{20}
\]

This failure persists on every exact kinetic-energy shell. Given \(E>0\),
set
\[
 N_a={a^2\|\psi_{s_a}\|_2^2\over E},\qquad
 u_a(x)=aN_a\psi_{s_a}(N_ax).                          \tag{21}
\]
Then \(\|u_a\|_2^2=E\). Both \(X\) and the full heat inverse
\(\mathcal B\) are invariant under the Navier--Stokes spatial scaling
\(u(x)\mapsto Nu(Nx)\), so (20) remains true for \(u_a\).

It follows that every scalar functional with exact pressure cancellation,
\(F=f(X-\mathcal B)\), has
\[
 F(u_a)=f(0)
\]
while \(X(u_a)\to\infty\). No such functional is coercive in the critical
norm, even at fixed kinetic energy.

## Exact conclusion

Nonlinear saturation can make the full-heat correction cubic and coercive,
but its chain rule restores an order-one multiple of the original pressure
work. Conversely, exact cancellation forces dependence only on
\(X-\mathcal B\), and that scalar is noncoercive by the explicit path and
amplitude construction.

This excludes all \(C^1\) scalar modified energies depending only on
\((X,\mathcal B)\) that demand exact algebraic cancellation of \(P_3\). It
does not exclude approximate signed cancellation proved by another argument,
a functional depending on further norms or frequency profiles, a
time-nonlocal correction, or a direct estimate of
\(D\mathcal B(u)[\mathbb PN(u)]\).

## Frontier record

**MODE / RESULT:** REPAIR/FALSIFY. Saturation repairs coercivity but fails
the exact chain-rule cancellation; every exactly cancelling scalar
\(F(X,\mathcal B)\) is noncoercive.

**FIRST GAP:** a viable normal form must control the residual pressure
coefficient in (15), or use additional state variables so pressure
cancellation does not force reduction to \(X-\mathcal B\).

**SURVIVING CONDITIONAL SUFFIX:** if the nonlinear remainder
\(D\mathcal B(u)[\mathbb PN(u)]\) and any residual pressure term can be
absorbed with an integrable datum-dependent remainder, a modified-energy
argument may still feed the critical continuation theorem.

**NON-CLAIMS:** no universal HF estimate, critical bound, blow-up, or global
regularity result is proved.
