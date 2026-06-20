# AcWing 20. 用两个栈实现队列 — 用两个栈实现队列

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/20/

## 题目描述

请用栈实现一个队列，支持如下四种操作：
push(x) - 将元素 x 插到队尾；
pop() - 将队首的元素弹出，并返回该元素；
peek() - 返回队首元素；
empty() - 返回队列是否为空。

### 输入格式

输入数据保证合法，例如，在队列为空时，不会进行 pop 或者 peek 等操作。

数据范围：每组数据操作命令数量`[0, 100]`。

### 输出格式

输出每个操作的结果。

### 样例

**输入:**
```
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();
queue.pop();
queue.empty();
```

**输出:**
```
1
1
false
```

### 提示

注意：

你只能使用栈的标准操作：`push to top`，`peek/pop from top`,`size`和`is empty`；如果你选择的编程语言没有栈的标准库，你可以使用list或者deque等模拟栈的操作；输入数据保证合法，例如，在队列为空时，不会进行`pop`或者`peek`等操作；

## AC代码

```cpp
class MyQueue {
public:
    stack<int> stk, cache;
    /** Initialize your data structure here. */
    MyQueue() {

    }

    /** Push element x to the back of queue. */
    void push(int x) {
        stk.push(x);

    }
    void copy(stack<int>& a, stack<int>& b){
        while (a.size()) {
            b.push(a.top());
            a.pop();
        }
    }
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        copy(stk,cache);//拷贝到cache数组
        int res = cache.top();
        cache.pop();
        copy(cache,stk);
        return res;
    }

    /** Get the front element. */
    int peek() {
        copy(stk,cache);//拷贝到cache数组
        int res = cache.top();
        copy(cache,stk);
        return res;
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return stk.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */
```
