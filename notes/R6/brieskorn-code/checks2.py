"""(1) r=2, odd P => beta_even = 0 (ell(Sigma(p,q,2+2jpq)) = ell(Sigma(2,p,q)) - j/8);
   (2) even P => no beta = 0;  (3) positive torus knots: A = 3/8 - 5/(16pq), beta = 3 (j even), pq-3 (j odd);
   (4) mirror odd-odd torus knots r = P-1: beta_even = 0."""
import json
from fractions import Fraction as F
from math import isqrt
from collections import Counter
cl = json.load(open('rays120_closed.json'))
c = Counter()
for x in cl:
    a1,a2,r = x['key']; P=a1*a2
    b = [isqrt((F(x['B%d'%e])*16*P).numerator) for e in (0,1)]
    A = F(x['A0'])
    if r == 2 and P % 2: c[('r=2,P odd: beta_even==0', b[0]==0)] += 1
    if P % 2 == 0: c[('P even: no zero beta', 0 not in b)] += 1
    if r == 1: c[('T(p,q): A==3/8-5/(16P) and beta==(3,P-3)', A == F(3,8)-F(5,16*P) and b == [3, P-3])] += 1
    if r == P-1 and P % 2: c[('mT odd-odd: beta_even==0', b[0]==0)] += 1

for k,v in sorted(c.items(), key=str): print(k, v)
# mirror even torus knots betas
for x in cl:
    a1,a2,r = x['key']; P=a1*a2
    if r == P-1 and P % 2 == 0 and P <= 60:
        b = [isqrt((F(x['B%d'%e])*16*P).numerator) for e in (0,1)]
        print("  mT(%d,%d): A=%s beta(j even, j odd)=%s" % (a1,a2,x['A0'],b))
