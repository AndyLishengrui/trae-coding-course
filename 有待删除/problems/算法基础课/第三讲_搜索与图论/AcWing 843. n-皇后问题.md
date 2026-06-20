# AcWing 843. n-皇后问题 — DFS试炼之n皇后问题

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/843/

## 题目描述

n-皇后问题是指将 n 个皇后放在 n∗n 的国际象棋棋盘上，使得皇后不能相互攻击到，即任意两个皇后都不能处于同一行、同一列或同一斜线上。

数据范围:1<=n<=12

### 输入格式

共一行，包含整数n。

### 输出格式

每个解决方案占n行，每行输出一个长度为n的字符串，用来表示完整的棋盘状态。

其中”.”表示某一个位置的方格状态为空，”Q”表示某一个位置的方格上摆着皇后。

每个方案输出完成后，输出一个空行。

输出方案的顺序请根据样例，按照次序从小到大，从左到右输出。

### 样例

**输入:**
```
4
```

**输出:**
```
.Q..
...Q
Q...
..Q.
..Q.
Q...
...Q
.Q..
```

### 提示

原题链接

Y总讲解

## AC代码

```cpp
#include <iostream>
using namespace std;

const int N = 20;  //最大值
int n;             //输入的n
char g[N][N];      //棋盘
//三个指示器列、对角线、反对角线,对角线以截距为编号
bool col[N], dg[N], udg[N];

void dfs(int u) {
  if (u == n) {
    //输出排列
    for (int i = 0; i < n; i++) puts(g[i]);
    puts("");
    return;
  }
  //枚举列0--n
  for (int i = 0; i < n; i++) {
    if (!col[i] && !dg[i + u] && !udg[i - u + n]) {
      g[u][i] = 'Q';  //当前位置设置为Q字符
      col[i] = dg[i + u] = udg[i - u + n] = true;  //标记数字i为已经使用郭
      dfs(u + 1);                                  //递归处理下一个位
      g[u][i] = '.';                               //恢复现场
      col[i] = dg[i + u] = udg[i - u + n] = false;  //恢复现场
    }
  }
}

int main() {
  cin >> n;
  //初始化图
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) g[i][j] = '.';
  dfs(0);
  return 0;
}
```
