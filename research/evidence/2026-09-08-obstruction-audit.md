# Independent audit: support rigidity, separated-label no-start, angular preparation

Date: 2026-09-08. Frozen input commit: `373bd3e0504df775434ad579607ded9481af624f`
(working tree clean at audit start; the three audited notes declare frozen input
`fedb45a640ea8537aa90578f2cafda9adca01756`).
Status: INDEPENDENT AUDIT. Fresh context; the auditor did not write the audited
notes and treated every claim as unproved until checked line by line.
Model tier: Opus 5 (1M context), deliberately distinct from the author lanes.
No promotion: no canonical graph node, no PLAN status change, no manuscript,
no formal file, no terminal claim. This note edits nothing else in the tree.

Audited files:

* (A) `research/evidence/2026-09-08-unforced-support-and-pulse-audit.md`
* (B) `research/evidence/2026-09-08-autonomous-pulse-obstruction.md`
* (C) `research/evidence/2026-09-08-angular-preparation-obstruction.md`

Primary source [OA]: OpenAI, *Finite Time Blowup for Navier--Stokes*, 165 pp.
A local copy was available to this audit in the session scratchpad and was read
through `helpy_pdf` only (pp. 1--2, 14--16, 63--66, 73--78, 80--81, 86--87).
No PDF is added to the repository and no binary hash is claimed.

## 0. Source-fidelity gate (upgrade relative to note A section 0)

Note A section 0 records that "the CDN binary could not be retrieved into the
local container". This audit did read a local copy and checked every equation
the three notes attribute to [OA]. All of them are quoted correctly:

* [OA, Thm 1.1, p.1]: `f in Cc^inf(R3 x (0,inf))`, compact `K`, smooth `u,p` on
  `R3 x [0,1)`, `u(.,0)=0`, `supp u(.,t) u supp p(.,t) subset K for every
  0<=t<1`, `sup ||u(t)||_L2 < inf`, `limsup_{t->1} ||u(t)||_Linf = inf`.
  This is EXACTLY the hypothesis class of note A Corollary 3.
* [OA, Thm 3.1(iii),(3.5), pp.14--16]: residual flat, not zero; and for
  `X >= X_ext` the residual is IDENTICALLY zero with `A=0`, `B=K(r,tau)`,
  `p = -int_r^inf K(rho,tau)^2/rho drho`. The exterior field is exactly
  `K(r,tau) e_theta`: z-independent on an open set. Note A Theorem 2(b)
  applies verbatim.
* [OA, (6.13), Lemma 6.1, p.65--66]: separation of enlarged rectangles, "with
  supports taken in (r,z,t,Y) uniformly in theta", and explicitly "including
  the separation needed for supports of derivatives". Note B's "uniform in
  theta" and "including derivative supports" are faithful.
* [OA, (6.16), p.66]: `psi(v)=1 if |v-Ls/2|<=Ls/5`, `supp psi subset
  {|v-Ls/2|<Ls/3}`. This is note B Theorem 2's cutoff verbatim and satisfies
  note A Proposition 6's extra hypothesis with `c_2=1/5`.
* [OA, (7.2), p.74]: `Bs^2 = lambda_0/(eps k^2 (1+u_*^2)^{3/2})`. Note C (4.4)
  `k^2 Bs^2 = lambda_0/(eps (1+u_*^2)^{3/2})` is an exact consequence.
  Note C's "independent of k" is correct.
* [OA, (7.16), p.78]: `exp(-C(v-Ls/2)^2/Ls) <= P(v) <= exp(-c(v-Ls/2)^2/Ls)`.
* [OA, (7.17), p.78]: `z_m' = A_m z_m + g_m`, `A_m = diag(lambda,-lambda) + E
  - m^2 d I_2`, `|E| <= C/S_*`, `lambda = lambda_0/sqrt(1+s^2)`. This is
  literally the frame equation of note C Lemma 6.
* [OA, Lemma 7.4, pp.80--81]: `z_+(0)=P(0)`, `z_-(0)=0`, `cP<=x<=CP`, every
  fixed derivative bounded by `C_I S_*^{b_I} P(v)`. This is exactly hypothesis
  (2.1) of note A Theorem 4 and (5) of note B Theorem 2.
* [OA, (7.40), p.86]: the cutoff residual is `(1-psi) f_m + psi' t_m`.
* [OA, p.87]: [OA] itself performs the same flatness computation,
  `q^{-N} Q^{-M} S_*^C e^{-c S_*} <= C_N exp(-c ell^2 + (M+N) ell log 2
  + 2C log ell) -> 0`, and states these "remain separate additive flat
  residuals". Note A/B's assertion that [OA] retains and does not cancel them
  is confirmed at the source.

Verdict on source fidelity: CONFIRMED. No misquotation was found. The
scope disclaimers ("not an independent validation of the 165-page proof")
remain appropriate; this audit did not check [OA]'s proofs.

## 1. Checker execution and exact scope

Observed on the frozen tree, `python3 <file>`:

* `research/check_unforced_preparation.py` -> `"status": "passed"`, exit 0,
  **218 assertions**, 18 rational history cases. Groups: `vector_angular` 77,
  `rational_history_cases` 54, `rotation_leray` 28, `mixed_inverse` 20,
  `pulse_trace` 14, `frame_growth` 9, `history_integral` 4,
  `principal_pressure` 4, `whole_nonlinearity` 4, `phase_geometry` 2,
  `pulse_scale` 2.
* `research/check_autonomous_pulse_obstruction.py` -> `"status": "PASS"`,
  exit 0, **86 exact assertions**. Groups: `angular` 33, `gauges` 18,
  `flatness` 16, `envelope` 8, `energy` 3, `full_nonlinearity` 3,
  `cutoff` 2, `transport` 2, `pressure` 1.

