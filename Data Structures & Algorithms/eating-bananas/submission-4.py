class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            m = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)
            # successfully eaten! try to go even more slow
            if time <= h:
                best = m
                r = m - 1
            # uh-oh! caught! try to hurry up
            if time > h:
                l = m + 1
            
        return best

