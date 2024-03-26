# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            if (list2 == None):
                return 
            #only list 1 empty:
            else: 
                return list2
        
        temp_arr = []
        while(list1 != None and list2 != None):
            if (list1.val >= list2.val):
                temp_arr.append(list2.val)
                list2 = list2.next
            else: #(list2.val > list1.val)
                temp_arr.append(list1.val)
                list1 = list1.next
        try:
            if (list1.val != None):
                while(list1 != None):
                    temp_arr.append(list1.val)
                    list1 = list1.next
        except:
            pass
        try:
            if (list2.val != None):
                while(list2 != None):
                    temp_arr.append(list2.val)
                    list2 = list2.next
        except:
            pass
        ans = ListNode(temp_arr[0])
        ans_head = ans
        for i in range(1,len(temp_arr),1):
            ans.next = ListNode(temp_arr[i])
            ans = ans.next
        return ans_head
            
                    
                    
                    
        