What they DO test (verified by reading both files):
the transverse angular quadratic form and its eigenvalues `(n-1)^2, (n+1)^2,
n^2` including the falsity of an `n^2` vector bound at `n=1`; Leray-projector
rotation equivariance for one rational rotation and three sample wavevectors;
the exact matrix product rule `(d_v - A)(psi h) = psi' h`; both trace choices
(`-psi h` and `(1-psi)h`) and their exact consequences; the Gaussian envelope
exponent at offsets 1/5, 1/4, 1/3; the flatness comparison `-c ell^2 +
(M+N+b) ell <= -c ell^2/2` for rational witnesses; the strain antiderivative
`-d/dtau[(C_B/h)(tau^-h - tau0^-h)] = C_B tau^{-1-h}`; the (7.2)-derived
identity `k^2 Bs^2 = lambda_0/(eps (1+u_*^2)^{3/2})`; the Lemma 6 cone bounds
`-3+4q+4q^2 < 0` and `3/4-q-2q^2 >= 1/2` at `q<=1/8`; nonzero nullspaces of
`d x (d+1)` Vandermonde matrices for the finite-gauge remark; and the
Cartesian-symbolic energy identities (transport divergence cancellation,
pressure pairing as a divergence, only-symmetric-strain, nine-term nonlinear
expansion).

What they do NOT test:
**nothing whatever in note A Section 1.** There is no assertion group bearing on
Lemma 1 (Gevrey/mild contraction, heat-multiplier bound, Cauchy--Schwarz tube
extension), on the identity theorem, on the rotation generator
`D_rot u = (Jx.grad)u - Ju`, or on the Fubini step in Theorem 2(b). The
load-bearing analytic core of note A is entirely uncertified by either checker.
Also untested: every function-space hypothesis; the `epsilon -> 0` regularizing
limit and the dominated/monotone convergence steps in note C Theorem 1; forward
uniqueness; Gronwall; the infinite-label sum; the whole-space Leray projector
beyond three sample frequencies; and any statement of [OA] (the (4.4) check
assumes the formula rather than verifying the source).

Three assertions are tautologies that test nothing, and should not be counted:

* `check_unforced_preparation.py`, `pulse_trace: "zero trace removes the
  carrier"` -- `equal(pulse-pulse, 0)` is `x-x=0`.
* same file, `history_integral: "required signed nonlinear work
  rearrangement"` -- both sides are the same sum reordered.
* same file, `history_integral: "necessary frequency ceiling"` -- with
  `dose = nu*freq/radius**2` the assertion is
  `(dose*eta*log)*radius^2/(nu*eta*log) == freq`, i.e. cancellation of the
  definition. It does not check any ceiling.
  Additionally the five `pulse_trace` assertions
  `diff(operator(fill)+residual, v, j) == 0` differentiate an expression that
  is already identically zero, so only `j=0` carries content.

Net: the honest count is ~213 non-vacuous assertions in checker 1 and 86 in
checker 2, all finite symbolic algebra, none of it a continuum certificate.
Both scope strings in the files are accurate and should be retained.

## 2. Note A, Section 1

### 2.1 Lemma 1 (spatial analyticity)

Hypotheses as I read them: `nu>0` fixed; `u` a real divergence-free classical
finite-energy whole-space NS solution on `(a,b)`, in `C_t H^s` on compact
subintervals for every `s`, with the canonical unforced pressure. Conclusion:
`u(t,.)` is real analytic on `R3` for every `a<t<b`.

Step check.

* (1.1) `||e^{alpha Lambda}(fg)||_Hs <= C_s ||e^{alpha Lambda}f||_Hs
  ||e^{alpha Lambda}g||_Hs`, `s>3/2`, constant independent of `alpha`.
  Correct: `e^{alpha|xi|} <= e^{alpha|eta|} e^{alpha|xi-eta|}` by the triangle
  inequality, then the stated `<xi>^s <= C_s(<eta>^s + <xi-eta>^s)` splitting
  with Young and `<xi>^{-2s} in L1` for `s>3/2`.
* "The linear heat term is bounded by `exp(lambda^2/4)||u(c)||_Hs`."
  Correct: `sup_xi [lambda sqrt(nu r)|xi| - nu r |xi|^2] = lambda^2/4`,
  attained at `|xi| = lambda/(2 sqrt(nu r))`.
* "`sqrt(r)-sqrt(s) <= sqrt(r-s)`" and the resulting multiplier bound
  `C_lambda/sqrt(nu(r-s))`. Correct: with `sigma = nu(r-s)`,
  `sup_xi |xi| exp(lambda sqrt(sigma)|xi| - sigma |xi|^2)
  = sigma^{-1/2} sup_y y e^{lambda y - y^2}`. All factors are Fourier
  multipliers and commute, so the order of composition used is legitimate.
* (1.2): `int_0^r C/sqrt(nu(r-s)) ds = 2 sqrt(r/nu) <= C sqrt(d/nu)`. Correct.
  Contraction in the ball of radius `2 exp(lambda^2/4)||u(c)||_Hs` needs
  `d <~ nu/||u(c)||_Hs^2`, which is uniform for `c` in a compact regular
  interval. Correct.
* Tube extension: `e^{lambda sqrt(nu d) Lambda} \hat u in L2` gives
  `int |\hat u| e^{a|xi|} dxi < inf` for `a < lambda sqrt(nu d)` by
  Cauchy--Schwarz against `<xi>^{-s} e^{(a-lambda')|xi|}`. Correct.

Failure modes checked and cleared. The analyticity radius is
`~ lambda nu / ||u(c)||_{H^s}` and DOES degenerate as `t` rises to a singular
endpoint. This is harmless here: the lemma is only ever used at a fixed
interior time, and no uniformity in `t` is asserted or consumed downstream.
No limit at `t -> T` is interchanged. No published theorem is imported: the
proof is self-contained and the Giga citation is correctly labelled as
historical context, not as the operative hypothesis.

