import sys
sys.setrecursionlimit(200000)
# 最短编辑距离
n = int(input())
a = input().strip()
m = int(input())
b = input().strip()
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    f[i][0] = i
for j in range(m + 1):
    f[0][j] = j
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            f[i][j] = f[i - 1][j - 1]
        else:
            f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
print(f[n][m])
