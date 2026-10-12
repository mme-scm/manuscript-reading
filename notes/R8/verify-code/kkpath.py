"""(d) Mod-1 SL(2,C) Chern-Simons of (Y_N, s) for 2-bridge knots, by Kirk-Klassen integration on the Riley curve
starting from an ABELIAN (reducible) character, where cs = 0 exactly.  Independent of the cusp/Schlafli bookkeeping.
Conventions (validated on torus knots vs Fintushel-Stern, see torus_test.py):
   rho(mu) ~ diag(e^{2 pi i a}), rho(lambda) ~ diag(e^{2 pi i b});  d cs_E = a db - b da   (SU(2) units)
   closed Y_N = E u V, slope N mu + lambda, dual mu:  cs(Y_N) = cs_E(a,b) + (N a + b) * a,   N a + b in Z.
Riley's longitude is reversed w.r.t. SnapPy's (shape check in shapes.py), so L_S = 1/L_Riley.
"""
import numpy as np, snappy, warnings, sys, math, cmath
warnings.filterwarnings('ignore')
from riley import *

class Curve:
    def __init__(s,p,q,flip=True):
        s.p,s.q,s.flip=p,q,flip; s.w=word(p,q); s.lw=longitude_word(p,q)
    def roots(s,M): return roots_u(M,s.w)
    def L(s,M,u):
        x=num_word(M,u,s.lw)[0,0]
        return 1/x if s.flip else x      # SnapPy-oriented longitude eigenvalue

def track(C, Mpath, u0, hmax=2e-3):
    """continue u along M(t), t in [0,1] (Mpath callable). returns lists M,u,L."""
    t=0.0; M=Mpath(0); u=u0; Ms=[M]; us=[u]; Ls=[C.L(M,u)]; up=None
    h=hmax
    while t<1-1e-15:
        h=min(h,1-t)
        Mn=Mpath(t+h); r=C.roots(Mn)
        pred=u if up is None else u+(u-up)
        d=np.abs(r-pred); i=np.argsort(d)
        if len(r)>1 and d[i[0]]>0.25*d[i[1]] and h>1e-9:
            h/=2; continue
        up=u; u=r[i[0]]; M=Mn; t+=h
        Ms.append(M); us.append(u); Ls.append(C.L(M,u))
        h=min(hmax,2*h)
    return np.array(Ms),np.array(us),np.array(Ls)

def unwrap_log(z, start=None):
    lz=np.empty(len(z),complex)
    lz[0]=cmath.log(z[0]) if start is None else start
    for k in range(1,len(z)): lz[k]=lz[k-1]+cmath.log(z[k]/z[k-1])
    return lz

def kk_integral(a,b):
    return np.sum(a[:-1]*b[1:]-b[:-1]*a[1:])   # = int a db - b da for piecewise linear (a,b)

def cone_path_H(E,N,n=400):
    Hs=[0j]
    for k in range(1,n+1):
        s=k/n; X=E.copy(); X.dehn_fill((N/s,1/s))
        Hs.append(complex(X.cusp_info()[0]['holonomies'][0]))
    return np.array(Hs)

