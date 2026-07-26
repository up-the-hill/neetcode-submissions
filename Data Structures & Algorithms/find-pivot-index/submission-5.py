class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sl, sr = 0, sum(nums)
        for i in range(len(nums)):
            if i - 1 >= 0:
                sl += nums[i - 1]
            sr -= nums[i]
            if sl == sr:
                return i
        return -1

            