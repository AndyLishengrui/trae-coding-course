# NQ: AcWing 672
x = float(input())
if x <= 2000:
    print('Isento')
else:
    x -= 2000
    t = 0
    if x > 0:
        v = min(x, 1000)
        t += v * 0.08
        x -= v
    if x > 0:
        v = min(x, 1500)
        t += v * 0.18
        x -= v
    if x > 0:
        t += x * 0.28
    print(f"R$ {t:.2f}")
