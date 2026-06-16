class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_n = -1001
        while l <= r:
            m = l + (r - l) // 2
            # if in left section (higher number section)
            if nums[m] > nums[-1]:
                l = m + 1
            # else, means we are in the proper section (lower section)
            else:
                min_n = nums[m]
                r = m - 1
        return min_n

