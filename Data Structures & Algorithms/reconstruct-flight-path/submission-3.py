class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)  # directional: u -> v

        for k in adj:
            adj[k].sort(reverse=True)

        res = []
        stack = ["JFK"]

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())

        return res[::-1]
