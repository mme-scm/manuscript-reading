import json
from fractions import Fraction as Fr
import sys
data=json.load(open(sys.argv[1] if len(sys.argv)>1 else "chains.json"))
summary=[]
for ch in data:
    aj,ak,r,P=ch['aj'],ch['ak'],ch['r'],ch['P']
    rows=ch['rows']
    issues=[]
    # beta per member (ties with different beta flagged)
    for x in rows:
        if len(x['betas'])>1: issues.append("tie-betas j=%d m=%d %s"%(x['j'],x['m'],x['betas']))
    # A* per member with each beta candidate
    Astar=[]
    for x in rows:
        m=x['m']; l=Fr(x['ell'])
        Astar.append({b: l+Fr(m*m-b*b,16*P*m) for b in x['betas']})
    # beta constant on parity classes?
    cls={0:set(),1:set()}
    for x in rows: cls[x['j']%2].add(tuple(x['betas']))
    # A* constant (use first beta)
    Avals=[min(d.values()) for d in Astar]
    Aset=set(Avals)
    # find members where A* differs from the mode
    from collections import Counter
    mode=Counter(Avals).most_common(1)[0][0]
    off=[(x['j'],x['m'],x['betas'],str(Fr(x['ell']))) for x,Av in zip(rows,Avals) if Av!=mode]
    # two-step drop formula check: ell_j - ell_{j+2} == 1/8 + beta_j^2/(8 m m'')? using beta of j (claim says beta constant on class)
    td_bad=[]
    for i in range(len(rows)-2):
        x,z=rows[i],rows[i+2]
        if z['j']!=x['j']+2: continue
        T=Fr(x['ell'])-Fr(z['ell'])
        ok=any(T==Fr(1,8)+Fr(b*b,8*x['m']*z['m']) for b in set(x['betas'])&set(z['betas']))
        if not ok: td_bad.append((x['m'],z['m'],str(T)))
    summary.append(((aj,ak,r),P,len(rows),{k:sorted(v) for k,v in cls.items()},str(mode),off,td_bad,issues))
nok=0
for s in summary:
    (ch,P,n,cls,mode,off,td,iss)=s
    good = all(len(v)==1 for v in cls.values()) and not off and not td
    nok+=good
    flag="OK " if good else "BAD"
    print(flag,ch,"P=",P,"members",n,"beta by class",cls,"A*=",mode, ("off:"+str(off)) if off else "", ("twostep-fail:"+str(td[:3])) if td else "", iss if iss else "")
print("chains fully consistent:",nok,"of",len(summary))
