import json,sys,math
R=[r for r in json.load(open(sys.argv[1])) if 'err' not in r]
def clean(r): return r['2']['worst']=='all' and r['-2']['worst']=='all' and r['2']['jump']<0.3 and r['-2']['jump']<0.3
C=[r for r in R if clean(r)]
print('total',len(R),'clean',len(C))
for lab,S in (('all',R),('clean',C)):
    if not S: continue
    w=max(S,key=lambda r:max(r['2']['window'],r['-2']['window']))
    print(lab,'max window',w['name'],round(max(w['2']['window'],w['-2']['window']),3))
    d=max(S,key=lambda r:abs(r['Z'][1]))
    print(lab,'max |Delta|',d['name'],round(d['Z'][1],4),'lead',round(d['Zlead'][1],4))
    e=sorted(S,key=lambda r:-abs(r['Z'][1]-r['Zlead'][1]))
    print(lab,'max |Delta-Dlead|',[(r['name'],round(r['Z'][1]-r['Zlead'][1],3)) for r in e[:6]])
    er=sorted(abs(r['Z'][1]-r['Zlead'][1]) for r in S); print(lab,'median |D-Dlead|',er[len(er)//2])
    ec=sorted(abs(complex(*r['Z'])-complex(-r['Zlead'][0],r['Zlead'][1])) for r in S); print(lab,'median |Z-Zlead| (complex, sign-fixed)',ec[len(ec)//2],'max',ec[-1])
    y=min(S,key=lambda r:r['tau'][1]); print(lab,'min Im tau',y['name'],round(y['tau'][1],3))
    L=max(S,key=lambda r:max(r['2']['L'],r['-2']['L'])); print(lab,'max L',L['name'],round(max(L['2']['L'],L['-2']['L']),3))
    Lm=max(min(r['2']['L'],r['-2']['L']) for r in S); print(lab,'max min(L+,L-)',round(Lm,3))
    t0=max(max(abs(r['2']['t0']),abs(r['-2']['t0'])) for r in S); print(lab,'max |t0|',round(t0,3))
    # ratio of window at the end
    we=max(max(abs(r[N]['uend'][1])/math.pi for N in ('2','-2')) for r in S); print(lab,'max |tau(2pi)|/pi',round(we,3))
