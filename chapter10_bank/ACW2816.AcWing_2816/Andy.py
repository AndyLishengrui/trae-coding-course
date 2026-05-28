# 判断子序列
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
for x in b:
    if i < n and a[i] == x:
        i += 1
print('Yes' if i == n else 'No')
