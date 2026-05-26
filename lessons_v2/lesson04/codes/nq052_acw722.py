# NQ: AcWing 722
while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0: break
    if a > b: a, b = b, a
    print(' '.join(str(i) for i in range(a, b + 1)), f"Sum={sum(range(a, b + 1))}")
