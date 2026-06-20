# 第15课：动态规划

> **课时：** 2小时 | **题目：** 8题（3例题+5练习） | **阶段：** 算法进阶 | **NQ146-NQ153**

## 一、教学目标

1. 理解 DP 本质：**带记忆的递归**，把大问题分解为有重叠的子问题
2. 三大模型：背包DP（01/完全）、线性DP（LIS/LCS/编辑距离）、区间DP（石子合并）
3. **Python 秘技：** `@lru_cache` 自动记忆化，理解 DP 的递归视角
4. 空间优化：01背包从二维dp降到一维（逆序循环）

## 二、DP 两种写法对照

### 01背包

```python
# 方法1：自底向上（迭代填表）
dp = [0] * (W + 1)
for w, v in items:
    for j in range(W, w - 1, -1):  # 逆序！
        dp[j] = max(dp[j], dp[j - w] + v)

# 方法2：自顶向下（@lru_cache 记忆化）
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(i, cap):
    if i == 0: return 0
    if w[i] > cap: return dfs(i-1, cap)
    return max(dfs(i-1, cap), dfs(i-1, cap-w[i]) + v[i])
```

**教学点：** `@lru_cache` 让学生看到 DP 就是"把递归树中重复计算的节点缓存起来"。画一棵递归树，标注哪些节点被重复计算，那些就是 memo 的用武之地。

### 关键递推公式

| 模型 | 递推式 |
|------|--------|
| 01背包 | `dp[j] = max(dp[j], dp[j-w] + v)` |
| 完全背包 | `dp[j] = max(dp[j], dp[j-w] + v)` (正序) |
| LIS | `dp[i] = max(dp[i], dp[j] + 1)` for j<i and a[j]<a[i] |
| LCS | `dp[i][j] = dp[i-1][j-1]+1` (等) / `max(dp[i-1][j], dp[i][j-1])` |
| 编辑距离 | `dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(a[i]!=b[j]))` |
| 区间DP | `dp[i][j] = min(dp[i][k] + dp[k+1][j]) + sum[i..j]` |
| 记忆化滑雪 | `dfs(i,j) = 1 + max(四个方向的dfs)` if 高度递减 |

## 三、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 模型 |
|---|-----|------|--------|------|------|
| 1 | NQ146 | 01背包问题 | 2 | 例题 | 01背包 |
| 2 | NQ147 | 完全背包问题 | 3 | 例题 | 完全背包 |
| 3 | NQ148 | 数字三角形 | 898 | 例题 | 线性DP |
| 4 | NQ149 | 最长上升子序列 | 895 | 练习 | LIS+bisect ★ |
| 5 | NQ150 | 最长公共子序列 | 897 | 练习 | LCS |
| 6 | NQ151 | 石子合并 | 282 | 练习 | 区间DP ★ |
| 7 | NQ152 | 最短编辑距离 | 902 | 练习 | 编辑距离 |
| 8 | NQ153 | 滑雪 | 901 | 练习 | 记忆化搜索 ★ |

**代码文件：** `codes/nq146_acw2.cpp` ～ `codes/nq153_acw901.cpp`
