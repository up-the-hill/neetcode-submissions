# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative bfs
        q = deque([(root, 1)])
        res = 0
        while q:
            node = q.popleft()
            if node[0] == None:
                continue
            res = max(res, node[1])
            q.append((node[0].right, node[1]+ 1))
            q.append((node[0].left, node[1]+ 1))
        return res