# Claim 3: reversed side, -Sigma with aK > P; targeted by band.
import random, json, sys
from math import gcd, prod
from fractions import Fraction as Fr
from multiprocessing import Pool
from famscan import Ymember, job, nontorus
if __name__=="__main__":
    random.seed(int(sys.argv[1])); PMAX=int(sys.argv[2]); per=int(sys.argv[3]); out=sys.argv[4]
    pairs=[(x,y) for x in range(2,PMAX) for y in range(x+1,PMAX) if gcd(x,y)==1 and x*y<=PMAX]
    fams=set()
    for lo,hi in [(1,2),(2,3),(3,4),(4,6)]:
        cnt=0; tries=0
        while cnt<per and tries<100000:
            tries+=1
            aj,ak=random.choice(pairs); P=aj*ak
            aK=random.randrange(lo*P+1,hi*P)
            t=(aj,ak,aK)
            if gcd(aK,P)!=1 or not nontorus(t): continue
            if (t,2) in fams: continue
            fams.add((t,2)); cnt+=1
    for t in [(2,5,23),(3,13,119)]: fams.add((t,2))
    fams=sorted(fams)
    tasks=sorted({Ymember(t,K,n,-1) for t,K in fams for n in range(0,5)},key=lambda x:prod(x[1]))
    print(len(fams),len(tasks)); sys.stdout.flush()
    with Pool(4) as p: res=dict(p.imap_unordered(job,tasks,chunksize=4))
    data=[]
    for t,K in fams:
        rows=[]
        for n in range(5):
            arg=Ymember(t,K,n,-1); v=res[arg]
            rows.append(dict(o=arg[0],B=arg[1],ell=None if v[0] is None else str(v[0]),arg=v[1],N=v[2]))
        data.append(dict(A=t,K=K,o=-1,rows=rows))
    json.dump(data,open(out,"w"))
