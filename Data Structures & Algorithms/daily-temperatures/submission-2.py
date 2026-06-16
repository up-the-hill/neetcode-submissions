class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t > s[-1][1]:
                res[s[-1][0]] = i - s[-1][0]
                s.pop()
            s.append((i, t))
        return res