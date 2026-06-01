import sys
data = sys.stdin.read().split()
n = int(data[0])
idx = 1
a = []
for i in range(n):
    a.append([int(data[idx+j]) for j in range(i+1)])
    idx += i + 1
for i in range(n-2, -1, -1):
    for j in range(i+1):
        a[i][j] += max(a[i+1][j], a[i+1][j+1])
print(a[0][0])
