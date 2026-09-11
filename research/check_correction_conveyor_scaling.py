#!/usr/bin/env python3
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
