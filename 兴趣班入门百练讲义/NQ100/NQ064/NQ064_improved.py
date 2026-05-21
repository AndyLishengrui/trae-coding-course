def calculate_cats(year):
    if year < 5:
        return year
    dp = [0] * (year + 1)
    for i in range(1, 5):
        dp[i] = i
    for i in range(5, year + 1):
        dp[i] = dp[i-1] + dp[i-3]  # 递推公式：第n年猫数=前一年+前三年
    return dp[year]

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    for _ in range(n):
        m = int(input[idx])
        idx += 1
        print(calculate_cats(m))

if __name__ == "__main__":
    main()