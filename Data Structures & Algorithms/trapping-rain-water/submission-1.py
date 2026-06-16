class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        # get array of max height to left and right
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        # loop over each value in heightmap
        for i, n in enumerate(height):
            # calculate the amount of water at that position with min(maxLeft, maxRight) - currHeight
            water_at_pos = min(max_left[i], max_right[i]) - height[i]
            total += 0 if water_at_pos < 0 else water_at_pos
            print(water_at_pos)
        # return total
        return total
        