# JD131：叠石成塔

> **AcWing 828** | 第12章 · 利器出鞘 | 知识点：剑道录

## 题目描述

梁嘉峰在墙角堆了一摞石块："栈——后进先出。只能从顶部放石块，也只能从顶部取。"

赵晴儿指着石块："push是放石块到顶部，pop是取走顶部的石块，query是看看顶部那块刻着什么数。"

"生活中到处是栈——叠盘子、摞书、函数调用。"

实现一个栈，支持push、pop、query操作。

## 输入格式

若干行操作命令：push x（入栈）、pop（出栈）、query（查询栈顶）。

## 输出格式

对每个query和pop操作输出一行结果。

## 样例

输入：

```text
10
push 5
query
push 6
pop
query
pop
push 3
query
push 4
query
```

输出：

```text
5
5
3
4
```

## 解题思路

数组模拟栈：tt指向栈顶。push: st[++tt]=x。pop: tt--。query: st[tt]。
