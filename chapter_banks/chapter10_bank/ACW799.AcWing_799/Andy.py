# 最长连续不重复子序列
n = int(input())
a = list(map(int, input().split()))
cnt = {}
l = 0
ans = 0
for r in range(n):
    cnt[a[r]] = cnt.get(a[r], 0) + 1
    while cnt[a[r]] > 1:
        cnt[a[l]] -= 1
        l += 1
    ans = max(ans, r - l + 1)
print(ans)
