"""kk2 with a stricter path tracker (fails instead of guessing near branch points) and more path families."""
import numpy as np, sys, math, cmath, json
import kkpath, kk2
from kkpath import Curve

def track_strict(C, Mpath, u0, hmax=2e-3, dlog=0.01):
    t=0.0; M=Mpath(0); u=u0; Ms=[M]; us=[u]; Ls=[C.L(M,u)]; up=None; h=hmax
    while t<1-1e-15:
        h=min(h,1-t)
        Mn=Mpath(t+h)
        if abs(cmath.log(Mn/M))>dlog and h>1e-12: h/=2; continue
        r=C.roots(Mn)
        pred=u if up is None else u+(u-up)*1.0
        d=np.abs(r-pred); i=np.argsort(d)
        if len(r)>1 and (d[i[0]]>0.15*d[i[1]] or d[i[0]]>0.05*(1+abs(u))):
            if h<1e-12: raise RuntimeError('branch point')
            h/=2; continue
        up=u; u=r[i[0]]; M=Mn; t+=h
        Ms.append(M); us.append(u); Ls.append(C.L(M,u))
        h=min(hmax,2*h)
    return np.array(Ms),np.array(us),np.array(Ls)

kkpath.track=track_strict
kk2.track=track_strict

if __name__=='__main__':
    p,q=int(sys.argv[1]),int(sys.argv[2])
    kk2.rng=np.random.default_rng(int(sys.argv[3]) if len(sys.argv)>3 else 7)
    _orig=kk2.cs_via_paths
    kk2.cs_via_paths=lambda C,N,Me,ue,want=3,tries=150: _orig(C,N,Me,ue,want=want,tries=tries)
    from kk2 import run, frac
    R=run(p,q)
    print('== b(%d,%d) = %s'%(p,q,R['name']))
    cs0={}
    for N in (2,-2):
        r=R[N]
        print(' N=%+d Vol/4pi^2=%.9f  x/2 mod 1/4=%.7f  I_N=(1/4pi^2)int tau=%.8f  endpoint-L check=%.1e'%(N,r['Vol']/(4*np.pi**2),(r['x']/2)%0.25,r['I'],r['endchk']))
        for lift in ('s0','s1'):
            for v in r[lift]:
                print('    %s [%s base %s n=%d]  cs = %.8f %+.8fi   (Re mod 1/4 = %.7f)'%(lift,v['kind'],np.round(v['M0'],4),v['n'],frac(v['cs'].real),v['cs'].imag,frac(v['cs'].real)%0.25))
        good=[v['cs'] for v in r['s0'] if abs(v['cs'].imag + r['Vol']/(4*np.pi**2))<2e-5]
        if good: cs0[N]=good[0]
        g1=[v['cs'] for v in r['s1'] if abs(v['cs'].imag + r['Vol']/(4*np.pi**2))<2e-5]
        if good and g1: print('    L2 check: cs(s1)-cs(s0) mod 1 = %.7f ; spread of good s0 values = %.1e'%(frac((g1[0]-good[0]).real), max(abs(frac(z.real-good[0].real+0.5)-0.5) for z in good)))
    if 2 in cs0 and -2 in cs0:
        D=frac((cs0[2]-cs0[-2]).real); Dl=R[2]['I']-R[-2]['I']
        print(' D = cs(Y2,s0)-cs(Y-2,s0) mod 1 = %.7f ;  Delta_K=%.7f : Delta_K/2 mod 1=%.7f  Delta_K mod 1=%.7f  Delta_K/2+1/2=%.7f Delta_K+1/2=%.7f'%(
            D,Dl,frac(Dl/2),frac(Dl),frac(Dl/2+0.5),frac(Dl+0.5)))
    json.dump(R,open('kk3_%d_%d.json'%(p,q),'w'),default=lambda o: [o.real,o.imag] if isinstance(o,complex) else str(o))