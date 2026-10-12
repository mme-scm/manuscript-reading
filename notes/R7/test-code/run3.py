from knots import torus
from triangle import *
D = torus(3, 5)
for which in ('I','II'):
    I = analyse(D, which, ('q1','q2'), 'int')
    M = I['M']
    for key in ('vA','vB'):
        print(key, 'failing entries:')
        for (x,y) in sorted(I['rel'][key], key=lambda e:(e[0].level,e[1].level)):
            print('   ', x.level, x.label, '->', y.level, y.label)
    # list gAn and gAs polygons
    for k in ('gAs','gAn','gM','c'):
        print(k)
        for p in sorted(I['P'][k], key=lambda p:p['src'].level):
            print('   %s %s -> %s %s area=%s corners=%s onb=%s' % (p['src'].level, p['src'].label, p['dst'].level, p['dst'].label, p['area'], p['corners'], p['onb']))
