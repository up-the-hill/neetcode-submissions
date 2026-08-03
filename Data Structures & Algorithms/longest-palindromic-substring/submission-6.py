class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        l, r = 0, 0
        for i in range(n):
            if i < r:
                p[i] = min(r - i, l + (r - i))
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
        
        resLen, centralIdx = max((v, i) for i, v in enumerate(p))
        startIdx = (centralIdx - resLen) // 2
        return s[startIdx: startIdx + resLen]