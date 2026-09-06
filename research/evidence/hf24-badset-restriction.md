# HF24-B: the bad-set restriction of (G) under the new regularity

Lane HF24-B, **MODE: DISCOVER**, 2026-09-06. Owned file:
`research/evidence/hf24-badset-restriction.md`. Nothing else in the repository
is edited, nothing is committed, nothing is promoted, the manuscript is
untouched. **(G) is neither proved nor refuted here, and NS-R3 remains open.**

**Inputs** [DI = directly inspected]: `PLAN.md` ("Frontier packet", "Beyond the
checkpoint", "HF18"–"HF23", "Ordered next actions"); `../navier-paper/main.tex`
`sec:quotient` read in full, in particular `def:quotient`,
`lem:quotient-minimizer`, `lem:quotient-coercive`, `lem:quotient-scaling`,
`def:qe-dissipation`, `lem:quotient-heatsign`, `prop:quotient-evolution`,
`lem:quotient-lowstrain`, `hyp:highstrain`, `rem:highstrain-normalisation`,
`prop:quotient-conditional`, `rem:highstrain-scope`, `rem:no-monotone`,
`rem:distance-balance`, and the newly imported
`lem:trace-control`, `prop:quotient-divcurl`, `cor:quotient-defect`,
`cor:quotient-vorticity-zero`, `lem:quotient-mixed-pressure`,
`cor:quotient-budgets`, `rem:quotient-divcurl-scope`, `rem:quotient-scope`;
outside that section `prop:localtheory`, `lem:upgrade`, `prop:energy`,
`prop:enstrophy` \eqref{eq:enstrophy}, `prop:scaling`(iii)
\eqref{eq:L4L3}/\eqref{eq:L4L3-constant}, `lem:GN`, `lem:sobolev`,
`lem:interp`, `def:sobolev-constant`, `def:D3P3`, `hyp:critical`,
`thm:continuation`, `thm:conditional`;
`research/evidence/hf22-good-set-dissipation.md` (audited REPAIR, repairs
applied) §§0–5 with Theorem A, Theorem B, the constraint list (T1)–(T9) and
the repaired family Theorem C′; `hf22-review-good-set-dissipation.md`;
`hf21-crossing-sign-structure.md` §§0–4 (Theorem 4.5 = crossing/measure bound);
`hf22-direct-attack.md` §2 (Propositions 2.1, 2.3, 2.4, Corollary 2.2: the
exact interpolation deficit \(\tfrac12\) and the Hölder overshoot
\(\tfrac2{3s}\)); `hf23-review-regularity-core.md` (PASS) for the scope of the
import.

---

## RESULT

Five findings, in the order the lane's four instructions ask for them.

1. **The instructed step (1) does not go through as posed, and its
 unconditional substitute is exactly the audited measure bound.** On
 \(\mathcal B_\delta\) the defining inequality forces
 \(Y=\|\nabla u\|_2^2>y_\delta:=\delta^4\nu^4/(48C_S^2C_\sharp^4E_0)\)
 (Prop. 1.1), and Chebyshev against the energy identity returns
 \(|\mathcal B_\delta|\le24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}=\beta\),
 the audited HF21-B constant **exactly**, digit for digit. The route through
 the *new* regularity — "Sobolev on \(q\), whose gradient is now in \(L^2\)" —
 is **not available**: by scaling the only admissible monomial is
 \(\|q\|_3\le C\|\nabla q\|_2^{1/2}\|u\|_2^{1/2}\) (Prop. 1.3), and it is not
 derivable from the audited record, because the two inequalities that would
 give it are exactly the two gaps the import left open (\(w\in L^2\), which
 `rem:quotient-divcurl-scope` explicitly declines to assert, and
 \(\sigma\in L^{3/2}\), the residual (H2)). Worse, **granting it changes
 nothing**: the new spacetime budgets of `cor:quotient-budgets` are fixed
 multiples of the energy budget (\(\tfrac54\) and \(\tfrac14\)), so the
 Chebyshev step through them returns the *same* bound with a worse constant —
 \(5\beta\) through \(\int\|\nabla w\|_2^2\) (Prop. 1.4). **The import adds no
 new time-integrability, hence no new cost on the bad set.**
2. **One genuinely new inequality: the first upper bound for the quotient
 dissipation.** For every solenoidal \(u\in H^m\), \(m\ge4\),
 \[
  D_{\mathcal Q}(u)=D_3(w)\le2\|w\|_6\|\nabla w\|_2\|\nabla u\|_3
  \le\tfrac52C_S\,Y\,\|\nabla u\|_3
  \le\tfrac{5\sqrt3}2C_S^{3/2}\,Y^{5/4}\|\Delta u\|_2^{1/2}
 \]
 (Theorem 2.1), scaling-exact. Before the import only the *lower* bound
 \(D_3(w)\ge c\|u\|_9^3\) existed. It is then shown **not to help**: any
 Hölder-in-time route that retains a positive power of \(D\) needs
 integrability of \(D\), of which the audited record has none (§2.3).
3. **A new reduction, sharper than the audited Theorem B, and a conditional
 criterion.** For every \(\delta\in(0,1)\) and \(\tau<T_*\),
 \[
  \int_0^\tau K\,dt\ \le\ \frac{\delta}{1-\delta}\,\mathcal Q(u_0)
  \;+\;\frac1{1-\delta}\int_{\mathcal B_\delta}K\,dt
  \tag{R1}
 \]
 (Theorem 3.1: the audited Theorem B with \(cD\) replaced by \(K\) throughout,
 which is admissible and strictly sharper). Feeding the *new* pointwise bound
 \(|K|\le\frac58C_S^3Y^2\) of `lem:quotient-mixed-pressure` into the remainder
 gives the **bad-set enstrophy criterion** (Theorem 3.3): if
 \(\operatorname*{ess\,sup}_{\mathcal B_\delta}Y\le N\) with \(N\) input-only,
 then `hyp:highstrain` holds with \(\theta=0\) and
 \(A_{\rm input}=\frac{\delta}{3(1-\delta)}\|u_0\|_3^3
 +\frac{5C_S^3E_0N}{16\nu(1-\delta)}\), hence the Clay conclusion for that
 datum. The hypothesis is **strictly weaker than a Serrin bound**: it
 constrains the enstrophy only on a set of times of input-bounded measure
 \(\beta\), and says nothing on the good set, where the enstrophy may be
 unbounded.
4. **The deficit, computed exactly, is one factor of the peak enstrophy on the
 bad set.** The route yields, unconditionally,
 \[
  \int_0^\tau K\,dt\ \le\ \frac{\delta}{3(1-\delta)}\|u_0\|_3^3
  +\frac{5C_S^3E_0}{16\nu(1-\delta)}\operatorname*{ess\,sup}_{\mathcal B_\delta}Y ,
 \]
 input-only **except for that single factor**, and the factor is sharp: the
 plateau family \(Y\equiv M\) on a subset of \(\mathcal B_\delta\) of measure
 \(E_0/(2\nu M)\) satisfies every audited budget and drives
 \(\int_{\mathcal B_\delta}Y^2=ME_0/(2\nu)\to\infty\) (Prop. 4.2). In
 Ladyzhenskaya–Prodi–Serrin bookkeeping (Prop. 4.3): the audited input hull sits
 at \(\lambda=\frac32\) and the new budgets sit **on the same point**
 \((2,6)\) of it, adding a new object but no new point; the \(cD\)/Hölder route
 demands \(\lambda=\frac56\), i.e. it *overshoots* the Serrin line by
 \(\frac16\); the new \(K\)-route demands \(\lambda=1\) **exactly**, overshoot
 \(0\). So the import buys precisely the removal of the \(\frac16\) overshoot
 and leaves the \(\frac12\) deficit of `hf22-direct-attack` Corollary 2.2
 untouched. **The restriction to the bad set contributes nothing to either
 number**: the measure bound is inert in the Hölder exponent, and can only be
 traded for a strictly worse exponent (Prop. 4.4).
