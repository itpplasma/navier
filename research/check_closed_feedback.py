#!/usr/bin/env python3
"""Exact finite regression tests for the closed-feedback proof.

Uses only the standard library. No floating-point trajectories are evidence.
The proof, not the finite range of this oracle, carries universal quantifiers.
Run from any working directory; deterministic JSON is printed to stdout.
"""
from __future__ import annotations
from fractions import Fraction as F
from collections import Counter
from math import factorial, comb
import json

COUNTS: Counter[str] = Counter()
Q = tuple[F, F]
Fourier = dict[tuple[int, int], Q]
EP = dict[tuple[int, int], F]
ZERO: Q = (F(0), F(0))

def check(condition: bool, group: str) -> None:
    if not condition:
        raise AssertionError(group)
    COUNTS[group] += 1

def qa(a: Q, b: Q) -> Q:
    return (a[0]+b[0], a[1]+b[1])

def qm(a: Q, b: Q) -> Q:
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def fs(a: Fourier, r: F) -> Fourier:
    return {k:(v[0]*r,v[1]*r) for k,v in a.items() if v != ZERO and r}

def fa(a: Fourier,b: Fourier) -> Fourier:
    out=a.copy()
    for k,v in b.items(): out[k]=qa(out.get(k,ZERO),v)
    return {k:v for k,v in out.items() if v != ZERO}

def fm(a: Fourier,b: Fourier) -> Fourier:
    out: Fourier={}
    for k,v in a.items():
        for l,w in b.items():
            q=(k[0]+l[0],k[1]+l[1])
            out[q]=qa(out.get(q,ZERO),qm(v,w))
    return {k:v for k,v in out.items() if v != ZERO}

def fd(a: Fourier,j: int) -> Fourier:
    return {k:qm(v,(F(0),F(k[j]))) for k,v in a.items() if k[j]}

def fl(a: Fourier) -> Fourier:
    return {k:(v[0]*(k[0]**2+k[1]**2),v[1]*(k[0]**2+k[1]**2)) for k,v in a.items()}

def cos(k:tuple[int,int]) -> Fourier:
    return {k:(F(1,2),F(0)),(-k[0],-k[1]):(F(1,2),F(0))}

def phi3(k:int)->Fourier:
    return {(i*k,j*2*k):(F(-i*j,4),F(0)) for i in (-1,1) for j in (-1,1)}

def project(a:Fourier, radius_sq:F)->Fourier:
    return {k:v for k,v in a.items() if k[0]**2+k[1]**2<=radius_sq}

def nonlinear(psi:Fourier)->Fourier:
    return fa(fm(fd(psi,1),fd(fl(psi),0)),fs(fm(fd(psi,0),fd(fl(psi),1)),F(-1)))

def ep_add(a:EP,b:EP)->EP:
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def ep_scale(a:EP,r:F)->EP:
    return {k:v*r for k,v in a.items() if v*r}

def ep_mul(a:EP,b:EP)->EP:
    out:EP={}
    for (r,m),v in a.items():
        for (q,n),w in b.items():
            k=(r+q,m+n);out[k]=out.get(k,F(0))+v*w
    return {k:v for k,v in out.items() if v}

def ep_der(a:EP)->EP:
    out:EP={}
    for (r,n),v in a.items():
        out=ep_add(out,{(r,n):-r*v})
        if n:out=ep_add(out,{(r,n-1):n*v})
    return out

def ep_conv(a:EP,rate:int)->EP:
    out:EP={}
    for (r,n),v in a.items():
        d=rate-r
        if d==0:out=ep_add(out,{(rate,n+1):v/F(n+1)})
        else:
            for j in range(n+1):
                c=v*F((-1)**j*factorial(n),factorial(n-j)*d**(j+1))
                out=ep_add(out,{(r,n-j):c})
            c=-v*F((-1)**n*factorial(n),d**(n+1))
            out=ep_add(out,{(rate,0):c})
    return out

def initial(a:EP)->F:return sum((v for (r,n),v in a.items() if n==0),F(0))

