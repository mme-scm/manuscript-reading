"""Closed-form exploration along chains: g(j) = ell(Z_j) + j/16 and fits alpha - gamma/(r+jP)."""
import json, sys
from fractions import Fraction as F
chains = json.load(open('rays120.json'))
def get(a1,a2,r):
    for ch in chains:
        if (ch['a1'],ch['a2'],ch['r'])==(a1,a2,r): return ch
for key in [(2,3,1),(2,3,5),(2,5,3),(2,5,7),(3,4,5),(3,4,7),(3,5,2),(3,5,7),(3,5,4),(2,7,9)]:
    ch = get(*key); P = ch['P']; r = ch['r']
    Z = {int(k):v for k,v in ch['Z'].items()}
    print("chain", key)
    for j in range(0, 11):
        v = Z[j]
        if v['ell'] is None: continue
        ell = F(v['ell']); m = r + j*P; a = P*m
        g = ell + F(j,16)
        mins = [(mm['l'], mm['e'] % (2*a), mm['gr'], 'T' if mm['traceless'] else '.') for mm in v['min']]
        # gamma such that ell = CS-like: 4a*(alpha - ell) ...
        print("  j=%2d m=%4d ell=%-14s g=ell+j/16=%-14s  8a*ell=%d  min=%s" % (j, m, ell, g, 8*a*ell, mins))
