/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *middle = head;
        ListNode *end = head;
        while (end->next != nullptr) {
            middle = middle->next;
            if (end->next->next == nullptr) {
                return middle;
            }
            end = end->next->next;
        }
        return middle;
    }
};