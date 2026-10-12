from glue import *
import sys
def circle_vals(S, r, m=256, nrad=60):
    out = S.path([r*j/nrad for j in range(1,nrad+1)])
    assert len(out)==nrad, 'radial failed'
    w = out[-1][4]
    us = [r*cmath.exp(2j*math.pi*k/m) for k in range(1,m+1)]
    out2 = S.path(us, w=w)
    if len(out2) < m: return None, None
    vals = [out2[-1][1]] + [o[1] for o in out2[:-1]]   # value at angle 0 (after full loop) then 1..m-1
    # monodromy check: compare value at angle 0 from start of loop vs after loop
    mono = abs(out2[-1][1] - out[-1][1])
    return np.array(vals), mono
def coeffs(S, r, m=256):
    vals, mono = circle_vals(S, r, m)
    if vals is None: return None, None
    c = np.fft.fft(vals)/m           # c_k r^k
    return np.array([c[k]/r**k for k in range(m//2)]), mono
if __name__=='__main__':
    name=sys.argv[1]; r=float(sys.argv[2])
    S=Sheet(name)
    c, mono = coeffs(S, r)
    print('monodromy |v_after - v_before| =', mono)
    print('tau (g\'(0)) =', c[1], ' snappy conj tau =', S.tau.conjugate())
    for k in range(1,40,2):
        print(k, abs(c[k]), abs(c[k])**(-1.0/k) if abs(c[k])>0 else None)
