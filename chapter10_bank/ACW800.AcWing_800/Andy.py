# 数组元素的目标和
n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, m - 1
while i < n and j >= 0:
    s = a[i] + b[j]
    if s == x:
        print(i, j)
        break
    elif s < x:
        i += 1
    else:
        j -= 1
