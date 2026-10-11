"""Validation of bk.py.
 1. DLME Example: Sigma(2,3,5): (CS,gr) = (1/120,1),(49/120,5), c = -7/60,-13/60.
 2. Sigma(2,3,7) = S^3_{-1}(RHT): c = 23/84, 29/84, (CS,gr) = (25/168,7),(121/168,3).
 3. Torus knots as fibres: S^3 = +-Sigma(p,q,1), K_3 = regular fibre = T(p,q) (resp. mirror);
    ell(Y_{+-1/n}), n<=5, against the 140-entry table of ../drops.md (independently re-checked
    in ../drops-check.md).
 4. Full generator multisets {c} of every pairwise-coprime Sigma(a1,a2,a3), a<=MAXFULL, against
    ../check-code/fs.py (exact FS + APS formulas, independent code), and grading parity.
 5. #R* from the separable count == Brieskorn signature count (milnor_count), all scanned A.
 6. Casson surgery formula lambda(Y_{1/m}(K_i)) = lambda(Sigma) + m a2(T(a_j,a_k)) for both
    orientations of Sigma, i = 1,2,3, m = +-1..+-4  (fixes the sign of the slope).
 7. Minimisers: c == -SigmaFS(e)/8 and 8(CS-c) integral (bk.fs_check), for many manifolds.
"""
import sys, re, itertools, time
from fractions import Fraction as F
from math import gcd
HERE = '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r6'
sys.path.insert(0, HERE + '/brieskorn-code')
import bk

t0 = time.time()
# 1, 2
for A, exp in [((2, 3, 5), {F(-7, 60): (F(1, 120), 1), F(-13, 60): (F(49, 120), 5)}),
               ((2, 3, 7), {F(23, 84): (F(25, 168), 7), F(29, 84): (F(121, 168), 3)})]:
    d = bk.analyse(A, want_all=True)
    got = {}
    for eps, l, c in d['all']:
        e, CS, gr = bk.fs_check(A, l, c)
        got[c] = (CS, gr)
    assert got == exp, (A, got)
    print("1/2. Sigma%s: (c: CS, gr) =" % (A,), {str(k): (str(v[0]), v[1]) for k, v in got.items()}, "OK")
d = bk.manifold((2, 3, 5), 1)
print("     ell(Sigma(2,3,5)) =", d['ell'], " ell(Sigma(2,3,7)) =", bk.manifold((2, 3, 7), 1)['ell'])

# 3: torus knots = regular fibre of +-Sigma(p,q,1)
txt = open(HERE + "/drops.md").read()
sec = txt.split("## 2.")[1].split("**Order")[0]
cols = [(+1, n) for n in range(1, 6)] + [(-1, n) for n in range(1, 6)]
ncmp = nbad = 0
for line in sec.splitlines():
    mm = re.match(r"\| (m?)T\((\d),(\d+)\) \|(.*)\|\s*$", line)
    if not mm:
        continue
    mirror, p, q = mm.group(1) == 'm', int(mm.group(2)), int(mm.group(3))
    s = -1 if mirror else 1
    vals = [v.strip().replace("−", "-") for v in mm.group(4).split("|")]
    for (sg, n), v in zip(cols, vals):
        Ap, sp = bk.surgered((p, q, 1), s, 2, sg * n)
        ell = bk.manifold(Ap, sp)['ell']
        ncmp += 1
        if ell != F(v):
            nbad += 1
            print("   MISMATCH", mirror, p, q, sg, n, ell, v)
print("3. torus knots (regular fibre of +-Sigma(p,q,1)) vs drops.md table: %d entries, %d mismatches" % (ncmp, nbad))
assert nbad == 0 and ncmp == 140

# 4: full multisets vs check-code/fs.py
sys.path.insert(0, HERE + '/check-code')
import fs
MAXFULL = 420
trip = [(a1, a2, a3) for a1 in range(2, 20) for a2 in range(a1 + 1, 60) for a3 in range(a2 + 1, 220)
        if a1 * a2 * a3 <= MAXFULL and gcd(a1, a2) == gcd(a1, a3) == gcd(a2, a3) == 1]
nrep = 0
for A in trip:
    mine = sorted(c for eps, l, c in bk.analyse(A, want_all=True)['all'])
    ref = fs.flats(A)
    assert mine == sorted(x['c'] for x in ref), A
    assert len({x['gr'] % 2 for x in ref}) == 1, A
    nrep += len(mine)
    # also a permuted order
    Pm = (A[2], A[0], A[1])
    assert sorted(c for eps, l, c in bk.analyse(Pm, want_all=True)['all']) == mine
print("4. full c-multisets vs check-code/fs.py: %d Brieskorn spheres (a<=%d), %d generators, 0 mismatches;"
      " one grading parity in each" % (len(trip), MAXFULL, nrep))

# 4b: a few against drops-code (mpmath cot sums with Seifert invariants), different code again
sys.path.insert(0, HERE + '/drops-code')
import brieskorn as bz
for A in [(2, 5, 7), (3, 4, 5), (2, 5, 13), (3, 5, 7), (2, 7, 9), (3, 4, 7)]:
    for s in (1, -1):
        ref = sorted(g['c'] for g in bz.generators(A, s))
        d = bk.analyse(A, want_all=True)
        mine = sorted((c if s == 1 else F(3, 8) - c) for eps, l, c in d['all'])
        assert ref == mine, (A, s)
print("4b. full c-multisets vs drops-code/brieskorn.py (mpmath) for 6 non-torus spheres x 2 orientations: OK")
print("    time %.1fs" % (time.time() - t0))
