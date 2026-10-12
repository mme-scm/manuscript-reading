"""4_1, triangle (II): local check at the binary-dihedral double point (1/4,0).
Each branch of Gamma near (1/4,0) is replaced by its tangent line (slope +-2 sqrt5 ~ +-559/125),
translated by db = +-eps (Thom perturbation).  We list the a'-polygons (A1 -> T, corner p'_A=(1/4,0))
and gM'-polygons (T -> A1, corners p'_B=(1/4,1/2), q' in L_-2^0 cap L_2^w) between generators on the
same branch, with their omega-areas.  Levels (exact, Seifert data): branch +: A1 1/5, T 1/5; branch -: A1 3/10, T 7/40."""
from fractions import Fraction as F
from pmodel import Arc, Gen, L, V, polygons, canon
HALF, Q = F(1, 2), F(1, 4)
S = F(559, 125)
lev = {'+': {'A1': F(1, 5), 'T': F(1, 5)}, '-': {'A1': F(3, 10), 'T': F(7, 40)}}
for sgn in (1, -1):
    eps = sgn * F(1, 10 ** 6)
    for br, s in (('+', S), ('-', -S)):
        h = F(1, 20)
        arc = Arc(br, (Q - h, -s * h + eps), (Q + h, s * h + eps))
        gens = {}
        for cx, fam in (('A1', L(2, 1)), ('T', V)):
            gens[cx] = [Gen(cx, arc, t, u, lev[br][cx], '%s%s' % (cx, br)) for (t, u) in arc.meets(fam)]
        pA, pB = (Q, F(0)), (Q, HALF)
        qs = {(F(1, 8), Q), (F(3, 8), F(3, 4))}
        a = polygons(gens['A1'], gens['T'], [L(2, 1), V], [{pA}], 'int')
        gM = polygons(gens['T'], gens['A1'], [V, L(-2, 0), L(2, 1)], [{pB}, qs], 'int')
        print('db=%+de-6 branch %s (slope %s): a\' polygons: %s ; gM\' polygons: %s' % (sgn, br, float(s),
              [(p['src'].label, p['dst'].label, float(p['area'])) for p in a],
              [(p['src'].label, p['dst'].label, float(p['area']), [(str(c[0]), str(c[1])) for c in p['corners']]) for p in gM]))
