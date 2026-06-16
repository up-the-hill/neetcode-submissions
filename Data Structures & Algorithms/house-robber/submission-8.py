class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0

        for i in range(len(nums)):
            temp = max(b, a + nums[i])
            a = b
            b = temp
        
        return max(a, b)
        