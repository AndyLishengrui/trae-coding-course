# NQ6-06：字符串插入

> 题目来源：AcWing 773 | 第6章

---

## 题目描述
有两个不包含空白字符的字符串 str 和 substr，str 的字符个数不超过 10，substr 的字符个数为 3。
将 substr 插入到 str 中 ASCII 码最大的那个字符后面，若有多个最大则只考虑第一个。

### 输入格式
输入包括若干行，每一行为一组测试数据，格式为 str substr。

### 输出格式
对于每一组测试数据，输出插入之后的字符串。

### 样例1
**输入：**
```
abcab eee
12343 555

```
**输出：**
```
abceeeab
12345553

```

---

## 参考代码

**C++ Code:** 见 `Andy.cpp`
**Python Code:** 见 `Andy.py`

> 原题链接：https://www.acwing.com/problem/content/773/
