import sympy as sp
a,b,p,q,r,S,t=sp.symbols('a b p q r S t')
ap=p*a+q*b; bp=r*a+S*b
g=2*q*r*a*b+p*r*a**2+q*S*b**2
# 1-form coefficients (da, db)
lhs_da=2*bp*sp.diff(ap,a)-2*b; lhs_db=2*bp*sp.diff(ap,b)
cond={S:(1+q*r)/p}
print(sp.simplify((lhs_da-sp.diff(g,a)).subs(cond)), sp.simplify((lhs_db-sp.diff(g,b)).subs(cond)))
print(sp.factor(sp.simplify(g.subs({a:t*q,b:-t*p}).subs(cond))))
# claim 5
from fractions import Fraction as Fr
for n in range(1,9):
    vals=set()
    for k in range(-3,4):
        s=Fr(-1,2)+k; f1=-(n-1)*s*s
        for j in range(-3,4):
            aa=Fr(-(n-1),2)+j; f2=aa
            vals.add((f1-f2)%1)
    print(n, vals, Fr(n-1,4)%1)
