# 差分
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] * (n + 2)
for i in range(1, n + 1):
    b[i] = a[i] - a[i - 1]
for _ in range(m):
    l, r, c = map(int, input().split())
    b[l] += c
    b[r + 1] -= c
res = []
cur = 0
for i in range(1, n + 1):
    cur += b[i]
    res.append(str(cur))
print(' '.join(res))
