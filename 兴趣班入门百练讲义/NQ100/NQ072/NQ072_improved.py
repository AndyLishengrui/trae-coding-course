def is_safe(row, col, positions):
    for i in range(row):
        if positions[i] == col: return False  # 检查列冲突
        if abs(positions[i] - col) == abs(row - i): return False  # 检查对角线冲突
    return True

def dfs(row, N, positions):
    if row == N:
        print(''.join(map(str, positions)))
        return
    for col in range(1, N + 1):
        if is_safe(row, col, positions):
            positions[row] = col
            dfs(row + 1, N, positions)  # 递归搜索下一行

def main():
    N = int(input().strip())
    positions = [0] * N
    dfs(0, N, positions)

if __name__ == "__main__":
    main()
