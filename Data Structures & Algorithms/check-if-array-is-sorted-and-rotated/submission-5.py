class Solution:
    def check(self, nums: List[int]) -> bool:
        jumps = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                jumps += 1
        return True if jumps <= 1 else False