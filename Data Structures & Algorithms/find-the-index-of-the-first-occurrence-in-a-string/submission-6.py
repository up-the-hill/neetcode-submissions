class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP algorithm
        # 1: build a LPS array

        lps = [0] * len(needle)
        prev, i = 0, 1

        while i < len(needle):
            if needle[i] == needle[prev]:
                lps[i] = prev + 1
                i += 1
                prev += 1
            elif prev != 0:
                prev = lps[prev - 1] 
            else:
                lps[i] = 0
                i += 1
        
        # run search
        i, j = 0, 0
        while j < len(haystack):
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            elif i != 0:
                i = lps[i - 1]
            else:
                j += 1

            if i == len(needle):
                return j - i

        
        return -1
        