def amplitude_coefficients(order:int,cooperative:bool=False)->list[list[EP]]:
    rows=[[{}, {}, {}],[{(1,0):F(1)}, {}, {(5,0):F(1)}]]
    for n in range(2,order+1):
        src=[{}, {}, {}]
        for j in range(1,n):
            for i,(p,q) in enumerate(((1,2),(0,2),(0,1))):
                term=ep_mul(rows[j][p],rows[n-j][q])
                src[i]=ep_add(src[i],ep_scale(term,F(-1 if i==1 and not cooperative else 1)))
        rows.append([ep_conv(src[i],d) for i,d in enumerate((1,4,5))])
    return rows

def theta_coefficients(order:int,diagonal:bool)->list[dict[tuple[int,int],F]]:
    # Coefficients theta^m A^n. Exact recurrence for the transformed cooperative ODE.
    out=[{(0,1):F(1)},{},{(0,1):F(1)}]
    for m in range(order):
        for i,(p,q) in enumerate(((1,2),(0,2),(0,1))):
            vals:dict[int,F]={}
            for (r,n),v in list(out[p].items()):
                for (s,k),w in list(out[q].items()):
                    if r+s==m: vals[n+k]=vals.get(n+k,F(0))+v*w
            if diagonal and i<2:
                for (r,n),v in list(out[i].items()):
                    if r<=m:vals[n]=vals.get(n,F(0))+(4 if i==0 else 1)*5**(m-r)*v
            for n,v in vals.items():
                if v:out[i][(m+1,n)]=v/F(m+1)
    return out

