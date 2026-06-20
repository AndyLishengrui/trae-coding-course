# JD025：信鸽传信

> **AcWing 671** | 第2章 · 歧路逢生 | 知识点：条件映射

## 题目描述

宗门各分舵之间用信鸽传信，每个分舵有一个编号（DDD码）。李少白拿到一个编号，需要查出它对应哪个分舵：61=Brasilia，71=Salvador，11=Sao Paulo，21=Rio de Janeiro，31=Belo Horizonte
19=Campinas，其他编号则输出"DDD nao cadastrado"。

## 输入格式

一个整数。

## 输出格式

输出对应分舵名称，或 `DDD nao cadastrado`。

## 样例

输入：

```text
11
```

输出：

```text
Sao Paulo
```

## 解题思路

用 if-elif 链逐一比对，或用字典/映射表查找。
