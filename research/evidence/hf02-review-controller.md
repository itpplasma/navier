# Proof audit of HF01 controller Sections 1--2

VERDICT: **PASS**

REVIEWED SCOPE: Sections “Existential HF and global strong continuation” and
“Repair of the amplitude split” in hf01-controller.md, frozen at repository
base 169ec50daa9295e0a713236bf969c2f42a507f51 with complete-file SHA-256
d05a7450d61cdfdc4651588e707dfc27121d486742b4f0eac30ac60658f30142.
Both values were independently reproduced. The audit checks quantifiers,
strong/mild continuation scope, all interpolation exponents, energy powers,
and the relation of the remaining amplitude-tail condition to critical
\(L^3\) control.

FIRST BAD BRIDGE: none. The controller uses the same ordinary existential
quantifiers as the current manuscript, graph, and plan. The reverse
construction is explicitly conditional on \(G\) and is offered as a logical
equivalence, not as a noncircular proof of HF.

EVIDENCE:

1. **Forward implication.** The declared existential HF implies the finite-horizon
   \(L^3\) estimate through the audited low-frequency bound and exact cubic
   balance. If \(T_*<\infty\), choosing \(H>T_*\) gives
   \(\sup_{t<T_*}\|u(t)\|_3<\infty\); viscosity normalization and the imported
   GKP/ESS endpoint theorem then give \(T_*=\infty\), a contradiction. Thus
   \(\mathrm{HF}\Rightarrow G\).

2. **Reverse implication at the weaker strength.** Assume \(G\) for the
   selected maximal strong branch from Schwartz data. Persistence gives
   bounded high Sobolev norms on every compact interval \([0,H]\). The
   classical/mild branch identification is justified by local uniqueness and
   persistence; no assertion about every conceivable smooth finite-energy
   solution is needed. Uniform \(L^3\) multiplier bounds give
   \[
    |Q_0(t)|\leq C\|u(t)\|_6^3\|\nabla u(t)\|_2,
   \]
   which is integrable on \([0,H]\). Hence \(J=0\), \(\theta=0\), and the
   trajectory integral above prove \(\mathrm{HF}\). Because the
   global selected trajectory is unique for the datum, this finite number is
   set-theoretically a datum-dependent remainder, exactly at the weak
   existential strength declared by the controller. Any fixed
   \(\theta\in[0,1)\) also works because \(D_3\geq0\). This establishes
   \[
    \mathrm{HF}\quad\Longleftrightarrow\quad G.
   \]
   This equivalence is therefore correct. It cannot be used to establish HF
   without circularity, because its reverse direction assumes \(G\).

3. **Low-amplitude pressure exponent.** On \(\{|u|\leq K\}\),
   \[
   \begin{aligned}
    \|p_J^\ell\|_3
    &\leq C\|u_i u_j\mathbf1_{|u|\leq K}\|_3\\
    &\leq C\left(\int_{|u|\leq K}|u|^6\right)^{1/3}
     \leq CK^{4/3}\left(\int|u|^2\right)^{1/3}
     \leq CK^{4/3}E_0^{1/3}.
   \end{aligned}
   \]
   The \(L^3\) multiplier norm of \((I-S_J)R_iR_j\) is uniform in \(J\).
   Formula (1) is correct.

4. **High-amplitude interpolation.** Interpolation at
   \(1/6=(1/4)(1/3)+(3/4)(1/9)\) gives
   \[
    \|u\mathbf1_{|u|>K}\|_6^2
    \leq B_K^{1/2}\|u\mathbf1_{|u|>K}\|_9^{3/2}
    \leq B_K^{1/2}\|u\|_9^{3/2}.
   \]
   For \(f=|u|^{3/2}\), homogeneous Sobolev and
   \(|\nabla f|=(3/2)|u|^{1/2}|\nabla|u||\) give
   \(\|u\|_9^{3/2}=\|f\|_6\leq CD_3^{1/2}\).
   No derivative of the amplitude indicator is taken. Formula (2) is
   correct.

5. **Test-factor exponent.** Writing
   \(u\nabla|u|=|u|^{1/2}(|u|^{1/2}\nabla|u|)\), Hölder with
   \(1/(3/2)=1/6+1/2\) gives
   \[
    \|u\nabla|u|\|_{3/2}
    \leq \||u|^{1/2}\|_6
          \||u|^{1/2}\nabla|u|\|_2
    \leq U^{1/2}D_3^{1/2}.
   \]
   Formula (3) is correct.

