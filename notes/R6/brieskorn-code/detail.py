"""Detailed analysis by exterior type.  Usage: python3 detail.py FILE1.json [FILE2.json ...]
Exterior of K_i: Seifert over D^2(a_j,a_k), P = a_j a_k, r = a_i mod P.
  torus-knot exterior  <=>  r = +-1 mod P.
Kinds: L+ (s=+1), L- (s=-1, a_K<P), R- (s=-1, a_K>P)."""
import sys, json
from fractions import Fraction as F
from collections import defaultdict, Counter

fams = []
for fn in sys.argv[1:]:
    fams += json.load(open(fn))
E = lambda y: None if y['ell'] is None else F(y['ell'])
seen = set()
U = []
for f in fams:
    key = (tuple(f['A']), f['s'], f['i'])
    if key in seen:
        continue
    seen.add(key)
    neg = {int(k): E(v) for k, v in f['neg'].items()}
    if any(v is None for v in neg.values()):
        continue
    A = f['A']; a = A[0] * A[1] * A[2]; P = a // f['aK']
    f['P'] = P
    f['r'] = f['aK'] % P
    f['torusext'] = f['r'] in (1 % P, (P - 1) % P)
    f['kind'] = 'L+' if f['s'] == 1 else ('L-' if f['aK'] < P else 'R-')
    f['_neg'] = neg
    U.append(f)


def name(f):
    return "%sS(%s),K=%d" % ('+' if f['s'] == 1 else '-', ",".join(map(str, f['A'])), f['aK'])


def tl(y):
    """traceless flags of all minimisers at the surgered fibre"""
    return "".join('T' if m['traceless'] else '.' for m in y['min'])


for tor in (False, True):
    print("\n################ %s exteriors" % ("TORUS-KNOT" if tor else "NON-TORUS"))
    for kind in ('L+', 'L-', 'R-'):
        G = [f for f in U if f['torusext'] == tor and f['kind'] == kind]
        if not G:
            continue
        T1 = lambda f: f['_neg'][1] - f['_neg'][3]
        D1 = lambda f: f['_neg'][1] - f['_neg'][2]
        D2 = lambda f: f['_neg'][2] - f['_neg'][3]
        print("\n== %s: %d families. (a) holds in %d. T1: min %s, #<1/8 %d, #=1/8 %d.  D1 min %s (%.5f) [%s]; D2 min %s (%.5f) [%s]"
              % (kind, len(G), sum(f['_neg'][1] > f['_neg'][2] > f['_neg'][3] for f in G),
                 min(map(T1, G)), sum(T1(f) < F(1, 8) for f in G), sum(T1(f) == F(1, 8) for f in G),
                 min(map(D1, G)), float(min(map(D1, G))), name(min(G, key=D1)),
                 min(map(D2, G)), float(min(map(D2, G))), name(min(G, key=D2))))
        eq = [f for f in G if T1(f) == F(1, 8)]
        if eq:
            print("   T1 = 1/8 cases (name, P, r, a'_K at n=1,3, traceless flags of minimisers at n=1,2,3):")
            for f in eq[:60]:
                print("     %-26s P=%-4d r=%-4d a'=%s,%s  TL=%s|%s|%s  ell=%s,%s,%s" % (
                    name(f), f['P'], f['r'], f['neg']['1']['A'][f['i']], f['neg']['3']['A'][f['i']],
                    tl(f['neg']['1']), tl(f['neg']['2']), tl(f['neg']['3']),
                    f['_neg'][1], f['_neg'][2], f['_neg'][3]))
        # traceless statistics: is T1 == 1/8 iff minimisers traceless at both ends?
        c = Counter()
        for f in G:
            t1 = any(m['traceless'] for m in f['neg']['1']['min'])
            t3 = any(m['traceless'] for m in f['neg']['3']['min'])
            c[(T1(f) == F(1, 8), t1 and t3)] += 1
        print("   (T1==1/8, minimisers traceless at n=1 and n=3) -> count:", dict(c))
        if kind == 'R-':
            bad = [f for f in G if not (f['_neg'][1] > f['_neg'][2] > f['_neg'][3])]
            for f in bad[:40]:
                ori = "".join('+' if f['neg'][str(n)]['s'] == 1 else '-' for n in (1, 2, 3, 4))
                print("     (a) FAILS %-24s P=%d r=%d  orient(Y-1..Y-1/4)=%s  ell=%s" % (
                    name(f), f['P'], f['r'], ori, [str(f['_neg'][n]) for n in (1, 2, 3, 4)]))
