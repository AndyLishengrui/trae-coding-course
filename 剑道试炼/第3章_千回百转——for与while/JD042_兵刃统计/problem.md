# JD042：兵刃统计

> **AcWing 718** | 第3章 · 千回百转 | 知识点：循环、统计

## 题目描述

演武场上，弟子们正在操练。李少白走过一排兵器架，记录了N次观察：每次看到一件兵器，C代表剑，R代表刀，F代表枪。赵晴儿让他统计每种兵器出现了多少把，以及各自的占比。

## 输入格式

第一行一个整数N。接下来N行，每行一个整数（数量）和一个字符（C/R/F），分别表示某次看到的兵器数量和类型。

## 输出格式

第一行输出 `Total: X weapons`（总数量）。接下来三行输出每种兵器的总数：`Total swords: X`、`Total blades: X`、`Total spears: X`。最后三行输出各自占比：`Percentage of swords: XX.XX %` 等，保留两位小数。

## 样例

输入：

```text
11
1 F
5 C
4 C
12 C
11 F
15 F
2 F
7 C
1 C
4 C
9 F
```

输出：

```text
Total: 71 weapons
Total swords: 33
Total blades: 0
Total spears: 38
Percentage of swords: 46.48 %
Percentage of blades: 0.00 %
Percentage of spears: 53.52 %
```

## 解题思路

三个计数器分别累加C、R、F的数量。注意每行先读数量再读类型。总数 = 所有数量之和。占比 = 各类数量 / 总数 × 100%，保留两位小数。
