# AcWing 28. 在O(1)时间删除链表结点 — 在 O (1) 时间删除链表结点

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/28/

## 题目描述

给定单向链表的一个节点指针，定义一个函数在 O (1) 时间删除该结点。假设链表一定存在，并且该节点一定不是尾节点。

### 输入格式

输入一个链表和一个要删除的节点。

数据范围：链表长度`[1,500]`

### 输出格式

输出删除节点后的链表。

### 样例

**输入:**
```
1->4->6->8
2
```

**输出:**
```
1->4->8
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
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```
