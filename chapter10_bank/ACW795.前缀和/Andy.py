import sys
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
a = list(map(int, data[2:2+n]))
s = [0]*(n+1)
for i in range(1,n+1): s[i] = s[i-1] + a[i-1]
idx = 2 + n
out = []
for _ in range(m):
    l, r = int(data[idx]), int(data[idx+1])
    idx += 2
    out.append(str(s[r] - s[l-1]))
print('\n'.join(out))
