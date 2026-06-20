# 第4课：循环的力量

> **课时：** 2小时 | **题目：** 3例题 + 3练习 | **难度：** ⭐⭐

## 一、本课目标
1. 掌握 `for` 和 `while` 两种循环的使用场景
2. 理解 `range()` 的三种用法：`range(n)`, `range(start,end)`, `range(start,end,step)`
3. 学会用嵌套循环解决表格型问题
4. **Python 特色：** `sum()`+生成器表达式、`collections.Counter` 初探

## 二、Python 工具箱

| 工具 | C++ 等价 | 用途 |
|------|---------|------|
| `range(n)` | `for(int i=0;i<n;i++)` | 循环n次 |
| `range(start,end,step)` | `for(int i=s;i<e;i+=s)` | 带步长 |
| `sum(iterable)` | `accumulate` | 求和 |
| `sum(1 for x in arr if cond)` | 循环+计数 | 条件计数 |
| `collections.Counter` | `map<char,int>` | 分类频率统计 |

## 三、例题

| 题号 | 题目 | 核心知识点 |
|------|------|-----------|
| NQ019 | 偶数 | `for` 循环基础，`range(2,101,2)` |
| NQ020 | 奇数 | 步长控制，`range(1,x+1,2)` |
| NQ021 | 乘法表 | 嵌套循环，`print(end=' ')` 控制换行 |

**Python 对比 C++：**
```python
# Python 的 range 比 C++ 的 for 更简洁
for i in range(2, 101, 2):   # Python
for (int i = 2; i <= 100; i += 2)  // C++
```

## 四、练习

| 题号 | 题目 | 核心技能 |
|------|------|---------|
| NQ022 | 正数 | 条件计数：`sum(1 for x in nums if x > 0)` |
| NQ023 | 连续奇数的和 | 累加：`sum(i for i in range(a+1, b) if i%2)` |
| NQ024 | 实验 | `collections.Counter` 分类统计 |

**NQ024 Python 亮点：**
```python
from collections import Counter
cnt = Counter()  # 类似 C++ 的 map<char,int>
for _ in range(n):
    k, t = input().split()
    cnt[t] += int(k)  # Counter 自动处理不存在的key
```

## 五、AI 协作要点

本课第一次引入标准库（`collections.Counter`）。教学重点：遇到统计需求时，先问 Trae "Python 有没有现成的统计工具？" 然后使用 Counter，而不是自己写循环。