**Verdict: CONFIRMED WITH REPAIR.** The repair is editorial and small: state
`s>3/2` in the hypothesis line rather than only inside the proof, and state
the uniqueness class used at "Local uniqueness identifies it with the given
classical solution" (uniqueness in `C_t H^s`, `s>3/2`, or LPS). As written a
reader must supply both.

### 2.2 Theorem 2 (a), (b), (c)

(a) `u=0` on a nonempty open set at a positive time in an unforced classical
interval implies `u(t,.)=0`. Correct: components analytic by Lemma 1, `R3`
connected, identity theorem.

(b) `partial_z u = 0` on a nonempty open set implies `u(t,.)=0`. Correct:
`partial_z u` is analytic, so `partial_z u = 0` globally; a z-independent
`L2(R3)` field is zero by Fubini. The finite-energy hypothesis is genuinely
used here and is available.

(c) `D_rot u = (Jx.grad)u - Ju` with `Jx=(-x2,x1,0)`. Differentiating
`u(R_theta x) = R_theta u(x)` at `theta=0` gives exactly `D_rot u = 0`, and
`D_rot u` has analytic components. Vanishing on an open set gives vanishing
everywhere; integrating the resulting linear first-order identity along
rotation orbits returns global equivariance. Correct.

One objection. The premise of (c) is stated as "`u` is axisymmetric on a
nonempty spatial open set". An arbitrary open set is NOT rotation-invariant, so
"axisymmetric on `V`" is not literally meaningful without a convention.

**Verdict (a): CONFIRMED. (b): CONFIRMED. (c): CONFIRMED WITH REPAIR.** The
repair: replace the premise of (c) by "`D_rot u` vanishes on a nonempty open
set", which is what the proof uses, and note that this is implied by
`u(R_theta x) = R_theta u(x)` for `x` and `R_theta x` both in the set for
small `theta`. With that convention the proof is exactly right, and the
application to [OA]'s exactly axisymmetric core is unaffected.

### 2.3 Corollary 3 (no unforced terminal slab)

Hypotheses: `U` smooth, divergence-free, spatially compactly supported in a
FIXED compact set, on `[0,T)`, with `limsup_{t->T} ||U(t)||_inf = inf`.
`F_U = partial_t U - nu Delta U + P div(U tensor U)`. Conclusion: for every
`t_* < T`, `F_U` is not identically zero on `(t_*,T) x R3`.

Proof check. `F_U = 0` on the slab gives, with `p = R_i R_j (U_i U_j)`,
`(I-P) div(U tensor U) = grad p`, hence `partial_t U - nu Delta U +
(U.grad)U + grad p = 0` with the canonical pressure. `U` smooth with support
in a fixed compact `K` is in `C_t H^s` for every `s` on compact subintervals
of `(t_*,T)`. Lemma 1 gives analyticity at each such time; Theorem 2(a)
(compact support contains an open null set) gives `U(t,.)=0` for every
`t in (t_*,T)`, contradicting the blowup limsup. Correct.

Two remarks the note does not make and which matter for the PLAN.

1. The corollary is STRONGER than its own headline. Nothing in the proof uses
   that the interval is terminal. The same argument shows `F_U` cannot vanish
   identically on ANY nonempty open time interval. Hence for a compactly
   supported blowing-up `U` there is no unforced sub-interval at all, and in
   particular there is no unforced exactification on `[t_0,T)` that keeps
   `supp U(.,t)` inside a fixed compact set. Note A only states the weaker
   terminal form, and PLAN Section 4 (UE0) only asks about a terminal slab.
2. The identification `F_U = P f` is correct and the note's remark that this
   defeats a change of trial pressure or removal of a gradient part of `f` is
   correct. Combined with [OA, Thm 1.1] as read above (`supp u(.,t) subset K`
   for every `t<1`, `limsup ||u(t)||_inf = inf`), the hypothesis class contains
   [OA]'s candidate exactly. So yes: the ACTUAL global `P f` of [OA]'s
   construction is excluded from vanishing on a terminal slab, and this is
   not a statement about one particular conversion.

**Verdict: CONFIRMED, and the stated conclusion is weaker than what the proof
delivers.** The repair (a strengthening, not a fix) is to state it for an
arbitrary open time interval. Recorded as a non-blocking adjacent improvement;
this audit does not edit note A.

## 3. Note A, Section 2 (Theorem 4, Corollary 5, Proposition 6)

Hypotheses: `Q=2^{-ell}`, `S=ell^2`, `c_L S <= L <= C_L S`; a smooth matrix
`C_Q` on `[0,L]`; a homogeneous `h_Q' = C_Q h_Q` with `|h_Q(L/2)| >= c_0` and
`|d_v^j h_Q| <= C_j S^{b_j} exp(-c(v-L/2)^2/L)`; a cutoff `psi` equal to one
near the midpoint, zero near both endpoints, derivative support in
`|v-L/2| >= c_1 L`, derivatives bounded by fixed powers of `S`.

Theorem 4. `a_Q = psi h_Q`, `r_Q = (d_v - C_Q) a_Q = psi' h_Q`: exact product
rule, correct. `a_Q(0)=0`, `||a_Q||_inf >= |h_Q(L/2)| >= c_0`, and on
`supp psi'` the Gaussian gives `exp(-c c_1^2 L) = exp(-c' S)`, so (2.3) holds
by Leibniz. The `log` computation `N ell log 2 + 2b log ell - c' ell^2 ->
-inf` is correct. Causal uniqueness identifies the zero-data response of
`r_Q` as exactly `a_Q`, so the operator norm on this family is at least
`c exp(c' S)/S^b`. All correct.

