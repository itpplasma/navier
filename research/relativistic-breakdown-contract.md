# RNS-BDNK-F001: forced relativistic singularity after failure of the direct lift

Updated 2026-10-07. Authority: `PLAN.md`. The original unforced NS-R3 target
and its accepted graph are unchanged.

## Forcing-status invariant

The released OpenAI Navier--Stokes finite-time breakdown theorem uses **smooth
forcing**. The classical **unforced** problem is still open. Consequently the
first like-for-like relativistic problem is:

> Does a fixed causal BDNK model admit smooth initial data and a smooth
> covariant source for which the classical solution loses regularity in finite
> time?

The corresponding unforced BDNK problem remains open and is downstream, not a
premise.

## What has already been ruled out

The direct normalized lift of the released shrinking vortex is not an available
answer. The author packet `evidence/bdnk-transfer-20261007.md` gives two
independent obstructions.

**Energy obstruction.** In the weighted-C2 slow-shrinking class

    γ,w ~ τ^(-a),
    Θ ~ τ^(-b),
    0<β_i<1,

the full BDNK energy equation excludes every profile with

    b > -a/κ,
    κ = (4χ0+2λ0)/(4χ0/3+2λ0-4η0/3).

For frame A, κ=25/12. A source that stays smooth/bounded at the target time
cannot cancel the leading dilation mismatch. Thus the noncooling direct lift
fails even **with forcing enabled**.

**Pulse obstruction.** The classical construction uses parabolic
high-frequency damping. Causal BDNK shear is telegraphic: its high-wavenumber
decay rate saturates rather than growing like k^2. Hence the classical
pulse-preparation/damping argument cannot be imported unchanged.

These results say "the released architecture is model-specific," not "smooth
relativistic forcing can never blow up BDNK."

## One active producer

**TARGET.** Construct an actual forced finite-time singular BDNK solution for
one explicit causal conformal frame, or prove an unconditional no-go for a
strictly larger nonempty family of smooth forced collapse profiles.

**FIRST GAP.** Find a relativistic collapse ansatz whose leading conservation
balance is compatible with the full BDNK time-derivative stress and whose source
extends smoothly to the singular time. The source is not allowed to hide the
singularity by becoming unbounded or nonsmooth.

**NATURAL ESCAPES TO TEST.**

1. bounded physical velocity with gradient blow-up rather than diverging proper
   velocity;
2. characteristic/shock scales β_i>=1, outside the previous slow-shrinking
   theorem;
3. a thermal profile at or below the cooling threshold;
4. oscillatory/finer-scale profiles not covered by weighted-C2 convergence;
5. a different smooth source design that uses the causal hyperbolic modes
   rather than relying on heat-semigroup damping.

**CHEAPEST FALSIFIER.** For each candidate, compute the full BDNK residual
before choosing the source. If its leading residual diverges at the target
time, that candidate cannot yield the desired smooth-forcing theorem.

## Retained unforced results

The separate virial hot-core theorem gives, for initially ideal data in strict
causal frames, finite-time **breakdown OR negative laboratory energy**. It does
not select a PDE singularity. A different Euler-prepared family smoothly exits
the positive classical-particle stress cone. Those are meaningful closure
results but do not prove either forced or unforced BDNK blow-up.

Do not merge the data families or promote smooth closure failure to singularity.

## Model-robustness interpretation

If a redesigned forced BDNK singularity is constructed, then the classical
phenomenon survives relativity, though possibly by a different mechanism. If a
broad causal-relativistic no-go ultimately excludes all smooth-forcing
singularities of the relevant type, that would identify a genuine relativistic
regularization mechanism. At present neither outcome is established.

A kinetic comparison requires an actual microscopic parent with a specified
collision operator and controlled closure error; collisionless Vlasov--Maxwell
is not automatically that parent.
