import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/gap16/triangle-code')
from tk import gens
from fractions import Fraction as Fr
from collections import Counter
for (p,q) in [(2,3),(2,5),(3,4)]:
    for N in [2,-2]:
        G = gens(p,q,N)
        cs = sorted((g['CSD'] for g in G))
        # chi pairs: CS differs by 1/2
        S = Counter(g['CSD'] for g in G)
        paired = all(S[(c+Fr(1,2))%1] == S[c] for c in S)
        grs = Counter(int(g['gr']) % 8 for g in G)
        print('T(%d,%d) N=%+d  #gens=%d  chi-paired(CS+1/2)=%s  gr mod 8 counts=%s' % (p,q,N,len(G),paired,dict(sorted(grs.items()))))
