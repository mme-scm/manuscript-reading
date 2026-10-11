import numpy as np
from scipy.optimize import brentq
exec(open('fig8.py').read().split('# scan grid')[0])
def f1(th,ph): return words(th,ph)[0][0,0].imag
def f2(th,ph): return words(th,ph)[0][0,1].real
c=(np.pi/2, (1.256637+2.513274)/2)
def pt(psi):
    d=np.array([np.cos(psi),np.sin(psi)])
    g=lambda r: f1(c[0]+r*d[0], c[1]+r*d[1]) if abs(np.cos(psi))<0.9 else f2(c[0]+r*d[0], c[1]+r*d[1])
    rs=np.linspace(1e-3,1.2,600); v=[g(r) for r in rs]
    for k in range(len(rs)-1):
        if v[k]*v[k+1]<0: 
            r=brentq(g,rs[k],rs[k+1],xtol=1e-14); return c[0]+r*d[0], c[1]+r*d[1]
    raise Exception(psi)
N=4000
P=[pt(2*np.pi*k/N) for k in range(N)]
A=[];B=[];res=[];comm=[]
for th,ph in P:
    R,L,X=words(th,ph)
    res.append(np.linalg.norm(R)); comm.append(np.linalg.norm(L@X-X@L))
    A.append(th/(2*np.pi)); B.append(np.angle(L[0,0])/(2*np.pi))
print('max residual',max(res),'max comm',max(comm), 'offdiag L', max(abs(words(*p)[1][0,1]) for p in P[::50]))
A=np.array(A); B=np.array(B)
Bl=np.unwrap(2*np.pi*B)/(2*np.pi)
Al=np.unwrap(2*np.pi*A)/(2*np.pi)
print('a range',A.min(),A.max(),' b range', B.min(), B.max())
n=Bl[-1]-Bl[0] + (Bl[0]-Bl[-1])  # placeholder
# close the loop: append first point
Al2=np.append(Al,Al[0]+np.round(Al[-1]-Al[0])*0); 
# compute winding of b: b at end vs start after going around
B_end=Bl[-1]+ (np.angle(np.exp(2j*np.pi*(B[0]-B[-1])))/(2*np.pi))
print('winding n =', B_end-Bl[0])
# integral of 2 b da over closed loop with continuous lift, starting at different base points
def integral(start):
    idx=np.r_[start:N, 0:start+1]
    a=A[idx]; b=np.unwrap(2*np.pi*B[idx])/(2*np.pi)
    # trapezoid
    I=np.sum((b[1:]+b[:-1])*(a[1:]-a[:-1]))
    return I, a[0], b[-1]-b[0]
for s in [0,500,1000,1500,2000,2500,3000,3500]:
    I,a0,nn=integral(s)
    print(s, 'a0=%.6f'%a0, 'n=%.4f'%nn, 'I=%.6f'%I, 'I-2n a0 =%.6f'%(I-2*round(nn)*a0), ' I mod 1=%.6f'%(I%1))
print('---- other forms')
for s in [0,700,1300,2200,3100]:
    idx=np.r_[s:N, 0:s+1]
    a=A[idx]; b=np.unwrap(2*np.pi*B[idx])/(2*np.pi)
    J=np.sum((a[1:]+a[:-1])*(b[1:]-b[:-1]))       # = int 2 a db
    S=0.5*J - 0.5*np.sum((b[1:]+b[:-1])*(a[1:]-a[:-1]))  # int (a db - b da)
    print(s,'a0=%.5f b0=%.5f'%(a[0],b[0]),' int 2a db = %.6f'%J, ' int(a db - b da) = %.6f'%S, ' +n a0 = %.6f'%(S+2*a[0]))
# double points / b at a=1/4
k=np.argsort(abs(A-0.25))[:4]; print('points near a=1/4:',[(round(A[i],4),round(B[i],4)) for i in k])
k=np.argsort(abs(A-1/6))[:2]; print('near a=1/6:',[(round(A[i],4),round(B[i],4)) for i in k])
