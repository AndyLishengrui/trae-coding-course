import sys
data = sys.stdin.read().split()
idx = 0
n, m, q = int(data[idx]), int(data[idx+1]), int(data[idx+2])
idx += 3
INF = 0x3f3f3f3f
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0
for _ in range(m):
    x, y, z = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    if z < d[x][y]:
        d[x][y] = z
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if d[i][k] == INF:
            continue
        for j in range(1, n + 1):
            if d[k][j] != INF and d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
out = []
for _ in range(q):
    a, b = int(data[idx]), int(data[idx+1])
    idx += 2
    out.append(str(d[a][b]) if d[a][b] < INF // 2 else 'impossible')
sys.stdout.write('\n'.join(out) + '\n')
