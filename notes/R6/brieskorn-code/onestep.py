"""(i) beta <= P on every class; (ii) beta(class of r) <= beta(other class);
(iii) one-step drop D_n >= m_n/(16 m_{n+1}) on link-oriented windows (families), equality cases."""
import json, sys
from fractions import Fraction as F
from math import isqrt
from collections import Counter
cl = json.load(open('rays120_closed.json'))
c = Counter()
for x in cl:
    a1,a2,r = x['key']; P=a1*a2
    b = [isqrt((F(x['B%d'%e])*16*P).numerator) for e in (0,1)]
    c[('beta<=P', max(b) <= P)] += 1
    c[('beta_even<=beta_odd', b[0] <= b[1])] += 1
print(dict(c))
c2 = Counter(); eq = []
E = lambda y: None if y['ell'] is None else F(y['ell'])
for fn in sys.argv[1:]:
    for f in json.load(open(fn)):
        i = f['i']
        ng = {int(k): v for k, v in f['neg'].items()}
        for n in range(1, 6):
            y0, y1 = ng[n], ng[n+1]
            if y0['s'] != 1 or y1['s'] != 1 or E(y0) is None or E(y1) is None: continue
            m0, m1 = y0['A'][i], y1['A'][i]
            D = E(y0) - E(y1); bound = F(m0, 16*m1)
            c2[('D >= m_n/(16 m_n+1)', D >= bound)] += 1
            if D == bound: c2['equality'] += 1
print(dict(c2))
