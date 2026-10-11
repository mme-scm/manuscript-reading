import json
from fractions import Fraction as F
from math import isqrt
from collections import Counter
cl = json.load(open('rays120_closed.json'))
c = Counter(); ev = Counter(); zr = Counter(); ex=[]
for x in cl:
    a1,a2,r = x['key']; P=a1*a2
    b = [isqrt((F(x['B%d'%e])*16*P).numerator) for e in (0,1)]
    if P % 2:
        c[('P odd', b[0]+b[1]==P)] += 1
        # zero beta: which class, r parity
        if 0 in b:
            zr[('r even' if r%2==0 else 'r odd', 'zero on class of j even' if b[0]==0 else 'zero on j odd')] += 1
        else:
            zr[('no zero', 'r even' if r%2==0 else 'r odd')] += 1
    else:
        ev[(b[0]+b[1]==P, b[0]+b[1]==P-2, (b[0]+b[1]) % 2 == 0, b[0]%2==1 and b[1]%2==1)] += 1
        if b[0]+b[1] not in (P, P-2) and len(ex)<12: ex.append(((a1,a2,r), b))
print("odd P: beta_even + beta_odd == P:", dict(c))
print("odd P zeros:", dict(zr))
print("even P: (sum==P, sum==P-2, sum even, both odd):", dict(ev), ex)
