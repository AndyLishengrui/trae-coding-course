import sys
data = sys.stdin.read().split()
n = int(data[0])
size = int(data[1])
arr = list(map(int, data[2:2+n]))
print(' '.join(map(str, arr[:size])))
