class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP algorithm
        # 1: build LPS
        lps = [0] * len(needle)
        p, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[p]:
                lps[i] = p + 1
                i += 1
                p += 1
            elif p != 0:
                p = lps[p - 1]
            else:
                lps[i] = 0
                i += 1
        
        # 2: compare
        i, j = 0, 0
        while j < len(haystack):
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]
            
            if i == len(needle):
                return j - i
                
        return -1
                
        