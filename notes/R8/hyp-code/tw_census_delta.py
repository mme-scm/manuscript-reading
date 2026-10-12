import snappy, warnings, math, sys, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
from tw_profile import analyse
from tw_frame import fix_frame
def job(nm):
    try:
        M=snappy.Manifold(nm); fix_frame(M)
        o=analyse(M,int(sys.argv[2]) if len(sys.argv)>2 else 80)
        for N in (2,-2): o[N].pop('prof')
        o['name']=nm; return o
    except Exception as e: return {'name':nm,'err':str(e)[:80]}
if __name__=='__main__':
    names=sys.argv[1].split(',') if not sys.argv[1].endswith('.json') else None
    if names is None:
        R=[r for r in json.load(open(sys.argv[1])) if 'err' not in r]
        R=sorted(R,key=lambda r:r['dW']); names=[r['name'] for r in R[:int(sys.argv[3])]]
    with Pool(4) as p: res=p.map(job,names)
    json.dump(res,open('tw_census_delta.json','w'))
    for o in res:
        if 'err' in o: print(o); continue
        d=o['Z'][1]; dl=o['Zlead'][1]
        print('%-9s tau=%+.3f%+.3fi D=%.4f Dlead=%.4f |Z-Zl|=%.4f win=%.3f,%.3f L=%.2f,%.2f worst=%s,%s'%(o['name'],*o['tau'],d,dl,
              abs(complex(*o['Z'])-complex(-o['Zlead'][0],o['Zlead'][1])),o[2]['window'],o[-2]['window'],o[2]['L'],o[-2]['L'],o[2]['worst'][:8],o[-2]['worst'][:8]))
