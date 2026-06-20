import sys
sys.setrecursionlimit(200000)
data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
p = list(range(n + 1))
d = [0] * (n + 1)

def find(x):
    if p[x] != x:
        root = find(p[x])
        d[x] += d[p[x]]
        p[x] = root
    return p[x]

ans = 0
idx = 2
for _ in range(k):
    t = int(data[idx]); x = int(data[idx+1]); y = int(data[idx+2])
    idx += 3
    if x > n or y > n:
        ans += 1; continue
    rx, ry = find(x), find(y)
    if t == 1:
        if rx == ry and (d[x] - d[y]) % 3 != 0: ans += 1
        elif rx != ry:
            p[rx] = ry
            d[rx] = d[y] - d[x]
    else:
        if rx == ry and (d[x] - d[y] - 1) % 3 != 0: ans += 1
        elif rx != ry:
            p[rx] = ry
            d[rx] = d[y] - d[x] + 1
print(ans)
