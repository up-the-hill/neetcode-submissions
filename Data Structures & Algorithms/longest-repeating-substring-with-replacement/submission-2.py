class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # get replacements needed by len(window) - maxf
        counts = {}
        maxf = 0
        res = 0
        l, r = 0, 0
        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(maxf, counts[s[r]])
            # if too many replacements needed, remove from l
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


            
