# AcWing 87. 把字符串转换成整数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/87/

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
    int strToInt(string str) {
        int k = 0;
        while (k < str.size() && str[k] == ' ') k ++ ;
        long long res = 0;

        int minus = 1;
        if (k < str.size())
        {
           if (str[k] == '-') minus = -1, k ++ ;
           else if (str[k] == '+') k ++ ;
        }
        while (k < str.size() && str[k] >= '0' && str[k] <= '9')
        {
          res = res * 10 + str[k] - '0';
          if (res > 1e11) break;
          k ++ ;
        }

        res *= minus;
        if (res > INT_MAX) res = INT_MAX;
        if (res < INT_MIN) res = INT_MIN;

        return res;
    }
};
```
