def longest_palindrome(s):
    """最长回文子串"""
    if not s:
        return ""
    
    n = len(s)
    start, max_len = 0, 0
    
    def expand_around_center(left, right):
        """从中心向两边扩展，返回回文子串的起始索引和长度"""
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1
    
    for i in range(n):
        # 奇数长度回文子串
        l1, len1 = expand_around_center(i, i)
        # 偶数长度回文子串
        l2, len2 = expand_around_center(i, i + 1)
        
        # 更新最长回文子串信息
        if len1 > max_len:
            start, max_len = l1, len1
        if len2 > max_len:
            start, max_len = l2, len2
    
    return s[start:start + max_len]

def main():
    s = input().strip()
    print(longest_palindrome(s))

if __name__ == "__main__":
    main()