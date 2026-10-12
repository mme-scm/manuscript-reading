import sys, json
from corr import drops, F
from math import gcd
PQ = int(sys.argv[1]) if len(sys.argv) > 1 else 120
knots = [(p, q) for p in range(2, 60) for q in range(p + 1, PQ + 1) if gcd(p, q) == 1 and p * q <= PQ]
names = ['m2 = l1(Y2)-l0(Y-2)', 'm1 = l0(Y2)-l1(Y-2)', 'u  = l0(Y2)-l0(Y-2)', 'w  = l1(Y2)-l1(Y-2)', 'D  = minl(Y2)-minl(Y-2)']
best = {}; rows = []; changed = []
def upd(key, val, name):
    if key not in best or val < best[key][0]: best[key] = (val, name)
for (p, q) in knots:
    for mir in (False, True):
        sig, r = drops(p, q, mir)
        name = f"T({p},{'-' if mir else ''}{q})"
        a, b = r[2], r[-2]
        l0a, l0b = a['lam0'], b['lam0']
        A = (a['lam1_lo'], a['lam1_hi']); B = (b['lam1_lo'], b['lam1_hi'])
        rng = {
          names[0]: (A[0] - l0b, A[1] - l0b),
          names[1]: (l0a - B[1], l0a - B[0]),
          names[2]: (l0a - l0b, l0a - l0b),
          names[3]: (A[0] - B[1], A[1] - B[0]),
          names[4]: (min(l0a, A[0]) - min(l0b, B[1]), min(l0a, A[1]) - min(l0b, B[0])),
        }
        old = {
          names[0]: a['lam1_old'] - l0b, names[1]: l0a - b['lam1_old'], names[2]: l0a - l0b,
          names[3]: a['lam1_old'] - b['lam1_old'],
          names[4]: min(l0a, a['lam1_old']) - min(l0b, b['lam1_old'])}
        for k in names:
            lo, hi = rng[k]
            upd(('worst', k), lo, name); upd(('best', k), hi, name); upd(('old', k), old[k], name)
        if (A[0], A[1]) != (a['lam1_old'],) * 2 or (B[0], B[1]) != (b['lam1_old'],) * 2:
            changed.append(name)
        rows.append(dict(knot=name, sigma=sig, **{k: [str(rng[k][0]), str(rng[k][1])] for k in names},
                         lam1_Y2=[str(A[0]), str(A[1])], lam1_Ym2=[str(B[0]), str(B[1])],
                         lam1_old=[str(a['lam1_old']), str(b['lam1_old'])], lam0=[str(l0a), str(l0b)]))
print(f"{len(knots)} torus knots T(p,q), pq <= {PQ}, both chiralities: {2*len(knots)} cases; lambda_1 changed by the correction in {len(changed)}")
for k in names:
    o, w, b = best[('old', k)], best[('worst', k)], best[('best', k)]
    print(f"{k:26s} uncorrected min {float(o[0]):+.5f} ({o[1]:9s}) | corrected, worst cancellation {str(w[0]):>14s} = {float(w[0]):+.5f} ({w[1]:9s}) | best {str(b[0]):>12s} = {float(b[0]):+.5f} ({b[1]})")
json.dump(rows, open(f'scan_{PQ}.json', 'w'), indent=0)
