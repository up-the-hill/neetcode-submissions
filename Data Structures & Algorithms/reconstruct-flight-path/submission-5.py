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
            if not adj[curr]:
                res.append(s.pop())
            else:
                n = adj[curr].pop()
                s.append(n)

        return res[::-1]