# 字符串乘方
while True:
    s = input().strip()
    if s == '.':
        break
    n = len(s)
    ne = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = ne[j - 1]
        if s[i] == s[j]:
            j += 1
        ne[i] = j
    length = n - ne[n - 1]
    if n % length == 0:
        print(n // length)
    else:
        print(1)
