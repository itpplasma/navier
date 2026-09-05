# HF10: primary-source check for pressure–speed corrections

Status: literature evidence only; no proof claim. Search completed 2026-09-05.

## Scope and conclusion

The exact static correction
\[
B(u)=\int_{\mathbb R^3}p|u|\,dx,
\qquad p=R_iR_j(u_i u_j),
\]
and the exact coefficient-one functional
\(\frac13\int|u|^3+B(u)\) were not found in the primary sources checked. No
priority or novelty claim follows from this finite search. The closest primary
literature consists of (i) a Bernoulli-pressure pointwise criterion and (ii) a
paper that explicitly derives the pressure-speed work term in the \(L^q\)
evolution, with conditional regularity criteria based on other norms.

## 1. Seregin–Šverák (2002): Bernoulli quantity

G. Seregin and V. Šverák, “Navier–Stokes Equations with Lower Bounds on the
Pressure,” *Archive for Rational Mechanics and Analysis* **163** (2002),
65–86, DOI [10.1007/s002050200199](https://doi.org/10.1007/s002050200199).
The authors’ primary preprint is available at
[pdmi.ras.ru/~seregin/Recent\_Publications/Pres.pdf](https://www.pdmi.ras.ru/~seregin/Recent%20Publications/Pres.pdf).

Exact location: Theorem 2.2 (PDF pp. 69–70; equations (2.7)–(2.10)). Let
\(v\) be a Leray–Hopf solution of the whole-space 3-D Cauchy problem and let
\(p\) be the normalized pressure. Assume there is a nonnegative \(g\) satisfying
condition (C): for every \(t_0>0\), some \(R_0(t_0)>0\) makes
\[
 \sup_{x_0}\sup_{t_0-R_0^2\le t\le t_0}
 \int_{B(x_0,R_0)}\frac{g(x,t)}{|x-x_0|}\,dx<\infty,
\]
and, for each fixed \(x_0\) and \(R\le R_0\), the displayed spatial integral
is left-continuous in time at \(t_0\). If either
\[
 |v|^2+2p\le g
 \quad\text{or}\quad
 p\ge-g
\]
pointwise, then \(v\) is Hölder continuous on \(\mathbb R^3\times(0,\infty)\),
and hence smooth and unique. Their Remark 2.3 notes that a positive constant
\(g\) satisfies (C).

This is a conditional theorem for a Leray–Hopf solution, with smooth/decaying
initial data as described in the paper’s introduction and with normalized
pressure. It does not establish the criterion for arbitrary data, does not use
\(\int p|u|\), and does not provide a finite-horizon pressure-speed absorption
estimate. The Bernoulli expression is \(|v|^2+2p=2(p+|v|^2/2)\), so its use is
pointwise upper control of the positive part, not testing against \(|v|\).

## 2. Chuong V. Tran (2021): explicit pressure-speed work term

C. V. Tran, “Velocity–pressure correlation in Navier–Stokes flows and the
problem of global regularity,” *Journal of Fluid Mechanics* **911** (2021),
A18, DOI [10.1017/jfm.2020.1033](https://doi.org/10.1017/jfm.2020.1033),
[open article](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/velocitypressure-correlation-in-navierstokes-flows-and-the-problem-of-global-regularity/CE28509C5B6844BC5F27F3EF52075E47).

Exact locations: equation (3.14) and Theorem 3.1 (HTML lines 642–658; article
§3.2). For a Leray–Hopf solution of the 3-D Navier–Stokes initial-value problem
that is smooth on \((0,T)\), the paper derives
\[
\frac1q\frac d{dt}\|u\|_q^q
\le (q-2)\int_{\Omega_0}p|u|^{q-2}\widehat u\cdot\nabla|u|\,dx
 -\text{dissipation terms}.
\]
At \(q=3\), the pressure integrand is exactly
\(p\,u\cdot\nabla|u|\), the pressure-speed work \(P_3\) used in HF10.
However, the paper’s Theorem 3.1 regularity criteria are for \(s>3\) (or
\(3<s\le5\), or \(s>5\)) and require finiteness of the time integrals in its
equations (3.16)–(3.18), involving \(\Gamma_s\), \(R_0\), and velocity norms.
They assume smoothness up to the candidate time and conclude continuation
beyond it. These are conditional criteria, not full arbitrary-data global
regularity and not an estimate for \(B(u)=\int p|u|\).

The same source explicitly states the whole-space setup with viscosity set to
one, divergence-free \(u_0\in L^2(\mathbb R^3)\) (equations (1.1)–(1.3)); viscosity
normalization is harmless for comparison but means its formulas are not written
for arbitrary \(\nu\).

## Evidence boundary

The checked primary sources therefore support only these statements: the exact
pressure-speed work appears in the standard \(L^q\) balance (and at \(q=3\)
is \(P_3\)); Bernoulli pressure \(p+|u|^2/2\) has a conditional pointwise
regularity criterion. Neither source proves the exact \(\int p|u|\) correction,
its coefficient-one coercivity, or the HF10 signed finite-horizon absorption
claim.
