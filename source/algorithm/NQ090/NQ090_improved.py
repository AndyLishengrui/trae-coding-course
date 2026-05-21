# Python equivalent of the optimized C++ code
# 黄金蛋糕人马切割问题
import sys

MAX_W = 27
MAX_H = 27
MAX_M = 407
INF = 0x3f3f3f3f

# 记忆化数组：minMax[w][h][cnt]表示将w×h的矩形切成cnt+1块时的最小最大面积
minMax = [[[-1 for _ in range(MAX_M)] for __ in range(MAX_H)] for ___ in range(MAX_W)]

def dfs(w, h, cnt):
    if w * h < cnt + 1:
        return INF  # 无法分割
    if cnt == 0:
        return w * h  # 不需要切
    if minMax[w][h][cnt] != -1:
        return minMax[w][h][cnt]  # 记忆化剪枝
    
    minMArea = INF
    
    # 尝试竖切
    for i in range(1, w):
        for k in range(cnt + 1):
            left = dfs(i, h, k)
            right = dfs(w - i, h, cnt - 1 - k)
            minMArea = min(minMArea, max(left, right))
    
    # 尝试横切
    for j in range(1, h):
        for k in range(cnt + 1):
            top = dfs(w, j, k)
            bottom = dfs(w, h - j, cnt - 1 - k)
            minMArea = min(minMArea, max(top, bottom))
    
    minMax[w][h][cnt] = minMArea  # 记忆化存储
    return minMArea

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        W, H, M = map(int, line.split())
        if W == 0 and H == 0:
            break
        # 重置记忆化数组
        for i in range(MAX_W):
            for j in range(MAX_H):
                for k in range(MAX_M):
                    minMax[i][j][k] = -1
        print(dfs(W, H, M - 1))

if __name__ == "__main__":
    main()