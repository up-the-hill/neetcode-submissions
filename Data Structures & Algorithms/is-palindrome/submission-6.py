class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isCharOrNumber(c: str) -> bool:
            return (
                ord(c) >= ord("a") and ord(c) <= ord("z") or
                ord(c) >= ord("0") and ord(c) <= ord("9")
            )
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isCharOrNumber(s[l].lower()):
                l += 1
            while l < r and not isCharOrNumber(s[r].lower()):
                r -= 1
            if s[r].lower() == s[l].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
            
