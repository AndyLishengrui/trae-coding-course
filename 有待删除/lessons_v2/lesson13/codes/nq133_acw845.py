import sys
from collections import deque
start = ''.join(sys.stdin.read().split())
target = '12345678x'
if start == target: print(0); sys.exit(0)
dx, dy = [-1,0,1,0], [0,1,0,-1]
q = deque([start])
dist = {start: 0}
while q:
    s = q.popleft()
    k = s.index('x')
    x, y = k//3, k%3
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<3 and 0<=ny<3:
            nk = nx*3 + ny
            lst = list(s)
            lst[k], lst[nk] = lst[nk], lst[k]
            ns = ''.join(lst)
            if ns not in dist:
                dist[ns] = dist[s] + 1
                if ns == target: print(dist[ns]); sys.exit(0)
                q.append(ns)
print(-1)
