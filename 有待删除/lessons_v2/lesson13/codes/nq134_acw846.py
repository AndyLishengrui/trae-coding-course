# 树的重心
import sys
sys.setrecursionlimit(200000)
n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = n
def dfs(u, fa):
    global ans
    sz = 1
    max_part = 0
    for v in adj[u]:
        if v != fa:
            sv = dfs(v, u)
            sz += sv
            max_part = max(max_part, sv)
    max_part = max(max_part, n - sz)
    ans = min(ans, max_part)
    return sz

dfs(1, -1)
print(ans)
