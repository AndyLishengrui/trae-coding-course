import sys
from collections import deque
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
g = []
idx = 2
for _ in range(n):
    g.append([int(data[idx+j]) for j in range(m)])
    idx += m
dist = [[-1] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
q.append((0, 0))
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
print(dist[n - 1][m - 1])
