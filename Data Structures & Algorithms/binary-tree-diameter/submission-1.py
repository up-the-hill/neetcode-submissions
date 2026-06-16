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

            if n == None:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)

            res = max(res, l + r)

            return max(l, r) + 1
        
        dfs(root)

        return res
