import snappy, warnings, sys, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def job(nm):
    try:
        M=snappy.HTLinkExteriors[nm]
        hfk=M.link().knot_floer_homology()
        A={}
        for (a,m),r in hfk['ranks'].items(): A[a]=A.get(a,0)+(-1)**m*r
        A={a:c for a,c in A.items() if c}
        if A=={0:1} or A=={0:-1}:
            return (nm, hfk['seifert_genus'], hfk['fibered'], hfk['tau'])
    except Exception as e:
        return (nm,'err',str(e)[:80])
    return None
if __name__=='__main__':
    names=['K11n%d'%k for k in range(1,186)]+['K12n%d'%k for k in range(1,889)]+['K13n%d'%k for k in range(1,5111)]
    with Pool(4) as p: res=[r for r in p.map(job,names,chunksize=20) if r]
    json.dump(res,open('D1.json','w')); print(res)
