"""(d) driver: mod-1 SL(2,C) CS of (Y_N, s0/s1) via Kirk-Klassen from abelian characters (cs=0), several paths."""
import numpy as np, snappy, warnings, sys, math, cmath, json
warnings.filterwarnings('ignore')
from riley import *
from kkpath import Curve, track, unwrap_log, kk_integral, cone_path_H, reducible_points

rng=np.random.default_rng(1)
def frac(z): return z-math.floor(z)

def geo_root(C,E):
    Xs=E.copy(); Xs.dehn_fill((2/1e-3,1/1e-3)); hh=Xs.cusp_info()[0]['holonomies']
    tS=complex(hh[1])/complex(hh[0])
    best=None
    for u0 in C.roots(-1+0j):
        M1=-np.exp(1e-6*np.exp(0.4j)); r=C.roots(M1); u1=r[np.argmin(abs(r-u0))]
        tau=np.log(C.L(M1,u1)/C.L(-1+0j,u0))/np.log(-M1)
        if best is None or abs(tau-tS)<best[0]: best=(abs(tau-tS),u0,tau)
    assert best[0]<1e-2, best
    return best[1], tS

def endpoint(C,E,N,ugeo,npath=200):
    H=cone_path_H(E,N,npath)
    assert np.max(np.abs(np.diff(H.imag)))<0.2
    I=(2*np.pi/npath)*(np.sum(H.imag)-0.5*H.imag[-1])/(4*np.pi**2)
    Mc=-np.exp(H/2); u=ugeo
    for k in range(1,len(Mc)):
        seg=lambda t,k=k: Mc[k-1]+(Mc[k]-Mc[k-1])*t
        m,uu,ll=track(C,seg,u,hmax=0.25); u=uu[-1]
    Mt=Mc[-1]; Lt=C.L(Mt,u)
    alpha_end=2*np.pi
    chk=abs(Lt-(-np.exp((1j*alpha_end-N*H[-1])/2)))
    return Mt,u,I,chk,H

def cs_via_paths(C,N,Mend,uend,want=4,tries=80):
    red=reducible_points(C); vals=[]
    lm0=cmath.log(Mend)
    for it in range(tries):
        M0=red[it%len(red)]
        lm1=cmath.log(M0); lm1=lm1+2j*np.pi*round(((lm0-lm1)/(2j*np.pi)).real)
        if it<len(red): kind='straight'; mid=None
        else:
            kind='via'; mid=(lm0+lm1)/2+complex(rng.normal(0,0.8),rng.normal(0,0.8))
        def path(t):
            if mid is None: return np.exp(lm0+(lm1-lm0)*t)
            return np.exp(lm0+2*t*(mid-lm0)) if t<=0.5 else np.exp(mid+(2*t-1)*(lm1-mid))
        try: m,uu,ll=track(C,path,uend,hmax=1.5e-3)
        except Exception: continue
        if abs(uu[-1])>1e-6: continue
        m,uu,ll=m[::-1],uu[::-1],ll[::-1]
        if abs(ll[0]-1)>1e-6: continue
        a=unwrap_log(m)/(2j*np.pi); b=unwrap_log(ll,start=0j)/(2j*np.pi)
        csE=kk_integral(a,b); nint=N*a[-1]+b[-1]
        if abs(nint-round(nint.real))>1e-6: continue
        cs=csE+round(nint.real)*a[-1]
        vals.append(dict(M0=complex(M0),kind=kind,cs=complex(cs),n=int(round(nint.real))))
        if len(vals)>=want: break
    return vals

def run(p,q,Ns=(2,-2)):
    E=snappy.RationalTangle(q,p).denominator_closure().exterior(); E.chern_simons()
    found=None
    for qq in [q,pow(q,-1,p),p-q,p-pow(q,-1,p)]:
        for flip in (True,False):
            C=Curve(p,qq,flip)
            try: ugeo,tS=geo_root(C,E); found=(qq,flip); break
            except AssertionError: pass
        if found: break
    assert found
    print('Riley word b(%d,%d), longitude flip=%s matches SnapPy exterior'%(p,found[0],found[1]))
    name=str(E.identify()[1]) if len(E.identify())>1 else str(E.identify()[0])
    res={'p':p,'q':q,'name':name}
    for N in Ns:
        X=E.copy(); X.dehn_fill((N,1)); V=float(X.volume()); x=float(X.chern_simons())
        Mt,ut,I,chk,H=endpoint(C,E,N,ugeo)
        r={'Vol':V,'x':x,'I':I,'endchk':chk}
        for lift,Me in (('s0',Mt),('s1',-Mt)):
            r[lift]=cs_via_paths(C,N,Me,ut)
        res[N]=r
    return res

if __name__=='__main__':
    p,q=int(sys.argv[1]),int(sys.argv[2])
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
    json.dump(R,open('kk_%d_%d.json'%(p,q),'w'),default=lambda o: [o.real,o.imag] if isinstance(o,complex) else str(o))
