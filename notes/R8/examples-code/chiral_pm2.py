# Riemannian-level orientation-reversing condition for S^3_2(K) = -S^3_{-2}(K):  X_K = J_2 + J_-2 + 2 cs(E_K) in Z
import snappy, warnings, json, math
warnings.filterwarnings('ignore')
R=json.load(open('/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code/survey10.json'))
rows=[]
for r in R:
    if 'err' in r: continue
    M=snappy.Manifold(r['name']); c=float(M.chern_simons())
    X=r['2']['I']+r['-2']['I']+2*c
    d=abs(X-round(X))
    amph=M.symmetry_group().is_amphicheiral()
    clean=r['2']['worst'].startswith('all') and r['-2']['worst'].startswith('all')
    rows.append((d,r['name'],amph,clean,X,r['Delta']))
am=[x for x in rows if x[2]]; ch=[x for x in rows if not x[2]]
print('amphichiral:',[(n,round(d,6)) for d,n,_,_,_,_ in am])
ch.sort()
print('chiral knots: n=',len(ch),' smallest dist(X_K,Z):',[(n,round(d,4),cl) for d,n,_,cl,_,_ in ch[:8]])
import statistics
print('median dist chiral:',statistics.median(d for d,*_ in ch))
