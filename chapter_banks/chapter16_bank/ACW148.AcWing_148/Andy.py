import sys, heapq
data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:1+n]))
heapq.heapify(a)
ans = 0
while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    ans += x + y
    heapq.heappush(a, x + y)
print(ans)
