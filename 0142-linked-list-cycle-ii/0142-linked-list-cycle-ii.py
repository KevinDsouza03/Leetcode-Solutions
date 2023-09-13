# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None ):
            return None
        visited = {}
        node = head
        pos = 0
        while (node.next != None):
            if (visited.get(node) != None):
                return node
            else:
                visited.update({node : pos})
                pos += 1
                node = node.next
        return None
        
        