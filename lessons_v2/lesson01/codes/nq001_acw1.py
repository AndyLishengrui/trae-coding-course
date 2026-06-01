import sys
data = sys.stdin.read().split()
if data:
    a, b = map(int, data[:2])
    print(a + b)
