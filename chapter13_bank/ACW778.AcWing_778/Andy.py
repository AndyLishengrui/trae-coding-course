# 字符串最大跨距
s, s1, s2 = input().split(',')
n = len(s)
l = s.find(s1)
r = s.rfind(s2)
if l == -1 or r == -1 or l + len(s1) > r:
    print(-1)
else:
    print(r - l - len(s1))