5. **The audited obstruction family survives the import, and it obstructs the
 bad-set restriction as well as the good-set one.** Theorem C′ of HF22-C
 carries its entire excess on \(\mathcal B_\delta\), so verbatim it shows the
 bad-set restriction is not derivable from (T1)–(T9). §5 augments the
 constraint list with everything the import supplies — \((T10)\)
 \(|K|\le\frac58C_S^3Y^2\), \((T11)\) \(\int Y\le E_0/2\nu\), \((T12)\)
 \(c\le2C_\sharp(3C_S^2E_0Y)^{1/4}\), \((T13)\) Theorem 2.1, \((T14)\) the
 enstrophy inequality \eqref{eq:enstrophy} — and verifies that the family still
 satisfies all of them, at the price of a spike enstrophy \(Y\gtrsim n\) and a
 fixed numerical condition with slack \(\approx5\times10^6\), both independent
 of \(n\) (Theorem 5.1). **Non-derivability, not falsity**, and the list is not
 claimed exhaustive.

**Verdict for the wave.** The bad-set restriction is *not* closed by the new
regularity. What the regularity does is convert the gap from a statement about
the pair (distance, dissipation) into a statement about the enstrophy alone on
a set of input-bounded measure, at the Serrin line with zero overshoot. What it
does not do is supply any spacetime integrability beyond the energy budget, and
that — one power of \(Y\) — is the whole of the remaining deficit.

---

## 0. Notation and the facts used

\(u\) is the maximal classical branch of `prop:localtheory` on \([0,T_*)\) from
a divergence-free Schwartz datum \(u_0\), \(\nu>0\), \(E_0=\|u_0\|_2^2\); the
package (R) of `subsec:qe-trajectories` holds on every compact subinterval, so
\(u(t)\in H^m\) for every \(m\) and every \(t<T_*\). At each such \(t\) write
\[
 q=q(u(t)),\quad w=u+q,\quad A=|w|w,\quad \sigma=-\operatorname{div}w,\quad
 \mathcal Q=\tfrac13\|w\|_3^3,\quad Y=\|\nabla u\|_2^2,
\]
\(D=D_{\mathcal Q}(u)=D_3(w)\ge0\) (`def:qe-dissipation`,
`lem:quotient-heatsign`, and HF18-A for the identification), \(K=K_u\) the
strain work on the right of \eqref{eq:quotient-evolution}, and, following
HF22-C,
\[
 c(t):=C_\sharp\|q(t)\|_3,\qquad C_\sharp=\tfrac32C_9C_S,\qquad
 \mathcal B_\delta=\{t\in(0,\tau):c(t)>\delta\nu\},\quad
 \mathcal G_\delta=(0,\tau)\setminus\mathcal B_\delta .
\]
\(C_S\) is `def:sobolev-constant`; for fields \(\|z\|_6\le C_S\|\nabla z\|_2\)
\eqref{eq:qdc-sobolev-field}. The target is

> **(G)** \(\displaystyle\int_0^\tau\|q(u(t))\|_3D_3(w(t))\,dt\le
> A_{\rm input}(\nu,u_0,H)\) uniformly for \(\tau<\min\{H,T_*\}\),

which by \(|K|\le cD\), `rem:highstrain-normalisation` and
`prop:quotient-conditional` implies `hyp:highstrain` with \(\theta=0\) and then
the Clay target; at these quantifiers it is equivalent to global continuation
of the branch, so nothing below is called closed.

Audited facts used, each cited where used:

