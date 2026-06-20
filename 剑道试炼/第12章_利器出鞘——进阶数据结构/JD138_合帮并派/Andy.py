import sys
sys.setrecursionlimit(200000)
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
p = list(range(n+1))
def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x
idx = 2
out = []
for _ in range(m):
    op, a, b = data[idx], int(data[idx+1]), int(data[idx+2])
    idx += 3
    if op == 'M': p[find(a)] = find(b)
    else: out.append('Yes' if find(a) == find(b) else 'No')
print('\n'.join(out))
