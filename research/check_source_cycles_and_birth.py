#!/usr/bin/env python3
"""Exact finite algebra for source cycles and newborn packet efficiency.

Standard library only. No Fourier-Galerkin dynamics is substituted for NS.
Checks rational finite Fourier polynomials and arithmetic inequalities, NOT
continuum estimates, time remainders, independent review, or global regularity.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
import json
from pathlib import Path

ZERO=(F(0),F(0),F(0)); checks=0

def require(c,m):
 global checks; checks+=1
 if not c: raise AssertionError(m)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def project(k,a):
 kk=dot(k,k)
 if not kk:return ZERO
 c=dot(k,a)/F(kk); return tuple(x-c*y for x,y in zip(a,k))
def scale(a,c): return {k:tuple(c*x for x in v) for k,v in a.items() if c and any(v)}
def total(*fs):
 out=defaultdict(lambda:ZERO)
 for f in fs:
  for k,v in f.items():out[k]=add(out[k],v)
 return {k:v for k,v in out.items() if any(v)}
def convection(a,b):
 out=defaultdict(lambda:ZERO)
 for p,av in a.items():
  for q,bv in b.items():
   k=add(p,q); c=dot(q,av)
   if c and any(k):out[k]=add(out[k],tuple(c*x for x in bv))
 out={k:project(k,v) for k,v in out.items()}
 return {k:v for k,v in out.items() if any(v)}
def energy(a): return sum(dot(v,v) for v in a.values())
def validate(a):
 for k,v in a.items():
  require(dot(k,v)==0,'solenoidality'); require(a.get(neg(k))==neg(v),'real odd symmetry')
def jrot(k): return (F(-k[1]),F(k[0]),F(0))
def two_carrier(p,q):
 pp,qq=dot(p,p),dot(q,q); a={p:tuple(-x/pp for x in jrot(p)),q:tuple(x/qq for x in jrot(q))}; a.update({neg(k):neg(v) for k,v in list(a.items())}); return a
def jets(initial,nu,degree):
 out=[initial]
 for n in range(degree):
  nonlinear=total(*(convection(out[j],out[n-j]) for j in range(n+1)))
  heat={k:tuple(-nu*dot(k,k)*x for x in v) for k,v in out[n].items()}
  out.append(scale(total(nonlinear,heat),F(1,n+1)))
 return out
def independent_planar_source(a):
 c={k:dot(jrot(k),v)/F(dot(k,k)) for k,v in a.items()}; out=defaultdict(F)
 for p,cp in c.items():
  for q,cq in c.items():
   k=add(p,q); kk=dot(k,k)
   if kk:
    omega=p[0]*q[1]-p[1]*q[0]; out[k]+=F(omega*(dot(q,q)-dot(p,p)),2*kk)*cp*cq
 return {k:tuple(x*ck for x in jrot(k)) for k,ck in out.items() if ck}

def main(output=None):
 p,q=(2,0,0),(1,1,0); b=two_carrier(p,q); g=convection(b,b); gg=convection(g,g); copy={tuple(2*x for x in k):v for k,v in b.items()}
 require(gg==scale(copy,F(1,5)),'exact full source cycle'); require(g[(3,1,0)]==(F(-1,20),F(3,20),F(0)),'sum channel'); require(g[(1,-1,0)]==(F(-1,4),F(-1,4),F(0)),'difference channel'); require(energy(b)==F(3,2),'initial energy'); require(energy(g)==F(3,10),'source energy'); require(dot(g[(1,-1,0)],g[(1,-1,0)])==5*dot(g[(3,1,0)],g[(3,1,0)]),'mandatory difference energy')
 j=jets(b,F(0),3); require(j[3][(4,0,0)]==(F(0),F(-4,65),F(0)),'full third jet at 2p'); require(j[3][(2,2,0)]==(F(-1,50),F(1,50),F(0)),'full third jet at 2q'); require(j[3][(7,1,0)]==(F(-11,52000),F(77,52000),F(0)),'comb exterior')
 for nu in [F(1,100),F(1),F(7,3)]:
  jnu=jets(b,nu,3)
  for k in [(4,0,0),(2,2,0),(7,1,0)]:require(jnu[3][k]==j[3][k],'minimal-degree viscosity independence')
  for f in jnu:validate(f)
 candidates=[(x,y,0) for x,y in product(range(-2,3),repeat=2) if x or y]; cases=0
 for p in candidates:
  for q in candidates:
   P,Q,R=dot(p,p),dot(q,q),dot(p,q); omega=p[0]*q[1]-p[1]*q[0]
   if not omega or not R or P==Q:continue
   cases+=1; b=two_carrier(p,q); g=convection(b,b); gg=convection(g,g); require(g==independent_planar_source(b),'independent planar first source'); require(gg==independent_planar_source(g),'independent planar second source'); D=(P+Q)**2-4*R**2; require(D>0,'positive geometric denominator'); coefficient=F(4*omega**3*R*(P-Q)**2,P**2*Q**2*D); copy={tuple(2*x for x in k):v for k,v in b.items()}; require(gg==scale(copy,coefficient),'general source-cycle formula')
   for f in [b,g,gg]:validate(f)
   j=jets(b,F(0),3); sign=1 if R>0 else -1; k=tuple(3*x+sign*y for x,y in zip(p,q)); require(k not in copy,'comb outside copy'); require(k in j[3] and any(j[3][k]),'mandatory full third-jet comb')
 ring={}
 for k in set(permutations((2,1,0))):ring[k]=neg(project(k,(F(1),)*3)); ring[neg(k)]=neg(ring[k])
 g=convection(ring,ring); gg=convection(g,g); forward={k:v for k,v in gg.items() if dot(k,k)>F(320,9)}
 require({dot(k,k) for k in g}=={14,18},'first-ring support'); require({dot(k,k) for k in gg}=={14,50,54,56,62,66},'full second support'); require(len(ring)==12 and len(g)==24 and len(gg)==84 and len(forward)==72,'all source counts')
 E0,E1,E2=energy(ring),energy(g),energy(forward); require(E0==F(72,5),'ring input energy'); require(E1==F(14688,175),'ring first source energy'); require(E2==F(15612389411328,1827546875),'ring forward self-source energy')
 for k in g:require(F(9,16)*20<dot(k,k)<F(9,4)*20,'first source multiplier plateau')
 for k in forward:require(F(9,16)*80<dot(k,k)<F(9,4)*80,'second forward multiplier plateau')
 for f in [ring,g,gg,forward]:validate(f)
 r2=E2*E0**2/(32*E1**3); require(r2==F(125485383,1340266400),'periodic efficiency-ratio squared'); gaussian_fourth=8*r2*r2; require(gaussian_fourth>F(51,100)**4,'Gaussian efficiency >0.51'); require(F(51460,100000)**4<gaussian_fourth<F(51461,100000)**4,'Gaussian ratio interval')
 result={'status':'PASS_EXACT_FINITE_ALGEBRA','assertions':checks,'rational_source_cycle_cases':cases,'E0':str(E0),'E1':str(E1),'E2':str(E2),'periodic_efficiency_ratio_squared':str(r2),'gaussian_efficiency_ratio_interval':['0.51460','0.51461'],'scope_exclusions':['No continuum packet-limit certification','No time-remainder certification','No independent mathematical audit','No turnover theorem or NS-R3 resolution']}; text=json.dumps(result,indent=2)+'\n'; print(text,end='')
 if output:output.parent.mkdir(parents=True,exist_ok=True); output.write_text(text)
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--json',type=Path); main(parser.parse_args().json)
