"""Coordinator request: generator-level level differences at common / chi-related pillowcase points,
the exactly-1/16 pairs, and (for mirror T(3,5)) mixed pairs with difference in [1/16, 1/8].
Bundles: A0 = (Y_2,P0), A1 = (Y_2,P1), B0 = (Y_-2,P0), B1 = (Y_-2,P1), T = traceless.
Mixed pairs: (A0,B1) [m1 type], (A1,B0) [m2 type]."""
from fractions import Fraction as F
from knots import torus
from pmodel import canon

HALF = F(1, 2)
def chi(u):
    return canon((HALF - u[0], -u[1]))

def table_torus(p, q, mirror=True):
    D = torus(p, q, mirror=mirror)
    rows = []
    for cx in ('A0', 'A1', 'T', 'B0', 'B1'):
        for g in D['gens'][cx]:
            s = (g.arc.d[1] / g.arc.d[0])
            rows.append(dict(cx=cx, level=g.level, pt=canon(g.u), arc=g.arc.name, slope=s))
    return rows

def fig8_rows():
    """4_1 (numerics of gap16/pillowcase-code/fig8_curve.npy, levels exact from Seifert data;
    branch labels: br+ = branch through (1/4,0) with slope +2 sqrt5, br- with slope -2 sqrt5;
    the A0 points lie on br+, the B0 points on br-; c^tl from the pillowcase rule Phi + sgn(slope)/16)."""
    x = (0.17800, -0.35615 % 1); xc = (0.32196, 0.35586)
    z = (0.32200, 0.64385); zc = (0.17804, 0.35586)
    r = []
    for pt in (x, xc):
        r.append(dict(cx='A0', level=F(19, 80), pt=pt, arc='br+', slope=6.94))
    for pt in (z, zc):
        r.append(dict(cx='B0', level=F(11, 80), pt=pt, arc='br-', slope=-6.94))
    bd = (F(1, 4), F(0))
    r += [dict(cx='A1', level=F(1, 5), pt=bd, arc='br+', slope=4.472), dict(cx='A1', level=F(3, 10), pt=bd, arc='br-', slope=-4.472),
          dict(cx='B1', level=F(3, 40), pt=bd, arc='br+', slope=4.472), dict(cx='B1', level=F(7, 40), pt=bd, arc='br-', slope=-4.472),
          dict(cx='T', level=F(1, 5), pt=bd, arc='br+', slope=4.472), dict(cx='T', level=F(7, 40), pt=bd, arc='br-', slope=-4.472)]
    return r

def samept(u, v):
    if isinstance(u[0], float) or isinstance(v[0], float):
        return abs(float(u[0]) - float(v[0])) < 1e-3 and abs((float(u[1]) - float(v[1]) + 0.5) % 1 - 0.5) < 1e-3
    return u == v

def chipt(u):
    if isinstance(u[0], float):
        return (0.5 - u[0], (-u[1]) % 1)
    return chi(u)

PAIRS = [('A0', 'B1', 'mixed P0->P1'), ('A1', 'B0', 'mixed P1->P0'), ('A0', 'B0', 'same P0'), ('A1', 'B1', 'same P1'),
         ('A0', 'T', 'Y2 P0 / traceless'), ('A1', 'T', 'Y2 P1 / traceless'), ('T', 'B0', 'traceless / Y-2 P0'), ('T', 'B1', 'traceless / Y-2 P1')]

def report(rows, name):
    print('==== %s' % name)
    for (c1, c2, lab) in PAIRS:
        out = []
        for r1 in rows:
            if r1['cx'] != c1: continue
            for r2 in rows:
                if r2['cx'] != c2: continue
                rel = 'same' if samept(r1['pt'], r2['pt']) else ('chi' if samept(chipt(r1['pt']), r2['pt']) else None)
                if rel is None: continue
                if rel == 'same' and r1['arc'] != r2['arc']:
                    rel = 'same pt, other branch/arc'
                out.append((rel, r1['level'] - r2['level'], r1['pt'], r1['arc'], r2['arc']))
        vals = sorted({(o[0], o[1]) for o in out}, key=lambda t: (t[0], t[1]))
        print('  %-20s %s' % (c1 + '-' + c2 + ' (' + lab + ')', '; '.join('%s: %s' % (a, b) for a, b in vals) if vals else 'no common points'))

def exact16(rows, name):
    print('  pairs with level difference exactly 1/16 (any positions):')
    for (c1, c2, lab) in PAIRS[:2]:
        for r1 in rows:
            if r1['cx'] != c1: continue
            for r2 in rows:
                if r2['cx'] == c2 and r1['level'] - r2['level'] == F(1, 16):
                    print('     %s %s @%s (%s) - %s %s @%s (%s)' % (c1, r1['level'], r1['pt'], r1['arc'], c2, r2['level'], r2['pt'], r2['arc']))

if __name__ == '__main__':
    R = table_torus(2, 3); report(R, 'mirror T(2,3)'); exact16(R, '')
    R = fig8_rows(); report(R, '4_1'); exact16(R, '')
    R = table_torus(3, 5); report(R, 'mirror T(3,5) (det 1)'); exact16(R, '')
    print('  mirror T(3,5): mixed pairs with c(Y2) - c(Y-2) in [1/16, 1/8]:')
    for (c1, c2, lab) in PAIRS[:2]:
        L = []
        for r1 in R:
            if r1['cx'] != c1: continue
            for r2 in R:
                if r2['cx'] != c2: continue
                d = r1['level'] - r2['level']
                if F(1, 16) <= d <= F(1, 8):
                    L.append((d, r1, r2))
        L.sort(key=lambda t: (t[1]['level'], t[0]))
        print('   %s (%s): %d pairs' % (c1 + '-' + c2, lab, len(L)))
        for d, r1, r2 in L:
            print('      d=%-9s(%.4f)  %s %s@(%s,%s)%s  ->  %s %s@(%s,%s)%s' % (d, float(d), c1, r1['level'], r1['pt'][0], r1['pt'][1], r1['arc'],
                                                                          c2, r2['level'], r2['pt'][0], r2['pt'][1], r2['arc']))
