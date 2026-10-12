import snappy, warnings, math, sys
warnings.filterwarnings('ignore')
from tw_profile import getM
def pathZ(M,p,q,k,n=200):
    X=M.copy(); acc=0; prev=None; jump=0; us=[]
    for j in range(1,n+1):
        s=j/n; X.dehn_fill((p/s,q/s)); h=X.cusp_info()[0]['holonomies']
        u=complex(h[0])+k*complex(h[1]); us.append(u)
    da=2*math.pi/n; I=da*(sum(us)-0.5*us[-1])
    win=max(abs(u.imag)/(math.pi*j/n) for j,u in enumerate(us,1))
    return I/(4*math.pi**2), win, X.solution_type()[:12], float(X.volume())
nm=sys.argv[1]; M=getM(nm); t=complex(M.cusp_info()[0]['shape'])
for k in [0,1,2,3,5,8]:
    tp=t/(1+k*t)  # shape in basis (mu'=mu+k lam, lam)
    Zp,wp,stp,vp=pathZ(M,2,2*k+1,k); Zm,wm,stm,vm=pathZ(M,-2,1-2*k,k)
    Z=Zp-Zm; Zl=2j/(4-tp*tp)
    L=lambda N: abs(N+tp)/math.sqrt(tp.imag)
    print('k=%d slopes 2/%d,2/%d  tau\'=%.4f%+.4fi  L=%.2f,%.2f  Delta\'=%.5f  lead=%.5f  1/2+x\'^2/8=%.5f  windows %.3f,%.3f  ends %s %.3f | %s %.3f'%(
        k,2*k+1,2*k-1,tp.real,tp.imag,L(2),L(-2),Z.imag,Zl.imag,0.5+tp.real**2/8,wp,wm,stp,vp,stm,vm))
