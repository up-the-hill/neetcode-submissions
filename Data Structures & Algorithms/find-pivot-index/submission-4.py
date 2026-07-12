class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sr = sum(nums[1:])
        sl = 0 
        for i in range(len(nums)):
            print(sl, sr)
            if sl == sr:
                return i
            sl += nums[i]
            if i+1 < len(nums):
                sr -= nums[i+1]
        return -1

            