# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def maxDepth(root):
            if not root: return 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            nonlocal balanced
            if abs(leftDepth - rightDepth) > 1: balanced = False

            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        
        maxDepth(root)

        return balanced