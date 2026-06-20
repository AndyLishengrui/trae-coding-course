import sys
sys.setrecursionlimit(200000)
# 最长上升子序列
n = int(input())
a = list(map(int, input().split()))
tails = []
for x in a:
    l, r = 0, len(tails)
    while l < r:
        mid = (l + r) // 2
        if tails[mid] >= x:
            r = mid
        else:
            l = mid + 1
    if l == len(tails):
        tails.append(x)
    else:
        tails[l] = x
print(len(tails))
