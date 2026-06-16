class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        for n in range(2, len(nums)):
            res[n] = max(res[n-2] + nums[n], res[n-1])
        
        return res[-1]

        