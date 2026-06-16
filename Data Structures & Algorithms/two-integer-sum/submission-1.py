class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_sum = {}
        for i, num in enumerate(nums):
            if num in required_sum:
                return [required_sum[num], i]
            required_sum[target - num] = i
        