import sys
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
g = [[10**15]*(n+1) for _ in range(n+1)]
idx = 2
for _ in range(m):
    u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    g[u][v] = g[v][u] = min(g[u][v], w)
INF = 10**15
dist = [INF]*(n+1)
st = [False]*(n+1)
ans = 0
for _ in range(n):
    t = -1
    for i in range(1, n+1):
        if not st[i] and (t == -1 or dist[i] < dist[t]): t = i
    if _ > 0 and dist[t] == INF: print('impossible'); sys.exit(0)
    if _ > 0: ans += dist[t]
    st[t] = True
    for v in range(1, n+1):
        if dist[v] > g[t][v]: dist[v] = g[t][v]
print(ans)
