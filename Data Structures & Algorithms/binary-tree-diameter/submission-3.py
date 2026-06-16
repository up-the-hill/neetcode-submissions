# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def maxDepth(root) -> int:
            if not root: return 0
            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)
            nonlocal longest
            longest = max(longest, leftDepth + rightDepth)
            return 1 + max(rightDepth, leftDepth)

        maxDepth(root)

        return longest
        