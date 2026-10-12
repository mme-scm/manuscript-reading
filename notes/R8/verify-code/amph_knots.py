# (e) PSL-level amphichiral consistency using SnapPy + cone paths.
import snappy, warnings, math, json
warnings.filterwarnings('ignore')
R={r['name']:r for r in json.load(open('../code/survey10.json')) if 'err' not in r}
for nm in ['4_1','6_3','8_3','8_9','8_12','8_17','8_18','10_17','10_33','10_37','10_43','10_45','10_79','10_81','10_88','10_99','10_109','10_115','10_118','10_123']:
    M=snappy.Manifold(nm); xE=float(M.chern_simons())
    if nm not in R: print(nm,'xE=%.6f'%xE,'(not in clean survey)'); continue
    r=R[nm]
    X=M.copy(); X.dehn_fill((2,1)); x2=float(X.chern_simons()); Y=M.copy(); Y.dehn_fill((-2,1)); xm2=float(Y.chern_simons())
    print('%-7s xE=%+.6f  I2=%+.6f I-2=%+.6f (sum %.1e)  x(Y2)+x(Y-2) mod 1/2=%.1e   x(Y2)-I2 mod 1/2=%.6f'%(
        nm,xE,r['2']['I'],r['-2']['I'],r['2']['I']+r['-2']['I'],((x2+xm2+0.25)%0.5)-0.25,((x2-r['2']['I']+0.25)%0.5)-0.25))
