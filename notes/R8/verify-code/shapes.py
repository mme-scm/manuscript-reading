import numpy as np, snappy, warnings, sys
warnings.filterwarnings('ignore')
from riley import *
def Lof(M,u,lw): return num_word(M,u,lw)[0,0]
def shapes(p,q):
    w=word(p,q); lw=longitude_word(p,q)
    E=snappy.RationalTangle(q,p).denominator_closure().exterior()
    tS=complex(E.cusp_info()[0]['shape'])
    res=[]
    for Mp in (-1.0+0j, 1.0+0j):
        for u0 in roots_u(Mp,w):
            Lp=Lof(Mp,u0,lw)
            d=1e-5*np.exp(0.3j)
            M1=Mp*np.exp(d)
            r=roots_u(M1,w); u1=r[np.argmin(abs(r-u0))]
            L1=Lof(M1,u1,lw)
            tau=np.log(L1/Lp)/np.log(M1/Mp)
            res.append((Mp.real,np.round(u0,6),np.round(Lp,6),np.round(tau,5)))
    return tS,res
if __name__=='__main__':
    p,q=int(sys.argv[1]),int(sys.argv[2])
    tS,res=shapes(p,q)
    print('SnapPy shape',np.round(tS,5))
    for r in res: print('  M_p=%+.0f u=%s L_p=%s tau_R=%s'%r)
