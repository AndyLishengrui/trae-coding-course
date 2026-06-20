# Dijkstra I (朴素版)
n, m = map(int, input().split())
g = [[0x3f3f3f3f] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    g[x][y] = min(g[x][y], z)
dist = [0x3f3f3f3f] * (n + 1)
dist[1] = 0
st = [False] * (n + 1)
for _ in range(n):
    t = -1
    for i in range(1, n + 1):
        if not st[i] and (t == -1 or dist[i] < dist[t]):
            t = i
    st[t] = True
    for v in range(1, n + 1):
        if dist[v] > dist[t] + g[t][v]:
            dist[v] = dist[t] + g[t][v]
print(dist[n] if dist[n] != 0x3f3f3f3f else -1)
