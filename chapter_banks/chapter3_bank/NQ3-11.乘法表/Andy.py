import sys
n = int(sys.stdin.read().strip())
for i in range(1, 11):
    print(f"{i} x {n} = {i * n}")
