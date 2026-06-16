# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def dfs(node, m):
            if not node: return 0
            if node.val >= m: return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else: return 0 + dfs(node.left, m) + dfs(node.right, m)
        
        return dfs(root, root.val)
