class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        m = [0] * len(nums)
        m[0] = nums[0]
        m[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            m[i] = max(nums[i] + m[i-2], m[i-1])
        return m[-1]
            
