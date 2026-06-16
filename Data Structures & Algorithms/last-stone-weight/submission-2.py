class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-s)
        heapq.heapify(heap)

        while len(heap) > 1:
            a = -(heapq.heappop(heap))
            b = -(heapq.heappop(heap))
            if a == b: continue
            heapq.heappush(heap, -(a-b))
        
        return -heap[0] if len(heap) > 0 else 0