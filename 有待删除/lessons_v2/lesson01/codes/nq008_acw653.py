import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    print(n)
    for v in [100, 50, 20, 10, 5, 2, 1]:
        print(f"{n // v} nota(s) de R$ {v},00")
        n %= v
