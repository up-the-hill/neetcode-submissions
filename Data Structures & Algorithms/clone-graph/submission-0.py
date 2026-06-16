"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hm = {}

        def clone(n):
            nonlocal hm

            if n in hm:
                return hm[n]

            new = Node(n.val)
            hm[n] = new

            for nei in n.neighbors:
                new.neighbors.append(clone(nei))

            return new

        return clone(node)

        