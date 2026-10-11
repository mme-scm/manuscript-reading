"""Answers (a)-(c) from a scan JSON.  Usage: python3 analyze.py FILE.json [label]"""
import sys, json
from fractions import Fraction as F
from collections import defaultdict

fams = json.load(open(sys.argv[1]))
label = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]
INF = None


def E(y):
    return None if y['ell'] is None else F(y['ell'])


def name(f):
    A = tuple(f['A'])
    return "%sS(%s) K=a%d(=%d)" % ('+' if f['s'] == 1 else '-', ",".join(map(str, A)), f['i'] + 1, f['aK'])


rows = []
for f in fams:
    neg = {int(k): E(v) for k, v in f['neg'].items()}
    pos = {int(k): E(v) for k, v in f['pos'].items()}
    base = E(f['base'])
    if any(v is None for v in neg.values()):
        continue
    r = dict(f=f, neg=neg, pos=pos, base=base,
             D1=neg[1] - neg[2], D2=neg[2] - neg[3], D3=neg[3] - neg[4],
             T1=neg[1] - neg[3], T2=neg[2] - neg[4], T3=neg[3] - neg[5])
    r['dec'] = all(neg[n] > neg[n + 1] for n in range(1, len(neg)))
    r['dec3'] = neg[1] > neg[2] > neg[3]
    rows.append(r)

print("== %s: %d families (Sigma x orientation x fibre)" % (label, len(rows)))
for s in (1, -1):
    R = [r for r in rows if r['f']['s'] == s]
    if not R:
        continue
    print("\n-- orientation s = %+d (%d families)" % (s, len(R)))
    print("  (a) ell(Y-1) > ell(Y-1/2) > ell(Y-1/3): %d/%d ;  strictly decreasing up to n=6: %d/%d"
          % (sum(r['dec3'] for r in R), len(R), sum(r['dec'] for r in R), len(R)))
    bad = [r for r in R if not r['dec3']]
    for r in bad[:10]:
        print("     FAIL", name(r['f']), [str(r['neg'][n]) for n in (1, 2, 3)])
    for key in ('T1', 'T2', 'T3', 'D1', 'D2', 'D3'):
        mn = min(R, key=lambda r: r[key])
        mx = max(R, key=lambda r: r[key])
        nlt = sum(r[key] < F(1, 8) for r in R)
        neq = sum(r[key] == F(1, 8) for r in R)
        print("  %s: min %s = %.5f at %s ; max %.5f at %s ; #<1/8: %d, #=1/8: %d"
              % (key, mn[key], float(mn[key]), name(mn['f']), float(mx[key]), name(mx['f']), nlt, neq))
