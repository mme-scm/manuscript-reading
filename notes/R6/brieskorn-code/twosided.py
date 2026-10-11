import json
from fractions import Fraction as F
d=json.load(open('rays120.json'))
idx={(c['a1'],c['a2'],c['r']):c for c in d}
KS=range(-6,11)
def ell(c,k):
    z=c['Z'].get(str(k)); return None if z is None or z['ell'] is None else F(z['ell'])
res={}
for c in d:
    a1,a2,r,P=c['a1'],c['a2'],c['r'],c['P']; m=idx[(a1,a2,P-r)]
    bot={k:ell(c,k) for k in KS}
    top={k:(None if not (-1-k in KS) or ell(m,-1-k) is None else F(3,8)-ell(m,-1-k)) for k in KS}
    for a in KS:
        for b in KS:
            if b<=a or None in (bot[a],bot[b],top[a],top[b]): continue
            v=max(bot[a]-bot[b], top[a]-top[b]); s=b-a
            if s not in res or v<res[s][0]: res[s]=(v,(a1,a2,r,a,b))
for s in sorted(res): print(s, res[s][0], round(float(res[s][0]),4), res[s][1], ' s/16=',s/16)
