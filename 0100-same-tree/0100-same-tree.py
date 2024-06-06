# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base cases:
        if ((p == None and q != None) or (p != None and q == None)):
            return False
        if (p == None and q == None):
            return True
        if (p.val != q.val):
            return False
        if (p.left == None and q.left != None):
            return False
        if (p.right == None and q.right != None):
            return False
        
        if (p.left == None and q.left == None):
            if (p.right == None and q.left == None):
                return True
        #means we have reached a leaf node so we must go back up, another base case.
        
        #now we need to determine where to traverse, essentially DFS.
        #the conditonals above tell us that we have reached a leaf, we want to know if we have to still tr
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))