- **(A1)** `prop:quotient-evolution` [DI]: \(\mathcal Q\circ u\in C^1\),
 \(\mathcal Q'+\nu D=K\), \(D\ge0\), all terms continuous.
- **(A2)** the sharpened size bound (HF21-B Prop. 3.1, audited):
 \(|K|\le C_\sharp\|q\|_3D_3(w)=cD\).
- **(A3)** `lem:quotient-coercive` [DI]: \(\mathcal Q\le\frac13\|u\|_3^3\) and
 \(\|w\|_3\le\|u\|_3\), hence \(\|q\|_3\le2\|u\|_3\);
 \(\|u\|_3^3\le3C_{\mathbb P}^3\mathcal Q\).
- **(A4)** `prop:energy` [DI]: \(\|u(t)\|_2^2\le E_0\) and
 \(\int_0^\tau Y\,dt\le E_0/(2\nu)\) for every \(\tau<T_*\).
- **(A5)** \eqref{eq:L4L3-constant} [DI]: \(\|u\|_3^4\le3C_S^2\|u\|_2^2Y\)
 pointwise in \(t\); with (A4), \(\|u\|_3^4\le3C_S^2E_0Y\).
- **(A6)** `prop:quotient-divcurl` [DI, audited PASS]: for solenoidal
 \(u\in H^1\), \(\nabla w,\nabla q\in L^2\), \(w,q\in L^6\),
 \(\|\nabla w\|_2^2\le\frac54Y\), \(\|\nabla q\|_2^2=\|\sigma\|_2^2\le\frac14Y\),
 \(\operatorname{curl}w=\operatorname{curl}u\); **no** claim \(w\in L^2\).
- **(A7)** `cor:quotient-defect` [DI]: \(A\in W^{1,3/2}(\R^3;\R^3)\) with
 \(|\nabla A|_F\le2|w||\nabla w|_F\) a.e.; \(\sigma=-\operatorname{div}w\) a.e.
 and distributionally, \(\|\sigma\|_2\le\frac12\|\nabla u\|_2\);
 \(\partial_kq_j=R_jR_k\sigma\).
- **(A8)** `lem:quotient-mixed-pressure` [DI]: \(K=\int\sigma\Pi_u\) with
 \(\Pi_u=R_iR_j(u_iA_j)\), \(\|\Pi_u\|_2\le\|u\|_6\|w\|_6^2\), and
 \(|K|\le\frac58C_S^3Y^2\) \eqref{eq:qdc-KY}.
- **(A9)** `cor:quotient-budgets` [DI]: \(\int_0^\tau\|\nabla w\|_2^2\le5E_0/(8\nu)\)
 and \(\int_0^\tau\|\sigma\|_2^2\le E_0/(8\nu)\), \(\tau\)-uniform.
- **(A10)** `lem:GN` [DI]: \(\|\nabla u\|_3\le(3C_S)^{1/2}Y^{1/4}\|\Delta u\|_2^{1/2}\);
 `prop:enstrophy` \eqref{eq:enstrophy} [DI]:
 \(\frac12Y'+\frac\nu2\|\Delta u\|_2^2\le C_E\nu^{-3}Y^3\),
 \(C_E=\frac{2187}{32}C_S^6\).
- **(A11)** HF22-C Theorem A/B (audited, repairs applied): the master deficit
 inequality and the reduction of (G) to \(\int_{\mathcal B_\delta}cD\); HF21-B
 Theorem 4.5 (audited, \(\tau\)-uniform form): \(|\mathcal B_\delta|\le\beta\).
- **(A12)** HF18-A (Q6), audited: \(D_3(w)\ge\frac{8}{9C_S^2C_9^3}\|u\|_9^3\).

Scaling conventions are those of HF21-B §0: under \(u\mapsto\lambda u(\lambda\cdot)\)
and the amplitude grading \(u\mapsto au\), a quantity of type \((a^m,\lambda^k)\)
carries \(a^m\lambda^k\). Then
\(\mathcal Q,\|q\|_3,\|u\|_3\sim(a^3,\lambda^0)\) resp. \((a,\lambda^0)\),
\(c,\nu\sim(a,\lambda^0)\), \(D\sim(a^3,\lambda^2)\), \(Y\sim(a^2,\lambda)\),
\(E_0\sim(a^2,\lambda^{-1})\), \(dt\sim(a^{-1},\lambda^{-2})\),
\(\|\nabla w\|_2,\|\sigma\|_2\sim(a,\lambda^{1/2})\),
\(\|\nabla u\|_3\sim(a,\lambda)\), \(\|\Delta u\|_2\sim(a,\lambda^{3/2})\).

---

## 1. What the bad set forces, and why the new regularity does not sharpen it

### 1.1 The unconditional enstrophy cost

**Proposition 1.1 (enstrophy lower bound on the bad set).** For every
\(\delta\in(0,1]\), every \(\tau<T_*\) and every \(t\in\mathcal B_\delta\),
\[
 \|u(t)\|_3>\frac{\delta\nu}{2C_\sharp},
 \qquad
 Y(t)\ >\ y_\delta:=\frac{\delta^4\nu^4}{48\,C_S^2\,C_\sharp^4\,E_0}\ .
 \tag{1.1}
\]

*Proof.* On \(\mathcal B_\delta\), \(C_\sharp\|q\|_3>\delta\nu\); by (A3)
\(\|q\|_3\le2\|u\|_3\), giving the first bound. By (A5),
\(Y\ge\|u\|_3^4/(3C_S^2E_0)>\delta^4\nu^4/(16C_\sharp^4\cdot3C_S^2E_0)\). \(\square\)

*Scaling.* \(y_\delta\sim(a^4/a^2,\lambda^4\cdot\lambda^{-0}/\lambda^{-1})\):
explicitly \(\nu^4/E_0\sim(a^4,\lambda^0)/(a^2,\lambda^{-1})=(a^2,\lambda)=Y\) ✓.

**Corollary 1.2 (the audited measure bound is exactly this cost).** With (A4),
\(y_\delta|\mathcal B_\delta|\le\int_{\mathcal B_\delta}Y\,dt\le E_0/(2\nu)\), so
\[
 |\mathcal B_\delta|\ \le\ \frac{E_0}{2\nu\,y_\delta}
 =\frac{24\,C_S^2C_\sharp^4E_0^2}{\delta^4\nu^5}=\beta ,
 \qquad\text{uniformly in }\tau<T_* ,
\]
which is (1.2) of HF22-C / Theorem 4.5 of HF21-B **with the identical
constant**. So the instruction's step (1) — "a large distance costs enstrophy"
— is, unconditionally, precisely the audited crossing-measure bound and
contains no new information. \(\square\)

### 1.2 The route through the new regularity is unavailable, and would be inert

The lane brief anticipates a bound \(\|q\|_3\le C\|\nabla q\|_2^{a}(\cdot)^{\cdot}\)
"that the regularity now permits, via Sobolev on \(q\) whose gradient is in
\(L^2\)". It does not permit one.

**Proposition 1.3 (scaling enumeration).** Let the admissible ingredients be
the quantities the import supplies together with the energy, i.e.
\(\|\nabla q\|_2=\|\sigma\|_2\), \(\|\nabla w\|_2\), \(Y^{1/2}\), \(\|u\|_2\),
\(\nu\). A bound \(\|q\|_3\le C\prod_i X_i^{\theta_i}\) that is consistent with
both gradings and does not already contain \(\|u\|_3\) must have
\[
 \|q\|_3\ \le\ C\,\|\nabla q\|_2^{1/2}\,\|u\|_2^{1/2}
 \tag{1.2}
\]
up to replacing \(\|\nabla q\|_2\) by \(\|\nabla w\|_2\) or \(Y^{1/2}\)
(equivalently, the exponent pair is forced).

*Proof.* Write the candidate as \(\|\nabla q\|_2^{\alpha}\|u\|_2^{\beta}\nu^{\gamma}\).
Dilation: \(\|q\|_3\sim\lambda^0\), \(\|\nabla q\|_2\sim\lambda^{1/2}\),
\(\|u\|_2\sim\lambda^{-1/2}\), \(\nu\sim\lambda^0\), so
\(\frac\alpha2-\frac\beta2=0\). Amplitude: \(\|q\|_3\sim a\),
\(\|\nabla q\|_2\sim a\), \(\|u\|_2\sim a\), \(\nu\sim a\), so
\(\alpha+\beta+\gamma=1\). With \(\alpha=\beta\) this leaves the one-parameter
family \(\alpha=\beta=(1-\gamma)/2\). A factor \(\nu^{\gamma}\) with
\(\gamma\ne0\) is inadmissible in a bound valid for the functional
\(\mathcal Q\) alone, which knows nothing of the viscosity
(`rem:quotient-scope`: the estimates are properties of a functional on
\(L^3\)); hence \(\gamma=0\) and \(\alpha=\beta=\frac12\). Replacing
\(\|\nabla q\|_2\) by \(\|\nabla w\|_2\) or \(Y^{1/2}\) changes nothing, since
all three have the same grading. \(\square\)

**(1.2) is not derivable from the audited record.** The two classical routes to
it are
(i) Gagliardo–Nirenberg \(\|q\|_3\le(\sqrt3C_S)^{1/2}\|q\|_2^{1/2}\|\nabla q\|_2^{1/2}\)
(`lem:interp` with `lem:sobolev`), which needs \(q\in L^2\), i.e. \(w\in L^2\),
which `rem:quotient-divcurl-scope` **explicitly declines to assert** and which
no argument in the import supplies (every step there is arranged to avoid an
\(L^2\) norm of \(w\)); and even granted, it produces \(\|q\|_2\), not
\(\|u\|_2\), and no inequality \(\|q\|_2\le C\|u\|_2\) is available;
(ii) Hardy–Littlewood–Sobolev applied to \(q=\nabla(-\Delta)^{-1}\sigma\)
(legitimate in the sense of \eqref{eq:qdc-potential}), which gives
\(\|q\|_3\le C\|\sigma\|_{3/2}\) — and \(\sigma\in L^{3/2}\) is **exactly the
residual (H2)** that `rem:quotient-divcurl-scope` records as still unproved,
noting that it does not follow from \(\sigma\in L^2\) on a space of infinite
measure.
This is a statement of non-derivability from the listed record, **not** a claim
that (1.2) is false.

**Proposition 1.4 (even granting it, there is no gain).** Suppose (1.2) holds
with a constant \(C\). Then on \(\mathcal B_\delta\),
\(\|\sigma\|_2>(\delta\nu/(CC_\sharp))^2E_0^{-1/2}\), and Chebyshev against the
new budget (A9) gives
\(|\mathcal B_\delta|\le(E_0/(8\nu))\cdot(CC_\sharp)^4E_0/(\delta\nu)^4
=C^4C_\sharp^4E_0^2/(8\delta^4\nu^5)\) — the same functional form as \(\beta\),
differing only in the numerical constant. The same happens without any
hypothesis through \(\|\nabla w\|_2\): since
\(\|\nabla w\|_2\ge\|\nabla u\|_2-\|\nabla q\|_2\ge\frac12Y^{1/2}\) by (A6),
Proposition 1.1 and (A9) give
\(|\mathcal B_\delta|\le(5E_0/(8\nu))/(y_\delta/4)=5\beta\), i.e. the new budget
reproduces the audited measure bound with a constant five times **worse**.

*Reason, stated once.* Both new budgets are fixed multiples of the energy
budget: \(\int\|\nabla w\|_2^2\le\frac54\int Y\) and
\(\int\|\sigma\|_2^2\le\frac14\int Y\) pointwise in \(t\) before integration.
The import therefore supplies **no new spacetime integrability whatsoever**;
it supplies new *objects* controlled by the integrability already present.
\(\square\)

**Corollary 1.5 (the defect's spacetime hull is a single point).** For \(u\)
the audited hull is the segment spanned by \(L^\infty_tL^2_x\) and
\(L^2_tL^6_x\) (hf22-direct-attack Prop. 2.1), whose midpoint is
\(L^4_tL^3_x\). For \(w\) and \(q\) the import gives \(L^2_tL^6_x\) only
(through \(\|w\|_6\le C_S\|\nabla w\|_2\) and (A9)); the endpoint
\(L^\infty_tL^2_x\) is missing precisely because \(w\in L^2\) is not asserted.
Hence **no interpolation segment exists for the defect**, and in particular the
\(\tau\)-uniform budget \(\int_0^\tau c^4\le A_4\) used by HF21-B and HF22-C
comes from \(\|q\|_3\le2\|u\|_3\) and \(u\)'s own hull, not from the import.

---

## 2. A new upper bound for the quotient dissipation, and why it cannot close

### 2.1 The inequality

**Theorem 2.1 (dissipation upper bound; new).** Let \(m\ge4\) and let
\(u\in H^m(\R^3;\R^3)\) be solenoidal, \(w=w(u)\), \(A=|w|w\). Then
\[
 D_{\mathcal Q}(u)=\int_{\R^3}\nabla A:\nabla u\,dx
 \ \le\ 2\|w\|_6\|\nabla w\|_2\|\nabla u\|_3
 \ \le\ \tfrac52C_S\,Y\,\|\nabla u\|_3
 \ \le\ \tfrac{5\sqrt3}{2}\,C_S^{3/2}\,Y^{5/4}\,\|\Delta u\|_2^{1/2}.
 \tag{2.1}
\]

*Proof.* By `def:qe-dissipation`, \(D_{\mathcal Q}(u)=-\langle A,\Delta u\rangle\),
absolutely convergent since \(A\in L^{3/2}\) and \(\Delta u\in L^3\).

*Integration by parts.* By (A7), \(A\in W^{1,3/2}(\R^3;\R^3)\). Choose
\(A_n\in C_c^\infty(\R^3;\R^3)\) with \(A_n\to A\) in \(W^{1,3/2}\) (mollify and
cut off; \(C_c^\infty\) is dense in \(W^{1,p}(\R^3)\) for \(1\le p<\infty\)).
Since \(m\ge4\), `lem:qe-embedding` and \eqref{eq:qdc-interp} give
\(\Delta u\in L^3\) and \(\nabla u\in L^3\). For each \(n\),
\(-\int A_n\cdot\Delta u=\int\nabla A_n:\nabla u\) classically. Letting
\(n\to\infty\), the left side converges because \(A_n\to A\) in \(L^{3/2}\) and
\(\Delta u\in L^3\), the right side because \(\nabla A_n\to\nabla A\) in
\(L^{3/2}\) and \(\nabla u\in L^3\). Hence
\(D_{\mathcal Q}(u)=\int\nabla A:\nabla u\).

*Estimate.* Cauchy–Schwarz on matrices gives
\(|\nabla A:\nabla u|\le|\nabla A|_F|\nabla u|_F\), and by (A7)
\(|\nabla A|_F\le2|w||\nabla w|_F\) a.e. Hölder with exponents
\((6,2,3)\), \(\frac16+\frac12+\frac13=1\), gives the first inequality. The
second uses \(\|w\|_6\le C_S\|\nabla w\|_2\) \eqref{eq:qdc-sobolev-field} and
\(\|\nabla w\|_2^2\le\frac54Y\) (A6): \(2\cdot C_S(\frac54Y)^{1/2}(\frac54Y)^{1/2}
=\frac52C_SY\). The third is (A10). \(\square\)

*Scaling.* \(D\sim(a^3,\lambda^2)\);
\(Y\|\nabla u\|_3\sim(a^2,\lambda)(a,\lambda)=(a^3,\lambda^2)\) ✓;
\(Y^{5/4}\|\Delta u\|_2^{1/2}\sim(a^{5/2},\lambda^{5/4})(a^{1/2},\lambda^{3/4})
=(a^3,\lambda^2)\) ✓.

*Consistency check.* At \(q=0\) (so \(w=u\), \(D=D_3(u)\)) the first bound
reads \(D_3(u)\le2\|u\|_6\|\nabla u\|_2\|\nabla u\|_3\); the direct route
\(\int|u||\nabla u|^2\le\|u\|_6\|\nabla u\|_{12/5}^2\) with
\(\|\nabla u\|_{12/5}\le\|\nabla u\|_2^{1/2}\|\nabla u\|_3^{1/2}\) gives the
same product, so (2.1) is of the correct shape and is not lossy at leading
order.

*Status.* Before the import no upper bound for \(D_{\mathcal Q}\) existed in the
record at all: `def:qe-dissipation` gives only \(D\ge0\), and (A12) gives a
lower bound. Theorem 2.1 needs \(|\nabla A|_F\le2|w||\nabla w|_F\), i.e. it
needs the import; it is new here.

### 2.2 It does not sharpen the bad set either

Combining Theorem 2.1 with Proposition 1.1 on \(\mathcal B_\delta\) yields
\(\|\nabla u\|_3\ge2D/(5C_SY)\), a *lower* bound on a supercritical quantity,
which no budget consumes. Combining it with the *lower* bound (A12) gives
\(\frac{8}{9C_S^2C_9^3}\|u\|_9^3\le\frac52C_SY\|\nabla u\|_3\), a valid but
inert inequality between two quantities neither of which is input-bounded.

### 2.3 Any closing route must carry zero power of \(D\)

**Proposition 2.2 (no integrability for \(D\)).** The audited record contains
no input-only bound for \(\int_0^\tau D\,dt\) nor for
\(\int_{\mathcal B_\delta}D\,dt\), for any \(\delta\). Indeed
\(\nu\int_0^\tau D=\mathcal Q(0)-\mathcal Q(\tau)+\int_0^\tau K\), whose right
side contains the open flux; the master inequality (A11) bounds only the
deficit-weighted \(\int(\nu-c)_+D\); and the repaired family Theorem C′ of
HF22-C satisfies every listed constraint with \(\int_0^2D\,dt\to\infty\).

**Corollary 2.3.** Let a candidate route bound \(\int_{\mathcal B_\delta}|K|\)
by Hölder in time from pointwise bounds of the form
\(|K|\le(cD)^{\theta}\bigl(\frac58C_S^3Y^2\bigr)^{1-\theta}\), \(\theta\in[0,1]\)
(the geometric means of (A2) and (A8)), against the input-only budgets
\(\{|\mathcal B_\delta|\le\beta,\ \int c^4\le A_4,\ \int Y\le E_0/2\nu,\
\int\|\nabla w\|_2^2\le5E_0/8\nu,\ \int\|\sigma\|_2^2\le E_0/8\nu\}\). Then any
such route with \(\theta>0\) requires a time-integrability statement for \(D\),
which by Proposition 2.2 the record does not contain. **Hence the only
available route is \(\theta=0\)**, i.e. the pure \(Y^2\) route of §3, and
Theorem 2.1 — the one new inequality about \(D\) — cannot enter it. This is a
statement about this enumerated family of arguments, not about all arguments.

---

## 3. The \(K\)-form bad-set reduction and the enstrophy criterion

### 3.1 The reduction

**Theorem 3.1 (bad-set reduction in the \(K\)-form).** For every
\(\delta\in(0,1)\) and every \(\tau<T_*\),
\[
 \int_0^\tau K\,dt\ \le\ \frac{\delta}{1-\delta}\,\mathcal Q(u_0)
 \;+\;\frac1{1-\delta}\int_{\mathcal B_\delta}K\,dt
 \ \le\ \frac{\delta}{3(1-\delta)}\|u_0\|_3^3
 +\frac1{1-\delta}\int_{\mathcal B_\delta}K^+\,dt .
 \tag{3.1}
\]

*Proof.* Write \(I_G=\int_{\mathcal G_\delta}\), \(I_B=\int_{\mathcal B_\delta}\).
By (A1), \(\mathcal Q\in C^1\) with continuous integrands, so
\(\mathcal Q(\tau)-\mathcal Q(0)=\int_0^\tau(K-\nu D)\); since
\(\mathcal Q(\tau)\ge0\),
\[
 I_G(\nu D-K)+I_B(\nu D-K)=\int_0^\tau(\nu D-K)\le\mathcal Q(u_0).
\]
On \(\mathcal G_\delta\), \(c\le\delta\nu\), so by (A2) \(K\le cD\le\delta\nu D\)
and \(\nu D-K\ge(1-\delta)\nu D\ge0\); hence
\[
 I_GK\ \le\ \delta\nu I_GD\ \le\ \frac{\delta}{1-\delta}I_G(\nu D-K)
 \ \le\ \frac{\delta}{1-\delta}\Bigl[\mathcal Q(u_0)+I_B(K-\nu D)\Bigr].
\]
Adding \(I_BK\) and using \(D\ge0\),
\(\frac{\delta}{1-\delta}(K-\nu D)+K\le\frac{K}{1-\delta}\) on
\(\mathcal B_\delta\), which is (3.1); the last form uses (A3) and
\(K\le K^+\). \(\square\)

*Relation to the audited Theorem B.* HF22-C Theorem B reads
\(\int_0^\tau cD\le\frac{\delta}{1-\delta}\mathcal Q(u_0)
+\frac1{1-\delta}\int_{\mathcal B_\delta}cD\). Theorem 3.1 is the same argument
with \(K\) in place of \(cD\) on both sides. It is weaker on the left (it
bounds \(\int K\), not \(\int cD\)) and correspondingly **weaker on the right**,
and that is the point: the remainder is now the smaller quantity
\(\int_{\mathcal B_\delta}K\), to which the new bound (A8) applies and to which
\(cD\) does not reduce. Since `hyp:highstrain` consumes only
\(\int_0^\tau K_L\,dt\), and by the audited `rem:highstrain-normalisation` the
\(L\)-form and the full-\(K\) form are equivalent up to an input-only change of
\(A_{\rm input}\), the left side of (3.1) is all that the producer needs.

*Scaling.* Every term is \((a^3,\lambda^0)\), the scaling of \(\mathcal Q\) ✓.

### 3.2 The enstrophy form

**Theorem 3.2 (unconditional).** For every \(\delta\in(0,1)\), \(\tau<T_*\),
\[
 \int_0^\tau K\,dt\ \le\ \frac{\delta}{3(1-\delta)}\|u_0\|_3^3
 \;+\;\frac{5C_S^3}{8(1-\delta)}\int_{\mathcal B_\delta}Y^2\,dt .
 \tag{3.2}
\]
*Proof.* Theorem 3.1 and \(K\le|K|\le\frac58C_S^3Y^2\) (A8), which holds at
every \(t<T_*\) with no hypothesis on the defect. \(\square\)

*Scaling.* \(\int Y^2dt\sim(a^4,\lambda^2)(a^{-1},\lambda^{-2})=(a^3,\lambda^0)\) ✓.

**Theorem 3.3 (bad-set enstrophy criterion; conditional).** Fix
\(\delta\in(0,1)\) and \(0<H<\infty\). Suppose there is a finite
\(N=N(\nu,u_0,H,\delta)\), depending only on the input, with
\[
 \operatorname*{ess\,sup}_{t\in\mathcal B_\delta(\tau)}Y(t)\ \le\ N
 \qquad\text{for every }\tau<\min\{H,T_*\}.
 \tag{H-BY}
\]
Then \(\int_0^\tau K\,dt\le A_{\rm input}\) for all such \(\tau\), with
\[
 A_{\rm input}=\frac{\delta}{3(1-\delta)}\|u_0\|_3^3
 +\frac{5C_S^3E_0}{16\,\nu\,(1-\delta)}\,N ,
\]
so `hyp:highstrain` holds for that datum with \(\theta=0\), and by
`prop:quotient-conditional` and `thm:conditional` the branch satisfies the
conclusion of `hyp:critical` on \([0,\min\{H,T_*\})\).

*Proof.* \(\int_{\mathcal B_\delta}Y^2\le N\int_{\mathcal B_\delta}Y\le NE_0/(2\nu)\)
by (A4); insert into (3.2). \(\square\)

**Remark 3.4 (the hypothesis is strictly weaker than a Serrin bound).**
(H-BY) constrains \(Y\) only on \(\mathcal B_\delta\), a set of measure at most
\(\beta\); it says nothing on \(\mathcal G_\delta\), where the enstrophy is
permitted to be unbounded. That the conclusion is nevertheless global is not a
paradox: on \(\mathcal G_\delta\) the audited (A1)+(A2) give
\(\mathcal Q'\le-(1-\delta)\nu D\le0\), so the trajectory cannot raise its
\(L^3\) norm while it stays in the good set, and by `thm:continuation` a
blowup must therefore do its work on \(\mathcal B_\delta\). Theorem 3.3
quantifies exactly that. **It is a conditional reduction; (H-BY) is not proved
here and is not implied by anything audited** (see §4).

**Remark 3.5 (a second, non-comparable reduction).** Pairing in \(L^2\times L^2\)
as in (A8) instead of using \eqref{eq:qdc-KY} gives, by Cauchy–Schwarz in time
and (A9),
\[
 \int_{\mathcal B_\delta}|K|\,dt
 \le\Bigl(\int_{\mathcal B_\delta}\|\sigma\|_2^2\Bigr)^{1/2}
 \Bigl(\int_{\mathcal B_\delta}\|\Pi_u\|_2^2\Bigr)^{1/2}
 \le\Bigl(\frac{E_0}{8\nu}\Bigr)^{1/2}
 \Bigl(\int_{\mathcal B_\delta}\|\Pi_u\|_2^2\,dt\Bigr)^{1/2},
\]
so an input bound on the spacetime \(L^2\) norm of the mixed pressure on the
bad set also closes the gap. Using \(\|\Pi_u\|_2\le\|u\|_6\|w\|_6^2\) this is
implied by an input bound on \(\int_{\mathcal B_\delta}Y^3\), which is
*stronger* than \(\int_{\mathcal B_\delta}Y^2\); in general the two hypotheses
are not comparable, since \(\|\Pi_u\|_2\) may be far below its pointwise
majorant. Scaling ✓ (both sides \((a^3,\lambda^0)\)). Recorded, not used.

---

## 4. The deficit, computed exactly

### 4.1 In enstrophy

**Proposition 4.1 (the shortfall is one factor of the peak enstrophy).**
Unconditionally, for every \(\delta\in(0,1)\) and \(\tau<T_*\),
\[
 \int_0^\tau K\,dt\ \le\ \underbrace{\frac{\delta}{3(1-\delta)}\|u_0\|_3^3}_{\text{input}}
 +\underbrace{\frac{5C_S^3E_0}{16\nu(1-\delta)}}_{\text{input}}\cdot
 \underbrace{\operatorname*{ess\,sup}_{\mathcal B_\delta}Y}_{\text{the entire deficit}} .
\]
Every constant is input-only; the single non-input factor is the peak enstrophy
on the bad set. Equivalently, the route needs \(Y\in L^2_t(\mathcal B_\delta)\)
input-boundedly, and the record supplies \(Y\in L^1_t\) only, with
\(\int Y\le E_0/(2\nu)\).

**Proposition 4.2 (the deficit is exactly attained; a computed family).** Let
\(\delta\in(0,1)\) and let \(y_\delta,\beta\) be as in §1. Consider measurable
\(Y\ge0\) subject only to the audited constraints available on the bad set:
\(Y>y_\delta\) on \(\mathcal B_\delta\), \(|\mathcal B_\delta|\le\beta\),
\(\int_{\mathcal B_\delta}Y\le E_0/(2\nu)\). Then
\[
 \sup\Bigl\{\int_{\mathcal B_\delta}Y^2\,dt\Bigr\}=+\infty ,
\]
attained along the plateau family: for \(M>\max\{y_\delta,\ E_0/(4\nu\beta)\}\)
take \(\mathcal B_\delta\) of measure \(E_0/(4\nu M)\le\beta\) and
\(Y\equiv M\) on it. All three constraints hold —
\(M>y_\delta\), \(|\mathcal B_\delta|\le\beta\),
\(\int_{\mathcal B_\delta}Y=E_0/(4\nu)\le E_0/(2\nu)\) — and
\(\int_{\mathcal B_\delta}Y^2=ME_0/(4\nu)\to\infty\) as \(M\to\infty\). Moreover the
elementary bound \(\int_{\mathcal B_\delta}Y^2\le(\sup_{\mathcal B_\delta}Y)
\int_{\mathcal B_\delta}Y\) is an equality on this family, so the factor in
Proposition 4.1 is sharp and cannot be improved by any rearrangement of the
same two budgets. \(\square\)

**Corollary 4.3 (the measure bound is inert).** \(|\mathcal B_\delta|\le\beta\)
enters Proposition 4.2 only through the requirement \(M\ge E_0/(2\nu\beta)\),
i.e. it excludes nothing; and the lower bound \(Y>y_\delta\) is a lower bound,
so it can only *increase* \(\int Y^2\). **The reduction of (G) to the bad set
buys nothing in this accounting** — a conclusion consistent with the audited
Theorem B, which is an equivalence and therefore cannot buy anything by
itself.

### 4.2 In Ladyzhenskaya–Prodi–Serrin bookkeeping

Write \(\lambda(r,q)=\frac2r+\frac3q\); the Serrin line is \(\lambda=1\)
(\(q>3\)) and the audited input hull is the segment at \(\lambda=\frac32\)
(hf22-direct-attack Prop. 2.1, audited).

**Proposition 4.4 (the three route values).**
1. *The import adds no point to the hull.* (A9) gives \(\nabla w,\sigma\in
 L^2_tL^2_x\), hence \(w\in L^2_tL^6_x\) with \(\lambda(2,6)=\frac32\), the
 **same** point of the hull already occupied by \(u\) through the energy
 identity; by Corollary 1.5 the endpoint \((\infty,2)\) is missing for \(w\),
 so the defect contributes a single point and no segment. Deficit unchanged at
 \(\frac12\).
2. *The \(cD\) route overshoots by \(\frac16\).* On \(\mathcal B_\delta\),
 Hölder with \(s=4\) gives
 \(\int_{\mathcal B_\delta}cD\le A_4^{1/4}(\int_{\mathcal B_\delta}D^{4/3})^{3/4}\),
 and by (A12) finiteness of the last factor forces \(u\in L^4_tL^9_x\) with
 \(\lambda(4,9)=\frac56\): strictly subcritical, exactly the value
 \(1-\frac2{3s}\) at \(s=4\) computed in hf22-direct-attack (2.1).
3. *The \(K\) route lands on the line.* By Theorem 3.2 the requirement is
 \(Y\in L^2_t(\mathcal B_\delta)\), i.e. \(\nabla u\in L^4_tL^2_x\), i.e.
 (Sobolev) \(u\in L^4_tL^6_x\), with \(\lambda(4,6)=\frac12+\frac12=1\):
 **exactly critical, overshoot \(0\)**.

*Proof of the optimality claim inside 2.* For \(s\in(1,4)\),
\(\int_{\mathcal B_\delta}c^s\le|\mathcal B_\delta|^{1-s/4}A_4^{s/4}\) by Hölder,
so the bad set's finite measure does allow smaller \(s\); but then
\(s'=\frac s{s-1}>\frac43\) and the demanded space is \(L^{3s'}_tL^9_x\) with
\(\lambda=1-\frac2{3s}<\frac56\), i.e. strictly worse. Hence \(s=4\) is optimal
and the measure bound only trades a constant for a worse exponent. \(\square\)

**Consequence.** The exact contribution of the newly proved regularity to the
gap is: *the overshoot past the Serrin line is removed* (\(\frac16\to0\)),
while *the deficit below it is unchanged* (\(\frac12\)). Both statements are
insensitive to the restriction to \(\mathcal B_\delta\). Two honest riders:
(i) a route that demands exactly \(\lambda=1\) is exactly as strong as an LPS
criterion, so Theorem 3.3 cannot be *easier* than a Serrin bound in general —
its only advantage is that it needs the bound on a set of input-bounded
measure only (Remark 3.4);
(ii) an input-only modulus of continuity for \(t\mapsto\|q(t)\|_3\) (the object
lane HF24-A attacks, **not assumed anywhere here**) would upgrade the measure
bound \(\beta\) to a crossing-*count* bound; by Corollary 4.3 that would still
leave the factor \(\sup_{\mathcal B_\delta}Y\) untouched, so it does not by
itself close the bad-set restriction. If it is wanted here it must be stated as
an explicit extra hypothesis; this note states none.

---

## 5. The audited obstruction family, confronted with the new facts

The lane brief asks whether the good-set obstruction family also obstructs the
bad-set route, and whether the new regularity voids it.

**Observation 5.1.** Theorem C′ of HF22-C obstructs the bad-set restriction
verbatim: its item 7 records that
\(\int_{\mathcal B_\delta}(c-\nu)D\,dt=n\mathcal Q_0\to\infty\) "carries the
entire excess", and on its bad phases \(c\equiv2\), \(D\equiv\mathcal Q_0/\ell\),
so \(\int_{\mathcal B_\delta}cD\,dt=2n\mathcal Q_0\to\infty\) while
\(|\mathcal B_\delta|=1/n\to0\). Since HF22-C Theorem B is an equivalence, this
was to be expected; it is recorded because it is the exact statement the
present lane's target needs.

The substantive question is whether the family survives the constraints the
import adds. Augment (T1)–(T9) of HF22-C by everything this note has
established, all of which is now available along the classical branch:

- **(T10)** \(|K|\le\frac58C_S^3Y^2\) — (A8), `lem:quotient-mixed-pressure`;
- **(T11)** \(\int_0^\tau Y\,dt\le E_0/(2\nu)\) — (A4);
- **(T12)** \(c\le2C_\sharp(3C_S^2E_0)^{1/4}Y^{1/4}\) — (A3)+(A5);
- **(T13)** \(D\le c_1Y^{5/4}\|\Delta u\|_2^{1/2}\),
 \(c_1=\frac{5\sqrt3}2C_S^{3/2}\) — Theorem 2.1 with (A10);
- **(T14)** \(\frac12Y'+\frac\nu2\|\Delta u\|_2^2\le C_E\nu^{-3}Y^3\),
 \(C_E=\frac{2187}{32}C_S^6\) — `prop:enstrophy`; integrated,
 \(\nu\int_0^\tau\|\Delta u\|_2^2\le Y(0)+2C_E\nu^{-3}\int_0^\tau Y^3\);
- **(T15)** \(\mathcal Q\le3^{-1/4}C_S^{3/2}E_0^{3/4}Y^{3/4}\) — (A3)+(A5).

**Theorem 5.2 (the family survives the enriched list).** The family of
Theorem C′ (\(\nu=1\), \(\tau=2\), \(\ell=n^{-2}\), \(2n\) phases on
\((0,2/n)\), \(D\equiv\mathcal Q_0n^2\) on the phases, \(c\equiv2\) and
\(K=cD\) on the bad phases, \(c=K=0\) on the good phases, tail
\(D\equiv D_\flat\)) extends to a tuple
\((\mathcal Q,c,D,K,Y,\|\Delta u\|_2)\) satisfying (T1)–(T15) with
\(\int_{\mathcal B_\delta}cD=2n\mathcal Q_0\to\infty\) and
\(|\mathcal B_\delta|=1/n\to0\). Consequently **the bad-set restriction of (G)
is not derivable from (T1)–(T15) either.**

*Construction and verification.* Keep every assignment of Theorem C′ and add
\[
 Y:=y_1n\ \text{ on the }2n\text{ phases},\qquad
 y_1:=\Bigl(\frac{16\mathcal Q_0}{5C_S^3}\Bigr)^{1/2},
 \qquad Y:=y_0\ \text{ on the tail},
\]
with \(y_0\) any constant satisfying (T15) for \(\mathcal Q\le3\mathcal Q_0\),
and \(\|\Delta u\|_2^2:=Z\) chosen at the minimum permitted by (T13),
\(Z=(D/(c_1Y^{5/4}))^4\).

- (T10): on the bad phases \(K=2\mathcal Q_0n^2\) and
 \(\frac58C_S^3Y^2=\frac58C_S^3y_1^2n^2=2\mathcal Q_0n^2\) by the choice of
 \(y_1\) ✓ (equality); elsewhere \(K=0\) ✓.
- (T11): \(\int_0^2Y=\frac2n\cdot y_1n+O(1)=2y_1+O(1)\), **independent of
 \(n\)**; the family already requires \(E_0\) arbitrarily large (to make
 \(\gamma\) small in (T8)), so \(2y_1+O(1)\le E_0/2\) holds ✓.
- (T12): \(c\le2\) and \(Y\to\infty\) on the bad phases ✓; \(c=0\) elsewhere ✓.
- (T13): equality by construction ✓.
- (T14): the required
 \(\int Z=\frac2n\cdot\frac{\mathcal Q_0^4n^8}{c_1^4y_1^5n^5}
 =\frac{2\mathcal Q_0^4}{c_1^4y_1^5}n^2\) must not exceed
 \(Y(0)+2C_E\int Y^3=Y(0)+2C_E\cdot\frac2n y_1^3n^3=Y(0)+4C_Ey_1^3n^2\).
 Both sides are \(\Theta(n^2)\), so the condition is the **\(n\)-independent**
 numerical inequality \(\mathcal Q_0^4\le2C_Ec_1^4y_1^8\). With
 \(c_1^4=(75/4)^2C_S^6\), \(C_E=\frac{2187}{32}C_S^6\) and
 \(y_1^8=(16\mathcal Q_0/(5C_S^3))^4\), the right side equals
 \(2\cdot\frac{2187}{32}\cdot\frac{5625}{16}\cdot\frac{65536}{625}\,
 \mathcal Q_0^4\approx5.0\times10^6\,\mathcal Q_0^4\), so the inequality holds
 with a slack factor \(\approx5\times10^6\) ✓. The rate condition on the
 smoothing ramps of C′ is \(Y'\le2C_EY^3-\nu Z\), i.e.
 \(\tfrac12y_1n^3\le(2C_Ey_1^3-\mathcal Q_0^4/(c_1^4y_1^5))n^3\), which reduces
 to \(\tfrac14\le C_Ey_1^2\) after the previous line; if the numerical value
 of \(C_S\) made this fail, the phase value \(y_1\) may simply be raised, which
 the energy budget permits (\(E_0\) is free in C\('\)), leaves (T10) slack
 rather than tight, and lowers the \(Z\) demanded by (T13) ✓.
- (T15): the tail value \(y_0\) is a fixed constant, and on the phases
 \(Y\to\infty\) makes (T15) slack ✓.
- (T1)–(T9): unchanged from C′, whose repaired verification the audit checked.

*Scaling.* Every constraint used is scaling-consistent (§0 table and the checks
in §§1–3); the family is stated at \(\nu=1\) and transported by
`lem:quotient-scaling`, as C′ is. \(\square\)

**Corollary 5.3 (what the import does cost the family).** The family is not
voided, but it is pinned: (T10) forces its bad-phase enstrophy to grow at least
like \(y_1n\), so its energy budget occupancy \(\int_{\mathcal B_\delta}Y\)
equals a fixed positive fraction \(2y_1\) of \(E_0/(2\nu)\), independent of
\(n\), and (T13)+(T14) force a spike in \(\|\Delta u\|_2^2\) of size
\(\Theta(n^3)\) per phase. The family therefore survives only by placing the
whole of its excess in the one direction the record does not measure: the
\(L^2_t\) norm of \(Y\), i.e. exactly the deficit of Proposition 4.1. This is a
consistency check on §4 by an independent route.

**Warning, in the audits' own terms.** Theorem 5.2 is **non-derivability from
an enumerated list**, not falsity of the bad-set restriction; the list is not
claimed exhaustive; and the family is a tuple of real functions on \((0,2)\),
**not** a Navier–Stokes solution, and is never claimed to be one (HF22-C
Theorem D: realization on a trajectory is equivalent to finite-time blowup of
that trajectory).

---

## 6. Scaling table

| Quantity | \((a,\lambda)\) grading | Checked in |
|---|---|---|
| \(\mathcal Q,\ \int K\,dt,\ \int(\nu-c)_+D\,dt\) | \((a^3,\lambda^0)\) | §3.1, §3.2 |
| \(y_\delta=\delta^4\nu^4/(48C_S^2C_\sharp^4E_0)\) vs \(Y\) | \((a^2,\lambda^1)\) | Prop. 1.1 |
| \(\beta=24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}\) vs \(|\mathcal B_\delta|\) | \((a^{-1},\lambda^{-2})\) | Cor. 1.2 |
| \(\|q\|_3\) vs \(\|\nabla q\|_2^{1/2}\|u\|_2^{1/2}\) | \((a,\lambda^0)\) | Prop. 1.3 |
| \(D\) vs \(Y\|\nabla u\|_3\) vs \(Y^{5/4}\|\Delta u\|_2^{1/2}\) | \((a^3,\lambda^2)\) | Thm. 2.1 |
| \(\int Y^2dt\) vs \(\mathcal Q\) | \((a^3,\lambda^0)\) | Thm. 3.2 |
| \(E_0\sup Y/\nu\) vs \(\mathcal Q\) | \((a^3,\lambda^0)\) | Prop. 4.1 |
| \((E_0/\nu)^{1/2}(\int\|\Pi_u\|_2^2)^{1/2}\) vs \(\mathcal Q\) | \((a^3,\lambda^0)\) | Rem. 3.5 |

Every inequality displayed in this note is scaling-exact in both gradings; none
is a mismatched interpolation.

---

## 7. Scope, non-claims, open questions

**SCOPE.** Theorem 2.1 and Theorems 3.1–3.3 are proved here from audited
inputs only. Theorem 2.1 uses the import (A6)–(A7) and holds for every
solenoidal \(u\in H^m\), \(m\ge4\); the restriction to \(m\ge4\) is used only
for \(\Delta u,\nabla u\in L^3\) and the integration by parts, exactly as
`lem:quotient-mixed-pressure` does. Theorems 3.1–3.3 are statements about the
classical branch on \([0,T_*)\), uniform in \(\tau\), with no horizon \(H\)
except where `hyp:highstrain` is invoked. No smallness is used anywhere. No
derivative of \(\|q\|_3\) is taken, no evolution for \(\|q\|_3\) is written, and
the merely-\(L^3\) minimizer is never differentiated: the only derivatives of
\(w\) used are the distributional ones supplied by the audited
`prop:quotient-divcurl`.

**NON-CLAIMS.** No proof of (G), of its bad-set restriction, of
`hyp:highstrain`, `hyp:highpressure`, `hyp:absorption`, `hyp:critical` or
NS-R3. **No claim that the bad-set restriction is false**: §5 refutes
derivability from (T1)–(T15), not the statement, and by HF22-C Theorem B the
bad-set restriction is *equivalent* to (G), so it cannot be false unless (G) is.
No claim that (1.2) is false — only that it is not derivable from the record
and that granting it changes nothing (Prop. 1.4). No bound on \(\sup_tY\),
\(\sup_t\mathcal Q\), \(\sup_t\|u\|_3\), \(\int D\,dt\), \(\int D^{4/3}dt\),
\(\int Y^2dt\) or \(\int\|\Delta u\|_2^2dt\) is claimed or used; (H-BY) of
Theorem 3.3 is a hypothesis, not a result. No modulus of continuity for
\(\|q\|_3\) and no crossing-count bound is assumed (lane HF24-A owns that
question); the one place it could enter is flagged in Prop. 4.4(ii), where it is
shown not to close the restriction by itself. No use of \(w\in L^2\) or
\(\sigma\in L^{3/2}\), both of which the import leaves open. No comparison
between \(D_3(u)\) and \(D_3(w)\) is used (`rem:distance-balance`, and HF22-A's
audited negative answer to sub-question (a)). No forced, periodic,
hyperdissipative or Euler substitute appears. No novelty or priority is
claimed for anything; Theorem 3.1 is the audited HF22-C Theorem B argument with
one substitution, and Theorem 3.2's ingredient \eqref{eq:qdc-KY} is a
manuscript lemma whose \(\int Y^2\) consequence `rem:quotient-divcurl-scope`
already records. Nothing is promoted and no manuscript or graph file is
touched.

**NEXT DISTINCT ACTION.** Decide (H-BY): is the enstrophy input-bounded on the
set of times at which the trajectory is far from the nonlinear-Hodge class?
This is a strictly weaker question than a Serrin bound (Remark 3.4), it is the
exact residue of the whole gap after the import (Prop. 4.1), and it is a
question about the *interaction* of the distance and the enstrophy, which no
lane has yet posed: HF21-B and HF22-C measured the bad set, HF24-A measures its
crossings, and neither constrains the height of \(Y\) on it.

## Open Questions

- needs review: whether \(\|q\|_3\le C\|\nabla q\|_2^{1/2}\|u\|_2^{1/2}\)
 (1.2) is true, false, or independent; it is the unique scaling-admissible
 monomial (Prop. 1.3) and would follow from either \(w\in L^2\) with
 \(\|q\|_2\lesssim\|u\|_2\) or from \(\sigma\in L^{3/2}\), both open. Prop. 1.4
 shows it is inert for the measure bound, but it is not known to be inert
 elsewhere.
- needs review: whether \(\operatorname*{ess\,sup}_{\mathcal B_\delta}Y\) admits
 an input-only bound (H-BY), or whether an explicit family refutes its
 derivability from (T1)–(T15) as Theorem 5.2 does for the restriction itself.
- needs review: whether the mixed-pressure reduction of Remark 3.5 —
 \(\int_{\mathcal B_\delta}\|\Pi_u\|_2^2dt\) input-bounded — is strictly weaker
 than (H-BY) on the classical branch, since \(\|\Pi_u\|_2\) may be far below
 \(\|u\|_6\|w\|_6^2\).
- needs review: whether Theorem 2.1 admits a form with \(\|\nabla u\|_2\) in
 place of \(\|\nabla u\|_3\) at the cost of a weight, which would put \(D\)
 inside the energy budget and void Corollary 2.3; the Hölder triple
 \((6,2,3)\) is forced by the exponents of \(|w|\), \(\nabla w\), \(\nabla u\)
 as they stand.
- needs review: whether Theorem 3.1 can be iterated over the connected
 components of \(\mathcal B_\delta\) (open by continuity of \(\|q\|_3\)) to
 replace \(\sup_{\mathcal B_\delta}Y\) by a per-component average; this is the
 only place where a crossing-count bound from lane HF24-A would enter.
