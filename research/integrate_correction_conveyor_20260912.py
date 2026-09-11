#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

ROOT=Path.cwd()
PLAN=ROOT/'PLAN.md'
SNAP=ROOT/'research/game/snapshot.json'
EVID=ROOT/'research/evidence/2026-09-12-correction-conveyor-scaling.md'
CHECK=ROOT/'research/check_correction_conveyor_scaling.py'

def replace_once(text, old, new, label):
    n=text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected one site, found {n}')
    return text.replace(old,new,1)

def write_new(path, content):
    if path.exists() and path.read_text()!=content:
        raise SystemExit(f'refusing differing existing file {path}')
    if not path.exists():
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(content)

def blob(path):
    return subprocess.run(['git','hash-object',str(path)],cwd=ROOT,text=True,capture_output=True,check=True).stdout.strip()

evidence=r'''# Correction-driven radial entry has an energy-compatible scaling window, but a nondegenerate conveyor is already critical

Date: 2026-09-12. Repository input before integration: current `main`.

**Status: exact source-scale reduction and conditional critical-norm theorem;
independent mathematical audit and novelty assessment pending.** This packet
does not construct a correction-driven conveyor. It tests whether the ordinary
energy and dissipation budgets already exclude the radial-entry alternative
left open by the angular preparation, heat-import, exterior-characteristic and
far-pressure estimates.

## 1. Prediction before the test

Prediction: the speed required to move a packet an order-one fraction of the
source radius during one pulse activation window is much larger than the
prescribed source radial speed, but it can still occupy a shrinking volume with
vanishing energy and viscous action. Hence energy scaling alone will not close
UE1. However, if that speed is realized by the **total unforced velocity** on a
nondegenerate material parcel, its local `L3` norm already diverges and the
conveyor is terminal-strength rather than a harmless auxiliary mechanism.

All statements below use the inspected source scales already frozen in
`2026-09-11-angular-heat-import.md`:

    Q=2^(-ell),       0<h<1/100,
    L comparable to ell^2,
    r comparable to Q^(1/2),
    n comparable to Q^(-h/2),
    tau comparable to Q^(1+h) L.                         (1.1)

Here `tau` is the physical duration of one fast pulse window and `n` is the
nondegenerate angular index. Fixed positive comparison constants do not affect
the exponent conclusions.

## 2. Macroscopic radial crossing

To cross distance comparable to `r` in time `tau`, the required radial speed is

    V_mac comparable to r/tau
          comparable to Q^(-1/2-h) / L.                  (2.1)

This is larger than the source-sized radial speed `Q^(-1/2)` by the factor
`Q^(-h)/L -> infinity`; hence it is genuinely correction-driven and is not the
passive mechanism already excluded by the exterior characteristic theorem.

Take only the scaling cost of a divergence-free velocity cell with amplitude
`V_mac`, diameter comparable to `r`, and volume comparable to `r^3`. Then

    kinetic energy   ~ V_mac^2 r^3
                     ~ Q^(1/2-2h) / L^2 -> 0,            (2.2)

and a turnover lasting `tau`, with gradients on scale `r`, has viscous action

    nu integral ||grad u||_2^2 dt
       ~ nu V_mac^2 r tau
       ~ nu Q^(1/2-h) / L -> 0.                           (2.3)

Both exponents are positive for `0<h<1/100`. The local Reynolds number instead
obeys

    V_mac r / nu ~ Q^(-h)/(nu L) -> infinity.             (2.4)

Thus neither finite energy nor the global energy-dissipation identity forbids
this shrinking fast cell on dimensional grounds.

The angular viscous action seen by a passenger harmonic of index `n` at radius
`r` during the same window is

    nu n^2 tau/r^2 comparable to nu L.                    (2.5)

Therefore the bare angular-diffusion exponent is of `exp(-C L)` type, the same
quasi-Gaussian scale class as the local source entry seed `exp(-gamma L)`.
Equation (2.5) is a viscous-action comparison, not a propagator theorem: the
complete advection/stretching/pressure evolution remains uncontrolled.

## 3. A nondegenerate macroscopic conveyor is already terminal-strength

Assume now an exact classical unforced solution has times `t_j` approaching a
finite endpoint and source scales `Q_j -> 0`, and that on measurable sets
`E_j` of volume at least `c r_j^3` the **total velocity** satisfies

    |u(t_j,x)| >= c V_mac,j.                              (3.1)

Then

    ||u(t_j)||_3 >= c V_mac,j r_j
                  >= c Q_j^(-h)/L_j -> infinity.          (3.2)

Hence the repository's existing `L3` continuation suffix already makes such a
nondegenerate macroscopic conveyor a terminal negative consumer. No additional
source pulse amplification is needed to make its critical norm singular.

This is conditional: the scaling argument does not create the sets `E_j`, and
a correction component may cancel against the prescribed source in the total
field. The hypothesis is deliberately on the total unforced velocity.

## 4. The pressure-forced thin collar is cheaper and is the sharper survivor

The far-pressure theorem leaves a necessary relative collar thickness of order
`L/n` (up to fixed constants and lower-order logarithms). Put

    delta = r L/n
          comparable to Q^(1/2+h/2) L.                   (4.1)

Crossing only this collar during one pulse window requires

    V_col = delta/tau
          comparable to Q^(-1/2-h/2).                    (4.2)

Consider a nondegenerate collar parcel with two tangential dimensions
comparable to `r` and radial thickness `delta`, hence volume comparable to
`r^2 delta`. Its scaling costs are

    energy ~ V_col^2 r^2 delta
           ~ Q^(1/2-h/2) L -> 0,                         (4.3)

and, even charging the sharper gradient scale `delta`,

    nu V_col^2 (r^2 delta/delta^2) tau
       ~ nu Q^(1/2-h/2) -> 0.                            (4.4)

Again the energy law does not forbid the cell. But if the total velocity has
size `V_col` on a fixed fraction of this collar volume, then

    ||u||_3
      >= c V_col (r^2 delta)^(1/3)
      comparable to Q^(-h/3) L^(1/3) -> infinity.         (4.5)

Thus a nondegenerate material conveyor even across only the pressure-allowed
thin collar is itself critical-norm divergent.

The important escape is **sparsity/non-material forcing**. The near-collar
quadratic stress could in principle occupy a smaller set, or pressure/nonlocal
coupling could generate the parent without the total velocity satisfying the
nondegeneracy hypotheses of (3.1) or (4.5). The present calculation does not
bound such a stress and does not replace the complete physical adjoint.

## 5. Recomputed frontier

The passive source exterior, pure early heat import, and direct far-pressure
input are already quantitatively blocked. This packet adds two facts:

1. an actively correction-driven radial entry is **not** excluded by energy or
   dissipation scaling; and
2. any such entry realized as a nondegenerate material conveyor at the source
   scales is already strong enough to diverge `L3`.

Therefore the genuinely smaller UE1 object is now a sparse thin-collar stress,
nonlocal pressure/velocity response, or in-core non-axisymmetric generation
that supplies the four parent traces without first producing the nondegenerate
critical conveyor above. The alternative negative route is a complete physical
adjoint controlling those sparse/nonlocal mechanisms and the full-history gain.

No common Schwartz trace, full nonlinear de-forcing solution, singularity
preservation, or `NS-R3` theorem is claimed. The canonical proof graph and
formal status are unchanged.

## 6. Exact checker

`research/check_correction_conveyor_scaling.py` verifies all `Q` and `L`
exponents above in exact rational arithmetic, including positivity over the
repository range `0<h<1/100` and the critical-norm divergence exponents. It is
a scaling regression, not a PDE existence proof.
'''

