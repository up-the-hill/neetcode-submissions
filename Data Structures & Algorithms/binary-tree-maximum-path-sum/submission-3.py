# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(n):
            nonlocal res
            if not n: return 0
            l = dfs(n.left)
            r = dfs(n.right)
            max_so_far = max(n.val, n.val + l, n.val + r, n.val + l + r)
            res = max(max_so_far, res)       
            return max(n.val, n.val + l, n.val + r)
        dfs(root)
        return res