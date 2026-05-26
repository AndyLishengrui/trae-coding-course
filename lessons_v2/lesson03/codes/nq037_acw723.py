# NQ: AcWing 723
n, m = map(int, input().split())
for i in range(1, n * m + 1):
    if i % m == 0:
        print('PUM')
    else:
        print(i, end=' ')
