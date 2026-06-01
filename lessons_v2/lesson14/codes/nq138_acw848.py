import sys
from collections import deque
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
adj = [[] for _ in range(n+1)]
indeg = [0]*(n+1)
idx = 2
for _ in range(m):
    x, y = int(data[idx]), int(data[idx+1])
    idx += 2
    adj[x].append(y); indeg[y] += 1
q = deque([i for i in range(1,n+1) if indeg[i]==0])
res = []
while q:
    u = q.popleft()
    res.append(str(u))
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
print(' '.join(res) if len(res)==n else -1)