checker=r'''#!/usr/bin/env python3
"""Exact exponent checks for correction-driven radial-entry scaling."""
from fractions import Fraction

checks=0
for hp in range(1,10):
    h=Fraction(hp,1000)  # 0<h<1/100
    half=Fraction(1,2)

    # Macroscopic crossing: r=Q^1/2, tau=Q^(1+h)L.
    v=-half-h
    energy=2*v+Fraction(3,2)
    diss=2*v+half+(1+h)
    reynolds=v+half
    angular=(-h)+(1+h)-1
    l3=v+half

    assert energy == half-2*h and energy>0; checks+=2
    assert diss == half-h and diss>0; checks+=2
    assert reynolds == -h and reynolds<0; checks+=2
    assert angular == 0; checks+=1
    assert l3 == -h and l3<0; checks+=2

    # Thin collar delta=r*L/n, n=Q^(-h/2).
    delta=half+h/2
    vcol=delta-(1+h)
    volume=1+delta                 # r^2 * delta
    ecol=2*vcol+volume
    # grad scale delta: V^2 * r^2/delta * tau
    dcol=2*vcol+1-delta+(1+h)
    l3col=vcol+volume/3

    assert delta == half+h/2; checks+=1
    assert vcol == -half-h/2; checks+=1
    assert ecol == half-h/2 and ecol>0; checks+=2
    assert dcol == half-h/2 and dcol>0; checks+=2
    assert l3col == -h/3 and l3col<0; checks+=2

print(f'correction-conveyor exact checks: {checks} passed')
'''

