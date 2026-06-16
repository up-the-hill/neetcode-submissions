class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        for i in range(1, len(nums)):
            pre *= nums[i-1]
            res[i] = pre
        post = 1
        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i+1]
            res[i] *= post
        return res
            