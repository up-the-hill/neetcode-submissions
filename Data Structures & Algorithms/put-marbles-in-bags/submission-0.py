class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # build heap of split sums
        minh = []
        maxh = []
        for i in range(len(weights) - 1):
            w = weights[i] + weights[i+1]
            heapq.heappush(minh, w)
            heapq.heappush(maxh, -w)

        maxS = 0
        minS = 0
        for i in range(k - 1):
            minS += heapq.heappop(minh)
            maxS -= heapq.heappop(maxh)

        return maxS - minS


            
