import sys
data = sys.stdin.read().split()
n, l, r = int(data[0]), int(data[1]), int(data[2])
a = list(map(int, data[3:3+n]))
a[l:r+1] = sorted(a[l:r+1])
print(' '.join(map(str, a)))
