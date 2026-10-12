# consistency of the SU(2)-level twist rule with naturality under phi on N=o10_150704
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from spin import *
import snappy, sympy, itertools
from fractions import Fraction as Fr
N=snappy.Manifold('o10_150704')
G=N.fundamental_group(); gens=G.generators(); rels=G.relators(); pc=G.peripheral_curves()
R=sympy.Matrix([[word_vec(r,gens)[g] for g in gens] for r in rels])
ker=R.nullspace()
# make integral
basis=[]
for v in ker:
    den=sympy.ilcm(*[x.q for x in v]); basis.append([int(x*den) for x in v])
print('rank Hom(H1,Z)=',len(basis))
def ev(vec,w):
    v=word_vec(w,gens); return sum(v[g]*vec[i] for i,g in enumerate(gens))
bdry=[[ (ev(b,pc[c][0]),ev(b,pc[c][1])) for c in range(4)] for b in basis]
for b in bdry: print('integral class boundary values (mu_j,l_j):',b)
# lattice rules: cs(a+1,b)=cs(a,b)-b ; cs(a,b+1)=cs(a,b)+a  (per cusp). shift to move (a,b) -> (a+m, b+n): path a-steps first
def shift(a,b,m,n):
    tot=Fr(0)
    step=1 if m>0 else -1
    for _ in range(abs(m)):
        if step==1: tot+=-b; a+=1
        else: a-=1; tot+=b
    step=1 if n>0 else -1
    for _ in range(abs(n)):
        if step==1: tot+=a; b+=1
        else: b-=1; tot-=a
    return tot
# P and P'' from ren_pc3 (s=(3,4)): cusp types
P  =[(Fr(1,2),Fr(0)),(Fr(0),Fr(0)),(Fr(1,2),Fr(0)),(Fr(0),Fr(0))]
Ppp=[(Fr(0),Fr(1,2)),(Fr(0),Fr(0)),(Fr(0),Fr(1,2)),(Fr(0),Fr(0))]
target=[ (int((2*(Ppp[j][0]-P[j][0]))%2), int((2*(Ppp[j][1]-P[j][1]))%2)) for j in range(4)]
print('chi restriction needed', target)
# find integral class chihat with chihat mod 2 having those boundary values
best=None
for coeffs in itertools.product(range(-1,2),repeat=len(basis)):
    bv=[ (sum(c*bdry[i][j][0] for i,c in enumerate(coeffs)), sum(c*bdry[i][j][1] for i,c in enumerate(coeffs))) for j in range(4)]
    if all((bv[j][0]%2,bv[j][1]%2)==target[j] for j in range(4)):
        best=(coeffs,bv); break
print('chihat',best)
coeffs,bv=best
# twisted base: Theta(rho chi at P+chihat/2) = Theta(rho at P) + sum_j(-c1 b0 + c2 a0) + Theta(chi at chihat/2)=0 (radial)
d=Fr(0); pts=[]
for j in range(4):
    c1,c2=Fr(bv[j][0],2),Fr(bv[j][1],2)
    d+= -c1*P[j][1]+c2*P[j][0]
    pts.append((P[j][0]+c1,P[j][1]+c2))
# lattice move to P''
for j in range(4):
    a,b=pts[j]; m=Ppp[j][0]-a; n=Ppp[j][1]-b
    assert m.denominator==1 and n.denominator==1
    d+=shift(a,b,int(m),int(n))
print('delta = Theta(sigma'',P'') - Theta(sigma,P) by rules =',d,' mod 1 =',d%1,'  (naturality requires 0)')
