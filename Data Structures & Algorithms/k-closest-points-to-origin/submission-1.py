class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def d(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        heap = []
        for p in points:
            heap.append((-d(p, [0, 0]), p))
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [x[1] for x in heap]
