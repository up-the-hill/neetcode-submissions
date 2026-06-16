class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] # monotonically increasing stack. (index, height)
        res = 0
        for i, h in enumerate(heights):
            back = i
            while s and h < s[-1][1]:
                x = s.pop()
                back = x[0]
                area = x[1] * (i - x[0]) # height * width
                res = max(res, area)
            s.append((back, h))
        
        # flush stack
        while s:
            x = s.pop()
            area = x[1] * (len(heights) - x[0]) # height * width
            res = max(res, area)

        return res