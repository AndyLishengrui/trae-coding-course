n = int(input())
a = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, i+1):
        a[i][j] = row[j-1]
f = [[0]*(n+1) for _ in range(n+1)]
f[1][1] = a[1][1] # 边界条件：顶点的路径和为自身
for i in range(2, n+1):
    for j in range(1, i+1):
        f[i][j] = max(f[i-1][j-1], f[i-1][j]) + a[i][j] # 取上方或左上方的最大值
res = 0
for j in range(1, n+1):
    res = max(res, f[n][j]) # 最后一行的最大值即为答案
print(res)