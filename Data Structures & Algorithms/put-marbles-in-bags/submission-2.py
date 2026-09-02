class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        maxHeap = []
        minHeap = []

        for i in range(1, len(weights)):
            cost = weights[i] + weights[i-1]
            if len(minHeap) < k - 1:
                heapq.heappush(minHeap, cost)
            else:
                heapq.heappushpop(minHeap, cost)
            if len(maxHeap) < k - 1:
                heapq.heappush(maxHeap, -cost)
            else:
                heapq.heappushpop(maxHeap, -cost)
        
        return sum(maxHeap) + sum(minHeap)