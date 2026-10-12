"""Absorption, depth delta and the return question in the pillowcase model.
Model used (see test.md 'model rules'): c-corners {q1,q2}, gA = g^sing + g^ns (chi-symmetrised edges),
corner rule 'int', graded (M5)."""
import sys
from fractions import Fraction as F
from knots import torus
from triangle import analyse, setup
from pmodel import apply, compose, add, rank, kernel_min_level, canon

CORNERS = ('pA', 'pB', 'q1', 'q2')

def degeneracies(D, which):
    S = setup(which)
    pts = {S[k]: k for k in CORNERS}
    out = []
    for cx in S['names']:
        for g in D['gens'][cx]:
            if canon(g.u) in pts:
                out.append((cx, g.level, canon(g.u), pts[canon(g.u)]))
    return out

def fmt(x):
    return '%s (%.5f)' % (x, float(x))

def study(D, which, tol=0, verbose=True, name=''):
    I = analyse(D, which, ('q1', 'q2'), 'int', verbose=verbose, edges=2, tol=tol)
    A, T, B, M, P = I['A'], I['T'], I['B'], I['M'], I['P']
    ok = all(len(v) == 0 for v in I['rel'].values())
    lamA = min(g.level for g in A); lamB = min(g.level for g in B); mu = min(g.level for g in T)
    bottom = [g for g in A if g.level == lamA]
    kap = kernel_min_level(M['a'], A, T)
    delta = (kap - lamA) if kap is not None else None
    # is some nonzero combination of bottom generators killed by a?
    absorbed = rank({(x, y) for (x, y) in M['a'] if x in bottom}, bottom, T) == len(bottom)
    rows = []
    for x in bottom:
        cg = apply(M['c'], apply(M['gA'], {x}))
        ga = apply(M['gM'], apply(M['a'], {x}))
        ret = []
        for pa in P['a']:
            if pa['src'] is x:
                for pm in P['gM']:
                    if pm['src'] is pa['dst'] and pm['dst'] is x:
                        ret.append((pa['dst'], pa['area'], pm['area'], pm['corners']))
        rows.append(dict(x=x, ax=apply(M['a'], {x}), gAx=apply(M['gA'], {x}), cg_x=(x in cg), gma_x=(x in ga), ret=ret))
    res = dict(name=name, which=which, ok=ok, rel={k: len(v) for k, v in I['rel'].items()}, lamA=lamA, lamB=lamB, mu=mu,
               m=lamA - lamB, kappa=kap, delta=delta, absorbed=absorbed, rows=rows,
               rk={k: rank(M[k], *{'a': (A, T), 'b': (T, B), 'c': (B, A), 'gA': (A, B), 'gM': (T, A)}[k]) for k in ('a', 'b', 'c', 'gA', 'gM')},
               sizes=(len(A), len(T), len(B)), info=I)
    if verbose:
        print('== %s (%s): relations all hold: %s %s' % (name, which, ok, res['rel']))
        print('   lambda_A=%s  lambda_B=%s  mu=%s  m=lambda_A-lambda_B=%s' % (fmt(lamA), fmt(lamB), fmt(mu), fmt(lamA - lamB)))
        print('   bottom absorbed (no nonzero bottom combination in ker a): %s ; kappa=%s delta=%s' % (absorbed, kap, delta))
        for r in rows:
            print('   bottom gen %s: a x = %s ; gA x = %s ; <c gA x, x>=%d  <gM a x, x>=%d' % (
                r['x'].label, [(t.level, t.label) for t in r['ax']], [(t.level, t.label) for t in r['gAx']], r['cg_x'], r['gma_x']))
            for (t, ea, em, cor) in r['ret']:
                print('      return via tau=%s %s : eta_a=%s  E_M=%s  sum=%s  (gM corners %s)' % (t.level, t.label, ea, em, ea + em, cor))
    return res

if __name__ == '__main__':
    p, q = int(sys.argv[1]), int(sys.argv[2])
    D = torus(p, q, mirror=True)
    for which in ('I', 'II'):
        print('degeneracies:', degeneracies(D, which))
        study(D, which, name='mirror T(%d,%d)' % (p, q))
