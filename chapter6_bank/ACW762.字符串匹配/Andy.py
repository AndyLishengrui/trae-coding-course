import sys
data = sys.stdin.read().split()
k = float(data[0])
a, b = data[1], data[2]
cnt = sum(1 for i in range(len(a)) if a[i] == b[i])
print("yes" if cnt / len(a) >= k else "no")
