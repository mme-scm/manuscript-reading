"""Chain-level maps of the mixed triangles in the pillowcase model (see pmodel.py for the rules).
(I)  A0 -a-> T -b-> B1 -c-> A0     lines L2^0, V, L-2^w
(II) A1 -a-> T -b-> B0 -c-> A1     lines L2^w, V, L-2^0
Topological levels: a,b: 0; c: 3/16; gA: -1/8; gM, gB: 1/16.  A polygon of omega-area E counted by a
map of topological level ell should satisfy c(out) = c(in) + ell - E ('level residual' = 0)."""
from fractions import Fraction as F
from pmodel import *

HALF = F(1, 2); Q = F(1, 4); E8 = F(1, 8)

def setup(which):
    if which == 'I':
        LA, LB = L(2, 0), L(-2, 1)
        pA, pB = (Q, HALF), (Q, F(0))                 # L2^0 cap V, V cap L-2^w
        q1, q2 = (E8, F(3, 4)), (F(3, 8), Q)          # L-2^w cap L2^0 ; q1 = gamma_1 (1/16 cap via corners)
        c0, cinf = (F(0), F(0)), (F(0), HALF)         # L2^0 cap Linf, Linf cap L-2^w (pillowcase corners)
        names = ('A0', 'T', 'B1')
    else:
        LA, LB = L(2, 1), L(-2, 0)
        pA, pB = (Q, F(0)), (Q, HALF)
        q1, q2 = (E8, Q), (F(3, 8), F(3, 4))
        c0, cinf = (F(0), HALF), (F(0), F(0))
        names = ('A1', 'T', 'B0')
    return dict(LA=LA, LB=LB, pA=pA, pB=pB, q1=q1, q2=q2, c0=c0, cinf=cinf, names=names)

TOP = dict(a=0, b=0, c=F(3, 16), gAs=-E8, gAn=-E8, gM=F(1, 16), gB=F(1, 16))

LINF2 = Fam('Linf+chi', (2, 0), 0)   # both edges a in Z/2 (L_inf and its chi-twist)

def maps(D, which, qset=('q1',), rule='int', edges=1):
    S = setup(which)
    A, T, B = (D['gens'][n] for n in S['names'])
    qs = {S[k] for k in qset}
    P = {}
    P['a'] = polygons(A, T, [S['LA'], V], [{S['pA']}], rule)
    P['b'] = polygons(T, B, [V, S['LB']], [{S['pB']}], rule)
    P['c'] = polygons(B, A, [S['LB'], S['LA']], [qs], rule)
    P['gAs'] = polygons(A, B, [S['LA'], V, S['LB']], [{S['pA']}, {S['pB']}], rule)
    if edges == 1:
        P['gAn'] = polygons(A, B, [S['LA'], LINF, S['LB']], [{S['c0']}, {S['cinf']}],
                            'free' if rule == 'free' else 'int')
    else:   # chi-symmetrised: corners on either edge a = 0 or a = 1/2
        chi = lambda u: canon((HALF - u[0], -u[1]))
        P['gAn'] = polygons(A, B, [S['LA'], LINF2, S['LB']], [{S['c0'], chi(S['c0'])}, {S['cinf'], chi(S['cinf'])}],
                            'free' if rule == 'free' else 'int')
    P['gM'] = polygons(T, A, [V, S['LB'], S['LA']], [{S['pB']}, qs], rule)
    P['gB'] = polygons(B, T, [S['LB'], S['LA'], V], [qs, {S['pA']}], rule)
    return A, T, B, P

def residuals(P):
    out = []
    for k, polys in P.items():
        for p in polys:
            r = p['dst'].level - (p['src'].level + TOP[k] - p['area'])
            out.append((k, p['src'], p['dst'], p['area'], r, p['corners']))
    return out

def analyse(D, which, qset=('q1',), rule='int', verbose=True, gA_parts=('gAs', 'gAn'), graded=True, edges=1, tol=0):
    A, T, B, P = maps(D, which, qset, rule, edges)
    if graded:   # rule M5: keep only polygons whose area equals the level drop (index-consistent)
        P = {k: [p for p in v if abs(p['dst'].level - (p['src'].level + TOP[k] - p['area'])) <= tol] for k, v in P.items()}
    Mx = {k: matrix(v) for k, v in P.items()}
    a, b, c, gM, gB = Mx['a'], Mx['b'], Mx['c'], Mx['gM'], Mx['gB']
    gA = add(*[Mx[k] for k in gA_parts])
    res = residuals(P)
    bad = [r for r in res if abs(r[4]) > tol]
    rel = {}
    rel['ba'] = compose(b, a, A, T, B)
    rel['cb'] = compose(c, b, T, B, A)
    rel['ac'] = compose(a, c, B, A, T)
    rel['vA'] = add(compose(c, gA, A, B, A), compose(gM, a, A, T, A), ident(A))
    rel['vT'] = add(compose(a, gM, T, A, T), compose(gB, b, T, B, T), ident(T))
    rel['vB'] = add(compose(b, gB, B, T, B), compose(gA, c, B, A, B), ident(B))
    info = dict(A=A, T=T, B=B, P=P, M=dict(Mx, gA=gA), res=res, bad=bad, rel=rel)
    if verbose:
        print('--- triangle (%s), c-corners %s, corner rule %s, gA = %s, graded=%s, edges=%d' % (which, qset, rule, '+'.join(gA_parts), graded, edges))
        print('  ranks: |A|=%d |T|=%d |B|=%d ; polygons: %s' % (len(A), len(T), len(B),
              ', '.join('%s:%d' % (k, len(v)) for k, v in P.items())))
        print('  rk a=%d rk b=%d rk c=%d rk gA=%d' % (rank(a, A, T), rank(b, T, B), rank(c, B, A), rank(gA, A, B)))
        print('  level residuals nonzero: %d of %d  %s' % (len(bad), len(res),
              sorted({(r[0], r[4]) for r in bad}, key=str)[:12]))
        print('  relations (number of nonzero entries): ' + ', '.join('%s:%d' % (k, len(v)) for k, v in rel.items()))
    return info