6. **Combined estimate and Young exponent.** The high source contributes
   \(C(UB_K)^{1/2}D_3\). The low source contributes
   \(CK^{4/3}E_0^{1/3}U^{1/2}D_3^{1/2}\), which Young's inequality bounds by
   \[
    \varepsilon D_3+
    C\varepsilon^{-1}K^{8/3}E_0^{2/3}U.
   \]
   Thus (4), including every exponent, is correct.

7. **Time integration and energy power.** Hölder in time and the standard
   energy interpolation yield
   \[
    \int_0^\tau U\,dt
    \leq H^{3/4}\left(\int_0^\tau U^4dt\right)^{1/4}
    \leq CH^{3/4}\nu^{-1/4}E_0^{1/2}.
   \]
   Multiplying by the coefficient in (4) gives
   \(C\varepsilon^{-1}K^{8/3}H^{3/4}\nu^{-1/4}E_0^{7/6}\).
   Formulas (5)--(6) are correct.

8. **Exact absorption threshold.** To obtain an HF coefficient
   \(\theta\nu\), one needs fixed choices satisfying
   \[
    \varepsilon+C(UB_K)^{1/2}\leq\theta\nu.
   \]
   For example, take \(\varepsilon=\theta\nu/2\) and require
   \[
    \sup_{t<\min\{H,T_*\}}U(t)B_K(t)
    \leq \left(\frac{\theta\nu}{2C}\right)^2.           \tag{A}
   \]
   The controller's phrase “uniformly small” should be replaced by (A) or an
   equivalent explicit threshold. This remains an unproved input.

9. **Tail condition already controls \(L^3\).** The amplitude split gives
   \(U^3\leq KE_0+B_K^3\). If \(UB_K\leq L<\infty\), then, for \(U>0\) and
   \(X=U^3\),
   \[
    X\leq KE_0+\frac{L^3}{X},
    \qquad
    X\leq\frac{KE_0+\sqrt{K^2E_0^2+4L^3}}2.
   \]
   The case \(U=0\) is immediate. Formula (7) is correct. Consequently,
   uniform finiteness of \(UB_K\) for one fixed \(K\) gives a uniform critical
   bound, and the small threshold (A) is stronger than mere critical
   boundedness. Conversely, \(U\leq M\) gives \(UB_K\leq U^2\leq M^2\), but
   does not generally give the smallness in (A). The source split repairs the
   artificial \(K\|u\|_4^4\) remainder but does not produce new critical
   control.

REPLACEMENT ARGUMENT: none required for correctness. Replace “uniformly
small” by the explicit sufficient threshold (A); this is a precision
improvement rather than a repair of a false inference. An explicit formula
in a fixed list of initial-data norms would be quantitatively stronger than
HF, as the controller correctly states, but is not part of the present
existential claim.

CONDITIONAL SUFFIX THAT SURVIVES: the amplitude-source decomposition,
estimates (1)--(6), and algebraic tail implication (7) survive. Under (A),
they yield HF if (A) itself is proved uniformly with the required quantifier
order and without assuming the continuation conclusion. HF then yields critical \(L^3\)
control and global continuation of the selected strong branch.

UNNECESSARY DEPENDENCIES: strict \(\theta<1\) is unnecessary for critical
control and endpoint continuation; \(\theta\leq1\) suffices there. Strictness
is used only to retain positive \(D_3\) control and in threshold (A). The
reverse construction of \(\mathrm{HF}\) needs no amplitude split.

NON-CLAIMS: this audit does not prove (A), HF without assuming \(G\), global
continuation, or a Clay alternative. It does not extend the selected
strong/mild branch argument to arbitrary weak or otherwise nonunique
solution classes.

REOPENING CONDITION: use the equivalence as a forward proof route only after
HF is established without assuming \(G\), the desired critical supremum, or
the finiteness of the pressure-work supremum being bounded. Reopen the
amplitude route after proving (A), or a comparable absorptive estimate, for
one fixed \(K\) uniformly through \(\min\{H,T_*\}\), without assuming the
same continuation conclusion.
