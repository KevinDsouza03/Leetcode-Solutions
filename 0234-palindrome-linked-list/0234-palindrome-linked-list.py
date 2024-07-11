# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head):
        if (head == None or head.next == None): return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        
        
        #fast and slow to reverse the second half of the list
        
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        reversed_middle = self.reverseList(slow)
        
        head_reversed = reversed_middle
        while head_reversed != None:
            if head.val != head_reversed.val:
                return False
            head_reversed = head_reversed.next
            head = head.next
            
        return True
        
        