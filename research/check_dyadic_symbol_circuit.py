#!/usr/bin/env python3
"""Exact Leray-symbol checks for the three-pulse dyadic circuit.

Pure SymPy rational algebra. This is a principal-symbol/circuit certificate,
not a Navier--Stokes trajectory, localized packet construction, or blowup proof.
"""
from __future__ import annotations
import json
from pathlib import Path
import argparse
import sympy as sp

CHECKS=[]

def check(ok, label):
    if not bool(ok):
        raise AssertionError(label)
    CHECKS.append(label)

def zero(x):
    if isinstance(x, sp.MatrixBase):
        return all(sp.simplify(v)==0 for v in x)
    return sp.simplify(x)==0

def V(x,y,z):
    return sp.Matrix([sp.Rational(x),sp.Rational(y),sp.Rational(z)])

def proj(k,v):
    return sp.simplify(v-k*(k.dot(v)/k.dot(k)))

def leray_pair(p,a,q,b):
    """Symmetric real Leray pair, omitting the common Fourier factor -i."""
    k=p+q
    if zero(k):
        raise ValueError("zero output wavevector")
    return sp.simplify(proj(k,(a.dot(q))*b+(b.dot(p))*a))

def gate(K,A):
    k1,k2,k3=K; a1,a2,a3=A
    return (
        [-k1-k2, k1-k3, k1+k3],
        [leray_pair(-k1,a1,-k2,a2),
         leray_pair(k1,a1,-k3,a3),
         leray_pair(k1,a1,k3,a3)]
    )

def selected_circuit():
    k1,k2,k3=V(1,0,0),V(1,1,0),V(1,0,1)
    a1=V(0,1,sp.Rational(1,2))
    a2=V(1,-1,sp.Rational(-2,3))
    a3=V(1,0,-1)
    K=[k1,k2,k3]; A=[a1,a2,a3]
    for j,(k,a) in enumerate(zip(K,A),1):
        check(zero(k.dot(a)),f"input transversality {j}")
    check(sp.Matrix.hstack(*K).det()!=0,"three input wavevectors genuinely span R3")

    T=sp.Matrix([[-1,-1,0],[1,0,-1],[1,0,1]])
    check(T**3==2*sp.eye(3),"signed wavevector gate cubes to exact doubling")

    expected=[
      ([V(-2,-1,0),V(0,0,-1),V(2,0,1)],
       [V(sp.Rational(-1,5),sp.Rational(2,5),sp.Rational(1,6)),
        V(sp.Rational(-1,2),1,0),
        V(sp.Rational(1,10),1,sp.Rational(-1,5))]),
      ([V(2,1,1),V(-4,-1,-1),V(0,-1,1)],
       [V(sp.Rational(-1,12),sp.Rational(1,6),0),
        V(sp.Rational(5,36),sp.Rational(-5,18),sp.Rational(-5,18)),
        V(sp.Rational(13,60),sp.Rational(-13,30),sp.Rational(-13,30))]),
      ([2*k1,2*k2,2*k3],
       [sp.Rational(5,54)*a1,
        sp.Rational(13,120)*a2,
        sp.Rational(-13,360)*a3])
    ]
    generations=[]
    for gen in range(3):
        K,A=gate(K,A)
        eK,eA=expected[gen]
        for j in range(3):
            check(K[j]==eK[j],f"generation {gen+1} wavevector {j+1}")
            check(A[j]==eA[j],f"generation {gen+1} polarization {j+1}")
            check(zero(K[j].dot(A[j])),f"generation {gen+1} transversality {j+1}")
        generations.append({
            "K":[list(map(str,k)) for k in K],
            "A":[list(map(str,a)) for a in A],
        })

    d1,d2,d3=sp.Rational(5,54),sp.Rational(13,120),sp.Rational(13,360)
    C=sp.simplify(d1**4*d2**2*d3**2)
    check(C==sp.Rational(28561,25389989167104),"exact three-gate projective circuit constant")

    alpha=sp.symbols("alpha", positive=True, real=True)
    z=[sp.I*alpha*d1,sp.I*alpha*d2,sp.I*alpha*d3]
    def sg(z):
        z1,z2,z3=z
        return [
          -sp.I*sp.conjugate(z1)*sp.conjugate(z2),
          -sp.I*z1*sp.conjugate(z3),
          -sp.I*z1*z3,
        ]
    for _ in range(3):
        z=list(map(sp.simplify,sg(z)))
    check(z[0]==sp.I*C*alpha**8,"complex phase recurrence component 1")
    check(z[1]==sp.I*C*alpha**8,"complex phase recurrence component 2")
    check(z[2]==-sp.I*C*alpha**8,"complex phase recurrence component 3")
    gains=[
      sp.simplify(z[0]*d1/(sp.I*alpha*d1)),
      sp.simplify(z[1]*d2/(sp.I*alpha*d2)),
      sp.simplify(z[2]*(-d3)/(sp.I*alpha*d3)),
    ]
    check(all(sp.simplify(g-C*alpha**7)==0 for g in gains),
          "all three physical outputs have common gain C alpha^7")
    target=sp.Rational(5,2)
    alpha7=sp.simplify(target/C)
    check(alpha7==sp.Rational(63474972917760,28561),"canonical gain exact alpha^7")
    check(target>2 and target**2<8,"gain 5/2 lies strictly inside half-scale energy window")
    check(sp.simplify(target**2/8)==sp.Rational(25,32),"localized half-scale energy ratio")
    check(sp.simplify(target/2)==sp.Rational(5,4),"critical L3/Reynolds gain ratio")
    return {
      "T":[list(map(int,T.row(i))) for i in range(3)],
      "generations":generations,
      "projective_multipliers":[str(d1),str(d2),str(-d3)],
      "circuit_constant":str(C),
      "gain_formula":"C*alpha^7",
      "canonical_gain":"5/2",
      "canonical_alpha7":str(alpha7),
      "canonical_alpha_float":float(sp.N(alpha7**sp.Rational(1,7),16)),
    }, (K,A), ([k1,k2,k3],[a1,a2,a3])

