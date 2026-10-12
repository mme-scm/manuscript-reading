# what each hypothetical purely cosmetic pair on a knot would require of the twist difference (spin level)
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *
from fractions import Fraction as Fr
half=Fr(1,2)
def kap(sl,P,eps=1):
    p,q=sl; r,s=dual(p,q); a0,b0=P
    A0=p*a0+q*b0; B0=r*a0+s*b0; assert (A0-half)%1==0
    return B0*(A0+eps)
def ext(sl,P): return (sl[0]*P[0]+sl[1]*P[1]-half)%1==0
S0=(half,half); S1=(Fr(0),half)
print('pair      spin pairing            Delta kappa (SU2)   => required DeltaJ = J(r)-J(r\') mod 2 (SnapPy units)')
for q in range(1,8):
    for sl1,sl2 in (((1,q),(-1,q)),):
        Ps=[P for P in (S0,S1) if ext(sl1,P)]
        P=Ps[0]
        dk=kap(sl1,P)-kap(sl2,P)
        print('+-1/%d   unique spin (%s)       %s      ΔJ ≡ %s mod 2'%(q,'s0' if P==S0 else 's1',dk%1,(2*dk)%2))
for N in (2,-2):
    pass
dk0=kap((2,1),S0)-kap((-2,1),S0); dk1=kap((2,1),S1)-kap((-2,1),S1)
print('+-2  same-type pairing s0<->s0: Δκ=%s ; with Lemma1 swap (s1(Y_-2)->s0(Y_2)) cs diff needs +1/2  => ΔJ ≡ 1 mod 2'%(dk0%1))
# numerics for 5_2 and K11n42
for name in ['5_2','K11n42']:
    M=snappy.Manifold(name); M.chern_simons()
    for q in (1,2,3,4,5):
        a=path(M,0,(1,q),n=150); b=path(M,0,(-1,q),n=150)
        P=S0 if ext((1,q),S0) else S1
        dk=kap((1,q),P)-kap((-1,q),P)
        print(name,'+-1/%d: ΔJ=%.6f  required ΔJ mod 2 = %s  -> distance to allowed set = %.4f'%(q,a['J']-b['J'],(2*dk)%2, abs(mod(a['J']-b['J']-float((2*dk)%2),2))))
