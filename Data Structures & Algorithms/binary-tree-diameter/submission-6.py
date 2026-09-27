# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(n):
            nonlocal res
            if not n:
                return 0
            maxDepthLeft = dfs(n.left)
            maxDepthRight = dfs(n.right)
            res = max(res, maxDepthLeft + maxDepthRight)
            return max(maxDepthLeft, maxDepthRight) + 1

        dfs(root)

        return res