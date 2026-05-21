# AcWing 891. Nim游戏 — Nim游戏

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/891/

## 题目描述

给定n堆石子，两位玩家轮流操作，每次操作可以从任意一堆石子中拿走任意数量的石子（可以拿完，但不能不拿），最后无法进行操作的人视为失败。

问如果两人都采用最优策略，先手是否必胜。

### 输入格式

第一行包含整数n。

第二行包含n个数字，其中第i个数字表示第i堆石子的数量。

### 输出格式

如果先手方必胜，则输出“Yes”。

否则，输出“No”。

### 样例

**输入:**
```
2
2 3
```

**输出:**
```
Yes
```

### 提示

原题链接

## AC代码

```cpp
// 作者：qiaoxinwei
// 链接：https://www.acwing.com/solution/content/14269/
// 来源：AcWing
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#include <iostream>
#include <cstdio>
using namespace std;

/*
先手必胜状态：先手操作完，可以走到某一个必败状态
先手必败状态：先手操作完，走不到任何一个必败状态
先手必败状态：a1 ^ a2 ^ a3 ^ ... ^an = 0
先手必胜状态：a1 ^ a2 ^ a3 ^ ... ^an ≠ 0
*/

int main(){
    int n;
    scanf("%d", &n);
    int res = 0;
    for(int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        res ^= x;
    }
    if(res == 0) puts("No");
    else puts("Yes");
}
```
