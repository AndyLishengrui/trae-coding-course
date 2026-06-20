# NQ8-03：用两个栈实现队列

> 题目来源：AcWing 20 | 第8章

---

## 题目描述
请用栈实现一个队列，支持如下四种操作：
push(x) - 将元素 x 插到队尾；
pop() - 将队首的元素弹出，并返回该元素；
peek() - 返回队首元素；
empty() - 返回队列是否为空。

### 输入格式
输入数据保证合法，例如，在队列为空时，不会进行 pop 或者 peek 等操作。
数据范围：每组数据操作命令数量[0, 100]。

### 输出格式
输出每个操作的结果。

### 样例1
**输入：**
```
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();
queue.pop();
queue.empty();

```
**输出：**
```
1
1
false

```

---

## 参考代码

**C++ Code:** 见 `Andy.cpp`
**Python Code:** 见 `Andy.py`

> 原题链接：https://www.acwing.com/problem/content/20/
