# Purely cosmetic Ren-type pair M(s) ~ M(A^2 s), M = o10_150704(inf,inf,As,inf); spin-level & Riemannian tests
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
from fractions import Fraction as Fr
import numpy as np
N=snappy.Manifold('o10_150704'); N.chern_simons()
A=np.array([[-1,-1],[1,0]]); AmT=np.array([[0,-1],[1,-1]])   # A^{-T}
def kap(sl,P,eps=1):
    p,q=sl; r,s=dual(p,q); a0,b0=P
    A0=p*a0+q*b0; B0=r*a0+s*b0
    assert (A0-Fr(1,2))%1==0,(sl,P,A0)
    return B0*(A0+eps)
def tf(v): return (Fr(int(round(2*v[0])),2),Fr(int(round(2*v[1])),2))
n=int(sys.argv[1]) if len(sys.argv)>1 else 200
for s in [(3,4),(2,1),(3,5),(1,3)]:
    As=tuple(int(x) for x in A@np.array(s)); A2s=tuple(int(x) for x in A@A@np.array(s))
    # cone paths on cusp 0 of M=N(inf,inf,As,inf)
    dX=path(N,0,s,n=n,fills=[None,None,As,None]); dY=path(N,0,A2s,n=n,fills=[None,None,As,None])
    # also N->M path on cusp 2 (same PSL path for both; cancels)
    for P0 in [(Fr(1,2),Fr(0)),(Fr(1,2),Fr(1,2)),(Fr(0),Fr(1,2))]:
        P2=P0
        if (s[0]*P0[0]+s[1]*P0[1]-Fr(1,2))%1 or (As[0]*P2[0]+As[1]*P2[1]-Fr(1,2))%1: continue
        P0pp=tf(AmT@np.array([float(P2[0]),float(P2[1])])); P2pp=tf(AmT@np.array([float(P0[0]),float(P0[1])]))
        K_X = kap(As,P2)+kap(s,P0)
        K_Y = kap(As,P2pp)+kap(A2s,P0pp)
        dK = K_Y-K_X
        dI = -(dY['J']-dX['J'])/2          # SU(2) twist difference I(A^2 s) - I(s)
        print('s',s,'As',As,'A2s',A2s,'P0',P0,'P0pp',P0pp,'P2pp',P2pp,'| J(s)=%.9f J(A2s)=%.9f  Delta_J=J(s)-J(A2s)=%.9f'%(dX['J'],dY['J'],dX['J']-dY['J']),
              '| dK=',dK,' spin-level dK+dI mod 1 = %+.9f'%mod(float(dK)+dI,1),' Riemannian 2(dK+dI) mod 1 = %+.9f'%mod(2*(float(dK)+dI),1),
              'bad',(dX['bad'],dY['bad']),'maxtor %.2f %.2f'%(dX['maxtor'],dY['maxtor']))
