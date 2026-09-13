class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ptc = sorted(zip(capital, profits))

        h, idx = [], 0

        for _ in range(k):
            while idx < len(ptc) and ptc[idx][0] <= w:
                heapq.heappush(h, -ptc[idx][1])
                idx += 1
            
            if not h:
                break
            
            profit = -heapq.heappop(h)
            w += profit

        return w
