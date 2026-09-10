#!/usr/bin/env python3
"""Dealiased floating-point two-dimensional reference/control evolution.

Not a simulation of the complete OpenAI flow. Spatial Fourier truncation,
finite time and ordinary RK4: no interval certificate or whole-space claim.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np


def run(N:int, dt:float, end:float, lam:float, A:float=1., B:float=2.) -> dict:
    if N<12 or dt<=0 or end<=0: raise ValueError('Invalid resolution/time')
    u=12/5; Q=13/5; nu=125/2197
    freq=np.fft.fftfreq(N)*N
    m,n=np.meshgrid(freq,freq,indexing='ij');kx=u*m;kz=n;K2=kx*kx+kz*kz
    inv=np.divide(1.,K2,out=np.zeros_like(K2),where=K2>0)
    cutoff=(N-1)//3; mask=(abs(m)<=cutoff)&(abs(n)<=cutoff)
    Y=np.zeros((2,N,N),complex)
    for km,kn,am in [(1,1,A),(-1,1,B),(-1,-1,A),(1,-1,B)]:
        Y[0,km%N,kn%N]=1j*kn*Q*Q*am
        Y[1,km%N,kn%N]=-Q*am
    initial=Y.copy(); norm=N*N
    def physical(h):return (np.fft.ifft2(h,axes=(-2,-1))*norm).real
    def velocities(state):
        omega=state[0]
        return np.stack((-1j*kz*inv*omega,1j*kx*inv*omega))
    def rhs(state):
        vel=velocities(state); uv=physical(vel)
        dx=physical(1j*kx*state);dz=physical(1j*kz*state)
        adv=uv[0]*dx+uv[1]*dz
        out=-(np.fft.fft2(adv,axes=(-2,-1))/norm)*mask-nu*K2*state
        out[0]+=-1j*lam*kz*state[1]
        out[1]+=-lam*vel[0]
        out[:,0,0]=0
        return out
    def observe(t,state):
        vv=velocities(state); energy=(abs(state[0])**2*inv+abs(state[1])**2)
        def mode(km,kn):
            r=vv[0,km%N,kn%N];theta=state[1,km%N,kn%N]
            # inviscid source coordinate at slope u. For lam=0 this is
            # only a diagnostic, not a growing eigenbranch.
            plus=(r-theta/Q)/2
            return {'radial_abs':float(abs(r)),'N_abs':float(abs(theta)),
                    'source_positive_coordinate_abs':float(abs(plus))}
        rhs0=rhs(state)
        derivative=2*np.real(np.sum(np.conj(state[0])*rhs0[0]*inv+np.conj(state[1])*rhs0[1]))
        budget=-4*lam*np.real(np.sum(np.conj(vv[0])*state[1]))-2*nu*np.sum(K2*energy)
        parent=sum(energy[km%N,kn%N] for km,kn in [(1,1),(-1,1),(-1,-1),(1,-1)])
        doubles=sum(energy[km%N,kn%N] for km,kn in [(2,2),(-2,2),(-2,-2),(2,-2)])
        quadruples=sum(energy[km%N,kn%N] for km,kn in [(4,4),(-4,4),(-4,-4),(4,-4)])
        return {'t':float(t),'energy':float(np.sum(energy)),
                'parent_energy':float(parent),'doubled_energy':float(doubles),
                'quadrupled_energy':float(quadruples),'doubled_positive':mode(2,2),
                'doubled_negative':mode(-2,2),
                'energy_identity_residual':float(derivative-budget),
                'edge_energy':float(np.sum(energy[(abs(m)>=cutoff-1)|(abs(n)>=cutoff-1)]))}
    steps=int(np.ceil(end/dt));dt=end/steps
    # Explicit diffusion/linear check; actual nonlinear CFL also checked.
    if dt*nu*np.max(K2[mask])>=2.: raise ValueError('Diffusive step too large')
    sample_steps=set(np.round(np.linspace(0,steps,21)).astype(int));rows=[]
    for j in range(steps+1):
        if j in sample_steps:rows.append(observe(j*dt,Y))
        if j==steps:break
        vphys=physical(velocities(Y))
        cfl=dt*(u*cutoff*np.max(abs(vphys[0]))+cutoff*np.max(abs(vphys[1])))
        if cfl>.8: raise RuntimeError(f'Nonlinear CFL {cfl} > .8')
        a=rhs(Y);b1=rhs(Y+dt*a/2);c=rhs(Y+dt*b1/2);d=rhs(Y+dt*c)
        Y=(Y+dt/6*(a+2*b1+2*c+d))*mask
        if not np.all(np.isfinite(Y)): raise RuntimeError('Nonfinite state')
    err=max(abs(r['energy_identity_residual']) for r in rows)
    if err>1e-8*max(r['energy'] for r in rows):raise AssertionError('Energy identity test failed')
    if lam==0:
        wanted=initial[0]*np.exp(-nu*Q*Q*end)
        relative=np.linalg.norm(Y[0]-wanted)/np.linalg.norm(wanted)
        if relative>5e-8:raise AssertionError(f'Exact smooth-control planar heat comparison {relative}')
    else:relative=None
    return {'grid':N,'cutoff':cutoff,'dt':dt,'nu':nu,'lambda':lam,'A':A,'B':B,
            'scope':'Full nonlinear local reference projected to the stated finite Fourier band, not the physical source.',
            'control_planar_heat_relative_error':relative,'observations':rows}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--N',type=int,default=48)
    p.add_argument('--dt',type=float,default=.001);p.add_argument('--T',type=float,default=2.)
    p.add_argument('--lambda-value',type=float,default=1.);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();begin=time.time();result=run(a.N,a.dt,a.T,a.lambda_value)
    a.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS',a.N,a.lambda_value,'seconds',time.time()-begin)
    print(json.dumps(result['observations'][-1],indent=2))
if __name__=='__main__':main()
