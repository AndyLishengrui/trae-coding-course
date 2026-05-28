import sys
from collections import deque
data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
a = list(map(int, data[2:2+n]))
q = deque()
for i in range(n):
    while q and a[q[-1]] >= a[i]: q.pop()
    q.append(i)
    if q[0] <= i - k: q.popleft()
    if i >= k - 1: sys.stdout.write(str(a[q[0]]) + (' ' if i < n-1 else '\n'))
q.clear()
for i in range(n):
    while q and a[q[-1]] <= a[i]: q.pop()
    q.append(i)
    if q[0] <= i - k: q.popleft()
    if i >= k - 1: sys.stdout.write(str(a[q[0]]) + (' ' if i < n-1 else '\n'))
