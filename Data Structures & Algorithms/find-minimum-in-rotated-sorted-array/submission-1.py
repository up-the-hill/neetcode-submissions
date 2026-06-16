class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[r] > nums[l]:
                return nums[l]
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # means m is in the left half
                l = m + 1
            else: 
                r = r - 1
        return res
            
