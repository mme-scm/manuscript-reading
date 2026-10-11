import json
from fractions import Fraction as F
d=json.load(open('rays120.json'))
idx={(c['a1'],c['a2'],c['r']):c for c in d}
def ell(c,k):
    z=c['Z'].get(str(k)); 
    return None if z is None or z['ell'] is None else F(z['ell'])
KS=range(-6,11)
nb=nt=nboth=0; ex_b=[]; ex_both=[]; jumps_top={}
for c in d:
    a1,a2,r,P=c['a1'],c['a2'],c['r'],c['P']
    m=idx[(a1,a2,P-r)]
    bot={k:ell(c,k) for k in KS}
    top={}
    for k in KS:
        e=ell(m,-1-k) if -1-k in KS else None
        top[k]=None if e is None else F(3,8)-e
    for a in KS:
        for b in KS:
            if b<=a: continue
            if bot[a] is not None and bot[a]==bot[b]:
                nb+=1; ex_b.append((a1,a2,r,a,b,bot[a]))
                if top[a] is not None and top[a]==top[b]:
                    nboth+=1; ex_both.append((a1,a2,r,a,b))
    # where does top go up along k?
    for k in KS:
        if k+1 in KS and top[k] is not None and top[k+1] is not None and top[k+1]>top[k]:
            jumps_top[k]=jumps_top.get(k,0)+1
print('chains',len(d))
print('pairs with equal ell (bottom):',nb)
print('examples:',ex_b[:12])
print('pairs with equal bottom AND top:',nboth, ex_both[:5])
print('top goes up at step k->k+1, counts by k:',sorted(jumps_top.items()))
# pairs a<b (b reached from a by b-a negative-definite steps): does bottom or top drop?
from collections import Counter
bad=Counter(); badex={}; tot=0
for c in d:
    a1,a2,r,P=c['a1'],c['a2'],c['r'],c['P']
    if r in (1,P-1): continue
    m=idx[(a1,a2,P-r)]
    bot={k:ell(c,k) for k in KS}
    top={k:(None if not (-1-k in KS) or ell(m,-1-k) is None else F(3,8)-ell(m,-1-k)) for k in KS}
    for a in KS:
        for b in KS:
            if b<=a or None in (bot[a],bot[b],top[a],top[b]): continue
            tot+=1
            if bot[b]>bot[a] and top[b]>top[a]:
                bad[(a,b)]+=1; badex.setdefault((a,b),(a1,a2,r))
print('non-torus pairs tested',tot,' pairs where neither bottom nor top drops:',sum(bad.values()))
print(sorted(bad.items())[:20]); print(list(badex.items())[:5])
# size: min over pairs with b-a = s of max(bottom drop, top drop); include torus chains (skip S^3 members)
for s in (1,2,3):
    best=None; arg=None; best_nt=None; arg_nt=None
    for c in d:
        a1,a2,r,P=c['a1'],c['a2'],c['r'],c['P']
        m=idx[(a1,a2,P-r)]
        bot={k:ell(c,k) for k in KS}
        top={k:(None if not (-1-k in KS) or ell(m,-1-k) is None else F(3,8)-ell(m,-1-k)) for k in KS}
        for a in KS:
            b=a+s
            if b not in KS or None in (bot[a],bot[b],top[a],top[b]): continue
            v=max(bot[a]-bot[b], top[a]-top[b])
            if best is None or v<best: best,arg=v,(a1,a2,r,a,b)
            if r not in (1,P-1) and (best_nt is None or v<best_nt): best_nt,arg_nt=v,(a1,a2,r,a,b)
    print('steps',s,' min max-drop all:',best,float(best),arg,' non-torus:',best_nt,float(best_nt),arg_nt)
