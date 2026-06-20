# 第7课：函数、递归与库的威力

> **课时：** 2小时 | **题目：** 12题（8例题+4练习） | **阶段：** 编程进阶 | **NQ079-NQ090**

## 一、教学目标

1. 掌握函数的定义、参数传递、返回值的跨语言写法
2. 理解递归的核心结构：基线条件 + 递归条件
3. **库优先第一课：** 学会"先查库，再手写"——全书最重要的工程习惯
4. Python `@lru_cache`、`math.gcd`、`itertools.permutations` 的实战

## 二、"库优先"的震撼案例

| 需求 | C++ 手写 | Python 库 | 行数比 |
|------|---------|----------|--------|
| 最大公约数 | 9行欧几里得递归 | `math.gcd(a,b)` | 9:1 |
| 阶乘 | 6行循环/递归 | `math.factorial(n)` | 6:1 |
| 排列生成 | 15行DFS回溯 | `itertools.permutations(arr)` | 15:1 |
| 组合数 | 手写递推/公式 | `math.comb(n, k)` | 10:1 |
| 记忆化递归 | 手写memo数组 | `@functools.lru_cache` | 5:1 |
| 数组排序 | `sort(begin,end)` | `arr.sort()` | 1:1 |

**核心教学理念：** 先让学生手写理解原理（10分钟），然后展示库方案一行秒杀，建立"手写理解 + 库调用实战"的双轨思维。**会找轮子比会造轮子更重要。**

## 三、关键教学案例

### NQ081: 最大公约数 — 库优先的开端

```python
# 方法1：手写欧几里得（理解原理）
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 方法2：库调用（工程实践）
import math
ans = math.gcd(a, b)  # 一行！

# Python 3.9+ 支持多参数
math.gcd(12, 18, 24)  # → 6
```

### NQ088: 跳台阶 — @lru_cache 记忆化

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # 自动记忆化！
def climb(n):
    if n <= 2:
        return n
    return climb(n-1) + climb(n-2)
```

**教学点：** 不用 `@lru_cache` 时，`climb(50)` 需要计算 2⁵⁰ 次（天文数字）。加了之后只需 O(n)。这就是 DP 的本质——**带记忆的递归**。对比 C++ 手写 memo 数组的写法。

### NQ090: 排列 — itertools 的威力

```python
from itertools import permutations
n = int(input())
for p in permutations(range(1, n+1)):
    print(' '.join(map(str, p)))
```

**C++ 对照：** `next_permutation` 循环 + 需要先排序。

## 四、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 核心 |
|---|-----|------|--------|------|------|
| 1 | NQ079 | n的阶乘 | 804 | 例题 | 递归/库 |
| 2 | NQ080 | x和y的最大值 | 805 | 例题 | 函数定义 |
| 3 | NQ081 | 最大公约数 | 808 | 例题 | math.gcd ★ |
| 4 | NQ082 | 交换数值 | 811 | 例题 | 引用/解包 |
| 5 | NQ083 | 打印数字 | 812 | 例题 | 数组参数 |
| 6 | NQ084 | 打印矩阵 | 813 | 例题 | 二维参数 |
| 7 | NQ085 | 递归求阶乘 | 819 | 例题 | 递归vs库 |
| 8 | NQ086 | 递归求斐波那契 | 820 | 例题 | 双递归+缓存 |
| 9 | NQ087 | 跳台阶 | 821 | 练习 | @lru_cache ★ |
| 10 | NQ088 | 走方格 | 822 | 练习 | math.comb ★ |
| 11 | NQ089 | 排列 | 823 | 练习 | itertools ★ |
| 12 | NQ090 | 数组排序 | 818 | 练习 | sort() |

## 五、AI 协作要点

**"Python 有现成的吗？"** —— 这应该是学生编程时的口头禅。每个需求先问 Trae："Python 标准库里有没有现成的函数可以做 X？"

**代码文件：** `codes/nq079_acw804.cpp` ～ `codes/nq090_acw818.cpp`
