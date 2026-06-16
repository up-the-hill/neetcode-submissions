class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adjacency list
        adj = defaultdict(list)
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
        
        # dfs
        seen = set()
        def dfs(node, prev):
            nonlocal seen

            if node in seen: return False
            seen.add(node)

            for nei in adj[node]:
                if nei == prev: continue
                if dfs(nei, node) == False: return False
            
            return True
        
        if dfs(0, -1) == False: return False
        return len(seen) == n
            
