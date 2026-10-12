from glue import *
import sys
name = sys.argv[1] if len(sys.argv)>1 else 'K11n42'
Rmax = float(sys.argv[2]) if len(sys.argv)>2 else 2.0
S = Sheet(name)
nth, nr = 72, 200
best = []
for k in range(nth):
    th = 2*math.pi*k/nth
    us = [Rmax*j/nr*cmath.exp(1j*th) for j in range(1,nr+1)]
    out = S.path(us)
    # first local minimum of sv along the ray / or failure
    svs = [o[3] for o in out]; ress=[o[2] for o in out]
    jmin = int(np.argmin(svs)); jfail = next((j for j,r in enumerate(ress) if r>1e-8), None)
    best.append((th, abs(us[jmin]), svs[jmin], None if jfail is None else abs(us[jfail])))
best.sort(key=lambda t: t[2])
for b in best[:10]: print('theta=%.3f  |u| at min sv=%.3f  min sv=%.2e  fail at %s'%b)
