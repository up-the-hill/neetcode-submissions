# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative bfs
        q = deque([root])
        while q:
            node = q.popleft()
            if node == None:
                continue
            node.left, node.right = node.right, node.left
            q.append(node.right)
            q.append(node.left)

        return root
