# 第6课：字符串处理

> **课时：** 2小时 | **题目：** 12题（7例题+5练习） | **阶段：** 编程进阶 | **NQ067-NQ078**

## 一、教学目标

1. 掌握字符串基本操作：长度、查找、比较、替换、插入、分割
2. **关键认知：** Python 字符串不可变（immutable），每次修改创建新对象
3. 学会 `join()` vs `+=` 的性能差异（循环中可达100倍差距）
4. 引入 `collections.Counter` 做字符频率统计

## 二、C++ string vs Python str

| 操作 | C++ `string` | Python `str` |
|------|-------------|-------------|
| 长度 | `s.length()` / `s.size()` | `len(s)` |
| 查找 | `s.find("x")` | `s.find("x")` / `s.index("x")` |
| 替换 | `s.replace(pos, len, "new")` | `s.replace("old", "new")` |
| 子串 | `s.substr(i, len)` | `s[i:i+len]` |
| 拼接列表 | 循环 `+=` | `' '.join(words)` 高效 |
| 分割 | 手动 / `stringstream` | `s.split()` |
| 字符判断 | `isdigit(c)` | `c.isdigit()` |
| 遍历字符 | `for(char c : s)` | `for c in s:` |
| 不可变性 | 可变 | **不可变（修改=创建新对象）** |

## 三、关键教学案例

### NQ070: 字符串加空格 — join 的高效用法

```python
# 低效：字符串不可变，每次 += 都创建新对象（O(n²)）
result = ""
for c in s:
    result += c + " "

# 高效：join 一次性构建（O(n)）
result = ' '.join(s)
```

**教学点：** Python 中循环 `+=` 拼串是常见性能陷阱。`''.join()` 只分配一次内存。让 Trae 解释为什么。

### NQ073: 只出现一次的字符

```python
from collections import Counter
cnt = Counter(s)
for c in s:
    if cnt[c] == 1:
        print(c)
        break
else:
    print("no")  # for-else：循环未被break时执行
```

**C++ 对照：** `map<char,int>` 手动计数，代码量约3倍。

### NQ075: 信息加密 — 字符循环偏移

```python
for c in s:
    if 'a' <= c <= 'z':
        c = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        c = chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
```

**教学点：** `% 26` 处理循环（z→a），Python的链式比较 `'a' <= c <= 'z'` 更简洁。

## 四、题目列表

| # | NQ# | 题目 | AcWing | 类型 | 核心 |
|---|-----|------|--------|------|------|
| 1 | NQ067 | 字符串长度 | 760 | 例题 | len() |
| 2 | NQ068 | 字符串中数字个数 | 761 | 例题 | isdigit() |
| 3 | NQ069 | 循环相克令 | 763 | 例题 | dict映射 |
| 4 | NQ070 | 字符串加空格 | 765 | 例题 | join() ★ |
| 5 | NQ071 | 替换字符 | 769 | 例题 | replace() |
| 6 | NQ072 | 字符串插入 | 773 | 例题 | 切片插入 |
| 7 | NQ073 | 只出现一次字符 | 772 | 例题 | Counter ★ |
| 8 | NQ074 | 字符串匹配 | 762 | 练习 | 暴力匹配 |
| 9 | NQ075 | 信息加密 | 767 | 练习 | ord/chr ★ |
| 10 | NQ076 | 输出字符串 | 764 | 练习 | 相邻字符 |
| 11 | NQ077 | 单词替换 | 770 | 练习 | split/join |
| 12 | NQ078 | 最长单词 | 774 | 练习 | split遍历 |

**代码文件：** `codes/nq067_acw760.cpp` ～ `codes/nq078_acw774.cpp`，Python同理
