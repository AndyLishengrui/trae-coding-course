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

    vector<int> printListReversingly(ListNode* head) {
        vector<int> res;
        if (!head) return res;
        auto p = head;
        while(p) {
            res.push_back(p->val);
            p=p->next;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
