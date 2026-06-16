class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNumeric(ch):
            return (ord("a") <= ord(ch.lower()) and ord(ch.lower()) <= ord("z")) or (ord("0") <= ord(ch) and ord(ch) <= ord("9"))

        a, b = 0, len(s) - 1
        while a < b:
            while a < b and not isAlphaNumeric(s[a]):
                a += 1
            while a < b and not isAlphaNumeric(s[b]):
                b -= 1
            if s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1

        return True
