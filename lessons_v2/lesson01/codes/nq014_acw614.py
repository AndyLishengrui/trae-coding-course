import sys
data = sys.stdin.read().split()
if data:
    a, b, c = map(int, data[:3])
    mx = max(a, b, c)
    print(f"{mx} eh o maior")
