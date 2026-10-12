# list all amphichiral closed census manifolds with homology; flag H_1 = Z/2 + odd (Rokhlin parity => or.-rev. isometry swaps
# the two spin structures => cs_SU2 in {1/4,3/4} => x = 2cs = 1/2 = 0 mod 1/2 ; x = cs would give 1/4 mod 1/2)
import snappy, warnings
warnings.filterwarnings('ignore')
from amph_closed import cs_closed
rows=[]
for M in snappy.OrientableClosedCensus:
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
        x,N=cs_closed(M)
    except Exception as e: continue
    H=M.homology(); el=[int(c) for c in H.elementary_divisors()]
    two=[e for e in el if e%2==0]
    typ = (len(two)==1 and two[0]%4==2 and 0 not in el)
    rows.append((M.name(),str(H),round(x,10),typ))
print(len(rows),'amphichiral;', sum(r[3] for r in rows),'with H1 = Z/2 + odd')
for r in rows:
    if r[3]: print('  ',r)
print('max |x mod 1/2| over all:', max(min(abs(r[2])%0.5, 0.5-abs(r[2])%0.5) for r in rows))
