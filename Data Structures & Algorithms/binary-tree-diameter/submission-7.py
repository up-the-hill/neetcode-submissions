# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if not n:
                return (0, 0)
            maxDepthLeft, dl = dfs(n.left)
            maxDepthRight, dr = dfs(n.right)

            curMaxDia = max(dl, dr, maxDepthLeft + maxDepthRight)
            curMaxDepth = max(maxDepthLeft, maxDepthRight) + 1

            return (curMaxDepth, curMaxDia)

        _, res = dfs(root)

        return res