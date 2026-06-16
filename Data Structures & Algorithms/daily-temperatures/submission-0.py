class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack of indexes
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            # before adding, remove all lesser to the left
            while stack and temperatures[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

