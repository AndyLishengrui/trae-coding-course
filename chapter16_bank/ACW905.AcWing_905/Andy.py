# 区间选点
n = int(input())
segs = []
for _ in range(n):
    l, r = map(int, input().split())
    segs.append((l, r))
segs.sort(key=lambda x: x[1])
ans = 0
last = -2 * 10**9
for l, r in segs:
    if l > last:
        ans += 1
        last = r
print(ans)
