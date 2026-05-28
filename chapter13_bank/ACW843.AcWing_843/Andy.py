import sys
sys.setrecursionlimit(200000)
# n-皇后问题
n = int(input())
g = [['.'] * n for _ in range(n)]
col = [False] * n
dg = [False] * (2 * n)
udg = [False] * (2 * n)

def dfs(r):
    if r == n:
        for row in g:
            print(''.join(row))
        print()
        return
    for c in range(n):
        if not col[c] and not dg[r + c] and not udg[r - c + n]:
            col[c] = dg[r + c] = udg[r - c + n] = True
            g[r][c] = 'Q'
            dfs(r + 1)
            g[r][c] = '.'
            col[c] = dg[r + c] = udg[r - c + n] = False

dfs(0)
