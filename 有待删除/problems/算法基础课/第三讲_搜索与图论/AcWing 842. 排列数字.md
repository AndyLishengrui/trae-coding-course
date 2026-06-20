# AcWing 842. 排列数字 — DFS试炼之排列数字

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/842/

## 题目描述

给定一个整数n，将数字1~n排成一排，将会有很多种排列方法。

现在，请你按照字典序将所有的排列方法输出。

数据范围：1<=n<=7

### 输入格式

共一行，包含一个整数n。

### 输出格式

按字典序输出所有排列方案，每个方案占一行。

### 样例

**输入:**
```
3
```

**输出:**
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

### 提示

Andy讲解(2021)

原题链接

## AC代码

```cpp
#include <iostream>
using namespace std;

const int N = 10;  //最大值
int n;             //读入的n
int path[N];       //记录路径每个位的值
bool used[N];      //记录第i个数是否被用过

void dfs(int u) {
  if (u == n) {
    //输出排列
    for (int i = 0; i < n; i++) cout << path[i] << " ";
    cout << endl;
    return;
  }
  //枚举数字1--n
  for (int i = 1; i <= n; i++) {
    if (!used[i]) {
      path[u] = i;      //记录当前位path[u]的数字为i
      used[i] = true;   //标记数字i为已经使用郭
      dfs(u + 1);       //递归处理下一个位
      used[i] = false;  //恢复现场
    }
  }
}

int main() {
  cin >> n;
  dfs(0);
  return 0;
}
```
