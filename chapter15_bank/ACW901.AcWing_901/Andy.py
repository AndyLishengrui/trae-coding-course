# 滑雪
import sys
sys.setrecursionlimit(1000000)
R, C = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1] * C for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and h[nx][ny] < h[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

ans = 0
for i in range(R):
    for j in range(C):
        ans = max(ans, dfs(i, j))
print(ans)
