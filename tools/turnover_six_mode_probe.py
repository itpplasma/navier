#!/usr/bin/env python3
"""Heuristic dealiased six-mode source-reference turnover probe.

Floating point / finite Fourier section only. Never a PDE certificate.
"""
from __future__ import annotations
import argparse, json
import numpy as np

K0=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,0.]])
MU=3/5
XS=(14,-13,5,-4,2,-1)
TARGETS=(5,-4,2,-1)

def ap(s): return np.array([1.,-np.sqrt(1+s*s),-s])

def run(N=48,dt=5e-4,T=0.8,A=1.0):
    freq=np.fft.fftfreq(N)*N
    m,z=np.meshgrid(freq,freq,indexing='ij')
    kx=(3*m-z)/20.; kz=z/2.; k2=kx*kx+kz*kz
    inv=np.divide(1.,k2,out=np.zeros_like(k2),where=k2>0)
    cutoff=(N-1)//3
    mask=(abs(m)<=cutoff)&(abs(z)<=cutoff)
    U=np.zeros((3,N,N),complex)
    for x in XS:
        mm=(x+1)//3
        vec=ap(x/10.)*A
        U[:,mm%N,1%N]=vec
        U[:,(-mm)%N,(-1)%N]=vec
    U0=U.copy(); norm=N*N
    def physical(h): return (np.fft.ifft2(h,axes=(-2,-1))*norm).real
    def project(F):
        dot=kx*F[0]+kz*F[2]
        out=F.copy()
        out[0]-=kx*dot*inv; out[2]-=kz*dot*inv
        out[:,0,0]=0
        return out
    def linear(S):
        KV=np.einsum('ab,bij->aij',K0,S)
        kd=kx*KV[0]+kz*KV[2]
        out=-KV
        out[0]+=kx*kd*inv; out[2]+=kz*kd*inv
        out-=MU*k2*S
        out[:,0,0]=0
        return out
    def rhs(S):
        u=physical(S)
        dx=physical(1j*kx*S); dz=physical(1j*kz*S)
        adv=u[0]*dx+u[2]*dz
        nh=-(np.fft.fft2(adv,axes=(-2,-1))/norm)*mask
        return (linear(S)+project(nh))*mask
    def energy(S,where=None):
        e=np.sum(abs(S)**2,axis=0)
        return float(np.sum(e if where is None else e[where]))
    def target_plus(S,K):
        mm=(2*K+2)//3
        f=S[:,mm%N,2%N]
        q=np.sqrt(1+(K/10.)**2)
        return float(abs((f[0]-f[1]/q)/2))
    Ein=energy(U0)
    oldmask=(abs(z)==1)
    z2mask=(abs(z)==2)
    rows=[]; steps=int(np.ceil(T/dt));dt=T/steps
    sample=set(np.round(np.linspace(0,steps,81)).astype(int))
    for j in range(steps+1):
        if j in sample:
            Et=energy(U); Eold=energy(U,oldmask); E2=energy(U,z2mask)
            gains=[target_plus(U,K)/A for K in TARGETS]
            rows.append(dict(t=j*dt,energy=Et,old_fraction=np.sqrt(Eold/max(Et,1e-300)),
                             z2_energy_fraction=E2/max(Et,1e-300),min_target_gain=min(gains),
                             target_gains=gains,edge_energy=energy(U,(abs(m)>=cutoff-1)|(abs(z)>=cutoff-1))))
        if j==steps: break
        up=physical(U)
        maxk=max(float(np.max(abs(kx[mask]))),float(np.max(abs(kz[mask]))))
        if dt*maxk*np.max(np.sqrt(np.sum(up*up,axis=0)))>.5:
            raise RuntimeError('CFL guard')
        a=rhs(U); b=rhs(U+dt*a/2); c=rhs(U+dt*b/2); d=rhs(U+dt*c)
        U=(U+dt*(a+2*b+2*c+d)/6)*mask
        if not np.all(np.isfinite(U)): raise RuntimeError('nonfinite')
    best=min(rows,key=lambda r:(r['old_fraction'],-r['min_target_gain']))
    turnover=[r for r in rows if r['old_fraction']<0.2 and r['min_target_gain']>2]
    return dict(N=N,cutoff=cutoff,dt=dt,T=T,A=A,initial_energy=Ein,
                scope='heuristic finite dealiased source-reference lattice only',rows=rows,best=best,
                turnover_candidate=turnover[0] if turnover else None)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,default=48);p.add_argument('--dt',type=float,default=5e-4)
    p.add_argument('--T',type=float,default=.8);p.add_argument('--A',type=float,default=1.);p.add_argument('--output')
    a=p.parse_args();r=run(a.N,a.dt,a.T,a.A)
    text=json.dumps(r,indent=2)
    if a.output: open(a.output,'w').write(text+'\n')
    print(json.dumps({'N':r['N'],'A':r['A'],'best':r['best'],'turnover_candidate':r['turnover_candidate']},indent=2))
