# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative dfs
        s = [(root, 1)]
        res = 0
        while s:
            node = s.pop()
            if node[0] == None:
                continue
            res = max(res, node[1])
            s.append((node[0].right, node[1]+ 1))
            s.append((node[0].left, node[1]+ 1))
        return res