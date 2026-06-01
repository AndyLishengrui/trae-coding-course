import sys
data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:1+n]))
a.sort()
mid = a[n // 2]
ans = sum(abs(x - mid) for x in a)
print(ans)
