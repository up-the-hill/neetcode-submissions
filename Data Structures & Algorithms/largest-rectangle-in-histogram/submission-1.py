class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        res = 0
        for i, h in enumerate(heights):
            lookback = i
            while s and h < s[-1][1]:
                area = (i - s[-1][0]) * s[-1][1]
                print(area)
                res = max(res, area)
                lookback = s[-1][0]
                s.pop()
            s.append((lookback, h))

        while s:
            area = (len(heights) - s[-1][0]) * s[-1][1]
            print(area)
            res = max(res, area)
            s.pop()

        return res