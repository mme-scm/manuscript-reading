"""Analysis of chains (ray.py output).  Usage: python3 rayan.py rays.json
Window W_j = (Z_j, Z_{j+1}, Z_{j+2}) = (Y_{-1}, Y_{-1/2}, Y_{-1/3}) for the base Z_{j-1}."""
import sys, json
from fractions import Fraction as F
from collections import Counter, defaultdict

chains = json.load(open(sys.argv[1]))
EIGHTH = F(1, 8)
for ch in chains:
    ch['Z'] = {int(k): v for k, v in ch['Z'].items()}
    ch['ell'] = {k: (None if v['ell'] is None else F(v['ell'])) for k, v in ch['Z'].items()}
    # Casson along the chain: lambda(Z_{k+1}) = lambda(Z_k) - a2(T(a1,a2))
    a2T = F((ch['a1'] ** 2 - 1) * (ch['a2'] ** 2 - 1), 24)
    lam = {k: F(-v['s'] * v['count'], 2) for k, v in ch['Z'].items()}
    for k in lam:
        if k + 1 in lam:
            assert lam[k + 1] == lam[k] - a2T, (ch['a1'], ch['a2'], ch['r'], k)
print("Casson surgery formula along all %d chains: OK" % len(chains))

ks = sorted(chains[0]['Z'])
KMIN, KMAX = ks[0], ks[-1]


def name(ch, j):
    v = ch['Z'][j]
    return "%sS(%d,%d,%d)" % ('+' if v['s'] == 1 else '-', *v['A'])


def tl(ch, j):
    return any(m['traceless'] for m in ch['Z'][j]['min'])


for tor in (False, True):
    print("\n########## %s chains" % ("TORUS-KNOT (r=+-1 mod P)" if tor else "NON-TORUS"))
    C = [ch for ch in chains if ch['torus'] == tor]
    # Link-oriented windows j >= 0
    stats = Counter()
    minD1 = minD2 = minT = None
    eq = []
    tlc = Counter()
    for ch in C:
        L = ch['ell']
        for j in range(0, KMAX - 1):
            if L[j] is None:
                continue
            a, b, c = L[j], L[j + 1], L[j + 2]
            stats['win'] += 1
            stats['a'] += (a > b > c)
            T = a - c
            stats['T<1/8'] += T < EIGHTH
            stats['T=1/8'] += T == EIGHTH
            if minT is None or T < minT[0]:
                minT = (T, name(ch, j))
            if minD1 is None or a - b < minD1[0]:
                minD1 = (a - b, name(ch, j), name(ch, j + 1))
            tlc[(T == EIGHTH, tl(ch, j) and tl(ch, j + 2))] += 1
            if T == EIGHTH:
                eq.append((ch['a1'], ch['a2'], ch['r'], j))
    print("LINK-ORIENTED windows (Z_j,Z_j+1,Z_j+2 all +Sigma, j=0..%d): %d windows; (a) holds %d; T<1/8: %d; T=1/8: %d"
          % (KMAX - 2, stats['win'], stats['a'], stats['T<1/8'], stats['T=1/8']))
    print("   min T = %s at %s;  min one-step drop = %s (%.5f) %s -> %s" % (minT[0], minT[1], minD1[0], float(minD1[0]), minD1[1], minD1[2]))
    print("   (T==1/8, traceless minimisers at both ends) ->", dict(tlc))
    # equality: which chains, which j
    byc = defaultdict(list)
    for a1, a2, r, j in eq:
        byc[(a1, a2, r)].append(j)
    print("   equality chains (a1,a2,r): j-list   [%d chains]" % len(byc))
    for key in sorted(byc)[:40]:
        print("     ", key, byc[key])
    # reversed / straddling windows
    st = Counter()
    worst = None
    for ch in C:
        L = ch['ell']
        for j in range(KMIN, 0):
            if j + 2 > KMAX or any(L[x] is None for x in (j, j + 1, j + 2)):
                continue
            a, b, c = L[j], L[j + 1], L[j + 2]
            pos = "".join('+' if ch['Z'][x]['s'] == 1 else '-' for x in (j, j + 1, j + 2))
            st[(pos, 'a ok' if a > b > c else 'a FAILS', 'T>=1/8' if a - c >= EIGHTH else 'T<1/8')] += 1
            if worst is None or a - c < worst[0]:
                worst = (a - c, name(ch, j), name(ch, j + 1), name(ch, j + 2))
    print("WINDOWS touching the reversed part: (orientations, (a), T) -> count")
    for k, v in sorted(st.items()):
        print("    ", k, v)
    print("   most negative T:", worst)
