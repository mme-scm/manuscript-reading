import snappy, warnings, math, cmath, sys, json
warnings.filterwarnings('ignore')
def getM(name):
    if name.startswith('K') and 'n' in name or name.startswith('K') and 'a' in name:
        return snappy.HTLinkExteriors[name]
    return snappy.Manifold(name)
def profile(M, N, n=120):
    """u_N(alpha) at alpha=2 pi k/n, continuing the filled structure step by step."""
    us=[]; worst='all'
    X=M.copy()
    for k in range(1,n+1):
        s=k/n; X.dehn_fill((N/s,1/s)); st=X.solution_type()
        if not st.startswith('all tetra'): worst=st[:20]
        us.append(complex(X.cusp_info()[0]['holonomies'][0]))
    return us, worst
def analyse(M, n=120):
    t=complex(M.cusp_info()[0]['shape']); x,y=t.real,t.imag
    out={'tau':[x,y]}
    Z={}
    for N in (2,-2):
        us,worst=profile(M,N,n)
        al=[2*math.pi*k/n for k in range(1,n+1)]
        da=2*math.pi/n
        Iu=da*(sum(us)-0.5*us[-1])  # trapezoid with u(0)=0
        Z[N]=Iu/(4*math.pi**2)
        lead=lambda a: 1j*a/(N+t)
        win=max(abs(u.imag)/(a/2) for u,a in zip(us,al))
        tN0=(N+x)/abs(N+t)**2
        jump=max(abs(us[i+1]-us[i]) for i in range(n-1))
        L2=abs(N+t)**2/y
        out[N]=dict(Z=[Z[N].real,Z[N].imag], Zlead=[0, 0], uend=[us[-1].real,us[-1].imag],
                    ulead_end=[(2j*math.pi/(N+t)).real,(2j*math.pi/(N+t)).imag],
                    window=win, t0=tN0, supT=max(abs(u.imag) for u in us), jump=jump, worst=worst, L=math.sqrt(L2),
                    prof=[[u.real,u.imag] for u in us[::max(1,n//24)]])
    Zt=Z[2]-Z[-2]; Zl=2j/(4-t*t)
    out['Z']=[Zt.real,Zt.imag]; out['Zlead']=[Zl.real,Zl.imag]
    return out
if __name__=='__main__':
    for nm in sys.argv[1].split(','):
        M=getM(nm); o=analyse(M, int(sys.argv[2]) if len(sys.argv)>2 else 120)
        print(nm,'tau=%.3f+%.3fi'%tuple(o['tau']),'Z=%.4f%+.4fi'%tuple(o['Z']),'Zlead=%.4f%+.4fi'%tuple(o['Zlead']))
        for N in (2,-2):
            r=o[N]; print('  N=%+d L=%.3f t0=%+.3f window=%.3f supT=%.3f uend=%.3f%+.3fi (lead %.3f%+.3fi) jump=%.3f %s'%(N,r['L'],r['t0'],r['window'],r['supT'],*r['uend'],*r['ulead_end'],r['jump'],r['worst']))
