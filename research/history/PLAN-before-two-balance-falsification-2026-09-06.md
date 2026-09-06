# Navier--Stokes: terminal-first strategic reset

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: arbitrary-data-strategic-pivot-2026-09-06
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: fixed-input-selector-falsification-after-intrinsic-extraction
active_architecture: intrinsic-record-objects-with-fixed-input-ancestry
complete_terminal_route: none-established
retired_primary_route: pressure-quotient-defect-shell-material-response
intrinsic_bridge_status: author-checked-independent-audit-pending
single-profile-rigidity_status: falsified-for-the-normalized-package
terminal_status: not-proved
formal_work_this_run: deferred
public_release: false
```

## 1. Binding decision and target

**Retire the pressure / cubic-gradient-quotient / defect / speed-shell /
material-response family as the primary arbitrary-data research route.**
This is an allocation decision based on repeated demonstrated failure to
supply an endpoint producer, not a theorem that all future pressure or
geometric arguments must fail. The valid conditional statements and their
reviews are retained. No more local derivatives, new rates, cancellations,
regularization devices, or manuscript sections in that family are an active
terminal task. Reopening it requires an actual input-only endpoint argument,
with the quantifiers and limiting uniformity established at the outset.

The owner's 2026-09-06 breakthrough protocol supersedes the old task order.
The former complete PLAN is preserved byte-for-byte at
`research/history/PLAN-before-intrinsic-pivot-2026-09-06.md`, using its original
blob `073faf6c7045c83363f3c9d33ed1919f5f0d7015`. It is history, not a second
live instruction surface. The original research head was
`c2c5f793d1e447a82dd99c7e434c76fc989ec316`; the inspected manuscript head was
`81f0cd1524e8a625e6ee46970d69e40e5a2e50bf`.

The unchanged target is the unforced whole-space problem: every smooth
solenoidal Schwartz datum on R3, every fixed positive viscosity, a global
smooth solution of the original equation with uniformly bounded kinetic
energy. Periodic, variable-viscosity, forced, averaged, and Euler examples
below are explicitly scoped mechanism tests, not substitutes for this target.

**The target is not proved.** This reset establishes a new extraction bridge
and a rigorous counterexample to an overbroad proposed rigidity suffix. It
does not claim an input-only critical bound, a full alternative proof, a
novelty result, or an independent mathematical audit.

## 2. Work backward from the terminal implication

For a fixed finite horizon H, make the exact normalization

$$
 v(y,s)=\sqrt{H/\nu}\,u(\sqrt{\nu H}\,y,Hs),\qquad
 q(y,s)=(H/\nu)p(\sqrt{\nu H}\,y,Hs),
$$

$$
 a(y)=\sqrt{H/\nu}\,u_0(\sqrt{\nu H}\,y),\qquad S_*=T_*/H.
$$

Then v solves unit-viscosity Navier--Stokes with datum a, horizon one, and
$\|v(s)\|_3=\nu^{-1}\|u(Hs)\|_3$. The smallest missing assertion in the
existing conditional graph is

$$
 \sup_{0\le s<\min(1,S_*)}\|v(s)\|_3\le F(a)<\infty,            \tag{T}
$$

where F is determined without using an unknown terminal solution norm.
The retained LOCAL, ENERGY, and CONTINUATION nodes then finish that graph.
Alternatively, a direct contradiction to $S_*<\infty$ can bypass (T);
there is no obligation to preserve the old critical-norm architecture.

The graph's EXISTENTIAL node already records that HIGH-PRESSURE, at its
ordinary existential quantifiers, is equivalent to global continuation.
Consequently replacing (T) by the existence of a pressure remainder was not
an independent producer. The exact signed identities remain valid as
conditional tools, but their right sides are not controlled by the inputs.

### Common obstruction, not a list of unrelated missing estimates

ENERGY controls $\int Y\,dt$, where $Y=\|\nabla u\|_2^2$. Repeated
consumers demand $\int Y^2\,dt$, a fourth-power defect integral, a signed
form rate, a residual rate, or an even stronger diffusion/strain action.
The changes of representation have not changed the critical time exponent.
The explicit scalar function $Y(t)=(T-t)^{-1/2}$ has finite first integral
and divergent square integral. This is a counterexample to the scalar
inference, not a Navier--Stokes blow-up solution.

The same mismatch appears geometrically. A critical-size event of radius r,
amplitude comparable to $\nu/r$, and duration comparable to $r^2/\nu$
uses kinetic energy and viscous dissipation of order $\nu^2r$. Such costs
are summable over geometrically decreasing radii. An additional geometric
proliferation theorem might change that conclusion; the energy budget alone
does not. No singular Navier--Stokes trajectory is constructed by this
scaling calculation.

The recent record is explicit about its own nonclosure:

- `2026-09-06-dissipation-budget-continuation.md`: the nonendpoint family
  still needs a critical temporal defect budget; the trajectory-finiteness
  comparison is author-checked, with independent review pending.
- `2026-09-06-speed-shell.md`: the depletion factor is scale invariant;
  the resulting fourth-power rate is still critical and has no input-only
  time bound.
- `2026-09-06-material-response.md`: the exact moving-frame action still
  contains weighted second derivatives, squared strain, and a commutator;
  uniform refinement is unproved.

All three paths are under `research/evidence/`. Retirement does not depend
on promoting their pending proofs to audited theorems. Their stated stopping
points, the graph's established equivalence, and the scaling tests already
justify changing the primary route.

## 3. Ten architectures screened from the terminal end

Each entry specifies a proposed terminal mechanism, one central missing
lemma, its non-tautology test, scaling, a fast falsifier, and the retained
project inputs. A proposal failing the non-tautology or falsifier gate is
not repaired by introducing another name. These are different mathematical
objects, not ten versions of the old functional.

### A. Minimal bad L3 initial datum and concentration compactness

**Mechanism.** Obtain a minimal singular solution with a compact orbit modulo
symmetries, then apply endpoint rigidity. **Decisive lemma proposed.**
Minimality of the initial L3 norm supplies precompactness of the entire
rescaled orbit in L3. **Non-tautology test.** Failed: initial minimality only
makes subsequent bad data have norm at least the threshold. It gives no
upper bound along the trajectory. Orbit precompactness would include the
very bounded critical norm needed by CONTINUATION. Minimal bad initial data
are already a literature construction, not a fresh bridge (Jia--Sverak,
arXiv:1201.1592). **Scaling.** L3 is invariant, while the nonlinear orbit
need not preserve its initial norm. **Fast test.** Inspect whether a proof
uses a finite supremum-in-time critical threshold rather than only initial
minimality. That is the old gap. **Reuse/discard.** Retain LOCAL, scaling,
and the endpoint consumer; discard quotient machinery. **Decision.**
Retire the automatic-orbit-compactness version; do not reprove minimal
initial-data existence as terminal progress.

### B. Minimize energy among bad data

**Mechanism.** A positive minimal energy object would combine an energy
Lyapunov law and minimality to force stationarity, then vanish.
**Decisive lemma proposed.** The infimum of squared L2 norms of bad data is
positive and attained by a nonzero datum. **Non-tautology test.** This is a
concrete variational assertion, not regularity renamed, but it is false
conditional on there being any bad datum. **Scaling.** For
$u_{0,\lambda}(x)=\lambda u_0(\lambda x)$, energy is
$\lambda^{-1}E_0$ and singular time is $\lambda^{-2}T_*$. Thus the
unconstrained infimum is zero; zero data are regular. **Fast falsifier.**
Send $\lambda\to\infty$. **Reuse/discard.** Only LOCAL and SCALE are
needed. **Decision.** Killed. A new scale-invariant variational problem
would need a new, actually proved monotonicity law; changing the objective
to an energy/enstrophy product does not establish one. After A and B, stop
refining the minimality family during this run.

### C. Classical bounded ancient velocity records

**Mechanism.** Point-picking produces an ancient object, then Liouville
rigidity contradicts its normalized nonzero velocity. **Decisive bridge
proposed.** The ancient object inherits a uniform global finite-energy
bound, excluding constants and allowing dissipative rigidity.
**Non-tautology test.** This would be additional structural information,
but it is not inherited by the displayed energy estimate. **Scaling.** At
velocity scale M, normalized energy is bounded only by $ME_0$, which
diverges. **Fast falsifier.** A nonzero constant is a bounded ancient mild
solution, and a normalized local limit need not retain spatial tails.
`compactness.md` already documents this failure and the KNSS reduction.
**Reuse/discard.** Retain LOCAL and the Stokes kernel, not a claimed global
energy bound on the tangent. **Decision.** Retire automatic energy
inheritance and zero-velocity rigidity. Revisit the high-level idea with a
normalized increment instead: architecture J.

### D. Backward uniqueness and Carleman propagation

**Mechanism.** A zero terminal vorticity trace propagates backward, then
contradicts nontriviality. **Decisive lemma proposed.** Arbitrary-data
blow-up extraction supplies that zero trace and the exterior coefficient
control needed for backward uniqueness. **Non-tautology test.** The
package is not supplied by LOCAL or ENERGY; importing the critical L3
compactness used by the endpoint theorem would make it the same endpoint
assumption in another form. **Scaling.** Vorticity scales as
$\lambda^2$, strain as $\lambda^2$, and critical exterior coefficient
bounds do not follow from the supercritical energy scaling. **Fast test.**
Track the final-time trace under the normalization before invoking a
Carleman theorem; a nonzero ancient profile does not have zero terminal
trace. **Reuse/discard.** Retain ESS/CONTINUATION only as conditional
consumers; quotient rates are irrelevant. **Decision.** No arbitrary-data
trace producer was proved; do not launch a Carleman implementation around
an assumed trace.

### E. Exact spectral feedback and a closed finite-band component

**Mechanism.** A nonzero ancient spectral component with bounded energy,
a frequency gap, and no exterior energy input would contradict
$E'+c\mu E\le0$ when $\mu>0$. **Decisive lemma proposed.** Extract such
a closed, nontrivial component from every singular frequency cascade,
without assuming tightness or zero incoming flux. **Non-tautology test.**
Those last two conditions are not consequences of a Fourier decomposition;
assuming them simply hides the selection problem. **Scaling.** Band
coordinates can normalize the central frequency, but energy and the
viscosity of the resulting dynamical system must still be tracked.
**Fast falsifier.** Convolution creates other modes, flux has both signs,
and helicity cancellation does not eliminate stretching. The exact
periodic snapshot in Section 5 below has zero helicity and positive total
stretching. **Reuse/discard.** Retain Fourier analysis and ENERGY;
discard scalar absolute-flux bounds as a closure argument. **Decision.**
Retire automatic closed-component and helicity-sign versions. No alleged
hull-selection or axisymmetry reduction is imported without checking all
of its compactness and closure premises.

### F. Geometric-measure packing of singular events

**Mechanism.** A singularity forces enough disjoint or branching events to
exhaust finite physical dissipation. **Decisive lemma proposed.** The
scale-normalized event tree has a quantitative branching law making the
sum of physical event costs diverge. **Non-tautology test.** A concrete
branching law would be more than a regularity criterion and could be tested
on smooth concentration episodes; none is established here. **Scaling.**
An isolated critical event costs order $\nu^2r$, not an order-one amount
independent of r. **Fast falsifier.** A single dyadic chain has summable
cost. A dimension or lower-density statement alone does not create the
missing branching. **Reuse/discard.** ENERGY and local suitable-solution
methods may be useful; old quotient identities are unnecessary.
**Decision.** Retire budget-only and one-cost-per-scale contradictions.
Do not cite partial regularity as the missing proliferation theorem.

### G. Stochastic-Lagrangian deformation cocycles

**Mechanism.** Stochastic averaging suppresses stretching of the inverse
flow derivative, controlling the represented velocity without a Eulerian
critical norm. **Decisive lemma proposed.** Incompressibility and additive
Brownian noise force a uniform contraction of the stretching cocycle.
**Non-tautology test.** This is a genuine pathwise/statistical mechanism,
but those two properties do not imply it. An unknown exponential strain
moment would merely replace the old clock. **Scaling.** The integrated
strain and the deformation matrix are dimensionless under NS scaling.
**Fast falsifier.** For the exact affine solution
$u=(ax,-ay,0)$, $p=-a^2(x^2+y^2)/2$, the additive-noise flow derivative
is $\mathrm{diag}(e^{at},e^{-at},1)$: determinant one is compatible
with unbounded stretching. This is an infinite-energy model falsifying
volume/noise-only contraction, not a whole-space finite-energy theorem.
**Reuse/discard.** Retain the original equation and the
Constantin--Iyer representation as background; discard any claim that a
representation itself bounds its Jacobian. **Decision.** Retire that
contraction mechanism; no coupled fixed-input replacement was proved.

### H. Similarity-variable Lyapunov or monotonicity principle

**Mechanism.** A coercive monotone quantity makes all normalized complete
orbits stationary, then a stationary classification gives a contradiction.
**Decisive lemma proposed.** The Gaussian/localized similarity energy has a
signed derivative after all pressure and transport fluxes are retained.
**Non-tautology test.** A specified identity with a proved sign would be a
new mechanism; an assumed monotonicity formula is not. **Scaling.** The
similarity transformation fixes the parabolic scale but does not turn the
original L2 bound into a uniform normalized energy bound. **Fast test.**
Evaluate the full pressure/transport term on solenoidal snapshots and
under velocity sign reversal; an uncancelled cubic term has no universal
sign. Do not drop boundary or harmonic-pressure contributions.
**Reuse/discard.** Retain LOCAL and the original local energy law, not the
quotient clock. **Decision.** Screened out: no sign-definite, coercive
formula survived derivation. This is not a theorem ruling out all future
monotonicity principles.

### I. Vortex-line geometry and forced dimensional reduction

**Mechanism.** The normalized high-vorticity set has an invariant planar
or integrable geometry, reducing the tangent equation to a class with
rigidity. **Decisive lemma proposed.** The original dynamics force that
geometry at every possible singularity, rather than merely preserve it
when imposed initially. **Non-tautology test.** Such a geometric selection
law would be independently testable. Assuming directional coherence or
planarity instead is just a conditional regularity route. **Scaling.**
Vorticity direction is dimensionless; its variation at the shrinking
scale is not controlled by global energy. **Fast test.** Alignment with
a positive strain eigenvector increases vorticity; incompressibility only
sets the trace of strain to zero. A prescribed initial geometry is not an
inherited arbitrary-data geometry. **Reuse/discard.** Retain the vorticity
equation and relevant restricted-class Liouville theorems; discard the
speed-shell representative. **Decision.** No forced-geometric-selection
lemma was proved. Do not assume a two-dimensional or axisymmetric tangent.

### J. Intrinsic Holder-record increments and fixed-input ancestry

**Mechanism.** Replace nonzero velocity by a nonzero spatial increment,
extract a canonical ancient object without a critical bound, and seek a
structural obstruction compatible with its actual source trajectory.
**Decisive first bridge.** Finite-time breakdown gives a centred ancient
NS/Euler tangent with unit increment, a uniform global Holder seminorm,
and noncollapsing local Reynolds number. **Non-tautology test.** Passed:
this is a necessary construction with explicit estimates, not a hidden
bound on the original seminorm. The resulting class has many nonzero
members, so the bridge alone does not assert regularity. **Scaling.**
$A_nr_n/\nu$, the normalized increment, and both normalized backward
domain lengths are invariant. **Fast falsifiers.** Constants test
nontriviality; a caloric limit tests Reynolds collapse; stationary Euler
shears test overbroad rigidity. The first two failures are excluded by
the proof. The third is real, even with viscous ancestry as in Section 4.
**Reuse/discard.** LOCAL, ENERGY, and the Stokes derivative kernel suffice;
none of the pressure-work, quotient, defect, or shell hypotheses is used.
**Decision.** Retain the proved extraction. Retire universal single-profile
rigidity, even strengthened by the normalized initial seminorm and the two
backward ages. No complete fixed-input rigidity suffix has been established.

## 4. Mathematical delta: extraction and a stronger falsifier

### 4.1 Proved first bridge, not a new endpoint criterion

The complete argument is
`research/evidence/2026-09-06-intrinsic-record-tangents.md`.
It fixes $1/3<\alpha<1/2$, uses first records of $[u]_{C^\alpha}$,
maximizing increments $A_n=h_nr_n^\alpha$, and a frame moving with the
local spatial mean. The normalization has no unproved critical input.
The decisive kernel estimate gives, for a fixed sufficiently large L,

$$
 1\le C_\alpha L^{(\alpha-1)/2}
  +C_\alpha\frac{A_nr_n}{\nu}
     (L^{1/2}+L^{\alpha+1/2}),
$$

hence $A_nr_n/\nu\ge c_\alpha>0$. This is a lower Reynolds bound,
not an upper bound or a temporal clock estimate. Uniform local compactness
then preserves a unit spatial increment. Constants cannot absorb the
nontriviality as they could in the older velocity-record construction.

The far pressure tail is integrable because $2\alpha<1$. The moving
frame's acceleration is explicitly retained as a linear pressure or as
subtraction of the mean generator; it is not an uncontrolled omitted term.
The limit has effective viscosity $\mu\ge0$. For $\mu=0$, the local
Constantin--E--Titi commutator with $3\alpha>1$ proves local energy
conservation and vanishing local viscous dissipation measures.

This removes an actual construction obstruction. It does **not** prove
that the remaining ancient objects are impossible. It makes no assertion
that normalized energy is globally finite, or that finite-energy tails of
the original solution survive the zoom.

### 4.2 Actual viscous counterexample to an overbroad rigidity suffix

The complete argument is
`research/evidence/2026-09-06-viscous-mixing-falsifier.md`.
On the periodic three-torus take the exact smooth NS family

$$
 U^\varepsilon=(e^{-2\varepsilon t}\sin x\cos y,
              -e^{-2\varepsilon t}\cos x\sin y,W^\varepsilon),
$$

where W solves the displayed passive advection-diffusion equation in that
note with initial datum $\sin y$. All members have the same smooth
periodic initial velocity and uniformly bounded energy per cell.
Choosing $\varepsilon_n=n^{-1/2}e^{-2n}$ gives actual first-record
increments with

$$
 t_n=n+O(1),\quad r_n\asymp e^{-n},\quad A_n\asymp1,
 \quad \mu_n\asymp n^{-1/2}e^{-n},
$$

$$
 S_n\asymp ne^n\to\infty,\qquad
 \mu_nS_n\asymp\sqrt n\to\infty,
 \qquad [v_n(-S_n)]_\alpha\to0.
$$

Nevertheless their nonconstant normalized ancient limit is a stationary
Euler shear. Thus the following properties can coexist: genuine viscous
parents, first-record selection, a unit increment, global Holder control,
a vanishing normalized initial seminorm, both arbitrarily long backward
domains, and zero local anomalous dissipation.

**Scope matters.** The viscosities vary, the record times tend to infinity,
and the parents are periodic rather than finite-energy on R3. This does not
construct a singular solution of the target equation. It does rigorously
prevent a future agent from claiming that the normalized package alone,
or a false exchange of the receding-initial-time and compactness limits,
excludes Euler shear tangents. A theorem about one fixed whole-space input,
one fixed viscosity, and a finite physical endpoint would need additional
information not present in that package.

After the bare shear test and this actual viscous-ancestry test, stop
refining blanket ancient rigidity in this run. The spectral and stochastic
alternatives were separately checked rather than adding another condition
to the same putative Liouville theorem.

## 5. A finite exact spectral falsifier

For the smooth periodic solenoidal snapshot

$$
 u=(0,-\cos x,\sin y+\cos(x+y)),
$$

let angle brackets denote the spatial average over a $2\pi$ cell. Direct
integration gives

$$
 \langle |u|^2\rangle=3/2,\quad
 \langle |\nabla u|^2\rangle=2,\quad
 \langle |\Delta u|^2\rangle=3,
$$

$$
 \langle u\cdot\omega\rangle=0,\qquad
 \langle\omega\cdot(\nabla u)\omega\rangle=1/4.
$$

For amplitude B, the exact initial enstrophy derivative of its smooth
local NS evolution is

$$
 \tfrac12Y'=(2\pi)^3(B^3/4-3\nu B^2),
$$

which is positive for $B>12\nu$. Hence zero total helicity does not force
nonpositive total stretching. This is not a counterexample to any
appropriately stronger spectral-feedback theorem. The identities were
checked by exact symbolic differentiation and integration, not a PDE
simulation. The explicit formulas make the check reproducible without
adding a new implementation workstream.

## 6. What is next, and what is not allowed to masquerade as next

The active exploratory object is the collection of intrinsic records from
**one fixed input and one fixed viscosity approaching one finite physical
endpoint**, not an arbitrary isolated ancient solution. The extraction in
Section 4.1 is available for this investigation. The mixing counterexample
is a mandatory regression test for any proposed inherited property.

A concrete first falsification target is a **nonlinear-activity selection
lemma**: does finite-time, fixed-input ancestry force at least one admissible
intrinsic tangent whose centred projected nonlinear generator is nonzero?
For the notation of the extraction note, that generator is

$$
 \mathcal N(v)=\nabla\cdot(v\otimes v)+\nabla\mathcal P[v]
  -\left\langle\nabla\cdot(v\otimes v)+\nabla\mathcal P[v]
    \right\rangle_\phi.
$$

The displayed condition is precise, can fail for nontrivial flows, and is
not itself a regularity theorem. The viscous mixing example has a limiting
$\mathcal N(v)=0$, so a proof based only on the normalized package is
already ruled out. A valid selection proof must use information that this
example lacks. **No such selection lemma is proved or assumed here.** Even
if proved, it would remove the passive-shear escape, not classify all
nonlinear ancient profiles or finish NS-R3. Its purpose is an immediate
non-tautological test, not a replacement name for the terminal theorem.

Do not define "reachable" to mean "produced by a singularity" and then
assert that this class is empty as though that were new mathematics. Do
not add an unproved critical norm, a tightness hypothesis, a bounded
regularization constant, or zero spectral forcing and call the result a
bridge. After two serious attempts encounter the same obstruction, change
the object or architecture rather than refine that family.

The commit gate remains the owner's gate: a terminal/near-terminal
implication, a rigorous major-route obstruction, a decisive new bridge,
or a strategy change based on such evidence. A conditional consumer,
local identity, formalization, or manuscript expansion is not a substitute.

## 7. Authority, preserved state, and verification scope

This PLAN is the sole live research allocation. The original
`docs/proof-graph.yaml` remains the retained conditional-paper dependency
record, not an instruction to resume its old primary route. No graph node
has been promoted. In particular NS-R3, CRITICAL, HIGH-PRESSURE,
HIGH-STRAIN, and DEFECT-L4 remain gaps. No new research note is registered
as an audited manuscript theorem or given a fictitious paper label.

The Phase I/II strings in the header preserve the existing formal coverage
status and the structural verifier's consistency requirements; they do
not authorize spending this run on formalization or claim a new Lean
result. Formal work and mathematical manuscript integration are deferred
in this terminal-first run. The manuscript's mathematical sources and
conditional statements are left unchanged. Its agent instructions are
updated only to prevent restarting the retired architecture by default.

The two new proofs are **author-checked, independent-audit pending**. Their
required audit points are listed in the notes. Exact algebra was checked
for the cellular-flow solution, its strain norm, and the spectral snapshot.
No independent reviewer, Lean build, Navier--Stokes simulation, full
repository structural-verifier run, or manuscript compilation is claimed
by these checks. The mathematical manuscript is not edited, so no new
manuscript integration or build claim is made. GitHub transport uses fresh
refs, explicit paths, and non-force fast-forward updates; this verifies
publication of the research record, not the truth of a PDE proof.

All repositories remain private. No outside contact, new authorship,
submission, public release, or Overleaf recreation is authorized.

## 8. Primary-source context

The notes distinguish their derivations from imported literature. The
following sources inform the architecture screen; none is an arbitrary-data
producer for this project.

- Koch--Nadirashvili--Seregin--Sverak, *Liouville theorems for the
  Navier--Stokes equations and applications*, arXiv:0709.3599. The Stokes
  derivative kernel is used in the extraction proof; its weighted moment
  and the intrinsic normalization are derived there.
- Jia--Sverak, *Minimal L3-initial data for potential Navier--Stokes
  singularities*, arXiv:1201.1592. Initial-data minimality is not orbit
  boundedness. This source is context, not a new project theorem.
- Seregin, *Remarks on Type II blowups of solutions to the Navier--Stokes
  equations*, arXiv:2304.04045v1. Proposition 1.2's additional growth and
  Morrey hypotheses are not silently dropped; its Euler-limit theorem is
  not imported as an arbitrary-data extraction result.
- Constantin--E--Titi, *Onsager's conjecture on the energy conservation for
  solutions of Euler's equation*, Commun. Math. Phys. 165 (1994), 207--209,
  DOI 10.1007/BF02099744. The local commutator argument needed in the
  new extraction note is written explicitly, without a global L2 premise.
- Gavrilov, *A steady Euler flow with compact support*, arXiv:1810.08020v1.
  Even adding finite energy to a general Euler Liouville assertion cannot
  eliminate all steady examples.
- Constantin--Iyer, *A stochastic Lagrangian representation of the
  three-dimensional incompressible Navier--Stokes equations*,
  arXiv:math/0511067. A representation is not a deformation bound.
- Tao, *Finite time blowup for an averaged three-dimensional Navier--Stokes
  equation*, arXiv:1402.0290. This is a different equation, useful only as
  a warning against trying to close the problem with energy cancellation
  and generic estimates alone.

A focused source check is not an exhaustive novelty survey. No claimed
recent proof or dimensional-reduction theorem is used without verifying
its actual hypotheses and the specific implication needed here.
