import sys
sys.setrecursionlimit(200000)
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
p = list(range(n+1))
sz = [1]*(n+1)
def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x
idx = 2
out = []
for _ in range(m):
    op = data[idx]
    if op == 'C':
        a, b = int(data[idx+1]), int(data[idx+2])
        idx += 3
        ra, rb = find(a), find(b)
        if ra != rb: p[ra] = rb; sz[rb] += sz[ra]
    elif op == 'Q1':
        a, b = int(data[idx+1]), int(data[idx+2])
        idx += 3
        out.append('Yes' if find(a)==find(b) else 'No')
    else:
        a = int(data[idx+1])
        idx += 2
        out.append(str(sz[find(a)]))
print('\n'.join(out))
