class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency list
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        # run djikstras
        minHeap = [(0, k)]
        seen = set()
        res = float("-inf")
        while minHeap:
            cur = heapq.heappop(minHeap)
            if cur[1] in seen: continue
            seen.add(cur[1])
            res = max(res, cur[0])

            for adjacent in adj[cur[1]]:
                if adjacent[0] not in seen:
                    heapq.heappush(minHeap, (cur[0] + adjacent[1], adjacent[0]))
            
        return res if n == len(seen) else -1