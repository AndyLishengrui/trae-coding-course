# AcWing 35. 反转链表 — 反转链表

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/35/

## 题目描述

定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

### 输入格式

输入一个链表的头结点。

数据范围：链表长度`[0, 30]`。

### 输出格式

输出反转后的链表的头结点。

### 样例1

**输入:**
```
1->2->3->4->5->NULL
```

**输出:**
```
5->4->3->2->1->NULL
```

### 样例2

**输入:**
```
10->74->87->19->NULL
```

**输出:**
```
19->87->74->10->NULL
```

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
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        auto p = head, q = p->next;
        while (q)
        {
          auto o = q->next;
          q->next = p;
          p = q, q = o;
        }
        head->next = NULL;

        return p;
    }
};
```
