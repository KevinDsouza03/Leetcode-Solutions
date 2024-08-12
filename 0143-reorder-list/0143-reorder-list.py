# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # how to get our offset?
        
        fast = head
        slow = head
        
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next != None:
            fast = fast.next
        
        end = fast
        
        middle = slow
        
        a = head
        while end != middle:
            prevEnd = middle
            while prevEnd.next != end:
                prevEnd = prevEnd.next
            prevEnd.next = None
            temp = a.next
            a.next = end
            end.next = temp
            end = prevEnd
            a = a.next.next
            
            