def run(p,q,Ns=(2,-2),npath=400,verbose=True):
    C=Curve(p,q)
    E=snappy.RationalTangle(q,p).denominator_closure().exterior()
    tS0=complex(E.cusp_info()[0]['shape']); xE=float(E.chern_simons())
    Xs=E.copy(); Xs.dehn_fill((2/1e-3,1/1e-3)); hh=Xs.cusp_info()[0]['holonomies']
    tS=complex(hh[1])/complex(hh[0])     # holonomy ratio H(lambda)/H(mu) near the complete structure (= conj of cusp_info shape)
    # geometric root at M=-1 (S^3 lift): shape (with L_S) must equal SnapPy's
    best=None
    for u0 in C.roots(-1+0j):
        M1=-np.exp(1e-6*np.exp(0.4j)); r=C.roots(M1); u1=r[np.argmin(abs(r-u0))]
        tau=np.log(C.L(M1,u1)/C.L(-1+0j,u0))/np.log(-M1)
        if best is None or abs(tau-tS)<best[0]: best=(abs(tau-tS),u0,tau)
    assert best[0]<1e-2, best
    ugeo=best[1]
    out={}
    for N in Ns:
        X=E.copy(); X.dehn_fill((N,1)); VolY=float(X.volume()); xY=float(X.chern_simons())
        H=cone_path_H(E,N,npath)
        assert np.max(np.abs(np.diff(H.imag)))<0.2
        Delta_piece=(2*np.pi/npath)*(np.sum(H.imag)-0.5*H.imag[-1])/(4*np.pi**2)   # (1/4pi^2) int tau dalpha (trapezoid)
        # follow Riley branch along cone path: M(s) = -exp(sg*H(s)/2), decide sg by consistency of L
        for sg in (+1,-1):
            Mc=-np.exp(sg*H/2)
            Ms=[Mc[0]]; us=[ugeo]; ok=True
            for k in range(1,len(Mc)):
                seg=lambda t,k=k: Mc[k-1]+(Mc[k]-Mc[k-1])*t
                m,uu,ll=track(C,seg,us[-1],hmax=0.25)
                us.append(uu[-1]); Ms.append(m[-1])
            Lc=np.array([C.L(Ms[k],us[k]) for k in range(len(Ms))])
            Hl_pred=sg*2*np.log(-Lc)   # should equal SnapPy H(lambda) = i alpha - N H(mu)
            alpha=2*np.pi*np.arange(len(H))/npath
            err=np.max(np.abs(np.exp((Hl_pred-(1j*alpha-N*H))/2)-1)) if True else 0
            if err<1e-6: break
        else:
            raise RuntimeError('branch mismatch')
        Mt,ut=Ms[-1],us[-1]
        fill=Mt**N*C.L(Mt,ut)
        res={'VolY':VolY,'xY':xY,'Delta_piece':Delta_piece,'sg':sg,'fill_eig':fill,'Mt':Mt,'ut':ut,'H_end':H[-1]}
        # lifts: s0 = (Mt,ut) [S^3 lift continued], s1 = (-Mt, ut)
        for lift,Mend in (('s0',Mt),('s1',-Mt)):
            # reducible base points: roots of f1(M,0); try each, straight path in log M from end to base
            red=[m for m in np.roots(np.trim_zeros(f1poly_red(C,),'b')[::-1])] if False else reducible_points(C)
            vals=[]
            for M0 in red:
                for detour in (0,0.6,-0.6):
                    lm0,lm1=cmath.log(Mend),cmath.log(M0)
                    # choose branch of log M0 closest
                    lm1=lm1+2j*np.pi*round(((lm0-lm1)/(2j*np.pi)).real)
                    path=lambda t: np.exp(lm0+(lm1-lm0)*t+detour*1j*(lm1-lm0)*t*(1-t))
                    try:
                        m,uu,ll=track(C,path,ut,hmax=2e-3)
                    except Exception as e:
                        continue
                    if abs(uu[-1])>1e-6: continue
                    # reverse: base -> end
                    m,uu,ll=m[::-1],uu[::-1],ll[::-1]
                    a=unwrap_log(m)/(2j*np.pi)
                    lb=unwrap_log(ll, start=0j)        # b(base)=0 exactly (L=1 at reducible)
                    assert abs(ll[0]-1)<1e-6, ll[0]
                    b=lb/(2j*np.pi)
                    csE=kk_integral(a,b)
                    nint=N*a[-1]+b[-1]
                    assert abs(nint-round(nint.real))<1e-6, nint
                    cs=csE+round(nint.real)*a[-1]
                    vals.append((M0,detour,cs))
            res[lift]=vals
        out[N]=res
    return E,tS,xE,out

def reducible_points(C):
    # f1(M,0)=0 : polynomial in M via sampling (degree bounded); use Laurent fit
    deg=2*len(C.w)+4
    Ms=np.exp(2j*np.pi*np.arange(4*deg)/(4*deg))
    vals=np.array([f1poly(M,C.w)[0]*M**(deg//2) for M in Ms])
    coef=np.fft.fft(vals)/len(Ms)          # coefficients of M^k (k=0..)
    c=coef[:deg+1]; c[np.abs(c)<1e-9]=0
    c=np.trim_zeros(c,'b'); r=np.roots(c[::-1])
    r=[z for z in r if abs(z)>1e-8]
    return [z for z in r if abs(f1poly(z,C.w)[0])<1e-6]

def frac(z): return z-math.floor(z)
if __name__=='__main__':
    p,q=int(sys.argv[1]),int(sys.argv[2])
    E,tS,xE,out=run(p,q)
    print('knot',E.identify()[:2],'shape',np.round(tS,5),' x_snappy(E)=%.8f'%xE)
    for N,r in out.items():
        print('N=%+d  Vol=%.8f  x_snappy=%.8f  (1/4pi^2)int tau=%.8f  sg=%d  fill eigenvalue=%s'%(N,r['VolY'],r['xY'],r['Delta_piece'],r['sg'],np.round(r['fill_eig'],9)))
        for lift in ('s0','s1'):
            for (M0,det,cs) in r[lift]:
                print('   %s base M0=%s det=%+.1f : cs = %.9f %+.9fi   Vol/4pi^2=%.9f  Re cs mod 1/4=%.6f  x/2 mod 1/4=%.6f -x/2 mod 1/4=%.6f'%(
                    lift,np.round(M0,4),det,frac(cs.real),cs.imag,r['VolY']/(4*np.pi**2),frac(cs.real)%0.25,(r['xY']/2)%0.25,(-r['xY']/2)%0.25))
