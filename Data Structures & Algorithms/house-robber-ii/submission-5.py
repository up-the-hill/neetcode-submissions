class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(houses):
            a = 0
            b = 0

            for i in range(len(houses)):
                c = max(a + houses[i], b)
                a = b
                b = c
            return b
        
        return max(dp(nums[:-1]), dp(nums[1:]), nums[0])