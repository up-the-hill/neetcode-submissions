class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        adj = defaultdict(list)
        visit = set()

        # make adjacency list 
        for (u, v, w) in times:
            adj[u].append((v, w))

        heap.append((0, k))

        res = 0

        while heap:
            w1, u1 = heapq.heappop(heap)
            if u1 in visit:
                continue
            
            visit.add(u1)
            res = max(res, w1)
            
            for v2, w2 in adj[u1]:
                heapq.heappush(heap, (w2+w1, v2))

        return res if len(visit) == n else -1
            