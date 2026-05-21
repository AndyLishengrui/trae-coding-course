import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    volume = [0] * (n + 1)
    value = [0] * (n + 1)
    for i in range(1, n + 1):
        volume[i] = int(input[idx])
        idx += 1
        value[i] = int(input[idx])
        idx += 1
    
    dp = [0] * (m + 1)  # dp[j] 表示背包容量为j时的最大价值
    
    # 遍历每个物品，逆序更新dp数组以避免重复选择
    for i in range(1, n + 1):
        for j in range(m, volume[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - volume[i]] + value[i])
    
    print(dp[m])

if __name__ == "__main__":
    main()
