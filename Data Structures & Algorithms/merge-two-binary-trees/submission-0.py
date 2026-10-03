# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
            
        l = root1 if root1 else TreeNode(0)
        r = root2 if root2 else TreeNode(0)

        head = TreeNode(l.val+r.val)

        head.left = self.mergeTrees(l.left,r.left)
        head.right = self.mergeTrees(l.right,r.right)

        return head