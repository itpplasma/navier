#!/usr/bin/env python3
"""Exact carrier algebra for the routed first-generation three-pulse gate.

This checks the finite Leray-symbol geometry used by the accompanying R3
short-time realization theorem.  It does not check the continuum packet
limit, Navier--Stokes local theory, or a multi-generation turnover.
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
import argparse
import sympy as sp

CHECKS=[]

def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def zero(x):
    if isinstance(x,sp.MatrixBase): return all(sp.simplify(v)==0 for v in x)
    return sp.simplify(x)==0

def V(*xs): return sp.Matrix([sp.Rational(x) for x in xs])

def proj(k,v): return sp.simplify(v-k*k.dot(v)/k.dot(k))

def pair(p,a,q,b):
    k=p+q
    if zero(k): return sp.zeros(3,1)
    return sp.simplify(proj(k,a.dot(q)*b+b.dot(p)*a))

k1,k2,k3=V(1,0,0),V(1,1,0),V(1,0,1)
a1=V(0,1,sp.Rational(1,2))
a2=V(1,-1,sp.Rational(-2,3))
a3=V(1,0,-1)

EXPECTED={
    'site13_difference':(k1-k3,V(sp.Rational(-1,2),1,0)),
    'site13_sum':(k1+k3,V(sp.Rational(1,10),1,sp.Rational(-1,5))),
    'site12_selected':(-k1-k2,V(sp.Rational(-1,5),sp.Rational(2,5),sp.Rational(1,6))),
    'site12_sibling':(k1-k2,V(-1,0,sp.Rational(7,6))),
    'unused23_sum':(k2+k3,V(sp.Rational(10,9),sp.Rational(-10,9),sp.Rational(-10,9))),
    'unused23_difference':(k2-k3,V(sp.Rational(2,3),sp.Rational(-2,3),sp.Rational(-2,3))),
}

def main(output=None):
    for j,(k,a) in enumerate(((k1,a1),(k2,a2),(k3,a3)),1):
        check(zero(k.dot(a)),f'input transversality {j}')
    actual={
      'site13_difference':pair(k1,a1,-k3,a3),
      'site13_sum':pair(k1,a1,k3,a3),
      'site12_selected':pair(-k1,a1,-k2,a2),
      'site12_sibling':pair(k1,a1,-k2,a2),
      'unused23_sum':pair(k2,a2,k3,a3),
      'unused23_difference':pair(k2,a2,-k3,a3),
    }
    for name,(k,v) in EXPECTED.items():
        check(actual[name]==v,f'exact coefficient {name}')
        check(zero(k.dot(v)),f'output transversality {name}')
        check(not zero(v),f'nonzero output {name}')

    modes=[]
    for i,(k,a) in enumerate(((k1,a1),(k2,a2),(k3,a3))):
        for sign in (-1,1): modes.append((sign*k,a,(i,sign)))
    outputs={}
    for left,right in itertools.combinations(modes,2):
        p,a,_=left; q,b,_=right; k=p+q
        if zero(k): continue
        v=pair(p,a,q,b)
        if zero(v): continue
        key=tuple(int(x) for x in k)
        outputs[key]=sp.simplify(outputs.get(key,sp.zeros(3,1))+v)
    check(len(outputs)==12,'complete co-located first source has twelve nonzero centers')
    mind2=None
    for p,q in itertools.combinations(outputs,2):
        d2=sum((sp.Integer(p[j])-q[j])**2 for j in range(3))
        mind2=d2 if mind2 is None or d2<mind2 else mind2
    check(mind2==1,'minimum squared separation between distinct output centers is one')
    check((2,1,1) in outputs and (0,1,-1) in outputs,
          'unused k2-k3 collision is genuinely present when co-located')

    # The two routed sites share no leading physical-space product when their
    # translates are disjoint; this is a continuum statement proved in the note.
    # The exact finite check records the carrier allocation only.
    site13={(1,1),(3,1),(3,-1)}
    site12={(1,1),(2,1),(1,-1),(2,-1)}
    check((2,1) not in site13 and (3,1) not in site12,'unused parent pair is split across sites')

    selected={tuple(int(x) for x in EXPECTED[n][0]) for n in
              ('site13_difference','site13_sum','site12_selected')}
    sibling=tuple(int(x) for x in EXPECTED['site12_sibling'][0])
    check(sibling not in selected,'mandatory site12 sibling is not relabelled selected')

    result={
      'status':'PASS_EXACT_CARRIER_ALGEBRA',
      'exact_assertions':len(CHECKS),
      'selected_centers':[list(k) for k in sorted(selected)],
      'mandatory_sibling':list(sibling),
      'co_located_nonzero_centers':[list(k) for k in sorted(outputs)],
      'minimum_squared_output_center_separation':str(mind2),
      'coefficients':{name:{'k':[str(x) for x in EXPECTED[name][0]],
                            'a':[str(x) for x in actual[name]]}
                      for name in EXPECTED},
      'scope':'Finite exact Leray-symbol geometry only; continuum routed packet theorem is in the evidence note.'
    }
    text=json.dumps(result,indent=2)+'\n'; print(text,end='')
    if output:
        output.parent.mkdir(parents=True,exist_ok=True); output.write_text(text)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',type=Path)
    main(p.parse_args().json)