def all_first_outputs(K,A):
    modes=[]
    for k,a in zip(K,A):
        modes.append((k,a))
        modes.append((-k,a))
    out={}
    for i in range(len(modes)):
        p,a=modes[i]
        for j in range(i+1,len(modes)):
            q,b=modes[j]
            if zero(p+q):
                continue
            v=leray_pair(p,a,q,b)
            if zero(v):
                continue
            key=tuple(sp.simplify(x) for x in p+q)
            out[key]=sp.simplify(out.get(key,sp.zeros(3,1))+v)
    expected={
      (-2,-1,-1):V(sp.Rational(-10,9),sp.Rational(10,9),sp.Rational(10,9)),
      (-2,-1,0):V(sp.Rational(-1,5),sp.Rational(2,5),sp.Rational(1,6)),
      (-2,0,-1):V(sp.Rational(-1,10),-1,sp.Rational(1,5)),
      (0,-1,0):V(-1,0,sp.Rational(7,6)),
      (0,-1,1):V(sp.Rational(-2,3),sp.Rational(2,3),sp.Rational(2,3)),
      (0,0,-1):V(sp.Rational(-1,2),1,0),
      (0,0,1):V(sp.Rational(1,2),-1,0),
      (0,1,-1):V(sp.Rational(2,3),sp.Rational(-2,3),sp.Rational(-2,3)),
      (0,1,0):V(1,0,sp.Rational(-7,6)),
      (2,0,1):V(sp.Rational(1,10),1,sp.Rational(-1,5)),
      (2,1,0):V(sp.Rational(1,5),sp.Rational(-2,5),sp.Rational(-1,6)),
      (2,1,1):V(sp.Rational(10,9),sp.Rational(-10,9),sp.Rational(-10,9)),
    }
    check(set(out)==set(expected),"complete first-generation support including siblings")
    for k,v in expected.items():
        check(out[k]==v,f"first-generation exact output {k}")
        check(zero(sp.Matrix(k).dot(v)),f"first-generation output transverse {k}")
    selected={(-2,-1,0),(0,0,-1),(0,0,1),(2,0,1),(2,1,0)}
    unwanted=set(out)-selected
    check((0,1,0) in unwanted and (0,-1,0) in unwanted,
          "k1-k2 sibling is genuinely nonzero")
    check((2,1,1) in unwanted and (-2,-1,-1) in unwanted,
          "unused k2-k3 collision is genuinely nonzero")
    return {
      "all_outputs":{"%s"% (k,):list(map(str,v)) for k,v in sorted(out.items())},
      "selected_or_conjugate":[str(k) for k in sorted(selected)],
      "unwanted":[str(k) for k in sorted(unwanted)],
    }

def two_parent_wall():
    t,R,z,w=sp.symbols("t R z w", real=True)
    c=(1-t**2)/(1+t**2); s=2*t/(1+t**2)
    p=sp.Matrix([1,0,0]); q=R*sp.Matrix([c,s,0])
    a=sp.Matrix([0,1,z]); b=sp.Matrix([-s,c,w])
    e=leray_pair(p,a,q,b); f=leray_pair(p,a,-q,b)
    E=leray_pair(p+q,e,p-q,f)
    F=leray_pair(p+q,e,q-p,f)
    CE=sp.factor(E.cross(a)[0])
    CF2=sp.factor(F.cross(b)[1])
    L1=t**2*w+t**2*z+w-z
    L2=t**2*w+t**2*z-w+z
    q1=sp.factor(CE/L1); q2=sp.factor(CF2/L2)
    check(sp.simplify(CE-q1*L1)==0,"two-parent first orientation residual factor")
    check(sp.simplify(CF2-q2*L2)==0,"two-parent second orientation residual factor")
    det=sp.det(sp.Matrix([[1+t**2,t**2-1],[t**2-1,1+t**2]]))
    check(sp.factor(det)==4*t**2,"two-parent polarization system determinant")
    check(zero(E.subs(R,1)) and zero(F.subs(R,1)),
          "equal-length two-parent second generation vanishes")
    return {
      "orientation_linear_factors":[str(L1),str(L2)],
      "determinant":str(sp.factor(det)),
      "scope":"For noncollinear t!=0 and unequal lengths R!=1, exact projective recurrence forces z=w=0; R=1 gives zero second generation.",
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    circuit,_,initial=selected_circuit()
    siblings=all_first_outputs(*initial)
    wall=two_parent_wall()
    result={
      "status":"Exact original Leray-symbol circuit only; no time-evolution/localization/blowup certificate.",
      "exact_assertion_count":len(CHECKS),
      "circuit":circuit,
      "first_generation":siblings,
      "two_parent_wall":wall,
    }
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(f"PASS: {len(CHECKS)} exact symbolic assertions.")
    print(result["status"])

if __name__=="__main__":
    main()
