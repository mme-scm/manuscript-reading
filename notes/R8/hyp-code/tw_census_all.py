import snappy, warnings, math, sys, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
from tw_profile import analyse
from tw_frame import fix_frame
def job(i):
    try:
        M=snappy.CensusKnots[i]; nm=M.name(); fix_frame(M)
        t=complex(M.cusp_info()[0]['shape'])
        if abs(t.real)>12: return {'name':nm,'skip':1,'tau':[t.real,t.imag]}
        o=analyse(M,60)
        for N in (2,-2):
            o[N].pop('prof')
            X=M.copy(); X.dehn_fill((N,1)); o[N]['endst']=X.solution_type()[:20]; o[N]['endvol']=float(X.volume())
        o['name']=nm; return o
    except Exception as e: return {'name':str(i),'err':str(e)[:80]}
if __name__=='__main__':
    with Pool(4) as p: res=p.map(job,range(len(snappy.CensusKnots)),chunksize=10)
    json.dump(res,open('tw_census_all.json','w')); print('done',len(res))
