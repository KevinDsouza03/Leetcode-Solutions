# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return

        ans = ListNode(0,head)
        prev  = ans
        
        t = head
        
        while t != None and n > 0:
            t = t.next
            n -= 1
            
        while t != None:
            prev = prev.next
            t = t.next
        
        prev.next = prev.next.next
        
        return ans.next