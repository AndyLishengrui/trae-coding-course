# JD132：列阵待命

> **AcWing 829** | 第12章 · 利器出鞘 | 知识点：剑道录

## 题目描述

赵晴儿指着一排队列："队列——先进先出。新来的站队尾，走的从队头走。"

梁嘉峰说："push是从队尾加入，pop是从队头弹出，query是看队头是谁。"

"排队买饭、消息队列、BFS——都是队列。"

实现一个队列，支持push、pop、query操作。

## 输入格式

若干行操作命令：push x（入队）、pop（出队）、query（查询队头）。

## 输出格式

对每个query和pop操作输出一行结果。

## 样例

输入：

```text
10
push 5
query
push 3
pop
query
push 7
push 8
pop
query
pop
```

输出：

```text
5
3
7
7
```

## 解题思路

数组模拟队列：hh队头，tt队尾。push: q[++tt]=x。pop: hh++。query: q[hh]。
