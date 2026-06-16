class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = {}
        res = 0
        # character replacement count = len(window) - mostCommonCharCount

        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)


            while (r - l + 1 - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
            r += 1
        
        return res