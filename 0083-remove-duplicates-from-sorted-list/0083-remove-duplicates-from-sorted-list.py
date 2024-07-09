# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        
        tbl = {}
        cur = head

        while cur is not None:
            if tbl.get(cur.val, None) == None:
                tbl.update({cur.val: 1})
                prev = cur
                cur = cur.next
            else: #does not equal none so already exists
                prev.next = cur.next
                cur = cur.next
        
        return head
                
        