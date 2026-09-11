#!/usr/bin/env python3
"""Exact all-orders effective Raman-lattice certificate.

Five state-triggered Raman modules synthesize the common inheritance filter H.
Their three distinct low shifts form a pointed semigroup.  Every repeated
translation of the tracked finite slow carriers and the complete inherited
ladder is either one of the five intended first h0 outputs or is strictly
damped by H at M=2048.  Repeated translated states do not collide with the
clean-target or intended-purifier windows.

This is a theorem for the leading high-frequency effective slow Raman operator,
not yet a full original-NS elimination/realization theorem.
"""
from __future__ import annotations
import itertools
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625); mid=(lo+hi)/2
check(Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1,
      'unique positive clean root isolated')

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
H200=((142,-200,147),(-200,-143,56),(147,56,1))
check(H==H.T and sp.trace(H)==0,'inheritance filter symmetric trace free')
fro2=sp.factor(sum(H[i,j]**2 for i in range(3) for j in range(3)))
check(fro2==sp.Rational(21263,5000),'exact Frobenius norm squared')
check(fro2<sp.Rational(33,16)**2,'operator norm bounded by 33/16')

# Actual ancestry-contaminated middle target coefficient, common -i phase removed.
pure=sp.Matrix([
 2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
 2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
 2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
])
other=sp.Matrix([
 (5*z**10-32*z**9+89*z**8-120*z**7+67*z**6-12*z**5+159*z**4-396*z**3+412*z**2-176*z+20)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 (4*z**7-31*z**6+85*z**5-132*z**4+89*z**3-3*z**2-42*z+10)/(3*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 (5*z**11-42*z**10+145*z**9-204*z**8-151*z**7+1108*z**6-1901*z**5+1324*z**4+374*z**3-1326*z**2+872*z-140)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
])
a=sp.Matrix([sp.cancel(x) for x in pure+other])
h=sp.Matrix([z-2,-1,-1])
check(sp.simplify(h.dot(a))==0,'actual contaminated trigger transverse')
dens=[sp.denom(x) for x in a]
D=dens[0]
for dd in dens[1:]: D=sp.lcm(D,dd)
A=sp.Matrix([sp.expand(sp.cancel(D*x)) for x in a])
check(sp.factor(h.dot(A))==0,'cleared trigger transverse')

# All-orders-safe basis.  Modules 2/3 share one low shift and modules 4/5
# share another, leaving only three distinct shifts in the slow semigroup.
GEOM=[
 ((-3,-3, 1),(1,-2,-3)),
 ((-3,-2, 2),(0, 1, 1)),
 ((-3,-2, 2),(2,-3, 0)),
 ((-2,-3, 2),(0, 2, 3)),
 ((-2,-3, 2),(1,-2,-2)),
]
SHIFTS=[(-3,-3,1),(-3,-2,2),(-2,-3,2)]

# Direct high-high silence and exact span at the clean algebraic root.
cols=[]
N=sp.symbols('N',positive=True)
for j,(lt,qt) in enumerate(GEOM):
    l=sp.Matrix(lt); Q=sp.Matrix(qt); m=Q.cross(l)
    check(l.dot(Q)==0,f'module {j}: l.Q=0')
    l2=l.dot(l); q2=Q.dot(Q)
    q=l/2+N*Q; r=l/2-N*Q
    beta=l-(l2/(2*N*q2))*Q+m
    eps=l+(l2/(2*N*q2))*Q-m
    check(sp.simplify(q.dot(beta))==0,f'module {j}: q.beta=0')
    check(sp.simplify(r.dot(eps))==0,f'module {j}: r.eps=0')
    direct=sp.simplify((beta.dot(r))*eps+(eps.dot(q))*beta)
    check(sp.simplify(direct-2*l2*l)==sp.zeros(3,1),
          f'module {j}: direct high-high source is longitudinal')

    kappa=h+l
    W=sp.expand(2*(A.dot(Q))*((l.dot(kappa))*l-(m.dot(kappa))*m))
    k2=sp.expand(kappa.dot(kappa))
    d=sp.expand(k2*W-kappa*(kappa.dot(W)))
    check(sp.expand(kappa.dot(d))==0,f'module {j}: triggered output transverse')
    S=(d*kappa.T+kappa*d.T)/2
    check(sp.expand(sp.trace(S))==0,f'module {j}: triggered strain trace free')
    cols.append(sp.Matrix([sp.expand(S[0,0]),sp.expand(S[1,1]),
                           sp.expand(S[0,1]),sp.expand(S[0,2]),sp.expand(S[1,2])]))
Span=sp.Matrix.hstack(*cols)
Pdet=sp.Poly(sp.expand(Span.det(method='berkowitz')),z)
check(Pdet.degree()==71,'all-orders basis span determinant degree 71')
check(sp.gcd(Pdet,Qclean).degree()==0,'span determinant coprime to clean return polynomial')
check(Pdet.eval(mid)!=0,'span determinant midpoint calibration nonzero')

# Integer helpers for the exact damping certificate.  For d transverse to k,
# R=-2048(d.H.d)/|d|^2-|k|^2<0 is equivalent to
#   25 |k|^2 |d|^2 + 256 d.H200.d > 0,
# after using H200=200H.  We use the denominator-free Leray vector
#   d=|k|^2 W-k(k.W).
def dot3(u,v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def cross3(u,v): return (u[1]*v[2]-u[2]*v[1],
                         u[2]*v[0]-u[0]*v[2],
                         u[0]*v[1]-u[1]*v[0])
def add3(u,v): return (u[0]+v[0],u[1]+v[1],u[2]+v[2])
def cert_int(k,l,Q):
    ko=add3(k,l); m=cross3(Q,l)
    lk=dot3(l,ko); mk=dot3(m,ko)
    W=(lk*l[0]-mk*m[0],lk*l[1]-mk*m[1],lk*l[2]-mk*m[2])
    k2=dot3(ko,ko); kw=dot3(ko,W)
    d=(k2*W[0]-ko[0]*kw,k2*W[1]-ko[1]*kw,k2*W[2]-ko[2]*kw)
    d2=dot3(d,d)
    if d2==0: return None,k2
    dh=(142*d[0]*d[0]-400*d[0]*d[1]+294*d[0]*d[2]
        -143*d[1]*d[1]+112*d[1]*d[2]+d[2]*d[2])
    return 25*k2*d2+256*dh,k2

# Universal coercive tail.  Since ||H||op<=||H||F<33/16,
# R < 2048*(33/16)-|k|^2 = 4224-|k|^2.
# Every low shift has x component <=-2.  The largest finite seed x coordinate
# is 1+z < 1428/625.  After 34 translations,
# x <= 1428/625-68 = -41072/625, whose square exceeds 4224.
check(sp.Rational(41072,625)**2>4224,'all paths of depth >=34 are universally damped')
# For inherited r_n=(-n,-1,0), n>=63, the first shift gives x<=-65.
check(65**2>4224,'ladder n>=63 universally damped after first translation')

# Enumerate all remaining z-independent semigroup states exactly.
INT_SEEDS=[('p1',(1,0,0)),('p2',(0,1,0)),('g1',(-1,-1,0))]
integer_cases=0
for dep in range(34):
  for n0 in range(dep+1):
    for n1 in range(dep-n0+1):
      n2=dep-n0-n1
      shift=(n0*(-3)+n1*(-3)+n2*(-2),
             n0*(-3)+n1*(-2)+n2*(-3),
             n0*1+n1*2+n2*2)
      for name,k0 in INT_SEEDS:
        kp=add3(k0,shift)
        for j,(l,Q) in enumerate(GEOM):
          C,k2=cert_int(kp,l,Q)
          if k2>=4224 or C is None: continue
          integer_cases+=1
          check(C>0,f'{name} dep={dep} counts={n0,n1,n2} module={j}')
      for nn in range(1,63):
        kp=add3((-nn,-1,0),shift)
        for j,(l,Q) in enumerate(GEOM):
          C,k2=cert_int(kp,l,Q)
          if k2>=4224 or C is None: continue
          integer_cases+=1
          check(C>0,f'r{nn} dep={dep} counts={n0,n1,n2} module={j}')
check(integer_cases==81406,'81406 exact integer damping certificates')

# Fast integer-polynomial arithmetic for the six z-dependent finite seeds.
def padd(a,b):
    out=[0]*max(len(a),len(b))
    for i in range(len(out)):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pscale(a,c): return [c*x for x in a] if c else [0]
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
      if x:
       for j,y in enumerate(b):
        if y: out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pdot(a,b):
    s=[0]
    for x,y in zip(a,b): s=padd(s,pmul(x,y))
    return s
def cert_poly(xc,xs,y0,z0,l,Q):
    k=[[xc,xs],[y0],[z0]]
    ko=[padd(k[i],[l[i]]) for i in range(3)]
    m=cross3(Q,l)
    lk=[0]; mk=[0]
    for i in range(3):
        lk=padd(lk,pscale(ko[i],l[i])); mk=padd(mk,pscale(ko[i],m[i]))
    W=[padd(pscale(lk,l[i]),pscale(mk,-m[i])) for i in range(3)]
    k2=pdot(ko,ko); kw=pdot(ko,W)
    d=[padd(pmul(k2,W[i]),pscale(pmul(ko[i],kw),-1)) for i in range(3)]
    d2=pdot(d,d)
    dh=[0]
    for c,i,j in [(142,0,0),(-400,0,1),(294,0,2),(-143,1,1),(112,1,2),(1,2,2)]:
        dh=padd(dh,pscale(pmul(d[i],d[j]),c))
    return padd(pscale(pmul(k2,d2),25),pscale(dh,256)),d2

ZLO=12847; ZHI=12848; ZDEN=10000
def poly_lower_num(coeffs):
    deg=len(coeffs)-1
    total=0
    for i,c in enumerate(coeffs):
        if not c: continue
        zz=ZLO if c>0 else ZHI
        total += c*(zz**i)*(ZDEN**(deg-i))
    return total

def k2_min_ge_4224(xc,xs,y0,z0,l):
    c=xc+l[0]
    u=c*ZDEN+xs*ZLO; v=c*ZDEN+xs*ZHI
    xmin=0 if min(u,v)<=0<=max(u,v) else min(abs(u),abs(v))
    yz=(y0+l[1])**2+(z0+l[2])**2
    return xmin*xmin+yz*ZDEN**2 >= 4224*ZDEN**2

ZSEEDS={
 'p3':(0,-1,0,1),
 'g2':(1, 1,0,-1),
 'g3':(1,-1,0,1),
 'h+':(0,-1,1,1),
 'h-':(0,-1,-1,1),
 'h0':(-2,1,-1,-1),
}
poly_cases=0
for dep in range(34):
  for n0 in range(dep+1):
    for n1 in range(dep-n0+1):
      n2=dep-n0-n1
      shift=(n0*(-3)+n1*(-3)+n2*(-2),
             n0*(-3)+n1*(-2)+n2*(-3),
             n0*1+n1*2+n2*2)
      for name,(xc,xs,y0,z0) in ZSEEDS.items():
        if dep==0 and name=='h0':
            continue # the five intended first h0 outputs synthesize H
        xc1=xc+shift[0]; y1=y0+shift[1]; z1=z0+shift[2]
        for j,(l,Q) in enumerate(GEOM):
          if k2_min_ge_4224(xc1,xs,y1,z1,l): continue
          C,d2=cert_poly(xc1,xs,y1,z1,l,Q)
          if len(d2)==1 and d2[0]==0: continue
          poly_cases+=1
          check(poly_lower_num(C)>0,
                f'{name} interval dep={dep} counts={n0,n1,n2} module={j}')
check(poly_cases==20747,'20747 exact clean-root interval damping certificates')
check(integer_cases+poly_cases==102153,'102153 finite low-frequency damping certificates')

# All repeated finite translated states are also disjoint from the three
# intended purifier frequencies h+A,h+B,h+C and the three clean target windows.
SEED_FORMS={
 'p1':((0,1),0,0),'p2':((0,0),1,0),'p3':((-1,0),0,1),
 'g1':((0,-1),-1,0),'g2':((1,1),0,-1),'g3':((-1,1),0,1),
 'h+':((-1,0),1,1),'h-':((-1,0),-1,1),'h0':((1,-2),-1,-1),
}
REQ=[]
for nm,l in zip(('A','B','C'),SHIFTS):
    REQ.append((f'pur_{nm}',(1,-2+l[0]),-1+l[1],-1+l[2]))
REQ += [('h+',(-1,0),1,1),('h0',(1,-2),-1,-1),('h-',(-1,0),-1,1)]
collision_checks=0
for dep in range(1,34):
  for n0 in range(dep+1):
    for n1 in range(dep-n0+1):
      n2=dep-n0-n1
      shift=(n0*(-3)+n1*(-3)+n2*(-2),
             n0*(-3)+n1*(-2)+n2*(-3),
             n0*1+n1*2+n2*2)
      for name,((sx,cx),yy,zz) in SEED_FORMS.items():
        if name=='h0' and dep==1: continue
        for rname,(rsx,rcx),ry,rz in REQ:
          collision_checks+=1
          if yy+shift[1]!=ry or zz+shift[2]!=rz: continue
          aa=sx-rsx; bb=cx+shift[0]-rcx
          if aa==0:
              check(bb!=0,f'no exact collision {name} -> {rname}')
          else:
              check(sp.gcd(sp.Poly(aa*z+bb,z),Qclean).degree()==0,
                    f'no clean-root collision {name} -> {rname}')
check(collision_checks==385488,'385488 exact finite required-window collision checks')
# Shifted inherited-ladder x coordinates are rational integers, whereas every
# required window above has x coefficient +/-1 in z.  A collision would make
# the monic integer polynomial Qclean have a rational root in (1.2847,1.2848),
# impossible by the rational-root theorem (its rational roots, if any, are
# integral divisors of 16).
check(lo>1 and hi<2,'clean root interval contains no integer rational root')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Span: five silent high-pair modules synthesize Sym_0(3), hence H, at the clean root.')
print(f'Damping: {integer_cases} integer + {poly_cases} interval = {integer_cases+poly_cases} exact low-frequency certificates; the rest is coercive.')
print(f'Collisions: {collision_checks} exact finite comparisons; no repeated translated state reaches a required window.')
print('Scope: all orders of the leading effective Raman slow lattice only; full NS high-mode elimination/localization remains open.')
