# Kruskal
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()
p = list(range(n + 1))

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

ans = 0
cnt = 0
for w, u, v in edges:
    ru, rv = find(u), find(v)
    if ru != rv:
        p[ru] = rv
        ans += w
        cnt += 1
print(ans if cnt == n - 1 else 'impossible')
