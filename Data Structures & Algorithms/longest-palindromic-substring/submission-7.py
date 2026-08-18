class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        dp = [0] * len(t)
        l, r = 0, 0
        for i, c in enumerate(t):
            if i < r:
                dp[i] = min(r-i, dp[l+r-i])
            
            while (
                i + dp[i] + 1 < len(t) and 
                i - dp[i] - 1 >= 0 and
                t[i+dp[i]+1] == t[i-dp[i]-1]
            ):
                dp[i] += 1
                if i + dp[i] > r:
                    l, r = i-dp[i], i+dp[i]
        
        resLen, resMid = max((l, i) for i, l in enumerate(dp))
        start = (resMid - resLen) // 2
        return s[start:start+resLen]

        


