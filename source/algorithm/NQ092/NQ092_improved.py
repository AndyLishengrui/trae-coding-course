# Python equivalent of the optimized C++ code
# 骑士最短路径问题
import sys
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
n, m = 0, 0
g = []
d = []
start = (0,0)
target = (0,0)
def check(x, y):
    global n, m, g, d
    return 1 <= x <= n and 1 <= y <= m and g[x-1][y-1] != '*' and d[x][y] == -1
def find_start_and_target():
    global n, m, g, start, target
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'K':
                start = (i+1, j+1)
            if g[i][j] == 'H':
                target = (i+1, j+1)
def bfs():
    global n, m, start, target, d
    d = [[-1]*(m+2) for _ in range(n+2)]
    q = deque()
    q.append(start)
    d[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if check(nx, ny):
                d[nx][ny] = d[x][y]+1
                q.append((nx, ny))
                if (nx, ny) == target:
                    return d[nx][ny]
    return -1
def main():
    global n, m, g
    m, n = map(int, sys.stdin.readline().split())
    g = [sys.stdin.readline().strip() for _ in range(n)]
    find_start_and_target()
    print(bfs())
if __name__ == "__main__":
    main()
