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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        //edge cases, where one of the lists is empty
        if (list1 == nullptr && list2 == nullptr){
            return NULL;}
        if (list1 == nullptr){
            return list2;}
        if (list2 == nullptr){
            return list1;}
        ListNode* original = new ListNode(); //original node to store head.
        ListNode* curr = original; // curr to traverse lists
        while (list1 != NULL && list2 != NULL) {
            if (list1->val >= list2->val){// running through example, list.1 = list2.1, so next = list2.1. so now curr = 1->1, list2 is now 3->4.
                curr->next = list2;
                list2 = list2->next;
            }
            else{ // more example, gets ran next. so 1->1->
                curr->next = list1;
                list1 = list1->next;}
            curr = curr->next; //increment for next iteration. 
        }
        
        if (list1 == NULL) {
            curr->next = list2;
        }
        else {
            curr->next = list1;
        }
        
        return original->next;
            
            
            
    }
            
                
            
};