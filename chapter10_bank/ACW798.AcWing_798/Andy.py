# 差分矩阵
n, m, q = map(int, input().split())
a = [[0] * (m + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))
b = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        b[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]
for _ in range(q):
    x1, y1, x2, y2, c = map(int, input().split())
    b[x1][y1] += c
    b[x2 + 1][y1] -= c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y2 + 1] += c
for i in range(1, n + 1):
    row = []
    cur = 0
    for j in range(1, m + 1):
        b[i][j] += b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
        row.append(str(b[i][j]))
    print(' '.join(row))
