# Primary source table for HIGH-PRESSURE

Status: source audit for the signed high-frequency pressure estimate (HF) in
`docs/proof-graph.yaml`, checked 5 September 2026. The target is an estimate
for every smooth trajectory on \(\mathbb R^3\times[0,T_*)\), uniform for
\(\tau<\min\{H,T_*\}\), with an input-only remainder and a coefficient
\(\theta<1\) multiplying weighted cubic dissipation. None of these six
sources proves that target for arbitrary data.

| Source and exact checked result | Hypotheses and domain | Relation to HF and consumed unknown bound |
|---|---|---|
| **Tran–Yu, “Regularity of Navier–Stokes flows with bounds for the pressure” (2016).** For \(r\ge3\), \(q=(r+6)/3\) (so \(3\le q\le r\)), Lemma 2 assumes a pressure moderator \(P\) satisfying \(\|p+P\|_2\le c'_2\|u\|_4^2\). With \(c_1\) depending on \(c'_2\), \(\|u_0\|_2\), and the Sobolev constant, and \(\Omega(t)=\{|u|>c_1\|u(t)\|_{L^r}\}\), it proves \(\int_{\mathbb R^3\setminus\Omega}|p+P||u|^{q-2}\hat u\cdot\nabla|u|\le\frac12\||u|^{(q-2)/2}\nabla|u|\|_2^2\). [Full primary PDF](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/12230/Tran_2016_Regularity_AML_AAM.pdf?isAllowed=true&sequence=1), Lemma 2. | The unit-viscosity, unforced Cauchy problem on \(\mathbb R^3\), with smooth divergence-free sufficiently decaying data and a classical solution. | Closest spatial absorption mechanism; it leaves the high-velocity set and consumes the moderator estimate plus the trajectory-dependent \(L^r\) norm. The displayed left side is signed in the flux, although the pressure factor is replaced by \(|p+P|\). It gives neither an input-only remainder nor a fixed Fourier cutoff. |
| **Beirão da Veiga–Yang (2020), “On mixed pressure-velocity regularity criteria … in Lorentz spaces.”** Theorem 5.2 assumes \(\pi/(e^{-|x|^2}+|v|)^\theta\) in the stated Lorentz class, \(0\le\theta\le1\), \(2/p+3/q=2-\theta\), and concludes regularity. [Primary arXiv text](https://arxiv.org/html/2007.02089), §§5–6. | Leray–Hopf weak solutions on \(\mathbb R^3\) or \(\mathbb T^3\); the Gaussian is replaced by a positive constant on the torus. | Formalizes pressure–velocity coupling but consumes the mixed Lorentz norm. It does not estimate signed dyadic high pressure or produce \(\theta\nu D_3+A_{\rm high}\). |
| **Ji–Wang–Wei (2019/20), “New regularity criteria based on pressure or gradient of velocity in Lorentz spaces.”** Theorem 1.1(1) gives regularity from sufficiently small \(L^{p,\infty}_tL^{q,\infty}_x\) pressure with \(2/p+3/q=2\), \(3/2<q<\infty\); Theorem 1.1(2) gives the gradient-pressure analogue with \(2/p+3/q=3\), \(1<q<\infty\). Theorem 1.2 instead concerns small \(\nabla u\), with \(u_0\in L^2\cap W^{1,2}\). [Primary arXiv text](https://arxiv.org/html/1909.09960), Theorems 1.1–1.2. | The pressure alternatives take a weak solution on unforced \(\mathbb R^3\) with divergence-free \(u_0\in L^2\cap L^4\); small critical Lorentz pressure quantity is assumed. | Consumes pressure smallness, stronger than energy. No signed high-tail estimate or input-only \(A_{\rm high}\). |
| **Beirão da Veiga–Yang (2020), Lemma 6.1.** For a regular solution \((v,\pi)\) on \(\Omega\times[0,T]\), \(\frac14\frac d{dt}\int|v|^4+\frac12\int|\nabla v|^2|v|^2+\frac12\int|\nabla|v|^2|^2\le\int|\pi|^2|v|^2\). [Primary arXiv HTML](https://arxiv.org/html/2007.02089#S6.Thmlemma1), Lemma 6.1. | The source’s relevant applications are \(\Omega=\mathbb R^3\) or \(\mathbb T^3\), with unit viscosity; the pressure is controlled absolutely by \(\pi^2|v|^2\). | Directly verifies the weighted-energy structure adjacent to the \(|u|^3\) test, but loses signed pressure cancellation and consumes a weighted pressure norm. It cannot imply HF. |
| **He–Wang–Zhou (2017/2019), “New \(\varepsilon\)-regularity criteria … at one scale.”** Theorem 1.1: a suitable weak solution in \(Q(1)\) with \(\|u\|_{L^{p,q}}+\|\Pi\|_{L^1}<\varepsilon\), \(1\le2/q+3/p<2\), is bounded in \(Q(1/2)\), where the paper’s convention is \(L^{p,q}=L^q_tL^p_x\). [Primary arXiv HTML](https://arxiv.org/html/1709.01382#S1.Thmtheorem1), Theorem 1.1. | Local suitable weak solutions in \(Q(1)=B(1)\times(-1,0)\); pressure decomposition is used with scale-local smallness. | Local pressure cancellation cannot give a whole-space, finite-horizon input-only bound. It consumes \(\varepsilon\)-smallness at a scale and does not control the aggregate high-frequency flux. |
| **Tran–Yu–Dritschel, “Velocity–pressure correlation in Navier–Stokes flows and the problem of global regularity” (JFM, 2021).** Theorem 3.1(a) assumes a 3D Leray–Hopf solution smooth on \((0,T)\) and, for some \(s>3\), the exact condition \(\int_0^T(\Gamma_s/R_0^2)^{s/(s-3)}\|u\|_{L^s}^{2s/(s-3)}dt<\infty\) (3.16). Equations (3.21)–(3.23) are a distinct \(L^3\) family using \(\Gamma'_s\), \(\|p\|_{L^s(\Omega_0)}\), \(R_0\), and \(\|u\|_3^{-3}\). [Primary full article](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/velocitypressure-correlation-in-navierstokes-flows-and-the-problem-of-global-regularity/CE28509C5B6844BC5F27F3EF52075E47), Theorem 3.1 and §§3–4. | Smooth Leray–Hopf solutions of the unit-viscosity 3D initial-value problem on \(\mathbb R^3\); \(\Gamma_s\) is a pressure–velocity correlation over a driving set. | Most direct endpoint logarithmic/Osgood mechanism, but it consumes correlation integrability, higher velocity norms, and \(\|u\|_3\)-dependent ratios. The article notes the pressure-work integrand is not sign definite; no Fourier high-tail absorption follows. |

## Audit conclusion

The sources establish pressure recovery by a Riesz-transform quadratic, weighted
\(|u|^{q-2}u\) diffusion, pressure moderators, local pressure decomposition,
and correlation-based Osgood criteria. Every result consumes an additional
pressure, correlation, smallness, symmetry, or critical velocity bound. None
proves, for arbitrary Schwartz data and every \(\tau<\min\{H,T_*\}\),
\[
 \int_0^\tau H_J(t)\,dt\le\theta\nu\int_0^\tau D_3(t)\,dt+A_{\rm high}(u_0,\nu,H,J),
 \qquad \theta<1,
\]
with no unknown trajectory norm on the right. No inspected source proves a
signed telescoping law or input-only high-frequency pressure absorption, so
HIGH-PRESSURE remains open.
