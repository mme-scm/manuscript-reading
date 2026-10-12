"""Per-instance summary: absorption depth delta, eta_g of the first kernel class, the bracket of
Theorem 5.1, strategy16's inequality (D) delta <= 1/16 + eta_g, and the return data
(with the check that the a-triangle and the gM-quadrilateral tile a mixed triangle of area 1/16)."""
import sys, itertools
from fractions import Fraction as F
from knots import torus
from study import study, degeneracies
from pmodel import apply, rank, area

E8, E16, E316 = F(1, 8), F(1, 16), F(3, 16)
EPS = F(1, 10 ** 6)

def vec_level(v):
    return max(g.level for g in v) if v else None

def kernel_vectors(a, A, kappa):
    gens = [g for g in A if g.level <= kappa]
    out = []
    for r in range(1, len(gens) + 1):
        for S in itertools.combinations(gens, r):
            v = set(S)
            if not apply(a, v) and vec_level(v) == kappa:
                out.append(v)
        if len(out) > 200:
            break
    return out

def summarise(p, q, mirror, which, verbose=True):
    D = torus(p, q, mirror=mirror)
    deg = degeneracies(D, which)
    tol = 0
    if deg:
        D = torus(p, q, mirror=mirror, shift={A.name: (0, EPS) for A in D['arcs']}); tol = F(1, 1000)
    r = study(D, which, tol=tol, verbose=False)
    I = r['info']; M = I['M']; A, T, B = I['A'], I['T'], I['B']
    lam, lamB, m, kap, delta = r['lamA'], r['lamB'], r['m'], r['kappa'], r['delta']
    eta_g = None
    if kap is not None:
        best = None
        for v in kernel_vectors(M['a'], A, kap):
            w = apply(M['gA'], v)
            if w:
                lv = vec_level(w)
                if best is None or lv < best:
                    best = lv
        if best is not None:
            eta_g = kap - E8 - best
    window = [z for z in B if lam - E316 <= z.level <= lam - E8]
    rets = []
    for row in r['rows']:
        for (t, ea, em, cor) in row['ret']:
            # tiling check: the gM quad has corners (pB, q); the a-triangle has corner pA; union triangle pA,pB,q
            rets.append((row['x'].level, t.level, ea, em, ea + em))
    out = dict(name='%sT(%d,%d)' % ('m' if mirror else '', p, q), which=which, deg=len(deg), ok=r['ok'], lam=lam, lamB=lamB, m=m,
               absorbed=r['absorbed'], delta=delta, kappa=kap, eta_g=eta_g,
               bracket=(E8 - delta + eta_g if (delta is not None and eta_g is not None) else None, (E316 - delta) if delta is not None else None),
               D_ineq=(delta <= E16 + eta_g) if (delta is not None and eta_g is not None) else None,
               forced=(r['absorbed'] and not window), rets=rets,
               cg=[row['cg_x'] for row in r['rows']], gma=[row['gma_x'] for row in r['rows']])
    if verbose:
        f = lambda x: 'None' if x is None else '%s(%.4f)' % (x, float(x))
        print('%-9s (%-2s) deg=%d rel_ok=%s m=%s absorbed=%s delta=%s eta_g=%s bracket=[%s, %s] (D):%s window-empty(forced return)=%s <cgA>=%s <gMa>=%s returns=%s' % (
            out['name'], which, out['deg'], out['ok'], f(m), out['absorbed'], f(delta), f(eta_g), f(out['bracket'][0]), f(out['bracket'][1]),
            out['D_ineq'], out['forced'], out['cg'], out['gma'],
            ['x=%s tau=%s eta_a=%.5f E_M=%.5f sum=%.5f' % (a, b, float(c), float(d), float(e)) for (a, b, c, d, e) in rets]))
        sys.stdout.flush()
    return out

if __name__ == '__main__':
    cases = [tuple(map(int, s.split(','))) for s in sys.argv[1:]] or [(2, 3), (3, 5)]
    for (p, q) in cases:
        for which in ('I', 'II'):
            summarise(p, q, True, which)
