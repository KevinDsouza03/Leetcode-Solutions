# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postorder(root: Optional[TreeNode]):
            # base case
            if root == None:
                return

            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
        postorder(root)
        return ans

        