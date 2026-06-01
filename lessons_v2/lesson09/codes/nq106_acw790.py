# 数的三次方根
n = float(input())
l, r = -10000.0, 10000.0
while r - l > 1e-8:
    mid = (l + r) / 2.0
    if mid ** 3 >= n:
        r = mid
    else:
        l = mid
print(f'{r:.6f}')
