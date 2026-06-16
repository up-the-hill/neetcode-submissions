class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return math.sqrt(p[0]**2 + p[1]**2)
        
        heap = []

        for p in points:
            heapq.heappush(heap, (-dist(p), p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [x[1] for x in heap]

        return res
        
