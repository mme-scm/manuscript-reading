"""Classify families by (s, a_K < P or a_K > P) and list failures / equality cases.
Usage: python3 classify.py FILE.json"""
import sys, json
from fractions import Fraction as F
from collections import defaultdict, Counter

fams = json.load(open(sys.argv[1]))
E = lambda y: None if y['ell'] is None else F(y['ell'])


def name(f):
    return "%sS(%s) K=%d" % ('+' if f['s'] == 1 else '-', ",".join(map(str, f['A'])), f['aK'])


def kind(f):
    A = f['A']; a = A[0] * A[1] * A[2]; P = a // f['aK']
    if f['s'] == 1:
        return 'L+'                 # link orientation: Y_{-1/n} = Sigma(.., a_K + nP, ..)
    return 'L-' if f['aK'] < P else 'R-'   # L-: Y_{-1/n} = Sigma(.., nP - a_K, ..) ; R-: first ones are -Sigma


groups = defaultdict(list)
for f in fams:
    neg = {int(k): E(v) for k, v in f['neg'].items()}
    if any(v is None for v in neg.values()):
        groups['skip'].append(f)
        continue
    f['_neg'] = neg
    groups[kind(f)].append(f)

for k in ('L+', 'L-', 'R-'):
    G = groups[k]
    if not G:
        continue
    T1 = [f['_neg'][1] - f['_neg'][3] for f in G]
    dec = sum(f['_neg'][1] > f['_neg'][2] > f['_neg'][3] for f in G)
    print("%s: %d families; (a) holds %d; min T1 = %s (%.5f); #T1<1/8 = %d; #T1=1/8 = %d; min D1 = %.5f; min D2 = %.5f"
          % (k, len(G), dec, min(T1), float(min(T1)), sum(t < F(1, 8) for t in T1), sum(t == F(1, 8) for t in T1),
             min(float(f['_neg'][1] - f['_neg'][2]) for f in G), min(float(f['_neg'][2] - f['_neg'][3]) for f in G)))
print("skipped (S^3 or lens among Y_{-1/n}):", len(groups['skip']))

# R- detail: where does the failure sit relative to the orientation switch n* = ceil(a_K/P)?
print("\nR- families: a_K/P, (a)?, T1, and the orientations of Y_{-1},Y_{-1/2},Y_{-1/3}")
cnt = Counter()
for f in groups['R-']:
    A = f['A']; a = A[0] * A[1] * A[2]; P = a // f['aK']
    ori = "".join('+' if f['neg'][str(n)]['s'] == 1 else '-' for n in (1, 2, 3))
    ok = f['_neg'][1] > f['_neg'][2] > f['_neg'][3]
    T1 = f['_neg'][1] - f['_neg'][3]
    cnt[(ori, ok, T1 >= F(1, 8))] += 1
print("  (orientations of Y_-1,Y_-1/2,Y_-1/3 ; (a) holds ; T1>=1/8) -> count")
for k, v in sorted(cnt.items()):
    print("   ", k, v)
