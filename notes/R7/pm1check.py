# RHT: Gamma = {b = 1/2 - 6a, a in [1/12,5/12]}, Phi = -6(a-1/4)^2 (+const), iota = 0 (slope -6).
# level c(Y_N,x) = Phi + N(a-1/4)^2 + 3/16 sgn N - N/16 - iota/8
from fractions import Fraction as F
def gens(N):
    out=[]
    # N a + b = integer with b = 1/2 - 6a  ->  (N-6)a = k - 1/2
    for k in range(-20,20):
        a=(F(k)-F(1,2))/(N-6)
        if F(1,12)<a<F(5,12): out.append(a)
    return out
def c(N,a):
    sg=1 if N>0 else -1
    return -6*(a-F(1,4))**2 + N*(a-F(1,4))**2 + F(3,16)*sg - F(N,16)
for N in (1,-1,2,-2):
    print(N,[ (str(a), str(c(N,a))) for a in gens(N)])
l1=min(c(1,a) for a in gens(1)); lm1=min(c(-1,a) for a in gens(-1))
print('ell(Y1)-ell(Y-1) =', l1-lm1, float(l1-lm1), ' DLME value 59/120-23/84 =', F(59,120)-F(23,84))
