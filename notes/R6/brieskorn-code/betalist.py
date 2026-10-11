import json
from fractions import Fraction as F
from math import isqrt
cl = json.load(open('rays120_closed.json'))
by = {}
for x in cl:
    a1,a2,r = x['key']; P=a1*a2
    b = [isqrt((F(x['B%d'%e])*16*P).numerator) for e in (0,1)]
    by.setdefault((a1,a2),[]).append((r,b,F(x['A0'])))
for pair in [(3,5),(3,7),(5,7),(3,11),(3,13),(5,9),(3,4),(4,5),(2,9)]:
    P=pair[0]*pair[1]
    print(pair, "P=%d"%P)
    for r,b,A in sorted(by[pair]):
        zero = 'ZERO(m even class)' if 0 in b else ''
        print("   r=%3d  r^-1 mod P=%3d  beta(even j, odd j)=%s  A=%s %s" % (r, pow(r,-1,P), b, A, zero))
