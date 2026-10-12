"""Scan torus knots (both chiralities, both mixed triangles) in the pillowcase model.
Degenerate instances (a generator at a corner pA, pB, q1, q2) are resolved by a small translation of
every base arc (Thom perturbation), run with both signs; levels keep their exact unperturbed values and
the grading rule M5 is applied with tolerance."""
import sys
from math import gcd
from fractions import Fraction as F
from knots import torus
from study import study, degeneracies

EPS = F(1, 10 ** 6)

def run(p, q, mirror, which, out):
    D = torus(p, q, mirror=mirror)
    deg = degeneracies(D, which)
    name = '%sT(%d,%d)' % ('m' if mirror else '', p, q)
    variants = []
    if not deg:
        variants.append(('none', D, 0))
    else:
        for sgn in (1, -1):
            sh = {A.name: (0, sgn * EPS) for A in D['arcs']}
            variants.append(('db=%+d eps' % sgn, torus(p, q, mirror=mirror, shift=sh), F(1, 1000)))
    for (vn, DD, tol) in variants:
        r = study(DD, which, tol=tol, verbose=False, name=name)
        rets = [(row['x'].label, row['cg_x'], row['gma_x'], [(t.level, ea, em) for (t, ea, em, cor) in row['ret']]) for row in r['rows']]
        line = '%-9s (%-2s) pert=%-9s deg=%d rel_ok=%-5s sizes=%s rk(a,b,c,gA,gM)=%s m=%-10s(%.4f) absorbed=%-5s delta=%s  ' % (
            name, which, vn, len(deg), r['ok'], r['sizes'], tuple(r['rk'][k] for k in ('a', 'b', 'c', 'gA', 'gM')),
            r['m'], float(r['m']), r['absorbed'], r['delta'])
        line += ' | bottom: ' + '; '.join('<cgA>=%d <gMa>=%d ret=%s' % (cg, ga, [(str(l), str(ea), str(em)) for (l, ea, em) in rt]) for (lab, cg, ga, rt) in rets)
        print(line); sys.stdout.flush()
        out.append((name, which, vn, r))

if __name__ == '__main__':
    maxpq = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    cases = [(p, q) for p in range(2, 8) for q in range(p + 1, 40) if gcd(p, q) == 1 and p * q <= maxpq]
    out = []
    for (p, q) in cases:
        for mirror in (True, False):
            for which in ('I', 'II'):
                run(p, q, mirror, which, out)
