class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-g for g in gifts]
        heapq.heapify(h)
        
        for i in range(k):
            v = -heapq.heappop(h)
            root = floor(sqrt(v))
            heapq.heappush(h, -root)

        return -sum(h)
