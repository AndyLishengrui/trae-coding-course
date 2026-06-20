import sys
data = sys.stdin.read().split()
for val in data:
    n = int(val)
    if n == 0: break
    for i in range(n):
        row = []
        for j in range(n):
            v = 1
            for k in range(i + j):
                v *= 2
            row.append(str(v))
        print(' '.join(row) + ' ')
    print()
