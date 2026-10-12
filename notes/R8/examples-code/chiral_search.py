import snappy, warnings, json, sys
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def gcd(a,b):
    while b: a,b=b,a%b
    return abs(a)
B=6
SL=[(p,q) for p in range(-B,B+1) for q in range(0,B+1) if gcd(p,q)==1 and not (q==0 and p!=1)]
def job(i):
    try:
        E=snappy.OrientableCuspedCensus(num_cusps=1)[i]
        nm=E.name(); E.chern_simons()
        rows=[]
        for sl in SL:
            X=E.copy(); X.dehn_fill(sl)
            if not X.solution_type().startswith('all tetrahedra positively'): continue
            v=float(X.volume())
            if v<0.9: continue
            cs=float(X.chern_simons())%0.5
            rows.append((sl,round(v,8),cs))
        cands=[]
        for a in range(len(rows)):
            for b in range(a+1,len(rows)):
                s1,v1,c1=rows[a]; s2,v2,c2=rows[b]
                if abs(v1-v2)<2e-8:
                    t=(c1+c2)%0.5; t=min(t,0.5-t)
                    y=c1%0.25; y=min(y,0.25-y)
                    if t<1e-7 and y>1e-5: cands.append((s1,s2,v1,c1,c2))
        return (nm,cands) if cands else None
    except Exception as e:
        return ('ERR%d'%i,str(e)[:50])
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2])
    with Pool(8) as P: res=[r for r in P.imap(job,range(a,b),chunksize=25) if r]
    json.dump(res,open('chiral_%d_%d.json'%(a,b),'w'))
    print(len(res)); 
    for r in res[:60]: print(r)
