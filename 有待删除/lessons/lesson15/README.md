# 第15课：动态规划入门

> **课时：** 2小时 | **题目：** 3例题 + 3练习 | **难度：** ⭐⭐⭐⭐

## 一、本课目标
1. 理解 DP 的核心公式：`dp[i] = f(dp[i-1], dp[i-2], ...)`
2. 掌握三大经典模型：背包DP、线性DP、区间DP
3. **Python 秘技：** `@lru_cache` 自动记忆化递归

## 二、DP 的两种写法

```python
# 方法1：自底向上（迭代填表）
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(w[i], W + 1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

# 方法2：自顶向下（记忆化递归）— Python 一行装饰器搞定！
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(i, capacity):
    if i == 0: return 0
    if w[i] > capacity: return dfs(i - 1, capacity)
    return max(dfs(i - 1, capacity), dfs(i - 1, capacity - w[i]) + v[i])
```

**教学要点：** `@lru_cache` 让学生看到 DP 的本质就是"带记忆的递归"。把递归树画出来，重复计算的地方就是 memo 起作用的地方。

## 三、题目

| 题号 | 题目 | 类型 | 模型 | 核心 |
|------|------|------|------|------|
| NQ085 | 01背包 | 例题 | 01背包 | `dp[j]=max(dp[j], dp[j-w]+v)` |
| NQ086 | 完全背包 | 例题 | 完全背包 | 正序循环 |
| NQ087 | 数字三角形 | 例题 | 线性DP | 自底向上 |
| NQ088 | 最长上升子序列 | 练习 | LIS | `bisect`优化O(n log n) |
| NQ089 | 最长公共子序列 | 练习 | LCS | 二维dp |
| NQ090 | 石子合并 | 练习 | 区间DP | 区间dp+前缀和 |

## 四、AI 协作要点

DP 是算法学习的分水岭。让学生理解：DP 不是魔法，是"把大问题分解成有重叠的小问题，并把小问题的答案存下来"。
