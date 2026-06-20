import sys
data = sys.stdin.read().split()
if len(data) >= 2:
    a = data[0]
    b = data[1]
    p = 0
    for i in range(len(a)):
        if a[i] > a[p]:
            p = i
    print(a[:p+1] + b + a[p+1:])
