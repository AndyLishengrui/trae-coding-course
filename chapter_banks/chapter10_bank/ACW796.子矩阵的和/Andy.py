import sys
data = sys.stdin.read().split()
n, m, q = int(data[0]), int(data[1]), int(data[2])
a = [[0]*(m+1)]
idx = 3
for _ in range(n):
    a.append([0] + [int(data[idx+j]) for j in range(m)])
    idx += m
s = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]
out = []
for _ in range(q):
    x1,y1,x2,y2 = int(data[idx]),int(data[idx+1]),int(data[idx+2]),int(data[idx+3])
    idx += 4
    out.append(str(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]))
print('\n'.join(out))
