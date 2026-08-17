# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(n, highest):
            res = 0
            if not n:
                return 0
            if n.val >= highest:
                res += 1
                highest = n.val
            return res + dfs(n.left, highest) + dfs(n.right, highest)
        
        return dfs(root, root.val)