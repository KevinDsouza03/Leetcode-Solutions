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
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return false;
        ListNode* slower = head->next;
        ListNode* faster = head->next->next;
        while (slower != faster && slower != nullptr && faster != nullptr && faster->next != nullptr && faster->next->next != nullptr) {
            slower = slower->next;
            faster = faster->next->next;
        }
        if (slower == faster) return true;
        return false;
    }
};