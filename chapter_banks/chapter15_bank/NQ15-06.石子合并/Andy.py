import sys
data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:1+n]))
s = [0] * (n + 1)
for i in range(1, n+1): s[i] = s[i-1] + a[i-1]
INF = 10**9
f = [[0]*n for _ in range(n)]
for length in range(2, n+1):
    for l in range(n-length+1):
        r = l + length - 1
        f[l][r] = INF
        for k in range(l, r):
            f[l][r] = min(f[l][r], f[l][k] + f[k+1][r] + s[r+1] - s[l])
print(f[0][n-1])
