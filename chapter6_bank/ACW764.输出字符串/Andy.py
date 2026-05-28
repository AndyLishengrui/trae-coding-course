import sys
data = sys.stdin.read().split()
a, b = data[0], data[1]
for i in range(len(a)):
    if a[i] != b[i]:
        print(b[i:])
        break
else:
    print(b)
