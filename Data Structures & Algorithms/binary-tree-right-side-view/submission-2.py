# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        if not root: return levels

        q = collections.deque()
        q.append(root)

        while q:
            levels.append([])
            for _ in range(len(q)):
                n = q.popleft()
                levels[-1].append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
        
        res = []

        for l in levels:
            res.append(l[-1])

        return res



