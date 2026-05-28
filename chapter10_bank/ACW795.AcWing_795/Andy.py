# 前缀和
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]
for _ in range(m):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])
