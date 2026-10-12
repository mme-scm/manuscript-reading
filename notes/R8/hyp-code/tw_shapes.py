import snappy, warnings, math, sys, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def dist_iZ(w): return math.hypot(w.real, w.imag-round(w.imag))
def feat(t):
    W=0.5j*t*t/(t*t-4); x,y=t.real,t.imag
    return dict(x=x,y=y,absT=abs(t),dW=dist_iZ(W),Dlead=(0.5j-W).imag,
                Lp=abs(2+t)/math.sqrt(y),Lm=abs(t-2)/math.sqrt(y))
from tw_frame import fix_frame
def job(args):
    tab,i=args
    try:
        M=(snappy.CensusKnots if tab=='C' else snappy.HTLinkExteriors)[i]
        if M.num_cusps()!=1: return None
        if not M.solution_type().startswith('all tetra'):
            M.randomize()
            if not M.solution_type().startswith('all tetra'): return {'name':M.name(),'err':'sol'}
        a=fix_frame(M) if tab=="C" else 0
        t=complex(M.cusp_info()[0]["shape"]); f=feat(t); f["shift"]=a; f['name']=M.name(); return f
    except Exception as e: return {'name':str(i),'err':str(e)[:60]}
if __name__=='__main__':
    tab=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3]); out=sys.argv[4]
    with Pool(4) as p: res=[r for r in p.map(job,[(tab,i) for i in range(a,b)],chunksize=50) if r]
    json.dump(res,open(out,'w'))
    ok=[r for r in res if 'err' not in r]
    print('n',len(res),'ok',len(ok))
    for key,lab in (('y','min Im tau'),('absT','min |tau|'),('dW','min dist(W_lead,iZ)')):
        s=sorted(ok,key=lambda r:r[key])[:6]
        print(lab,[(r['name'],round(r['x'],3),round(r['y'],3),round(r['dW'],4),round(r['Lp'],2),round(r['Lm'],2)) for r in s])
    s=sorted(ok,key=lambda r:-abs(r['Dlead']-round(r['Dlead'])))[:6]
    print('max |Dlead| mod 1',[(r['name'],round(r['x'],3),round(r['y'],3),round(r['Dlead'],4)) for r in s])
    sm=[r for r in ok if min(r['Lp'],r['Lm'])>=7.5832]; print('both L>=7.5832:',len(sm),'of',len(ok))
    sm=[r for r in ok if r['y']<1]; print('y<1:',len(sm), 'of which |x|<=4:',len([r for r in sm if abs(r['x'])<=4]))
