import sys
data = sys.stdin.read().split()
n = int(data[0])
out = []
idx = 1
for _ in range(n):
    a, b, p = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    out.append(str(pow(a, b, p)))
print('\n'.join(out))
