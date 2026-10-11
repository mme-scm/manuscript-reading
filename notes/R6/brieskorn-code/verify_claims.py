import json, sys
from fractions import Fraction as F
from collections import Counter
E = lambda y: None if y['ell'] is None else F(y['ell'])
c = Counter(); mins = {}
for fn in sys.argv[1:]:
    for f in json.load(open(fn)):
        A, s, i = f['A'], f['s'], f['i']; P = A[0]*A[1]*A[2]//A[i]
        kind = 'L+' if s == 1 else ('L-' if A[i] < P else 'R-')
        ng = {int(k): v for k, v in f['neg'].items()}; ps = {int(k): v for k, v in f['pos'].items()}
        if any(E(v) is None for v in ng.values()): continue
        L = [E(ng[n]) for n in range(1, 7)]
        c[(kind, 'strict decr n=1..6', all(L[t] > L[t+1] for t in range(5)))] += 1
        b, y1, p1 = E(f['base']), E(ng[1]), E(ps[1])
        if b is not None:
            c[(kind, 'ell(Sigma) > ell(Y-1)', b > y1)] += 1
            if p1 is not None:
                c[(kind, 'ell(Y+1) > ell(Sigma)', p1 > b)] += 1
        # one-step > 1/24 on link-oriented windows
        for n in range(1, 6):
            if ng[n]['s'] == 1 and ng[n+1]['s'] == 1:
                D = E(ng[n]) - E(ng[n+1])
                if kind == 'L+':
                    c[('L+', 'D_n > 1/24', D > F(1, 24))] += 1
                k = (kind, 'minD')
                if k not in mins or D < mins[k][0]: mins[k] = (D, s, tuple(A), A[i], n)
        # equality windows (link-oriented, n=1..4) and traceless
        for n in range(1, 5):
            if ng[n]['s'] == 1 and ng[n+2]['s'] == 1:
                T = E(ng[n]) - E(ng[n+2])
                tl = any(m['traceless'] for m in ng[n]['min']) and any(m['traceless'] for m in ng[n+2]['min'])
                c[('link windows n=1..4', 'T==1/8' if T == F(1,8) else 'T>1/8', 'TL' if tl else 'notTL')] += 1
for k, v in sorted(c.items(), key=str): print(k, v)
for k, v in sorted(mins.items()): print(k, v[0], float(v[0]), v[1:])
