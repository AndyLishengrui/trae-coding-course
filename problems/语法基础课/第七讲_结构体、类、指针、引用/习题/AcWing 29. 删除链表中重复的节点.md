# AcWing 29. 删除链表中重复的节点 — 删除链表中重复的节点

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/29/

## 题目描述

在一个排序的链表中，存在重复的节点，请删除该链表中重复的节点，重复的节点不保留。

### 输入格式

输入一个排序的链表。

数据范围：链表中节点`val`取值范围`[0, 100]`。链表长度`[0, 100]`。

### 输出格式

输出删除重复节点后的链表。

### 样例1

**输入:**
```
1->2->3->3->4->4->5->NULL
```

**输出:**
```
1->2->5->NULL
```

### 样例2

**输入:**
```
1->1->1->1->2->3->NULL
```

**输出:**
```
2->3->NULL
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
    ListNode* deleteDuplication(ListNode* head) {
        auto dummy = new ListNode(-1);
        dummy->next = head;
        auto p = dummy;

        while (p->next)
        {
          auto q = p->next;
          while (q->next && q->next->val == p->next->val) q = q->next;

          if (q == p->next) p = q;
          else p->next = q->next;
        }

        return dummy->next;
    }
};
```
