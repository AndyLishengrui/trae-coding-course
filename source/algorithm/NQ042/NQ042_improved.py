# NQ042 最长无重复子串
def length_of_longest_substring(s):
    """计算不包含重复字符的最长子串长度"""
    count = {}  # 字符计数
    res = 0  # 最长长度
    j = 0  # 左指针
    for i in range(len(s)):
        c = s[i]
        count[c] = count.get(c, 0) + 1
        # 处理重复字符
        while count[c] > 1:
            count[s[j]] -= 1
            j += 1
        res = max(res, i - j + 1)
    return res
def main():
    s = input().strip()
    print(length_of_longest_substring(s))
if __name__ == "__main__":
    main()