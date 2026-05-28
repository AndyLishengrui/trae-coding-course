import sys
sys.setrecursionlimit(200000)
# Floyd求最短路
n, m, q = map(int, input().split())
INF = 0x3f3f3f3f
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    d[x][y] = min(d[x][y], z)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i][k] != INF and d[k][j] != INF:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
for _ in range(q):
    a, b = map(int, input().split())
    print(d[a][b] if d[a][b] < INF // 2 else 'impossible')
