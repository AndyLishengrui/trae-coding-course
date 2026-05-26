# NQ: AcWing 670
a, b, c = input().split()
b = int(b)
if a == 'vertebrado':
    if b == 0: print('aguia' if c == 'carnivoro' else 'pomba')
    else: print('homem' if c == 'onivoro' else 'vaca')
else:
    if b == 0: print('pulga' if c == 'hematofago' else 'lagarta')
    else: print('sanguessuga' if c == 'hematofago' else 'minhoca')
