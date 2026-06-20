import sys
sys.setrecursionlimit(200000)
# 排列数字
n = int(input())
path = []
used = [False] * (n + 1)

def dfs():
    if len(path) == n:
        print(' '.join(map(str, path)) + ' ')
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            path.append(i)
            dfs()
            path.pop()
            used[i] = False

dfs()
