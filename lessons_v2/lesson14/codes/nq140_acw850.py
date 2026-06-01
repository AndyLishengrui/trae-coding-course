import sys
import heapq
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
heap = [(0, 1)]
while heap:
    d, u = heapq.heappop(heap)
    if st[u]: continue
    st[u] = True
    for v, w in adj[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            heapq.heappush(heap, (dist[v], v))
print(dist[n] if dist[n] != INF else -1)
