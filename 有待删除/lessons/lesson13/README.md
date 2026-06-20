# 第13课：搜索与回溯

> **课时：** 2小时 | **题目：** 3例题 + 3练习 | **难度：** ⭐⭐⭐⭐ | **算法进阶**

## 一、本课目标
1. 掌握 DFS 回溯框架：选择→递归→撤销选择
2. 掌握 BFS 层序框架：`deque` + visited + 方向数组
3. 理解搜索树的大小与剪枝优化

## 二、核心框架

### DFS 回溯模板
```python
def dfs(path, choices):
    if 满足条件:
        result.append(path[:])
        return
    for choice in choices:
        if 合法:
            path.append(choice)       # 做选择
            dfs(path, choices)        # 递归
            path.pop()                # 撤销（回溯）
```

### BFS 最短路径模板
```python
from collections import deque
q = deque([start])
dist = {start: 0}
while q:
    cur = q.popleft()
    for nxt in neighbors(cur):
        if nxt not in dist:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
```

## 三、题目

| 题号 | 题目 | 类型 | 算法 | Python工具 |
|------|------|------|------|-----------|
| NQ073 | 排列数字 | 例题 | DFS回溯 | 手写/`itertools.permutations` |
| NQ074 | n-皇后问题 | 例题 | DFS+剪枝 | 对角线判断 |
| NQ075 | 走迷宫 | 例题 | BFS | `deque`+方向数组 |
| NQ076 | 八数码 | 练习 | BFS状态搜索 | `tuple`做不可变状态 |
| NQ077 | 树的重心 | 练习 | DFS树 | `defaultdict(list)`存树 |
| NQ078 | 图中点的层次 | 练习 | BFS层序 | `deque` |

## 四、AI 协作要点

DFS/BFS 是面试最高频考点。让学生理解：DFS=递归栈，BFS=显式队列。两种搜索的本质区别是什么？让 Trae 用通俗语言解释。
