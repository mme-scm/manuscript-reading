import snappy
M = snappy.Manifold('5_2')
print(M.num_cusps(), M.volume(), M.chern_simons(), M.complex_volume())
print(M.cusp_info()[0])
for c in [(2,1),(-2,1),(1,0)]:
    N = M.copy(); N.dehn_fill(c)
    try:
        print(c, N.solution_type(), N.volume(), N.chern_simons(), N.cusp_info()[0].get('core_length'))
    except Exception as e:
        print(c, 'err', e)
# cone
for s in [0.25,0.5,0.75,1.0]:
    N = M.copy(); N.dehn_fill((2/s,1/s))
    print(s, N.solution_type(), N.volume(), N.cusp_info()[0].get('core_length'))