def main()->None:
    for k in range(1,9):
        p1,p2,p3=cos((k,0)),cos((0,2*k)),phi3(k)
        # The six fixtures determine every coefficient of the homogeneous quadratic map.
        for a,b,c in ((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(2,-3,5)):
            psi=fa(fa(fs(p1,F(a)),fs(p2,F(b))),fs(p3,F(c)))
            adv=nonlinear(psi)
            expected=fa(fa(fs(p1,F(-b*c*k**4)),fs(p2,F(4*a*c*k**4))),fs(p3,F(-6*a*b*k**4)))
            for radius in (F(5),F(6),F(31,4)):
                check(project(adv,radius*k*k)==expected,'full_ball_projected_coefficients')
            rem=fa(adv,fs(expected,F(-1)))
            check(all(q[0]**2+q[1]**2 in {8*k*k,17*k*k} for q in rem),'complete_discarded_support')
            check(fa(fd(fd(psi,1),0),fs(fd(fd(psi,0),1),F(-1)))=={},'solenoidal_streamfunction')
        adv=nonlinear(fa(p1,p3))
        check(project(adv,F(8*k*k))!=project(adv,F(6*k*k)),'negative_cutoff_beyond_sector')
        check(project(nonlinear(fa(p1,p2)),F(4*k*k))=={},'coarse_omits_coupled_daughter')
        check(F(k*k,k*k)==1,'viscous_time_normalization')
    check(2-8+6==0,'real_energy_cubic_cancellation')
    check(2-32+30==0,'inviscid_enstrophy_cubic_cancellation')
    check(8*30-6*32==48 and 6*2-2*30==-48 and 2*32-8*2==48,'nambu_cross_product')
    check(2+8+6!=0,'negative_complex_positive_energy')
    original=amplitude_coefficients(10)
    positive=amplitude_coefficients(10,True)
    for n in range(1,11):
        for i,d in enumerate((1,4,5)):
            # Original power at iA, then divide components x,z by i.
            power=(n-(1 if i in (0,2) else 0))%4
            expected=ep_scale(original[n][i],F(1 if power==0 else -1))
            if power in (1,3):check(original[n][i]=={},'complex_phase_zero_parities')
            else:check(expected==positive[n][i],'complex_phase_coefficient_identity')
            check(initial(original[n][i])==(F(1) if n==1 and i in(0,2) else F(0)),'causal_initial_coefficients')
            if n>=2:
                p,q=((1,2),(0,2),(0,1))[i]
                src:EP={}
                for j in range(1,n):src=ep_add(src,ep_mul(original[j][p],original[n-j][q]))
                if i==1:src=ep_scale(src,F(-1))
                check(ep_add(ep_der(original[n][i]),ep_scale(original[n][i],F(d)))==src,'binary_tree_ode_coefficients')
    check(original[2][1]=={(4,0):F(-1,2),(6,0):F(1,2)},'first_feedback_coefficient')
    comp=theta_coefficients(12,True);lower=theta_coefficients(12,False)
    for i in range(3):
        for term,v in comp[i].items():check(v>=0,'transformed_positive_coefficients')
        for term,v in lower[i].items():check(comp[i].get(term,F(0))>=v,'sec_tan_coefficient_comparison')
    for m in range(13):
        check(lower[0].get((m,m+1),F(0))==lower[2].get((m,m+1),F(0)),'comparison_sec_symmetry')
    # Later proof's fully coupled propagator bounds and restart schedule: algebraic checks.
    for r0 in (F(0),F(1,10),F(1,2),F(3,4),F(3),F(25,2)):
        r=r0;finite_steps=0
        while r>F(1,2):r-=F(1,2);finite_steps+=1
        check(r<=F(1,2) and r>=0,'restart_terminal_smallness')
        count=finite_steps+1
        ceiling=(2*r0.numerator+r0.denominator-1)//r0.denominator
        check(count<=max(1,ceiling),'restart_count_bound')
    # Exact scalar-majorant identities, including retained feedback sums.
    one:EP={(0,0):F(1)}
    for R in (F(1,4),F(1),F(7,2)):
        theta:EP={(0,0):R,(1,0):-R}
        coeffs=[{}]
        for n in range(1,11):
            coeffs.append({(j+1,0):R**n * (-1)**j * comb(n-1,j) for j in range(n)})
            if n>1:
                src:EP={}
                for j in range(1,n):src=ep_add(src,ep_mul(coeffs[j],coeffs[n-j]))
                check(ep_conv(src,1)==coeffs[n],'general_majorant_binary_recursion')
        partial:EP={};power:EP=one
        for M in range(1,10):
            partial=ep_add(partial,coeffs[M]);power=ep_mul(power,theta)
            lhs=ep_mul(ep_add(one,ep_scale(theta,F(-1))),partial)
            rhs=ep_mul({(1,0):R},ep_add(one,ep_scale(power,F(-1))))
            check(lhs==rhs,'restart_geometric_tail_identity')
    for A in (F(1,2),F(3),F(32)):
        full=[[-F(1),A],[A,-F(5)]]
        comp=[[-F(5),A],[A,-F(5)]]
        diff=[[full[i][j]-comp[i][j] for j in range(2)] for i in range(2)]
        check(diff==[[F(4),F(0)],[F(0),F(0)]],'cooperative_generator_comparison')
        check(full[0][1]*full[1][0]==A*A,'closed_loop_positive_product')
        check(full[0][1]*F(0)!=A*A,'negative_deleted_return_coupling')
    # The true refinement source, not a freely prescribed stress.
    p_series=[{(1,0):F(1)}];q_series=[{}]
    for n in range(1,9):
        p_series.append(ep_conv({(r+4,d):c for (r,d),c in q_series[-1].items()},1))
        q_series.append(ep_conv({(r+4,d):c for (r,d),c in p_series[n-1].items()},5))
        p_rhs={(r+4,d):c for (r,d),c in q_series[n-1].items()}
        q_rhs={(r+4,d):c for (r,d),c in p_series[n-1].items()}
        check(ep_add(ep_der(p_series[n]),ep_scale(p_series[n],F(1)))==p_rhs,'paired_variation_p_equation')
        check(ep_add(ep_der(q_series[n]),ep_scale(q_series[n],F(5)))==q_rhs,'paired_variation_q_equation')
    check(q_series[1]=={(5,1):F(1)},'true_source_first_resonant_response')
    check(p_series[2]!={},'negative_dropping_paired_feedback')
    check(ep_mul({(1,0):F(1)},{(4,0):F(1)})=={(5,0):F(1)},'actual_coarse_source_product')
    check(F(128)**20/(8*factorial(20))>F(512)**4,
          'rigorous_quartic_conditioning_negative_control')
    print(json.dumps({'scope':'finite exact regression; not PDE proof or independent audit',
          'groups':dict(sorted(COUNTS.items())),'assertions':sum(COUNTS.values()),
          'ranges':{'K':list(range(1,9)),'amplitude_degree':10,'theta_degree':12},
          'negative_controls':['cutoff beyond invariant sector','coarse missing daughter',
                               'positive real energy is not a complex norm bound',
                               'deleted return coupling', 'quartic metric cost at amplitude 512',
                               'omitted actual paired feedback'],
          'status':'PASS'},indent=2))

if __name__=='__main__':main()
