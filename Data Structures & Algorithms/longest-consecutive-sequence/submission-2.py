class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s:
            l = 1
            if n - 1 in s:
                continue
            while n + 1 in s:
                l += 1
                n = n + 1
            longest = max(longest, l)
        return longest
                
