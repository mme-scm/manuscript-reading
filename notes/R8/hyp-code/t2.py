import snappy, warnings
warnings.filterwarnings('ignore')
for name in ['K11n42','K11n34','7_4','6_2','6_3']:
    M = snappy.Manifold(name)
    ci = M.cusp_info()[0]
    out=[name, 'vol %.6f cs %.6f'%(M.volume(), M.chern_simons()), 'shape', ci['shape']]
    for c in [(2,1),(-2,1)]:
        N = M.copy(); N.dehn_fill(c)
        out.append((c, N.solution_type(), '%.6f'%N.volume(), '%.6f'%N.chern_simons(), N.cusp_info()[0].get('core_length')))
    print(*out, sep='\n  ')
N = snappy.Manifold('K11n42'); N.dehn_fill((2/0.75,1/0.75)); print(N.cusp_info()[0])