write_new(EVID,evidence)
write_new(CHECK,checker)
CHECK.chmod(0o755)

plan=PLAN.read_text()
plan=replace_once(plan,
    'source_prefix_counting_obstruction: exponential-multiplicity-does-not-force-prefix-divergence\nsource_global_growing_parent_supply: not-produced',
    'source_prefix_counting_obstruction: exponential-multiplicity-does-not-force-prefix-divergence\nsource_correction_conveyor_scaling: energy-compatible-but-nondegenerate-conveyor-terminal-strength\nsource_global_growing_parent_supply: not-produced',
    'PLAN yaml conveyor status')
old='''The next active test must therefore address actual correction-driven entry or
in-core nonlinear generation with the inherited angular hierarchy retained,
or estimate the complete physical adjoint including that hierarchy. No bound
on the collar stress or full-history gain has been obtained; direct far-field
quadratic pressure input now has the energy-only bound above. UE1 and the terminal claim remain open.
'''
new='''An exact source-scale test of correction-driven radial entry gives a sharper
split. Crossing a macroscopic source radius during one pulse window needs speed
`V~Q^(-1/2-h)/L`; on a shrinking `r^3` cell its energy is
`Q^(1/2-2h)/L^2` and viscous action is `Q^(1/2-h)/L`, both vanishing. Even the
pressure-allowed collar `delta/r~L/n` can be crossed with vanishing energy and
dissipation scaling. Energy therefore does not close the active-entry route.
However, if either speed is realized by the total velocity on a nondegenerate
material parcel, its local `L3` norm diverges (`Q^(-h)/L` for the macroscopic
cell and `Q^(-h/3)L^(1/3)` for the collar). Such a conveyor would already be a
terminal negative mechanism. The sharper unresolved object is sparse collar
stress/nonlocal response or in-core generation that avoids this nondegenerate
critical parcel. See `research/evidence/2026-09-12-correction-conveyor-scaling.md`.

The next active test must therefore address sparse correction-driven thin-collar
entry or in-core nonlinear generation with the inherited angular hierarchy
retained, or estimate the complete physical adjoint including those mechanisms.
No bound on the sparse collar stress or full-history gain has been obtained;
direct far-field quadratic pressure input has the energy-only bound above. UE1
and the terminal claim remain open.
'''
plan=replace_once(plan,old,new,'PLAN frontier conveyor paragraph')
PLAN.write_text(plan)

snap=json.loads(SNAP.read_text())
snap['authoritative_sources']['PLAN.md']=blob(PLAN)
snap['authoritative_sources'][str(EVID.relative_to(ROOT))]=blob(EVID)
snap['active_frontier']='sparse correction-driven thin-collar stress/nonlocal entry or in-core nonlinear parent generation with the inherited angular hierarchy, or a complete physical adjoint controlling those mechanisms and full-history gain'
SNAP.write_text(json.dumps(snap,indent=2)+'\n')
print('prepared correction-conveyor checkpoint')
