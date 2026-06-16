class Solution:
    def trap(self, height: List[int]) -> int:
        maxBefore = [0] * len(height)
        maxAfter = [0] * len(height)
        for i in range(1, len(height)):
            maxBefore[i] = max(height[i-1], maxBefore[i-1])
        for i in range(len(height)-2, -1, -1):
            maxAfter[i] = max(height[i+1], maxAfter[i+1])
        res = 0
        for i in range(len(height)):
            water = min(maxBefore[i], maxAfter[i]) - height[i]
            res += water if water > 0 else 0
        return res
        