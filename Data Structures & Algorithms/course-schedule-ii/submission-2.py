class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        # build adjacency list
        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        # run dfs
        visited = set()
        def dfs(c, visiting):
            nonlocal visited
            nonlocal res

            if c in visited:
                return True
                
            if c in visiting:
                return False
                
            visiting.add(c)
            for n in adj[c]:
                if dfs(n, visiting) == False: return False
            visiting.remove(c)
            
            visited.add(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if dfs(i, set()) == False: return []
        
        return res