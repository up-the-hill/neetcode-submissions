# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def depth(r):
            if not r:
                return 0
            depthLeft = depth(r.left)
            depthRight = depth(r.right) 
            nonlocal dia
            dia = max(dia, depthLeft + depthRight)
            return 1 + max(depthLeft, depthRight)
        
        depth(root)

        return dia
        