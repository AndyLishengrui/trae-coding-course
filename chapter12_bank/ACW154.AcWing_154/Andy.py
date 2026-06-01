import sys
from collections import deque
data = sys.stdin.buffer.read().split()
n, k = int(data[0]), int(data[1])
a = [int(x) for x in data[2:2+n]]
q = deque()
mins = []
for i in range(n):
    while q and a[q[-1]] >= a[i]: q.pop()
    q.append(i)
    if q[0] <= i - k: q.popleft()
    if i >= k - 1: mins.append(str(a[q[0]]))
q.clear()
maxs = []
for i in range(n):
    while q and a[q[-1]] <= a[i]: q.pop()
    q.append(i)
    if q[0] <= i - k: q.popleft()
    if i >= k - 1: maxs.append(str(a[q[0]]))
sys.stdout.write(' '.join(mins) + '\n')
sys.stdout.write(' '.join(maxs) + '\n')
