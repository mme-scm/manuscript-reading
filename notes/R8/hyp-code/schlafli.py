import snappy, warnings, math, sys
warnings.filterwarnings('ignore')
def run(name, N, n=400, verbose=False):
    M = snappy.Manifold(name)
    V0, cs0 = float(M.volume()), float(M.chern_simons())
    ss = [k/n for k in range(1,n+1)]
    Hs=[]; bad=[]
    for s in ss:
        X = M.copy(); X.dehn_fill((N/s, 1/s))
        st = X.solution_type()
        if not st.startswith('all tetrahedra positively'): bad.append((s,st))
        Hs.append(complex(X.cusp_info()[0]['holonomies'][0]))
    # core complex length L = H(mu) (dual curve mu); length = |Re|, torsion = Im (continuous)
    ell = [abs(h.real) for h in Hs]; tor=[h.imag for h in Hs]
    # check continuity
    jumps = max(abs(tor[i+1]-tor[i]) for i in range(len(tor)-1))
    # trapezoid in alpha = 2 pi s, with value 0 at s=0
    da = 2*math.pi/n
    Iell = da*(0.5*ell[0] + sum(ell[:-1]) + 0.5*ell[-1]) ; Iell = da*(sum(ell)-0.5*ell[-1])
    Itor = da*(sum(tor)-0.5*tor[-1])
    X = M.copy(); X.dehn_fill((N,1))
    V1, cs1 = float(X.volume()), float(X.chern_simons())
    return dict(name=name,N=N,dVol=V1-V0, schl_vol=-0.5*Iell, dCS_snappy=cs1-cs0,
                schl_cs_plus=0.5*Itor/(2*math.pi**2), schl_cs_minus=-0.5*Itor/(2*math.pi**2),
                maxjump=jumps, maxabs_tor=max(abs(t) for t in tor), tor_end=tor[-1], ell_end=ell[-1],
                nbad=len(bad), firstbad=bad[:2])
if __name__=='__main__':
    name=sys.argv[1]
    for N in (2,-2):
        r=run(name,N, n=int(sys.argv[2]) if len(sys.argv)>2 else 400)
        print({k:(round(v,6) if isinstance(v,float) else v) for k,v in r.items()})
