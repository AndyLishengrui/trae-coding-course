# KMP字符串
n = int(input())
p = input().strip()
m = int(input())
s = input().strip()
ne = [0] * n
j = 0
for i in range(1, n):
    while j > 0 and p[i] != p[j]:
        j = ne[j - 1]
    if p[i] == p[j]:
        j += 1
    ne[i] = j
j = 0
res = []
for i in range(m):
    while j > 0 and s[i] != p[j]:
        j = ne[j - 1]
    if s[i] == p[j]:
        j += 1
    if j == n:
        res.append(str(i - n + 1))
        j = ne[j - 1]
print(' '.join(res))
