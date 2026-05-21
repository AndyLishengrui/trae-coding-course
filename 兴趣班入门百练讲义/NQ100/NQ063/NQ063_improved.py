def precalculate():
    MAX_N = 40
    dp = [0] * (MAX_N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, MAX_N + 1):
        dp[i] = dp[i-1] + dp[i-2]  # 动态规划：第i级台阶的走法数=前一级+前两级
    return dp

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    dp = precalculate()
    q = int(input[idx])
    idx += 1
    for _ in range(q):
        n = int(input[idx])
        idx += 1
        if 1 <= n <= 40:
            print(dp[n])

if __name__ == "__main__":
    main()