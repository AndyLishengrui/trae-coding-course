# NQ053 最长回文子串

## 问题描述
寻找字符串中最长的回文子串。

## 算法选择
采用**中心扩展法**，该方法利用回文子串的对称性，通过以每个字符或两个相邻字符为中心向两边扩展，找到最长的回文子串。

## 算法原理
1. **回文子串的对称性**：回文子串从中心向两边对称，因此可以通过中心扩展的方式检测
2. **中心类型**：
   - 奇数长度回文子串：中心为单个字符（如 "aba" 的中心是 "b"）
   - 偶数长度回文子串：中心为两个相邻字符（如 "abba" 的中心是 "bb"）
3. **扩展过程**：从中心向两边扩展，直到字符不匹配或越界

## 实现步骤
1. **边界处理**：如果字符串为空或长度为1，直接返回原字符串
2. **遍历可能的中心**：
   - 对于每个字符位置 i，作为奇数长度回文子串的中心
   - 对于每个相邻字符对 (i, i+1)，作为偶数长度回文子串的中心
3. **扩展并记录**：
   - 从中心向两边扩展，记录当前回文子串的长度
   - 如果找到更长的回文子串，更新结果
4. **返回结果**：返回找到的最长回文子串

## 代码实现分析

### C++ 实现
```cpp
string longestPalindrome(string s) {
    string res;
    int n = s.size();
    
    for (int i = 0; i < n; i++) {
        // 奇数长度回文子串扩展
        int l = i, r = i;
        while (l >= 0 && r < n && s[l] == s[r]) {
            l--;
            r++;
        }
        if (res.size() < r - l - 1) {
            res = s.substr(l + 1, r - l - 1);
        }
        
        // 偶数长度回文子串扩展
        l = i, r = i + 1;
        while (l >= 0 && r < n && s[l] == s[r]) {
            l--;
            r++;
        }
        if (res.size() < r - l - 1) {
            res = s.substr(l + 1, r - l - 1);
        }
    }
    return res;
}
```

### Python 实现
```python
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
```

## 代码优化点
1. **变量命名**：使用更清晰的变量名（如 `n` 表示字符串长度）
2. **代码结构**：将扩展逻辑封装为辅助函数（Python实现），提高代码可读性
3. **性能优化**：
   - 记录起始索引和长度，避免频繁创建子串（Python实现）
   - 减少重复计算，提高代码效率

## 算法分析
- **时间复杂度**：O(N²)，其中 N 是字符串长度
  - 需要遍历每个可能的中心（共 2N-1 个）
  - 每个中心最多扩展 N 次
- **空间复杂度**：O(1)，只使用了常数级的额外空间

## 测试案例
- 输入："babad" → 输出："bab" 或 "aba"
- 输入："cbbd" → 输出："bb"
- 输入："a" → 输出："a"
- 输入："" → 输出：""

## 总结
中心扩展法是解决最长回文子串问题的有效方法，它利用回文的对称性，通过线性扫描和中心扩展的方式，在 O(N²) 的时间复杂度内找到最长回文子串。该方法代码简洁，易于理解，同时具有较好的性能表现。