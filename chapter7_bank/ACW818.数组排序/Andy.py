import sys
data = sys.stdin.read().split()
n, size = int(data[0]), int(data[1])
a = list(map(int, data[2:2+n]))
a.sort()
print(' '.join(map(str, a[:size])))
