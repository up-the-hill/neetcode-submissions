# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def depth(r: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not r: return 0

            depthLeft = depth(r.left)
            depthRight = depth(r.right)

            if abs(depthLeft - depthRight) > 1:
                balanced = False

            return 1 + max(depthLeft, depthRight)
        
        depth(root)

        return balanced

        