# AcWing 763. 循环相克令 — 循环相克令

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/763/

## 题目描述

循环相克令是一个两人玩的小游戏。令词为“猎人、狗熊、枪”，两人同时说出令词，同时做出一个动作——

猎人的动作是双手叉腰；狗熊的动作是双手搭在胸前；枪的动作是双手举起呈手枪状。

双方以此动作判定输赢，猎人赢枪、枪赢狗熊、狗熊赢猎人，动作相同则视为平局。

现在给定你一系列的动作组合，请你判断游戏结果。

### 输入格式

第一行包含整数 T，表示共有 T 组测试数据。
数据范围：1 ≤ T ≤ 100

接下来 T 行，每行包含两个字符串，表示一局游戏中两人做出的动作，字符串为`Hunter`、`Bear`、`Gun`中的一个，

这三个单词分别代表猎人、狗熊和枪。

### 输出格式

如果第一个玩家赢了，则输出`Player1`。
如果第二个玩家赢了，则输出`Player2`。
如果平局，则输出`Tie`。

### 样例

**输入:**
```
3
Hunter Gun
Bear Bear
Hunter Bear
```

**输出:**
```
Player1
Tie
Player2
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n -- )
    {
      string a, b;
      cin >> a >> b;

      int x, y;
      if (a == "Hunter") x = 0;
      else if (a == "Bear") x = 1;
      else x = 2;

      if (b == "Hunter") y = 0;
      else if (b == "Bear") y = 1;
      else y = 2;

      if (x == y) puts("Tie");
      else if (x == (y + 1) % 3) puts("Player1");
      else puts("Player2");
    }

  return 0;  
}
```
