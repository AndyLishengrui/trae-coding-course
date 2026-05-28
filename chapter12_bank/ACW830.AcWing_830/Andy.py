# 单调栈
n = int(input())
a = list(map(int, input().split()))
stk = []
res = []
for x in a:
    while stk and stk[-1] >= x:
        stk.pop()
    res.append(str(stk[-1]) if stk else '-1')
    stk.append(x)
print(' '.join(res))
