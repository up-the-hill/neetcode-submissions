class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for n in nums:
            currSum = max(currSum, 0) + n
            maxSum = max(currSum, maxSum)
        return maxSum