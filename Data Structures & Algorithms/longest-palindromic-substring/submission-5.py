class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)
        bestL, bestR, best = -1, -1, 0
        for i, c in enumerate(s):
            l1, r1 = expand(s, i, i)
            if i + 1 < len(s):
                l2, r2 = expand(s, i, i+1)
                if r2 - l2 + 2 > best:
                    best = r2 - l2 + 1
                    bestR = r2
                    bestL = l2
            if r1 - l1 + 1 > best:
                best = r1 - l1 + 1
                bestR = r1
                bestL = l1

        return s[bestL:bestR+1]