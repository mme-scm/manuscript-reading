"""Fully anchored absolute test of (P): compute c_E = cs_E(S^3-lift of the complete structure, normal form (1/2,1/2)) by KK from an
abelian character (cs = 0) to the cusp point M=-1, then predict  cs(Y_N,s0) = c_E + (N+3)/4 + (1/8pi^2) int tau_N  (mod 1)
and compare with the independent KK-from-abelian values of cs(Y_N,s0) (kk2 runs). No free constant."""
import numpy as np, sys, cmath, math, snappy, warnings
warnings.filterwarnings('ignore')
import kk3, kk2
from kkpath import Curve, unwrap_log, kk_integral, reducible_points
from kk3 import track_strict
def frac(z): return z-math.floor(z)
rng=np.random.default_rng(3)
def c_E(p,q,want=3,tries=400):
    E=snappy.RationalTangle(q,p).denominator_closure().exterior()
    for qq in [q,pow(q,-1,p),p-q,p-pow(q,-1,p)]:
        for flip in (True,False):
            C=Curve(p,qq,flip)
            try: ugeo,tS=kk2.geo_root(C,E); break
            except AssertionError: C=None
        if C: break
    red=reducible_points(C); vals=[]
    Mend=-1+0j; lm0=cmath.log(Mend)
    for it in range(tries):
        M0=red[it%len(red)]; lm1=cmath.log(M0); lm1=lm1+2j*np.pi*round(((lm0-lm1)/(2j*np.pi)).real)
        mid=None if it<len(red) else (lm0+lm1)/2+complex(rng.normal(0,0.8),rng.normal(0,0.8))
        def path(t):
            if mid is None: return np.exp(lm0+(lm1-lm0)*t)
            return np.exp(lm0+2*t*(mid-lm0)) if t<=0.5 else np.exp(mid+(2*t-1)*(lm1-mid))
        try: m,uu,ll=track_strict(C,path,ugeo,hmax=1.5e-3)
        except Exception: continue
        if abs(uu[-1])>1e-6 or abs(ll[-1]-1)>1e-6: continue
        m,uu,ll=m[::-1],uu[::-1],ll[::-1]
        a=unwrap_log(m)/(2j*np.pi); b=unwrap_log(ll,start=0j)/(2j*np.pi)
        I=kk_integral(a,b); ac,bc=a[-1],b[-1]
        j=round((ac-0.5).real); k=round((bc-0.5).real)
        assert abs(ac-0.5-j)<1e-6 and abs(bc-0.5-k)<1e-6, (ac,bc)
        cE=I+k*ac-j*bc
        vals.append((complex(M0),mid is not None,complex(cE)))
        if len(vals)>=want: break
    return vals
if __name__=='__main__':
    p,q=int(sys.argv[1]),int(sys.argv[2])
    for v in c_E(p,q): print('base %s via=%s  c_E = %.8f %+.8fi'%(np.round(v[0],4),v[1],frac(v[2].real),v[2].imag))
