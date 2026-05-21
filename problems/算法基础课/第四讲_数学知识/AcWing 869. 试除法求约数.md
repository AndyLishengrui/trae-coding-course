# AcWing 869. 试除法求约数 — 试除法求约数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/869/

## 题目描述

给定n个正整数ai，对于每个整数ai,请你按照从小到大的顺序输出它的所有约数。

### 输入格式

第一行包含整数n。

接下来n行，每行包含一个整数ai。

### 输出格式

输出共n行，其中第 i 行输出第 i 个整数ai的所有约数。

### 样例

**输入:**
```
2
6
8
```

**输出:**
```
1 2 3 6 
1 2 4 8
```

### 提示

原题链接

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//求约数，返回值存在vector之中
vector<int> get_divisors(int n)
{
    vector<int> res;

    for (int i=1; i<=n /i; i++)
       if (n % i == 0)//是n的约数
         {
             res.push_back(i);//i如果是约数
             if (i != n/i) res.push_back(n /i);// n/i也是约数
         }
    //排序
    sort(res.begin(), res.end());//使用算法sort排序
    return res;
}

int main(){
    int n;  cin>>n;//读入n
    while(n--){
        int a;  cin>>a; //读入a
        auto res=get_divisors(a);//使用auto自动判定属性
        for(auto i:res) cout<<i<<' ';
        cout<<endl;
    }
    return 0;
}
```
