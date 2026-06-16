class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency list
        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        # run dfs on all courses
        checked = set()

        def dfs(c, checking):
            nonlocal checked
            
            if len(adj[c]) == 0 or c in checked:
                return True

            if c in checking:
                return False
            
            checking.add(c)
            for prereq in adj[c]:
                if dfs(prereq, checking) == False:
                    return False
            
            checking.remove(c)
            checked.add(c)
            return True


        for i in range(0, numCourses):
            print(i)
            if dfs(i, set()) == False: return False
        
        return True


