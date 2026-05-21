# AcWing 66. 两个链表的第一个公共结点 — 两个链表的第一个公共结点

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/66/

## 题目描述

输入两个链表，找出它们的第一个公共结点。当不存在公共节点时，返回空节点。

### 输入格式

输入两个链表。

数据范围：链表长度 `[1, 2000]`。保证两个链表不完全相同，即两链表的头结点不相同。

### 输出格式

输出第一个公共节点。

### 样例

**输入:**
```
a1->a2->c1->c2->c3
b1->b2->b3->c1->c2->c3
```

**输出:**
```
c1
```

### 提示

注意输出格式。

## AC代码

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *findFirstCommonNode(ListNode *headA, ListNode *headB) {
        auto p = headA, q = headB;

        while (p != q)
        {
          if (p) p = p->next;
          else p = headB;
          if (q) q = q->next;
          else q = headA;
        }

        return p;
    }
};
```
