class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algorithm, greedy, spanning tree
        
        # distance helper function
        def d(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # create adjacency list
        adj = defaultdict(list)
        for p in points:
            for q in points:
                if q==p: 
                    continue
                adj[tuple(p)].append((d(p,q), tuple(q)))
        
        # start prim's algorithm on arbitrary point 
        minheap = [(0, tuple(points[0]))]
        res = 0
        seen = set()
        while len(seen) < len(points):
            d, p = heapq.heappop(minheap)
            print(d, p)
            if p in seen: 
                continue
            res += d
            seen.add(p)
            for n in adj[p]:
                if n[1] in seen: continue
                heapq.heappush(minheap, n)
        return res


