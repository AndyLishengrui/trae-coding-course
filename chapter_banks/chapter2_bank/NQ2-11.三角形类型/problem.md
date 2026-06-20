# NQ2-11：三角形类型

> 题目来源：AcWing 666 | 第2章

---

## 题目描述
给定三个浮点数，先判断能否构成三角形，如果能，再进一步判断是直角三角形、钝角三角形、锐角三角形、等边三角形还是等腰三角形。

### 输入格式
一行，三个浮点数A、B、C。

### 输出格式
按顺序输出满足的类型，可能多行。先输出"NAO FORMA TRIANGULO"（不能构成），否则依次检查直/钝/锐/等边/等腰。

### 样例1
**输入：**
```
7.0 5.0 7.0
```
**输出：**
```
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES
```

---

## 参考代码

**C++ Code:** 见 `Andy.cpp`
**Python Code:** 见 `Andy.py`

> 原题链接：https://www.acwing.com/problem/content/666/
