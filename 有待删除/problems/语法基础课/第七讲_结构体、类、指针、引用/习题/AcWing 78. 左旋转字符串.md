# AcWing 78. 左旋转字符串

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/78/

## 题目描述
> 待补充

### 输入格式
> 待补充

### 输出格式
> 待补充

### 样例
> 待补充

## AC代码

```cpp
class Solution {
public:
    string leftRotateString(string str, int n) {
        return str.substr(n) + str.substr(0, n);
    }
};
```
