import sys
data = list(map(int, sys.stdin.read().split()))
n = data[0]
vals = data[1:n+1]
mx = max(vals)
pos = vals.index(mx) + 1
print(mx)
print(pos)
