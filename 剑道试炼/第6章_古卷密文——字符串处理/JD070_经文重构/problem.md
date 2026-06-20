# JD070：经文重构

> **AcWing 764** | 第6章 · 古卷密文 | 知识点：字符串、构造

## 题目描述

赵晴儿递给李少白一段经文a，让他按规则重新构造一段经文b：每个位置b[i]的ASCII值等于a[i]和a[i+1]的ASCII值之和。

## 输入格式

一行字符串a（长度3~100）。

## 输出格式

构造后的字符串b。

## 样例

输入：

```text
=-9+=.3'<<-!!'+5.</=+/3672?96,7'<%5 //>$#:)6*(6.(;7>*)>35#5.72#/44;/)0#864"!51$1=00*:$&'
```

输出：

```text
jfdhkaZcxiNBHR`cjklhZbimiqxobc^caZUO^mbG]c_`R^dVcruhSgqhXXceiURchojXYS[njVCVfUUnm`Zd^JMd
```

## 解题思路

遍历a，b[i] = chr(ord(a[i]) + ord(a[i+1]))。最后一个用a[-1]和a[0]。
