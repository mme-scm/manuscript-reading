import json, sys
from fractions import Fraction as Fr
from math import prod
data=json.load(open(sys.argv[1] if len(sys.argv)>1 else "fam.json"))
INF=None
def L(r): return None if r['ell'] is None else Fr(r['ell'])
kinds={}
c2=dict(n=0,a_fail=[],T_lt=[],Tmin=None,eq=[],mono_fail=[])
bands={b:dict(n=0,a_fail=0,Tge=0,Tlt=0,Tpos=0,Tmin=None,Tmax=None) for b in ("1-2P","2-3P","3-4P",">4P")}
c3ex=[]
one=dict(windows=0,viol=[],eq=0,minLplus={},)
onemin={}  # n -> (D, family)
nbig=0
for f in data:
    A=tuple(f['A']);K=f['K'];o=f['o'];rows=f['rows']
    a=prod(A);P=a//A[K];aK=A[K]
    ls=[L(r) for r in rows]
    if o==1: kind="L+"
    elif aK<P: kind="L-"
    else: kind="R-"
    kinds[kind]=kinds.get(kind,0)+1
    if o==1:
        c2['n']+=1; nbig+= a>2000
        l1,l2,l3=ls[1],ls[2],ls[3]
        if not(l1>l2>l3): c2['a_fail'].append((A,K))
        T=l1-l3
        if c2['Tmin'] is None or T<c2['Tmin'][0]: c2['Tmin']=(T,A,K)
        if T<Fr(1,8): c2['T_lt'].append((A,K,T))
        if T==Fr(1,8): c2['eq'].append((A,aK))
        if not all(ls[i]>ls[i+1] for i in range(len(ls)-1)): c2['mono_fail'].append((A,K))
    if kind=="R-":
        b="1-2P" if aK<2*P else "2-3P" if aK<3*P else "3-4P" if aK<4*P else ">4P"
        B=bands[b]; B['n']+=1
        l1,l2,l3=ls[1],ls[2],ls[3]
        if None in (l1,l2,l3): print("inf in R-",A,K); continue
        if not(l1>l2>l3): B['a_fail']+=1
        T=l1-l3
        if T>=Fr(1,8): B['Tge']+=1
        else: B['Tlt']+=1
        if T>0: B['Tpos']+=1
        B['Tmin']=T if B['Tmin'] is None else min(B['Tmin'],T)
        B['Tmax']=T if B['Tmax'] is None else max(B['Tmax'],T)
        if (A,aK) in [((2,5,23),23),((3,13,119),119)]: c3ex.append((A,aK,[str(x) for x in ls[1:4]],str(T)))
    # one-step windows (both link-oriented)
    for n in range(len(rows)-1):
        r0,r1=rows[n],rows[n+1]
        if r0['o']==1 and r1['o']==1 and ls[n] is not None and ls[n+1] is not None:
            D=ls[n]-ls[n+1]; m0=r0['B'][2]; m1=r1['B'][2]
            one['windows']+=1
            bd=Fr(m0,16*m1)
            if D<bd: one['viol'].append((A,K,o,n,D,bd))
            if D==bd: one['eq']+=1
            if kind=="L+":
                key=n
                if key not in onemin or D<onemin[key][0]: onemin[key]=(D,A,aK)
print("kinds",kinds)
print("CLAIM2 L+ families",c2['n'],"(base a>2000:",nbig,") (a) failures",len(c2['a_fail']),c2['a_fail'][:5])
print("  T1<1/8:",len(c2['T_lt']),c2['T_lt'][:5]," min T1",c2['Tmin'])
print("  T1=1/8 cases",c2['eq'])
print("  strict monotone n=0..5 failures",len(c2['mono_fail']),c2['mono_fail'][:5])
print("CLAIM3 R- bands")
for b,B in bands.items(): print("  ",b,{k:(str(v) if isinstance(v,Fr) else v) for k,v in B.items()})
print("  examples",c3ex)
print("CLAIM6 link-oriented one-step windows",one['windows'],"violations of D>=m/(16m')",len(one['viol']),one['viol'][:5],"equalities",one['eq'])
for n in sorted(onemin): D,A,aK=onemin[n]; print("  L+ min drop n=%d->%d:"%(n,n+1),D,float(D),A,"aK=",aK, "  >1/24?",D>Fr(1,24))
