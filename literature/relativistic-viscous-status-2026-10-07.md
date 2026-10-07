# Relativistic viscous hydrodynamics: source ledger

Updated 2026-10-07. This note records source scope, not project acceptance of every theorem or numerical interpretation. It supports `docs/relativistic-viscous-programme.md`.

## Closest relativistic analogue: BDNK

**Bemfica, Disconzi, Noronha, First-Order General-Relativistic Viscous Fluid Dynamics, Phys. Rev. X 12, 021044 (2022).**  
https://doi.org/10.1103/PhysRevX.12.021044

The paper presents a first-order relativistic viscous theory with shear, bulk and heat conduction that can be causal and strongly hyperbolic, with stable equilibria and nonnegative entropy production in its regime of validity. This is the primary BDNK foundation used here. “First-order” refers to the constitutive gradient expansion; conservation makes the PDE second order in the hydrodynamic variables.

**Hegade K. R., Ripley, Yunes, Nonrelativistic limit of first-order relativistic viscous fluids, Phys. Rev. D 107, 124029 (2023).**  
https://doi.org/10.1103/PhysRevD.107.124029

The BDNK nonrelativistic limit can reproduce Navier--Stokes under restrictions on transport coefficients; relativistic causality leaves constraints in that limit. Fourier heat conduction requires higher-gradient corrections in the analyzed scaling. This is a formal/model bridge, not a uniform transfer theorem for singular solutions.

**Sroczinski, Global existence and decay of small solutions for quasi-linear second-order uniformly dissipative hyperbolic-hyperbolic systems, JDE 383 (2024), 130--162.**  
https://doi.org/10.1016/j.jde.2023.10.056

The theorem gives global strong solutions and decay for sufficiently small perturbations of homogeneous states for a class that includes recent relativistic viscous models. Disconzi's review identifies it as a BDNK global-well-posedness result for perturbations of constant states with specific equations of state/transport coefficients. It is not arbitrary-large-data global regularity.

**Disconzi, Recent developments in mathematical aspects of relativistic fluids, Living Rev. Relativ. 27, 6 (2024).**  
https://doi.org/10.1007/s41114-024-00052-x

Useful status review. It emphasizes that relativistic viscous theories are causal hyperbolic systems rather than the standard parabolic Navier--Stokes--Fourier system, summarizes BDNK causality/local well-posedness/stability and small-data global results, and separately records finite-time breakdown for DNMR/MIS-type systems.

## BDNK: evidence in both directions

**Keeble, Pretorius, First-order viscous relativistic hydrodynamics on the two-sphere, Phys. Rev. D 112, 124034 (2025).**  
https://doi.org/10.1103/d4wd-zj7w

Numerical BDNK evolution of a smooth stationary Gaussian energy pulse develops very steep gradients and loses convergence for sufficiently large entropy-normalized shear viscosity; the behavior persists across tested resolutions and in higher-resolution planar (1+1) simulations. The authors call this numerical evidence of finite-time singularity formation from smooth data. They also state that the evolution leaves equilibrium and the regime of validity of first-order hydrodynamics. This is therefore neither a rigorous blow-up theorem nor evidence of a microscopic physical singularity.

**Clarisse, Pinho, Patel, Bemfica, Hippert, Noronha, Flux-conservative BDNK hydrodynamics and shock regularization, Phys. Rev. D 113, 024051 (2026).**  
https://doi.org/10.1103/f8y1-3yck

For conformal (1+1)-dimensional BDNK at zero chemical potential, numerical smooth data that form shocks in relativistic Euler instead have their sharp features regularized in the studied BDNK evolution. The observed prevention occurs in a hydrodynamic-frame-robust small-Knudsen regime. The paper explicitly does not exclude shocks for other BDNK data. This is the best current control against the claim that every steepening mechanism survives viscosity unchanged.

Together these two papers make “BDNK always heals” and “BDNK always blows up” equally unsupported.

## Israel--Stewart / DNMR: rigorous breakdown exists

**Disconzi, Hoang, Radosz, Breakdown of smooth solutions to the Müller--Israel--Stewart equations of relativistic viscous fluids, Lett. Math. Phys. 113, 55 (2023).**  
https://doi.org/10.1007/s11005-023-01677-9  
Preprint: https://arxiv.org/abs/2008.03841

For a bulk-viscous MIS-type system in four-dimensional Minkowski space there is a class of smooth localized perturbations of constant states whose unique Cauchy solutions break down in finite time: a singularity develops or the solution becomes unphysical in the paper's precise sense. This already refutes any model-independent thesis that causality + relativity + viscosity implies global smoothness.

**Bemfica, Finite-time gradient blow-up and shock formation in Israel-Stewart theory: Bulk, shear, and diffusion regimes, Phys. Rev. E 112, 065105 (2025).**  
https://doi.org/10.1103/blhw-xplr

For simplified (1+1)-dimensional plane-symmetric Israel--Stewart systems, the paper proves existence of smooth initial data leading to finite-time gradient blow-up/shocks in separate pure bulk, shear and diffusion regimes, with numerical bulk-viscous shock checks. The scope is intentionally reduced; full coupled (3+1) Israel--Stewart remains a different problem.

## Large-gradient causal modifications

**Gavassino, Extending Israel--Stewart theory: Causal bulk viscosity at large gradients, Phys. Rev. D 111, 083014 (2025).**  
https://doi.org/10.1103/PhysRevD.111.083014

Constructs bulk-viscous models that reduce to Israel--Stewart at small viscous stress but adjust at large stress so that the equations remain symmetric hyperbolic and causal throughout the thermodynamic state space along (C^1) flows, with an exact second law. The paper explicitly qualifies this as behavior “away from singularities”; it does not prove global smoothness. This is nevertheless a concrete candidate for testing whether better far-from-equilibrium constitutive physics changes breakdown.

## OpenAI inputs

**OpenAI, Finite Time Blowup for Navier--Stokes (2026).**  
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf  
Formalization: https://github.com/openai/NavierStokesAndEuler

The released theorem is forced: for every positive viscosity it constructs smooth data and smooth forcing giving Clay breakdown alternatives on (mathbb R^3) and the torus. The formalization metadata reports the main results with no `sorry`, but labels review status self-assessed. This result is a concrete collapse mechanism and hostile control for regularity criteria; it is not this repository's unforced `NS-R3` theorem.

**OpenAI math family 362, Global classical solutions of the three-dimensional relativistic Vlasov--Maxwell system (2026).**  
https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a  
Independent intake: https://github.com/itpplasma/vlasov-maxwell

The archived manuscript claims arbitrary-large-data global classical regularity in its stated one-species collisionless class. The sibling ITP repository is independently reconstructing the proof; do not import the headline as accepted evidence here. The reusable strategy is source-scoped: an absolute retarded-force estimate loses `sqrt(w)`, and a signed causal calculation is designed to produce the compensating `w^(-1/2)` factor before a separate bootstrap closure.

## Status conclusion

As of this source screen:

- there is **no model-independent relativistic healing theorem**;
- there is rigorous relativistic viscous breakdown in MIS/DNMR-type models;
- there is no located theorem deciding arbitrary smooth large (3+1) BDNK data;
- BDNK numerics contain both apparent singularity formation (outside first-order validity) and shock regularization (inside a frame-robust small-Knudsen regime);
- the physically sharp question is therefore whether breakdown persists **inside a controlled constitutive regime**, and whether a microscopic kinetic model continues smoothly when a fluid closure fails.

Novelty claims require a fresh search at the time of submission.
