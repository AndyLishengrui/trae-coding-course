import sys
sys.setrecursionlimit(200000)
# 染色法判定二分图
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
color = [0] * (n + 1)

def dfs(u, c):
    color[u] = c
    for v in adj[u]:
        if color[v] == 0:
            if not dfs(v, 3 - c):
                return False
        elif color[v] == c:
            return False
    return True

ok = True
for i in range(1, n + 1):
    if color[i] == 0:
        if not dfs(i, 1):
            ok = False
            break
print('Yes' if ok else 'No')
