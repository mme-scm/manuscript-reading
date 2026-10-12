import snappy, warnings, math, sys
warnings.filterwarnings('ignore')
from tw_profile import profile, getM
from tw_frame import fix_frame
def haze(z): return 3.3957*z*(1-z*z)/(1+z*z)
def haze_inv(A):
    lo,hi=math.sqrt(math.sqrt(5)-2),1.0   # haze decreasing on [lo,1)
    if A>haze(lo): return None
    for _ in range(80):
        m=(lo+hi)/2
        if haze(m)>A: lo=m
        else: hi=m
    return (lo+hi)/2
def run(nm,n=400):
    M=getM(nm) if not nm.startswith('K') or ('n' in nm or 'a' in nm) else snappy.Manifold(nm)
    if nm.startswith('K') and '_' in nm: fix_frame(M)
    t=complex(M.cusp_info()[0]['shape'])
    for N in (2,-2):
        us,_=profile(M,N,n); al=[2*math.pi*k/n for k in range(1,n+1)]
        ell=[abs(u.real) for u in us]; A=[a*l for a,l in zip(al,ell)]
        ac=next((a for a,x in zip(al,A) if x>1.0197),None); ac2=next((a for a,x in zip(al,A) if x>0.980),None)
        drift=0.0; da=2*math.pi/n
        for a,l,x in zip(al,ell,A):
            if x>0.980: break
            z=haze_inv(x); drift+=2*l*(1-z*z)/(a*a*z*z*(3-z*z))*da
        t0=(N+t.real)/abs(N+t)**2
        ts=[u.imag/a for u,a in zip(us,al)]
        realdrift=max(abs(tt-t0) for tt,a in zip(ts,al) if a<=(ac2 or 0)) if ac2 else None
        L=abs(N+t)/math.sqrt(t.imag)
        print('%-9s N=%+d L=%.2f A(2pi)=%.2f  HK-controlled alpha<=%.2f (=%.0f%% of path, %.0f%% of Delta-weight)  drift bound on it %.4f (actual %.4f)  t0=%+.3f'%(
            nm,N,L,A[-1],ac2 or float('nan'),100*(ac2 or 0)/(2*math.pi),100*((ac2 or 0)/(2*math.pi))**2,drift,realdrift or float('nan'),t0))
if __name__=="__main__":
    for nm in sys.argv[1].split(","): run(nm)