Corollary 5. Uniqueness for `(d_v - C_Q) w = -r_Q`, `w(0)=0`, gives `w=-a_Q`
and `a_Q+w=0`. Correct and trivial.

Proposition 6. `w_Q=(1-psi)h_Q` gives `(d_v-C_Q)w_Q = -psi' h_Q = -r_Q`,
`a_Q+w_Q=h_Q`, `w_Q(0)=h_Q(0)`, and flatness because `1-psi` is supported in
`|v-L/2| >= c_2 L`. (2.7) is the standard variation-of-constants
parametrization. All correct.

Applicability to [OA]: hypothesis (2.1) is [OA, Lemma 7.4] plus (7.16)
verbatim (see Section 0 above); `C_Q = A_Phi - d I` at `m=1` is [OA, (7.17)]
with `m=1`; the cutoff is [OA, (6.16)]. The identification is faithful.

**Objection, and it is the substantive one.** Theorem 4's "superalgebraic
inverse cost" is an artifact of measuring the source in an UNWEIGHTED norm.
[OA, Prop 7.2, (7.14)] bounds `|D^I t_m| <= C S_*^{b'} sqrt(zeta)^{...} P(v)`
GIVEN `|D^I f_m| <= C S_*^{b} sqrt(zeta)^{...} P(v)`: source and response are
weighted by the same envelope `P`. For the seed, `h_Q ~ P` by [OA, (7.21)]
(`cP <= x <= CP`) and `psi' ~ 1/L_s`, so `g/P = psi' h_Q / P ~ 1/L_s ~
S_*^{-1}`. That is not flat; it is `S_*^{-1}`. Feeding it through (7.14)
predicts a response of size `S_*^{b} P(v)`, and the exact response `psi h_Q`
has size `~ P` -- i.e. the exact answer SATURATES [OA]'s weighted bound to
within the allowed polynomial factor. There is no loss and no anomaly.

Note A Corollary 5 and note B Section 3 both say this ("in a norm that divides
by the Gaussian envelope, `psi' h_Q/P` is NOT a flat input"), so no error is
being asserted. But the consequence should be stated plainly and is not: this
pair of theorems is a norm-bookkeeping caution, not an obstruction. Every
unstable linear ODE has an exponentially large causal inverse in unweighted
norms; nothing here is specific to the pulse. Proposition 6, in the same note,
then exhibits an exactly flat repair with a free trace -- confirming that the
"cost" evaporates as soon as either the norm or the trace is chosen naturally.

**Verdicts. Theorem 4: CONFIRMED (exact, and non-obstructive in the sense just
stated). Corollary 5: CONFIRMED. Proposition 6: CONFIRMED.** The
amplitude-ODE/PDE boundary is drawn correctly and repeatedly in note A; I
found no place where an amplitude statement is silently used as a PDE
statement. Section 3's summary sentence ("Theorem 4 and Corollary 5 exclude
treating it as a small zero-trace causal correction merely because it is
flat") is accurate and appropriately narrow.

## 4. Note B

### 4.1 Theorem 1 (exact label energy identity)

Hypotheses: classical finite-energy `(U,p,f)` on `[s,t_*]`, `nu>0`;
`U = B + sum_gamma W_gamma` with `M B = B`, `M W_gamma = 0`, all pieces
divergence-free; `C_t H^m` cap `C^1_t H^{m-2}`, `m>=4`, `f in C_t L2`,
`grad p` in the corresponding class; pairwise separated closed spacetime
supports including derivative supports. Conclusion (2), and: if `P f = 0`
and `W_gamma(s)=0` then `W_gamma == 0`.

Every step of (2) checks.

* `M` is a self-adjoint orthogonal projection commuting with `d_t`, `Delta`
  and `P`, so `<d_t B, W_gamma> = <d_t B, M W_gamma> = 0` and likewise for
  `Delta B`. Correct.
* `(B.grad)B` is axisymmetric because `T_alpha[(v.grad)w] = (T_alpha v .grad)
  (T_alpha w)`, so `M[(B.grad)B] = (B.grad)B` and the pairing vanishes.
  Correct.
* Cross labels: `d_t W_{gamma'}`, `Delta W_{gamma'}`, `(B.grad)W_{gamma'}`,
  `(W_{gamma'}.grad)B` are all supported in `supp W_{gamma'}`, and
  `(W_{gamma'}.grad)W_{gamma''}` is nonzero only for `gamma'=gamma''`. All
  pairings with `W_gamma` vanish. Correct, and the note is right to flag
  explicitly that this includes `d_t W_{gamma'}` (no packet substitution).
* `(B.grad)W_gamma` and `(W_gamma.grad)W_gamma` pair to zero by divergence
  cancellation; `(W_gamma.grad)B` gives exactly `int W_gamma . S(B) W_gamma`
  (antisymmetric part drops for a real field). Correct.
* Pressure: `grad p` with `grad p in L2` is orthogonal to the solenoidal
  subspace of `L2(R3)` by the Helmholtz decomposition. The test field IS
  divergence-free and IS in `L2`. No pressure term is dropped illegitimately.
  Correct.
* `<f,W_gamma> = <P f,W_gamma>`. Correct.
* Gronwall: `E' <= 2 b E` with `b = ||S(B)||_inf` integrable on compact
  classical intervals; `exp(-2 int b)` and `E(s)=0` give `E == 0`. Correct.
  (3) follows by regularizing `sqrt(E)`; the note correctly refuses to call
  it a continuation estimate.

So the identity and the conclusion are right. **Verdict: CONFIRMED.**

**But: the no-start conclusion is subsumed by a three-line argument the same
author proved in note A, and the stronger version is missed.**

Suppose the hypotheses of Theorem 1 hold with `P f = 0` on an interval. Then
`U` is an unforced classical `C_t H^m` (`m>=4 > 3/2`) finite-energy solution,
so note A Lemma 1 applies and `U(t,.)` is real analytic on `R3`. Averaging
over a compact rotation group preserves the common holomorphic tube, so
`M U` is analytic too. Theorem 1's own hypotheses force `B = M U` (apply `M`
to the decomposition), hence `U - B = sum_gamma W_gamma` is ANALYTIC. It
vanishes on the open complement of the union of the label supports. By the
identity theorem `U - B == 0`, so EVERY label vanishes -- not only those with
zero initial value.

