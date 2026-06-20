# AcWing 26. 二进制中1的个数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/26/

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
    // lowbit写法
    int NumberOf1(int n) {
        int res = 0;

        while (n) n -= n & -n, res ++;

        return res;
    }
};
```
