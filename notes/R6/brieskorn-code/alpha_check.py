import sys; sys.path.insert(0,'.')
from bk import analyse
from fractions import Fraction as F
# beta from closed form: beta^2 = m^2 - 16 P m (A* - ell), A* = A + r/(16P); fit A* from two members of same class
def core_dev(A0, out, idx):
    # sorted presentation
    A=out['A_sorted']; b=out['b_sorted']
    order=sorted(range(3), key=lambda i: A0[i]); pos=order.index(idx)
    m=A[pos]; bK=b[pos]
    res=[]
    for eps,l in out['argmin']:
        lK=l[idx]
        k=0 if eps==1 else 1
        # core c = u q + v h with m v - bK u = 1
        for u in range(1,2*m):
            if (1+bK*u) % m==0:
                v=(1+bK*u)//m; break
        th=F(u*lK,m)+v*k     # theta/pi
        t=th%1               # in [0,1)
        res.append(abs(2*m*t-m))
    return res
for (aj,ak,r) in [(3,5,7),(3,5,8),(3,7,11),(5,7,9),(2,5,7),(2,3,1),(3,7,13)]:
    P=aj*ak; data=[]
    for j in range(0,8):
        m=r+j*P; out=analyse((aj,ak,m))
        if out['count']==0: continue
        data.append((j,m,out['cmin'],core_dev((aj,ak,m),out,2)))
    # fit A*: for each class use ell = A* - (m^2-beta^2)/(16Pm); with 2 members per class solve
    for par in (0,1):
        cl=[d for d in data if d[0]%2==par]
        (j1,m1,l1,_),(j2,m2,l2,_)=cl[-2],cl[-1]
        # A* - m/(16P) + beta^2/(16Pm) = l
        # unknowns A*, B=beta^2: A* + B/(16Pm) = l + m/(16P)
        y1=l1+F(m1,16*P); y2=l2+F(m2,16*P)
        B=(y1-y2)/(F(1,16*P*m1)-F(1,16*P*m2)); As=y1-B/(16*P*m1)
        print((aj,ak,r),'class',par,'A*=',As,'beta^2=',B,' core deviations:',[(d[1],d[3]) for d in cl])
