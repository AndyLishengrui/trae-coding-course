import sys
import bisect
data = sys.stdin.read().split()
n, q = int(data[0]), int(data[1])
a = list(map(int, data[2:2+n]))
idx = 2 + n
out = []
for _ in range(q):
    x = int(data[idx]); idx += 1
    l = bisect.bisect_left(a, x)
    r = bisect.bisect_right(a, x) - 1
    if l < n and a[l] == x: out.append(f'{l} {r}')
    else: out.append('-1 -1')
print('\n'.join(out))
