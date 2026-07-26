class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        resL, resR = 0, 0
        for i in range(len(t)):
            l, r = i, i
            while l >= 0 and r < len(t) and t[l] == t[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r - l > resR - resL:
                resL, resR = l, r
            
        return t[resL:resR + 1].replace('#', '')