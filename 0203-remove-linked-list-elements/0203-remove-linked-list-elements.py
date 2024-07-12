# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #head can be edited so a dummy is good
        dummy = ListNode(0,head)
        
        prev = dummy
        
        while head is not None:
            if head.val == val:
                #remove
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dummy.next
        