The needed open set is available in exactly the case the note cares about.
For [OA] the heat exterior `X >= X_ext` is an open region on which
`u = K(r,tau) e_theta` is axisymmetric, so `u - Mu = 0` there; independently,
`u` is compactly supported, so `u - Mu` vanishes outside a ball. Corollary
1.2's own hypothesis `q >= T-t` also makes only finitely many labels nonempty
at each fixed `t<T`, so their union is closed with open complement.

Consequences for the audit.

* Corollary 1.1 and Corollary 1.2: **CONFIRMED**, and both are strictly weaker
  than the analyticity argument, which needs neither `W_gamma(s)=0`, nor
  `S(B)` integrability, nor Gronwall, nor the energy identity.
* The genuinely new content of Theorem 1 is therefore (3), the weighted
  necessary FORCING/preparation estimate in the forced case, where analyticity
  is unavailable. The note's own framing ("no-start theorem") advertises the
  part that was already free.
* Practical warning: because the exclusion is really an analyticity rigidity,
  the class it removes is one no unforced flow could have occupied anyway. It
  does not narrow the live search. A repair note should either lead with (3)
  or relabel Theorem 1 as the forced quantitative statement.

I found no interchange of limits at `t -> T` (none is taken), no non-solenoidal
or non-decaying test field, no mode projection commuted through the
nonlinearity (label separation is used instead, correctly), and no
amplitude-ODE statement used as a PDE statement in Section 1.

### 4.2 Applicability of Theorem 1 to [OA]

Checked against the source, and it holds up better than I expected.

* Every nonzero harmonic carries `e^{i k m Phi}` with `Phi = p theta + ...`
  and `k m p in Z \ {0}` [OA, (7.3), Lemma 7.1, p.75]. In cylindrical
  components this has zero angular mean, so `M W_gamma = 0`. Correct.
* Each label's velocity is `curl_* A_m` of a supported potential
  [OA, Lemma 7.7, p.86], hence divergence-free, and a potential carrying only
  `m != 0` produces a velocity carrying only `m != 0`. So `div W_gamma = 0`
  and `M W_gamma = 0` simultaneously. Correct.
* [OA, (6.13)] separation is stated uniformly in `theta`, so passing to
  `(I - M)` does not enlarge a label's support onto another label's rotation
  orbit. This is the one place where a naive reading would break the
  hypothesis, and the source closes it. Note B's parenthetical "The support
  condition is uniform in theta" is doing real work and is correct.
* Corollary 1.2's arithmetic: `q >= T-t` from `q - z^2 q^{2h} = T-t`, and
  band `ell` supported where `q/Q in [1/2,2]`, `Q=2^{-ell}` [OA, (6.8)], so
  `q <= 2*2^{-ell}`. At fixed `s<T`, a nonempty label needs
  `T-s <= 2*2^{-ell}`, i.e. `ell <= log_2(2/(T-s))`. Correct.

**Verdict on Section 2 (source mapping): CONFIRMED.** One caveat the note
already carries: "the subsequent corrections preserve these properties" is
sourced to Prop. 9.3 and pp.104--105, which this audit did not read. That
single link is UNVERIFIED here, not disputed.

### 4.3 Theorem 2 and Section 3

Theorem 2 is note A's Theorem 4 with `psi_L` fixed to [OA, (6.16)] and the
tail exponent `exp(-cL/25)` from the `L/5` margin. `x_L(0)=0`,
`(d_v - A_L)x_L = g_L`, `|x_L(L/2)| >= c0`, (6) and (7): all correct,
identical checks as in Section 3 above. **Verdict: CONFIRMED**, with the same
deflation: it is a statement about unweighted norms, and the note's own
paragraph on Prop 7.2 concedes the point. The disclaimer "Theorem 2 is an
amplitude-equation theorem, NOT a full-PDE inverse theorem" is honoured
throughout.

The finite-gauge extension is algebraically correct: for `d` linear gauges,
pick `d+1` labels, solve the `d x (d+1)` homogeneous system, normalize the
largest coefficient to one, and read off the direct-sum sup norms. Correct.

