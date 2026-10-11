import numpy as np
exec(open('fig8d.py').read().split("print('max residual'")[0])
A=np.array(A); B=np.array(B)
# lift along loop from index 0
b=np.unwrap(2*np.pi*B)/(2*np.pi); a=A.copy()
fG=np.concatenate([[0],np.cumsum((b[1:]+b[:-1])*(a[1:]-a[:-1]))])   # int 2b da from base
for (p,q) in [(1,1),(-1,1),(1,2),(1,-2)]:
    g=p*a+q*b  # want integer
    ks=np.where(np.floor(g[1:])!=np.floor(g[:-1]))[0]
    out=[]
    for k in ks:
        # linear interpolate where p a + q b = integer
        m=np.floor(max(g[k],g[k+1]));

        t=(m-g[k])/(g[k+1]-g[k]); 
        ax=a[k]+t*(a[k+1]-a[k]); bx=b[k]+t*(b[k+1]-b[k]); fx=fG[k]+t*(fG[k+1]-fG[k])
        # find lift of (ax,bx) on line p a + q b = 0: translate by v=(m1,n1) with p m1+q n1 = -m
        # solve with extended gcd small search
        sol=None
        for m1 in range(-10,11):
            for n1 in range(-10,11):
                if p*m1+q*n1==-m: 
                    if sol is None or abs(m1)+abs(n1)<abs(sol[0])+abs(sol[1]): sol=(m1,n1)
        m1,n1=sol
        ax2,bx2=ax+m1,bx+n1
        fx2=fx+2*n1*ax   # cocycle: f(x+v)=f(x)+2 n a(x) (+integer)
        s=ax2/q if q!=0 else -bx2/p
        fL=-p*q*s*s
        out.append((ax,bx%1,(fx2-fL)%1,(fx-(-p*q*((ax- 0)/q if q else 0)**2))%1))
    print('slope',p,q,'#pts',len(out))
    for o in out: print('   a=%.5f b=%.5f  A(corrected)=%.6f  naive=%.6f'%o)
    if len(out)>=2:
        As=[o[2] for o in out]; print('   pairwise diffs*168:', [round(((x-y)%1)*168,3) for x in As for y in As if x!=y])
