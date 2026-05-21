import sys

def dfs(i, j, h, d, R, C):
    if d[i][j] != -1: return d[i][j]  # 记忆化剪枝
    
    max_len = 1  # 初始长度为1（当前位置）
    
    # 四个方向的偏移量：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # 检查边界并确保高度递减
        if 0 <= ni < R and 0 <= nj < C and h[i][j] > h[ni][nj]:
            length = dfs(ni, nj, h, d, R, C) + 1
            max_len = max(max_len, length)
    
    d[i][j] = max_len  # 记忆化存储结果
    return max_len

def main():
    input = sys.stdin.read().split()
    idx = 0
    R = int(input[idx])
    idx += 1
    C = int(input[idx])
    idx += 1
    
    # 读取高度矩阵（0-based索引）
    h = []
    for _ in range(R):
        row = []
        for __ in range(C):
            row.append(int(input[idx]))
            idx += 1
        h.append(row)
    
    d = [[-1 for _ in range(C)] for _ in range(R)]  # 初始化记忆化数组
    
    ans = 0
    for i in range(R):
        for j in range(C):
            ans = max(ans, dfs(i, j, h, d, R, C))
    
    print(ans)

if __name__ == "__main__":
    main()
