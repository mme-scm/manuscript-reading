# Closed census: amphichiral manifolds and their SnapPy CS (x = CS_conv/2pi^2, mod 1/2).
# Prediction if x = 2*cs_SU2 : x == 0 mod 1/2 for every closed amphichiral hyperbolic manifold.
# Prediction if x = cs_SU2   : x in {0, 1/4} mod 1/2 (1/4 forced when the isometry swaps spin str. with mu={1,-1}).
import snappy, warnings, sys
warnings.filterwarnings('ignore')
n=int(sys.argv[1]) if (len(sys.argv)>1 and __name__=="__main__") else 3000
def cs_closed(M):
    nm=M.name(); base=nm.split('(')[0]
    N=snappy.Manifold(base); N.chern_simons()
    N.dehn_fill([tuple(c['filling']) for c in M.cusp_info()])
    return float(N.chern_simons()), N
if __name__=='__main__':
    cnt={}; ex=[]; nam=0
    for i,M in enumerate(snappy.OrientableClosedCensus[:n]):
        try:
            G=M.symmetry_group()
            if not G.is_amphicheiral(): continue
            nam+=1
            x,N=cs_closed(M)
        except Exception as e:
            print('err',M,repr(e)[:80]); continue
        key=round(x%0.5,4)%0.5
        cnt[key]=cnt.get(key,0)+1
        if len(ex)<15: ex.append((M.name(), round(x,8), str(M.homology())))
    print('amphichiral closed among first',n,':',nam,' CS mod 1/2 histogram',cnt)
    print(ex)
