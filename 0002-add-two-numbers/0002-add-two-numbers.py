# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        
        
        carryStack = []
        while l1 != None or l2 != None:
            if (l1 == None or l2 == None):
                break
            try: 
                add = l1.val + l2.val + carryStack.pop()
            except:
                add = l1.val + l2.val
            if (add > 9):
                remainder = 1
                carryStack.append(remainder)
                add = add % 10
            print(add)
            print(carryStack)
            l1 = l1.next
            l2 = l2.next
            head.next = ListNode(add,next=None)
            head = head.next
        #accomdate for bigger vals.
        notEmpty = None
        if l1 == None:
            nonEmpty = l2
        elif l2 == None:
            nonEmpty = l1
        
        while nonEmpty != None:
            if nonEmpty == None:
                break
            try: 
                add = nonEmpty.val + carryStack.pop()
            except:
                add = nonEmpty.val
            if (add > 9):
                remainder = 1
                carryStack.append(remainder)
                add = add % 10
            nonEmpty = nonEmpty.next
            head.next = ListNode(add,next=None)
            head = head.next
        try:
            head.next = ListNode(carryStack.pop(),next=None)
        except:
            pass
        return ans.next