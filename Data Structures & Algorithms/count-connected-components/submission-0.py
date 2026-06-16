class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)

        seen = set()
        def dfs(node, prev):
            nonlocal seen
            if node in seen: return 0
            seen.add(node)
            for nei in adj[node]:
                if nei == prev: continue
                dfs(nei, node)
            return 1

        res = 0
        for i in range(n):
            res += dfs(i, -1)
        return res

