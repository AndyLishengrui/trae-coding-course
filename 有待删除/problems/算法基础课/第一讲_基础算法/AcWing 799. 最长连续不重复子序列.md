# AcWing 799. 最长连续不重复子序列 — 最长连续不重复子序列

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/799/

## 题目描述

给定一个长度为n的整数序列，请找出最长的不包含重复数字的连续区间，输出它的长度。

数据范围：

1≤n≤100000

### 输入格式

第一行包含整数n。

第二行包含n个整数（均在0~100000范围内），表示整数序列。

### 输出格式

共一行，包含一个整数，表示最长的不包含重复数字的连续子序列的长度。

### 样例

**输入:**
```
5
1 2 2 3 5
```

**输出:**
```
3
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
using namespace std;
const int N=100007;
int num[N],visited[N];

int main(){
    int n;
    cin>>n;
    for (int i=0; i<n; i++ ) cin>>num[i];//读入n个数
    //双指针扫描
    int res=0;//初始化为最小值
    for (int i=0, j=0; i<n; i++){
        visited[num[i]]++;
        while(j<=i && visited[num[i]]>1){
            visited[num[j]]--;
            j++; //去掉重复数
        }
        res= max(res,i-j+1);//j--i 之间的数字个数
    }
    cout<<res<<endl;
    return 0;
}
```
