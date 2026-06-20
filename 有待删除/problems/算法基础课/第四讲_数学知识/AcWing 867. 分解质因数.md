# AcWing 867. 分解质因数 — 分解质因数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/867/

## 题目描述

给定n个正整数ai，将每个数分解质因数，并按照质因数从小到大的顺序输出每个质因数的底数和指数。

### 输入格式

第一行包含整数n。

接下来n行，每行包含一个正整数aiai。

### 输出格式

对于每个正整数aiai,按照从小到大的顺序输出其分解质因数后，每个质因数的底数和指数，每个底数和指数占一行。

每个正整数的质因数全部输出完毕后，输出一个空行。

### 样例

**输入:**
```
2
6
8
```

**输出:**
```
2 1
3 1

2 3
```

### 提示

原题链接

Y总讲解

Y总代码

## AC代码

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void divide(int n){
    for (int i=2; i<= n / i; i++)//注意不要用i*i<=n避免溢出
     if (n % i==0){
         int nums = 0;
         while(n % i == 0){
             n /= i;
             nums ++;
         }
         printf("%d %d\n",i,nums);//i出现nums次
     }
     //n中只包含一个大于sqrt(n)的质因子
     if (n > 1) printf("%d %d\n",n,1);//n是除掉所有因子后剩下的数
     puts("");//换行
}

int main()
{
    int n; cin >> n; //读入n
    while (n--)
    {
        int a;cin >> a;             //读入a
        divide(a); //使用auto自动判定属性
    }
    return 0;
}
```
