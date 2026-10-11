"""
Exact checks of the abstract filtered models used in critic.md.

A model is a 3-periodic triangle of filtered complexes over F_2 (DLME's
triangle-detection data with h = 0, q = id):
    C1 --f1--> C0 --f0--> Cm1 --fm1--> C1
    g1: C1 -> Cm1,  g0: C0 -> C1,  gm1: Cm1 -> C0
with
    d f = f d,   d g + g d = f f,   f g + g f = id   (all mod 2).
Generators carry (degree, c-level), c = CS - deg/8.  The differential must
lower CS strictly (positive energy), i.e. raise c by < 1/8.
Every map must be homogeneous, and its c-shift on every nonzero matrix entry
must respect the level bound of the corresponding instanton map:
    A = f1, B = f0 : c-shift < 0           (energy > 0, no flat contribution)
    Gamma = fm1    : c-shift <= 3/16
    G+ = g1        : c-shift < -1/8        (energy > 0 on simply connected W')
    GM = g0, G- = gm1 : c-shift <= 1/16
ell = least c-level of a nonzero homology class (min over representatives
of the max level), ell+ = largest such birth level.
"""
from fractions import Fraction as F
from itertools import product

def mat_apply(m, vec):
    out = set()
    for s in vec:
        for t in m.get(s, ()):
            out ^= {t}
    return frozenset(out)

def compose(m2, m1, gens):
    return {s: mat_apply(m2, mat_apply(m1, {s})) for s in gens}

def add(*ms, gens):
    out = {}
    for s in gens:
        v = frozenset()
        for m in ms:
            v = v ^ mat_apply(m, {s})
        out[s] = v
    return out

def is_zero(m):
    return all(len(v) == 0 for v in m.values())

def lev(vec, G):
    return max(G[s][1] for s in vec) if vec else None

def span(gens):
    gens = list(gens)
    for bits in product([0, 1], repeat=len(gens)):
        yield frozenset(g for g, b in zip(gens, bits) if b)

def homology_levels(C, d):
    """Return sorted list of (level, degree) of births of infinite bars,
    computed by brute force: classes = cycles mod boundaries."""
    gens = list(C)
    cycles = [v for v in span(gens) if v and len(mat_apply(d, v)) == 0]
    bnds = {mat_apply(d, v) for v in span(gens)}
    # group cycles by homology class (homogeneous only)
    classes = {}
    for z in cycles:
        degs = {C[s][0] for s in z}
        if len(degs) != 1:
            continue
        if z in bnds:
            continue
        key = None
        for k in classes:
            if (z ^ k) in bnds and {C[s][0] for s in k} == degs:
                key = k
                break
        if key is None:
            classes[z] = [z]
        else:
            classes[key].append(z)
    out = []
    for k, reps in classes.items():
        out.append((min(lev(r, C) for r in reps), next(iter({C[s][0] for s in k}))))
    return sorted(out)

