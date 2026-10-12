import snappy, warnings, math, sys, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def path(M, N, n):
    tors=[]; ells=[]; worst='all tetrahedra positively oriented'
    for k in range(1,n+1):
        s=k/n; X=M.copy(); X.dehn_fill((N/s,1/s)); st=X.solution_type()
        if not st.startswith('all tetra'): worst=st
        h=complex(X.cusp_info()[0]['holonomies'][0]); tors.append(h.imag); ells.append(abs(h.real))
    da=2*math.pi/n
    I=da*(sum(tors)-0.5*tors[-1])/(4*math.pi**2)
    IV=-0.5*da*(sum(ells)-0.5*ells[-1])
    jump=max(abs(tors[i+1]-tors[i]) for i in range(n-1))
    return I, IV, max(abs(t) for t in tors), jump, worst
def job(name):
    try:
        M=snappy.Manifold(name)
        if M.solution_type()!='all tetrahedra positively oriented': return None
        V0=float(M.volume()); c0=float(M.chern_simons())
        out={'name':name}
        for N in (2,-2):
            X=M.copy(); X.dehn_fill((N,1))
            I,IV,mt,jump,worst=path(M,N,int(sys.argv[2]) if len(sys.argv)>2 else 60)
            dcs=float(X.chern_simons())-c0
            r=(dcs-I)*2; mod=abs(r-round(r))  # check I == dcs mod 1/2
            out[N]=dict(I=I,dV=float(X.volume())-V0,IV=IV,maxtor=mt,jump=jump,worst=worst,modchk=mod,st=X.solution_type())
        out['Delta']=out[2]['I']-out[-2]['I']
        return out
    except Exception as e:
        return {'name':name,'err':str(e)}
if __name__=='__main__':
    maxc=int(sys.argv[1])
    names=[]
    if maxc<=10:
        cnt={3:1,4:1,5:2,6:3,7:7,8:21,9:49,10:165}
        names=['%d_%d'%(c,k) for c in cnt if c<=maxc for k in range(1,cnt[c]+1)]
    else:
        names=sys.argv[3].split(',')
    with Pool(8) as p: res=p.map(job,names,chunksize=4)
    res=[r for r in res if r]
    json.dump(res,open(f'survey{maxc}.json','w'))
    ok=[r for r in res if 'err' not in r]
    print('n',len(res),'ok',len(ok))
    bad=[r for r in ok if r[2]['modchk']>1e-3 or r[-2]['modchk']>1e-3]
    print('Schlafli/SnapPy mismatches (mod 1/2):',len(bad), [b['name'] for b in bad[:10]])
    D=sorted(ok,key=lambda r:-abs(r['Delta']))
    print('max |Delta|:',[(r['name'],round(r['Delta'],4)) for r in D[:8]])
    mt=sorted(ok,key=lambda r:-(r[2]['maxtor']+r[-2]['maxtor']))
    print('max sup|tau2|+sup|tau-2|:',[(r['name'],round(r[2]['maxtor']+r[-2]['maxtor'],3)) for r in mt[:8]])
    nonpos=[r['name'] for r in ok if not (r[2]['worst'].startswith('all') and r[-2]['worst'].startswith('all'))]
    print('paths with non-positively-oriented solutions:',len(nonpos))
