"""Riley representations of 2-bridge knot groups, longitude, and polynomial-in-u machinery (numerical)."""
import numpy as np
from numpy.polynomial import polynomial as P

def eps(p,q): return [(-1)**((i*q)//p) for i in range(1,p)]

def word(p,q):
    e=eps(p,q); w=[]
    for i,ei in enumerate(e):
        w.append((1 if i%2==0 else 2, ei))
    return w

# matrices with entries = polynomials in u (coefficient arrays, low->high), at fixed M
def mat_const(a,b,c,d): return [[np.array([a],complex),np.array([b],complex)],[np.array([c],complex),np.array([d],complex)]]
def gen(M,g,e):
    if g==1:
        return mat_const(M,1,0,1/M) if e==1 else mat_const(1/M,-1,0,M)
    else:
        if e==1: return [[np.array([M],complex),np.array([0],complex)],[np.array([0,1],complex),np.array([1/M],complex)]]
        else:    return [[np.array([1/M],complex),np.array([0],complex)],[np.array([0,-1],complex),np.array([M],complex)]]
def mmul(A,B):
    return [[P.polyadd(P.polymul(A[i][0],B[0][j]),P.polymul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def wpoly(M,w):
    W=mat_const(1,0,0,1)
    for (g,e) in w: W=mmul(W,gen(M,g,e))
    return W
def f1poly(M,w):
    W=wpoly(M,w)
    return P.polysub(W[0][0], (M-1/M)*W[0][1])

def num_gen(M,u,g,e):
    if g==1: A=np.array([[M,1],[0,1/M]],complex)
    else: A=np.array([[M,0],[u,1/M]],complex)
    return A if e==1 else np.linalg.inv(A)
def num_word(M,u,wd):
    A=np.eye(2,dtype=complex)
    for (g,e) in wd: A=A@num_gen(M,u,g,e)
    return A

def roots_u(M,w):
    c=np.trim_zeros(f1poly(M,w),'b')
    return np.roots(c[::-1])

def longitude_word(p,q):
    w=word(p,q); wr=[(g,e) for (g,e) in reversed(w)]
    s=sum(e for (_,e) in w)
    return wr+w+[(1,-1)]*(2*s) if s>0 else wr+w+[(1,1)]*(-2*s)

def check(p,q,M=0.7+0.4j):
    w=word(p,q); lw=longitude_word(p,q)
    out=[]
    for u in roots_u(M,w):
        X1=num_gen(M,u,1,1); X2=num_gen(M,u,2,1); W=num_word(M,u,w)
        rel=np.abs(W@X1-X2@W).max()
        Lm=num_word(M,u,lw); comm=np.abs(Lm@X1-X1@Lm).max()
        out.append((u,rel,comm,Lm[0,0],Lm[1,0]))
    return out
if __name__=='__main__':
    for (p,q) in [(3,1),(5,3),(7,3),(11,3),(17,5)]:
        print(p,q,eps(p,q))
        for r in check(p,q): print('   u=%s rel=%.1e comm=%.1e L=%s L21=%.1e'%(np.round(r[0],5),r[1],r[2],np.round(r[3],5),abs(r[4])))
