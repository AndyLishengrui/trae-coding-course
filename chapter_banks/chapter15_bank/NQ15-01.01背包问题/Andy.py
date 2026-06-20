# 01背包问题
N, V = map(int, input().split())
f = [0] * (V + 1)
for _ in range(N):
    v, w = map(int, input().split())
    for j in range(V, v - 1, -1):
        f[j] = max(f[j], f[j - v] + w)
print(f[V])
