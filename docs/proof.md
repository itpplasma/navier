# Whole-space proof dossier and extended endpoint interfaces

PLAN.md is the live allocation; this file describes the logical interfaces.
The terminal theorem is NOT PROVED. This update promotes no graph node.
The complete previous dossier is preserved byte-for-byte in
[the archived dossier](history/proof-before-clay-hilbert-programme-2026-09-06.md).
The canonical [proof graph](proof-graph.yaml), its evidence and manuscript
labels are unchanged. [The programme map](programme-graph.yaml) is a separate
map of unproved specifications, not an imported-theorem graph.

## Original target and retained suffix

NS-R3 is Clay alternative A: every divergence-free Schwartz u0 on R3 and
nu>0 admit smooth velocity and pressure on R3 x [0,infinity), solving the
original unforced equation and initial datum, with energy bounded by its
initial value. A periodic result is separate and does not automatically
establish this target.

LOCAL supplies the maximal classical/mild branch, smoothness through the
initial time and the finite-time blow-up alternative. ENERGY supplies

    ||u(t)||_2^2 + 2 nu integral_0^t ||grad u||_2^2 = ||u0||_2^2.

CONTINUATION says that a finite maximal time requires the uniform L3 norm
to diverge. Its published endpoint input, local/energy hypotheses and
manuscript-owned bridges remain exactly as recorded in the canonical graph.
An input-only L3 bound on every finite horizon therefore closes NS-R3.
An appropriate L5 spacetime bound may instead feed the existing SERRIN node.
Neither is obtained from energy alone.

The pressure/quotient consumers and later author-checked paper components
remain valid within their stated hypotheses; their arbitrary-data producers
remain missing. Their retired primary allocation is not a retraction. The
structural-obstructions paper and no-go notes keep their distinct premise
classes and independent-audit/prior-art qualifications.

## Kinetic candidate suffix (not yet an instantiated proof)

Use the whole-space hard-sphere GSR framework with the Maxwellian preparation
M(v-epsilon u0(x)), prescribed viscosity, relative entropy and a justified
projected/truncated momentum m_tilde_epsilon. The source application must
supply a Leray velocity limit with the right energy/trace properties; finite
entropy alone does not permit arbitrary classical moment manipulations.

For an input-determined delta inside the classical lifespan, let S_J be KPC's
compact spatial mollifiers. The candidate producer is

    sup_J liminf_k ||S_J m_tilde_epsilon_k||_{L-infinity(delta,H;L3(R3))}
      <= C(u0,nu,H,delta),

on one convergent kinetic sequence and with the same constant for every J.
Distributional convergence/duality first at fixed J, then removal of J,
yields the limiting L3 bound. Weak--strong uniqueness identifies the Leray
limit with the classical branch before its maximal time. LOCAL handles
[0,delta], CONTINUATION rules out a finite endpoint, and ENERGY finishes.
See [the full contracts](../research/kinetic-clay-hilbert-contracts.md) and
[the existing KPC calculations](../research/evidence/2026-09-06-kinetic-plan-contracts.md).

This is an explicit conditional chain, not a claim that the hard estimate
has been made easier or proved. Its nonlinear producer and application audit
must be completed before the canonical graph can change.

## Microscopic extension is downstream and independently gated

KIN-R3 retains a kinetic realization of the regular fluid. MIC-R3 additionally
requires Newtonian hard-sphere initial laws and particle-to-kinetic, domain,
scaling and observable limits. A particle theorem requiring regular Boltzmann
cannot simply be applied to arbitrary renormalized solutions. A theorem on
a fixed torus does not cover R3 with infinite Maxwellian background mass.

After an independent NS regularity proof, a suitable smooth-target kinetic
theorem may legitimately reconstruct regular kinetic solutions on each finite
horizon. Then apply a matched microscopic theorem, with a separate whole-space
or thermodynamic-limit adapter and an explicit diagonal. Alternatively prove
a microscopic theorem in the weak kinetic class actually used. Neither path
is currently complete. These extra gaps do not delay the primary critical-
estimate attack and do not turn MIC-R3 into a claim about all of Hilbert VI.

Formal Phase I/II retains its existing meaning. Planning checks and source
inspection are not mathematical audits, axiom reports or Lean coverage.
