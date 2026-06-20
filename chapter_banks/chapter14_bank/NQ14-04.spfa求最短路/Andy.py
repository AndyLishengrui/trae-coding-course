import sys
from collections import deque
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
adj = [[] for _ in range(n+1)]
idx = 2
for _ in range(m):
    x, y, z = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    adj[x].append((y, z))
INF = 10**15
dist = [INF]*(n+1)
dist[1] = 0
st = [False]*(n+1)
q = deque([1])
st[1] = True
while q:
    u = q.popleft()
    st[u] = False
    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            if not st[v]:
                q.append(v); st[v] = True
print(dist[n] if dist[n] != INF else 'impossible')
