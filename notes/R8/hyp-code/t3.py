import snappy, warnings, math, cmath, sys
warnings.filterwarnings('ignore')
name = sys.argv[1] if len(sys.argv)>1 else 'K11n42'
M = snappy.Manifold(name)
print(name, M.cusp_info()[0].keys())
N = M.copy(); N.dehn_fill((2/0.6,1/0.6)); print(N.cusp_info()[0]['holonomies'], N.solution_type())
