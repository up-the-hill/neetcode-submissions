class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        maximum = weights[0] + weights[-1]
        minimum = maximum

        maxHeap = []
        minHeap = []

        for i in range(1, len(weights)):
            cost = weights[i] + weights[i-1]
            heapq.heappush(minHeap, cost)
            heapq.heappush(maxHeap, -cost)
        
        for i in range(k-1):
            minCost = heapq.heappop(minHeap)
            minimum += minCost
            maxCost = heapq.heappop(maxHeap)
            maximum -= maxCost
        
        return maximum - minimum

