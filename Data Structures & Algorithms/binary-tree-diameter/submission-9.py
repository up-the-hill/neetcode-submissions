# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        s = [root]
        mp = {None:(0,0)}
        while s:
            n = s[-1]
            if n.left not in mp:
                s.append(n.left)
            elif n.right not in mp:
                s.append(n.right)
            else:
                n = s.pop()
                lDep, lDia = mp[n.left]
                rDep, rDia = mp[n.right]
                mp[n] = (max(lDep, rDep)+1, max(lDia, rDia, lDep+rDep))
            
        return mp[root][1]

