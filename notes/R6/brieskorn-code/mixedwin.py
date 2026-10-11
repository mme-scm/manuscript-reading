"""Windows (Z_j, Z_{j+2}) with j = -1 or -2 (start reversed, end link-oriented), and reversed windows j+2 <= -2:
is T - 1/8 = beta^2/(8 m m'') (resp. T = g^2/(2 m m''))?"""
import json
from fractions import Fraction as F
from math import isqrt
from collections import Counter
chains = json.load(open('rays120.json'))
c = Counter(); mn = {}
def sq(x):
    return x >= 0 and x.denominator == 1 and isqrt(x.numerator)**2 == x.numerator
for ch in chains:
    P, r = ch['P'], ch['r']
    Z = {int(k): v for k, v in ch['Z'].items()}
    L = {k: (None if v['ell'] is None else F(v['ell'])) for k, v in Z.items()}
    for j in (-2, -1):
        if L[j] is None or L[j+2] is None: continue
        m, m2 = abs(r + j*P), abs(r + (j+2)*P)
        T = L[j] - L[j+2]
        x = (T - F(1,8))*8*m*m2
        c[('j=%d'%j, 'T-1/8 = b^2/(8mm\')', sq(x))] += 1
        key = 'j=%d'%j
        if key not in mn or T < mn[key][0]: mn[key] = (T, (ch['a1'],ch['a2'],r))
    for j in range(min(Z), -3):
        if L[j] is None or L[j+2] is None: continue
        m, m2 = abs(r + j*P), abs(r + (j+2)*P)
        T = L[j] - L[j+2]
        c[('reversed', 'T = g^2/(2mm\')', sq(T*2*m*m2))] += 1
for k, v in sorted(c.items()): print(k, v)
print("min T:", {k: (str(v[0]), float(v[0]), v[1]) for k, v in mn.items()})
