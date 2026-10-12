"""Chain-level listing of all maps (generators, levels, polygons, areas, corners) for one instance."""
import sys
from fractions import Fraction as F
from knots import torus
from study import study, degeneracies
EPS = F(1, 10 ** 6)
def show(p, q, which, sgn=1, maps=('a','b','c','gAs','gAn','gM','gB'), only_bottom=False):
    D = torus(p, q)
    deg = degeneracies(D, which); tol = 0
    if deg:
        D = torus(p, q, shift={A.name: (0, sgn * EPS) for A in D['arcs']}); tol = F(1, 1000)
    r = study(D, which, tol=tol, verbose=False)
    I = r['info']
    print('#### mirror T(%d,%d) triangle (%s)%s; degeneracies: %s' % (p, q, which, ' perturbed db=%+d eps' % sgn if deg else '', deg))
    for nm, G in (('A', I['A']), ('T', I['T']), ('B', I['B'])):
        print('  %s: ' % nm + ', '.join('%s@(%s,%s)%s' % (g.level, g.label.split('a=')[1].split(' ')[0], g.label.split('b=')[1], g.arc.name) for g in sorted(G, key=lambda g: g.level)))
    lam = r['lamA']
    for k in maps:
        L = I['P'][k]
        if only_bottom:
            L = [P for P in L if P['src'].level <= lam + F(1,8) or P['dst'].level <= lam + F(1, 8)]
        print('  %s (%d polygons):' % (k, len(I['P'][k])))
        for P in sorted(L, key=lambda P: (P['src'].level, P['dst'].level)):
            print('     %s %s -> %s %s  area=%s(%.5f) corners=%s' % (P['src'].level, P['src'].label, P['dst'].level, P['dst'].label, P['area'] if not deg else '~', float(P['area']),
                  [(str(c[0]), str(c[1])) for c in P['corners']]))
if __name__ == '__main__':
    p, q = int(sys.argv[1]), int(sys.argv[2])
    for which in ('I', 'II'):
        show(p, q, which, only_bottom=(p*q > 6))
