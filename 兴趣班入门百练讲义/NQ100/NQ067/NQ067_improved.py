def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    k_max_column = 30
    dp = [0] * (k_max_column + 1)
    dp[0] = 1  # 空墙面
    dp[2] = 3  # 3x2 墙面的基础铺法
    
    # 递推计算偶数列的铺法数
    for i in range(4, k_max_column + 1, 2):
        dp[i] = 4 * dp[i-2] - dp[i-4]
    
    # 处理输入
    while idx < len(input):
        n = int(input[idx])
        idx += 1
        if n == -1:
            break
        print(dp[n])

if __name__ == "__main__":
    main()