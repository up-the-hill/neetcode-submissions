class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = -1
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            A = heapq.heappop(stones)
            B = heapq.heappop(stones)
            result = B - A
            if result == 0:
                continue
            else:
                heapq.heappush(stones, -result)
        if stones:
            return -stones[0]
        else:
            return 0
                