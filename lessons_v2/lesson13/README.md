# 第13课：搜索与回溯

> **课时：** 2小时 | **题目：** 8题（3例题+5练习） | **阶段：** 核心算法 | **NQ130-NQ137**

## 一、教学目标

1. 掌握 DFS 回溯框架：选择 → 递归 → 撤销选择
2. 掌握 BFS 层序框架：deque + visited + 方向数组
3. 理解搜索树大小与剪枝优化的关系
4. 字符串高级题：周期串（KMP 的简化理解）、find/rfind 双向搜索

## 二、核心框架

### DFS 回溯

```python
def dfs(path, choices):
    if 满足结束条件:
        result.append(path[:])  # 注意拷贝！
        return
    for choice in choices:
        if 合法(choice):
            path.append(choice)   # 做选择
            dfs(path, choices)    # 递归
            path.pop()            # 撤销（回溯）
```

### BFS 最短路径

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

### N皇后剪枝

```python
# 核心：用集合判断列/对角线冲突 O(1)
cols = set()       # 列冲突
diag1 = set()      # 主对角线 i+j
diag2 = set()      # 副对角线 i-j
```

**教学点：** 对角线哈希 `i+j` 和 `i-j` 是 N 皇后的精髓。同一主对角线上所有格子 `i+j` 相同，同一副对角线 `i-j` 相同。

## 三、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 算法 |
|---|-----|------|--------|------|------|
| 1 | NQ130 | 排列数字 | 842 | 例题 | DFS回溯 |
| 2 | NQ131 | n-皇后问题 | 843 | 例题 | DFS+对角线剪枝 ★ |
| 3 | NQ132 | 走迷宫 | 844 | 例题 | BFS+方向数组 |
| 4 | NQ133 | 八数码 | 845 | 练习 | BFS状态搜索 ★★ |
| 5 | NQ134 | 树的重心 | 846 | 练习 | DFS树 |
| 6 | NQ135 | 图中点的层次 | 847 | 练习 | BFS层序 |
| 7 | NQ136 | 字符串乘方 | 777 | 练习 | 周期串 |
| 8 | NQ137 | 字符串最大跨距 | 778 | 练习 | find/rfind双向 |

**代码文件：** `codes/nq130_acw842.cpp` ～ `codes/nq137_acw778.cpp`
