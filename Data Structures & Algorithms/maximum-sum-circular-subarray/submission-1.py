class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = float('-inf'), float('inf')
        currMaxSum, currMinSum = 0, 0
        for n in nums:
            currMaxSum = max(currMaxSum, 0) + n
            currMinSum = min(currMinSum, 0) + n
            maxSum = max(currMaxSum, maxSum)
            minSum = min(currMinSum, minSum)
        
        total = sum(nums)
        return max(maxSum, total-minSum) if maxSum > 0 else maxSum
        