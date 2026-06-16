# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] 
        q = deque()

        q.append(root)

        while q:
            cur_layer = []
            for _ in range(len(q)):
                n = q.popleft()

                if n == None: continue

                cur_layer.append(n.val)
                
                q.append(n.left)
                q.append(n.right)

            if cur_layer != []:
                res.append(cur_layer)

        return res
        
        