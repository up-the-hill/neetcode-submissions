class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)

        for k in adj:
            adj[k].sort(reverse=True)
        
        s = ['JFK']
        res = []
        while s:
            curr = s[-1]
            if adj[curr]:
                s.append(adj[curr].pop())
            else:
                res.append(s.pop())
        
        res.reverse()
        return res

