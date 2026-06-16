class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26
        for c in s1:
            s1_counts[ord(c) - ord("a")] += 1
        counts = [0] * 26
        l, r = 0, 0
        while r < len(s2):
            counts[ord(s2[r]) - ord("a")] += 1
            if r - l + 1 == len(s1):
                if counts == s1_counts: return True
                r += 1

                counts[ord(s2[l]) - ord("a")] -= 1
                l += 1
            else: 
                r += 1
        return False
            


        