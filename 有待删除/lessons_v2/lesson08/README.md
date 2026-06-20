# 第8课：结构体、指针与STL容器

> **课时：** 2小时 | **题目：** 10题（5例题+5练习） | **阶段：** 编程进阶 | **NQ091-NQ100**

## 一、教学目标

1. 理解 C++ 中 `struct/class`、指针、引用的基本概念
2. **Python 对照：** `dataclass`、对象引用（一切皆对象，无指针）
3. 掌握链表、栈的核心操作（C++ 手写 vs Python `list`/`deque`）
4. 为第12课"基础数据结构"做铺垫

## 二、C++ 指针/引用 vs Python 对象模型

| 概念 | C++ | Python |
|------|-----|--------|
| 结构体 | `struct Node { int val; Node* next; };` | `@dataclass class Node: val: int; next: 'Node'` |
| 指针 | `Node* p = new Node();` | 无指针，变量即引用：`node = Node(5)` |
| 空值 | `NULL` / `nullptr` | `None` |
| 链表节点 | `new` 分配，`delete` 释放 | 自动垃圾回收（GC） |
| 数组链表 | `e[N], ne[N], idx` | `list` 或 `dict` 模拟 |
| 栈 | `stack<int>` 或数组+`tt` | `list.append/pop` |
| 队列 | `queue<int>` 或数组+`hh,tt` | `collections.deque` |

## 三、关键教学案例

### NQ091: 替换空格 — 原地修改 vs 构建新串

```cpp
// C++: string 可变，可以原地修改
string replaceSpaces(string &str) {
    string res;
    for (char c : str) {
        if (c == ' ') res += "%20";
        else res += c;
    }
    return res;
}
```

```python
# Python: str 不可变，构建新字符串
def replace_spaces(s: str) -> str:
    return s.replace(' ', '%20')  # 一行！
```

### NQ094: 反转链表 — 经典面试题

```python
# Python: 不需要指针，对象引用天然是"指针"
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next  # 保存后继
        curr.next = prev  # 反转指向
        prev = curr
        curr = nxt
    return prev
```

**教学点：** C++ 和 Python 的链表代码结构几乎一致。Python 不需要 `->` 和 `new`，代码更干净。但理解"prev/curr/nxt 三个指针接力"是核心。

### NQ095: 合并两个排序链表 — 归并思想的萌芽

递归写法最优雅：
```python
def merge(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val <= l2.val:
        l1.next = merge(l1.next, l2)
        return l1
    else:
        l2.next = merge(l1, l2.next)
        return l2
```

**教学点：** 这是第9课归并排序的前导。理解两个有序链表的合并，就理解了归并排序的核心操作。

## 四、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 核心 |
|---|-----|------|--------|------|------|
| 1 | NQ091 | 替换空格 | 16 | 例题 | 字符串构建 |
| 2 | NQ092 | 从尾到头打印链表 | 17 | 例题 | vector/栈 |
| 3 | NQ093 | 用两个栈实现队列 | 20 | 例题 | 栈模拟队列 |
| 4 | NQ094 | 斐波那契(类) | 21 | 例题 | 类封装 |
| 5 | NQ095 | 反转链表 | 35 | 例题 | 三指针接力 ★ |
| 6 | NQ096 | 合并两个排序链表 | 36 | 练习 | 归并思想 ★ |
| 7 | NQ097 | 三元组排序 | 862 | 练习 | struct+sort |
| 8 | NQ098 | 绝对值 | 810 | 练习 | 函数重载 |
| 9 | NQ099 | 复制数组 | 814 | 练习 | 数组传递 |
| 10 | NQ100 | 数组翻转 | 816 | 练习 | reverse() |

**代码文件：** `codes/nq091_acw16.cpp` ～ `codes/nq100_acw816.cpp`