**Objection: the finite-gauge remark does not reach the realistic repair.**
[OA] modulates PER LABEL -- the squared amplitudes `a_+`, `a_-` are chosen in
each slow box (Prop 7.5, p.81), and the covariance increment operator `L` is
applied per label. The natural modulation family therefore has one or more
gauges per label, i.e. countably many, not a fixed finite `d`. The argument as
written excludes only a globally finite-dimensional modulation. Note B does
qualify the claim ("for the DECOUPLED amplitude system only, not a claim about
a quotient of the full nonlinear PDE by all possible modulations"), which is
enough to keep it from being wrong, but the per-label counting is the
concrete reason it cannot be strengthened, and it is not stated.
**Verdict on the finite-gauge remark: CONFIRMED as stated, INAPPLICABLE to
[OA]'s per-label modulation.**

Section 4 ("What remains") is accurate. In particular "A single initial datum
must prepare the entire late family, not just any prescribed finite set" is
the right consumer statement, and the chain of unfilled terminal arrows is
honestly reported.

## 5. Note C

### 5.1 Theorem 1 (angular occupation/work inequality)

Hypotheses: `t0<T`, `tau=T-t`, `h,nu,R>0`, `C_B>=0`; `B` real, axisymmetric,
divergence-free, smooth with derivatives bounded on compact preterminal
intervals, and `||S(B(t))||_{Linf,op} <= C_B tau^{-1-h}`; `v_n` a smooth
solenoidal finite-energy solution in rotation mode `n` of (2.2), with `G_n`
the ENTIRE solenoidal source in that mode. Conclusion (2.4), plus the
zero-tolerant version with `W_n^+`.

Step check.

* (1.2): with `d_theta e_r = e_theta`, `d_theta e_theta = -e_r`, the Cartesian
  derivative along a rotation orbit of
  `v = e^{i n theta}(v_r e_r + v_theta e_theta + v_z e_z)` is exactly
  `e^{i n theta}[(i n v_r - v_theta)e_r + (i n v_theta + v_r)e_theta
  + i n v_z e_z]`. Correct.
* Eigenvalues: setting `alpha=v_r - i v_theta`, `beta=v_r + i v_theta`,
  `i n v_r - v_theta = (i/2)[(n-1)alpha + (n+1)beta]` and
  `i n v_theta + v_r = (1/2)[-(n-1)alpha + (n+1)beta]`, so the transverse
  form equals `((n-1)^2|alpha|^2 + (n+1)^2|beta|^2)/2 >= (|n|-1)^2
  (|v_r|^2+|v_theta|^2)`. Correct, and the axial eigenvalue `n^2` also
  dominates `(|n|-1)^2`. The note's warning that `n^2` would be FALSE for a
  vector field is correct (`n=1` gives eigenvalue 0).
* (1.3): `d_theta v = (Jx.grad)v` with `|Jx|=r`, so
  `|grad v|^2 >= |d_theta v|^2/r^2` pointwise, and integrating gives
  `||grad v||_2^2 >= (|n|-1)^2 int |v|^2/r^2`. Correct; genuinely no boundary
  condition and no Hardy inequality is used.
* `Pi_n` with `(T_theta v)(x) = R_{-theta} v(R_theta x)`: a unitary
  representation of `SO(2)`, so `Pi_n` is an orthogonal projection; it
  selects `e^{i n theta}` dependence of the CYLINDRICAL components; it
  commutes with `Delta` and with the whole-space `P`, and preserves
  solenoidality. Correct.
* (2.5): pairing (2.2) with `conj(v_n)` and taking real parts. `P` drops
  against the solenoidal `v_n`; `Re int conj(v_n).(B.grad)v_n =
  (1/2) int B.grad|v_n|^2 = 0`; the remaining quadratic term keeps only
  `S(B)` on the real part. Correct.
* (2.6): restricting (1.3) to `r <= R sqrt(tau)` and using
  `1/r^2 >= 1/(R^2 tau)`. Correct.
* Strain integral: `int_{t0}^{t} C_B (T-s)^{-1-h} ds =
  (C_B/h)(tau^{-h} - tau0^{-h})`. Correct.
* Zero-energy version: dividing by `E_n + eps^2` weakens the damping term in
  the right direction, `eta_n^eps <= 1` gives dominated convergence,
  `[Re<G_n,v_n>]^+/(E_n+eps^2)` increases as `eps` decreases so monotone
  convergence applies, and the initial bound is `sqrt(M^2+eps^2) -> M`.
  Correct.

Failure modes: no `t -> T` limit is taken anywhere (all statements are at
`t_j < T`); the test field is solenoidal and in `L2` so the pressure removal
is legitimate and the note says so explicitly; the mode projection is NOT
commuted through the nonlinearity -- `G_n = -Pi_n P[(z.grad)z]` keeps the full
projection, and the only commutations used (`Pi_n` past `(B.grad)` and past
`(.grad)B` for axisymmetric `B`, and past `Delta`, `P`) are exact. The
statement is per-mode and is never upgraded to "all harmonics".

**Verdict: CONFIRMED.**

### 5.2 Section 3 exactness

`B = Pi_0 u`, `z = u-B`, `v_n = Pi_n u`. Applying `Pi_n P` to unforced NS:
`Pi_n P[(B.grad)B] = 0` for `n != 0` since `(B.grad)B` is axisymmetric;
`Pi_n P[(B.grad)z] = P[(B.grad)v_n]` and `Pi_n P[(z.grad)B] =
P[(v_n.grad)B]` by rotation equivariance and linearity; the remainder is
`G_n = -Pi_n P[(z.grad)z]`. Exact. The claim that `B` need not solve unforced
NS separately, because its mean Reynolds forcing is annihilated by `Pi_n`,
is correct. **Verdict: (3.1) CONFIRMED as an exact identity.**

### 5.3 Corollaries 2, 3 and Theorem 4

Corollary 2: `J_n >= eta_* log(tau0/tau)` gives (2.7); with
`(|n_j|-1)^2 >= c_- q_j^{-h}` the exponent is at most
`-(nu eta_* c_-/R^2) q_j^{-h} L_j + (C_B/h) q_j^{-h}`, and for `L_j` beyond
`2 C_B R^2/(h nu eta_* c_-)` this is at most `-c_* q_j^{-h} L_j` with
`c_* = nu eta_* c_-/(2R^2)`. Exactly (2.9). The incompatibility with (2.10)
holds because `q^{-h} log(1/q) = L e^{hL}` beats every `(1+L)^p`. The single
finite-energy datum supplies a uniform `M = ||d||_2 >= ||Pi_n d||_2`. Forward
uniqueness for the homogeneous linear equation legitimises taking logs.
Correct throughout. **CONFIRMED.**

Corollary 3: (2.11) is (2.4) rearranged and divided by `nu c_- q_j^{-h}/R^2`;
`J_j` is then bounded, so `J_j/L_j -> 0`; and Chebyshev in the measure
`ds/(T-s)` (total mass `L_j`) gives the occupation fraction bound. Correct.
**CONFIRMED.**

Theorem 4: (3.2) is Theorem 1 with `G_n` from (3.1) and `J >= eta_* L_j`,
rearranged. Correct. It is a rearrangement, not an independent estimate, and
the note says so. The warning that `W_n^+` is normalized by `E_n` and is
therefore NOT an absolute energy cost, and must not be summed as one, is
correct and important. **CONFIRMED.**

### 5.4 Calibration to [OA]: better than the note claims, and narrower

Positive finding the note does not state. Hypothesis (2.1) is not an arbitrary
ansatz: from [OA, p.16], `E_core ~ tau^{3/2-h} tau^{-1-2h}` with core volume
`tau^{3/2-h}` gives `|u| ~ tau^{-1/2-h}` on a radial width `~ tau^{1/2}`,
hence a core strain `~ tau^{-1-h}` -- EXACTLY (2.1) with the same `h`.
Likewise the column `r <= R sqrt(tau)` matches [OA, (6.8)]'s active shell
`X_a <= r^2/(2q) <= X_b` whenever `q ~ tau`, and (2.8)
`(|n|-1)^2 ~ q^{-h}` matches the carrier `k = ceil(eps^{-1/2})`,
`eps = Q^h` of [OA, (7.2)] at bounded pitch. The note asserts only the last of
these. Stating the first two would strengthen its relevance claim materially.

Negative finding, and it bounds the reach of Corollaries 2 and 3 and
Theorem 4. `q ~ tau + |z|^{1/D}` [OA, p.15], so a label with
`|z|^{1/D} >> tau` sits at `r ~ sqrt(q) >> sqrt(tau)` and has `eta_n -> 0`.
The hypothesis `eta_n >= eta_* > 0` therefore selects only the sub-family with
`q ~ tau`, i.e. the axially concentrated core labels. The note disclaims the
hypothesis ("DOES NOT claim its externally forced pulses have a prehistory
satisfying `eta_n >= eta_*`"), so nothing is overstated, but the reason is
geometric and specific and should be recorded: the excluded class is
"core-trapped preparation", not "preparation".

Third finding: the entire mechanism is exactly ONE logarithm deep. Damping
`~ nu eta_* c_- R^{-2} tau^{-h} L` versus strain gain `~ (C_B/h) tau^{-h}`:
the powers of `tau` cancel identically, and the whole exclusion is the factor
`L = log(tau0/tau)`. This is why the proposed repair is precisely "lower `k`
by `sqrt(log(1/Q))`", and it is why Section 4 matters.

### 5.5 Section 4: frequency ceiling and the attempted logarithmic repair

Corollary 5 (4.1): (2.4) rearranged with `G_n=0`, `eta_n>=eta_*`,
`log(a_*/M) <= log(A(t)/A(t0))`. Correct. (4.2): with the quasi-polynomial
lower size, the `tau^{-h}` term dominates `(1+L)^p`, giving
`|n|-1 = O(tau^{-h/2}/sqrt(L))`. Correct. The interpretive sentence -- that
the instantaneous balance `n^2 ~ tau^{-h}` omits the logarithm of the
preceding preparation interval -- is the correct reading.

Lemma 6. `r = z_-/z_+` satisfies
`r' = E_21 + (-2 lambda + E_22 - E_11) r - E_12 r^2`; the scalar damping `d`
cancels exactly. Correct (and this is [OA]'s own computation in the proof of
Lemma 7.4, p.80). At `r = 2 delta/lambda_min` the right side is at most
`delta(-3 + 4q + 4q^2)` with `q = delta/lambda_min <= 1/8`, hence negative; at
the negative endpoint it is positive; so the interval is invariant, provided
`z_+ > 0`, which the growth bound `z_+' >= lambda_min(3/4 - q - 2q^2) z_+
>= (lambda_min/2) z_+` bootstraps. Correct. The bootstrap is stated in one
terse sentence ("Positivity follows by its scalar integrating factor, closing
the ratio argument"); it is a standard continuity/open-closed argument and it
does close, but a reader is entitled to more. Minor.

Applicability: [OA, (7.17)] has exactly `diag(lambda,-lambda) + E - m^2 d I`
with `|E| <= C/S_*` and `lambda = lambda_0/sqrt(1+s^2)` bounded below since
`u_*/2 <= |s| <= 3u_*/2`. So `delta = C/S_* <= lambda_min/8` for large bands.
In the UNMODIFIED construction `d_ref = lambda_0(1+s^2)/(1+u_*^2)^{3/2}`
exceeds `lambda` past the turning point `|s|=u_*`, so `d <= lambda_min/4`
fails and the lemma does NOT apply -- correctly, since [OA]'s pulse does
decay. The lemma is aimed only at the lowered-`k` variant, and the note says
so ("If `d = eps k^2 |n_Phi|^2` goes to zero with bounded `|n_Phi|`").

(4.4) is verified verbatim against [OA, (7.2)] (Section 0 above): reducing `k`
at [OA]'s prescribed `B_s` leaves `k^2 B_s^2` invariant, so the damping is
restored. Correct and decisive against the naive repair.

(4.5) is the honest non-result: a genuinely modified geometry with reduced
`eps k^2 ~ 1/log` would need `|s| ~ log^{1/3}` at the turning point, which
changes the polarization and stress-realization problem. The note explicitly
declines to validate or exclude it.

**Verdicts. Corollary 5: CONFIRMED. Lemma 6: CONFIRMED (with a terse but
correct positivity bootstrap). (4.4): CONFIRMED. The Section 4 repair
analysis: NOT AN EXCLUSION, and correctly not claimed as one.** Item 5 of
note C Section 5 ("fix (4) solely by lowering the carrier in an otherwise
fixed bounded phase geometry while preserving a two-sided Gaussian pulse") is
exactly the right scope for what was proved.

## 6. Overall verdicts

### 6.1 On the PLAN Section 1a claim

"Exact label separation with zero late-label initial values is no longer an
admissible unforced conversion."

**CONFIRMED as literally stated, with two qualifications that should be
recorded in PLAN before this sentence is relied on.**

1. It is true, and the label energy identity (2) proves it. But it is a
   corollary of classical spatial analyticity in a strictly stronger form: for
   an unforced classical `C_t H^s` solution with the stated separated-support
   decomposition and one open gap, ALL labels vanish, with or without zero
   initial values, with no strain hypothesis and no Gronwall. Note A's own
   Lemma 1 supplies this; note B never invokes it. The PLAN sentence therefore
   describes a barrier that is real but not new, and understates it.
2. Consequently the conversion branch it closes was never open. PLAN 1a's
   further sentence "This excludes ANY unforced exactification preserving zero
   late-band initial values and exact label separation while retaining nonzero
   late pulses" is correct but should not be read as narrowing the live search:
   the hypothesis "exact separated supports" is itself incompatible with an
   unforced flow whenever the flow coincides with its angular mean on any open
   set. The PLAN's operative instruction ("permit inherited overlap or justify
   one continuous initial preload") already points the right way.

The remaining PLAN 1a sentence about the flat principal inverse
("no fixed algebraic Q-loss bound extends to all raw-flat sources") is
CONFIRMED but should carry the norm caveat of Section 3 above: in the
envelope-weighted class where [OA] actually works, the seed is `~ S_*^{-1}`
and the exact response saturates [OA, (7.14)] with only polynomial loss.
"Superalgebraic loss" is a property of the unweighted norm, not of the inverse.

### 6.2 On whether [OA]'s force is removable

Question: do these obstructions, taken together, exclude [OA]'s force from
being removable by ANY unforced exactification preserving its support
structure?

The answer depends entirely on which support structure is meant, and the three
notes together settle three readings and leave the fourth -- the live one --
completely open.

1. **Compact spatial support of the velocity** (`supp u(.,t) subset K` for
   every `t<1`, [OA, Thm 1.1]): **EXCLUDED.** Note A Theorem 2(a) plus
   Corollary 3, and by the strengthening in Section 2.3 the exclusion holds on
   every open time interval, not only a terminal slab. This is classical
   (instantaneous spatial analyticity), correctly labelled as prior art in
   note A, and it applies to the ACTUAL global `P f`, not to a particular
   conversion. Any unforced exactification must give the velocity noncompact,
   analytic tails.
2. **The exact heat exterior / axisymmetric core patches**
   ([OA, (3.5)]: `A=0`, `B=K(r,tau)`, z-independent on an open set):
   **EXCLUDED.** Note A Theorem 2(b),(c). No quantitative lower bound on the
   required leakage is proved, and none is claimed.
3. **Exact label separation with zero late-label initial data**: **EXCLUDED.**
   Note B Theorem 1 and Corollaries 1.1--1.2, and more cheaply by analyticity
   as in Section 4.1.
4. **The compact space-time support of the FORCE alone, with the velocity
   allowed analytic tails, overlapping labels, and a continuous prehistory:
   NOT EXCLUDED, and untouched by any of the three notes.** This is precisely
   UE1--UE4 in PLAN Sections 3--4. Nothing here bears on it. In particular:
   note C's exclusions require `G_n = 0` (a linearized, not nonlinear,
   preparation), `eta_n >= eta_* > 0` (core-trapped preparation only -- see
   Section 5.4), and (2.1)/(2.8) with a common `h`; note C's own Corollary 3
   states that the exterior route is left open; note B Section 3's finite-gauge
   remark does not reach [OA]'s per-label modulation; and note A Proposition 6
   exhibits an exact flat free-trace repair on a single pulse interval.

So: **NO.** The obstructions exclude every exactification that keeps [OA]'s
compact velocity support, its exact rigid patches, or its exact zero-data label
separation -- i.e. every shortcut that reinterprets the existing fields --
but they do not exclude removal of the force by an exactification that changes
the flow. They collectively make one thing precise and correct: an unforced
counterexample cannot be obtained by relabelling [OA]'s residual, and must
instead solve the coupled autonomous free-trace preparation problem with
noncompact analytic tails. That problem is untouched.

Neither an unforced counterexample nor unforced regularity follows from
anything audited here, and none is claimed by the notes. No promotion is
warranted and none is made.

## 7. Non-blocking items for the author lanes (reported, not performed)

* Note A Corollary 3: state it for an arbitrary open time interval; the proof
  already gives that.
* Note A Lemma 1: move `s>3/2` and the uniqueness class into the hypotheses.
* Note A Theorem 2(c): replace "axisymmetric on an open set" by
  "`D_rot u = 0` on an open set".
* Note B Theorem 1: add the analyticity subsumption remark and re-lead with
  (3), the forced estimate, which is the part analyticity does not give.
* Note B Section 3: record that [OA]'s modulation is per-label, so the
  finite-gauge remark cannot be strengthened.
* Note C: record the (2.1)/(6.8)/(7.2) calibration of Section 5.4, and record
  that `eta_n >= eta_*` selects only the `q ~ tau` core sub-family.
* Both checkers: drop or replace the three tautological assertions named in
  Section 1, and add at least one assertion touching the rotation generator
  `D_rot u = (Jx.grad)u - Ju` and the `z`-independent `L2` triviality, since
  note A Section 1 is currently uncovered by any check.
