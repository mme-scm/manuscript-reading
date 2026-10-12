"""Check: for each return (x -a-> tau -gM-> x), the a-triangle and the gM-quadrilateral glue along the
Gamma-chord tau--x into the mixed triangle (pA, pB, q) of omega-area 1/16, with x on the edge q--pA and
tau on the edge pA--pB."""
import sys
from fractions import Fraction as F
from knots import torus
from study import study
from pmodel import area, cross
def on_seg(u, p, q):
    return cross(p, q, u) == 0 and min(p[0], q[0]) <= u[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= u[1] <= max(p[1], q[1])
for (p, q) in [tuple(map(int, s.split(','))) for s in sys.argv[1:]]:
    D = torus(p, q)
    for which in ('I', 'II'):
        r = study(D, which, verbose=False)
        P = r['info']['P']
        for pa in P['a']:
            for pm in P['gM']:
                if pm['src'] is pa['dst'] and pm['dst'] is pa['src'] and pa['src'].level == r['lamA']:
                    x, pA, tau = pa['verts']; tau2, pB, qq, x2 = pm['verts']
                    tri = [pA, pB, qq]
                    print('mT(%d,%d) (%s): x=%s tau=%s : union triangle pA=%s pB=%s q=%s area=%s ; x on [q,pA]: %s ; tau on [pA,pB]: %s ; areas %s + %s' % (
                        p, q, which, x, tau, pA, pB, qq, abs(area(tri)), on_seg(x, qq, pA), on_seg(tau, pA, pB), pa['area'], pm['area']))
