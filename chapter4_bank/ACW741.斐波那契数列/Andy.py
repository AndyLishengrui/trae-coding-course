import sys
data = sys.stdin.read().split()
n = int(data[0]) if data else 0
a, b = 0, 1
for _ in range(n):
    sys.stdout.write(str(a) + (' ' if _ < n-1 else '\n'))
    a, b = b, a + b
