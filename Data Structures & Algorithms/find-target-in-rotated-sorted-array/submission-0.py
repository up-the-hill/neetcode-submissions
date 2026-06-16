class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = l + 1
                else:
                    r = r - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = r - 1
                else:
                    l = l + 1
        return -1
