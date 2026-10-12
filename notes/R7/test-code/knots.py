"""Generators and exact levels for T(p,q) and its mirror on the pillowcase model.
Levels: gap16/triangle-code/tk.py (uniform normalisation c = (3+rho)/16 for both bundles,
Seifert-framed c^tl).  Mirror: Y_N(Kbar) = -Y_{-N}(K): position (a,b) -> (a,-b), c -> 3/8 - c."""
import sys, os
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'gap16', 'triangle-code'))
import tk
from pmodel import Arc, Gen, L, V, F as FF

COMPLEX = {  # name: (family, N, twisted)
    'A0': (L(2, 0), 2, False), 'A1': (L(2, 1), 2, True),
    'B0': (L(-2, 0), -2, False), 'B1': (L(-2, 1), -2, True), 'T': (V, None, None)}

def torus(p, q, mirror=True, shift=None):
    """returns dict: arcs, gens[cx] (list of Gen), with exact levels.
    shift: optional dict arcname -> (da, db) small translation of that base arc (Thom perturbation)."""
    s = -1 if mirror else 1
    arcs = []
    for (k, l, amin, amax) in tk.arcs(p, q):
        # positive: b = k/2 - pq a ; mirror: b = pq a - k/2
        P0 = (amin, s * (F(k, 2) - p * q * amin)); P1 = (amax, s * (F(k, 2) - p * q * amax))
        name = '(%d,%d)' % (k, l)
        if shift and name in shift:
            dx, dy = shift[name]
            P0 = (P0[0] + dx, P0[1] + dy); P1 = (P1[0] + dx, P1[1] + dy)
        A = Arc(name, P0, P1); A.k, A.l = k, l
        arcs.append(A)
    # exact level tables from tk (positive knot)
    lev = {}
    for cx, (fam, N, tw) in COMPLEX.items():
        if cx == 'T':
            for x in tk.traceless(p, q):
                v = tk.ctl_via(p, q, x, tk.common_N(p, q, x)[0])['c']
                lev[(cx, x['k'], x['l'], F(1, 4))] = (F(3, 8) - v) if mirror else v
        else:
            NN = -N if mirror else N
            for g in tk.gens(p, q, NN, tw):
                lev[(cx, g['k'], g['l'], g['a'])] = (F(3, 8) - g['c']) if mirror else g['c']
    gens = {}
    for cx, (fam, N, tw) in COMPLEX.items():
        gens[cx] = []
        for A in arcs:
            pts = A.meets(fam)
            # unperturbed a-values on this arc for level matching (order along the arc preserved)
            keys = sorted([key for key in lev if key[0] == cx and key[1] == A.k and key[2] == A.l],
                          key=lambda kk: kk[3])
            assert len(keys) == len(pts), (cx, A.name, len(keys), len(pts))
            for i, (t, u) in enumerate(pts):
                key = keys[i]
                if not shift:
                    assert key[3] == u[0], (key, u)
                gens[cx].append(Gen(cx, A, t, u, lev[key], '%s a=%s b=%s' % (A.name, key[3], u[1] % 1)))
    return dict(arcs=arcs, gens=gens, p=p, q=q, mirror=mirror)

if __name__ == '__main__':
    for (p, q) in [(2, 3), (3, 5)]:
        D = torus(p, q)
        print('mirror T(%d,%d)' % (p, q))
        for cx in ['A0', 'A1', 'T', 'B0', 'B1']:
            G = sorted(D['gens'][cx], key=lambda g: g.level)
            print('  %s (%d):' % (cx, len(G)), ', '.join('%s@%s(%s,%s)' % (g.level, g.arc.name, g.u[0], g.u[1] % 1) for g in G))