def check_model(name, cx, maps, bounds, strict):
    C1, C0, Cm1 = cx['C1'], cx['C0'], cx['Cm1']
    d1, d0, dm1 = cx['d1'], cx['d0'], cx['dm1']
    f1, f0, fm1 = maps['f1'], maps['f0'], maps['fm1']
    g1, g0, gm1 = maps['g1'], maps['g0'], maps['gm1']
    ok = True
    def need(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
            print('   FAIL:', msg)
    # differentials
    for C, d, nm in [(C1, d1, 'C1'), (C0, d0, 'C0'), (Cm1, dm1, 'Cm1')]:
        need(is_zero(compose(d, d, C)), f'd^2 on {nm}')
        for s, ts in d.items():
            for t in ts:
                need(C[t][0] == C[s][0] - 1, f'degree of d {s}->{t}')
                cs_s = C[s][1] + F(C[s][0], 8)
                cs_t = C[t][1] + F(C[t][0], 8)
                need(cs_t < cs_s, f'energy of d {s}->{t} not positive')
    # chain maps
    need(compose(d0, f1, C1) == compose(f1, d1, C1), 'f1 chain')
    need(compose(dm1, f0, C0) == compose(f0, d0, C0), 'f0 chain')
    need(compose(d1, fm1, Cm1) == compose(fm1, dm1, Cm1), 'fm1 chain')
    # homotopies: d g + g d = f f
    need(add(compose(dm1, g1, C1), compose(g1, d1, C1), gens=C1) == compose(f0, f1, C1), 'g1 relation')
    need(add(compose(d1, g0, C0), compose(g0, d0, C0), gens=C0) == compose(fm1, f0, C0), 'g0 relation')
    need(add(compose(d0, gm1, Cm1), compose(gm1, dm1, Cm1), gens=Cm1) == compose(f1, fm1, Cm1), 'gm1 relation')
    # f g + g f = id (q = id, h = 0)
    idC1 = {s: frozenset({s}) for s in C1}
    idC0 = {s: frozenset({s}) for s in C0}
    idCm1 = {s: frozenset({s}) for s in Cm1}
    need(add(compose(fm1, g1, C1), compose(g0, f1, C1), gens=C1) == idC1, 'q1 = id')
    need(add(compose(f1, g0, C0), compose(gm1, f0, C0), gens=C0) == idC0, 'q0 = id')
    need(add(compose(f0, gm1, Cm1), compose(g1, fm1, Cm1), gens=Cm1) == idCm1, 'qm1 = id')
    # levels and homogeneity
    src = {'f1': C1, 'f0': C0, 'fm1': Cm1, 'g1': C1, 'g0': C0, 'gm1': Cm1}
    tgt = {'f1': C0, 'f0': Cm1, 'fm1': C1, 'g1': Cm1, 'g0': C1, 'gm1': C0}
    for k in maps:
        degs = set()
        for s, ts in maps[k].items():
            for t in ts:
                degs.add(tgt[k][t][0] - src[k][s][0])
                shift = tgt[k][t][1] - src[k][s][1]
                if k in strict:
                    need(shift < bounds[k], f'{k} {s}->{t} shift {shift} not < {bounds[k]}')
                else:
                    need(shift <= bounds[k], f'{k} {s}->{t} shift {shift} > {bounds[k]}')
        need(len(degs) <= 1, f'{k} not homogeneous: {degs}')
    print(f'{name}: relations and level bounds', 'OK' if ok else 'FAILED')
    for nm, C, d in [('C1', C1, d1), ('C0', C0, d0), ('Cm1', Cm1, dm1)]:
        hl = homology_levels(C, d)
        if hl:
            print(f'   {nm}: infinite bars born at c-levels', [str(l) for l, _ in hl],
                  ' ell =', hl[0][0], ' ell+ =', hl[-1][0])
        else:
            print(f'   {nm}: acyclic')
    return ok

BOUNDS = {'f1': F(0), 'f0': F(0), 'fm1': F(3, 16), 'g1': F(-1, 8), 'g0': F(1, 16), 'gm1': F(1, 16)}
STRICT = {'f1', 'f0', 'g1'}

# ---------------------------------------------------------------------------
# Model 1: cosmetic-type configuration for the two bundle-exchanging triangles.
# Y has P0 = <x0> at level u, P1 = <x1> at level v; traceless = <z, zp>.
mu, u, v, mup = F(0), F(3, 100), F(3, 100), F(6, 100)
P0 = {'x0': (0, u)}
P1 = {'x1': (0, v)}
TL = {'z': (1, mu), 'zp': (-1, mup)}
empty = lambda C: {s: frozenset() for s in C}
# Triangle (I): P0(Y_2) -> TL -> P1(Y_-2) -> P0(Y_2)
cxI = {'C1': P0, 'C0': TL, 'Cm1': P1, 'd1': empty(P0), 'd0': empty(TL), 'dm1': empty(P1)}
mapsI = {'f1': {'x0': frozenset({'z'})},
         'f0': {'z': frozenset(), 'zp': frozenset({'x1'})},
         'fm1': {'x1': frozenset()},
         'g1': {'x0': frozenset()},
         'g0': {'z': frozenset({'x0'}), 'zp': frozenset()},
         'gm1': {'x1': frozenset({'zp'})}}
check_model('Model 1, triangle (I)', cxI, mapsI, BOUNDS, STRICT)
# Triangle (II): P1(Y_2) -> TL -> P0(Y_-2) -> P1(Y_2)
cxII = {'C1': P1, 'C0': TL, 'Cm1': P0, 'd1': empty(P1), 'd0': empty(TL), 'dm1': empty(P0)}
mapsII = {'f1': {'x1': frozenset({'z'})},
          'f0': {'z': frozenset(), 'zp': frozenset({'x0'})},
          'fm1': {'x0': frozenset()},
          'g1': {'x1': frozenset()},
          'g0': {'z': frozenset({'x1'}), 'zp': frozenset()},
          'gm1': {'x0': frozenset({'zp'})}}
check_model('Model 1, triangle (II)', cxII, mapsII, BOUNDS, STRICT)
print('   Model 1: Y_2 and Y_-2 carry the same filtered complexes in each bundle;')
print('   min(l0,l1)(Y_2) - min(l0,l1)(Y_-2) =', min(u, v) - min(u, v),
      '; m1 + m2 =', (u - v) + (v - u))
print('   window: mu < min(u,v) <= max(u,v) <= mu + 1/16 :', mu < min(u, v) <= max(u, v) <= mu + F(1, 16))
print('   dual window: mu+ - 1/16 <= min(u,v) <= max(u,v) < mu+ :', mup - F(1, 16) <= min(u, v) <= max(u, v) < mup)

# ---------------------------------------------------------------------------
# Model 2: absorption by a FINITE bar of the middle term (middle term acyclic),
# with the bottom of the Y_-2 side above the bottom of the Y_2 side.
O_plus = {'x': (0, F(0))}
M = {'z': (1, F(-1, 100)), 'y': (2, F(5, 100))}
O_minus = {'w': (3, F(2, 100))}
cx2 = {'C1': O_plus, 'C0': M, 'Cm1': O_minus,
       'd1': empty(O_plus), 'd0': {'y': frozenset({'z'}), 'z': frozenset()}, 'dm1': empty(O_minus)}
maps2 = {'f1': {'x': frozenset({'z'})},
         'f0': {'y': frozenset({'w'}), 'z': frozenset()},
         'fm1': {'w': frozenset({'x'})},
         'g1': {'x': frozenset()},
         'g0': {'z': frozenset({'x'}), 'y': frozenset()},
         'gm1': {'w': frozenset({'y'})}}
check_model('Model 2 (finite-bar absorption)', cx2, maps2, BOUNDS, STRICT)
print('   drop ell(O+) - ell(O-) =', F(0) - F(2, 100), '(negative), although H(M) = 0')
cs = lambda C, s: C[s][1] + F(C[s][0], 8)
print('   CS-length of the bar of M:', cs(M, 'y') - cs(M, 'z'))

# ---------------------------------------------------------------------------
# Model 3: absorption by an infinite bar, negative drop, non-cosmetic.
O_plus3 = {'x': (0, F(0)), 'xp': (0, F(17, 100))}
M3 = {'z': (1, F(-3, 100))}
O_minus3 = {'w': (3, F(2, 100))}
cx3 = {'C1': O_plus3, 'C0': M3, 'Cm1': O_minus3,
       'd1': empty(O_plus3), 'd0': empty(M3), 'dm1': empty(O_minus3)}
maps3 = {'f1': {'x': frozenset({'z'}), 'xp': frozenset()},
         'f0': {'z': frozenset()},
         'fm1': {'w': frozenset({'xp'})},
         'g1': {'x': frozenset(), 'xp': frozenset({'w'})},
         'g0': {'z': frozenset({'x'})},
         'gm1': {'w': frozenset()}}
check_model('Model 3 (infinite-bar absorption)', cx3, maps3, BOUNDS, STRICT)
print('   drop ell(O+) - ell(O-) =', F(0) - F(2, 100))
