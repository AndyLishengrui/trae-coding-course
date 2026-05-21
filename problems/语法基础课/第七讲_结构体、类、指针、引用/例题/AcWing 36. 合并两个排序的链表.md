# AcWing 36. 合并两个排序的链表 — 合并两个排序的链表

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/36/

## 题目描述

输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。

### 输入格式

输入两个链表。

数据范围：链表长度`[0, 500]`

### 输出格式

输出合并后的链表。

### 样例

**输入:**
```
1->3->5
2->4->5
```

**输出:**
```
1->2->3->4->5->5
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
    ListNode* merge(ListNode* l1, ListNode* l2) {
        auto dummy = new ListNode(-1), tail = dummy;
        while (l1 && l2)
            if (l1->val < l2->val)
            {
              tail = tail->next = l1;
              l1 = l1->next;
            }
            else
            {
              tail = tail->next = l2;
              l2 = l2->next;
            }

        if (l1) tail->next = l1;
        if (l2) tail->next = l2;

        return dummy->next;  
    }
};
```
