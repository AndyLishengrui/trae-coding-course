import sys
n = int(sys.stdin.read().split()[0])
cx = cy = n // 2
for i in range(n):
    row = []
    for j in range(n):
        if abs(i-cx) + abs(j-cy) <= n//2: row.append('*')
        else: row.append(' ')
    print(''.join(row))
