# exact SU(2)-level bookkeeping checks (T_inv trivialisation): kappa = B0 (A0 + eps)
from fractions import Fraction as F
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import dual
def kappa(sl,P,eps=1):
    p,q=sl; r,s=dual(p,q); a0,b0=P
    A0=p*a0+q*b0; B0=r*a0+s*b0
    assert (A0-F(1,2))%1==0, (sl,P)
    return B0*(A0+eps)
def m1(x): return x%1
half=F(1,2)
# (a) amphichiral knots, h:(mu,lambda)->(mu,-lambda); 2Theta = 1/2 at (1/2,1/2) [shift b+1 costs +a], 0 at (0,1/2)
bad=[]
for p in range(-30,31):
    for q in range(1,16):
        from math import gcd
        if gcd(p,q)!=1 or p%2: continue
        for P,twoTheta in (((half,half),half),((F(0),half),F(0))):
            tot=twoTheta+kappa((p,q),P)+kappa((-p,q),P)
            if m1(tot)!=0: bad.append(((p,q),P,tot))
print('(a) amphichiral knots, even p, |p|<=30, q<=15: identity 2Theta+kappa_r+kappa_-r = 0 mod 1 fails for',len(bad),'cases', bad[:5])
# (a') odd p: only sigma0? for odd p, sigma0 (1/2,1/2): A0=(p+q)/2 needs p+q odd; sigma1 (0,1/2): q odd
bad=[]
for p in range(-31,32):
    for q in range(1,16):
        from math import gcd
        if gcd(p,q)!=1: continue
        for P,twoTheta in (((half,half),half),((F(0),half),F(0))):
            if ((p*P[0]+q*P[1])-half)%1: continue
            tot=twoTheta+kappa((p,q),P)+kappa((-p,q),P)
            if m1(tot)!=0: bad.append(((p,q),P,tot))
print("(a') all slopes extendable: failures",len(bad),bad[:5])
# (c) knot +-2 cosmetic constants
for P in ((half,half),(F(0),half)):
    print('(c) P',P,'kappa(2,1)=',kappa((2,1),P),' kappa(-2,1)=',kappa((-2,1),P),' diff mod 1 =',m1(kappa((2,1),P)-kappa((-2,1),P)))
# Lemma 2 for all even N: cs(s1)-cs(s0) = Theta1-Theta0 + kappa(sigma1)-kappa(sigma0) with Theta1-Theta0 = 1/4 (twisting) ; must equal N/4
bad=[]
for N in range(-40,41,2):
    if N==0: continue
    d=F(1,4)+kappa((N,1),(F(0),half))-kappa((N,1),(half,half))
    if m1(d-F(N,4))!=0: bad.append((N,d))
print('(Lemma 2 consistency, N even in [-40,40]) failures:',bad)
# (b) o9 / N Ren-type spin-level identity: K1+K2+I1+I2+shift = 0, I1+I2 = -(J(X1)+J(X2))/2
J1=-0.007006478; J2=-0.492993522
K1=kappa((1,0),(half,F(0)))+kappa((-1,3),(F(0),half))
K2=kappa((-3,2),(half,half))+kappa((1,0),(half,half))
I=-(J1+J2)/2
print('(b) K1=',K1,'K2=',K2,'I1+I2=%.9f'%I,' total K1+K2+I+1/2 = %.9f'%(float(K1+K2)+I+0.5))
# (a'') redo amphichiral with the dual-correspondence correction k/4  (I(-r, l'') = -I(r,l) + k/4, l'' = h(l) + k*(-p,q))
from math import gcd
bad=[]; cnt=0
for p in range(-31,32):
    for q in range(1,16):
        if gcd(p,q)!=1: continue
        r_,s_=dual(p,q); hl=(r_,-s_); r2,s2=dual(-p,q)
        # l'' - h(l) = k*(-p,q)
        dx,dy=r2-hl[0],s2-hl[1]
        k = dx//(-p) if p!=0 else dy//q
        assert (dx,dy)==(k*(-p),k*q),(p,q,dx,dy,k)
        for P,twoTheta in (((half,half),half),((F(0),half),F(0))):
            if ((p*P[0]+q*P[1])-half)%1: continue
            cnt+=1
            tot=twoTheta+kappa((p,q),P)+kappa((-p,q),P)+F(k,4)
            if m1(tot)!=0: bad.append(((p,q),P,k,tot))
print("(a'') amphichiral, all extendable (p,q), |p|<=31, q<=15, with dual correction:",cnt,'cases, failures',len(bad),bad[:5])
