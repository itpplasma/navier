# RNS-BDNK-001: relativistic fate of the OpenAI collapse mechanism

Mode: **DISCOVER / FALSIFY**  
Status: **open**  
Updated: 2026-10-07

This is one concrete companion question. It does not change `NS-R3`.

## Frozen working packet

**TERMINAL CLAIM.** Fix one explicit conformal, zero-chemical-potential BDNK constitutive law on Minkowski (3+1) spacetime with transport/frame parameters satisfying its causal/stability conditions. Prove one of:

1. a smooth admissible BDNK solution realizes finite-time breakdown of a specified norm/continuation quantity; or
2. an unconditional theorem excludes a nonempty class containing the relativistic adaptation of the OpenAI shrinking-vortex collapse.

The first screen may allow a smooth covariant source to test compatibility. The main physical target is the closed/unforced model and must be stated separately.

**ESTABLISHED FOR THIS TASK.**

- The OpenAI classical NS construction supplies a concrete forced collapse profile; existing project notes already audit its forcing/preparation interfaces.
- BDNK has causal/strongly-hyperbolic local formulations and a nonrelativistic relation to Navier--Stokes for constrained transport coefficients.
- Small perturbations of suitable homogeneous BDNK states have global decay results.
- Existing BDNK numerics do not settle arbitrary large data: one study reports apparent singular steepening outside first-order validity, another reports shock regularization for selected data in a frame-robust small-Knudsen regime.
- Relativistic causal viscous theories can develop rigorous shocks/breakdown in Israel--Stewart-type reductions, so no universal “relativity heals” premise is allowed.

**FIRST GAP.** Construct a faithful covariant scaling adapter from the classical collapse variables to the full chosen BDNK stress tensor. Compute the leading orders of every term in (partial_mu T^{mu
u}=0) with timelike normalization and Lorentz factor retained. We do not yet know whether the classical balance survives, fails by one exact power/sign, or leaves the BDNK validity region before the singular scale.

**CHEAPEST FALSIFIERS.**

- an unavoidable BDNK term has a leading order incompatible with the collapse balance;
- the proposed profile violates (u^mu u_mu=-1), positivity/thermodynamic admissibility, or the chosen causal/stability inequalities;
- the only balance requires a forcing/source singular at the target time;
- the Knudsen/inverse-Reynolds measures necessarily become order one before the claimed BDNK mechanism, so the claim is only a closure-breakdown statement;
- conversely, an exact leading-order solution with all residuals lower order falsifies a proposed relativistic exclusion and justifies deeper construction work.

**FORBIDDEN INFERENCES.**

- bounded three-velocity implies bounded derivatives or Lorentz factor;
- formal (c\to\infty) convergence transfers a singular solution;
- BDNK shock regularization for one data family implies global regularity;
- numerical loss of convergence proves blow-up;
- Israel--Stewart breakdown proves BDNK breakdown;
- a forced relativistic singular history proves closed/unforced breakdown;
- leaving hydrodynamic validity proves microscopic physical singularity;
- a continuation criterion supplies its own arbitrary-data hypothesis.

**CHECK.** Symbolically derive the full scale table for the chosen BDNK equations. Compare it with the classical NS limit and with the exact OpenAI source profile. Record which term first changes order, sign or admissibility. No large simulation is justified before this table discriminates the mechanisms.

## Exact-loss design

The first result must name a deficit, not a framework. Examples:

- Lorentz saturation destroys one amplitude exponent;
- a causal characteristic term introduces a derivative at the same order as collapse;
- entropy production gives a sign but misses one gradient power;
- a transport coefficient required by causality becomes too small/large in the nonrelativistic scaling;
- or no new deficit appears and the classical leading balance survives.

If an obstruction is found, search for an RVM-style signed/coupled identity only for the exact offending term. If no obstruction is found, switch to construction: close the residual, forcing status, admissibility and singularity observation separately.

## Follow-up decision tree

### If the BDNK collapse survives

1. Upgrade the formal scaling to an exact forced (3+1) BDNK solution.
2. Determine whether forcing can be removed/internalized without changing the singular observation.
3. Check whether the singularity occurs while the constitutive expansion is controlled.
4. Test the same mechanism in Israel--Stewart and extended large-gradient causal models.

A common mechanism across distinct causal closures would support a broad “viscosity + relativity is insufficient” theorem.

### If BDNK excludes the collapse

1. Isolate the exact exclusion identity/inequality.
2. Test it against other BDNK frames and transport parameters.
3. Test Israel--Stewart, where known reduced models do blow up.
4. Test large-gradient extensions such as Gavassino's causal bulk model.

If the exclusion is BDNK-specific, pursue a model-separation theorem. If it is common to a broad physically admissible class, investigate a global continuation theorem.

### If the fluid model leaves validity first

Hand the same initial state to a kinetic model. The natural ITP bridge is `itpplasma/vlasov-maxwell`, ultimately with relativistic Maxwell--Landau or another explicitly chosen collision operator. The target is then not “fluid blow-up disappears” but a theorem that the hydrodynamic closure fails while the microscopic solution remains regular.

## Highest-value outcomes

Ranked by information value rather than expected ease:

1. **Full (3+1) BDNK breakdown or arbitrary-large-data regularity.**
2. **A model-separation theorem**: matched low-gradient physics, different finite-time behavior.
3. **A kinetic-escape theorem**: fluid closure singular/invalid, kinetic model regular.
4. **A broad closure breakdown theorem** for a causal hyperbolic viscous class.
5. **A classical back-transfer**: identify a physically motivated correction with a nontrivial (c\to\infty) limit that removes the collapse class. Any claimed uniform NS-limit regularity must confront the forced NS breakdown control quantitatively.
