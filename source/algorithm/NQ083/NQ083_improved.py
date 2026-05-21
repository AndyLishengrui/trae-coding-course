def longest_common_subsequence(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # 字符相同，长度加1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 字符不同，取最大值
    return dp[len1][len2]

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        s1, s2 = parts
        result = longest_common_subsequence(s1, s2)
        print(result)

if __name__ == "__main__":
    main()
