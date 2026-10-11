"""Plain-text table of every family in the given scan files.
Usage: python3 dump.py OUT.txt FILE.json [...]"""
import sys, json
from fractions import Fraction as F

E = lambda y: None if y['ell'] is None else F(y['ell'])
rows = []
for fn in sys.argv[2:]:
    for f in json.load(open(fn)):
        A, s, i = f['A'], f['s'], f['i']
        P = A[0] * A[1] * A[2] // A[i]
        kind = 'L+' if s == 1 else ('L-' if A[i] < P else 'R-')
        ng = {int(k): E(v) for k, v in f['neg'].items()}
        ps = {int(k): E(v) for k, v in f['pos'].items()}
        ok = all(ng[n] is not None for n in (1, 2, 3))
        tl = "".join('T' if any(m['traceless'] for m in f['neg'][str(n)]['min']) else '.' for n in (1, 2, 3))
        ori = "".join('+' if f['neg'][str(n)]['s'] == 1 else '-' for n in (1, 2, 3))
        rows.append("%s%-14s K=%-5d P=%-5d %s  ell(base)=%-14s | Y-1..-1/4: %s | Y+1..+1/3: %s | D1=%s D2=%s T1=%s | orient %s TL %s" % (
            '+' if s == 1 else '-', "S(%d,%d,%d)" % tuple(A), A[i], P, kind, E(f['base']),
            " ".join(str(ng[n]) for n in (1, 2, 3, 4)), " ".join(str(ps[n]) for n in (1, 2, 3)),
            "%.5f" % float(ng[1] - ng[2]) if ok else '-', "%.5f" % float(ng[2] - ng[3]) if ok else '-',
            ("%.5f" % float(ng[1] - ng[3]) if ng[1] - ng[3] != F(1, 8) else "1/8") if ok else '-', ori, tl))
with open(sys.argv[1], 'w') as fh:
    fh.write("# every family: base s*Sigma(A), fibre K, P = a/a_K, kind (L+: s=+1; L-: s=-1, a_K<P; R-: s=-1, a_K>P)\n")
    fh.write("# D1 = ell(Y-1)-ell(Y-1/2), D2 = ell(Y-1/2)-ell(Y-1/3), T1 = ell(Y-1)-ell(Y-1/3); orient = orientations of Y-1,Y-1/2,Y-1/3;\n")
    fh.write("# TL = minimiser traceless at the surgered fibre in Y-1,Y-1/2,Y-1/3.  'None' = S^3 (no irreducibles, ell = +infinity).\n")
    fh.write("\n".join(rows) + "\n")
print(len(rows), "rows ->", sys.argv[1])
