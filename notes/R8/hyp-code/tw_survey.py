import snappy, warnings, math, sys, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
from tw_profile import analyse, getM
def job(nm):
    try:
        M=getM(nm)
        if not M.solution_type().startswith('all tetra'): return {'name':nm,'err':'complete not positive'}
        o=analyse(M,int(sys.argv[3]) if len(sys.argv)>3 else 60)
        for N in (2,-2): o[N].pop('prof')
        o['name']=nm; return o
    except Exception as e:
        return {'name':nm,'err':str(e)[:80]}
if __name__=='__main__':
    which=sys.argv[1]; out=sys.argv[2]
    if which=='rolf':
        cnt={3:1,4:1,5:2,6:3,7:7,8:21,9:49,10:165}
        names=['%d_%d'%(c,k) for c in cnt for k in range(1,cnt[c]+1)]
    else:
        names=which.split(',')
    with Pool(4) as p: res=p.map(job,names,chunksize=4)
    json.dump(res,open(out,'w'))
    ok=[r for r in res if 'err' not in r]
    print('n',len(res),'ok',len(ok))
