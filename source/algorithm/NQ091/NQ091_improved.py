# Python equivalent of the optimized C++ code
# 骑士周游问题
import sys
dirs = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
path = [None]*30
n, m = 0, 0  # n是行数，m是列数
visited = [[False]*30 for _ in range(30)]
def dfs(r, c, step):
    global visited, path, n, m
    if step == n*m:
        return True
    if r < 0 or r >= n or c < 0 or c >= m or visited[r][c]:
        return False
    visited[r][c] = True
    path[step] = (r, c)
    for i in range(8):
        dr, dc = dirs[i]
        if dfs(r+dr, c+dc, step+1):
            return True
    visited[r][c] = False
    return False
def main():
    global visited, path, n, m
    t = int(sys.stdin.readline())
    for tt in range(1, t+1):
        print("#"+str(tt)+":")
        m, n = map(int, sys.stdin.readline().split())  # m是列数，n是行数
        for i in range(30):
            for j in range(30):
                visited[i][j] = False
        found = False
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    found = True
                    for k in range(n*m):
                        print(chr(ord('A')+path[k][0])+str(path[k][1]+1), end="")
                    break
            if found:
                break
        if not found:
            print("none", end="")
        print()
if __name__ == "__main__":
    main()
