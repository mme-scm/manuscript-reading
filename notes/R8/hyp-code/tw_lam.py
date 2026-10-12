import snappy, warnings, math, sys
warnings.filterwarnings('ignore')
from tw_profile import getM
def lam(nm,n=200):
    M=getM(nm); t=complex(M.cusp_info()[0]['shape'])
    res={}
    for N in (2,-2):
        X=M.copy(); us=[];vs=[]
        for k in range(1,n+1):
            s=k/n; X.dehn_fill((N/s,1/s)); h=X.cusp_info()[0]['holonomies']
            us.append(complex(h[0])); vs.append(complex(h[1]))
        chk=max(abs(N*u+v-2j*math.pi*k/n) for k,(u,v) in enumerate(zip(us,vs),1))
        da=2*math.pi/n
        Iu=da*(sum(us)-0.5*us[-1]); Iv=da*(sum(vs)-0.5*vs[-1])
        al=[2*math.pi*k/n for k in range(1,n+1)]
        thw=min(min(v.imag/a for v,a in zip(vs,al)), 0), max(v.imag/a for v,a in zip(vs,al))
        res[N]=(Iu,Iv,chk,thw)
    Z=(res[2][0]-res[-2][0])/(4*math.pi**2); W=(res[2][1]+res[-2][1])/(8*math.pi**2)
    print(nm,'tau=%.3f%+.3fi'%(t.real,t.imag),'Z=%.5f%+.5fi'%(Z.real,Z.imag),'W=%.5f%+.5fi'%(W.real,W.imag),
          'i/2-W=%.5f%+.5fi'%((0.5j-W).real,(0.5j-W).imag),'Wlead=%.5f%+.5fi'%((0.5j*t*t/(t*t-4)).real,(0.5j*t*t/(t*t-4)).imag),
          'chk(Nu+v=i a)=%.1e,%.1e'%(res[2][2],res[-2][2]),'theta/alpha range N=2:',[round(z,3) for z in res[2][3]],'N=-2:',[round(z,3) for z in res[-2][3]])
for nm in sys.argv[1].split(','): lam(nm)
